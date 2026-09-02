# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 1. [DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://arxiv.org/abs/2608.28590)

**<font color=#1a73e8>作者：</font>** Fan Liu, Hao Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Existing data-science agents often leave this harness implicit, making results difficult to reproduce, compare, and attribute across heterogeneous tasks. We introduce DS-Lighting, a unified harness toolkit that makes harness design explicit for data-science automation. DS-Lighting decomposes the harness into four reusable layers: data, workflow, execution, and evaluation, and represents diverse agents as executable operator programs that support both predefined pipelines and adaptive search. We further integrate multiple open-source data-science benchmarks into an MLE-Bench-style task format, enabling controlled comparison under a shared task interface, sandboxed runtime, and metric protocol. Experiments across agents, harnesses, models, and ablations show that explicit harness design improves reproducibility, comparability, and reliability, while reducing avoidable system-level failures in end-to-end data-science workflows. Our code is available at this https URL

---


### 2. [Expert-validated STEM QA](https://arxiv.org/abs/2608.28591)

**<font color=#1a73e8>作者：</font>** Kihwan Han, Saurabh Patil, Chinmayee Shukla 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in AI are helping scientists achieve breakthroughs in fields such as mathematics, medicine, and materials sciences. New evaluation datasets for AI models contribute to such advancement in AI. In the STEM domain, frontier models have consumed most of the available online data, creating the need for human-created datasets that codify the knowledge of leading experts in the domain. There are several STEM datasets available for the research community in this field. However, there are some gaps in these datasets, leaving room for improvement. Examples of gaps include (1) saturation in model performance on these datasets, leaving no head-room for meaningful evaluations, (2) skewed taxonomy distributions, (3) multiple choice question format that is misaligned with how scientists use AI in the real world, and (4) inaccurate answers and rationales partially led by a contest-based data collection and a time-bound review process. In this study, we present 'Expert-validated STEM QA', a high-quality, expert-validated STEM dataset (N=398) in Physics, Chemistry, Biology, and Mathematics, created by 241 domain experts. We (1) carefully designed a taxonomy with balanced distribution, (2) vetted question contributors with quality-driven incentive, (3) conducted multiple rounds of reviews with revisions validated by domain experts based on consensus, and (4) created the dataset in verifiable question and answer format. Our study demonstrated low performance ($<25\%$) of frontier AI models on the dataset as a benchmark. Post-training on a separate, private version of the dataset (N=2,000) increased performance of the open source model by $15\%$ relative to the baseline model (p=0.045) on the STEM subset of HLE-verified dataset, indicating potential utility of the dataset for model training. We have open-sourced a portion of our dataset for the AI research community.

---


### 3. [From Question-First to Analyst-First: Domain-Expert Skills and Verified Knowledge Compilation for Proactive Enterprise Analytics](https://arxiv.org/abs/2608.28594)

**<font color=#1a73e8>作者：</font>** Harmohit Singh, Rahul Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational analytics systems assume the user already has a well-formed question, leaving a non-expert facing a blank query box on an unfamiliar enterprise schema. Commercial 'proactive' tools narrow this gap only by detecting statistical anomalies over analyst-curated metric layers, and academic next-question recommenders depend on query logs that a fresh dataset lacks. We describe a production analytics system that inverts the interaction model from question-first to analyst-first through two coupled architectural ideas. First, a pluggable domain-expert 'skill' abstraction: a folder-based, database-free subject-matter pack (a manifest, per-stage prompt facets, keyword-routed references, report templates, and optional compute) auto-selected per (client, dataset) by deterministic schema matching and spliced as a cross-cutting concern into every stage of an agentic pipeline, the schema explorer, and the report engines, degrading to a strict no-op when absent. Because a skill is a self-contained folder resolved deterministically, the catalogue is open-ended: an extensible marketplace of domain experts. Second, an offline knowledge-compilation loop: an agent probes the dataset's parquet via DuckDB (zero load on production), runs critic-gated per-table convergence with self-healing retries, and data-validates joins by value overlap, producing durable schema knowledge that drives standing expert reports whose every published metric is re-verified by re-executing its evidence SQL, plus suggested questions that mirror the report agenda. These close a proactive loop: reports surface numbers, the numbers seed questions, and a click launches a verified deep dive, all before the query box is used. We give a formal model and report illustrative single-tenant evidence. We make no user-study or benchmark claims; the contribution is the architecture and its defensibility.

---


### 4. [The Signal in the Noise: An Auditable Reliability Layer for Biomedical Text Classification](https://arxiv.org/abs/2608.28595)

**<font color=#1a73e8>作者：</font>** Moustafa Yehia Hassan, Sharon Wong, Woh Kai Xuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical NLP pipelines routinely presuppose clean input text, yet large-scale corpora assembled through automated PDF parsing harbour pervasive OCR-like artifacts, token splits and merges, hyphenation remnants, and character-level corruption, that systematically erode lexical evidence and degrade downstream classifiers. We introduce a conservative, fully auditable spell-correction reliability layer conceived as a safety-oriented preprocessing module rather than a maximal-accuracy corrector: under conditions of uncertainty, the system abstains from editing, in accordance with a medical do-no-harm philosophy. The deterministic architecture couples bounded edit-distance candidate generation with corpus-derived n-gram scoring and a suite of biomedical safety gates that protect domain-critical terminology. We evaluate the layer both intrinsically, on a manually curated benchmark of 2,104 token-level cases, and extrinsically, on a tri-class CORD-19 topic classifier (Prevention, Treatment, Epidemiology) spanning 10,000 examples under a principled four-run protocol (Clean, Noisy, Restored, Safety). Intrinsically, the layer attains 94.61% error-fix recall on synthetic errors with zero harmful edits on negative controls. Downstream, it recovers approximately 80.45% of the noise-induced macro-F1 degradation, elevating macro-F1 from 0.7654 (Noisy) to 0.7717 (Restored) while preserving near-clean performance (Safety: 0.7721). A supplementary case study on 103 real-world OCR-extracted abstracts classified with BioBERT confirms that transformer encoders appeared relatively robust to mild noise, motivating a future grey-box architecture that integrates bounded neural signals and UMLS lexicons without compromising auditability. The system is fully deterministic, artifact-driven, and designed with deployment and auditability in mind.

---


### 5. [Integrating Triaxial IMU Sensors and Ensemble Learning for Effective Parkinson Disease Severity Classification](https://arxiv.org/abs/2608.28602)

**<font color=#1a73e8>作者：</font>** Rehan Khan, Muhammad Junaid Asif, Rana Fayyaz Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parkinson disease PD is a progressive neurodegenerative disease that can have a significant impact on motor performance resulting in the appearance of symptoms such as tremors rigidity postural instabilities and bradykinesia. Timely clinical treatment disease management and quality life of the patients are closely linked to early and appropriate identification of PD. Over the past few years the growth of wearable sensor technology and artificial intelligence AI have made it possible to create noninvasive and data driven disease detection methods. This paper proposes a comparative system using artificial intelligence to detect Parkinsons disease by analyzing the motion and tremor data captured by an inertial measurement unit IMU. The data comprises the signals of the acceleration and gyroscope sensors measuring movement in three directions X Y and Z. The signs and symptoms provide helpful information about subtle motor deficits associated with PD. Several classification models like Support Vector Machine SVM Logistic Regression LR KNearest Neighbors KNN Decision Tree DT Extreme Gradient Boosting XGBoost and Light Gradient Boosting Machine LightGBM were used to compare their effectiveness. The Logistic Regression model had a performance around 75 percent in all evaluation metrics and KNearest Neighbours KNN around 90 percent. The support vector machine SVM performed almost 94 percent whereas the performance of classifiers such as Decision Tree and XGBoost was close to 96 percent and overall classification efficacy respectively. LightGBM model performs consistently at the best rank among all of the evaluated methods having Accuracy, Precision, Recall and F1score of around 97 percent. The results show that the proposed machine learning approach offers an accurate and effective predictive capability in the classification of PD severity.

---


### 6. [C3-UniMM: Causal Cycle-Consistent Unified Multimodal Modeling via Super Alignment and Shared Decoding Space](https://arxiv.org/abs/2608.28603)

**<font color=#1a73e8>作者：</font>** Yujie Shen, Lianlei Shan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models aim to achieve any-to-any understanding and generation across arbitrary modalities. However, existing methods primarily rely on modeling implicit statistical correlations and lack cross-modal structural consistency constraints. This deficiency leads to profound issues, including semantic drift, poor compositional generalization, and instability under interventions. In this paper, we propose C3-UniMM, a unified multimodal modeling framework based on Causal Cycle Consistency and Super Alignment. Specifically, we introduce a Structured Latent Causal Graph (SLCG) as a shared cross-modal semantic space and design unified multimodal encoding blocks, enabling understanding and generation to be synergistically optimized within the identical causal semantic structure. Furthermore, we propose a Unified Decoding Space to enforce structural preservation and semantic invertibility during the cross-modal generation process. Theoretical analyses demonstrate that our approach significantly enhances both the invertibility and mechanism invariance of cross-modal mappings. Extensive experimental results across multiple understanding, generation, and compositional generalization tasks indicate that C3-UniMM substantially outperforms existing unified multimodal baselines.

---


### 7. [NLP-Driven Knowledge Extraction and Thematic Classification of Translated Ancient Indian Medical Texts](https://arxiv.org/abs/2608.28608)

**<font color=#1a73e8>作者：</font>** M. S. Rajeevan, B. Mini Devi, V.S. Anoop 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ancient Indian medical texts like Sushruta Samhita have extensive information on diseases, treatments, and surgical techniques. Yet, their ancient format and use of intricate vocabulary pose difficulties in accessibility and systematic ordering. The research here utilizes Natural Language Processing (NLP) methods like Named Entity Recognition (NER), BERTopic modeling, and Knowledge Graph development in Neo4j to extract, categorize, and visualize important concepts based on translated versions. Thematic classification with BERTopic allows for the identification of the underlying medical topics, whereas NER supports the structured entity recognition of diseases, treatments, researchers, and medicinal plants. Graphbased network analysis with Neo4j also allows for the semantic representation of relationship among extracted entities, supporting knowledge retrieval and digital preservation. The findings illustrate how graph databases, topic modeling, and entity recognition facilitate the computational organization of Ayurveda's historical medical wisdom, closing the gap between the conventional texts and contemporary data-driven inquiry. The suggested method promotes historical text analysis, medical informatics, and digital humanities to make ancient Indian medical wisdom more accessible and understandable.

---


### 8. [STAGEET: Stage-wise Typed Edit Tagging for Grammatical Error Correction with Arabic as a Case Study](https://arxiv.org/abs/2608.28614)

**<font color=#1a73e8>作者：</font>** Wenjie Lou, Alaa Mamdouh Akef  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sequence-to-edit approaches make grammatical error correction (GEC) efficient and locally interpretable by predicting edit labels over the input rather than generating a full corrected sentence. Their interpretability, however, is primarily operational: a label specifies how the string should change, but a single edit vocabulary does not always reveal the type of correction being made. We propose STAGEET, a stage-wise typed edit-tagging framework that reorganizes Seq2Edit supervision into typed executable stages and extends edit operations to correction categories. STAGEET decomposes correction into an ordered sequence of medium-grained typed stages; each stage predicts from its own label space, rewrites the current hypothesis once, and passes the resulting intermediate sentence to the next stage. We instantiate the framework as both an end-to-end shared-encoder multi-head model with stage-specific adapters and a fully specialized variant with one independent tagger per stage. Experiments on QALB-2014 and ZAEBUC show that category-aware staged correction retains competitive edit-based GEC performance while exposing a more inspectable correction trajectory, and attains state-of-the-art results on QALB-2014.

---


### 9. [Preference Elicitation for Policy Optimization and Application to Aligning Heart Transplantation with Human Values](https://arxiv.org/abs/2608.28620)

**<font color=#1a73e8>作者：</font>** Itai Zilberstein, Ioannis Anagnostides, Zachary W Sollie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preference elicitation is essential for aligning AI systems with human values. Prior approaches (e.g., for organ allocation) often ask stakeholders to compare the decisions of an algorithm (e.g., patient A vs. patient B). Such a decision-level approach conflates the means with the ends. Instead, we elicit preferences directly over allocation outcomes to learn a utility function for policy optimization. We construct a novel preference elicitation algorithm for linear utilities that outperforms prior techniques in practice. Our algorithm has two phases. The first phase learns cutting planes through pairwise comparisons to rapidly shrink the space of possible attribute weights and warm-starts the second phase by eliminating dominated regions. The second phase then provably converges to the user's utility function. We apply our technique to heart transplant allocation where a policy must balance competing objectives such as post-transplant outcomes, waitlist mortality, geographic ease, and equity. Using our algorithm, we conduct a user study to learn and aggregate a community-aligned utility function, and use it to optimize heart transplant policies that are significantly better aligned with human values. Compared to the hindsight optimum, the status quo policy achieves a competitive ratio of just 0.54, while our method is near-optimal with a competitive ratio of 0.95.

---


### 10. [Asymmetric Within-Document Predictive Learning for Scientific Document Representation](https://arxiv.org/abs/2608.28625)

**<font color=#1a73e8>作者：</font>** You Zuo, Éric de la Clergerie, Benoît Sagot  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study predictive pretraining for scientific document representation using the discourse structure of papers. We propose SciJEPA, a citation-free framework that learns through asymmetric within-document prediction: title and abstract representations are used to predict method representations, and method representations are used to predict conclusion representations. Experiments on RELISH, high-influence citation, SciDocs, and cite prediction show that plain predictive training is viable but weaker than a controlled contrastive baseline using the same section pairs. Adding Sliced Isotropic Gaussian Regularization (SIGReg) substantially improves performance and narrows this gap. The effect of regularization is task-dependent: moderate SIGReg helps fine-grained ranking, while stronger regularization can weaken local alignment. We further show that different encoding branches support different retrieval regimes. These results position within-document predictive learning as a promising citation-free complement for scientific document representation, provided that embedding geometry is carefully controlled.

---


### 11. [Machine Learning-Enhanced Tabu Search for Tactical Wireless Network Design](https://arxiv.org/abs/2608.28627)

**<font color=#1a73e8>作者：</font>** Wissem Ahmed Zaid, Alain Hertz, Defeng Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing high-performance tactical wireless networks under realistic operational constraints gives rise to challenging combinatorial optimization problems, where the evaluation of candidate solutions relies on detailed physical and traffic-aware models. Although classical metaheuristics such as Tabu Search offer effective mechanisms for exploring large search spaces, their computational cost remains high because numerous candidate moves must be evaluated at every iteration. In this paper, we propose a data-driven framework that improves the efficiency of Tabu Search by learning to guide its move selection process. Rather than altering the neighborhood structure, our approach exploits the information contained in the search trajectories generated during the optimization process. At each iteration, we record both improving and non-improving edge-based transformations together with a set of descriptive features capturing the structural, geometric, and performance characteristics of the network. This information is used to train a Graph Neural Network (GNN) that predicts the impact of candidate moves on the objective function. The trained model is then integrated into the Tabu Search algorithm to rank candidate transformations according to their predicted quality, thereby reducing the number of costly objective evaluations while maintaining an effective exploration of the search space. Experimental results on synthetic benchmark instances demonstrate that the proposed learning-assisted Tabu Search notably reduces computation time while consistently producing higher-quality solutions than the standard algorithm. These findings highlight the potential of combining machine learning with metaheuristics by leveraging the implicit knowledge embedded in search trajectories, paving the way for more efficient solution methods for large-scale network design problems.

---


### 12. [CrossAudit: A Git-Native, Cross-Vendor Audit Loop for Agentic Science](https://arxiv.org/abs/2608.28631)

**<font color=#1a73e8>作者：</font>** Zhaohe Dong, Yuhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI scientist should not grade its own homework. Yet in the systems we examined, the agent that reviews the work usually comes from the same model family as the agent that produced it, or at least from the same vendor. Model evaluators are known to favour their own generations. Whether models trained alike also share blind spots is a conjecture, not a settled finding, but if they do, the reviewer inherits the author's. The record of what was flagged and what was waved through often sits in platform logs that nobody outside can replay.
We present CrossAudit, a protocol for supervising autonomous research pipelines. It rests on three commitments. Each increment of work is audited by an agent from a different vendor against a rulebook a human wrote and versioned. Reports, verdicts, disputes and rulings are git commits, so the supervision history can be re-read and cited; raw model exchanges are not yet part of that record. Scripted checks run before any model does. Advisory judgement never gates the pipeline: a model blocks only by citing a rule, and no model may waive a deterministic failure. Blockers that survive a bounded number of revision rounds go to a person.
We state the protocol as eight invariants. We describe a reference implementation built from GitHub Actions and a few hundred lines of Python, and report a live deployment of a closely related variant in a computational-chemistry pipeline. We also ran a seeded-defect trial (30 increments, 43 seeded defects, one run per configuration). A cross-vendor audit of our own repository then voided its blinding. We adopt that audit's findings and report the corrected results. The trial shows that two vendors read the same rulebook differently. It does not show that either is better. The strongest evidence here is the committed, uncontrolled record of cross-vendor audits of this paper itself.

---


### 13. [AI Scientist Mission Control (AIMC): Visual Analytics for Human Oversight of Autonomous Scientific Discovery](https://arxiv.org/abs/2608.28637)

**<font color=#1a73e8>作者：</font>** Rikathi Pal, Klaus Mueller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific discovery systems can generate large numbers of research ideas, experiments, and manuscripts with minimal human intervention. As these systems become increasingly capable, scientists require effective mechanisms to monitor output quality, identify recurring failure modes, understand research evolution, and prioritize promising discoveries for review. We present AIMC, a visual analytics framework for human oversight of autonomous scientific discovery. AIMC combines semantic embeddings, automated weakness extraction, temporal analysis, and interactive visualizations to support the exploration of AI-generated research artifacts. We demonstrate the framework through a case study of the papers generated by an autonomous AI Scientist (FARS), together with their associated review feedback. Our analysis reveals recurring methodological weaknesses, evolving research themes, domain-specific differences in quality, and a small set of highly novel papers that warrant deeper human inspection. These findings illustrate how visual analytics can support transparency, diagnosis, and human AI collaboration in emerging autonomous scientific discovery workflows.

---


### 14. [PromptKWS: A Novel Prompt-Guided Open-Vocabulary Keyword Spotting Framework](https://arxiv.org/abs/2608.28640)

**<font color=#1a73e8>作者：</font>** Gaopeng Xu, Chengfei Li, Xianliang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we present PromptKWS, a novel Prompt-guided keyword spotting (KWS) framework to improve the accuracy of open vocabulary KWS systems. In specific terms, we introduce the Prompt Phrases Prediction Network (PPN), an encoder-decoder architecture designed to effectively extract keyword prompts embeddings. we employ the PPN encoder to encode the keyword prompts and infuse the prompt embedding into the Prompt-guided KWS encoder by utilizing a Prompt-acoustic Multi-head Cross-attention (MHCA). Experiments show that PromptKWS improves the wakeup rate by over 10% compared to baseline system. Notably, another strength of PromptKWS is its ability to effectively leverage keyword prompts for adapting to complex real-world environments involving noise and pronunciation variations. In comparison to purely acoustic models, which often struggle in such situations, PromptKWS demonstrates remarkable performance, with an average accuracy improvement of over 15% in test sets.

---


### 15. [From Extraction to Governed Memory: Multi-Agent Knowledge Graph Construction with Domain-Expert Review](https://arxiv.org/abs/2608.28642)

**<font color=#1a73e8>作者：</font>** Pranav Bykampadi, Neel Mokaria, Vishesh Narayan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs used by agentic systems are often treated as flat stores of extracted triples, with little record of who owns a fact, why it was admitted, or how it should be used downstream. We argue that reliable agentic knowledge systems require governance as an essential component of graph construction to bridge this gap. We propose MAGG, a principled multi-agent framework for constructing Governed Knowledge Graphs that introduces explicit governance decisions for reliable and trustworthy knowledge sharing. A domain classifier first induces entity and relation types directly from document content, enabling operation in open-world settings without fixed schemas. Candidate triples are assigned to domain owners, reviewed against supporting evidence, admitted through governance decisions, and stored with audit metadata. The same ownership structure is reused during question answering, where queries are routed to domain-specific graph experts rather than answered through undifferentiated retrieval. Our evaluation demonstrates MAGG's effectiveness: On SciERC, MAGG improves strict triple F1 by 47% and mapped triple F1 by 51% over flat insertion. A blinded review of 120 triples finds governed-only triples more often source-supported than flat-only ones, and revised triples supported in 100% of cases. Finally, on MuSiQue, MAGG outperforms Microsoft GraphRAG by 9.0 exact-match points and 11.2 token-F1 points.

---


### 16. [Redesigning and Auditing Deep Research Writing for Faithful Reports](https://arxiv.org/abs/2608.28643)

**<font color=#1a73e8>作者：</font>** Hiroaki Hayashi, Pranav Narayanan Venkit, Prafulla Kumar Choubey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluations of deep-research (DR) systems often obscure fine-grained factual failures in generated reports. We introduce CLAIMPROBE, a claim-level audit that decomposes DR reports into claims and measures hallucination, misattribution, citation hygiene, and necessary-fact recall against retrieved evidence. Using CLAIMPROBE, we find that strong DR pipelines can omit key evidence and misattribute claims even when their rubric scores remain stable. We then propose CLAIMWRITER, a hierarchical claim-based writer that extracts source facts, maps them to a query-derived outline, and drafts each section from a source-linked claim representation. Across three prior DR frameworks, replacing only the report writer with CLAIMWRITER reduces hallucination by 2.6 to 4.5 times and improves necessary-fact recall by 1.2 to 1.7 times, while largely preserving overall report quality. CLAIMWRITER also enables localized revision: when sources change, it propagates changed source facts into revised reports at the highest rate among update methods, while also being more cost-effective.

---


### 17. [Goal Staying Makes Sum-of-Costs Anonymous Multi-Agent Path Finding NP-Hard](https://arxiv.org/abs/2608.28658)

**<font color=#1a73e8>作者：</font>** Hang Ma  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Anonymous Multi-Agent Path Finding (AMAPF) admits polynomial-time network-flow algorithms for several objectives, including makespan, total distance, and sum-of-costs (SoC) when agents disappear upon reaching goals. We show that standard goal-staying AMAPF is fundamentally different. We first formulate SoC minimization by augmenting the standard time-expanded flow model with goal-settlement constraints and show that the resulting linear programming relaxation is non-integral. We then prove that minimizing SoC in goal-staying AMAPF is NP-hard via a reduction from 3-SAT. Together with the polynomial-time result for the disappearing variant, this establishes a sharp complexity boundary determined by whether completed agents remain at their goals.

---


### 18. [Open-Set Cattle Muzzle Identification: A Leakage-Controlled Benchmark and Evaluation Protocol](https://arxiv.org/abs/2608.28663)

**<font color=#1a73e8>作者：</font>** Lalit BC, Dharmendra Singh Chaudhary, Shovit Nepal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable individual cattle identification supports disease surveillance, vaccination records, breeding management, and livestock insurance. Although the bovine muzzle provides a stable, non-contact biometric, existing muzzle-recognition systems largely assume a closed set of enrolled animals, limiting their practical deployment. We reformulate cattle muzzle biometrics as an open-set, gallery-based identification problem that can reject previously unseen animals and support incremental enrollment without model retraining. We introduce a leakage-controlled evaluation protocol based on identity-disjoint splits, per-fold retraining, held-out threshold calibration, verified duplicate removal, and bootstrap confidence intervals. We evaluate the framework using two contrasting embedding configurations: a hybrid CNN-ViT metric-learning model and the MegaDescriptor-L foundation model. Under oracle threshold selection, the hybrid model achieves detection-and-identification rates of 98.3%, 96.4%, and 93.6% at target false-acceptance rates of 10^(-1), 10^(-2), and 10^(-3), respectively, while MegaDescriptor-L achieves 99.3%, 98.1%, and 96.1%. However, deployable threshold calibration reveals a substantial difference between oracle and calibrated performance: the hybrid model achieves a false-acceptance rate of 1.03% at a 1% target, whereas MegaDescriptor-L reaches 2.44%. Incremental enrollment further achieves Rank-1 accuracy above 91% with a single reference image and up to 97.3% with eight reference images, without retraining the model or degrading the existing gallery. These results demonstrate that threshold calibration, leakage control, and embedding quality are critical for reliable open-set cattle identification and provide a practical evaluation framework for deployment-oriented animal biometric systems.

---


### 19. [Understanding Temporal Semantic Stability in Open-Vocabulary UAV Perception through Metric 3D Fusion](https://arxiv.org/abs/2608.28665)

**<font color=#1a73e8>作者：</font>** Saurbh Singh Jamwal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent open-vocabulary segmentation models have advanced semantic perception for UAVs, but predictions from moving aerial platforms can remain temporally inconsistent across repeated observations of the same physical scene. We investigate temporal semantic stability by associating frame-wise predictions with persistent world-space locations through metric 3D fusion. We introduce a voxel-level evaluation framework that jointly characterises final semantic agreement, Semantic Belief Drift (SBD), Observation Persistence (OP), and semantic uncertainty. Experiments on UAVid-3D reveal substantial frame-wise semantic flicker and show that high aggregate world-space agreement can overstate temporal stability when locations have limited repeated-observation support. Persistence-stratified analysis shows that recurrent voxels expose greater semantic disagreement, while belief drift decreases as additional evidence accumulates. This behaviour is observed across two segmentation backbones and remains consistent under variations in voxel resolution, geometric association, and temporal sampling density. Conditions that reduce world-space recurrence can increase apparent aggregate stability, demonstrating that semantic consistency must be interpreted together with observation support. Our findings highlight observation persistence as an essential conditioning variable for evaluating long-horizon semantic reliability.

---


### 20. [MIRAGE-CAD: Construction-Mediated Multimodal Generation of Executable CAD Programs](https://arxiv.org/abs/2608.28669)

**<font color=#1a73e8>作者：</font>** Jizong Zhan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering an executable parametric CAD program from an observed object is fundamentally ambiguous, because the same final geometry can result from different construction procedures. We study this problem from four types of input: natural-language descriptions, rendered images, point clouds, and STEP/B-Rep geometry. MIRAGE-CAD maps each input to a shared construction representation and mediates program generation through an explicit construction-plan interface. The resulting Python CAD code is executed by an OpenCASCADE kernel to build the solid and export it as STEP. On 2,500 held-out queries per modality, the system achieves 55.4-70.0% build success and 52.3-66.2% STEP export success without retrieval at inference. Controlled comparisons show that strong reconstruction does not depend on expressing the construction representation as text: a decoder conditioned directly on the continuous representation also reconstructs strongly, while an exposure-matched plan-based decoder shows no detected material loss in per-part geometric fidelity. The explicit plan instead provides a readable and separately measurable intermediate representation whose agreement with the reference construction is informative about downstream execution success. Finally, we show that executable validity, geometric fidelity, and parametric responsiveness can diverge substantially and should therefore be evaluated separately.

---


### 21. [Memory-Efficient Training-Free Acceleration of Diffusion Transformers with BaryCache](https://arxiv.org/abs/2608.28670)

**<font color=#1a73e8>作者：</font>** Chengjie Lu, Tianchi Deng, Zhengqi He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers achieve high-fidelity image and video generation, but their iterative sampling remains expensive, for each denoising step requires large matrix operations. Existing cache-based acceleration reduces redundant computation yet increases the VRAM footprint by storing intermediate states, which can directly constrain inference batch size. In this work, we propose a training-free acceleration method that performs stepwise forecasting for DiT sampling using a Barycentric Extrapolator. By leveraging barycentric extrapolation, our predictor is numerically stable and alleviates oscillatory artifacts analogous to the Runge phenomenon during forward forecasting. Across extensive experiments on both image and video generation, our approach provides a favorable trade-off between memory usage and perceptual quality, while delivering up to 3.30x end-to-end sampling speedup compared with baseline DiT inference.

---


### 22. [Measuring Similarity between Artistic and AI Generated Images using Siamese Neural Networks](https://arxiv.org/abs/2608.28671)

**<font color=#1a73e8>作者：</font>** Diego Castro Elvira, Navil Pineda Rugerio, Jesús García-Ramírez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated art has sparked debates around potential plagiarism, as these images may closely resemble existing artworks. This research quantifies the similarity between original pieces and AI-generated counterparts, particularly those produced by the Stable Diffusion XL Refiner 1.0. We use Siamese Networks with frozen CLIP encoders and cosine similarity optimized through triplet loss. A dataset of paired original and generated images was built using image-to-image generation and custom prompts, enriched with semantic descriptors and BLIP-2 captions. Prior studies report up to 81\% style replication and 90\% visual similarity. Our results show high discriminative performance: training accuracy reached 99.9\%, and the best model configuration achieved 99.4\% test accuracy with strong inter-class separation ($\delta \mu$ = 0.677), demonstrating the effectiveness of our semantic-visual embeddings.

---


### 23. [FrameScope: Temporal Data Valuation for Stream Active Learning in Autonomous Vehicle Systems](https://arxiv.org/abs/2608.28672)

**<font color=#1a73e8>作者：</font>** Yuheng Zhu, Man-Ki Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles operate in dynamic, ever-changing environments where new scenarios and edge cases constantly emerge. As a result, static learning models are inadequate for ensuring safe and reliable operation. Continuous learning is essential for adapting to these evolving conditions and maintaining robust performance across diverse real-world settings. However, autonomous vehicles generate massive streams of visual data during operation, and existing continuous learning approaches typically rely on heuristic sampling methods that fail to capture temporal dynamics, often overlooking critical learning opportunities or selecting redundant frames. In this paper, we introduce FrameScope, a temporal data valuation framework for continuous learning in autonomous vehicles. FrameScope extends neural tangent kernel theory to temporal domains, enabling principled valuation of streaming visual data. Unlike cloud-centric methods that transmit all video data for processing, our approach performs principled, local frame selection on the vehicle and queries a cloud-based oracle model only for labels of those high-value frames. Extensive experiments across multiple domain shifts show that FrameScope consistently outperforms existing methods, achieving higher sample efficiency and significantly reducing catastrophic forgetting in autonomous vehicle perception. By valuing data on the vehicle and querying only labels for selected frames, FrameScope reduces bandwidth requirements, enabling scalable operation with a lightweight cloud labeling service.

---


### 24. [AdaptAV: Continuous Adaption of Vision Models for Autonomous Vehicles Using Cloud-based Oracle](https://arxiv.org/abs/2608.28673)

**<font color=#1a73e8>作者：</font>** Yuheng Zhu, Dhruva Ungrupulithaya, Boluo Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying vision perception models in autonomous vehicles requires that we prioritize inference speeds, resulting in a model with shallower architectures and lesser model parameters (i.e., more pruned). Such small models do not generalize well, which could result in poor performance when encountered with novel scenarios. We propose a system that overcomes this by continuously retraining the vision models on the cloud with data uploaded by vehicles. We leverage the abundant compute resources, including machine learning accelerators, of the cloud to run a highly-accurate oracle model that will guide the retraining process of the on-vehicle model. This newly trained model is transmitted to the vehicle over the network and is utilized by the vehicle for perceptions, leading to improved inference accuracy over time.

---


### 25. [Multi-exposure HDR Imaging: A Review of Pixel-level and Feature-level Reconstruction Methods](https://arxiv.org/abs/2608.28674)

**<font color=#1a73e8>作者：</font>** Qian Tao, Wei Wang, Chaobing Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-exposure is an efficient way to capture real-world high-dynamic-range (HDR) scenes. However, HDR imaging suffers from severe ghosting artifacts in dynamic scenes due to the temporal gap between sequential exposures. In this article, we categorize the literature on two important topics on HDR imaging: multi-exposure fusion (MEF) and ghost removal. Conventional filter-based and data-driven methods are studied in pixel space and feature space. For popular deep learning-based approaches, we provide a granular taxonomy based on their alignment and fusion domains: pixel-space methods, which typically employ explicit motion compensation such as optical flow or spatial transformers, and feature-space methods, which leverage implicit alignment through deformable convolutions, attention mechanisms, or latent representation merging. Representative works are compared across different supervision settings, and key design principles are summarized. In addition, this survey summarizes commonly used datasets and evaluation metrics, discussing their applicability under diverse output forms. Finally, major bottlenecks and promising directions for future research are outlined.

---


### 26. [Multi-Agent Self-Improving Reinforcement Learning for Video Reasoning](https://arxiv.org/abs/2608.28675)

**<font color=#1a73e8>作者：</font>** Mingwen Zhang, Jisheng Dang, Minqiang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning tasks such as grounded video question answering and temporal grounding require selecting temporal evidence that supports the query. In many current training setups, temporal supervision is applied through local objectives such as boundary regression or span generation, while verification is used mainly to rerank candidate segments at inference time. We study whether a frozen verifier can also guide training. Our multi-agent framework couples a trainable \emph{Grounder} with a frozen \emph{Verifier}: the Grounder samples candidate trajectories and evidence segments, the Verifier assigns query-conditioned segment scores, a group-relative policy-gradient objective favors trajectories that outperform their within-input peers, and a bootstrapped calibration loss steers temporal predictions toward verifier-preferred spans. Trained on source tasks and evaluated without target-dataset fine-tuning, a two-billion-parameter instantiation transfers zero-shot across grounded question answering, temporal grounding, and long-video question answering, reaching 28.7\% intersection-over-union and 25.4\% answer-grounding accuracy on a grounded-question-answering benchmark, 46.1\% intersection-over-union on a temporal-grounding benchmark, and 54.1\% on a long-video question-answering benchmark. Relative to a strong same-scale baseline, the gains are modest but consistent, with the clearest improvements on relevance-oriented metrics such as intersection-over-union and moderate-overlap recall. Within the tested benchmarks and transfer setting, the results support frozen verification as a training signal for evidence selection, while showing that strict boundary precision remains comparatively weaker. Code and models are available at this https URL

---


### 27. [Multi-Sensor Mapping of Vulnerable Urban Settlements Using SAR, Multispectral, and Hyperspectral Imagery: A Case Study in Córdoba, Argentina](https://arxiv.org/abs/2608.28680)

**<font color=#1a73e8>作者：</font>** Luigi Russo, Anabella Ferral, Silvia Liberata Ullo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Informal settlements represent a major urban challenge in rapidly expanding cities, yet their identification from Earth Observation (EO) data remains difficult because of their heterogeneous appearance and incomplete official inventories. This work presents a multi-sensor deep learning (DL) framework for slum-likelihood mapping in Córdoba, Argentina, integrating high-resolution PlanetScope multispectral (MS) imagery, COSMO-SkyMed (CSK) Synthetic Aperture Radar (SAR) data, and medium-resolution PRISMA hyperspectral (HS) observations. The problem is formulated as a patch-level classification task using the official Registro Nacional de Barrios Populares (ReNaBaP) inventory as reference, and the models are evaluated through four geographically partitioned folds. SAR-only and MS-only baselines, their configurations with PRISMA HS support, and early fusion (EF), middle fusion (MF), and late fusion (LF) strategies are systematically compared. Results show that LF+HS provides the best overall balance between classification performance and spatial selectivity, while PRISMA contributes complementary spectral information alongside the higher-resolution MS and SAR representations. Beyond the standard evaluation against ReNaBaP, an external municipal vulnerability layer is used to interpret detections outside the official polygons, showing that several apparent false positives overlap broader vulnerable urban areas. Thermal analysis further shows that ReNaBaP settlements exhibit significantly higher surface temperatures than their immediate surroundings during a heatwave event, indicating localised surface-heat amplification. Taken together, these results suggest that multi-sensor EO fusion can support both the mapping of ReNaBaP settlements and the interpretation of broader urban vulnerability patterns.

---


### 28. [CARD: Calibration via Agreement in Reverse Diffusion for Out-of-Domain MRI Segmentation](https://arxiv.org/abs/2608.28681)

**<font color=#1a73e8>作者：</font>** Jiaheng Dai, Weidong Guo, Qingbiao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Probability calibration aligns model confidence with predictive accuracy, enabling clinicians to identify unreliable segmentation regions. This alignment breaks down under domain shift, where artifacts and unseen protocols produce confident errors. Existing post-hoc methods adapt the correction at test time, conditioning on predictive entropy, the logit pattern, or augmentation response, but each proxy is read from the terminal prediction, the very quantity that shift corrupts. This motivates reliability evidence beyond the terminal prediction, which categorical diffusion provides in two ways. First, a generative shape prior keeps a capacity-limited reference intact when appearance is corrupted, so its disagreement with the primary segmentor highlights primary-model errors. Second, every reverse step yields a class distribution, separating persistent disagreement from transient discrepancy. Aggregated over the trajectory, this disagreement correlates with Dice at 0.788, against 0.521 for a matched discriminative control. We therefore propose CARD (Calibration via Agreement in Reverse Diffusion), which maps the temporal aggregate of this disagreement to a temperature field applied per pixel across all classes, so that confidence changes while the segmentation does not. Across cardiac, prostate and brain MRI shifts, CARD lowers calibration error in 45 of 49 comparisons against the strongest baseline in each setting.

---


### 29. [Distributed Semantic Segmentation With Improved Rate-Distortion Trade-Off](https://arxiv.org/abs/2608.28684)

**<font color=#1a73e8>作者：</font>** Danish Nazir, Timo Bartels, Thorsten Bagdonat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distributed deep neural networks (DNNs) for dense perception tasks such as semantic segmentation execute an encoder DNN on edge devices, and a decoder DNN typically on a large-scale cloud platform with a particular constraint on transmission bitrate. Recent works employ source codecs to enable bitrate-efficient transmission between the edge device and the cloud. However, as these approaches are typically bound to a particular type of source codec and alternative network architectures are often not explored, this results in a suboptimal rate-distortion (RD) trade-off in the low-bitrate regime. In this work, we propose two novel source codecs that \textit{enable extremely low bitrates, while improving RD performance}. We demonstrate the effectiveness of our proposed source codecs by achieving state-of-the-art performance in distributed semantic segmentation at below 0.2 (0.03) bits per pixel, measured using the mean intersection-over-union metric on ADE20K (Cityscapes).

---


### 30. [Data Diversity, Not Frequency Invariance: A Controlled and Self-Audited Study of Compression-Robust Deepfake Detection](https://arxiv.org/abs/2608.28685)

**<font color=#1a73e8>作者：</font>** Abbas Aliyev, Samir Rustamov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frequency features and compression-invariant representation learning are widely assumed to be key to deepfake detection that survives video compression. We test this with CAFRL - block-DCT and FFT-phase streams, compression-level-conditioned band attention, and adversarial (gradient-reversal) compression invariance - and report a controlled negative. Under a pre-registered protocol with capacity- and augmentation-matched controls, a plain EfficientNet-B0 on multi-quality data beat CAFRL as specified at every compression level on the FaceForensics++ test split, by 3.66 AUC points at CRF 40 (paired, single seed). A self-audit of our own negative found four defects biased against the frequency hypothesis, and pre-specified re-tests repairing all four showed the deficit to be a recipe artifact, not an architecture failure: the baseline recipe recovered 3.96 points over the matching shipped-recipe variant. The frequency path made no detectable difference: discriminative alone (standalone validation AUC 0.91-0.98 late in training) but of no marginal value under this fusion, at two feature widths of one 4.0 M trunk, every seed-pooled interval for the intra-dataset compression contrasts including zero; on the single held-out manipulation tested, the fair variants sat below the plain backbone. The adversarial branch, as specified, added nothing and degraded its own conditioning estimator; at the fair recipe it is untested. Robustness under single-pass H.264 re-encoding came instead from data diversity: real constant-rate-factor variants beat synthetic JPEG augmentation by 7.3 points (single runs, non-overlapping intervals). The evidence is FaceForensics++-family, GAN-era and single-codec. Match controls on training recipe as well as capacity, and buy compression robustness with codec diversity before architecture.

---


### 31. [Projection-Aware End-to-End Learned Video Compression for 360-Degree Video](https://arxiv.org/abs/2608.28689)

**<font color=#1a73e8>作者：</font>** Niloofar Maani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 360-degree video supports immersive applications such as virtual reality, autonomous driving, and education. Because spherical content cannot be processed directly by conventional video codecs, it must first be mapped to a two-dimensional projection. Projection choice affects spatial continuity, sampling uniformity, motion estimation, and compression efficiency.
This thesis investigates how projection format influences end-to-end neural compression of 360-degree video. Seven formats supported by JVET 360Lib are evaluated using the scale-space flow model, JVET test sequences, and common test conditions. Each sequence is converted from its source equirectangular projection to a coding projection, compressed at multiple rate points, reconstructed, and converted back. Performance is assessed using PSNR, spherical PSNR, weighted spherical PSNR, and Bjøntegaard delta rate. A differentiable pipeline combining projection conversion, neural compression, and inverse projection is also compared with 360Lib.
Results show that equirectangular and padded equirectangular projections provide the highest compression efficiency with the scale-space flow model, while cubemap-based and rhombic dodecahedron projections are less effective. This differs from the conventional HM-16.16 codec, for which cubemap-based formats, particularly equi-angular and adjusted cubemap projections, outperform equirectangular formats. Neural models based on optical flow benefit from the spatial continuity of single-face projections, whereas block-based hybrid codecs better accommodate multi-face layouts. These findings show that projection efficiency is codec-dependent and provide guidance for selecting projections for learning-based 360-degree video compression.

---


### 32. [Growing a Stand, Not a Tree: Joint Canopy Generation Reproduces Crown Shyness](https://arxiv.org/abs/2608.28692)

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In closed forests, neighboring tree crowns often stop short of touching, leaving a network of narrow gaps known as crown shyness. The pattern belongs to the stand rather than to any single tree, which makes it a natural probe of a question in generative modeling: can a learned model produce a set of objects whose defining structure exists only between them? We formulate stand-level canopy generation as set generation with a flow-matching model, in which attention between trees is the only channel through which coupling can arise. Trained on stands grown by a resource-competition simulation that is provably not reducible to per-tree geometry, the joint model halves the clearance distribution error of an identical-capacity model that generates each tree alone, and the advantage persists at stem densities outside the training range. Against field measurements of a tropical oak forest, a single calibrated scalar yields held-out agreement in gap magnitude and crown asymmetry. The directional statistics of the gaps are controlled by stem placement rather than by the growth rule, and match the field once stem jitter is calibrated. Crown shyness, in both the simulation and the learned model, is a property of the stand and not of the tree.

---


### 33. [SNF-Bench: Separating Static Drift from Natural Flow in Long-Horizon Fixed-Camera Video Generation](https://arxiv.org/abs/2608.28694)

**<font color=#1a73e8>作者：</font>** Matiur Rahman Minar, Seunghun Oh, Ganghyeon Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon video generation is evaluated with whole-frame metrics that reward motion and temporal consistency. For fixed-camera nature scenes this creates an ambiguity: motion of water, fire, smoke, or rain is desirable, whereas motion of the background is an error. A system can therefore score well on motion while its scene drifts, or on consistency while its flow stagnates. We introduce SNF-Bench, an evaluation framework for long-horizon fixed-camera generation that partitions each scene into static support and dynamic flow and reports static fidelity, flow persistence with absolute magnitude, and drift leakage separately, never as one score. Drift leakage is interpretive context rather than a headline measurement. Each factor is validated mechanistically rather than by correlation with preference: we inject global translation, rotation, and scale drift and progressive late freezing at known severity into real generations, and require each factor to respond in its stated direction and to remain selective against corruptions it does not target. Auditing publicly released long-horizon text-conditioned checkpoints under one recorded common inference configuration, plus an image-conditioned track with released-pipeline references and a deployment-sensitivity panel, we find that whole-frame motion and static-region drift induce near-opposite orderings of the same outputs. At maximum controlled translation, fBD and NBF rise to $1.86\times$ and $1.32\times$ baseline, but whole-frame Dynamic Degree reaches only $1.07\times$---rewarding the corruption. SNF-Bench measures where motion occurs and whether it persists; it does not measure physical realism. Project page: this https URL.

---


### 34. [Stochastic Liquid Deformation Fields: An SDE Generalisation of Closed-Form Continuous-Time Cells for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2608.28702)

**<font color=#1a73e8>作者：</font>** Mingzhao Li, Arghya Pal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable 3D Gaussian Splatting (D-3DGS) reconstructs dynamic scenes by deforming a canonical set of 3D Gaussians through a deformation field of frame time. Replacing its MLP with a stack of Closed-form Continuous-time (CfC) cells-a Liquid Neural Network that solves the Liquid Timeconstant ODE in closed form-gives the field continuous-time behaviour at feed-forward cost. That closed form, however, is only the deterministic limit of a noise-driven system, and drops the stochastic term usually credited for the robustness of liquid networks. We put it back: a small Gaussian perturbation is added to the time gate of every CfC cell, turning the deterministic field into a simple stochastic (SDE) one. The noise is used only during training, needs no solver, and reduces exactly to the CfC when switched off. On the synthetic D-NeRF scenes the stochastic field is on par with the deterministic CfC and beats the MLP baseline on most scenes; on the real-world NeRF-DS scenes the deterministic limit is already best and adding noise does not help. The study thus gives both a clean way to read the CfC field as an SDE and an honest account of when a plain noise term helps and when it does not.

---


### 35. [ORDDAR: Observation-Driven Reasoning for Distortion-Resilient Decision, Action, and Cognitive Recovery](https://arxiv.org/abs/2608.28704)

**<font color=#1a73e8>作者：</font>** Deblina Kar, Anant Nawalgaria, Shyamal Kumar Das Mandal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly perform long-term reasoning, planning, tool use, memory integration, and autonomous decision making, yet erroneous intermediate states can propagate and cause inconsistent decisions and unreliable outputs. Existing reasoning approaches mainly rely on iterative planning, self-reflection, augmented memory, or verification, but rarely localize and selectively repair faulty reasoning. We present ORDDAR (Observation-Driven Reasoning for Distortion-Resilient Decision, Action, and Cognitive Recovery), a reasoning framework that models reasoning as cognitive state transitions, detects localized distortions, retrieves related reasoning from prior experiences, and repairs only the affected states. ORDDAR therefore performs recovery at the local reasoning-transition level rather than regenerating the complete trajectory. Experiments across mathematical, commonsense, multi-hop, and clinical reasoning benchmarks demonstrate improved reasoning quality, recovery ability, and interpretability over multiple evaluated reasoning baselines.

---


### 36. [Variable-Granularity Tokenization for High-Resolution Object Detection](https://arxiv.org/abs/2608.28706)

**<font color=#1a73e8>作者：</font>** Khayrul Islam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ViT detectors fix a uniform token grid before any learned stage. A native-resolution aerial detector must then choose between resolving few-pixel objects and staying inside compute and memory limits. We introduce VGTok, a training-free tokenizer that sets patch granularity per region from pixels, ahead of the encoder. VGTok scores each region by multi-scale morphological top-hat separability from its surround, then thresholds those scores at a per-image percentile, which fixes the token budget. A structure-tensor gate ($\lambda_{\min}$) refines only where two-dimensional object structure supports it, leaving one-dimensional clutter coarse. The resulting token set is a strict partition of the image. In a Co-DETR detector with an EVA-02 ViT-L encoder, VGTok clears every published VisDrone-val AP and AP$_S$ at every budget from 40\% to 100\% of tokens. At 40\% it records 44.22 AP with three fifths of the sequence discarded before the first transformer block; dense, it reaches 48.38 AP, $6.08$ above the strongest published entry. VGTok transfers to AI-TOD-v2 untouched, same scorer and same rank, and sets a new state of the art at 37.27 AP and 19.51 AP$_{vt}$. As a pure drop-in into a frozen checkpoint it reaches 36.29 AP at 78.5\% of tokens, above every published entry, where our 376.3M-parameter detector clears a 3.0B multi-expert model. We show that a token budget fixed before the backbone, from local separability and structure geometry alone, holds accuracy on the tiny-object regimes that dominate aerial detection, at $3.1\times$ less encoder compute and $1.9\times$ less encoder memory. Code and models are available at \href{this https URL}{\texttt{this http URL}} and \href{this https URL}{\texttt{this http URL}}.

---


### 37. [MANTLE: A Framework for Adaptive In-Situ Planetary Perception Using a Modular Uplink Principle](https://arxiv.org/abs/2608.28724)

**<font color=#1a73e8>作者：</font>** Pranav Durai, Gary Doran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Planetary surface exploration missions rely increasingly on autonomous robotic platforms capable of interpreting complex terrain to ensure safe navigation, enable targeted science, and improve operational efficiency, as demonstrated across past Mars missions from Viking through Perseverance. Among the key perception capabilities, landform classification provides contextual information for landing site selection and scientific analysis, while boulder segmentation supports hazard assessment and path planning. This paper presents MANTLE, a multi-task adaptive network for terrain and landform extraction. The model uses a shared DINOv2 backbone for high-level feature extraction with task-specific heads: a classification head for large-scale landform classification, and a segmentation head for pixel-wise boulder localization, each trained on curated datasets built respectively from HiRISE orbital imagery and MSL surface-level imagery. The classification head achieved a test accuracy of 92.56% across seven Martian terrain classes, while the segmentation head achieved a validation IoU of 0.753 and showed strong cross-sol generalization on a held-out test set from previously unseen rover traverses. A key advantage of MANTLE is its modular, extensible design, formalized here as the Modular Uplink Principle: only a shared, frozen backbone needs to remain onboard, while subsequent perception capabilities are trained on Earth as lightweight task-specific heads and uplinked without retraining the full model. This work demonstrates two such high-impact capabilities, terrain classification and boulder segmentation, as an initial realization of a framework built to support many more over a mission's lifetime. With this foundation, future explorers need not arrive on Mars fully formed, but can continue to learn, adapt, and grow more capable with every uplink.

---


### 38. [A Conceptual Framework for Modeling Team Adaptation in Cooperative Games Through Ludic Knowledge](https://arxiv.org/abs/2608.28729)

**<font color=#1a73e8>作者：</font>** Caleb Vatral  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the increasing importance of teamwork skills for modern workplaces, development of teamwork training programs has received substantial attention. Game-based teamwork training is one promising approach that is engaging, cost-effective, and well-suited to increasingly decentralized workplaces. However, design of effective game-based teamwork training requires understanding how a game elicits specific desired teamwork behaviors. Significant progress has been made in characterizing these relationships. However, despite its critical importance, little work has examined how a game's design influences team adaptability behaviors. This paper presents a preliminary framework for analyzing adaptability in cooperative games by conceptualizing adaptive stimuli as retrieval or disruption of players' ludic knowledge. We illustrate this framework through a qualitative case study that applies interaction analysis methods to gameplay videos of a Overcooked!, a cooperative cooking game. We examined instances where game events led to players altering their behavior and connected the game's design features that resulted in each event with three adaptive stimulus cue categories. Although exploratory and limited to a small case study of a single game, the proposed framework is grounded in established theories across teamwork research and game studies, and it offers an initial vocabulary for describing how cooperative games can be designed to create demands for team adaptation. With this continued development, the framework may provide an analytic tool to help inform the design and evaluation of purpose-built game-based teamwork training environments.

---


### 39. [Evaluating Multilingual Sentence Embeddings for Translation Error Detection:An English--Greek Contrastive Study](https://arxiv.org/abs/2608.28776)

**<font color=#1a73e8>作者：</font>** Eleftherios Kalogeros, Athanasios Ntalakas, Manolis Gergatsoulis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual sentence embeddings are increasingly used to estimate semantic similarity across languages, yet their sensitivity to fine-grained translation errors remains insufficiently understood. This study investigates whether general-purpose multilingual embedding models can distinguish correct English-Greek translations from minimally modified erroneous alternatives. A contrastive dataset was developed from FLORES+ sentence-aligned reference translations and reviewed by two translation experts. It contains 1,850 examples across ten core and five exploratory error categories, covering factual, lexical-semantic, grammatical, relational, referential, and discourse-level phenomena.
Five multilingual sentence-embedding models (BGE-M3, Multilingual E5, Multilingual MPNet, LaBSE, and Jina Embeddings v3) were evaluated using cosine similarity between each English source sentence and its correct and erroneous Greek translations. A reference-free COMETKiwi model was also evaluated as an MT quality-estimation baseline. Performance was assessed through contrastive accuracy and score margins for category-specific sensitivity. BGE-M3 achieved the highest accuracy among embedding models at 89.30 percent, while COMETKiwi achieved 94.49 percent. Embedding models detected explicit factual and lexical changes more reliably than tense-and-aspect and pronoun-coreference errors. COMETKiwi improved performance on several difficult categories, including tense and aspect, pronoun and coreference, and semantic-role errors, but showed lower sensitivity to date-and-time errors and underperformed the embedding models on numbers. The results show complementary error-sensitivity profiles: multilingual sentence embeddings provide useful semantic adequacy signals but are better suited as components of broader translation-evaluation frameworks than as standalone metrics.

---


### 40. [FairReL: Deepfake Detection using Fairness-Aware Representation Learning](https://arxiv.org/abs/2608.28777)

**<font color=#1a73e8>作者：</font>** Xiaoman Lu, Jiaqi Li, Shuntian Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although recent deepfake detectors achieve high overall accuracy, their errors remain unevenly distributed across demographic subgroups, with real faces from certain groups more often misclassified as fake. Existing fairness-aware detectors typically regularise the entire feature representation, without identifying or controlling the specific components that drive unfair predictions. Such coarse intervention can over-suppress useful forgery cues while leaving demographic structure in component-specific subspaces. To address this, we identify two subgroup-sensitive components: multi-scale spatial features, which encode local facial and forgery patterns, and fine-tuning-induced residual features, which adapt the backbone to the unfair training distribution. We propose FairReL, a fairness-aware representation-learning framework that targets both components with dedicated demographic supervision. FairReL uses an SVD-decomposed foundation-model backbone to isolate the fine-tuning-induced residual representation, and introduces two complementary losses. Group-Conditional Wavelet Decorrelation (GCWD) suppresses subgroup-imbalanced structure across spatial wavelet sub-bands, while Subspace-Localised Mean Alignment (SLMA) aligns subgroup means within each real/fake class in the residual representation. Experiments on FF++, Celeb-DF, DFD and DFDC show that, against the state-of-the-art fairness-aware detector, FairReL improves unseen-dataset AUC by 3.9% while reducing subgroup FPR disparity by 10.2%. Code is available at this https URL .

---


### 41. [Bringing Data to Life: Designing Data Characters for the Emotional Self](https://arxiv.org/abs/2608.28780)

**<font color=#1a73e8>作者：</font>** Diego Abarcar Calugay, Isabella Amador, Keke Wu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Journaling is a common practice for emotional expression, reflection, and processing. However, as entries accumulate, it can become difficult to interpret and compare their affective content, especially since traditional text-based analyses and visualizations often struggle to convey affective nuance. We introduce Data Characters, a visualization approach that represents affective content in journaling through human-like characters. Using a customizable Data Character as a design probe, we investigate the potential of character-based representations for conveying affective experiences and explore what visual encodings emerge through customization. Preliminary walkthroughs with two participants demonstrate the intuitiveness and feasibility of the approach. This work contributes an exploratory approach to studying how affective experiences can be visually represented and encoded through anthropomorphic forms.

---


### 42. [Beyond Representation Learning: A Systematic Study of Joint-Embedding Predictive Generation for 3D Brain MRI](https://arxiv.org/abs/2608.28787)

**<font color=#1a73e8>作者：</font>** Meng Zhou, Wenhao You, Yuxing Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) have primarily been developed for self-supervised representation learning. Denoising JEPA (D-JEPA) recently demonstrated strong generative capabilities on natural images, yet the applicability to 3D medical imaging remains unexplored. Building on the D-JEPA framework, we present Med-D-JEPA, a systematic adaptation and evaluation of joint-embedding predictive generation for 3D brain MRI. Med-D-JEPA operates on continuous latent tokens produced by a 3D KL-regularized adversarial variational autoencoder, and combines masked context prediction, representation-level alignment, per-token diffusion, and iterative next-set-of-token sampling. We evaluate unconditional and class-conditional generation quality on BraTS2019 and OASIS-1 datasets; downstream classification utility; and preliminary whole-tumor segmentation on BraTS2020. Across different generation settings, Med-D-JEPA achieves superior or competitive performance compared to several strong baselines on fidelity and diversity metrics. Compared to training with real samples, Med-D-JEPA-based synthetic pretraining improves classification AUC from 0.63 to 0.85 on BraTS2019 and from 0.78 to 0.87 on OASIS-1. In the segmentation study, pretraining on Med-D-JEPA samples improves Dice from 0.74 to 0.80 and reduces HD95 from 13.40 to 9.56 mm. These findings establish joint-embedding predictive generation as a promising direction for 3D medical image synthesis and encourage further research in this direction.

---


### 43. [Efficient Geothermal Well-Control Optimization via Diffusion-Surrogate Reinforcement Learning](https://arxiv.org/abs/2608.28791)

**<font color=#1a73e8>作者：</font>** Ruimin Dai, Guodong Chen, Randy Harsuko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time decision-making for enhanced geothermal systems (EGS) is challenging because long-term production periods involve high-dimensional control spaces and a large number of time-consuming high-fidelity hydrothermal simulations. Reinforcement learning provides a natural framework for state-dependent sequential control, but direct policy training with numerical simulators is computationally expensive. To address this issue, we propose a diffusion-surrogate guided reinforcement learning framework for long-horizon EGS well-control optimization. The reservoir temperature and pressure fields are used as system states, while injection rates are selected as control actions. A learned surrogate environment is constructed using conditional diffusion models to predict the evolution of reservoir temperature and pressure fields and a separate reward model to estimate the corresponding economic return. The surrogate environment is then integrated with Proximal Policy Optimization (PPO) for efficient policy training. Experiments on a fractured EGS benchmark show that the diffusion surrogate can accurately reproduce reservoir-state evolution over multiple control stages. The resulting surrogate-assisted PPO policy achieves competitive well-control performance compared with direct simulator-based PPO and existing optimization methods, while substantially reducing the dependence on expensive high-fidelity simulations. These results demonstrate the potential of diffusion-based surrogate environments for efficient reinforcement learning in geothermal well-control optimization.

---


### 44. [Blind Stereoscopic Omnidirectional Image Quality Assessment Using Predictive Coding Hierarchy](https://arxiv.org/abs/2608.28798)

**<font color=#1a73e8>作者：</font>** Wei Zhou, André Kaup  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereoscopic omnidirectional images (SOIs) have provided users with newly immersive quality of experience in virtual reality environments. However, developing efficient and accurate perceptual quality assessment metrics for SOIs remains challenging due to many factors such as freely changeable field of views and binocular vision. In this paper, based on the characteristics of the human visual system (HVS), we propose a Predictive Coding Hierarchy-inspired metric (PCH) for blind/no-reference stereoscopic omnidirectional image quality assessment. Motivated by the viewing process of SOIs, the proposed PCH includes a local cyclopean perception module, a global predictive perception module, and a visual quality regressor. First, observers browse different spherical sceneries from viewports, and aggregate the local visual information to infer the perceptual quality of SOIs. Therefore, we extract various viewports, followed by cyclopean conversion and saliency detection to approach the perception and attention of the human brain. After the local aggregation, viewers then infer the global scene in their minds. Based on the binocular mechanism, we fuse left and right views to perform predictive coding hierarchy modelling. Finally, the visual quality regressor is exploited to obtain the ultimate quality score related to both local and global perceptual cues. Extensive experiments demonstrate that the proposed PCH achieves competitive and consistently improved performance compared with state-of-the-art quality assessment methods.

---


### 45. [A Large-scale Evaluation of Text-guided Models for Facial Editing](https://arxiv.org/abs/2608.28802)

**<font color=#1a73e8>作者：</font>** Rahul Nair, Saurav Pandit, Hannah Kerner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial appearance editing powers popular applications like FaceApp and Photoshop. Generative Adversarial Networks (GANs) and 3D Morphable Models (3DMMs) have been widely used for facial editing. GANs can perform varied facial edits (e.g., changing hair color, hairstyle), but often produce unstable edits. 3DMMs produce stable edits, but can only alter pose and facial expression. Recently, text-guided diffusion models like Nano Banana have become popular for image editing. Text-guided models are a compelling alternative to GANs and 3DMMs since they can produce both stable and varied image edits. While text-guided models have been widely tested for whole-scene edits (e.g., ``make the woman play a guitar''), they have not been comprehensively tested for facial editing. We conducted the first large-scale evaluation ($\sim1$M images evaluated) of six popular text-guided models on a sequential facial editing task. We present Face-Edit-Attributes, the largest collection of $169$ facial editing attributes focused on hair, accessories, and pose edits. We compared model performance using two popular celebrity face datasets: CelebA and CelebSET. Our results show that most models performed hair and accessory edits well, but struggled with editing pose. All models over-edit (e.g., changing hair color when asked only to change the hairstyle). We also evaluated demographic biases in each model. Our results show surprising biases in overediting: almost all models created more overedits for dark-skinned male faces and old faces. The code and data for our results (including our repository of $\sim 1$M images) can be accessed \href{this https URL}{\textcolor{blue}{here}}.

---


### 46. [FigMirror: Ground It, Code It, Plot It](https://arxiv.org/abs/2608.28814)

**<font color=#1a73e8>作者：</font>** Xiaohan Zhao, Jiacheng Liu, Yaxin Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Converting scientific figures into executable code has gained increasing attention, yet existing methods primarily focus on reproducing the reference figure itself. A more practical setting is to plot new data while preserving the visual style of a reference figure (e.g., color scheme and typography). Prior approaches mimic the reference through pixel-level optimization and struggle to carry its style to new data. We show that the key to this task lies in the coordinate grounding and coding capabilities present in modern computer-use models. We propose FigMirror, an agentic framework that unlocks these capabilities through Grounded Measurement, which locates visual elements by coordinates and measures their properties through executable code. We further introduce PlotTwin-Bench, an expert-curated benchmark with fine-grained code and image-level style metrics. Experiments show that FigMirror consistently outperforms existing methods on reference-conditioned style transfer. All plots in this paper are generated by FigMirror, except those produced by other methods for comparison. Our code and data are available at: this https URL.

---


### 47. [Explainable Artificial Intelligence (XAI) in Computational Pathology: Definitions, Taxonomy, and Recommendations](https://arxiv.org/abs/2608.28820)

**<font color=#1a73e8>作者：</font>** Shubham Innani, Suhang You, Adam Shephard 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational pathology (CompPath) is transforming medicine by leveraging artificial intelligence (AI) algorithms to support diagnosis, prognosis, and treatment prediction from gigapixel whole-slide images. Clinical adoption is progressing, but is constrained by concerns about safety, accountability, and regulatory oversight in high-stakes clinical environments. Explainable AI (XAI) systems hold promise for building trust and enabling verification, yet the literature remains fragmented due to inconsistent terminology, overlapping methodological families, ad hoc validation, and current reviews. This review aims to formalize XAI methods in CompPath through the: i) introduction of a pathology-centric vocabulary comprising seven core terms; ii) development of a taxonomy across methodological families and three orthogonal axes (stage, type, scope); and iii) establishment of a task-driven framework that maps five clinical questions to recommended methods, method evaluation, and deployment context. Five key gaps between current XAI capabilities and clinical deployment are identified, and actionable steps are proposed to advance XAI for CompPath.

---


### 48. [Text-Driven Artistic Staging: Pose, Lighting, and Camera References from Paintings](https://arxiv.org/abs/2608.28823)

**<font color=#1a73e8>作者：</font>** Yunge Wen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artists coordinate human pose, illumination, and camera placement to convey narrative and emotion, but existing generative methods typically model these elements independently. We introduce text-to-editable 3D staging, a task that jointly generates human poses, a dominant light, and a camera configuration from an affective description. We construct 11,911 text--staging pairs from 2,328 figurative paintings by reconstructing SMPL bodies, estimating low-frequency illumination, recovering camera parameters, and pairing each scene with ArtEmis descriptions. We train a flow-matching transformer that supports variable numbers of figures and produces multiple staging alternatives for each prompt. On held-out descriptions, the model achieves 32.2\% retrieval R@1, compared with 16.6\% for CLIP-based nearest-neighbor retrieval, while approximately preserving corpus-level diversity. These results demonstrate the feasibility of generating editable, emotionally conditioned 3D staging references from text.

---


### 49. [BlobBoards: Robust Markers for Accurate Pose](https://arxiv.org/abs/2608.28830)

**<font color=#1a73e8>作者：</font>** James Pritts, Till Sittart, Hendrik Sauer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose BlobBoards, a fiducial marker system comprising a dense, multi-scale field of Gaussian blobs and a feature-based pipeline for joint detection, identification, and pose estimation. Each board is registered from hundreds of blob features whose dense spatial coverage constrains pose, while multiple scales preserve detectability across large changes in focal length, distance, and obliquity. Learned local descriptors are matched to the reference pattern and spatially verified, so the correspondences determine pose and certify identity. Against motion-capture ground truth, BlobBoards achieve median translation errors of 3.6-5.0 mm, reducing AprilTag's median translation error by 89% on small boards and 70% on large ones. They also produce far fewer large-rotation failures than state-of-the-art tag systems. BlobBoards achieve the highest detection rate, 80% versus 74% for AprilTag and 58% for ArUco, with the largest margin on the smallest markers. Under 50% occlusion, they still detect 69% of boards with essentially unchanged median translation error, while AprilTag and ArUco detect none. In experiments BlobBoards give state-of-the-art detection rate, pose accuracy and occlusion robustness.

---


### 50. [Unsupervised Latent Space Alignment with Hyperspherical Geodesic Matching](https://arxiv.org/abs/2608.28840)

**<font color=#1a73e8>作者：</font>** Cameron Ryan, Vivek Sivaraman Narayanaswamy, Kowshik Thopalli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Independently trained neural networks tend to encode the same data with similar latent geometries. These latent geometries are not directly compatible, yet they can be nearly the same up to some class of transformations. While there exists many methods for alignment between different latent spaces, it is typically done using a set of shared sample correspondences, known as anchors. This leaves a fundamental question: are the geometric signatures of different latent spaces representing similar data sufficient to recover an alignment between them? To that end, we introduce HGA (Hyperspherical Gaussian Alignment), a method that directly optimizes a transformation between two latent spaces by maximizing a geometric measure of "fit" between them. Since it is driven by the geometry of the latent spaces rather than paired data, HGA can operate in both an unsupervised and weakly supervised regime. On tasks such as model stitching or multilingual word embedding correspondence recovery, HGA manages to match supervised results with minimal or no supervision.

---


> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
