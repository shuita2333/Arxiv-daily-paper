# 📦 其他研究 | 2026年08月31日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 1. [EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction](https://arxiv.org/abs/2608.26107)

**<font color=#1a73e8>作者：</font>** Yu Fu, Yongqi Kang, Yong Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting students' academic risk in online education is crucial for enabling timely interventions that can improve retention and learning outcomes. However, existing models often suffer from limited early detection capability and insufficient interpretability, leading to a "black-box" trust crisis that hinders their adoption in real-world pedagogical settings. To address these challenges, we propose EduRiskX, a neuro-symbolic framework that integrates a temporal Transformer-based predictor with F-Logic symbolic reasoning. The neural component models longitudinal student activity sequences using temporal attention, class-weighted loss, and dynamic weekly truncation. Acting as a data-driven expert system, an F-Logic rule base -- grounded in established educational theories (Engagement Theory and Student Integration Model) to mimic the diagnostic logic of human educators -- is constructed exclusively from the training data. The neural risk probability and the symbolic confidence score are then combined through a logistic regression-based fusion mechanism that learns the relative contribution of each signal. Experiments on the Open University Learning Analytics Dataset (OULAD) using a strict 80/10/10 student-level split show that EduRiskX achieves an accuracy of 0.900 and an F1-score of 0.894 at the end of the semester (Week 38), with an average early detection week of 9.32 and a detection rate of 94.30 percent. Compared with state-of-the-art time-series models (PatchTST, iTransformer) and common deep learning baselines (LSTM, CNN), EduRiskX yields improved recall and earlier risk identification under identical conditions. Beyond predictive performance, the F-Logic module provides structured rule-based explanations linking predictions to observable behavioral patterns and educational theories.

---


### 2. [Large Models for Battery Prognostics and Health Management: A Review and Future Roadmap](https://arxiv.org/abs/2608.26111)

**<font color=#1a73e8>作者：</font>** Jiale Liu, Huan Wang, Weicheng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Battery Prognostics and Health Management (BPHM) is critical for ensuring the safe, reliable, and cost-effective operation of batteries across electric vehicles, grid storage, and consumer electronics. Conventional BPHM approaches, including physics-based models and task-centric deep learning methods, face challenges in computational efficiency and parameterization, cross-domain generalization, dependence on extensive labeled run-to-failure data, and model interpretability. Recent Large Models (LMs), built upon Transformer architectures and self-supervised pre-training, offer a transformative new paradigm to overcome these long-standing bottlenecks. This review provides the first comprehensive survey of LM applications in BPHM, systematically examining how these models address challenges in the field. We begin by elucidating the foundational technologies enabling LMs, including Transformer architectures, self-supervised learning, large-scale multimodal datasets, and PEFT techniques. We then categorize recent progress along four critical dimensions: mitigating data scarcity, enhancing generalization and robustness, integrating domain knowledge for interpretability, and enabling system-level automation. Despite promising results, significant challenges remain across data accessibility, intelligence validation, trustworthiness, and deployment feasibility. To guide future research, we propose a roadmap focused on building collaborative data ecosystems, validating intelligence for industrial applications, enhancing trustworthiness with physics-informed designs, and enabling efficient on-device deployment. This review establishes a systematic approach to understand and advance LM-driven BPHM, providing researchers and practitioners with essential insights for developing next-generation battery management systems capable of safe, reliable, and autonomous operation throughout battery lifecycles.

---


### 3. [The Artificial Experimentalist: Discovery and Control of Self-Organizing Phenomena with Autotelic Reinforcement Learning](https://arxiv.org/abs/2608.26116)

**<font color=#1a73e8>作者：</font>** Marko Cvjetko, Benedikt Hartl, Michael Levin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing methods for exploring cellular automata and other complex systems mostly operate in open loop: they set initial conditions, execute a full simulation, and observe the outcome, without intervening during execution. We introduce a closed-loop framework based on autotelic reinforcement learning, in which an agent autonomously samples diverse goals and learns a goal-conditioned policy to intervene in a complex system through minimal, local perturbations. We instantiate this framework on Lenia, a continuous cellular automaton known for life-like self-organizing patterns, in an agentic system we call CARL, and demonstrate three capabilities. First, CARL discovers stable solitons across a wide range of Lenia update rules at a higher rate than heuristic baselines. Second, it learns to steer the movement direction of existing solitons with few interventions, showing that CARL can control self-organizing patterns, not only create them. Third, humans can use trained agents to guide solitons through maze environments in real time by specifying high-level directional commands that the agent translates into low-level interventions. Trained across diverse goals, update rules, and random initial states, the agents acquire policies that generalize zero-shot to various out-of-distribution conditions. These results suggest a path toward artificial experimentalist agents that, autonomously or with human guidance, discover and control emergent phenomena in complex systems.

---


### 4. [ElementCheck: Complexity-Aware Long-Form Text Factuality Evaluation via Sentence Elements](https://arxiv.org/abs/2608.26118)

**<font color=#1a73e8>作者：</font>** Xinming Wang, Haoran Du, Yi Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing long-form factuality evaluation relies on the decompose-retrieve-verify pipeline. However, the pipeline suffers from noise from claim decomposition and fixed verification granularity, resulting in unreliable results. We propose ElementCheck, a complexity-aware framework that verifies long-form outputs via sentence elements. Instead of uniformly decomposing sentences into atomic sub-claims, ElementCheck extracts entity pairs that are explicitly linked through verifiable connections in the original sentence as elements, and organizes these into an element graph. The graph topology provides a structural signal for estimating sentence complexity, enabling direct verification for simple sentences and targeted element-level refinement and verification for complex ones. To support fine-grained evaluation, we construct a new benchmark FastFact-Sent by mapping isolated claims from FastFact-Bench back to their source sentences. Experiments on FastFact-Sent and two domain-specific benchmarks show ElementCheck consistently improves factuality verification across five backbone models while maintaining a favorable accuracy-cost trade-off. Further analyses demonstrate that complexity-aware verification reduces unnecessary re-verification and maintains stability across different backbones.

---


### 5. [Training-Time Explainability for Multilingual Hate Speech Detection: Aligning Model Reasoning with Human Rationales](https://arxiv.org/abs/2608.26125)

**<font color=#1a73e8>作者：</font>** Muhammad Deedahwar Mazhar Qureshi, Sannaan Khan, Muhammad Atif Qureshi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online hate against Muslim communities often appears in culturally coded, multilingual forms that evade conventional AI moderation. Such systems, though accurate, remain opaque and risk bias, over-censorship, or under-moderation, particularly when detached from sociocultural context. We propose a \emph{training-time} explainability framework that aligns model reasoning with human-annotated rationales, improving both classification performance and interpretability. Our approach is evaluated on HateXplain (English) and BullySent (Hinglish), reflecting the prevalence of anti-Muslim hate across both languages. Using LIME, Integrated Gradients, Grad X Input, and attention, we assess accuracy, explanation quality, and cross-method agreement. Results show that gradient- and attention-based regularization improve F-scores, enhance plausibility and faithfulness, and capture culturally specific cues for detecting implicit anti-Muslim hate, offering a path toward multilingual, culturally aware content moderation.

---


### 6. [FIRSTPASS: A Multi-Domain, Multi-Round Peer Review Dataset Grounded in Real Editorial Outcomes](https://arxiv.org/abs/2608.26129)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Somnath Luitel, Manmeet Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific peer review datasets have trained AI systems exclusively on Computer Science and Machine Learning venues, producing models that critique ablation studies yet have never seen a biology reviewer demand contamination controls or a chemist question Nuclear Magnetic Resonance (NMR) spectral assignments. We introduce FIRSTPASS, the first large-scale peer review dataset built on complete multi-round editorial dialogues from a multidisciplinary high-impact journal. Curated from Nature Communications mandatory transparent peer review (instituted November 2022), FIRSTPASS comprises 3,668 records spanning five scientific domains (biology, chemistry, neuroscience, physics, and earth science), capturing the full iterative structure of scientific validation: initial referee reports, author point-by-point responses, and updated reviewer assessments. Each record carries an outcome label derived directly from editorial decisions (STANDARD for two-round review; EXTENDED for three or more rounds), providing ground truth absent in all prior corpora. An automated audit confirms 100% content integrity. Expert reviews average 2,155 words, substantially denser than conference venue reviews. All data, parsing pipelines, and evaluation scripts are released to enable reproducible benchmarking of AI scientific judgment across disciplines.

---


### 7. [Agent Seer: Synthesizing Scenarios from Specification Understanding](https://arxiv.org/abs/2608.26133)

**<font color=#1a73e8>作者：</font>** Harish Karumuri, Mahesh Vemula, David Lopes Pegna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating AI agents that use external tools requires realistic test scenarios that capture how practitioners compose tools and iterate across conversation turns. Constructing such scenarios by hand demands deep domain expertise, does not scale across tool ecosystems, and produces static benchmarks that cannot track evolving APIs. We observe that tool specifications -- function names, natural-language descriptions, and typed parameter schemas -- already encode sufficient semantic information to synthesize realistic evaluation scenarios without manual curation or live tool execution. Agent Seer builds off this latent information: from a single Model Context Protocol (MCP) specification, with no examples, no live tool access, and no domain-specific tuning. This pipeline enriches raw schemas, generates graded scenarios with synthetic tool outputs, and expands them into mock-data-grounded multi-turn dialogues that exhibit strong tool-calling correctness and conversational coherence.
Evaluation quality is measured by applying this pipeline on seven MCP specifications spanning diverse domains and tool-suite sizes and measuring the tool-calling correctness and conversational coherence. The pipeline achieves strong quality across all domains, with complete tool coverage on small and medium specifications. Two findings emerge within this analysis: parameter schema complexity is the strongest correlate of quality variation -- tool-suite size plays a smaller, orthogonal role -- and argument value accuracy is the dominant failure mode among imperfect scenarios, a sub-dimension invisible to coarse-grained name-match metrics.

---


### 8. [The Accuracy-Efficiency Paradox Quantifying Net Energy Loss in on-Device Energy Forecasting](https://arxiv.org/abs/2608.26134)

**<font color=#1a73e8>作者：</font>** Jaeik Jeong, Tai-Yeon Ku, Wan-Ki Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Energy forecasting aims to maximize accuracy to ensure energy efficiency by reducing energy waste, an objective that applies equally to on-device forecasting for mission-critical edge environments, including military systems. However, this paper identifies the Accuracy-Efficiency Paradox: high-precision energy forecasting models can ironically trigger a net energy deficit. This stems from both edge AI's inference energy consumption and battery aging. We propose a Total Cost of Ownership (TCO) framework for energy forecasting, designed to minimize net energy loss. This framework treats not only inference energy consumption but also battery aging as a unified form of energy loss, as degradation represents a physical dissipation of the system's future energy-carrying capacity. We demonstrate that in thermally sensitive edge environments, energy saved by the superior precision of complex architectures is often outweighed by the total energy lost through their high operational intensity.

---


### 9. [Data Science Approaches to Evaluating Honours Candidates](https://arxiv.org/abs/2608.26135)

**<font color=#1a73e8>作者：</font>** Francesca von Braun-Bates, Sunreeta Sen, Indraayudh Talukdar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a modular data-science pipeline for estimating public sentiment towards individuals from fragmented, unstructured open-source intelligence (OSINT). The method chains web search, text extraction, relevance filtering, tokenisation, co-reference resolution, and sentiment analysis to convert heterogeneous web material into auditable person-level sentiment distributions. We compare AFINN and VADER with MINOS, a domain-informed sentiment algorithm designed to detect language associated with reputational risk, misconduct, and positive public contribution. Applied to public figures with known reputational outcomes, MINOS gives the clearest separation between positive, ambiguous, and negative cases. The results show that chained NLP and OSINT methods can support transparent, reproducible, human-in-the-loop sentiment assessment for high-stakes decision support. We demonstrate the approach on the UK Honours system, where individuals are required to display high standards of public conduct to maintain an Honour.

---


### 10. [Cross-Platform Generalisation Failure in Mental Health Natural Language Processing: A Five-Axis Fairness Audit of Transformer Models on Social Media](https://arxiv.org/abs/2608.26138)

**<font color=#1a73e8>作者：</font>** Rajveer Singh Pall, Sameer Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the Cross-Platform Fairness Evaluation (CPFE) framework -- a five-axis audit protocol covering discriminative performance, calibration, statistical significance, prediction equity, and attribution stability -- and apply it to four transformer models (BERT, RoBERTa, Emotion-DistilRoBERTa, GoEmotions-RoBERTa) trained on a Kaggle mental health corpus (n=35,556) and evaluated on Reddit (n=6,257) and Twitter (n=2,883) test sets with emotion labels mapped to clinical proxies. All three independently evaluated models exhibit consistent and substantial cross-platform AUC degradation (30.3-35.4% on Reddit, 37.9-39.5% on Twitter) relative to within-platform performance (AUC 0.983-0.987), confirmed across five independent training seeds. Calibration failure is concurrent and severe: ECE rises from 0.056-0.060 in-domain to 0.196-0.229 on Reddit and 0.499-0.542 on Twitter. Platform-specific temperature scaling reduces mean ECE by 88.0% without altering discriminative performance (mean |delta AUC|<0.01), confirming separable failure modes. Prediction equity analysis reveals large cross-platform disparities (raw DI < 0.17; prior-shift-adjusted DI: 0.11-0.29 on Reddit), with equalized odds differences of 0.753-0.830 for mental health proxy classes on Reddit and 0.755-0.831 for anxiety on Twitter. Attribution stability analysis shows near-complete vocabulary divergence across platforms (Jaccard J=0 in 14/16 model-class pairs at K=10). These findings support treating cross-platform validation across all five CPFE axes as a standard requirement for mental health NLP systems in heterogeneous environments. In a single-seed fine-tuning experiment, mean AUC improved by 0.216, suggesting target-platform labels provide greater benefit as training signal than as calibration signal.

---


### 11. [Why Current XAI Is Not Enough for Arabic NLP: A Critical Survey of the Explainability Gap](https://arxiv.org/abs/2608.26144)

**<font color=#1a73e8>作者：</font>** Salima Lamsiyah, Ruslan Mitkov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) is now a major theme in NLP; however, Arabic NLP remains under-explained in three connected senses. First, there is a method gap: Arabic XAI relies heavily on a small set of post-hoc techniques such as LIME, SHAP, attention visualization, and saliency, while broader NLP XAI offers richer diagnostic, counterfactual, probing, rationale-based, and human-centered methods. Second, there is a task gap: existing Arabic XAI work is concentrated in classification tasks, especially sentiment analysis, hate/offensive language detection, fake news, and spam, with weaker coverage of generation, retrieval, translation, summarization, structured prediction, and dialogue. Third, there is a linguistic gap: many explanations identify influential tokens, but rarely explain Arabic-specific phenomena such as morphology, clitics, dialectal variation, diglossia, orthographic ambiguity, diacritics, code-switching, named entities, cultural references, or Classical and religious registers. This critical structured survey synthesizes the reviewed literature on Arabic XAI across text, speech, and multimodal settings. We argue that Arabic NLP does not only need explanations of model decisions; it needs explanations that are faithful to Arabic as a linguistic, cultural, and sociotechnical object. We introduce a taxonomy of tasks, methods, linguistic units, varieties, goals, and evaluation practices, and propose a research agenda for linguistically grounded Arabic XAI.

---


### 12. [Vagdhenu: A Vrutta (Meter) Aware Shloka-to-Chant (TTS) System for Sanskrit](https://arxiv.org/abs/2608.26146)

**<font color=#1a73e8>作者：</font>** Prathosh A P  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Vagdhenu, a vrutta (meter) aware shloka-to-chant system for Sanskrit: a text-to-speech system that maps
a metrical verse to its chanted parayana recitation at high fidelity. This is an experience report, not a new
architecture. We take an off-the-shelf flow-matching TTS backbone and a large-scale neural vocoder, and add the
components a faithful Sanskrit chant pipeline needs: a frontend that routes Sanskrit through Kannada orthography to
avoid the Hindi-style schwa deletion that Devanagari triggers in Indic models; a frontend that obeys subtle
Sanskrit phonology (visarga sandhi with its jihvamuliya and upadhmaniya allophones, the aspiration contrast of
alpaprana and mahaprana, and the dental, retroflex, and palatal sibilants kept distinct); and a vrutta-aware
mechanism that detects the meter and picks an exactly matched reference under a half-reference rule. We report a
negative result that shaped the system: in a self-infilling flow-matching backbone, a text-side prosody conditioner
is architecturally inert, because the model recovers pitch from the context mel and the embedding gets no
gradient; the reference clip and a voice-steering retrain are the only working prosody levers. We also report a
comparative lineage across four families (StyleTTS2, VITS2, Matcha-TTS, and the flow-matching backbone), where each
earlier family hit a ceiling on conjuncts or prosody that a five-hour clone cleared at an expert MOS near 4.6. The
system shipped two deployments: a 32-chapter, 5183-verse video corpus (about 17.5 hours) and an audio app covering
about 18000 verses across 12 books. We release the frontend, inference and training code, weights, a
single-speaker chant dataset, and an interactive demo.

---


### 13. [Towards Interpretable Depression Detection: Linking Acoustic Features to DSM-5 Indicators](https://arxiv.org/abs/2608.26148)

**<font color=#1a73e8>作者：</font>** Jonas Länzlinger, Katharina O.E. Müller, Burkhard Stiller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression affects millions worldwide, yet diagnosis relies on subjective self-reports that may miss authentic behavior. This paper presents an approach linking speech acoustics to DSM-5 depressive-behavior indicators through a transparent Linkage Framework. Unlike black-box models, the framework explicitly maps acoustic features (pitch variability, pauses, speech tempo) to clinical indicators, enabling interpretable, indicator-level outputs. The system runs locally on commodity hardware (HW) to preserve privacy. Preliminary evaluation on DAIC-WOZ shows directionally consistent associations between acoustic features and DSM-5 indicators for psychomotor change and concentration difficulty, supporting the design rationale. Future work will validate on longitudinal datasets and extend multimodal integration while maintaining edge constraints.

---


### 14. [Methodological and Conceptual Framework for 5D Multi-Table Analysis: A Unified Approach for Complex Data Reuse](https://arxiv.org/abs/2608.26149)

**<font color=#1a73e8>作者：</font>** Edouard Lansiaux, Hugo Kazzi, Aurélien Loison 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-table learning remains a major challenge in machine learning for healthcare and other complex information systems. Relational data combine several sources of complexity, including large data volume, high-dimensional variables, high-cardinality categorical features, complex inter-table dependencies, and repeated temporal observations. We introduce the Relational Hypergraph Transformer (RHT), a unified architecture that represents relational databases as hypergraphs, learns pentadimensional embeddings (PentE), and performs sparse relational attention with complexity proportional to the average relational degree rather than the square of the number of entities. We formally define the architecture, derive the complexity of its attention mechanism, and provide an open-source reference implementation. We evaluate RHT on the public Synthea synthetic electronic health record dataset using multi-label prediction of SNOMED CT condition codes per encounter, a task characterized by high categorical cardinality and long-tailed label distributions. Comparisons with tabular, relational, and temporal graph baselines show that RHT produces more semantically coherent embeddings while remaining computationally scalable. In this benchmark, the highest rare-code recall is achieved by XGBoost, whereas RHT attains the strongest embedding semantic coherence. We also report ablation studies quantifying the contribution of each architectural component. Clinical validation on MIMIC-IV is planned following PhysioNet credentialing. Source code and experimental protocols are provided in the accompanying repository.

---


### 15. [Explainable Artificial Intelligence for Customer Churn Prediction in Telecommunications: A Framework for CRM Integration](https://arxiv.org/abs/2608.26151)

**<font color=#1a73e8>作者：</font>** Sandeep Gaddamwar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subscriber attrition is a costly, persistent challenge for telecommunications providers, with monthly churn of roughly 1.9% in mature markets eroding billions in revenue annually. Predictive models can flag at-risk customers accurately, yet they are routinely excluded from frontline CRM workflows because high-performing ensemble and non-linear architectures are opaque: a retention specialist cannot design a personalised intervention from a probability score alone, without knowing why a subscriber is at risk. This paper addresses that gap. We benchmark four classifiers--Logistic Regression, Random Forest, XGBoost, and LightGBM--on the IBM Telco Customer Churn benchmark (7,043 records; 19 features; 26.5% churn, balanced to 50% via SMOTE on the training partition only). Logistic Regression attains the strongest AUC-ROC (0.8411) and LightGBM the highest accuracy (78.42%); all four fall within a 0.011 AUC band (0.831--0.841), and 5-fold cross-validation confirms the leading models are effectively tied. Explanations are delivered at two granularities: a global SHAP ranking identifying tenure, total charges, and month-to-month contract as the dominant churn signals, and instance-level SHAP and LIME decompositions that expose the drivers behind each prediction. Building on these outputs, we introduce a four-layer CRM integration architecture that converts risk scores and attribution vectors into tiered segmentation, maps top features to structured retention-action templates, and routes campaign outcomes into a retraining feedback loop. Targeting the highest-risk quintile is projected to cut overall churn by 3.3--5.3 percentage points, preserving an estimated $199K--$319K per campaign cycle.

---


### 16. [Selection Bias Correction in Retail Intelligence](https://arxiv.org/abs/2608.26156)

**<font color=#1a73e8>作者：</font>** Spandan Ghose Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retail intelligence often relies on monitoring popular, high-velocity products, potentially biasing economic indicators by ignoring the "long tail" of niche items. This simulation study investigates selection bias in inflation estimation and compares correction methods across diverse data-generating processes. Through 400 Monte Carlo replications spanning four scenarios--aligned step functions, smooth gradients, misaligned breaks, and polynomial relationships--we test the robustness of Inverse Probability Weighting (IPW) with five specifications against stratification with varying strata counts. Our findings reveal fundamental limits of weighting methods in retail long-tail contexts: stratification achieves superior performance in three of four scenarios, maintaining sub-0.04pp median error even when boundaries deliberately misalign with population breaks (116x advantage over IPW). However, IPW with spline propensity models wins under smooth polynomial relationships (median error 0.007pp vs. 0.013pp), demonstrating context-dependency. Critically, even an oracle IPW specification with perfect structural knowledge achieves 6.06pp error compared to stratification's 0.008pp in step-function scenarios. This reflects violation of the Positivity Assumption--a fundamental causal inference requirement--rather than IPW methodological inferiority. When selection probabilities differ dramatically (90% vs. 1%), weighting methods operate outside their theoretical design envelope. These results demonstrate that stratification provides a safer engineering choice in retail long-tail distributions with severe positivity violations.

---


### 17. [SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud Continuum](https://arxiv.org/abs/2608.26160)

**<font color=#1a73e8>作者：</font>** Viorica Rozina Chifu, Tudor Cioara, Vasile Ofrim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nowadays semantic models provide limited support for representing distributed AI workflows and their execution across heterogeneous edge, fog, and cloud environments. Therefore, AI processes and resources are often described using incompatible semantic representations, affecting the interoperability, orchestration, and reuse. To address these challenges, this paper proposes a SAREF-compliant ontology for representing distributed AI workflows across the edge-fog-cloud continuum. We extend the SAREF4SYST ontology with concepts for modeling AI pipelines, executable AI jobs, computational resources, deployment constraints, and communication relationships, providing a unified semantic model of both AI workflows and heterogeneous computing infrastructures. The ontology enables semantic interoperability, automated reasoning, and resource-aware orchestration of distributed AI applications while remaining fully aligned with the ETSI SAREF ecosystem. The ontology is evaluated using proof-of-concept smart grid energy services orchestration scenarios and validated using competency questions showing its ability to support AI workflow deployment, execution reasoning, and workload adaptation across heterogeneous edge, fog, and cloud environments. All competency questions were successfully validated using SPARQL querying and semantic reasoning. Experimental results demonstrate deployment success rates of 90-100% with average orchestration decision times below 80 ms across heterogeneous edge-fog-cloud environments, highlighting its effectiveness on ensuring semantic interoperability for distributed AI orchestration.

---


### 18. [Knowledge Cards: Structured Knowledge for AI Systems](https://arxiv.org/abs/2608.26176)

**<font color=#1a73e8>作者：</font>** Liliana Ferreira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems whose outputs inform real decisions, and increasingly consequential ones, require something that current documentation practice does not provide: a structured, inspectable representation of the knowledge they need to ground, contextualize, and reason about those decisions, ideally reviewed and signed off by a domain expert. Established documentation artefacts already capture important aspects of an AI system. Model cards describe how a system behaves, data cards describe what it was trained on, and system cards describe the risks of a deployed system. None of them addresses the layer between inputs and outputs, more precisely, the concepts a system holds, the relationships it models, and the patterns of reasoning it applies. For pattern-recognition tasks this gap is tolerable. For agentic AI, where systems act on their conclusions, it is the step that most often separates a promising proof of concept from an operational solution an organisation can rely on. This paper introduces the Knowledge Card, a structured artefact that captures validated knowledge about a single bounded concept in a form that experts can review, organisations can audit, and AI systems can reason over. For one concept, such as a specific failure mode, a compliance obligation, or a process decision, a Knowledge Card records the entities and relationships involved, the reasoning that connects them, the conditions under which that reasoning no longer holds, and the provenance of every claim, all grounded in a formal domain ontology and signed off by a domain expert. Initial prototype cards have been built in the energy and pharmaceutical domains. The schema is released as a public draft for community engagement.

---


### 19. [TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Assisted Programming Education](https://arxiv.org/abs/2608.26184)

**<font color=#1a73e8>作者：</font>** David Barron, Xiaohang Tang, Rezky Dwisantika 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI programming tutors provide scalable support, yet lack the behavioral context human tutors rely on to adapt support to learners' needs. We present TutorTrace, a dataset and behavioral abstraction pipeline that makes learners' behavioral context visible and computable in real time from low-level IDE telemetry. Across four deployments in two introductory Python courses (N=480), TutorTrace captures approximately 180K telemetry events, 13,633 behavioral segments, and 27 continuously computed metrics. From this foundation, we derive a taxonomy of learner activity before the first AI query, between consecutive queries, and across the full session, enabling systems to respond not just to what learners say, but to what they have done leading up to the help-seeking moment. In a preliminary classroom evaluation, behavior-aware prompts were associated with a decrease in intervals between queries with no independent work from 50.0% to 20.7%. As an additional demonstration of downstream utility, we evaluate TutorTrace on two held-out prediction tasks: whether a learner will query within the next 60 seconds (AUROC=.726) and whether an upcoming query reflects guided or dependent help-seeking (AUROC=.717). Together, these findings show how behavioral context can enable adaptive AI tutoring at scale.

---


### 20. [Can You Say This for Me? Speaking Up by Proxy in Co-Located Discussion](https://arxiv.org/abs/2608.26185)

**<font color=#1a73e8>作者：</font>** Yue Shen, Rehema Abulikemu, Ryan P. McMahan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equal participation in co-located discussion is important for effective collaboration, yet people often hold back when they anticipate negative interpersonal or professional consequences, especially when raising a point requires voicing it themselves. We present SecondVoice, a mixed-reality system that enables people to speak up through an embodied virtual proxy. By separating what is said from who says it, SecondVoice brings hesitant points into the live spoken discussion without putting the speaker on the spot. Using a private overlay, users specify their intent through a structured specification process rather than composing a full utterance. The system reformulates the input and voices it into the conversation through the proxy. We characterize a design space of participation channels under social risk. In a preliminary within-subject study (N = 16), we compare the complete SecondVoice system with an anonymous text-board channel across two group discussion tasks. Half of participants reported using SecondVoice for a point they did not say aloud, compared with 18.8% for the text board. Proxy-delivered points entered the spoken floor and were followed by multi-turn group engagement, which we did not observe after text-board posts. Participants described the channel as situationally valuable but identified tradeoffs around timing, ownership, and trust in reformulation.

---


### 21. [Predicting Consequences and Reinforcing Navigation Policies with Latent World Models](https://arxiv.org/abs/2608.26190)

**<font color=#1a73e8>作者：</font>** Zengmao Wang, Wei Gao, Shuhan Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models enable agents to reason about future outcomes and learn policies from their knowledge of state transition, but existing approaches primarily focus on reconstructing future observations or features, which introduces unnecessary complexity and limits their effectiveness for decision making. In this work, we propose a compatibility prediction Latent World Model (LWM) for robot navigation that predicts action-conditioned latent feature compatibility rather than reconstructing observations. Our key insight is that spatial proximity correlates with latent feature similarity, enabling action consequences to be evaluated directly in latent space. To support counterfactual training, our model leverages action sequences sampled across trajectories and learns to predict which sequences lead closer to the goal. Furthermore, we demonstrate how the learned world model can supervise policy learning from unlabeled video data and further improve policies through reinforcement learning entirely within the world model. This imagination-driven framework eliminates the need for action annotations and additional environment interaction. Extensive experiments on multiple real-world robot navigation datasets show that our approach significantly outperforms prior world model and imitation learning methods in prediction accuracy, policy learning, and real-world navigation performance. The code, pretrained models, and additional materials are available at this https URL.

---


### 22. [Structured Evidence Routing for Incident Risk Prediction from Multimodal Longitudinal EHRs](https://arxiv.org/abs/2608.26191)

**<font color=#1a73e8>作者：</font>** Animesh Agarwal, Meysam Ghaffari, Nina Fatehi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incident risk prediction from longitudinal electronic health records (EHRs) is challenging because relevant signals are multimodal, weak in isolation, and distributed across irregular patient histories. We propose structured evidence routing, a router-predictor-reviewer workflow that separates full-record access from disease-specific assessment. The router organizes the complete pre-index EHR into a compact summary and targeted evidence slices; the predictor uses this evidence to form an evidence-linked risk assessment, which the reviewer critiques. For comparison with supervised EHRSHOT baselines, we pair the routed evidence summaries with a supervised classifier readout. Across five 1-year incident diagnosis tasks, our method reaches the AUROC range of established supervised EHRSHOT baselines and remains competitive on AUPRC, while exposing a patient-specific evidence trail. Internal pre-readout ablations further suggest that routing, laboratory evidence, task guidance, and review each contribute to performance.

---


### 23. [GameWAM: A World Action Model for Video Games](https://arxiv.org/abs/2608.26200)

**<font color=#1a73e8>作者：</font>** Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern video games combine first-person perception, rapid visual changes, persistent world state, and heterogeneous native controls. Existing game agents map visual and task context directly to actions but lack explicit world dynamics modeling, whereas interactive game world models predict visual futures from supplied actions but do not serve as task policies. World-Action Models (WAMs) unify these objectives, but remain largely unexplored under the dynamics and open-ended interaction of video games. We introduce GameWAM, to our knowledge the first WAM for native closed-loop gameplay and GUI control. GameWAM jointly generates future visual observations and executable keyboard-mouse trajectories through parallel visual and action generative processes with block-causal conditioning and flow matching. To support joint world-action learning, we construct synchronized gameplay and GUI trajectories. To handle heterogeneous native control, GameWAM predicts a gameplay/GUI mode at each action step and generates actions with mode-specific prediction distributions and continuous-action normalization. For long-horizon interaction, block-cycle control predicts beyond the committed horizon, executes only a short action prefix, and replans from new observations, while fine-grained within-cycle context and hierarchical cross-cycle history preserve temporal continuity. Experiments demonstrate competitive task success with fewer executed native actions than the compared agents. We further uncover Low-Frequency Action Source Imprinting (LASI), in which low-frequency components of the sampled action source systematically steer coarse generated camera motion under fixed conditioning, revealing a source-sensitivity failure mode in generative control. Project page is available at this https URL.

---


### 24. [Agent Mesh: Reliability Primitives for Non-Idempotent Agent Delegation - Identity Adequacy and Evidence Adequacy](https://arxiv.org/abs/2608.26225)

**<font color=#1a73e8>作者：</font>** Mazhar Shaikh, Anurag Rajkumar Bombarde, Harshal Pathak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents increasingly perform bounded software tasks under an orchestrator that retries, resumes, and budgets them. The machinery such orchestrators reach for is the service mesh's: retry, timeout, and error-rate circuit breaking. We report a failure study of a production agentic software-delivery platform over 147 numbered incidents spanning 81 runs, each with a measured cost and, in most cases, a mutation proof reproducing the failure. All three assumptions those primitives rest on are violated in practice, and we quantify the consequences: a loop of fifty-four consecutive successful tool calls no error-rate breaker could see; a progress signal constant by construction, guaranteeing a false trip on the third repair round and driving one run from six of six components to three; twenty-one events accumulated across six invocations of one delegation, making a correct, idempotent component unwinnable; a misrouted failure that woke five components for a two-component fault, leaving three bystanders regressing working code; and twelve incidents in which the enforcement layer blocked correct work, the most expensive costing 107 agent turns and zero accepted writes. We find one cross-cutting cause and its dual. Identity adequacy: in five separate subsystems an identity that failed to discriminate produced a confident wrong answer, and two of them derived the corrective rule independently. Evidence adequacy: a reliability decision may be taken only on evidence capable of moving, attributable to what it measures, and deterministic under identical conditions. From the findings we derive seven reliability primitives whose enforcement unit is the delegation rather than the message, and specify the controlled evaluation the study motivates but does not constitute.

---


### 25. [Pruning Binarized Neural Networks: A Dedicated Framework and Globally Weighted Algorithms](https://arxiv.org/abs/2608.26233)

**<font color=#1a73e8>作者：</font>** Roan Rubiales, Jean Pierre David  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme compression of deep neural networks, up to full binarization, dramatically reduces memory footprint and arithmetic complexity, facilitating deployment on constrained edge hardware with field-programmable gate arrays (FPGAs) and microcontrollers. Although combining binarization with pruning promises additional efficiency gains, existing pruning strategies are ill-suited to binarized representations and rarely translate into meaningful hardware savings. We introduce a PyTorch-based, research-oriented framework that incorporates freezing and pruning mechanisms for designing and optimizing binarized neural networks. The framework enables rapid and reproducible evaluation of state-of-the-art approaches and the fast prototyping of new ones. Leveraging this framework, we propose a novel pruning method that accounts for the relative importance of learned parameters across abstraction levels. Such a global weighting mechanism consistently achieves a superior trade-off between model accuracy and pruning rate, achieving a 70% pruning rate on VGG11 with constant accuracy, while state-of-the-art results reach only 41% in the binarized setting.

---


### 26. [6.5% of the Neuro-Symbolic Literature Can Be Reproduced from Its Published Artifacts, a Six-Stage Audit Framework and First Instantiation](https://arxiv.org/abs/2608.26236)

**<font color=#1a73e8>作者：</font>** Brandon Colelough, Vladimir Martirosyan, Ishan Tamrakar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a six-stage framework for auditing the reproducibility of scientific claims across a research literature within the computer science domain, and instantiate our framework for the neuro-symbolic AI (NSAI) subdomain. Instantiating the framework on the NSAI subdomain produced a multi-year audit. Stage one retrieved 5,497 records and removed 3,018 duplicates. Stage two screened the 2,479 unique records at title and abstract, identifying 1,365 self-identified NSAI records, then removed a further 61 at full text for off-topic, non-research, no-quantitative-evaluation, or inaccessible-full-text reasons. Stage three sought a verifiable public code artifact for each of the 1,304 eligible records and found none for 849, leaving 455 to enter the artifact inventory and bounded rerun of stages four and five. We fully or partially reproduced 85 studies, 6.52% of the eligible corpus and 18.68% of attempted reruns. We found that 321 attempted reruns were blocked by missing non- code artifacts and 42 by missing or unusable code repositories. These figures quantify a persistent reproducibility deficit that survives even nominal "code available" declarations, and signal the need for enforced, versioned, and permanently archived artifact bundles in future NSAI publications. We argue that empirical NSAI papers should be required at submission time to provide complete, versioned, and permanently archived artifact bundles.

---


### 27. [Algebraic Multigrid Acceleration for Efficient Label Spreading](https://arxiv.org/abs/2608.26309)

**<font color=#1a73e8>作者：</font>** Antonia van Betteray, Jonathan Klees, Miriam Schäfers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning models rely on large amounts of labeled data. However, manual annotation of large-scale datasets is expensive and time-consuming. Label spreading is a semi-supervised learning technique that addresses this challenge by propagating information from a few labeled examples to a larger pool of unlabeled data. Despite its effectiveness, its application to large-scale, high-dimensional datasets is limited by computational costs and memory constraints. To address these limitations, we propose Algebraic Multigrid Acceleration for Efficient Label Spreading (AMELS), an efficient label spreading framework that improves scalability by fast construction of neighborhood graphs and the incorporation of algebraic multigrid solvers. The latter is an iterative solver that replaces the ordinary random walk iteration typically performed in label spreading. Due to the multilevel nature of algebraic multigrid solvers, AMELS spreads given label information across a graph of any size in a single multigrid cycle. We demonstrate that AMELS achieves significant runtime reductions compared to existing implementations while also being more robust to hyperparameter choices in terms of both runtime and classification accuracy. Our framework therefore enables efficient label spreading on large-scale image datasets and produces accurate labels even when only a few labeled samples are available.

---


### 28. [Calibration-Free Cuffless Blood Pressure Estimation Using Multimodal ECG-PPG Fusion on a Google Pixel Watch](https://arxiv.org/abs/2608.26325)

**<font color=#1a73e8>作者：</font>** Jathushan Kaetheeswaran, Boyi Ma, Ali Abedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Inadequate blood pressure (BP) monitoring and management outside of clinical settings can worsen major cardiovascular risk factors such as hypertension. While cuff-based devices are commonly used for at-home monitoring, these devices can be inconvenient for daily use due to their sensitivity to body positions, upper-arm constrictions, and limited portability. A promising alternative is emerging in the form of consumer-grade smartwatches, where physiological signals related to cardiac activity can be used to estimate BP non-invasively and continuously across daily living conditions. In this work, we use data collected from a Google Pixel Watch in 40 participants to develop and compare several algorithm approaches for BP estimation. We found that our proposed deep learning model achieved the strongest overall performance, and that fusing smartwatch signals with demographic information improved model generalizability to unseen individuals. However, we also identified that model accuracy was not consistent across participant subgroups, with obese individuals yielding higher estimation errors than others. This study highlights the feasibility of consumer-grade smartwatches as accessible platforms for deploying robust BP estimation algorithms, though clinical reliability will require larger, more diverse populations and additional sensing modalities.

---


### 29. [ProofEvolve: Neuro-Symbolic Evolution for Formal Automated Theorem Proving](https://arxiv.org/abs/2608.26334)

**<font color=#1a73e8>作者：</font>** Wenqian Ye, Ziwei Guan, Eric Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated theorem proving offers a natural foundation for recursive self-improvement in scientific discovery. However, existing neural provers do not fully preserve this recursive structure, where the learning process should be self-improving over time. Existing methods either embed proof experience into model parameters through expensive weight updates, or keep verified intermediate deductions only within the current problem. In addition, these methods also heavily rely on sparse whole-proof feedback, even when unsuccessful partial attempts contain useful discoveries. To close the gap, we propose ProofEvolve, a neuro-symbolic framework that evolves explicit, formally verified symbolic proof structures with neural models to decisively expand the knowledge boundary. In this framework, the neural model proposes variation operators, including decompositions, repairs, and schema recombinations. The symbolic Lean kernel verifies every proof transition. Over the evolution loops, ProofEvolve computes verified closure over the resulting proof directed acyclic graphs (DAGs). Within each problem, ProofEvolve evolves partial AND-OR proof DAGs in a behaviorally indexed archive. Across problems, kernel-checked schema extraction adds newly proved sub-DAGs to a persistent schema library. Proof DAGs inherit the solved results through typed schema recombination, with every residual premise exposed as a new subgoal. This evolutionary process preserves verified results from incomplete attempts and makes them available for later proofs without weakening formal soundness. Across three competition-level Lean benchmarks, ProofEvolve achieves the highest average solve rate among the evaluated proof systems.

---


### 30. [MoganColBERT-TR: A Late-Interaction Multi-Vector Retrieval Model for Turkish](https://arxiv.org/abs/2608.26344)

**<font color=#1a73e8>作者：</font>** Furkan Yilmaz, Habibe Aleyna Tasdemir, Muhammed Faruk Gozay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We previously reported a ModernBERT encoder trained from scratch for Turkish (MoganBERT-TR) and a single-vector embedding model built on top of it (MoganBERT-embed). This work introduces the third model in that lineage: MoganColBERT-TR, a multi-vector retrieval model that, instead of compressing a query or a document into a single vector, represents it at the token level through a 768->128 projection and scores it with MaxSim late interaction. The model is not trained from scratch: the embedding model's encoder is taken as the starting point and adapted to the ColBERT objective with a single-epoch distillation phase. Training data is produced from two sources - title-to-passage pairs carved out of our own pretraining corpus in the character domain and at sentence boundaries, and two Turkish question-based retrieval sets - and is distilled from the soft scores of a cross-encoder teacher (bge-reranker-v2-m3) over one positive and seven mined negatives. We show that in hard negative mining, rank-based skipping alone is insufficient and must be combined with a group mask and a cosine ceiling. Evaluation is carried out with the official pipeline of TurkColBERT, a benchmark built for Turkish late-interaction retrieval (PLAID index, exact MaxSim), on five Turkish BEIR datasets; none of them appears in our training pool, so all five results are clean zero-shot. With 148.9M parameters, MoganColBERT-TR reaches an overall score of 37.36 (35.53 nDCG@100, 31.81 nDCG@10) averaged over the five datasets and finishes second among the five models compared: it outperforms the twice-as-large ColmmBERT-base-TR on four of five datasets and by +3.05 overall, and the benchmark's largest model by +12.30. The gap to the leading model (mLateOn) is concentrated on ArguAna-TR, the dataset with by far the longest queries.

---


### 31. [Kale: A Transformation-Safe Spreadsheet System](https://arxiv.org/abs/2608.26345)

**<font color=#1a73e8>作者：</font>** Michael Coblenz, Jacob Yim, Ajinkya Bokade 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spreadsheet formulas can refer to rectangular ranges of arbitrary size. When a user changes the structure of a referenced table, the spreadsheet system updates the references to refer to a new range. Unfortunately, this new range may differ from the user's expectations, introducing bugs in spreadsheets. We describe a user study showing that standard reference semantics are error-prone, resulting in significant risk to users. We introduce Kale, a prototype system that eliminates the risk of inserting these kinds of bugs by restricting the kinds of references that can be expressed. We show that Kale can be used effectively by users to complete tasks that are error-prone in traditional spreadsheet systems. Finally, we describe a corpus study that evaluates the extent to which the reference restrictions in Kale might have implications on users.

---


### 32. [Decolonial Discourse in Postcolonial Contexts: How YouTubers Negotiate Audience Tensions, Platform Governance, and State Influence](https://arxiv.org/abs/2608.26351)

**<font color=#1a73e8>作者：</font>** Dipto Das, Bryan Semaan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Decolonial discourse on online platforms is often framed in terms of creator motivations and expressive possibilities. In this paper, we examine what it takes to sustain such discourse under layered sociotechnical constraints. Drawing on semi-structured interviews with YouTubers engaging in Bengali decolonial discourse, we analyze how audience publics, platform governance, and state influences shape what becomes sayable, visible, and viable. We show how fragmented postcolonial identities among audiences produce legitimacy policing, harassment, and coordinated backlash, requiring ongoing relational labor from creators. At the platform level, differential monetization, opaque moderation, and copyright regimes reorganize which publics are economically viable and reinforce existing hierarchies. Further, intermediaries such as multi-channel networks mediate regulatory pressure, introducing political risks and constraints on participation. In response, content creators engage in strategies of negotiation, including boundary work, infrastructural improvisation, and multi-platform distribution. Overall, our findings highlight the layered dynamics of decolonial discourse in postcolonial contexts and the continuous work required to sustain it in platformed environments.

---


### 33. [FRESCO: Complete and Scalable Temporal Safety for CHERI Application Processors](https://arxiv.org/abs/2608.26353)

**<font color=#1a73e8>作者：</font>** Merve Gülmez, Nils Jordan, Jialun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> CHERI provides hardware-enforced spatial memory safety. While prior work extends it with heap temporal safety, stack use-after-return remains unaddressed. Existing defenses fall short: compiler analysis reliably catches only references that escape as function return values, while dynamic sanitizers impose overheads that preclude production deployment.
We present FRESCO, built on the principle that a stack capability must not outlive the frame that created it. FRESCO "colors" the stack pointer with per-invocation provenance identifiers; every capability derived from it inherits that lifetime and is hardware-invalidated the moment the function exits, regardless of how or where it escaped.
Because stack frames retire orders of magnitude more frequently than heap allocations, FRESCO manages the resulting color pressure through: 1) Color Saver, a static capability-aware escape analysis that confines coloring to functions needing it, and whose core algorithm we mechanically verify in Rocq, and 2) capability-color segmentation, which partitions memory into disjoint segments, each with an independent color namespace. Color segmentation lets stack and heap temporal safety coexist on one system, making FRESCO the first hardware/software co-design to provide complete and scalable temporal safety for CHERI application processors.
We realize FRESCO on the CHERI-RISC-V QEMU full-system emulator and the out-of-order CHERI-Toooba FPGA softcore, with software support in the CHERI-enabled Clang/LLVM compiler and CheriBSD OS. FRESCO systematically prevents use-after-return, use-after-free, and double-free across the NIST Juliet Test Suite and CVEs, with only a small run-time overhead in SPEC CPU (4% g.m.), SQLite, and PostgreSQL (10-14%).

---


### 34. [A Unified Framework for the Mechanics of Information in Convolutional Neural Network Image Space](https://arxiv.org/abs/2608.26363)

**<font color=#1a73e8>作者：</font>** Aryan Shukla, Matthew Toews  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a unified mathematical framework for modeling information propagation through convolutional neural networks (CNNs), with the aim of connecting descriptions of physical space and information space.
A correspondence is presented linking discrete filter symmetry and the relativistic energy--momentum relation under the widely used nonlinear rectified convolution operation. Specifically, symmetric filter components (e.g. the sum $\Sigma = [1,1]$) operate analogously to rest energy $mc^2$ in preserving the image centre of mass (e.g. isotropic diffusion), whereas antisymmetric components (e.g. the gradient $\nabla = [-1,1]$) operate analogously to the momentum term $pc$ in generally inducing a displacement (e.g. vibration or translation). For typical small discrete filters, this displacement is determined by the ratio of antisymmetric to total filter energy, analogously to how the displacement of a relativistic particle relates to a Lorentz transform with beta parameter $\beta = \frac{v}{c}=\frac{pc}{E}$ equal to the ratio of momentum $pc$ to total energy $E$.
Repeated filtering leads to the Gaussian scale-space and emergent scale-invariant features. These constructions share a Laplacian-driven structure with the classical heat (diffusion) equation and, via standard mathematical correspondences, with the Schrödinger equation and aspects of the Friedmann equations, together with emergent Morse topological structure. Demonstrations in 3D images reveal blob-like, scale-invariant Morse critical points in images spanning a wide range of physical scales, including organic sugar molecules and inorganic silicon crystals, human and primate brains in magnetic resonance images (MRI), galaxies and the cosmic microwave background (CMB).

---


### 35. [PRISM: Lightweight Enclave Isolation with Prismatic Capabilities](https://arxiv.org/abs/2608.26367)

**<font color=#1a73e8>作者：</font>** Merve Gülmez, Adam Caulfield, Hakan Englund 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted execution environments (TEEs) protect sensitive code and data from external interference, but lack inherent memory safety. CHERI can enforce spatial memory safety at the object level. Attempts to establish a TEE using CHERI primitives suffer from (1) expensive capability revocation operations, (2) need to rely on the host operating system (OS) to support provenance tracking and physical memory protection, (3) expensive domain transitions, and (4) lack of support for remote attestation.
We introduce prismatic capabilities and present PRISM, a TEE architecture for CHERI leveraging prismatic capabilities to create userspace enclaves while addressing these challenges. PRISM binds enclave 'hues' (identifiers) in prismatic capabilities to physical memory access controls, enables O(1) ownership establishment without memory sweeps, and supports efficient domain transitions that atomically activate and deactivate prismatic capabilities. Additionally, PRISM enables remote attestation of its enclaves. We demonstrate that execution of userspace enclaves in PRISM incurs only moderate overhead (<= 15%), a significant improvement over the same workloads under Intel SGX

---


### 36. [CG4AI: A Column Generation Framework for Training AI Models Under Constraints](https://arxiv.org/abs/2608.26375)

**<font color=#1a73e8>作者：</font>** Youcef Magnouche, Abderrahmane Driouch, Sébastien Martin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard machine-learning training minimizes a loss function over a dataset, but does not guarantee that the resulting model will satisfy predefined rules or constraints on its outputs. In many real-world applications, ranging from autonomous systems to network routing, such guarantees are essential. We propose CG4AI, a framework that builds a convex combination of AI models while enforcing linear constraints on the combined output. A master linear program (LP) determines the optimal mixture weights, while a pricing subproblem generates new models guided by LP dual variables, focusing attention on the most violated constraints. A cutting-plane procedure extends feasibility guarantees beyond the training set. We apply CG4AI to two problems: (i) digit classification on MNIST, where we demonstrate four distinct uses of constraints, learning from constraints alone, improving adversarial robustness, correcting misclassified examples, and enforcing output relabeling; and (ii) the multi-commodity flow problem, where link capacity constraints are enforced on neural-network routing predictors. Experiments on MNIST and standard SNDLIB benchmark networks show that CG4AI reliably produces feasible predictors while achieving better accuracy than single-model baselines.

---


### 37. [Improving the Robustness of the XRP Ledger Network via Edge Augmentation Strategies](https://arxiv.org/abs/2608.26380)

**<font color=#1a73e8>作者：</font>** Afonso Vilalonga, Orkun İrsoy, João S. Resende 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The XRP Ledger allows its network participants to select a set of trusted peers within the network (i.e., the Unique Node List (UNL)) and communicate with them to reach consensus on which transactions should be included in the next ledger state. However, its consensus protocol requires significant overlap among participants' UNLs, along with a high agreement threshold among the nodes within each UNL (e.g., 80\%). Consequently, an attacker could disrupt the consensus process in such a network by targeting the nodes that form the network's connectivity backbone and reducing the number of trusted participants that can communicate with one another below the required threshold. In this paper, we evaluate strategies to improve the robustness of the XRP Ledger's existing topology, as measured by our formal definitions of quorum and network robustness, and compare them to a second strategy from prior work. The strategy we present is an addition/augmentation approach, in which new edges are added based on different constructions. The second strategy is a rewiring or edge-replacement approach, in which the overall number of edges is preserved but they are rearranged. For each strategy, we consider two different cases: one in which all nodes participate in the edge construction or rewiring process, and another in which only a subset of nodes participates. Our findings demonstrate substantial improvements in robustness when augmentation strategies are used over the default XRP Ledger topology and show that some augmentation strategies achieve robustness metrics equal to or exceeding the rewiring strategy, even when the number of edges added is small (e.g., three edges per node). Additionally, we show that the random K-out-based augmentation strategy maintains higher topological similarity to the original network than rewiring, as measured by Jaccard similarity.

---


### 38. [Case2Flow: Bridging Patient Cases and Guideline Flowcharts through Multimodal Retrieval](https://arxiv.org/abs/2608.26414)

**<font color=#1a73e8>作者：</font>** Jiale Wei, Yufan Chen, Alexander Jaus 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical guidelines encode rich, evidence-based decision logic, yet the specific decision artifact a clinician needs is hard to locate within a guideline, let alone across guidelines covering plausible diseases and treatments. While guideline passages have supported end-to-end question answering, flowcharts remain largely underused in decision support despite their ability to encode actionable clinical pathways. We therefore introduce Case2Flow, a task designed to retrieve the most relevant guideline flowchart for a given patient case from a collection of guideline documents. To support it, we construct FlowAtlas, a curated corpus of 202 flowcharts extracted from 2,080 medical guidelines, together with a pipeline that synthesises 1,911 aligned case-flowchart pairs. Our evaluation of multimodal retrieval methods reveals systematic failure modes, including overreliance on keywords and spurious token-patch matches induced by uninformative background regions in flowcharts. Motivated by this, we propose CRISP, a training-free scoring method that sharpens late-interaction retrieval by suppressing uninformative patches, discounting ambiguous token matches, and incorporating bidirectional query-image alignment. CRISP improves Recall@1 by up to 18.71 percentage points, while a blinded physician assessment on published case narratives provides preliminary feasibility evidence beyond synthetic queries.

---


### 39. [IoMT-SecAlarmBench: A Counterfactual Benchmark for Integrity Attacks in IoMT](https://arxiv.org/abs/2608.26416)

**<font color=#1a73e8>作者：</font>** Emmanuel C. Ugwuabonyi, Dmitri Perkins  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Medical Things (IoMT) combines clinical physiological data with cyber-system information, creating challenges in determining whether an abnormal reading reflects a genuine physiological event, a device fault, or a cyber-attack within the expected physiological range. Answering this requires counterfactual ground truth, which no existing dataset provides. We present IoMT-SecAlarmBench, a semi-synthetic benchmark that injects controlled integrity attacks into genuine coupled ECG+PPG recordings using a structured experimental design combining four attack morphologies, four severity levels, two physiological plausibility conditions, and replay attacks. Each injected window retains its cause, attack subtype, and the clean signal that would have been observed without the attack. We evaluate six detectors from five method families using threshold-independent measures and a matched false-alarm budget. Results show no method consistently detects the most difficult cases: replay attacks and low-amplitude transient spikes remain close to chance-level performance across detectors. Results also reveal a trade-off between detecting attacks and distinguishing them from sensor faults: the best-performing detector on hard cases flags fault/artifact windows at 5.3 times its false-alarm rate on normal data. Three-way classification performs poorly for genuine physiological events, and a leakage audit of a dual-modality network dataset indicates previously reported IoMT intrusion-detection performance is partly driven by identifying information. Benchmark, generation code, preprocessing, evaluation tools, and datasheet are released.

---


### 40. [Fine-Tuning of Transformer models with Frames](https://arxiv.org/abs/2608.26430)

**<font color=#1a73e8>作者：</font>** Harshavardhan Adepu, Li Zhang, Sanjiv Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) strategies such as Low-Rank Adaptation (LoRA) are effective solutions for fine-tuning large-scale pre-trained models; however, their memory requirements scale with the size of the model, $\mathcal{O}(dr)$, where $d$ is the model's hidden dimension and $r$ is the rank. Our proposal, FrameFT, models the parameter update $\Delta W$ with a sparse coefficient matrix in a Fusion Frame basis. Fusion Frames can be generated algorithmically and shared across model layers, enabling very efficient updates. Only the sparse coefficients of the basis expansion are stored/optimized, reducing the memory footprint. The sparse structure of the coefficient matrix in FrameFT and the sparsity in the Fusion Frames give large compute benefits, and our analysis provides formal convergence results. We evaluate the idea across a suite of supervised fine-tuning benchmarks, focusing on language tasks, but also report application to vision models. Our experiments show that FrameFT achieves performance on par with/exceeding state-of-the-art PEFT techniques, but needs far fewer trainable parameters.

---


### 41. [FedCMAPSS: A Benchmark for Federated Learning in Remaining Useful Life Estimation](https://arxiv.org/abs/2608.26433)

**<font color=#1a73e8>作者：</font>** Amelia Sorrenti, Matteo Pennisi, Concetto Spampinato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven prognostics and health management has emerged as a key enabler for Industry 4.0, yet the development of robust remaining useful life (RUL) estimation models is often limited by the scarcity of run-to-failure data. While federated learning offers a promising paradigm to collaboratively train predictive models without sharing sensor data, research efforts have operated so far in the absence of a common evaluation framework. To address this gap, this paper introduces FedCMAPSS, a benchmark for federated RUL estimation based on the commonly-used NASA C-MAPSS dataset. We define a set of five standardized tasks designed to simulate real-world industrial challenges, ranging from ideal IID settings to extreme statistical heterogeneity, and conduct a systematic evaluation of state-of-the-art federated optimization algorithms across multiple neural architectures. By establishing reproducible baselines and making the source code and data splits publicly available, this work aims to provide a standard foundation for developing and comparing federated predictive maintenance solutions.

---


### 42. [AfriSwitch: A Benchmark for In-the-Wild African Code-Switched Speech Recognition](https://arxiv.org/abs/2608.26434)

**<font color=#1a73e8>作者：</font>** Gabrial Zencha Ashungafac, Busayo Awobade, Tobi Olatunji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching is pervasive in bilingual African conversation, yet most ASR systems assume monolingual input and are evaluated on curated monolingual benchmarks. We present AfriSwitch, a 61.36-hour human-transcribed benchmark of in-the-wild code-switched speech spanning 16 African languages and language varieties, released with switch-level English span tags, perutterance Code-Mixing Index (CMI), and switch-point counts. Corpus statistics show that mixing behaviour varies widely across African languages along two largely independent axes: how often speakers alternate, and how balanced the mixture is. No single scalar captures how code-switched a language is. Benchmarking five open and commercial multilingual ASR systems zero-shot yields word error rates far above published monolingual figures for the same languages, with the best system averaging 35.93% WER and no system falling below 24% on any language. Africa-targeted training, not model scale or nominal language coverage, best predicts performance.

---


### 43. [NeoTriFuse: Reliability-Aware Multimodal Fusion under Missingness Heterogeneity for Neonatal Mortality Risk Prediction](https://arxiv.org/abs/2608.26436)

**<font color=#1a73e8>作者：</font>** Jiyuan Tian, Qincheng Shen, Ye Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neonatal mortality risk prediction from bedside monitoring data remains challenging due to extreme class imbalance, heterogeneous clinical risk factors, multi-scale temporal dynamics, and substantial missingness. We propose NeoTriFuse, a reliability-aware multimodal fusion framework for missingness-heterogeneous neonatal monitoring data. Unlike conventional multimodal approaches that treat missingness primarily as a preprocessing issue, NeoTriFuse models missingness as an explicit reliability signal that dynamically modulates modality contributions during fusion. The framework integrates static perinatal variables, local-global temporal encoders, and patient-level statistical summaries through reliability-guided gating mechanisms, while jointly optimizing mortality prediction and an auxiliary length-of-stay objective. NeoTriFuse achieves competitive performance, with an F1 score of 0.6736 +/- 0.0216 and an AUROC of 0.9454 +/- 0.0056. Ablation studies indicate that the local-global temporal architecture and patient-level summary branch contribute most substantially to predictive performance, while reliability-aware gating provides additional improvements on threshold-dependent metrics under heterogeneous observation completeness. Sensitivity analyses further suggest stable performance across nearby hyperparameter settings. Overall, the findings support reliability-aware multimodal fusion as a practical approach for neonatal mortality prediction under realistic clinical missingness conditions.

---


### 44. [Subgraph Filtering for Fair Graph Neural Networks](https://arxiv.org/abs/2608.26437)

**<font color=#1a73e8>作者：</font>** Haohui Lu, jiyuan Tian, Fangyu Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) can exhibit unfair behavior even when sensitive attributes are excluded from node features, because graph topology and message passing propagate group-correlated signals under sensitive homophily. Existing fairness-aware GNN methods mainly constrain representations or prediction distributions at a global level, without explicitly controlling the local structural pathways through which biased information propagates during aggregation. We propose Subgraph Filtering for Fair Graph Neural Networks (SF-GNN), a lightweight and architecture-agnostic framework that mitigates structural bias at its source. SF-GNN identifies bias-prone edges by combining sensitive homophily with structural propagation amplifiers, including hub participation and triadic closure. It then incorporates stochastic edge filtering into each message-passing step to selectively downweight or remove these edges while preserving the remaining graph structure. Training further incorporates a statistical-parity regularizer with a warm-up schedule to stabilize optimization. Experiments on five benchmark datasets show that SF-GNN achieves consistent fairness improvements while maintaining competitive predictive performance, leading to a better fairness--accuracy trade-off than recent fairness-aware GNN baselines.

---


### 45. [Toward Equitable Low-Carbon Mobility: Fairness-Aware Demand Prediction for Expanding Bike-Sharing Systems](https://arxiv.org/abs/2608.26451)

**<font color=#1a73e8>作者：</font>** Man Luo, Yixuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bike-sharing systems are an important component of low-carbon urban mobility, but continued expansion creates challenges in both cold-start prediction and equitable resource allocation. Newly deployed stations lack historical ridership records, causing a mismatch between training and inference for graph-based models on evolving networks. Historical demand may also encode structural inequalities, as lower ridership in low-income neighborhoods can reflect limited infrastructure access rather than weak latent demand. Models trained directly on such data may therefore reinforce existing mobility disparities. We propose FairGIN, a fairness-aware graph neural network for demand prediction in expanding bike-sharing systems. FairGIN integrates three components. Expansion-Simulated Increment Training stochastically simulates network expansion during training to reduce the cold-start distribution gap. Attention-Based Knowledge Transfer combines station-adaptive temperature scaling with orthogonal embedding alignment to transfer representations from data-rich existing stations to data-sparse new stations. Fairness-Aware Optimization introduces income-stratified regularization and an equity-calibrated deployment score to support more inclusive station placement. Experiments on NYC and Seattle demonstrate that FairGIN achieves state-of-the-art predictive accuracy across diverse expansion scenarios while substantially reducing income-based disparities without compromising overall system efficiency.

---


### 46. [Distributed Training using an Intelligent Network](https://arxiv.org/abs/2608.26453)

**<font color=#1a73e8>作者：</font>** Nihar Shah, Ben Blier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed training across a wide area network (WAN) is challenging, as continuous parameter exchange by islands of compute is constrained by limited bandwidth, high latency, and uneven topology. We propose making the network an active participant in training. On the systems side, such networks should leverage (i) multicast technology to replicate outbound traffic and (ii) in-line FPGAs to aggregate inbound traffic, to ease egress and ingress bottlenecks. These technologies are used for training across workers within a data center, but this paper extends them to the WAN. On the algorithms side, we develop an optimization framework that produces rich synchronization schedules (namely, rotating cliques of islands) around the underlying network topology and these technologies, to maximize information exchange. Finally, we illustrate this on a nine-city topology modeled on the DoubleZero network, a live programmable WAN equipped with both technologies, and show how the optimal schedules shift with the network's capabilities. Together, these can narrow the gap to the gold standard of colocated training.

---


### 47. [Compositional Generalization via Structural Identification in a Category-Theoretic Framework](https://arxiv.org/abs/2608.26465)

**<font color=#1a73e8>作者：</font>** Akihiro Maeda, Thomas Seiller, Yohei Oseki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compositional generalization is usually evaluated through model accuracy. We instead ask which structural or lexical identifications make held-out COGS examples admissible from the structures observed in training. Sentences are represented as functors from syntactic addresses to lexical tokens, and selective collapses induce Kan extensions that propagate observed associations. Across 21 COGS generalization types, admissibility follows distinct identification profiles, while residual failures separate unsupported structural templates. These data-side diagnoses characterize what the training corpus licenses under specified identifications, without training a predictive model.

---


### 48. [Active Curriculum Refinement for Reinforcement Learning](https://arxiv.org/abs/2608.26469)

**<font color=#1a73e8>作者：</font>** Zhenya Liu, Yuxin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many reinforcement learning (RL) domains, environments are connected by prerequisite relations, such as difficulty-increasing edits or parameter increments, which induce a directed acyclic curriculum graph (DAG). Although this structure is often exploited only implicitly, explicitly modeling it can improve training. We introduce PATH, a curriculum-learning framework that performs active learning over the curriculum graph. PATH first expands coverage by sampling diverse curriculum paths and then reallocates training toward regions that remain unmastered. Experiments across diverse environments show that PATH explicitly leverages the graph structure to achieve strong robustness and generalization.

---


### 49. [Mapping Woody Vegetation from Multi-Source Imagery and Prediction Fusion for Enhanced Data Efficiency and Accuracy](https://arxiv.org/abs/2608.26471)

**<font color=#1a73e8>作者：</font>** Kal Backman, Jared Wood, Adam Roff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tree cover maps are a fundamental remote sensing product, used to derive ecological insights about the landscape and are essential to change detection, vegetation mapping and fire monitoring programs. However, comprehensive tree cover mapping requires reliable and high-quality imagery, free of cloud and weather defects to ensure accurate model outputs. Deep learning approaches can generate high quality maps with minimal human intervention but require large amounts of human annotated data to be successful. In this work we propose a framework consisting of methods that aim to improve the data efficiency and robustness of deep learning models using data fusion techniques to segment woody vegetation defined as vegetation over the height of 2m across the state of New South Wales, Australia. To improve robustness against varying image quality, we propose an image composition method that normalizes the imagery and removes defects, whilst also minimizing the reliance on individual image quality by proposing a prediction fusion method. The two methods resulted in an error reduction of 38.2% and 53.6% respectively compared to single-source imagery. To address deep learning approaches' limitation of requiring large amounts of data, we apply label transfer to multiple sources of imagery as a form of data augmentation to improve data efficiency. Learning from multiple image sources was shown to be the biggest improvement in performance, resulting in an error reduction between 28.1% to 76.2% across the different validation experiments, whilst reducing the standard deviation of performance across image dates by a factor of 13.

---


### 50. [Zero-Shot Video Restoration and Enhancement with Text-to-Image Latent Diffusion Models and Multi-Modal References](https://arxiv.org/abs/2608.26476)

**<font color=#1a73e8>作者：</font>** Cong Cao, Huanjing Yue, Xin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot image restoration methods with text-to-image latent diffusion models have achieved great success in universal image restoration tasks without training. However, applying them to video restoration will result in severe temporal flickering. In this paper, we propose a novel framework for zero-shot video restoration and enhancement which uses a text-to-image latent diffusion model and multi-modal references. Through the proposed dual prompt tuning inversion and sampling, the inference time can be reduced to nearly 1/3 of the original. The performance and temporal consistency can be also significantly stregthened. By using the proposed texture-aware video token merging, the temporal correlation between frames can be further utilized to improve the temporal consistency. We futher propose the referenced self-attention and referenced token merging to support image reference. Experimental results demonstrate the superiority of the proposed method in restoring and enhancing temporally consistent videos.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
