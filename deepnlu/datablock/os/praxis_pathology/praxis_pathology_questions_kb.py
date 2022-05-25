
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# SEMI-AUTONOMOUS generation on 25-April-2022
# http://localhost:8889/notebooks/grafflbox/GRAFFL-298%20(Speech%20Disorder)%20Create%20QA%20Pairs.ipynb


praxis_pathology_questions = [
    "By the time a child is around 24 months old, how much of the child's speech should the parents be able to understand?",
    "By the time the child is about 36 months old, how much of the child's speech should the parents be able to understand?",
    'Do professors expect graduate students to be automatically proficient in such writing skills?',
    'Do these programs eschew punishment?',
    'Does Brocas aphasia impair receptive language ability?',
    'Does the IEP only apply to school-age children?',
    "How can the judgment of how natural an individual's speech sounds be rated?",
    'How do hearing aids and cochlear implants work?',
    'How do language deficits often cause children to perform below ability on school assessments?',
    'How do sound waves become sound perceptions?',
    'How does aphasia differ from dysarthria and apraxia?',
    'How does botulinum toxin work?',
    'How does the palatal lift work?',
    'How does this extra chromosome affect individuals with Down syndrome?',
    'How is velopharyngeal function typically evaluated?',
    'How many muscles and nerves are involved in the normal adult human eating and swallowing processes?',
    'How many relationships does an expert suggest maintaining?',
    'How many school SLPs report receiving information about students therapy via phone calls?',
    'How old were these studies as of 2013?',
    'In what cultures is it considered offensive to use the come here forefinger gesture with humans?',
    'In what cultures is it considered rude or disrespectful to make direct eye contact when talking with others?',
    'In what setting is the SLP required to comply with the IDEA?',
    'In what setting is the childs third birthday the criterion for automatic discharge?',
    'Is African-American Vernacular English a disorder?',
    'Profound sensorineural hearing loss means that the hair cells in the **** of Corti at the cochlea no longer function. This type of hearing loss cannot be remedied by hearing aids, which 33',
    'What actions are involved in the complete hearing process?',
    'What affects receptive language?',
    'What age group has the highest rates of hospitalizations and deaths related to TBIs?',
    'What are ASHAs criteria for discharging SLP clients?',
    'What are answer choices, , and related to?',
    'What are cognitive skills of a typically developing 1-year-old?',
    'What are criterion-referenced tests better for measuring?',
    'What are dysarthrias?',
    'What are exercises prescribed for?',
    'What are norm-referenced tests better for measuring?',
    'What are people with Wernickes aphasia able to do?',
    'What are phonemes?',
    'What are phonological process disorders characterized by?',
    'What are rigidity and problems with scaling movements characteristic of?',
    'What are sensory skills of a typical 1-year-old?',
    'What are some advantages of using standardized tests?',
    'What are some age-appropriate activities for autistic elementary-school-age children?',
    'What are some benefits of the cognitive approach to language remediation?',
    'What are some causes of vocal cord nodules?',
    'What are some conditions that can cause or contribute to esophagitis?',
    'What are some conditions that violate the ASHA Code of Ethics, Principle of Ethics II, Rule B?',
    'What are some difficulties that cognitive communication disorders involve?',
    "What are some dysfluencies that are normal in young children's speech?",
    'What are some examples of how Iatrogenic etiology can cause dysphagia?',
    'What are some exceptions to the rule?',
    'What are some methods of direct approaches to stuttering therapy?',
    'What are some neurological etiologies for stuttering?',
    'What are some of the anatomical defects that can cause velopharyngeal insufficiency?',
    'What are some of the benefits of analytic languages?',
    'What are some of the causes of speech and language delays?',
    'What are some of the common features of Down syndrome?',
    'What are some of the conditions that can cause mixed nasality in speech?',
    'What are some of the developments that enable human children to develop speech?',
    'What are some of the disadvantages of an electrolarynx?',
    'What are some of the gaps in the system that lead to this loss?',
    'What are some of the implications of a neurological basis for stuttering?',
    'What are some of the other possible causes of a cognitive communication disorder?',
    'What are some of the physiological defects that can cause velopharyngeal incompetence?',
    'What are some of the potential consequences of scleroderma?',
    'What are some of the things that Cochlear implants will not do?',
    'What are some of the trends that have been stimulated by federal law?',
    "What are some of the ways in which language deficits can infringe on children's development?",
    'What are some other obstacles to follow up?',
    'What are some other ways of producing speech besides esophageal speech?',
    'What are some symptoms of right-hemisphere neurological damage?',
    'What are some treatments for dysphagia?',
    'What are some ways in which computers save time for school SLPs?',
    'What are sound waves always longitudinal and never transverse?',
    'What are the advantages of authentic assessments?',
    'What are the advantages of dynamic assessments?',
    "What are the approximate age norms for the child's speech being intelligible to strangers?",
    'What are the benefits of open questions?',
    'What are the causes of dysphagia?',
    'What are the clients goals and choices included under ASHAs discharge criteria?',
    'What are the clinical indications for screening both children and adults?',
    'What are the conditions or steps required for learning according to Albert Bandura?',
    'What are the consequences of a mild hearing loss?',
    'What are the consequences of co-articulation?',
    'What are the consequences of esophagitis?',
    'What are the consequences of not having a universal newborn hearing screening?',
    'What are the consequences of this loss?',
    'What are the consequences of velopharyngeal mislearning?',
    'What are the differences between an IFSP and IEP?',
    'What are the different types of dysarthria caused by neurological damage?',
    'What are the disadvantages of authentic assessments?',
    'What are the drawbacks of closed questions?',
    'What are the effects of conductive hearing loss?',
    "What are the four distinct stages of cognitive development posited by Piaget's theory?",
    'What are the four stages of eating and swallowing?',
    'What are the four stages of the four-stage model?',
    'What are the functional impairments in swallowing caused by chemoradiation therapy to treat cancer of the head and neck?',
    'What are the functions of the left and right hemisphere of the brain?',
    'What are the levels of severity on the ALS Severity Scale?',
    'What are the most frequent causes of aphasia in adults?',
    'What are the ossicles?',
    'What are the possible causes of stuttering according to the Demands and Capacities Model?',
    'What are the possible outcomes for late-talking children?',
    'What are the principles of language disorder treatment for the youngest children?',
    'What are the results of one study never sufficient for?',
    "What are the signs of this patient's aphasia?",
    'What are the symptoms of Hunter syndrome?',
    'What are the symptoms of Parkinson disease?',
    'What are the symptoms of a functional speech disorder?',
    'What are the three types of aphasia?',
    'What are the two most common ways school SLPs receive information about students therapy from professionals at other facilities?',
    'What are two phonological processes that normally end around the age of 3 years?',
    'What are typical motor skills development of a 1-year-old?',
    'What can Esophagoscopy detect?',
    'What can aerodynamic testing measure?',
    'What can be objectively measured about stuttering?',
    'What can be objectively measured about the rate of speech?',
    'What can cause mixed nasality in speech?',
    'What can children normally do by 5 to 6 years and what has Tommy not attained by age 9?',
    'What can lowering blood pressure prevent?',
    "What can parents do to help prevent their child's normal dysfluencies from developing into stuttering?",
    'What can proton pump inhibitors treat?',
    'What can psychometric review of tests for evaluating preschool language skills identify?',
    'What can the intra-**** examination assess for?',
    'What causes more than 10% of all speech problems?',
    'What causes nonsyndromic deafness?',
    'What causes phonetic deviations in children with cleft palates?',
    'What develops sooner, receptive or expressive language?',
    'What did disabled students have to be included in before the 1997 and 2004 reauthorizations of the IDEA?',
    'What did state school systems have to change with the accountability mandated by the laws?',
    'What difficulties does a patient with Brocas aphasia have?',
    'What do ASHA discharge criteria reflect?',
    'What do ASHA discharge guidelines and independent clinicians and researchers recommend in addition to normative standardized test results and functional communication skills?',
    'What do Middle Eastern cultures believe about the left hand?',
    'What do TBI patients frequently develop postinjury?',
    'What do all of the diseases named have in common?',
    'What do babies typically do between birth and 3 months?',
    'What do babies typically do from around 4 to 6 months?',
    'What do experts say is the best way to provide quality service to students?',
    'What do many websites and software programs now exist?',
    'What do patients with vocal cord nodules or polyps often experience?',
    'What do post-TBI cognitive communication disorders typically NOT cause impairment of?',
    'What do the IDEA and No Child Left Behind demand of educators?',
    'What do the data from the ASHA National Outcomes Measurement System find?',
    'What do the expressions quoted reflect?',
    'What do young children with primary stuttering not experience?',
    "What does ASHA recommend that parents do if they are worried about their child's speech development?",
    'What does Brocas aphasia affect?',
    'What does Multi-view videofluoroscopy give 3-D imaging of?',
    'What does Part C of the IDEA do?',
    'What does Piaget state about children and learning?',
    'What does Skinners behaviorist theory emphasize?',
    'What does Vygotsky state about social interactions in regards to learning?',
    'What does Wernickes aphasia affect?',
    'What does Wernickes aphasia do?',
    "What does children's language development focus on most?",
    'What does counseling do for clients?',
    'What does it mean when patients have difficulty understanding others questions or statements?',
    'What does lack of progress beyond chance suggest?',
    'What does left-hemisphere brain damage result in for only about half of left-handed people?',
    'What does left-hemisphere brain damage result in for the majority of right-handed people?',
    'What does meta-analysis of a number of recent research studies show?',
    'What does nasal air emission sound like in the obstructed form?',
    'What does nasal air emission sound like in the unobstructed form?',
    'What does nasometry do?',
    'What does the ASHA Code of Ethics prohibit?',
    'What does the IDEA take precedence in determining?',
    'What does the SLP do after giving the individual a description of the strategy?',
    'What does the SLP do first?',
    'What does the auricle do?',
    'What does the data in the meta-analysis confirm?',
    'What does the entire sequence of hearing involve?',
    'What does the expression mean?',
    'What does the fact that the pharynx elongates vertically during human development mean for adults?',
    'What does the law require for infants and toddlers?',
    'What does the law require for preschoolers and school-age children?',
    'What does the palatal obturator do?',
    'What does the process of audition involve?',
    'What does the stapedius reflex do?',
    'What does this description exemplify?',
    'What does this enable clients and students to do?',
    'What does this substitution imply about the speaker?',
    'What groups are NOT found to prevail among certain socioeconomic groups, cultural backgrounds or ESL/ELL children. ?',
    'What happens in the three-word stage?',
    'What happens when liquids enter the pharynx prematurely?',
    'What happens when the larynx does not close soon enough after a bolus reaches the larynx?',
    'What has research not shown about most SLPs?',
    'What have research studies found?',
    'What have researchers found about the majority of SLPs?',
    'What illnesses can cause aphasia?',
    "What is ASHA's advice to parents who have concerns about their child's fluency?",
    'What is African-American Vernacular English?',
    'What is Behaviorism?',
    'What is Brocas aphasia caused by?',
    'What is Brocas aphasia?',
    'What is Brocas area responsible for?',
    'What is Brocas area?',
    'What is Chomskys theory?',
    'What is Fetal Alcohol Syndrome associated with?',
    'What is GERD?',
    'What is Hunter syndrome?',
    'What is Iatrogenic etiology?',
    'What is Manometry?',
    "What is Tommy's age and what does he have the vocabulary of?",
    'What is Wernickes aphasia?',
    'What is Wernickes area?',
    'What is a PET scan?',
    'What is a case study?',
    'What is a caveat with standardized tests?',
    'What is a characteristic of mixed nasality?',
    'What is a cognitive communication disorder?',
    'What is a cohort study?',
    'What is a common characteristic of some dialects in England?',
    'What is a common symptom of patients with vocal cord nodules or polyps?',
    'What is a common treatment for laryngeal cancer?',
    'What is a cross-sectional study?',
    'What is a disadvantage of norm-referenced, standardized tests?',
    'What is a feature of secondary stuttering?',
    'What is a feeding tube?',
    'What is a formant?',
    'What is a hypernasal voice characterized by?',
    'What is a hyponasal voice characterized by?',
    'What is a pediatric feeding evaluation?',
    'What is a perceptual exam?',
    'What is a phoneme?',
    'What is a phonological disorder?',
    'What is a protoword?',
    'What is a trend that was observed by those conducting recent literature reviews?',
    'What is a videofluoroscopic swallow study?',
    'What is amplitude?',
    'What is an advantage of norm-referenced, standardized tests?',
    'What is an articulation disorder?',
    'What is an endoscope used for?',
    'What is an example of a complex utterance?',
    'What is an example of a direct therapeutic method for treating stuttering?',
    'What is an example of a phonological process disorder?',
    'What is an example of an indirect therapeutic method for treating stuttering?',
    'What is an example of classical conditioning?',
    'What is an example of devocalization?',
    'What is an exception to the confidentiality provision in the IDEAs?',
    'What is another advantage of many websites and software programs?',
    'What is another common symptom of patients with vocal cord nodules or polyps?',
    'What is another grammatical category?',
    'What is anoxia?',
    'What is apraxia of speech?',
    'What is apraxia?',
    'What is aspiration pneumonia?',
    'What is asymmetrical hearing loss?',
    'What is ataxia?',
    'What is botulinum toxin used for?',
    'What is cerebral palsy?',
    'What is classical conditioning?',
    'What is co-articulation?',
    'What is conductive hearing loss?',
    'What is dehydration?',
    'What is dermatomyositis?',
    'What is dilation used to treat?',
    'What is diverticulitis?',
    'What is dysphagia?',
    'What is esophagitis?',
    'What is fluency shaping?',
    'What is frequency?',
    'What is hypernasal speech resonance?',
    'What is included among indirect treatment approaches?',
    'What is included in fluency shaping?',
    'What is included in the ASHA discharge guidelines?',
    'What is malnutrition?',
    'What is more age-appropriate for high school students with autism: practicing skills for successfully responding in job interviews, or practicing phrases and strategies for peer interactions?',
    'What is more age-appropriate for young children with autism: reinforcing the childs response to hearing his or her name called, or practicing phrases and strategies for peer interactions?',
    'What is more appropriate for school-age children?',
    'What is more appropriate when treating younger children when promoting language-based social interactions?',
    'What is more necessary with younger children not yet in school when it comes to parental involvement?',
    'What is most appropriate for older children when promoting metalinguistic awareness?',
    'What is muscular dystrophy?',
    'What is often impaired with right-hemisphere neurological damage?',
    'What is one barrier to connecting newborns who fail hearing screenings with needed services?',
    'What is one characteristic of individuals with cognitive communication disorders?',
    'What is one example of a property or rule that students frequently transfer from their native language to English?',
    'What is one of the impairments that leads to aspiration?',
    'What is one physical characteristic of children with Down syndrome?',
    'What is one set of criteria for discharge that ASHA uses?',
    'What is one way to treat esophageal stenosis?',
    'What is operant conditioning?',
    'What is pH monitoring?',
    'What is period?',
    'What is permissible to give clients, family members, or prospective clients general informational or educational communications via e-mail, messaging, written letters, or other correspondence?',
    'What is phonemics?',
    'What is phonetics?',
    'What is phonology?',
    'What is poliomyelitis?',
    'What is polymyositis?',
    'What is positive predictive value?',
    'What is primary stuttering characterized by?',
    'What is reliability?',
    'What is required for infants and toddlers diagnosed with language disorders?',
    'What is required for school-age children and preschoolers diagnosed with language disorders?',
    'What is required in states that do not license CFs?',
    'What is required in states that license CFs?',
    'What is required of the supervising SLP in all states?',
    'What is retropharyngeal augmentation?',
    'What is school phobia?',
    'What is scleroderma?',
    'What is social learning theory?',
    'What is speech-language therapy less effective for?',
    'What is speech-language therapy more effective for?',
    'What is symmetrical hearing loss?',
    'What is the ALS Severity Scale?',
    'What is the ASHA Code of Ethics, Principle of Ethics II, Rule B?',
    'What is the ASHA National Outcomes Measurement System?',
    'What is the Covert Repair Hypothesis?',
    'What is the FERPA?',
    'What is the advice that researchers give to evaluators?',
    'What is the age norm for changing liquid phonemes into glides?',
    'What is the age norm for difficult consonants like /s/?',
    'What is the argument against the behaviorist theory?',
    'What is the ataxic type of dysarthria characterized by?',
    'What is the ataxic type of dysarthria?',
    'What is the attitude of Vietnamese and Hmong cultures towards complimenting babies as beautiful or cute?',
    'What is the attitude of Western mainstream cultures towards making eye contact when talking to people?',
    'What is the audiogram for age-related hearing loss typically like?',
    'What is the audiogram for noise-induced hearing loss typically like?',
    'What is the basis of Behaviorism?',
    'What is the best early intervention for young children?',
    'What is the best way to communicate progress to parents, teachers, and others?',
    'What is the best way to integrate language goals in classrooms?',
    'What is the cause of hypernasality in cleft palate?',
    'What is the cause of hypernasality in speech apraxia?',
    'What is the cause of unclear articulation in children with Down syndrome?',
    'What is the clearest advantage of an electrolarynx over esophageal speech?',
    'What is the clinical term for an abnormally small tongue?',
    'What is the clinical term for speech composed of unintelligible syllables that sound like speech but are meaningless?',
    'What is the clinical term for tongue-tied?',
    'What is the cognitive approach to language remediation?',
    'What is the correct term for a complete absence of any nasal resonance?',
    'What is the correlation between mild hearing loss and speech and language development?',
    'What is the counseling not restricted to?',
    'What is the cricopharyngeus muscle?',
    'What is the difference between /k/ and /g/?',
    'What is the difference between Chomskys theory and Skinners theory?',
    'What is the difference between Hunter syndrome and Turner syndrome?',
    'What is the difference between a PET scan and an fMRI?',
    'What is the difference between a complex utterance and a four-word utterance?',
    'What is the difference between a vocal cord nodule and a vocal cord polyp?',
    'What is the difference between an MRI and an fMRI?',
    'What is the difference between anxiety and depression?',
    'What is the difference between dysarthria and apraxia?',
    'What is the difference between functional speech disorders and phonological disorders?',
    'What is the difference between hearing aids and cochlear implants?',
    'What is the difference between hearing and the other senses?',
    'What is the difference between how we see colors and how we hear sounds?',
    'What is the difference between longitudinal and transverse waves?',
    'What is the difference between nonreduplicated babbling and reduplicated babbling?',
    'What is the difference between patients with damage to the right hemisphere and those with damage to the left hemisphere?',
    'What is the difference between protowords and babbling?',
    'What is the difference between syndromic and nonsyndromic deafness?',
    'What is the difference between the four-stage model and the process model?',
    'What is the difference between the obstructed and unobstructed form of nasal air emission?',
    'What is the difference between the three-stage and four-stage models?',
    'What is the difference between validity and reliability?',
    'What is the domain of language focused on language use in social contexts?',
    'What is the domain of language focused on speech sounds and their relationships and systems?',
    'What is the domain of language focused on the meanings of words?',
    'What is the early one-word stage?',
    'What is the error most likely due to?',
    'What is the etiology of functional speech disorders?',
    'What is the evidence for a neurological basis of stuttering?',
    'What is the evidence regarding exercise and dysarthria symptoms in ALS patients?',
    'What is the expression?',
    'What is the feature of mixed nasality in speech?',
    'What is the first principle of the Universalist-Linguistic theory of phonological acquisition?',
    'What is the first thing the SLP would do?',
    'What is the flaccid type of dysarthria characterized by?',
    "What is the focus of Skinner's theory of cognitive development?",
    "What is the focus of Vygotsky's theory of cognitive development?",
    'What is the frontal lobe of the brain responsible for?',
    'What is the function of the trachea?',
    'What is the future perfect tense of the verb?',
    'What is the genotype of a seed with two different alleles?',
    'What is the goal of fluency shaping?',
    'What is the goal of the stuttering modification technique?',
    'What is the goal of these recommendations?',
    'What is the hippocampus responsible for?',
    'What is the hyperkinetic type of dysarthria?',
    'What is the later one-word stage?',
    'What is the least-restrictive environment?',
    'What is the linguistic term for language variations peculiar to an individual person?',
    'What is the loss of follow-up diagnosis and treatment of many infants failing newborn hearing screenings due to?',
    'What is the main benefit of computer technology for school SLPs?',
    'What is the main cause of apraxia of speech?',
    'What is the main cause of children starting school with language deficits?',
    'What is the main finding of the research?',
    'What is the main focus of positive behavioral support programs?',
    'What is the main obstacle to connecting newborns who fail hearing screenings with needed services?',
    'What is the main reason why deaf adults refuse to consider any measures to allow them to hear better or hear at all?',
    'What is the mildest level on the ALS Severity Scale?',
    'What is the most authentic and comprehensive remediation of language disorders?',
    'What is the most common age for children to start losing their deciduous or baby teeth?',
    'What is the most common cause of a cognitive communication disorder?',
    'What is the most common newborn disability?',
    'What is the most common problem for patients with aphasia?',
    'What is the most common type of aphasia?',
    'What is the most effective way to give instruction on scientific writing skills?',
    'What is the most likely age group to incur a traumatic brain injury?',
    'What is the most recent of the choices?',
    "What is the next step after screening the child's hearing and vision?",
    'What is the number of citizens to sustain TBIs each year in the United States estimated to be?',
    'What is the obstacle that school SLPs find most often that interferes with communicating with other professionals about their students?',
    'What is the obstructed form of nasal air emission?',
    'What is the oldest of the choices?',
    'What is the only progressive motor neuron disease that causes degeneration in both the upper and lower motor neurons?',
    'What is the palatal lift?',
    'What is the pharyngeal flap procedure?',
    'What is the pharynx constrictor muscle?',
    'What is the phenotype of a heterozygous seed?',
    'What is the phonological process of consonant harmony?',
    'What is the pinna?',
    'What is the positive predictive value of a screening tool inversely correlated with?',
    'What is the preferred exposure for children in terms of reading material?',
    'What is the prefrontal cortex responsible for?',
    'What is the primary language structure of English?',
    'What is the purpose of diagnostic interventions?',
    'What is the purpose of teacher referrals to SLPs?',
    'What is the purpose of the stapedius reflex?',
    'What is the recommendation for hearing screening?',
    'What is the relationship between muscular dystrophy and speech disorders?',
    'What is the role of educators in these programs?',
    'What is the role of the SLP?',
    'What is the role of the audiologist?',
    'What is the second place obstacle that school SLPs find that interferes with communicating with other professionals about their students?',
    'What is the second principle of the Universalist-Linguistic theory of phonological acquisition?',
    'What is the second thing the SLP would do?',
    'What is the spastic type of dysarthria characterized by?',
    'What is the speech bulb obturator?',
    'What is the speech that is clearest to the general listener?',
    'What is the stage of complex utterances?',
    'What is the stapedius reflex?',
    'What is the stuttering modification technique?',
    'What is the submental muscle?',
    'What is the temporal lobe of the brain responsible for?',
    'What is the term for language variations peculiar to a certain geographic region and/or cultural group?',
    'What is the third thing the SLP would do?',
    'What is the two-word stage?',
    'What is the tympanic membrane?',
    'What is the unobstructed form of nasal air emission?',
    'What is thyromegaly?',
    'What is typical of a normally developing 2-year-old?',
    'What is unilateral hearing loss?',
    'What is validity?',
    'What is velopharyngeal incompetence?',
    'What is velopharyngeal insufficiency?',
    'What is velopharyngeal mislearning?',
    'What makes it easier for deaf and hard-of-hearing individuals to produce vocalized speech sounds?',
    'What may adult screenings result in?',
    'What may pediatric screenings result in?',
    'What muscles and nerves are involved in the normal adult human eating and swallowing processes?',
    'What muscles are controlled by the Hypoglossal nerve?',
    'What muscles are controlled by the Vagus nerve?',
    'What muscles does the glossopharyngeal nerve control?',
    'What muscles does the hypoglossal nerve control?',
    'What muscles does the trigeminal nerve control?',
    'What must children understand before they can produce their own language?',
    'What percentage of children referred to SLPs for help with their speech have conductive hearing losses?',
    'What percentage of children referred to SLPs for help with their speech have speech sound disorders attributed to genetically based linguistic processing deficits?',
    'What percentage of children referred to SLPs for help with their speech have speech sound disorders attributed to genetically based speech motor control deficits?',
    'What percentage of congenital deafness cases in the United States are genetic?',
    'What physiological differences are produced by the extra chromosome found in Down syndrome?',
    'What problems are patients with damage to the right hemisphere of the brain more likely to experience?',
    'What processes are involved in the normal adult human eating and swallowing processes?',
    'What processes language in the brain?',
    'What progressive motor neuron disease causes degeneration of only lower motor neurons?',
    'What progressive motor neuron disease causes degeneration of only upper motor neurons?',
    'What progressive neurological disorders can cause aphasia?',
    'What should be done before scrapping the entire program for another?',
    'What should parents NOT do when their child is speaking?',
    'What should patients be encouraged to do in order to improve their speech?',
    'What should we do if one study shows statistically nonsignificant or weak effects of an intervention?',
    'What sounds do babies typically demonstrate limitation of between the ages of 7 months and 1 year?',
    'What type of dysarthria is caused by neurological damage localized to the basal ganglia control circuit?',
    'What type of dysarthria is caused by neurological damage localized to the cerebellar control circuit?',
    'What types of problems do patients with damage to the right hemisphere of the brain typically experience?',
    'What violates Principle of Ethics I of the ASHA Code of Ethics, Rule C?',
    'What violates Rule K of this same principle?',
    'What was the problem with the four-stage model?',
    'What will the SLP often need to do?',
    'What would a language disorder produce?',
    'What would a patient with Wernickes aphasia have difficulty with?',
    'What would be characterized by misarticulation of speech sounds?',
    'What would include problems with word finding or retrieval?',
    'What would support the behaviorist view?',
    'When does the phonological process of substituting the stop /b/ for the fricative /v/ normally stop?',
    'When does the phonological process of substituting the stop /d/ for the affricate /d3/ normally disappear?',
    'When does the phonological process of substituting the stop /t/ for the fricative /f/ normally end?',
    'When is it recommended to discharge an intellectually disabled client in more recent years?',
    'When were some of the studies that researchers reviewed on this topic conducted?',
    'Where does ataxic dysarthria typically originate from?',
    'Where is apraxia localized?',
    'Where is music processed in the brain?',
    'Where is the trachea located?',
    'Which choice represents a proportion much greater than reality?',
    'Who are the best candidates for cochlear implantation?',
    'Who is at risk for velopharyngeal mislearning?',
    'Who is the palatal lift for?',
    'Who treats problems with the brain, nervous system, and spinal cord?',
    'Why are Cochlear implants generally recommended for children having profound bilateral hearing loss?',
    'Why are devocalized sounds harder for those with hearing loss?',
    'Why are the consonants /r/ and /s/ the most difficult to produce?',
    'Why are those hearing very well using hearing aids not advised to pursue serious surgery if it is unnecessary?',
    'Why are vowel sounds easier?',
    "Why can't we choose a particular intervention approach based on the results of one research study of that intervention?",
    'Why do ASHA and other national and world health organizations advocate for universal newborn hearing screenings?',
    'Why is it a disadvantage that standardized, norm-referenced tests do not allow any individualization in their administration?',
    "Why is it important to screen the child's hearing and vision?",
    'Why is the average effect found by the meta-analysis of all studies different than the effect for any individual study?',
    'Why is the period from birth to 3 years critical for children to learn language?',
    'Why might improvement of less than 20 percent after 3 months be due to chance?']
