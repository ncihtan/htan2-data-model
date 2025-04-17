-- # Class: "program" Description: "Program in the Cancer Data Service refer to a broad framework of goals under which related projects or other research activities are grouped. Example - Clinical Proteomic Tumor Analysis Consortium (CPTAC)"
--     * Slot: id Description: 
--     * Slot: program_name Description: The name of the program under which related studies will be grouped, in full text and unabbreviated form, exactly as it will be displayed within the UI.
--     * Slot: program_acronym Description: The name of the program under which related studies will be grouped, expressed in the form of the acronym by which it will identified within the UI. <br>This property is used as the key via which study records can be associated with the appropriate program during data loading, and to identify the correct records during data updates.
--     * Slot: program_short_description Description: An abbreviated, single sentence description of the program.
--     * Slot: program_full_description Description: A more detailed, multiple sentence description of the program.
--     * Slot: program_external_url Description: The external url to which users should be directed in order to learn more about the program.
--     * Slot: program_sort_order Description: An arbitrarily-assigned value used to dictate the order in which programs are displayed within the application's UI.
--     * Slot: program_short_name Description: An acronym or abbreviated form of the title of a broad framework of goals under which related projects or other research activities are grouped. Example - CPTAC
--     * Slot: institution Description: TBD
--     * Slot: study_name Description: Official name of study
--     * Slot: study_acronym Description: Short acronym or other study desginator
--     * Slot: study_description Description: Human-readable study description
--     * Slot: short_description Description: Short description that will identify the dataset on public pages A clear and concise formula for the title would be like: {methodology} of {organism}: {sample info}
--     * Slot: study_external_url Description: Website or other url relevant to study
--     * Slot: primary_investigator_name Description: Name of principal investigator
--     * Slot: primary_investigator_email Description: Email of principal investigator
--     * Slot: co_investigator_name Description: Name of co-principal investigator
--     * Slot: co_investigator_email Description: Email of co-principal investigator
--     * Slot: phs_accession Description: PHS accession number (a.k.a dbGaP accession)
--     * Slot: bioproject_accession Description: NCBI BioProject accession ID
--     * Slot: index_date Description: Index date (Day 0) to which all dates are relative, for this study
--     * Slot: cds_requestor Description: Identifies the user requesting storage in CDS
--     * Slot: funding_agency Description: Funding agency of the requestor study
--     * Slot: funding_source_program_name Description: The funding source organization/sponsor
--     * Slot: grant_id Description: Grant or contract identifier
--     * Slot: clinical_trial_system Description: Organization that provides clinical trial identifier (if study is a clinical trial)
--     * Slot: clinical_trial_identifier Description: Study identifier in the given clinical trial system
--     * Slot: clinical_trial_arm Description: Arm of clinical trial, if appropriate
--     * Slot: organism_species Description: Species binomial of study participants
--     * Slot: adult_or_childhood_study Description: Study participants are adult, pediatric, or other
--     * Slot: data_types Description: Data types for storage
--     * Slot: file_types Description: File types for storage
--     * Slot: data_access_level Description: Is data open, controlled, or mixed?
--     * Slot: cds_primary_bucket Description: The primary bucket for depositing data
--     * Slot: cds_secondary_bucket Description: Secondary bucket for depositing data (non-sequence files)
--     * Slot: cds_tertiary_bucket Description: Secondary bucket for depositing data (non-sequence files)
--     * Slot: number_of_participants Description: How many participants in the study
--     * Slot: number_of_samples Description: How many total samples in the study
--     * Slot: study_data_types Description: Types of scientific data in the study
--     * Slot: file_types_and_format Description: Specific kinds of files in the dataset that will be uploaded to CDS
--     * Slot: size_of_data_being_uploaded Description: Size of the data being uploaded to CDS
--     * Slot: acl Description: open or restricted access to data
--     * Slot: study_access Description: Study access
--     * Slot: authz Description: multifactor authorization
--     * Slot: study_version Description: The version of the phs accession
--     * Slot: role_or_affiliation Description: The text that describes the distinguishable characteristics of the action or activity assigned to or required or expected of a person in a formal association with a group or organization.
--     * Slot: title Description: The abbreviation that represents an affix occurring at or before the beginning of an individual's name.
--     * Slot: first_name Description: A word or group of words indicating a person's first (personal or given) name; the name that precedes the surname. Synonym = Given Name.
--     * Slot: middle_name Description: A means of identifying an individual by using a word or group of words indicating a person's middle name.
--     * Slot: last_name Description: A means of identifying an individual by using a word or group of words indicating a person's last (family) name. Synonym = Last Name, Surname.
--     * Slot: suffix Description: Text term to represent an individual's position in a family lineage or pedigree.
--     * Slot: email Description: The string of characters that represents the electronic mail address of a person.
--     * Slot: clinical_trial_repository Description: The name of the organization that provides the clinical trial identifier.
-- # Class: "study" Description: "The narrative title used as a textual label for a research data collection. Example – University of Texas PDX Development and Trial Center Grant"
--     * Slot: id Description: 
--     * Slot: study_name Description: Official name of study
--     * Slot: study_acronym Description: Short acronym or other study desginator
--     * Slot: study_description Description: Human-readable study description
--     * Slot: short_description Description: Short description that will identify the dataset on public pages A clear and concise formula for the title would be like: {methodology} of {organism}: {sample info}
--     * Slot: study_external_url Description: Website or other url relevant to study
--     * Slot: primary_investigator_name Description: Name of principal investigator
--     * Slot: primary_investigator_email Description: Email of principal investigator
--     * Slot: co_investigator_name Description: Name of co-principal investigator
--     * Slot: co_investigator_email Description: Email of co-principal investigator
--     * Slot: phs_accession Description: PHS accession number (a.k.a dbGaP accession)
--     * Slot: bioproject_accession Description: NCBI BioProject accession ID
--     * Slot: index_date Description: Index date (Day 0) to which all dates are relative, for this study
--     * Slot: cds_requestor Description: Identifies the user requesting storage in CDS
--     * Slot: funding_agency Description: Funding agency of the requestor study
--     * Slot: funding_source_program_name Description: The funding source organization/sponsor
--     * Slot: grant_id Description: Grant or contract identifier
--     * Slot: clinical_trial_system Description: Organization that provides clinical trial identifier (if study is a clinical trial)
--     * Slot: clinical_trial_identifier Description: Study identifier in the given clinical trial system
--     * Slot: clinical_trial_arm Description: Arm of clinical trial, if appropriate
--     * Slot: organism_species Description: Species binomial of study participants
--     * Slot: adult_or_childhood_study Description: Study participants are adult, pediatric, or other
--     * Slot: data_types Description: Data types for storage
--     * Slot: file_types Description: File types for storage
--     * Slot: data_access_level Description: Is data open, controlled, or mixed?
--     * Slot: cds_primary_bucket Description: The primary bucket for depositing data
--     * Slot: cds_secondary_bucket Description: Secondary bucket for depositing data (non-sequence files)
--     * Slot: cds_tertiary_bucket Description: Secondary bucket for depositing data (non-sequence files)
--     * Slot: number_of_participants Description: How many participants in the study
--     * Slot: number_of_samples Description: How many total samples in the study
--     * Slot: study_data_types Description: Types of scientific data in the study
--     * Slot: file_types_and_format Description: Specific kinds of files in the dataset that will be uploaded to CDS
--     * Slot: size_of_data_being_uploaded Description: Size of the data being uploaded to CDS
--     * Slot: acl Description: open or restricted access to data
--     * Slot: study_access Description: Study access
--     * Slot: authz Description: multifactor authorization
--     * Slot: study_version Description: The version of the phs accession
--     * Slot: role_or_affiliation Description: The text that describes the distinguishable characteristics of the action or activity assigned to or required or expected of a person in a formal association with a group or organization.
--     * Slot: title Description: The abbreviation that represents an affix occurring at or before the beginning of an individual's name.
--     * Slot: first_name Description: A word or group of words indicating a person's first (personal or given) name; the name that precedes the surname. Synonym = Given Name.
--     * Slot: middle_name Description: A means of identifying an individual by using a word or group of words indicating a person's middle name.
--     * Slot: last_name Description: A means of identifying an individual by using a word or group of words indicating a person's last (family) name. Synonym = Last Name, Surname.
--     * Slot: suffix Description: Text term to represent an individual's position in a family lineage or pedigree.
--     * Slot: email Description: The string of characters that represents the electronic mail address of a person.
--     * Slot: clinical_trial_repository Description: The name of the organization that provides the clinical trial identifier.
-- # Class: "participant" Description: "Individual who takes part in the study"
--     * Slot: id Description: 
--     * Slot: study_participant_id Description: The property study_participant_id is a compound property, combining the property participant_id and the parent property study.phs_accession. It is the ID property for the node participant. The reason why we are doing that is because is some cases, there are same participant id in different studies repersent different participants.
--     * Slot: participant_id Description: A number or a string that may contain metadata information, for a participant who has taken part in the investigation or study.
--     * Slot: race Description: OMB Race designator
--     * Slot: gender Description: Biological gender at birth
--     * Slot: ethnicity Description: OMB Ethinicity designator
--     * Slot: dbGaP_subject_id Description: Identifier for the participant as assigned by dbGaP
--     * Slot: sex Description: A textual description of a person's sex at birth.
--     * Slot: crdc_id Description: The crdc_id is a unique identifier that is generated by Data Hub
-- # Class: "diagnosis" Description: "Text term used to describe the patient's histologic diagnosis, as described by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O)."
--     * Slot: id Description: 
--     * Slot: study_diagnosis_id Description: The property study_diagnosis_id is a compound property, combining the property diagnosis_id and the parent property participant.study_participant_id. It is the ID property for the node diagnosis.
--     * Slot: diagnosis_id Description: Internal identifier
--     * Slot: disease_type Description: Type of disease [?]
--     * Slot: vital_status Description: Vital status as of last known follow up
--     * Slot: primary_diagnosis Description: Primary disease diagnosed for this diagnosis and subject
--     * Slot: primary_site Description: Anatomical site of disease in primary diagnosis for this diagnosis
--     * Slot: age_at_diagnosis Description: Participant age at relevant diagnosis
--     * Slot: tumor_grade Description: Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.
--     * Slot: tumor_stage_clinical_m Description: Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.
--     * Slot: tumor_stage_clinical_n Description: Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.
--     * Slot: tumor_stage_clinical_t Description: Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.
--     * Slot: morphology Description: ICD-O-3 Morphology term associated with this diagnosis
--     * Slot: incidence_type Description: For this diagnosis, disease incidence relative to prior status of subject
--     * Slot: progression_or_recurrence Description: Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment.
--     * Slot: days_to_recurrence Description: Days to disease recurrence, relative to study index date
--     * Slot: days_to_last_followup Description: Days to last participant followup, relative to study index date
--     * Slot: last_known_disease_status Description: Last known disease incidence for this subject and diagnosis
--     * Slot: days_to_last_known_status Description: Days to last known status of participant, relative to study index date
--     * Slot: tissue_or_organ_of_origin Description: The text term used to describe the anatomic site of origin, of the patient's malignant disease, as described by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
--     * Slot: site_of_resection_or_biopsy Description: The organ or part of the body resected or biopsied, as described by the topography codes of the International Classification of Diseases for Oncology, 3rd Edition (ICD-O-3).
--     * Slot: days_to_last_known_disease_status Description: The number of days from the date of the initial cancer diagnosis to the date of last known disease status.
-- # Class: "treatment" Description: "An action or administration of therapeutic agents to produce an effect that is intended to alter the course of a pathologic process."
--     * Slot: id Description: 
--     * Slot: treatment_id Description: Internal identifier
--     * Slot: treatment_type Description: Text term that describes the kind of treatment administered
--     * Slot: treatment_outcome Description: Text term that describes the patient's final outcome after the treatment was administered
--     * Slot: days_to_treatment Description: Days to start of treatment, relative to index date
--     * Slot: therapeutic_agents Description: Text identification of the individual agent(s) used as part of a treatment regimen.
--     * Slot: response Description: Text term that describes the patient's final outcome after the treatment was administered.
-- # Class: "sample" Description: "Specimen tissue type collected from the participant."
--     * Slot: id Description: 
--     * Slot: sample_id Description: Sample identifier as submitted by requestor
--     * Slot: sample_type Description: Tissue type of this sample
--     * Slot: sample_description Description: Text description of a sample or specimen.
--     * Slot: sample_type_category Description: The kind of material that forms the sample.
--     * Slot: sample_tumor_status Description: Tumor or normal status
--     * Slot: sample_anatomic_site Description: Anatomic site from which sample was collected
--     * Slot: sample_age_at_collection Description: Number of days to collection, relative to index date
--     * Slot: derived_from_specimen Description: Identier of the parent specimen of this sample
--     * Slot: biosample_accession Description: NCBI BioSample accession ID (SAMN) for this sample
-- # Class: "file" Description: "A set of related records kept together provided by a submitter."
--     * Slot: id Description: 
--     * Slot: file_id Description: File identifier
--     * Slot: file_name Description: Name of file
--     * Slot: file_type Description: File type from enumerated list
--     * Slot: file_description Description: Human-readable description of file
--     * Slot: file_size Description: File size in bytes
--     * Slot: md5sum Description: MD5 hex digest for this file
--     * Slot: file_url_in_cds Description: Location of the file on the CDS cloud, using AWS S3 protocol
--     * Slot: experimental_strategy_and_data_subtypes Description: What is the experimental strategy used for the study (or what type of data subtypes exist in the study)?
--     * Slot: submission_version Description: The version of the metadata file submitted to CDS
--     * Slot: checksum_value Description: checksum (hash) for file (using checksum_algorithm) - if you want to use a checksum other than md5
--     * Slot: checksum_algorithm Description: The method by which the file checksum was calculated.
--     * Slot: crdc_id Description: The crdc_id is a unique identifier that is generated by Data Hub
--     * Slot: file_mapping_level Description: Describes if the file belongs to a Participant, a Sample, or a Study
-- # Class: "genomic_info" Description: "In CDS genomic info refers to the sequencing methodsm techniques and equipment."
--     * Slot: id Description: 
--     * Slot: genomic_info_id Description: Genomic info identifier, the ID property for the ndoe genomic_info.
--     * Slot: library_id Description: Library identifier as submitted by requestor
--     * Slot: bases Description: Total number of unique bases read
--     * Slot: number_of_reads Description: Total number of reads performed
--     * Slot: avg_read_length Description: Average sequence read length
--     * Slot: coverage Description: Average depth of coverage on reference used
--     * Slot: reference_genome_assembly Description: Accession or name of genome reference or assembly used for alignment
--     * Slot: custom_assembly_fasta_file_for_alignment Description: File name of any custom assembly fasta file used during alignment
--     * Slot: design_description Description: Human-readable description of methods used to create sequencing library
--     * Slot: library_strategy Description: Nucleic acid capture or processing strategy for this library
--     * Slot: library_layout Description: Library layout as submitted by requestor
--     * Slot: library_source Description: Source material used to create library
--     * Slot: library_selection Description: Library selection method
--     * Slot: platform Description: Instrument platform or manufacturer
--     * Slot: instrument_model Description: Instrument model
--     * Slot: sequence_alignment_software Description: Name of software program used to align nucleotide sequence data
--     * Slot: reporter_label Description: The text term used to describe the labeled methyl group used as a molecular tag.
--     * Slot: methylation_platform Description: The equipment used to detect the presence and/or location of methyl groups during DNA or protein analysis.
--     * Slot: library_source_material Description: Source Material
--     * Slot: library_source_molecule Description: Source Molecule
--     * Slot: file_id Description: File identifier
--     * Slot: file_name Description: Name of file
--     * Slot: file_type Description: File type from enumerated list
--     * Slot: file_description Description: Human-readable description of file
--     * Slot: file_size Description: File size in bytes
--     * Slot: md5sum Description: MD5 hex digest for this file
--     * Slot: file_url_in_cds Description: Location of the file on the CDS cloud, using AWS S3 protocol
--     * Slot: experimental_strategy_and_data_subtypes Description: What is the experimental strategy used for the study (or what type of data subtypes exist in the study)?
--     * Slot: submission_version Description: The version of the metadata file submitted to CDS
--     * Slot: checksum_value Description: checksum (hash) for file (using checksum_algorithm) - if you want to use a checksum other than md5
--     * Slot: checksum_algorithm Description: The method by which the file checksum was calculated.
--     * Slot: crdc_id Description: The crdc_id is a unique identifier that is generated by Data Hub
--     * Slot: file_mapping_level Description: Describes if the file belongs to a Participant, a Sample, or a Study
-- # Class: "image" Description: "The imaging data from DICOM and non-DICOM standards into CDS."
--     * Slot: id Description: 
--     * Slot: study_link_id Description: The study_link_id is ID property for the node image. It should consist of a string and a number.
--     * Slot: de_identification_method_type Description: General description of the de-identification method
--     * Slot: de_identification_method_description Description: Description of the process of removing potentially identifying data or data elements to render data into a form that does not identify individuals and where identification is not likely to take place.
--     * Slot: de_identification_software Description: Software that was used to de-identify the images (if used)
--     * Slot: license Description: Official or legal permission to do or own a specified thing.
--     * Slot: citation_or_DOI Description: Publication and/or digital object identifier of the publication for open access studies
--     * Slot: species Description: Use the NCBI Taxonomy ID to identify species. A label provided by NCBI Taxonomy Database (https://www.ncbi.nlm.nih.gov/taxonomy/),  which uniquely identifies group or category, at any level, in a system for classifying plants or animals (including humans) providing ranked categories for the classification of organisms according to their suspected evolutionary relationships.
--     * Slot: image_modality Description: The method in which the images are generated.
--     * Slot: imaging_equipment_manufacturer Description: Producer of the imaging equipment that was used to generate the digital image
--     * Slot: imaging_equipment_model Description: The words used to describe the specific model of the instrument used to carry out an imaging experiment.
--     * Slot: imaging_sofware Description: The name of the software package that was used to capture, generate, and process the image.
--     * Slot: imaging_protocol Description: A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol (e.g. surface markers used in Smart-seq, dissociation duration, lot/batch numbers for key reagents such as primers, sequencing reagent kits, etc.) or the protocol by which the image was obtained or generated.
--     * Slot: organ_or_tissue Description: Site where images are associated
--     * Slot: performed_imaging_study_description Description: The textual representation of the certain or salient aspects, characteristics, or features of the imaging study. [Adapted from www.businessdictionary.com]
--     * Slot: performed_imaging_study_admittingDiagnosisCode Description: The identified disease(s) or illness(es) at the time of the admission during which imaging was performed.
--     * Slot: performed_imaging_study_nonAcquisitionModalitiesInStudyCode Description: A coded value specifying the type of equipment that created the images in this imaging study other than that used to acquire the original data.
--     * Slot: performed_imaging_study_lossyImageCompressionIndicator Description: Specifies whether any images in the study are irreversibly altered during encoding at any time during its life.
--     * Slot: performed_imaging_study_summary Description: A brief statement about the characteristics of this element, which is intended for use by the radiologist, technologist and/or physicist during management of the imaging protocol to understand the characteristics of the element in the protocol.
--     * Slot: performed_imaging_study_primaryAnatomicSiteCode Description: A coded value specifying the anatomic location that is the focus of this imaging process protocol element.
--     * Slot: performed_imaging_study_acquisitionTypeCode Description: A coded value specifying spatial aspects of the mechanism of data collection.
--     * Slot: performed_imaging_study_cardiacSynchronizationTechniqueCode Description: The means used to coordinate the collection or reconstruction of data with the cardiac cycle.
--     * Slot: performed_imaging_study_dataCollectionDiameter Description: The diameter of the region over which information is acquired.
--     * Slot: performed_imaging_study_respiratoryMotionTechniqueCode Description: The means to be used to coordinate the collection or reconstruction of data with breathing.
--     * Slot: performed_imaging_study_bodyPositionCode Description: A coded value specifying the 3-dimensional spatial orientation of a subject during this imaging acquisition protocol element.
--     * Slot: performed_imaging_study_typeCode Description: A coded value specifying the kind of algorithm used when reconstructing the image from the data acquired during the acquisition process.
--     * Slot: performed_imaging_study_algorithmCode Description: A coded value specifying the algorithm to use when reconstructing the image from the data acquired during the acquisition process
--     * Slot: performed_imaging_study_reconstructionFieldOfViewHeight Description: The vertical dimension of the rectangular region from which data is used in creating the reconstruction of the image.
--     * Slot: performed_imaging_study_reconstructionFieldOfViewWidth Description: The horizontal dimension of the rectangular region from which data is used in creating the reconstruction of the image.
--     * Slot: performed_imaging_study_reconstructionDiameter Description: The diameter of the region from which data is used in creating the reconstruction of the image.
--     * Slot: performed_imaging_study_sliceThickness Description: The cross plane dimension of the reconstructed image.
--     * Slot: performed_imaging_study_reconstructionInterval Description: The cross plane distance between the centers of adjacent, parallel reconstructed images.
--     * Slot: longitudinal_temporal_event_type Description: The type of event to which Longitudinal Temporal Offset from Event is relative.
--     * Slot: longitudinal_temporal_event_offset Description: An offset in days from a particular event of significance. May be fractional. In the context of a clinical trial, this is often the days since enrollment, or the baseline imaging Study.
--     * Slot: CTAquisitionProtocolElement_singleCollimationWidth Description: The width of a single row of acquired data. The units are of linear distince, e.g. mm.
--     * Slot: CTAquisitionProtocolElement_totalCollimationWidth Description: The width of the total collimation over the area of active x-ray detection. The units are of linear distince, e.g. mm.
--     * Slot: CTAquisitionProtocolElement_gantryDetectorTilt Description: Nominal angle of tilt in degrees of the scanning gantry. The units are of plane angle , e.g. degrees.  Zero degrees means the gantry is not tilted, negative degrees are when the top of the gantry is tilted away from where the table enters the gantry.
--     * Slot: CTAquisitionProtocolElement_spiralPitchFactor Description: Ratio of the distance that the table moves during a complete revolution of the source around the gantry orbit, to the width of the total collimation over the area of active x-ray detection. The units are of unity.
--     * Slot: CTAquisitionProtocolElement_ctdiVol Description: The average dose over the total volume scanned for the selected CT conditions of operation (calculated according to IEC 60601-2-44, Ed.2.1 (Clause 29.1.103.4)). The units are energy dose, e.g. mGy.
--     * Slot: CTAquisitionProtocolElement_ctdiPhantomTypeCode Description: The type of phantom to use for CTDI measurement according to IEC 60601-2-44
--     * Slot: CTAquisitionProtocolElement_kVp Description: Peak kilovoltage output of the x-ray generator. The units are of electrical potential.
--     * Slot: CTAquisitionProtocolElement_exposureModulationType_Code Description: The manner in which tube current is varied in order to limit the dose.
--     * Slot: CTImageReconstructionProtocolElement_convolutionKernel Description: A label describing the mathematical operations used to reconstruct images from the acquired data. The values for this attribute are vendor specific and not coded.
--     * Slot: CTImageReconstructionProtocolElement_convolutionKernelGroupCode Description: A coded value specifying the family of mathematical operations to use to reconstruct images from the acquired data
--     * Slot: MRImageAcquisitionProtocolElement_echoPulseSequenceCategoryCode Description: A coded value specifying an echo category of pulse sequences.
--     * Slot: MRImageAcquisitionProtocolElement_diffusionBValue Description: The factor by which the acquisition is sensitized to the Brownian motion of water molecules. The units are of time/area, e.g. s/mm2
--     * Slot: MRImageAcquisitionProtocolElement_diffusionDirectionalityCode Description: A coded value specifying whether diffusion conditions for the frame are directional, or isotropic with respect to direction
--     * Slot: MRImageAcquisitionProtocolElement_magneticFieldStrength Description: A vector quantity indicating the ability of a magnetic field to exert a force on moving electric charges. [The American Heritage® Science Dictionary]. The units are of magnetic flux density, e.g. tesla.
--     * Slot: MRImageAcquisitionProtocolElement_resonantNucleusCode Description: A coded value specifying the atomic nucleus that is the target of the acquisition
--     * Slot: MRImageAcquisitionProtocolElement_acquisitionContrastCode Description: A coded value specifying the inherent (as opposed to exogenous) contrast in the acquisition.
--     * Slot: MRImageAcquisitionProtocolElement_inversionRecoveryIndicator Description: Specifies whether an inversion recovery preparatory sequence is used in the acquisition.
--     * Slot: MRImageAcquisitionProtocolElement_pulseSequenceName Description: Name of the pulse sequence that is used for the acquisition. This is usually a vendor-specific name.
--     * Slot: MRImageAcquisitionProtocolElement_multipleSpinEchoIndicator Description: Specifies whether different lines in k-space are collected for a single frame.
--     * Slot: MRImageAcquisitionProtocolElement_phaseContrastIndicator Description: Specifies whether this is a pulse sequence in which the flowing spins are velocity encoded in phase.
--     * Slot: MRImageAcquisitionProtocolElement_timeOfFlightContrastIndicator Description: Specifies whether contrast is created by the inflow of blood in the saturated plane.
--     * Slot: MRImageAcquisitionProtocolElement_arterialSpinLabelingContrastCode Description: A coded value specifying how arterial water is used as a diffusable tracer.
--     * Slot: MRImageAcquisitionProtocolElement_steadyStatePulseSequenceCode Description: A coded value specifying how residual transverse magnetization is maintained during the acquisition.
--     * Slot: MRImageAcquisitionProtocolElement_echoPlanarPulseSequenceIndicator Description: Specifies whether multiple echos of different phase steps are acquired using rephasing gradients instead of repeated 180-degree pulses.
--     * Slot: MRImageAcquisitionProtocolElement_saturationRecoveryIndicator Description: Specifies whether a saturation recovery pulse sequence is used
--     * Slot: MRImageAcquisitionProtocolElement_spectrallySelectedSuppressionCode Description: A coded value specifying the type of substance-specific signal suppression is used.
--     * Slot: MRImageReconstructionProtocolElement_complexImageComponentCode Description: A coded value specifying the channel of the quadrature detected data, or the combination derived from those channels, used to reconstruct the image
--     * Slot: PETImagingAcquisitionProtocolElement_gantryDetectorTilt Description: Nominal angle of tilt in degrees of the scanning gantry. The units are of plane angle , e.g. degrees.  Zero degrees means the gantry is not tilted, negative degrees are when the top of the gantry is tilted away from where the table enters the gantry.
--     * Slot: Radiopharmaceutical_radionuclideCode Description: A coded value that specifies the radioactive isotope in the radiophamaceutical.
--     * Slot: acquisition_method_type Description: Records the method of acquisition or source for the specimen under consideration
--     * Slot: tumor_tissue_type Description: Text that describes the kind of disease present in the tumor specimen as related to a specific timepoint (add rows to select multiple values along with timepoints)
--     * Slot: tissue_fixative Description: A compound that preserves tissues and cells for microscopic study.
--     * Slot: embedding_medium Description: A material that infiltrates and supports a specimen and preserves its shape and structure for sectioning and microscopy.
--     * Slot: staining_method Description: Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination.
--     * Slot: objective Description: An objective is an optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object.
--     * Slot: nominal_magnification Description: The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. floating point value > 1(no units)
--     * Slot: immersion Description: Immersion medium
--     * Slot: lens_numerical_aperture Description: The numerical aperture of the lens. Floating point value > 0.
--     * Slot: working_distance Description: The working distance of the lens, expressed as a floating point number. Floating point > 0. Size needs to be specified in microns (um)
--     * Slot: imaging_assay_type Description: Type of imaging assay
--     * Slot: pyramid Description: The data file contains an image pyramid
--     * Slot: physical_size_x Description: Physical size (X-dimension) of a pixel. Floating point value > 0. Size needs to be specified in microns (um)
--     * Slot: physical_size_y Description: Physical size (Y-dimension) of a pixel. Floating point value > 0. Size needs to be specified in microns (um)
--     * Slot: physical_size_z Description: Physical size (Z-dimension) of a pixel. Floating point value > 0. Size needs to be specified in microns (um)
--     * Slot: size_c Description: Number of channels. Integer >= 1
--     * Slot: size_t Description: Number of time points. Integer >= 1
--     * Slot: size_x Description: Size of image: X dimension (in pixels). Integer >= 1
--     * Slot: size_y Description: Size of image: Y dimension (in pixels). Integer >= 1
--     * Slot: size_z Description: Size of image: Z dimension (in pixels). Integer >= 1
--     * Slot: channel_metadata_filename Description: File name of uploaded companion CSV file containing channel-level metadata details
--     * Slot: channel_metadata_file_url_in_cds Description: 
--     * Slot: channel_id Description: The unique channel identifier for each channel in this image must match the corresponding field in the OME-TIFF header
--     * Slot: channel_name Description: Channel label for each channel in this image must match the corresponding field in the OME-TIFF header
--     * Slot: cycle_number Description: the cycle # in which the co-listed reagent(s) was(were) used
--     * Slot: sub_cycle_number Description: sub-cycle #
--     * Slot: target_name Description: short descriptive name (abbreviation) for this target (antigen)
--     * Slot: antibody_name Description: short descriptive name for this antibody
--     * Slot: rrid_identifier Description: Research Resource Identifier
--     * Slot: fluorophore Description: Fluorescent dye label
--     * Slot: clone Description: Unique clone identifier
--     * Slot: lot Description: lot number from vendor
--     * Slot: catalog_number Description: catalog number from vendor
--     * Slot: excitation_wavelength Description: center/peak of the excitation spectrum (nm)
--     * Slot: emission_wavelength Description: center/peak of the emission spectrum (nm)
--     * Slot: excitation_bandwidth Description: nominal width of excitation spectrum (nm)
--     * Slot: emission_bandwidth Description: nominal width of emission spectrum (nm)
--     * Slot: metal_isotope_element_abbreviation Description: Element abbreviation
--     * Slot: metal_isotope_element_mass Description: Element mass number
--     * Slot: oligo_barcode_upper_strand Description: DNA barcode used for labeling
--     * Slot: oligo_barcode_lower_strand Description: DNA barcode used for labeling
--     * Slot: dilution Description: Final dilution ratio used in experiment
--     * Slot: concentration Description: Final concentration used in experiment
--     * Slot: crdc_id Description: The crdc_id is a unique identifier that is generated by Data Hub
--     * Slot: file_id Description: File identifier
--     * Slot: file_name Description: Name of file
--     * Slot: file_type Description: File type from enumerated list
--     * Slot: file_description Description: Human-readable description of file
--     * Slot: file_size Description: File size in bytes
--     * Slot: md5sum Description: MD5 hex digest for this file
--     * Slot: file_url_in_cds Description: Location of the file on the CDS cloud, using AWS S3 protocol
--     * Slot: experimental_strategy_and_data_subtypes Description: What is the experimental strategy used for the study (or what type of data subtypes exist in the study)?
--     * Slot: submission_version Description: The version of the metadata file submitted to CDS
--     * Slot: checksum_value Description: checksum (hash) for file (using checksum_algorithm) - if you want to use a checksum other than md5
--     * Slot: checksum_algorithm Description: The method by which the file checksum was calculated.
--     * Slot: file_mapping_level Description: Describes if the file belongs to a Participant, a Sample, or a Study

CREATE TABLE program (
	id INTEGER NOT NULL, 
	program_name TEXT, 
	program_acronym TEXT, 
	program_short_description TEXT, 
	program_full_description TEXT, 
	program_external_url TEXT, 
	program_sort_order INTEGER, 
	program_short_name TEXT, 
	institution TEXT, 
	study_name TEXT, 
	study_acronym TEXT, 
	study_description TEXT, 
	short_description TEXT, 
	study_external_url TEXT, 
	primary_investigator_name TEXT, 
	primary_investigator_email TEXT, 
	co_investigator_name TEXT, 
	co_investigator_email TEXT, 
	phs_accession TEXT, 
	bioproject_accession TEXT, 
	index_date VARCHAR(18), 
	cds_requestor TEXT, 
	funding_agency TEXT, 
	funding_source_program_name TEXT, 
	grant_id TEXT, 
	clinical_trial_system TEXT, 
	clinical_trial_identifier TEXT, 
	clinical_trial_arm TEXT, 
	organism_species TEXT, 
	adult_or_childhood_study VARCHAR(17), 
	data_types TEXT, 
	file_types TEXT, 
	data_access_level VARCHAR(10), 
	cds_primary_bucket TEXT, 
	cds_secondary_bucket TEXT, 
	cds_tertiary_bucket TEXT, 
	number_of_participants FLOAT, 
	number_of_samples FLOAT, 
	study_data_types VARCHAR(9), 
	file_types_and_format TEXT, 
	size_of_data_being_uploaded TEXT, 
	acl TEXT, 
	study_access VARCHAR(10), 
	authz TEXT, 
	study_version TEXT, 
	role_or_affiliation TEXT, 
	title TEXT, 
	first_name TEXT, 
	middle_name TEXT, 
	last_name TEXT, 
	suffix TEXT, 
	email TEXT, 
	clinical_trial_repository TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE study (
	id INTEGER NOT NULL, 
	study_name TEXT, 
	study_acronym TEXT, 
	study_description TEXT, 
	short_description TEXT, 
	study_external_url TEXT, 
	primary_investigator_name TEXT, 
	primary_investigator_email TEXT, 
	co_investigator_name TEXT, 
	co_investigator_email TEXT, 
	phs_accession TEXT, 
	bioproject_accession TEXT, 
	index_date VARCHAR(18), 
	cds_requestor TEXT, 
	funding_agency TEXT, 
	funding_source_program_name TEXT, 
	grant_id TEXT, 
	clinical_trial_system TEXT, 
	clinical_trial_identifier TEXT, 
	clinical_trial_arm TEXT, 
	organism_species TEXT, 
	adult_or_childhood_study VARCHAR(17), 
	data_types TEXT, 
	file_types TEXT, 
	data_access_level VARCHAR(10), 
	cds_primary_bucket TEXT, 
	cds_secondary_bucket TEXT, 
	cds_tertiary_bucket TEXT, 
	number_of_participants FLOAT, 
	number_of_samples FLOAT, 
	study_data_types VARCHAR(9), 
	file_types_and_format TEXT, 
	size_of_data_being_uploaded TEXT, 
	acl TEXT, 
	study_access VARCHAR(10), 
	authz TEXT, 
	study_version TEXT, 
	role_or_affiliation TEXT, 
	title TEXT, 
	first_name TEXT, 
	middle_name TEXT, 
	last_name TEXT, 
	suffix TEXT, 
	email TEXT, 
	clinical_trial_repository TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE participant (
	id INTEGER NOT NULL, 
	study_participant_id TEXT, 
	participant_id TEXT, 
	race VARCHAR(41), 
	gender VARCHAR(12), 
	ethnicity VARCHAR(22), 
	"dbGaP_subject_id" TEXT, 
	sex VARCHAR(25), 
	crdc_id TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE diagnosis (
	id INTEGER NOT NULL, 
	study_diagnosis_id TEXT, 
	diagnosis_id TEXT, 
	disease_type VARCHAR(52), 
	vital_status VARCHAR(12), 
	primary_diagnosis VARCHAR(138), 
	primary_site VARCHAR(42), 
	age_at_diagnosis INTEGER, 
	tumor_grade VARCHAR(18), 
	tumor_stage_clinical_m VARCHAR(12), 
	tumor_stage_clinical_n VARCHAR(12), 
	tumor_stage_clinical_t VARCHAR(13), 
	morphology VARCHAR(12), 
	incidence_type VARCHAR(11), 
	progression_or_recurrence VARCHAR(22), 
	days_to_recurrence INTEGER, 
	days_to_last_followup INTEGER, 
	last_known_disease_status VARCHAR(60), 
	days_to_last_known_status INTEGER, 
	tissue_or_organ_of_origin VARCHAR(39), 
	site_of_resection_or_biopsy VARCHAR(39), 
	days_to_last_known_disease_status FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE treatment (
	id INTEGER NOT NULL, 
	treatment_id TEXT, 
	treatment_type VARCHAR(50), 
	treatment_outcome VARCHAR(26), 
	days_to_treatment INTEGER, 
	therapeutic_agents VARCHAR(167), 
	response TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE sample (
	id INTEGER NOT NULL, 
	sample_id TEXT, 
	sample_type VARCHAR(11), 
	sample_description TEXT, 
	sample_type_category TEXT, 
	sample_tumor_status VARCHAR(12), 
	sample_anatomic_site VARCHAR(38), 
	sample_age_at_collection INTEGER, 
	derived_from_specimen TEXT, 
	biosample_accession TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE file (
	id INTEGER NOT NULL, 
	file_id TEXT, 
	file_name TEXT, 
	file_type VARCHAR(5), 
	file_description TEXT, 
	file_size INTEGER, 
	md5sum TEXT, 
	file_url_in_cds TEXT, 
	experimental_strategy_and_data_subtypes TEXT, 
	submission_version TEXT, 
	checksum_value TEXT, 
	checksum_algorithm TEXT, 
	crdc_id TEXT, 
	file_mapping_level VARCHAR(12), 
	PRIMARY KEY (id)
);
CREATE TABLE genomic_info (
	id INTEGER NOT NULL, 
	genomic_info_id TEXT, 
	library_id TEXT, 
	bases INTEGER, 
	number_of_reads INTEGER, 
	avg_read_length FLOAT, 
	coverage FLOAT, 
	reference_genome_assembly VARCHAR(21), 
	custom_assembly_fasta_file_for_alignment TEXT, 
	design_description TEXT, 
	library_strategy VARCHAR(39), 
	library_layout VARCHAR(14), 
	library_source VARCHAR(26), 
	library_selection VARCHAR(38), 
	platform VARCHAR(17), 
	instrument_model VARCHAR(28), 
	sequence_alignment_software TEXT, 
	reporter_label TEXT, 
	methylation_platform TEXT, 
	library_source_material VARCHAR(13), 
	library_source_molecule VARCHAR(18), 
	file_id TEXT, 
	file_name TEXT, 
	file_type VARCHAR(5), 
	file_description TEXT, 
	file_size INTEGER, 
	md5sum TEXT, 
	file_url_in_cds TEXT, 
	experimental_strategy_and_data_subtypes TEXT, 
	submission_version TEXT, 
	checksum_value TEXT, 
	checksum_algorithm TEXT, 
	crdc_id TEXT, 
	file_mapping_level VARCHAR(12), 
	PRIMARY KEY (id)
);
CREATE TABLE image (
	id INTEGER NOT NULL, 
	study_link_id TEXT, 
	de_identification_method_type VARCHAR(14), 
	de_identification_method_description TEXT, 
	de_identification_software TEXT, 
	license VARCHAR(60), 
	"citation_or_DOI" TEXT, 
	species TEXT, 
	image_modality VARCHAR(21), 
	imaging_equipment_manufacturer TEXT, 
	imaging_equipment_model TEXT, 
	imaging_sofware TEXT, 
	imaging_protocol TEXT, 
	organ_or_tissue TEXT, 
	performed_imaging_study_description TEXT, 
	"performed_imaging_study_admittingDiagnosisCode" TEXT, 
	"performed_imaging_study_nonAcquisitionModalitiesInStudyCode" TEXT, 
	"performed_imaging_study_lossyImageCompressionIndicator" VARCHAR(1), 
	performed_imaging_study_summary TEXT, 
	"performed_imaging_study_primaryAnatomicSiteCode" TEXT, 
	"performed_imaging_study_acquisitionTypeCode" TEXT, 
	"performed_imaging_study_cardiacSynchronizationTechniqueCode" VARCHAR(13), 
	"performed_imaging_study_dataCollectionDiameter" TEXT, 
	"performed_imaging_study_respiratoryMotionTechniqueCode" VARCHAR(13), 
	"performed_imaging_study_bodyPositionCode" VARCHAR(13), 
	"performed_imaging_study_typeCode" TEXT, 
	"performed_imaging_study_algorithmCode" TEXT, 
	"performed_imaging_study_reconstructionFieldOfViewHeight" TEXT, 
	"performed_imaging_study_reconstructionFieldOfViewWidth" TEXT, 
	"performed_imaging_study_reconstructionDiameter" TEXT, 
	"performed_imaging_study_sliceThickness" TEXT, 
	"performed_imaging_study_reconstructionInterval" TEXT, 
	longitudinal_temporal_event_type FLOAT, 
	longitudinal_temporal_event_offset FLOAT, 
	"CTAquisitionProtocolElement_singleCollimationWidth" TEXT, 
	"CTAquisitionProtocolElement_totalCollimationWidth" TEXT, 
	"CTAquisitionProtocolElement_gantryDetectorTilt" TEXT, 
	"CTAquisitionProtocolElement_spiralPitchFactor" TEXT, 
	"CTAquisitionProtocolElement_ctdiVol" TEXT, 
	"CTAquisitionProtocolElement_ctdiPhantomTypeCode" TEXT, 
	"CTAquisitionProtocolElement_kVp" TEXT, 
	"CTAquisitionProtocolElement_exposureModulationType_Code" VARCHAR(12), 
	"CTImageReconstructionProtocolElement_convolutionKernel" TEXT, 
	"CTImageReconstructionProtocolElement_convolutionKernelGroupCode" TEXT, 
	"MRImageAcquisitionProtocolElement_echoPulseSequenceCategoryCode" VARCHAR(8), 
	"MRImageAcquisitionProtocolElement_diffusionBValue" TEXT, 
	"MRImageAcquisitionProtocolElement_diffusionDirectionalityCode" VARCHAR(11), 
	"MRImageAcquisitionProtocolElement_magneticFieldStrength" TEXT, 
	"MRImageAcquisitionProtocolElement_resonantNucleusCode" VARCHAR(5), 
	"MRImageAcquisitionProtocolElement_acquisitionContrastCode" VARCHAR(57), 
	"MRImageAcquisitionProtocolElement_inversionRecoveryIndicator" TEXT, 
	"MRImageAcquisitionProtocolElement_pulseSequenceName" TEXT, 
	"MRImageAcquisitionProtocolElement_multipleSpinEchoIndicator" TEXT, 
	"MRImageAcquisitionProtocolElement_phaseContrastIndicator" TEXT, 
	"MRImageAcquisitionProtocolElement_timeOfFlightContrastIndicator" TEXT, 
	"MRImageAcquisitionProtocolElement_arterialSpinLabelingContrastCode" TEXT, 
	"MRImageAcquisitionProtocolElement_steadyStatePulseSequenceCode" VARCHAR(15), 
	"MRImageAcquisitionProtocolElement_echoPlanarPulseSequenceIndicator" TEXT, 
	"MRImageAcquisitionProtocolElement_saturationRecoveryIndicator" TEXT, 
	"MRImageAcquisitionProtocolElement_spectrallySelectedSuppressionCode" VARCHAR(13), 
	"MRImageReconstructionProtocolElement_complexImageComponentCode" VARCHAR(9), 
	"PETImagingAcquisitionProtocolElement_gantryDetectorTilt" TEXT, 
	"Radiopharmaceutical_radionuclideCode" TEXT, 
	acquisition_method_type TEXT, 
	tumor_tissue_type TEXT, 
	tissue_fixative VARCHAR(17), 
	embedding_medium VARCHAR(22), 
	staining_method VARCHAR(9), 
	objective TEXT, 
	nominal_magnification TEXT, 
	immersion TEXT, 
	lens_numerical_aperture TEXT, 
	working_distance TEXT, 
	imaging_assay_type TEXT, 
	pyramid TEXT, 
	physical_size_x TEXT, 
	physical_size_y TEXT, 
	physical_size_z TEXT, 
	size_c TEXT, 
	size_t TEXT, 
	size_x TEXT, 
	size_y TEXT, 
	size_z TEXT, 
	channel_metadata_filename TEXT, 
	channel_metadata_file_url_in_cds TEXT, 
	channel_id TEXT, 
	channel_name TEXT, 
	cycle_number TEXT, 
	sub_cycle_number TEXT, 
	target_name TEXT, 
	antibody_name TEXT, 
	rrid_identifier TEXT, 
	fluorophore TEXT, 
	clone TEXT, 
	lot TEXT, 
	catalog_number TEXT, 
	excitation_wavelength TEXT, 
	emission_wavelength TEXT, 
	excitation_bandwidth TEXT, 
	emission_bandwidth TEXT, 
	metal_isotope_element_abbreviation TEXT, 
	metal_isotope_element_mass TEXT, 
	oligo_barcode_upper_strand TEXT, 
	oligo_barcode_lower_strand TEXT, 
	dilution TEXT, 
	concentration TEXT, 
	crdc_id TEXT, 
	file_id TEXT, 
	file_name TEXT, 
	file_type VARCHAR(5), 
	file_description TEXT, 
	file_size INTEGER, 
	md5sum TEXT, 
	file_url_in_cds TEXT, 
	experimental_strategy_and_data_subtypes TEXT, 
	submission_version TEXT, 
	checksum_value TEXT, 
	checksum_algorithm TEXT, 
	file_mapping_level VARCHAR(12), 
	PRIMARY KEY (id)
);