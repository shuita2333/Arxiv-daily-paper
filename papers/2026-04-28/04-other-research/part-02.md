# 📦 其他研究 | 2026年04月28日

> 本类共 **154** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-154](./part-04.md)

---

### 51. [From Global to Local: Rethinking CLIP Feature Aggregation for Person Re-Identification](https://arxiv.org/abs/2604.22190)

**<font color=#1a73e8>作者：</font>** Aotian Zheng, Winston Sun, Bahaa Alattar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP-based person re-identification (ReID) methods aggregate spatial features into a single global \texttt{[CLS]} token optimized for image-text alignment rather than spatial selectivity, making representations fragile under occlusion and cross-camera variation. We propose SAGA-ReID, which reconstructs identity representations by aligning intermediate patch tokens with anchor vectors parameterized in CLIP's text embedding space -- emphasizing spatially stable evidence while suppressing corrupted or absent regions, without requiring textual descriptions of individual images. Controlled experiments isolate the aggregation mechanism under two qualitatively distinct conditions -- synthetic masking, where identity signal is absent, and realistic human distractors, where an overlapping person introduces semantically confusing signal -- with SAGA's advantage over global pooling growing substantially as occlusion increases across both conditions. Benchmark evaluations confirm consistent gains over CLIP-ReID across standard and occluded settings, with the largest improvements where global pooling is most unreliable: up to +10.6 Rank-1 on occluded benchmarks. SAGA's aggregation outperforms dedicated sequential patch aggregation on a stronger backbone, confirming that structured reconstruction addresses a bottleneck that backbone quality and architectural complexity alone cannot resolve. Code available at this https URL.

---


### 52. [ArchSym: Detecting 3D-Grounded Architectural Symmetries in the Wild](https://arxiv.org/abs/2604.22202)

**<font color=#1a73e8>作者：</font>** Hanyu Chen, Ruojin Cai, Steve Marschner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Symmetry detection is a fundamental problem in computer vision, and symmetries serve as powerful priors for downstream tasks. However, existing learning-based methods for detecting 3D symmetries from single images have been almost exclusively trained and evaluated on object-centric or synthetic datasets, and thus fail to generalize to real-world scenes. Furthermore, due to the inherent scale ambiguity of monocular inputs, which makes localizing the 3D plane an ill-posed problem, many existing works only predict the plane's orientation. In this paper, we address these limitations by presenting the first framework for detecting 3D-grounded reflectional symmetries from single, in-the-wild RGB images, focusing on architectural landmarks. We introduce two key innovations: (1) a scalable data annotation pipeline to automatically curate a large-scale dataset of architectural symmetries, ArchSym, from SfM reconstructions by leveraging cross-view image matching; and building on the dataset, (2) a single-view symmetry detector that accurately localizes symmetries in 3D by parameterizing them as signed distance maps defined relative to predicted scene geometry. We validate our symmetry annotation pipeline against geometry-based alternatives and demonstrate that our symmetry detector significantly outperforms state-of-the-art baselines on our new benchmark.

---


### 53. [ArguMath: AI-Simulated Environment for Pre-Service Teacher Training in Orchestrating Classroom Mathematics Argumentation](https://arxiv.org/abs/2604.22205)

**<font color=#1a73e8>作者：</font>** Jiwon Chun, Yuling Zhuang, Armanto Sutedjo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Facilitating productive mathematical argumentation, especially asking rational questions, is essential yet remains challenging for pre-service mathematics teachers (PMTs), who often have limited opportunities to apply abstract theoretical knowledge in authentic practice. At the same time, recent advances in large language models (LLMs) have expanded the potential for simulating students in educational settings, enabling low-risk environments for instructional practice. To inform the design of a system that supports PMTs in orchestrating classroom argumentation, we conducted a formative study with eight experienced mathematics teachers to identify key design requirements, including personalization, realistic simulations, structured reflection, and ease of use. Building on these requirements, we developed ArguMath, an AI-simulated classroom environment that supports PMTs in practicing the orchestration of mathematical argumentation. ArguMath comprises three core components: (1) customization of classroom settings; (2) simulation of classroom discussions with AI-based students grounded in authentic transcripts and augmented with real-time instructional suggestions; and (3) structured reflection through discourse annotation and overall feedback. Results from an exploratory user study with seven PMTs, complemented by interviews with four experienced teachers, indicate that ArguMath has the potential to support PMTs' classroom orchestration skills, particularly theory-aligned questioning strategies.

---


### 54. [Breaking Watermarks in the Frequency Domain: A Modulated Diffusion Attack Framework](https://arxiv.org/abs/2604.22220)

**<font color=#1a73e8>作者：</font>** Chunpeng Wang, Binyan Qu, Xiaoyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital image watermarking has advanced rapidly for copyright protection of generative AI, yet the comparatively limited progress in watermark attack techniques has broken the attack-defense balance and hindered further advances in the field. In this paper, we propose FMDiffWA, a frequency-domain modulated diffusion framework for watermark attacks. Specifically, we introduce a frequency-domain watermark modulation (FWM) module and incorporate it into the sampling stages both the forward and reverse diffusion processes. This mechanism enables selective modulation of watermark-related frequency components, thereby allowing FMDiffWA to effectively neutralize the invisible watermark signals while preserving the perceptual quality of the attacked watermarked images. To achieve a better trade-off between attack efficacy and visual fidelity, we reformulate the training strategy of conventional diffusion models by augmenting the canonical noise estimation objective with an auxiliary refinement constraint. Comprehensive experiments demonstrate that FMDiffWA achieves superior visual fidelity compared to existing watermark attacks, while exhibiting strong generalization across diverse watermarking schemes.

---


### 55. [TTS-PRISM: A Perceptual Reasoning and Interpretable Speech Model for Fine-Grained Diagnosis](https://arxiv.org/abs/2604.22225)

**<font color=#1a73e8>作者：</font>** Xi Wang, Jie Wang, Xingchen Song 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While generative text-to-speech (TTS) models approach human-level quality, monolithic metrics fail to diagnose fine-grained acoustic artifacts or explain perceptual collapse. To address this, we propose TTS-PRISM, a multi-dimensional diagnostic framework for Mandarin. First, we establish a 12-dimensional schema spanning stability to advanced expressiveness. Second, we design a targeted synthesis pipeline with adversarial perturbations and expert anchors to build a high-quality diagnostic dataset. Third, schema-driven instruction tuning embeds explicit scoring criteria and reasoning into an efficient end-to-end model. Experiments on a 1,600-sample Gold Test Set show TTS-PRISM outperforms generalist models in human alignment. Profiling six TTS paradigms establishes intuitive diagnostic flags that reveal fine-grained capability differences. TTS-PRISM is open-source, with code and checkpoints at this https URL.

---


### 56. [Preserve Support, Not Correspondence: Dynamic Routing for Offline Reinforcement Learning](https://arxiv.org/abs/2604.22229)

**<font color=#1a73e8>作者：</font>** Zhancun Mu, Guangyu Zhao, Yiwu Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-step offline RL actors are attractive because they avoid backpropagating through long iterative samplers and keep inference cheap, but they still have to improve under a critic without drifting away from actions that the dataset can support. In recent one-step extraction pipelines, a strong iterative teacher provides one target action for each latent draw, and the same student output is asked to do both jobs: move toward higher Q and stay near that paired endpoint. If those two directions disagree, the loss resolves them as a compromise on that same sample, even when a nearby better action remains locally supported by the data. We propose DROL, a latent-conditioned one-step actor trained with top-1 dynamic routing. For each state, the actor samples $K$ candidate actions from a bounded latent prior, assigns each dataset action to its nearest candidate, and updates only that winner with Behavior Cloning and critic guidance. Because the routing is recomputed from the current candidate geometry, ownership of a supported region can shift across candidates over the course of learning. This gives a one-step actor room to make local improvements that pointwise extraction struggles to capture, while retaining single-pass inference at test time. On OGBench and D4RL, DROL is competitive with the one-step FQL baseline, improving many OGBench task groups while remaining strong on both AntMaze and Adroit. Project page: this https URL.

---


### 57. [Navigating Large-Scale Document Collections: MuDABench for Multi-Document Analytical QA](https://arxiv.org/abs/2604.22239)

**<font color=#1a73e8>作者：</font>** Zhanli Li, Yixuan Cao, Lvzhou Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces the task of analytical question answering over large, semi-structured document collections. We present MuDABench, a benchmark for multi-document analytical QA, where questions require extracting and synthesizing information across numerous documents to perform quantitative analysis. Unlike existing multi-document QA benchmarks that typically require information from only a few documents with limited cross-document reasoning, MuDABench demands extensive inter-document analysis and aggregation. Constructed via distant supervision by leveraging document-level metadata and annotated financial databases, MuDABench comprises over 80,000 pages and 332 analytical QA instances. We also propose an evaluation protocol that measures final answer accuracy and uses intermediate-fact coverage as an auxiliary diagnostic signal for the reasoning process. Experiments reveal that standard RAG systems, which treat all documents as a flat retrieval pool, perform poorly. To address these limitations, we propose a multi-agent workflow that orchestrates planning, extraction, and code generation modules. While this approach substantially improves both process and outcome metrics, a significant gap remains compared to human expert performance. Our analysis identifies two primary bottlenecks: single-document information extraction accuracy and insufficient domain-specific knowledge in current systems. MuDABench is available at this https URL.

---


### 58. [OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space](https://arxiv.org/abs/2604.22240)

**<font color=#1a73e8>作者：</font>** Zhuding Liang, Tianyi Yan, Dubing Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world models increasingly rely on 4D occupancy for realistic autonomous driving simulation. However, existing generation frameworks depend on rigid geometric conditions (e.g., explicit trajectories) or simplistic attribute-level text, failing to orchestrate complex, sequential multi-agent interactions. To address this semantic-spatiotemporal gap, we propose OccDirector, a pioneering framework that generates 4D occupancy dynamics conditioned solely on natural language. Operating as a ``scenario director'', OccDirector maps natural language scripts into physically plausible voxel dynamics without requiring geometric priors. Technically, it employs a VLM-driven Spatio-Temporal MMDiT equipped with a history-prefix anchoring strategy to ensure long-horizon interaction consistency. Furthermore, we introduce OccInteract-85k, a novel dataset uniquely annotated with multi-level language instructions: ranging from static layouts to intricate multi-agent behaviors, alongside a novel VLM-based evaluation benchmark. Extensive experiments demonstrate that OccDirector achieves state-of-the-art generation quality and unprecedented instruction-following capabilities, successfully shifting the paradigm from appearance synthesis to language-driven behavior orchestration.

---


### 59. [Fast Neural-Network Approximation of Active Target Search Under Uncertainty](https://arxiv.org/abs/2604.22254)

**<font color=#1a73e8>作者：</font>** Bilal Yousuf, Zsofia Lendek, Lucian Busoniu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of searching for an unknown number of stationary targets at unknown positions with a mobile agent. A probability hypothesis density filter is used to estimate the expected number of targets under measurement uncertainty. Existing planners, such as Active Search (AS) and its Intermittent variant (ASI), achieve accurate detection but require costly online optimization. To reduce online computation, we propose to use a convolutional neural network to approximate AS or ASI decisions through direct inference. The network is trained on AS/ASI data using a multi-channel grid that encodes target beliefs, the agent position, visitation history, and boundary information. Simulations with uniform and clustered target distributions show that the network achieves detection rates comparable to AS or ASI while reducing computation by orders of magnitude.

---


### 60. [Protect the Brain When Treating the Heart: A Convolutional Neural Network for Detecting Emboli](https://arxiv.org/abs/2604.22258)

**<font color=#1a73e8>作者：</font>** Andrea Angino, Ken Trotti, Diego Ulisse Pizzagalli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaseous microemboli (GME) represent a common complication of cardiac structural interventions across both surgical and transcatheter approaches. Transthoracic cardiac ultrasound imaging represents a convenient methodology to visualize the presence of circulating GME. However, their detection and quantification are far from trivial due to operator-dependent view, high velocity, and objects with similar structure in the background. Here, we propose an approach based on a 2.5D U-Net architecture to segment GME in space-time connected data. Such an approach yields robust detection against the background and high segmentation accuracy while retaining real-time execution speed. These properties facilitated the integration of the proposed pipeline into patient-monitoring surgical protocols, providing the quantification of GME area over time.

---


### 61. [CAGE-SGG: Counterfactual Active Graph Evidence for Open-Vocabulary Scene Graph Generation](https://arxiv.org/abs/2604.22274)

**<font color=#1a73e8>作者：</font>** Suiyang Guang, Chenyu Liu, Ruohan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary scene graph generation (SGG) aims to describe visual scenes with flexible and fine-grained relation phrases beyond a fixed predicate vocabulary. While recent vision-language models greatly expand the semantic coverage of SGG, they also introduce a critical reliability issue: predicted relations may be driven by language priors or object co-occurrence rather than grounded visual evidence. In this paper, we propose an evidence-rounded open-vocabulary SGG framework based on counterfactual relation verification. Instead of directly accepting plausible relation proposals, our method verifies whether each candidate relation is supported by relation-pecific visual, geometric, and contextual evidence. Specifically, we first generate open-vocabulary relation candidates with a vision-language proposer, then decompose predicate phrases into soft evidence bases such as support, contact, containment, depth, motion, and state. A relation-conditioned evidence encoder extracts predicate-relevant cues, while a counterfactual verifier tests whether the relation score decreases when necessary vidence is removed and remains stable under irrelevant perturbations. We further introduce contradiction-aware predicate learning and graph-level preference optimization to improve fine-grained discrimination and global graph consistency. Experiments on conventional, open-vocabulary, and panoptic SGG benchmarks show that our method consistently improves standard recall-based metrics, unseen predicate generalization, and counterfactual grounding quality. These results demonstrate that moving from relation generation to relation verification leads to more reliable, interpretable, and evidence-grounded scene graphs.

---


### 62. [Multi-Agent Consensus as a Cognitive Bias Trigger in Human-AI Interaction](https://arxiv.org/abs/2604.22277)

**<font color=#1a73e8>作者：</font>** Soohwan Lee, Kyungho Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As multi-agent AI systems become more common, users increasingly encounter not a single AI voice but a collective one. This shift introduces social dynamics, such as consensus, dissent, and gradual convergence, that can trigger cognitive biases and distort human judgment. We present findings from a controlled experiment (N = 127) comparing three multi-agent configurations: Majority, Minority, and Diffusion. Quantitative results show that majority consensus accelerates opinion change and inflates confidence, consistent with social proof and bandwagon heuristics. Minority dissent slows this process and promotes more deliberative engagement. Qualitative analysis identifies three interpretive trajectories: reinforcing, aligning, and oscillating, shaped by how users interpret agent independence and group dynamics over time. These findings suggest that agent agreement structure, independent of content, functions as a bias-relevant signal in LLM interactions. We hope this work contributes to the Bias4Trust agenda by grounding multi-agent social influence as a concrete and designable source of bias in human-AI interaction.

---


### 63. [DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](https://arxiv.org/abs/2604.22281)

**<font color=#1a73e8>作者：</font>** Joonmyung Choi, Sanghyeok Lee, Jongha Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models have demonstrated remarkable performance across diverse multi-modal tasks, including document question answering that leverages structured visual cues from text, tables, and figures. However, unlike natural images, document images contain large backgrounds and only sparse supporting evidence, leading to the inefficient consumption of substantial computational resources, especially for long documents. We observe that existing token-reduction methods for natural images and videos fall short in utilizing the structural sparsity unique to documents. To address this, we propose DocPrune, a training-free and progressive document token pruning framework designed for efficient long-document understanding. The proposed method preserves only the essential tokens for the task while removing unnecessary ones, such as background or question-irrelevant tokens. Moreover, it automatically selects the appropriate layers to initiate token pruning based on the model's level of comprehension. Our experiments on the M3DocRAG show that DocPrune improves throughput by 3.0x and 3.3x in the encoder and decoder, respectively, while boosting the F1 score by +1.0, achieving both higher accuracy and efficiency without any additional training.

---


### 64. [ReLeVAnT: Relevance Lexical Vectors for Accurate Legal Text Classification](https://arxiv.org/abs/2604.22292)

**<font color=#1a73e8>作者：</font>** Ishaan Gakhar, Harsh Nandwani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The classification of legal documents from an unstructured data corpus has several crucial applications in downstream tasks. Documents relevant to court filings are key in use cases such as drafting motions, memos, and outlines, as well as in tasks like docket summarisation, retrieval systems, and training data curation. Current methods classify based on provided metadata, LLM-extracted metadata, or multimodal methods. These methods depend on structured data, metadata, and extensive computational power. This task is approached from a perspective of leveraging discriminative features in the documents between classes. The authors propose ReLeVAnT, a framework for legal document binary classification. ReLeVAnT utilises n-gram processing, contrastive score matching, and a shallow neural network as the primary drivers for discriminative classification. It leverages one-time keyword extraction per corpus, followed by a shallow classifier to swiftly and reliably classify documents with 99.3% accuracy and 98.7% F1 score on the LexGLUE dataset.

---


### 65. [Contexts are Never Long Enough: Structured Reasoning for Scalable Question Answering over Long Document Sets](https://arxiv.org/abs/2604.22294)

**<font color=#1a73e8>作者：</font>** Harshit Joshi, Priyank Shethia, Jadelynn Dao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world document question answering is challenging. Analysts must synthesize evidence across multiple documents and different parts of each document. However, any fixed LLM context window can be exceeded as document collections grow. A common workaround is to decompose documents into chunks and assemble answers from chunk-level outputs, but this introduces an aggregation bottleneck: as the number of chunks grows, systems must still combine and reason over an increasingly large body of extracted evidence. We present SLIDERS, a framework for question answering over long document collections through structured reasoning. SLIDERS extracts salient information into a relational database, enabling scalable reasoning over persistent structured state via SQL rather than concatenated text. To make this locally extracted representation globally coherent, SLIDERS introduces a data reconciliation stage that leverages provenance, extraction rationales, and metadata to detect and repair duplicated, inconsistent, and incomplete records. SLIDERS outperforms all baselines on three existing long-context benchmarks, despite all of them fitting within the context window of strong base LLMs, exceeding GPT-4.1 by 6.6 points on average. It also improves over the next best baseline by ~19 and ~32 points on two new benchmarks at 3.9M and 36M tokens, respectively.

---


### 66. [Evaluation of image simulation open source solutions for simulation of synthetic images in lunar environment](https://arxiv.org/abs/2604.22296)

**<font color=#1a73e8>作者：</font>** Jai G Singla, Hinal B Patel, Nitant Dube  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic image generation is one of the crucial input for planetary missions. It enables researchers and engineers to visualize planned planetary missions, test imaging systems and plan exploration activities in a virtual environment before actual deployment. Image simulation is essential for assessing landing sites, detecting hazards, and validating navigation systems in a missions. This study offers a detailed evaluation of various image simulation approaches for the lunar environment, with particular emphasis on the effects of different camera models and light illumination conditions on the quality of synthetic lunar images. These images are produced using real Digital Elevation Models (DEM) and terrain data derived from instruments such as Chandrayaan-2 Orbiter High Resolution Camera (OHRC) and NASA's Wide Angle Camera (WAC), and Narrow Angle Camera (NAC) instruments. This research aims to improve the reliability of synthetic imagery in supporting autonomous navigation and decision-making systems in lunar exploration. This work contributes to the development of more effective tools for generating important information for future lunar missions and enhances the understanding of the moon's surface environment.

---


### 67. [Knowledge Visualization: A Benchmark and Method for Knowledge-Intensive Text-to-Image Generation](https://arxiv.org/abs/2604.22302)

**<font color=#1a73e8>作者：</font>** Ran Zhao, Sheng Jin, Size Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image (T2I) models have demonstrated impressive capabilities in photorealistic synthesis and instruction following. However, their reliability in knowledge-intensive settings remains largely unexplored. Unlike natural image generation, knowledge visualization requires not only semantic alignment but also strict adherence to domain knowledge, structural constraints, and symbolic conventions, exposing a critical gap between visual plausibility and scientific correctness. To systematically study this problem, we introduce KVBench, a curriculum-grounded benchmark for evaluating knowledge-intensive T2I generation. KVBench covers six senior high-school subjects: Biology, Chemistry, Geography, History, Mathematics, and Physics. The benchmark consists of 1,800 expert-curated prompts derived from over 30 authoritative textbooks. Using this benchmark, we evaluate 14 state-of-the-art open- and closed-source models, revealing substantial deficiencies in logical reasoning, symbolic precision, and multilingual robustness, with open-source models consistently underperforming proprietary systems. To address these limitations, we further propose KE-Check, a two-stage framework that improves scientific fidelity via (1) Knowledge Elaboration for structured prompt enrichment, and (2) Checklist-Guided Refinement for explicit constraint enforcement through violation identification and constraint-guided editing. KE-Check effectively mitigates scientific hallucinations, narrowing the performance gap between open-source and leading closed-source models. Data and codes are publicly available at this https URL.

---


### 68. [Resource-Aware Layered Intrusion Detection Allocation Model](https://arxiv.org/abs/2604.22304)

**<font color=#1a73e8>作者：</font>** Ioan Pădurean, Béla Genge, Roland Bolboacă  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper proposes a resource-aware allocation model for layered intrusion detection in het erogeneous networks. Monitoring traffic at higher protocol layers improves the ability to detect sophisticated attacks, but it also increases computational and storage costs. The problem is formu lated as an integer linear program that assigns a single monitoring depth, ranging from Ethernet to the application layer, to each device, while accounting for device importance, attack probability, layer-dependent detection rates, and per-layer monitoring costs. The model further enforces a global resource budget, a minimum monitoring level for critical devices, and maximum-feasibility limits for constrained devices such as simple IoT sensors. The formulation is solved with the SCIP optimization framework on a small heterogeneous network of six devices, and the resulting allocation illustrates how the model concentrates monitoring effort on important and high-risk devices while respecting feasibility and budget constraints.

---


### 69. [Introducing the Cyber-Physical Data Flow Diagram to Improve Threat Modelling of Internet of Things Devices](https://arxiv.org/abs/2604.22307)

**<font color=#1a73e8>作者：</font>** Simon Liebl, Ian Ferguson, Andreas Aßmuth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A growing number of Internet of Things (IoT) devices are used across consumer, medical, and industrial domains. They interact with their environment through sensors and actuators and connect to networks such as the Internet. Because sensors may collect sensitive data and actuators can trigger physical actions, security, privacy, and safety are major challenges. Threat modelling can help identify risks, but established IT-focused methods transfer to the IoT only to a limited extent. In this paper, a new modelling technique specifically for IoT devices called Cyber-Physical Data Flow Diagram (CPDFD) is proposed that also allows modelling of hardware with the aim to support manufacturers in identifying threats and developing countermeasures. The technique was examined through an experimental study and a survey with interviews. The results suggest that numerous other attack scenarios can be found through the modelling technique, improving the identification of threats to IoT devices.

---


### 70. [Revisiting Geometric Obfuscation with Dual Convergent Lines for Privacy-Preserving Image Queries in Visual Localization](https://arxiv.org/abs/2604.22310)

**<font color=#1a73e8>作者：</font>** Jeonggon Kim, Heejoon Moon, Je Hyeong Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Privacy-Preserving Image Queries (PPIQ) are an emerging mechanism for cloud-based visual localization, enabling pose estimation from obfuscated features instead of private images or raw keypoints. However, the main approaches for PPIQ, primarily geometry-based and segmentation-based obfuscation, both suffer from vulnerabilities to recent privacy attacks. In particular, a fundamental limitation of geometry-based obfuscation is that the spatial distribution of obfuscated neighboring lines still effectively surrounds the original keypoint location, providing exploitable cues for recovering the original points. We revisit this geometric paradigm and introduce Dual Convergent Lines (DCL), a novel keypoint obfuscation method demonstrating strong resilience against such attack. DCL places two fixed anchors on a central partition line and lifts each keypoint to a line originating from one of them, with the active anchor determined by the keypoint's location. This arrangement invalidates the geometry-recovery attack by making its optimization ill-posed: Neighboring lines either misleadingly converge to one anchor, yielding a trivial solution, or become near-parallel at the partition boundary, yielding an unstable high-variance solution. Both outcomes thwart point recovery. DCL is also compatible with an existing line-based solver, enabling deployment in traditional localization pipelines. Experiments on both indoor and large-scale outdoor datasets demonstrate DCL's robustness against privacy attacks, efficiency, and scalability, while achieving practical localization performance.

---


### 71. [CLARITY: A Framework and Benchmark for Conversational Language Ambiguity and Unanswerability in Interactive NL2SQL Systems](https://arxiv.org/abs/2604.22313)

**<font color=#1a73e8>作者：</font>** Tabinda Sarwar, Farhad Moghimifar, Cong Duy Vu Hoang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> NL2SQL systems deployed in industry settings often encounter ambiguous or unanswerable queries, particularly in interactive scenarios with incomplete user clarification. Existing benchmarks typically assume a single source of ambiguity and rely on user interaction for resolution, overlooking realistic failure modes.
We introduce Clarity, a framework for automatically generating an NL2SQL benchmark with multi-faceted ambiguities and diverse user behaviors across both single- and multi-turn settings. Using a constraint-driven pipeline, Clarity transforms executable SQL into ambiguous queries, augmented with grounded conversational continuations and schema-level metadata.
Empirical evaluation on Spider and BIRD shows that leading NL2SQL systems, including those based on strong LLMs, suffer significant performance degradation under multi-faceted ambiguity. While these systems often detect ambiguity, they struggle to accurately localize and resolve the underlying schema-level sources. Our results highlight the need for more robust ambiguity detection and resolution in industry-grade NL2SQL systems.

---


### 72. [Rethinking AI-Mediated Minority Support in Power-Imbalanced Group Decision-Making: From Anonymity To Authenticity](https://arxiv.org/abs/2604.22319)

**<font color=#1a73e8>作者：</font>** Soohwan Lee, Kyungho Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-mediated Communication (AIMC) systems increasingly aim to protect minority voices by anonymizing or proxying their input, but anonymity and authenticity are not the same construct. This position paper draws on an ongoing empirical study comparing two LLM-powered minority support strategies in hierarchical group decision-making. We found that relaying minority input anonymously through AI increased participation but significantly reduced psychological safety and satisfaction, while generating only autonomous counterarguments improved satisfaction and reduced marginalization. These counterintuitive findings reveal three provocations for AIMC design in hierarchical contexts: the inherent trade-offs among anonymity, authenticity, agency, and accountability; the risk that power asymmetry reverses intended effects; and the need for AI to facilitate group reflection rather than substitute for human responsibility. These findings and provocations are offered as a contribution to the Restoring Human Authenticity in AI-Mediated Communication workshop.

---


### 73. [A Brain-Inspired Deep Separation Network for Single Channel Raman Spectra Unmixing](https://arxiv.org/abs/2604.22324)

**<font color=#1a73e8>作者：</font>** Gaoruishu Long, Jinchao Liu, Bo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Raman spectra obtained in real world applications are often a noisy combination of several spectra of various substances in a tested sample. Unmixing such spectra into individual components corresponding to each of the substances is of great value and has been a longstanding challenge in Raman spectroscopy. Existing unmixing methods are predominantly designed to invert an overdetermined mixed model and therefore require multiple mixed spectra as input. However, open domain and/or non-cooperative detection applications in Raman spectroscopy such as controlled substance detection, call for single-channel solutions which can identify individual components from thousands of candidates by analyzing only a single noisy mixed spectrum. To our knowledge, sparse regression is the only existing solution which can cope with this scenario, yet it has very low tolerance to noises and can hardly be applicable in practice. To address these limitations, we introduce a novel neural approach for single-channel Raman spectrum unmixing inspired by speech separation. It aims at solving underdetermined systems and can decompose a noisy mixed spectrum from a library of thousands of components (substances). The core of our method is a deep separation neural network (RSSNet) which takes a mixed spectrum as input and outputs spectra of pure components. We created two synthetic datasets of single-channel Raman spectra unmixing and demonstrated feasibility and superiority of RSSNet on these datasets (outperform competing methods by >4dB). Furthermore, we verified that RSSNet, trained solely on synthetic data, can successfully unmix real-world mixed spectra of mixtures of mineral powders, exhibiting strong generalization. Our approach represents a new paradigm for Raman unmixing and enables new possibilities for fast detection of Raman mixtures.

---


### 74. [Depth-Aware Rover: A Study of Edge AI and Monocular Vision for Real-World Implementation](https://arxiv.org/abs/2604.22331)

**<font color=#1a73e8>作者：</font>** Lomash Relia, Jai G Singla, Amitabh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study analyses simulated and real-world implementations of depth-aware rover navigation, highlighting the transition from stereo vision to monocular depth estimation using edge AI. A Unity-based lunar terrain simulator with stereo cameras and OpenCV's StereoSGBM was used to generate disparity maps. A physical rover built on Raspberry Pi 4 employed UniDepthV2 for monocular metric depth estimation and YOLO12n for real-time object detection. While stereo vision yielded higher accuracy in simulation, the monocular approach proved more robust and cost-effective in real-world deployment, achieving 0.1 FPS for depth and 10 FPS for detection.

---


### 75. [ChangeQuery: Advancing Remote Sensing Change Analysis for Natural and Human-Induced Disasters from Visual Detection to Semantic Understanding](https://arxiv.org/abs/2604.22333)

**<font color=#1a73e8>作者：</font>** Dongwei Sun, Jing Yao, Kan Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid situational awareness is critical in post-disaster response. While remote sensing damage assessment is evolving from pixel-level change detection to high-level semantic analysis, existing vision-language methodologies still struggle to provide actionable intelligence for complex strategic queries. They remain severely constrained by unimodal optical dependence, a prevailing bias towards natural disasters, and a fundamental lack of grounded interactivity. To address these limitations, we present ChangeQuery, a unified multimodal framework designed for comprehensive, all-weather disaster situation awareness. To overcome modality constraints and scenario biases, we construct the Disaster-Induced Change Query (DICQ) dataset, a large-scale benchmark coupling pre-event optical semantics with post-event SAR structural features across a balanced distribution of natural catastrophes and armed conflicts. Furthermore, to provide the high-quality supervision required for interactive reasoning, we propose a novel Automated Semantic Annotation Pipeline. Adhering to a ``statistics-first, generation-later'' paradigm, this engine automatically transforms raw segmentation masks into grounded, hierarchical instruction sets, effectively equipping the model with fine-grained spatial and quantitative awareness. Trained on this structured data, the ChangeQuery architecture operates as an interactive disaster analyst. It supports multi-task reasoning driven by diverse user queries, delivering precise damage quantification, region-specific descriptions, and holistic post-disaster summaries. Extensive experiments demonstrate that ChangeQuery establishes a new state-of-the-art, providing a robust and interpretable solution for complex disaster monitoring. The code is available at \href{this https URL}{this https URL}.

---


### 76. [FILTR: Extracting Topological Features from Pretrained 3D Models](https://arxiv.org/abs/2604.22334)

**<font color=#1a73e8>作者：</font>** Louis Martinez, Maks Ovsjanikov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in pretraining 3D point cloud encoders (e.g., Point-BERT, Point-MAE) have produced powerful models, whose abilities are typically evaluated on geometric or semantic tasks. At the same time, topological descriptors have been shown to provide informative summaries of a shape's multiscale structure. In this paper we pose the question whether topological information can be derived from features produced by 3D encoders. To address this question, we first introduce DONUT, a synthetic benchmark with controlled topological complexity, and propose FILTR (Filtration Transformer), a learnable framework to predict persistence diagrams directly from frozen encoders. FILTR adapts a transformer decoder to treat diagram generation as a set prediction task. Our analysis on DONUT reveals that existing encoders retain only limited global topological signals, yet FILTR successfully leverages information produced by these encoders to approximate persistence diagrams. Our approach enables, for the first time, data-driven extraction of persistence diagrams from raw point clouds through an efficient learnable feed-forward mechanism.

---


### 77. [Context-Fidelity Boosting: Enhancing Faithful Generation through Watermark-Inspired Decoding](https://arxiv.org/abs/2604.22335)

**<font color=#1a73e8>作者：</font>** Weixu Zhang, Fanghua Ye, Qiang Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often produce content that contradicts or overlooks information provided in the input context, a phenomenon known as faithfulness hallucination. In this paper, we propose Context-Fidelity Boosting (CFB), a lightweight and general decoding-time framework that reduces such hallucinations by increasing the generation probability of source-supported tokens. Motivated by logit-shaping principles from watermarking techniques, CFB applies additive token-level logit adjustments based on a token's degree of support from the input context. Specifically, we develop three boosting strategies: static boosting, which applies a fixed bias to source-supported tokens; context-aware boosting, which scales this bias using the divergence between next-token distributions with and without context; and token-aware boosting, which further redistributes the adaptive bias according to local relevance estimated from source-position attention and source-scoped semantic similarity. CFB requires no retraining or architectural changes, making it compatible with a wide range of LLMs. Experiments on summarization and question answering tasks across multiple open-source LLMs show that CFB consistently improves faithfulness metrics with minimal generation overhead. Our implementation is fully open-sourced.

---


### 78. [TabSCM: A practical Framework for Generating Realistic Tabular Data](https://arxiv.org/abs/2604.22337)

**<font color=#1a73e8>作者：</font>** Sven Jacob, Bardh Prenkaj, Weijia Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most tabular-data generators match marginal statistics yet ignore causal structure, leading downstream models to learn spurious or unfair patterns. We present TabSCM, a mixed-type generator that preserves those causal dependencies. Starting from a Completed Partially Directed Acyclic Graph (CPDAG) found by any causal structure discovery algorithm, TabSCM (i) orients edges to a DAG, (ii) fits root-node marginals with KDE or categorical frequencies, and (iii) learns topologically ordered structural assignments. Such assignments are achieved using conditional diffusion models for continuous variables as child nodes and gradient-boosted trees for categorical ones. Ancestral sampling yields semantically valid records and enables exact counterfactual queries. On seven public datasets, encompassing healthcare, finance, housing, environment, TabSCM matches or surpasses state-of-the-art GAN, diffusion, and LLM baselines in statistical fidelity, downstream utility, and privacy risk, while also cutting rule-violation rates and providing causally meaningful and robust conditional interventions. Because generation is decomposed into explicit equations, it runs up to 583$\times$ faster than diffusion-only models and exposes interpretable knobs for fairness auditing and policy simulation, making TabSCM a practical choice for realism, explainability, and causal soundness.

---


### 79. [Flow4DGS-SLAM: Optical Flow-Guided 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2604.22339)

**<font color=#1a73e8>作者：</font>** Yunsong Wang, Gim Hee Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handling the dynamic environments is a significant research challenge in Visual Simultaneous Localization and Mapping (SLAM). Recent research combines 3D Gaussian Splatting (3DGS) with SLAM to achieve both robust camera pose estimation and photorealistic renderings. However, using SLAM to efficiently reconstruct both static and dynamic regions remains challenging. In this work, we propose an efficient framework for dynamic 3DGS SLAM guided by optical flow. Using the input depth and prior optical flow, we first propose a category-agnostic motion mask generation strategy by fitting a camera ego-motion model to decompose the optical flow. This module separates dynamic and static Gaussians and simultaneously provides flow-guided camera pose initialization. We boost the training speed of dynamic 3DGS by explicitly modeling their temporal centers at keyframes. These centers are propagated using 3D scene flow priors and are dynamically initialized with an adaptive insertion strategy. Alongside this, we model the temporal opacity and rotation using a Gaussian Mixture Model (GMM) to adaptively learn the complex dynamics. The empirical results demonstrate our state-of-the-art performance in tracking, dynamic reconstruction, and training efficiency.

---


### 80. [PoseFM: Relative Camera Pose Estimation Through Flow Matching](https://arxiv.org/abs/2604.22350)

**<font color=#1a73e8>作者：</font>** Dominik Kuczkowski, Laura Ruotsalainen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular visual odometry (VO) is a fundamental computer vision problem with applications in autonomous navigation, augmented reality and more. While deep learning-based methods have recently shown superior accuracy compared to traditional geometric pipelines, particularly in environments where handcrafted features struggle due to poor structure or lighting conditions, most rely on deterministic regression, which lacks the uncertainty awareness required for robust applications. We propose PoseFM, the first framework to reformulate monocular frame-to-frame VO as a generative task using Flow Matching (FM). By leveraging FM, we model camera motion as a distribution rather than a point estimate, learning to transform noise into realistic pose predictions via continuous-time ODEs. This approach provides a principled mechanism for uncertainty estimation and enables robust motion inference under challenging visual conditions. In our evaluations, PoseFM achieves strong performance on TartanAir, KITTI and TUM-RGBD benchmarks, achieving the lowest absolute trajectory error (ATE) on some of the trajectories and overall being competitive with the best frame-to-frame monocular VO methods. Code and model checkpoints will be made available at this https URL.

---


### 81. [One Shot Learning for Edge Detection on Point Clouds](https://arxiv.org/abs/2604.22354)

**<font color=#1a73e8>作者：</font>** Zhikun Tu, Yuhe Zhang, Yiou Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Each scanner possesses its unique characteristics and exhibits its distinct sampling error distribution. Training a network on a dataset that includes data collected from different scanners is less effective than training it on data specific to a single scanner. Therefore, we present a novel one-shot learning method allowing for edge extraction on point clouds, by learning the specific data distribution of the target point cloud, and thus achieve superior results compared to networks that were trained on general data distributions. More specifically, we present how to train a lightweight network named OSFENet (One-Shot edge Feature Extraction Network), by designing a filtered-KNN-based surface patch representation that supports a one-shot learning framework. Additionally, we introduce an RBF_DoS module, which integrates Radial Basis Function-based Descriptor of the Surface patch, highly beneficial for the edge extraction on point clouds. The advantage of the proposed OSFENet is demonstrated through comparative analyses against 7 baselines on the ABC dataset, and its practical utility is validated by results across diverse real-scanned datasets, including indoor scenes like S3DIS dataset, and outdoor scenes such as the Semantic3D dataset and UrbanBIS dataset.

---


### 82. [SOC-ICNN: From Polyhedral to Conic Geometry for Learning Convex Surrogate Functions](https://arxiv.org/abs/2604.22355)

**<font color=#1a73e8>作者：</font>** Kang Liu, Jianchen Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical ReLU-based Input Convex Neural Networks (ICNNs) are equivalent to the optimal value functions of Linear Programming (LP). This intrinsic structural equivalence restricts their representational capacity to piecewise-linear polyhedral functions. To overcome this representational bottleneck, we propose the SOC-ICNN, an architecture that generalizes the underlying optimization class from LP to Second-Order Cone Programming (SOCP). By explicitly injecting positive semi-definite curvature and Euclidean norm-based conic primitives, our formulation introduces native smooth curvature into the representation while preserving a rigorous optimization-theoretic interpretation. We formally prove that SOC-ICNNs strictly expand the representational space of ReLU-ICNNs without increasing the asymptotic order of forward-pass complexity. Extensive experiments demonstrate that SOC-ICNN substantially improves function approximation, while delivering competitive downstream decision quality. The code is available at this https URL.

---


### 83. [Selective Contrastive Learning For Gloss Free Sign Language Translation](https://arxiv.org/abs/2604.22374)

**<font color=#1a73e8>作者：</font>** Changhao Lai, Rui Zhao, Xuewen Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language translation (SLT) converts continuous sign videos into spoken-language text, yet it remains challenging due to the intrinsic modality mismatch between visual signs and written text, particularly in gloss-free settings. Recent SLT systems increasingly adopt CLIP-like Vision-Language pretraining (VLP) for cross-modal alignment, but the random in-batch contrast provides few, batch-dependent negatives and may mislabel semantically similar (or even identical) pairs as negatives, introducing noisy and potentially inconsistent alignment supervision. In this work, we first conduct a preliminary trajectory-based analysis that tracks negative video-text similarity over training. The results show that only a small subset of negatives exhibits the desired behavior of being consistently pushed away, while the remaining negatives display heterogeneous and often non-decreasing similarity dynamics, suggesting that random in-batch negatives are frequently uninformative for effective alignment. Inspired by this, we propose Selective Contrastive Learning for SLT (SCL-SLT) with a Pair Selection (PS) strategy. PS scores candidate negatives using similarity dynamics from reference checkpoints and constructs mini-batches via a curriculum that progressively emphasizes more challenging negatives, thereby strengthening contrastive supervision while reducing the influence of noisy or semantically invalid negatives.

---


### 84. [Efficient Diffusion Distillation via Embedding Loss](https://arxiv.org/abs/2604.22379)

**<font color=#1a73e8>作者：</font>** Jincheng Ying, Yitao Chen, Li Wenlin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in distilling expensive diffusion models into efficient few-step generators show significant promise. However, these methods typically demand substantial computational resources and extended training periods, limiting accessibility for resource-constrained researchers, and existing supplementary loss functions have notable limitations. Regression loss requires pre-generating large datasets before training and limits the student model to the teacher's performance, while GAN-based losses suffer from training instability and require careful tuning. In this paper, we propose Embedding Loss (EL), a novel supplementary loss function that complements existing diffusion distillation methods to enhance generation quality and accelerate training with smaller batch sizes. Leveraging feature embeddings from a diverse set of randomly initialized networks, EL effectively aligns the feature distributions between the distilled few-step generator and the original data. By computing Maximum Mean Discrepancy (MMD) in the embedded feature space, EL ensures robust distribution matching, thereby preserving sample fidelity and diversity during distillation. Within distribution matching distillation frameworks, EL demonstrates strong empirical performance for one-step generators. On the CIFAR-10 dataset, our approach achieves state-of-the-art FID values of 1.475 for unconditional generation and 1.380 for conditional generation. Beyond CIFAR-10, we further validate EL across multiple benchmarks and distillation methods, including ImageNet, AFHQ-v2, and FFHQ datasets, using DMD, DI, and CM distillation frameworks, demonstrating consistent improvements over existing one-step distillation methods. Our method also reduces training iterations by up to 80%, offering a more practical and scalable solution for deploying diffusion-based generative models in resource-constrained environments.

---


### 85. [HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388)

**<font color=#1a73e8>作者：</font>** Xu Lu, Qianhong Peng, Qihao Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transrectal ultrasound (TRUS) imaging is a cost-effective and non-invasive modality widely used in the diagnosis of prostate cancer. The computer-aided diagnosis (CAD) relying on TRUS images has been extensively investigated recently. Compared to static images, TRUS video provides richer spatial-temporal information, which make it a promising alternative for improving the accuracy and robustness of CAD systems. However, TRUS video analysis also introduces new challenges. These include information redundancy, which increases computational costs; high intra- and inter-class similarity, which complicates feature extraction; and a low signal-to-noise ratio, which hinders the identification of clinically relevant information. To address these problems, we propose a heuristic frame selection (HFS) and a three-branch collaborative feature learning network (HFS-TriNet) for prostate cancer classification from TRUS videos. Specifically, selecting a clip of video frames at intervals for training can mitigate redundancy. The HFS strategy dynamically initializes the starting point of each training clip, which ensures that the sampled clips span the entire video sequence. For better feature extraction, besides a regular ResNet50 branch, we also utilize 1) a large model branch based a pre-trained medical segment anything model (SAM) to extract deep features of each frame and a normalization-based attention module to explore the temporal consistency; and 2) a wavelet transform convolutional residual (WTCR) branch that extracts lesion edge information in the high-frequency domain and performs denoising in the low-frequency domain.

---


### 86. [Region Matters: Efficient and Reliable Region-Aware Visual Place Recognition](https://arxiv.org/abs/2604.22390)

**<font color=#1a73e8>作者：</font>** Shunpeng Chen, Yukun Song, Changwei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Place Recognition (VPR) determines a query image's geographic location by matching it against geotagged databases. However, existing methods struggle with perceptual aliasing caused by irrelevant regions and inefficient re-ranking due to rigid candidate scheduling. To address these issues, we introduce FoL++, a method combining robust discriminative region modeling with adaptive re-ranking. Specifically, we propose a Reliability Estimation Branch to generate spatial reliability maps that explicitly model occlusion resistance. This representation is further optimized by two spatial alignment losses (SAL and SCEL) to effectively align features and highlight salient regions. For weakly supervised learning without manual annotations, a pseudo-correspondence strategy generates dense local feature supervision directly from aggregation clusters. Our Adaptive Candidate Scheduler dynamically resizes candidate pools based on global similarity. By weighting local matches by reliability and adaptively fusing global and local evidence, FoL++ surpasses traditional independent matching systems. Extensive experiments across seven benchmarks demonstrate that FoL++ achieves state-of-the-art performance with a lightweight memory footprint, improving inference speed by 40% over FoL. Code and models will be released (and merged with FoL) at this https URL.

---


### 87. [Robust Fuzzy local k-plane clustering with mixture distance of hinge loss and L1 norm](https://arxiv.org/abs/2604.22405)

**<font color=#1a73e8>作者：</font>** Junjun Huang, Xiliang Lu, Xuelin Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> K-plane clustering (KPC), hyperplane clustering, and mixture regression all essentially fall within the same class of problems. This problem can be conceptualized as clustering in relatively high-dimensional K subspaces or K linear manifolds. Traditional KPC or fuzzy KPC models demonstrate a pronounced susceptibility to outliers, as they presuppose that the projection distance between data points and the plane normal vector adheres to the L2 distance. Meanwhile, the assumption of infinitely extending clusters adversely affects clustering performance. To solve these problems, this paper proposed a new robust fuzzy local k-plane clustering (RFLkPC) method that combines the mixture distance of hinge loss and L1 norm. The RFLkPC model assumes that each plane cluster is bounded to a finite area, which can flexibly and robustly handle plane clustering tasks with outliers or not. The corresponding model and optimization algorithms of RFLkPC were provided. Compared to other related models on this topic, a large number of experiments verify the efficiency of RFLkPC on simulated data and real data. The source code for the proposed RFLkPC method is publicly available at this https URL.

---


### 88. [Hidden Failure Modes of Gradient Modification under Adam in Continual Learning, and Adaptive Decoupled Moment Routing as a Repair](https://arxiv.org/abs/2604.22407)

**<font color=#1a73e8>作者：</font>** Yuelin Hu, Zhenbo Yu, Zhengxue Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many continual-learning methods modify gradients upstream (e.g., projection, penalty rescaling, replay mixing) while treating Adam as a neutral backend. We show this composition has a hidden failure mode. In a high-overlap, non-adaptive 8-domain continual LM, all shared-routing projection baselines collapse close to vanilla forgetting (12.5--12.8 vs. 13.2). A 0.5% replay buffer is the strongest shared alternative but still reaches 11.6, while fixed-strength decoupling falls below vanilla at 14.1. Only adaptive decoupled routing remains stable at 9.4, improving over vanilla by 3.8 units. On a 16-domain stream, its gain over the strongest shared-routing projection baseline grows to 4.5--4.8 units. The failure is largely invisible on clean benchmarks.
We explain this effect through Adam's second-moment pathway: in the tested regime, projection induces a 1/(1-alpha) inflation of the old-direction effective learning rate, matching measurements within 8% across eight alpha values. The same conflict appears with penalty methods, replay mixing, and at 7B scale under LoRA. Our fix routes the modified gradient only to the first moment while preserving magnitude-faithful second-moment statistics, with overlap-aware adaptive strength. This simple change is the only tested configuration that consistently avoids collapse across methods, optimizers, and scale.

---


### 89. [Distance-Misaligned Training in Graph Transformers and Adaptive Graph-Aware Control](https://arxiv.org/abs/2604.22413)

**<font color=#1a73e8>作者：</font>** Qinhan Hou, Jing Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Transformers can mix information globally, but this flexibility also creates failure modes: some tasks require long-range communication while others are better served by local interaction. We study this through a synthetic node-classification benchmark on contextual stochastic block model graphs, where labels are generated by a controllable mixture of local and far-shell signals. We define distance-misaligned training as a mismatch between where label-relevant information lies and where the model allocates communication over graph distance. On this benchmark, we find three points. First, the preferred graph-distance bias changes systematically with task locality. Second, an oracle adaptive controller, given offline access to the task-side distance target, nearly matches the best fixed bias across regimes and strongly improves over a neutral baseline on mixed and local tasks. Third, a task-agnostic zero-gap controller is weaker, indicating that adaptation alone is not enough and that the control target matters. These results suggest that distance-resolved diagnosis is useful for understanding Graph Transformer failures and for designing graph-aware control.

---


### 90. [From Local to Cluster: A Unified Framework for Causal Discovery with Latent Variables](https://arxiv.org/abs/2604.22416)

**<font color=#1a73e8>作者：</font>** Zongyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent variables pose a fundamental challenge to causal discovery and inference. Conventional local methods focus on direct neighbors but fail to provide macro level insights. Cluster level methods enable macro causal reasoning but either assume clusters are known a priori or require causal sufficiency. Moreover, directly applying single variable causal discovery methods to cluster level problems violates causal sufficiency and leads to incorrect results. To overcome these limitations, this paper proposes L2C (Local to Cluster Causal Abstraction), a unified framework that bridges local structure learning and cluster level causal discovery. Unlike prior work that requires a complete manual assignment of micro variables to clusters, L2C discovers the partition automatically from local causal patterns. Our solution leverages a cluster reduction theorem to reduce any cluster to at most three nodes without loss of causal information, applies local causal discovery to identify direct causes, effects, and V structures in the presence of latent variables, and performs macro level causal inference via cluster level calculus on the learned cluster graph. L2C does not assume causal sufficiency, as latent variables are handled through local discovery. Theoretical analysis shows that L2C ensures soundness, atomic completeness, and computational efficiency. Extensive experiments on synthetic and real world data demonstrate that L2C accurately recovers ground truth clusters and achieves superior macro causal effect identification compared to existing baselines.

---


### 91. [CognitiveTwin: Robust Multi-Modal Digital Twins for Predicting Cognitive Decline in Alzheimer's Disease](https://arxiv.org/abs/2604.22428)

**<font color=#1a73e8>作者：</font>** Bulent Soykan, Gulsah Hancerliogullari Koksalmis, Hsin-Hsiung Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting individual cognitive decline in Alzheimer's disease (AD) is difficult due to the heterogeneity of disease progression. Reliable clinical tools require not only high accuracy but also fairness across demographics and robustness to missing data. We present CognitiveTwin, a digital twin framework that predicts patient-specific cognitive trajectories. The model integrates multi-modal longitudinal data (cognitive scores, magnetic resonance imaging, positron emission tomography, cerebrospinal fluid biomarkers, and genetics). We use a Transformer-based architecture to fuse these modalities and a Deep Markov Model to capture temporal dynamics. We trained and evaluated the framework using data from 1,666 patients in the TADPOLE (Alzheimer's Disease Neuroimaging Initiative) dataset. We assessed the model for prediction error, demographic fairness, and robustness to missing-not-at-random (MNAR) data patterns. ognitiveTwin provides accurate and personalized predictions of cognitive decline. Its demonstrated fairness across patient demographics and resilience to clinical dropout make it a reliable tool for clinical trial enrichment and personalized care planning.

---


### 92. [Horizontal SCA Attacks on Binary kP Algorithms using Chevallier-Mames Atomic Blocks](https://arxiv.org/abs/2604.22429)

**<font color=#1a73e8>作者：</font>** Gerald Isheanesu Matungamire, Alkistis Aikaterini Sigourou, Gerrit Schrock 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Scalar multiplication kP is the operation most frequently targeted in Elliptic Curve (EC) cryptosystems. To protect against single-trace Side-Channel Analysis (SCA) attacks, the atomicity principle and various atomic block patterns have been proposed in the past. In this work we use our software and hardware implementations to demonstrate that binary right-to left and left-to-right kP algorithms, when implemented with Chevallier-Mames atomic block patterns, are still vulnerable to single-trace SCA attacks. The vulnerability remains true for the left-to-right kP algorithm with projective coordinate randomization.

---


### 93. [Beyond Land Surface Temperature: Explainable Spatial Machine Learning Reveals Urban Morphology Effects on Human-Centric Heat Stress](https://arxiv.org/abs/2604.22433)

**<font color=#1a73e8>作者：</font>** Yuan Wang, Shengao Yi, Xiaojiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heat exposure connects the built environment and public health, directly shaping the livability and sustainability of urban areas. Understanding the spatial heterogeneity of heat exposure and its drivers is vital for climate-adaptive urban planning. However, most planning-oriented studies rely on land surface temperature (LST), and whether LST adequately represents human heat exposure and how it differs from physiologically relevant heat stress remains insufficiently examined. Here, adopting Landsat-retrieved 30-m LST and GPU-accelerated 1-m universal thermal climate index (UTCI) in Singapore, this study establishes a comprehensive "Modeling-Comparing-Assessing" framework to systematically evaluate the spatial and mechanistic discrepancies between the two metrics. We further investigate pronounced non-stationary and threshold-based quantitative relationships of the two metrics with urban factors by employing a novel geographically weighted XGBoost (GW-XGBoost) and generalized additive model (GAM) workflow. Our results demonstrate notable discrepancies in spatial patterns of LST and UTCI, along with substantial spatial heterogeneity in how 2D and 3D urban factors impact these two thermal metrics, as revealed by explainable GW-XGBoost models (global out-of-bag R2 = 0.855 for LST and 0.905 for UTCI, respectively). Crucially, spatially explicit SHAP interprets that sky view factor plays a central role in explaining UTCI variability but exhibits a comparatively marginal independent contribution to LST, indicating that LST inadequately captures shading-driven and radiative processes governing actual human heat stress. Notably, SHAP-GAM analysis indicates that higher albedo is associated with increased UTCI. These novel findings provide evidence for integrating physiologically relevant thermal indices to inform targeted heat risk management and climate-adaptive urban planning.

---


### 94. [AgentSearchBench: A Benchmark for AI Agent Search in the Wild](https://arxiv.org/abs/2604.22436)

**<font color=#1a73e8>作者：</font>** Bin Wu, Arastun Mammadli, Xiaoyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of AI agent ecosystems is transforming how complex tasks are delegated and executed, creating a new challenge of identifying suitable agents for a given task. Unlike traditional tools, agent capabilities are often compositional and execution-dependent, making them difficult to assess from textual descriptions alone. However, existing research and benchmarks typically assume well-specified functionalities, controlled candidate pools, or only executable task queries, leaving realistic agent search scenarios insufficiently studied. We introduce AgentSearchBench, a large-scale benchmark for agent search in the wild, built from nearly 10,000 real-world agents across multiple providers. The benchmark formalizes agent search as retrieval and reranking problems under both executable task queries and high-level task descriptions, and evaluates relevance using execution-grounded performance signals. Experiments reveal a consistent gap between semantic similarity and actual agent performance, exposing the limitations of description-based retrieval and reranking methods. We further show that lightweight behavioral signals, including execution-aware probing, can substantially improve ranking quality, highlighting the importance of incorporating execution signals into agent discovery. Our code is available at this https URL.

---


### 95. [NRGS: Neural Regularization for Robust 3D Semantic Gaussian Splatting](https://arxiv.org/abs/2604.22439)

**<font color=#1a73e8>作者：</font>** Zaiyan Yang, Xinpeng Liu, Heng Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a neural regularization method that refines the noisy 3D semantic field produced by lifting multi-view inconsistent 2D features, in order to obtain an accurate and robust 3D semantic Gaussian Splatting. The 2D features extracted from vision foundation models suffer from multi-view inconsistency due to a lack of cross-view constraints. Lifting these inconsistent features directly into 3D Gaussians results in a noisy semantic field, which degrades the performance of downstream tasks. Previous methods either focus on obtaining consistent multi-view features in the preprocessing stage or aim to mitigate noise through improved optimization strategies, often at the cost of increased preprocessing time or expensive computational overhead. In contrast, we introduce a variance-aware conditional MLP that operates directly on the 3D Gaussians, leveraging their geometric and appearance attributes to correct semantic errors in 3D space. Experiments on different datasets show that our method enhances the accuracy of lifted semantics, providing an efficient and effective approach to robust 3D semantic Gaussian Splatting.

---


### 96. [HubRouter: A Pluggable Sub-Quadratic Routing Primitive for Hybrid Sequence Models](https://arxiv.org/abs/2604.22442)

**<font color=#1a73e8>作者：</font>** Abhinaba Basu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce HubRouter, a pluggable module that replaces O(n^2) attention layers with O(nM) hub-mediated routing, where M << n is a small number of learned hub tokens. We demonstrate it in two from-scratch architectures: a Jamba-style hybrid and a 12-layer Transformer; retrofit into pretrained models is a tested negative case. HubRouter implements an encode-decode-score-council pipeline: M learned hubs cross-attend to all tokens, tokens project against hubs for routing fingerprints, a score head selects top-k tokens, and a sparse council attends only to the selected subset.
We validate HubRouter in three settings. (1) Hub-Jamba yields a nominal 4.2% PPL improvement (200.2 vs 209.0, single seed; possibly within seed noise) and up to ~90x training throughput at sequence length 1024 in matched PyTorch-native baselines; an optimised baseline would narrow this to ~10-15x. (2) Graduated replacement of 25% of Transformer attention layers gives the best perplexity in our matched-budget sweep (268.0 vs 282.4 pure Transformer). (3) Hub-GPT provides strictly causal routing, achieving PPL 211.5 +/- 0.4 over 3 seeds (post council-causal fix); approximately 3 PPL worse than Jamba's 208.5 +/- 0.7, a measurable quality cost for avoiding O(n^2) computation. Post-fix, chunk size C has little effect; the pre-fix chunk-size benefit was an artifact of a bidirectional-council leak we found in adversarial review.
A multi-seed hub-count sweep (~105 runs across M=1-32) reveals M=8-14 as the reliably-converging sub-band (4-5/5 seeds); M=6 is rescued to 5/5 by orthogonal regularization, while M>=20 shows increasing seed sensitivity. Companion paper arXiv:2603.20997 (Basu, 2026) defines the routing diagnostic task. Code and scripts will be released.

---


### 97. [From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company](https://arxiv.org/abs/2604.22446)

**<font color=#1a73e8>作者：</font>** Zhengxu Yu, Yu Fu, Zhiyuan He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Individual agent capabilities have advanced rapidly through modular skills and tool integrations, yet multi-agent systems remain constrained by fixed team structures, tightly coupled coordination logic, and session-bound learning. We argue that this reflects a deeper absence: a principled organisational layer that governs how a workforce of agents is assembled, governed, and improved over time, decoupled from what individual agents know. To fill this gap, we introduce \emph{OneManCompany (OMC)}, a framework that elevates multi-agent systems to the organisational level. OMC encapsulates skills, tools, and runtime configurations into portable agent identities called \emph{Talents}, orchestrated through typed organisational interfaces that abstract over heterogeneous backends. A community-driven \emph{Talent Market} enables on-demand recruitment, allowing the organisation to close capability gaps and reconfigure itself dynamically during execution. Organisational decision-making is operationalised through an \emph{Explore-Execute-Review} ($\text{E}^2$R) tree search, which unifies planning, execution, and evaluation in a single hierarchical loop: tasks are decomposed top-down into accountable units and execution outcomes are aggregated bottom-up to drive systematic review and refinement. This loop provides formal guarantees on termination and deadlock freedom while mirroring the feedback mechanisms of human enterprises. Together, these contributions transform multi-agent systems from static, pre-configured pipelines into self-organising and self-improving AI organisations capable of adapting to open-ended tasks across diverse domains. Empirical evaluation on PRDBench shows that OMC achieves an $84.67\%$ success rate, surpassing the state of the art by $15.48$ percentage points, with cross-domain case studies further demonstrating its generality.

---


### 98. [Superminds Test: Actively Evaluating Collective Intelligence of Agent Society via Probing Agents](https://arxiv.org/abs/2604.22452)

**<font color=#1a73e8>作者：</font>** Xirui Li, Ming Li, Yunze Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collective intelligence refers to the ability of a group to achieve outcomes beyond what any individual member can accomplish alone. As large language model agents scale to populations of millions, a key question arises: Does collective intelligence emerge spontaneously from scale? We present the first empirical evaluation of this question in a large-scale autonomous agent society. Studying MoltBook, a platform hosting over two million agents, we introduce Superminds Test, a hierarchical framework that probes society-level intelligence using controlled Probing Agents across three tiers: joint reasoning, information synthesis, and basic interaction. Our experiments reveal a stark absence of collective intelligence. The society fails to outperform individual frontier models on complex reasoning tasks, rarely synthesizes distributed information, and often fails even trivial coordination tasks. Platform-wide analysis further shows that interactions remain shallow, with threads rarely extending beyond a single reply and most responses being generic or off-topic. These results suggest that collective intelligence does not emerge from scale alone. Instead, the dominant limitation of current agent societies is extremely sparse and shallow interaction, which prevents agents from exchanging information and building on each other's outputs.

---


### 99. [On the Hybrid Nature of ABPMS Process Frames and its Implications on Automated Process Discovery](https://arxiv.org/abs/2604.22455)

**<font color=#1a73e8>作者：</font>** Anti Alman, Izack Cohen, Avigdor Gal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A core component of any AI-Augmented Business Process Management System (ABPMS) is the process frame, which gives the system process-awareness and defines the boundaries in which the system must operate. Compared to traditional process models, the process frame should, in principle, provide a somewhat more permissive representation of the managed processes, such that the (semi) autonomous behavior of an ABPMS, referred to as framed autonomy, could emerge. At the same time, it is not limited to a single linguistic or symbolic formalism and may incorporate heterogeneous knowledge ranging from predefined procedures to commonsense rules and best practices. In this paper, we conceptualize the notion of an ABPMS process frame as a hybrid business process representation, consisting of semi-concurrently executed procedural and declarative process models. We rely on our earlier works to outline the execution semantics of this type of process frame, arguing in favor of adopting the open-world assumption of the declarative paradigm also for procedural process models. The latter leads to a constraint-like interpretation, where each procedural model is considered to constrain the activities within that model, without imposing explicit execution requirements nor limitations on activities that may be present in other models. This is analogous to existing declarative languages, such as Declare, where each constraint has a direct effect only on the specific activities being constrained. Given this similarity, we propose mapping subsets of discovered declarative constraints into equivalent semi-concurrently executed procedural fragments, thus laying the foundation for a corresponding process (frame) discovery approach.

---


### 100. [Towards Adaptive Continual Model Merging via Manifold-Aware Expert Evolution](https://arxiv.org/abs/2604.22464)

**<font color=#1a73e8>作者：</font>** Haiyun Qiu, Xingyu Wu, Kay Chen Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual Model Merging (CMM) sequentially integrates task-specific models into a unified architecture without intensive retraining. However, existing CMM methods are hindered by a fundamental saturation-redundancy dilemma: backbone-centric approaches face parameter saturation and representation interference within fixed capacities, whereas Mixture-of-Experts (MoE) variants resort to indiscriminate expansion, incurring expert redundancy and a routing bottleneck reliant on additional data-driven optimization. To resolve these challenges, we propose MADE-IT (Manifold-Aware Dynamic Expert Evolution and Implicit rouTing), an adaptive CMM method that orchestrates expert management and activation by grounding intrinsic expert representations in manifold geometry. We introduce a projection-based subspace affinity metric coupled with a distribution-aware adaptive threshold mechanism to guide autonomous expert evolution, harmonizing diversity with architectural parsimony. Furthermore, to bypass parameterized gating networks, we design a data-free and training-free implicit routing mechanism that activates experts via feature-subspace alignment. Extensive experiments demonstrate that MADE-IT consistently outperforms strong baselines in accuracy and robustness across long-horizon and shuffled task sequences, while significantly pruning redundant experts, particularly within generic modules and early layers.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-154](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
