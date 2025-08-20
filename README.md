# HTAN Phase 2 Data Model (HTAN2)

---

## ⚠️ **DO NOT USE – UNDER DEVELOPMENT** ⚠️  

This data model is in **active development**. It builds on **HTAN Phase 1** and incorporates input from the **Cancer Data Standards (CDS)** initiative. Expect frequent changes until a stable version is released.

---

## Overview 

This repository is part of ongoing efforts to refine and standardize the HTAN2 data model. 

## 🏗️ Data Model Architecture

The HTAN2 data model is built using **LinkML**, a modeling language for schemas that generates Python data model classes and JSON schemas. The model follows a modular architecture with clear separation of concerns:

### **Core Module**
- **Purpose**: Universal attributes shared across all file-based modules
- **Location**: `modules/Core/domains/core.yaml`
- **Key Features**: 
  - Primary and foreign key definitions
  - HTAN identifier validation patterns
  - Base class for inheritance (`CoreFileAttributes`)

### **Clinical Module**
- **Purpose**: Clinical and demographic data
- **Location**: `modules/Clinical/`
- **Structure**: Multiple domain files (demographics, diagnosis, therapy, etc.)
- **Features**: Comprehensive validation rules and conditional requirements

### **WES Module**
- **Purpose**: Bulk Whole Exome Sequencing data
- **Location**: `modules/WES/`
- **Structure**: Three processing levels (Level 1, 2, 3)
- **Features**: Sequencing platform enums, quality metrics, variant calling

## 📁 Project Structure

```
htan-linkml/
├── modules/                    # All data model modules
│   ├── Core/                  # Universal attributes
│   ├── Clinical/              # Clinical data domains
│   └── WES/                   # Whole Exome Sequencing
├── config/                    # LinkML configuration
├── scripts/                   # Utility scripts
├── tests/                     # Root-level tests
└── docs/                      # Documentation
```

## 🔧 Development Conventions

### **Enum Organization**
- All enums are **alphabetically ordered** for consistency
- Enum values within each enum are also alphabetically ordered
- This applies to both enum names and their permissible values

### **Schema Structure**
- **Inheritance**: Modules inherit from `CoreFileAttributes` for universal attributes
- **Validation**: Regex patterns for HTAN identifiers
- **Documentation**: Each attribute includes `title` and `description` fields

### **File Naming**
- **Domain files**: `domains/[domain_name].yaml`
- **Test files**: `tests/test_[module_name].py`
- **Generated code**: `src/htan_[module]/datamodel/`

## 🧪 Testing Strategy

### **Module Testing**
- **Schema loading**: Verify YAML files can be parsed
- **Inheritance**: Confirm Core module inheritance works correctly
- **Enums**: Validate enum definitions and values
- **Validation**: Test regex patterns and required fields

### **Test Data**
- **Valid cases**: Sample data that should pass validation
- **Invalid cases**: Sample data that should fail validation
- **Edge cases**: Boundary conditions and special scenarios

## 🚀 Getting Started

### **Prerequisites**
- Python 3.11+
- Poetry (dependency management)
- LinkML tools

### **Installation**
```bash
# Clone the repository
git clone <repository-url>
cd htan-linkml

# Install dependencies
poetry install

# Generate schemas
make modules-gen

# Run tests
make test
```

### **Module Development**
1. **Create module structure**: Follow existing module patterns
2. **Define schemas**: Use LinkML YAML syntax
3. **Add tests**: Include comprehensive test coverage
4. **Update documentation**: Maintain README files

## 📚 Module-Specific Documentation

Each module contains detailed documentation:

- **Core Module**: See `modules/Core/README.md` for primary/foreign key definitions
- **Clinical Module**: See `modules/Clinical/README.md` for domain descriptions
- **WES Module**: See `modules/WES/README.md` for sequencing levels

## 🔗 Key Relationships

### **Data Hierarchy**
```
Participant (HTAN_PARTICIPANT_ID)
├── Biospecimen (HTAN_BIOSPECIMEN_ID)
│   └── Level 1 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _B####
│       └── Level 2 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
│           └── Level 3 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
```

### **Primary Keys**
- `HTAN_PARTICIPANT_ID`: Unique identifier for research participants
- `HTAN_DATA_FILE_ID`: Unique identifier for data files across all levels
- `HTAN_BIOSPECIMEN_ID`: Unique identifier for biospecimens

### **Foreign Keys**
- `HTAN_PARENT_ID`: References parent entity using suffix convention
  - `_B####` - References a biospecimen
  - `_D####` - References a data file

## 🤝 Contributing

### **Development Workflow**
1. Create feature branch: `git checkout -b feat-[module-name]`
2. Make changes following conventions
3. Add/update tests
4. Run test suite: `make test`
5. Update documentation
6. Submit pull request

### **Code Quality**
- **Formatting**: Use `make format` for consistent code style
- **Testing**: Ensure all tests pass before submitting
- **Documentation**: Update README files for any new modules

## 📖 Additional Resources

- **LinkML Documentation**: [https://linkml.io/](https://linkml.io/)
- **HTAN Phase 1 (archived)**: [https://github.com/ncihtan/data-models](https://github.com/ncihtan/data-models)
- **Cancer Data Standards**: [https://cancer.gov/cancer-data-standards](https://cancer.gov/cancer-data-standards)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
