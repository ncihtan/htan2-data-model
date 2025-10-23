#!/usr/bin/env python3
"""
Test to analyze and report on 'none types' across the HTAN2 data model.

This test scans all enum YAML files to count occurrences of values that represent
missing, unknown, not applicable, or not recorded data across the entire data model.
"""

import os
import yaml
import pytest
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple


class NoneTypesAnalyzer:
    """Analyzer for counting 'none types' across the HTAN2 data model."""
    
    # Define patterns that represent "none types" - missing/unknown/not applicable data
    NONE_TYPE_PATTERNS = [
        "not applicable", "not recorded", "unknown", "not available", 
        "not specified", "not provided", "missing", "n/a",
        "not known", "not observed", "not reported", "refused", 
        "unavailable", "not assessed", "cannot be assessed", "not determined",
        "not available", "not captured", "not stored", "not relevant"
    ]
    
    def __init__(self, modules_dir: str = "modules"):
        """Initialize analyzer with modules directory path."""
        self.modules_dir = Path(modules_dir)
        self.none_types_count = defaultdict(int)
        self.enum_files_analyzed = []
        self.total_enums = 0
        self.total_permissible_values = 0
        self.none_values_found = 0
        
    def analyze_enum_file(self, yaml_file: Path) -> Dict[str, int]:
        """Analyze a single enum YAML file for none types."""
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)
            
            none_types_in_file = defaultdict(int)
            
            # Check if file has enums section
            if 'enums' not in data:
                return none_types_in_file
                
            # Analyze each enum in the file
            for enum_name, enum_data in data['enums'].items():
                if 'permissible_values' not in enum_data:
                    continue
                    
                self.total_enums += 1
                
                # Check each permissible value
                for value, value_data in enum_data['permissible_values'].items():
                    self.total_permissible_values += 1
                    
                    # Check if value matches any none type pattern
                    value_lower = value.lower()
                    for pattern in self.NONE_TYPE_PATTERNS:
                        if pattern in value_lower:
                            none_types_in_file[value] += 1
                            self.none_types_count[value] += 1
                            self.none_values_found += 1
                            break
                            
            return none_types_in_file
            
        except Exception as e:
            print(f"Error analyzing {yaml_file}: {e}")
            return {}
    
    def scan_all_modules(self) -> Dict[str, any]:
        """Scan all modules for enum files and analyze none types."""
        results = {
            'modules_analyzed': [],
            'enum_files_analyzed': [],
            'none_types_by_module': defaultdict(dict),
            'summary_stats': {}
        }
        
        # Scan each module directory
        for module_dir in self.modules_dir.iterdir():
            if not module_dir.is_dir():
                continue
                
            module_name = module_dir.name
            results['modules_analyzed'].append(module_name)
            
            # Look for domains directory with YAML files
            domains_dir = module_dir / 'domains'
            if domains_dir.exists():
                yaml_files = list(domains_dir.glob('*.yaml'))
                
                for yaml_file in yaml_files:
                    if 'enum' in yaml_file.name.lower():
                        results['enum_files_analyzed'].append(str(yaml_file))
                        none_types = self.analyze_enum_file(yaml_file)
                        
                        if none_types:
                            results['none_types_by_module'][module_name][yaml_file.name] = none_types
        
        # Calculate summary statistics
        results['summary_stats'] = {
            'total_modules': len(results['modules_analyzed']),
            'total_enum_files': len(results['enum_files_analyzed']),
            'total_enums': self.total_enums,
            'total_permissible_values': self.total_permissible_values,
            'total_none_values': self.none_values_found,
            'none_types_count': dict(self.none_types_count),
            'most_common_none_types': Counter(self.none_types_count).most_common(10)
        }
        
        return results


def test_none_types_analysis():
    """Test to analyze and report none types across the data model."""
    analyzer = NoneTypesAnalyzer()
    results = analyzer.scan_all_modules()
    
    # Print detailed report
    print("\n" + "="*80)
    print("HTAN2 DATA MODEL - NONE TYPES ANALYSIS")
    print("="*80)
    
    # Summary statistics
    stats = results['summary_stats']
    print(f"\n📊 SUMMARY STATISTICS:")
    print(f"   • Total modules analyzed: {stats['total_modules']}")
    print(f"   • Total enum files: {stats['total_enum_files']}")
    print(f"   • Total enums: {stats['total_enums']}")
    print(f"   • Total permissible values: {stats['total_permissible_values']}")
    print(f"   • Total 'none' values found: {stats['total_none_values']}")
    
    # Total none types count at the top
    print(f"\n🔢 TOTAL NONE TYPES ACROSS ALL MODULES: {stats['total_none_values']}")
    print("="*80)
    
    if stats['total_permissible_values'] > 0:
        none_percentage = (stats['total_none_values'] / stats['total_permissible_values']) * 100
        print(f"   • Percentage of 'none' values: {none_percentage:.2f}%")
    
    # Most common none types
    print(f"\n🔍 MOST COMMON 'NONE' TYPES:")
    for none_type, count in stats['most_common_none_types']:
        print(f"   • '{none_type}': {count} occurrences")
    
    # None types by module
    print(f"\n📁 'NONE' TYPES BY MODULE:")
    for module_name, enum_files in results['none_types_by_module'].items():
        if enum_files:
            print(f"\n   📂 {module_name}:")
            for enum_file, none_types in enum_files.items():
                if none_types:
                    print(f"      • {enum_file}: {len(none_types)} none types")
                    for none_type, count in none_types.items():
                        print(f"        - '{none_type}': {count}")
    
    # Detailed breakdown by enum file
    print(f"\n📋 DETAILED BREAKDOWN BY ENUM FILE:")
    for enum_file in results['enum_files_analyzed']:
        print(f"   • {enum_file}")
    
    # Assertions for test validation
    assert stats['total_modules'] > 0, "Should analyze at least one module"
    assert stats['total_enum_files'] > 0, "Should find at least one enum file"
    assert stats['total_enums'] > 0, "Should find at least one enum"
    assert stats['total_permissible_values'] > 0, "Should find at least one permissible value"
    
    # Check that we found some none types (expected in a data model)
    assert stats['total_none_values'] > 0, "Should find at least some 'none' values in the data model"
    
    # Check that the percentage is reasonable (not too high, not too low)
    if stats['total_permissible_values'] > 0:
        none_percentage = (stats['total_none_values'] / stats['total_permissible_values']) * 100
        assert 0.1 <= none_percentage <= 10, f"None types percentage ({none_percentage:.2f}%) should be between 0.1% and 10%"
    
    print(f"\n✅ All assertions passed!")
    print("="*80)
    
    return results


def test_none_types_consistency():
    """Test to check consistency of none types across modules."""
    analyzer = NoneTypesAnalyzer()
    results = analyzer.scan_all_modules()
    
    # Check for consistent none type usage
    none_types_by_module = results['none_types_by_module']
    
    # Find modules that use none types
    modules_with_none_types = [module for module, enums in none_types_by_module.items() if enums]
    
    print(f"\n🔍 CONSISTENCY ANALYSIS:")
    print(f"   • Modules with 'none' types: {len(modules_with_none_types)}")
    print(f"   • Modules: {', '.join(modules_with_none_types)}")
    
    # Check that all major modules have some none types
    expected_modules = ['Clinical', 'Biospecimen', 'WES']
    for module in expected_modules:
        if module in modules_with_none_types:
            print(f"   ✅ {module} module has 'none' types")
        else:
            print(f"   ⚠️  {module} module has no 'none' types")
    
    # Assert that we have none types in at least some modules
    assert len(modules_with_none_types) > 0, "Should have none types in at least one module"


if __name__ == "__main__":
    # Run the analysis
    test_none_types_analysis()
    test_none_types_consistency()
