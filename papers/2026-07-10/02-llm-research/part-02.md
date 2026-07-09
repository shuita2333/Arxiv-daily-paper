# 🧠 大模型相关研究 | 2026年07月10日

> 本类共 **84** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-84**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-84**

---

### 51. [Does AI Understand Imaging? A Systematic Benchmark of Agentic AI for Computational Imaging Tasks](https://arxiv.org/abs/2607.07189)

**<font color=#1a73e8>作者：</font>** Ethan Chung, Chuanjun Zheng, Jasper Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) and agentic AI have shown strong performance on semantic visual tasks, but it remains unclear whether they can handle the physics and inverse problems that underlie computational imaging. We present ImagingBench, a benchmark of 20 computational imaging tasks spanning five categories: ray and wave optics, image signal processing, inverse reconstruction, computational sensing, and calibration. ImagingBench evaluates three complementary settings: Expert, fixed expert-guided inverse reconstruction; Planner, planner-guided inverse reconstruction; and Forward, forward-system simulation for consistency checking. We benchmark leading proprietary and open-source image-centric multimodal systems, including Gemini, GPT, and Qwen, and compare them with representative task-specific non-agentic baselines. Across tasks, agentic models remain consistently weaker than specialized methods, especially on computational sensing problems such as lensless imaging, event-based reconstruction, time-of-flight imaging, and holography. Planner guidance provides only modest and inconsistent gains over the fixed-prompt Expert baseline. Although the models often generate visually plausible outputs, their reference-based fidelity remains poor, revealing a substantial gap between semantic visual competence and physically grounded imaging performance. ImagingBench provides a unified testbed for measuring this gap and tracking progress in agentic AI for computational imaging.

---


### 52. [Vision Foundation Models in Radiology: A Scoping Review of Data, Methodology, Evaluation and Clinical Translation](https://arxiv.org/abs/2607.07219)

**<font color=#1a73e8>作者：</font>** Alejandro Vergara-Richart, Xavier Rafael-Palou, Almudena Fuster-Matanzo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) are increasingly being developed for radiological imaging, yet their definition, development and evaluation remain heterogeneous. We conducted a PRISMAScR scoping review of peer-reviewed studies published between January 2017 and March 2026 describing foundation models trained exclusively on radiological imaging data. Sixty-seven studies were included and mapped across three pillars: data scale and heterogeneity, architectural and pretraining scalability, and downstream transferability and generalization. Datasets primarily covered brain MRI, thoracoabdominal CT, and chest X-ray, ranging from fewer than 100,000 samples to multi-million-image cohorts. Transformer-based architectures and self-supervised pretraining predominated, particularly masked image modeling, contrastive learning and multi-stage approaches. Evaluation focused mainly on segmentation and classification, whereas cross-center, cross-scanner, anatomical and modality-shift validation was inconsistently reported. Alignment with FUTURE-AI principles was uneven. Overall, radiology-specific VFMs show promising transferability, but clinical translation remains constrained by limited data representativeness, heterogeneous benchmarks, incomplete reporting and insufficient deployment-oriented evaluation.

---


### 53. [Evaluation of Multilingual Ability to Use Spatial Deictic Expressions in Vision-Language Models](https://arxiv.org/abs/2607.07251)

**<font color=#1a73e8>作者：</font>** Kaito Watanabe, Taisei Yamamoto, Tomoki Doi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One of the expected abilities of vision-language models (VLMs) is spatial reasoning ability based on a given text and image. To evaluate the spatial reasoning abilities of VLMs, we focus on the use of spatial deictic expressions, which are defined as spatial expressions whose referent is determined by their situational context, such as ``this'' and ``that''. To handle spatial deictic expressions, VLMs must jointly reason over language and visual space, grounding context-dependent references in the image's spatial structure. In addition, selecting appropriate spatial deictic expressions across languages requires VLMs to understand the language-specific spatial distinctions encoded by these expressions. In this paper, we develop a benchmark to evaluate the multilingual ability of VLMs to use spatial deictic expressions in four languages. Our experiments using this benchmark reveal that the tested models use demonstratives in a manner different from that of humans, particularly in selecting the appropriate demonstratives based on the distance to the object.

---


### 54. [InfraQR: Edge-Placed QR-Inspired Structured Patch Attacks on Infrared Vision-Language Models](https://arxiv.org/abs/2607.07288)

**<font color=#1a73e8>作者：</font>** Xin Li, Jiaju Han, Ma Yaqi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared vision-language models are increasingly used for perception under low-light and adverse visual conditions, yet their robustness to localized structured perturbations remains underexplored. Existing infrared adversarial studies mainly focus on object detectors, leaving the security of infrared vision-language models less systematically examined. We present InfraQR, a QR-inspired structured patch attack for infrared vision-language models. Unlike localized attacks that attach perturbations to the target object, InfraQR places a compact structured patch along image boundaries and optimizes learnable grid cells through surrogate CLIP-style encoders. The resulting patch has a near-binary structured appearance, but is not required to be a valid or machine-readable QR code. We evaluate InfraQR on infrared classification, caption transfer, and question-answer-aware visual question answering (VQA) tasks. On a 300-image infrared benchmark, InfraQR sharply reduces the accuracy of multiple CLIP-style classifiers, including reducing OpenAI CLIP accuracy from 98.67% to 0.70%. The generated adversarial images also transfer to black-box captioning and VQA models, causing semantic degradation in captions and more error-prone answers under GPT-5.4-based evaluation. These results show that infrared vision-language models remain vulnerable to structured edge-placed perturbations, motivating further study of cross-task robustness beyond direct object occlusion.

---


### 55. [Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations](https://arxiv.org/abs/2607.07302)

**<font color=#1a73e8>作者：</font>** Quentin Brabant  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper reports an empirical study evaluating the relevance of several RAG metrics. The experiment is based on a question-answering dataset created by human annotators from business data. The generated responses and retrieved spans of a RAG system are scored using evaluation metrics from four libraries (Ragas, DeepEval, RAGChecker, Opik). These metrics are compared to scores given by two evaluators, as well as to standard metrics such as recall. An analysis of correlations is conducted. Finally, we highlight certain limitations of our methodology, compare it to those used in the literature, and suggest some avenues for future research. This paper is an English translation of a paper originally published in the French-speaking workshop EvalLLM (Brabant, 2026).

---


### 56. [From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents](https://arxiv.org/abs/2607.07321)

**<font color=#1a73e8>作者：</font>** Haipeng Ding, Yuexiang Xie, Zhewei Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates. In this study, we propose that agents can achieve self-evolution by synthesizing these atomic actions into reusable Standard Operating Procedures (SOPs), which function as callable higher-order tools that encapsulate multi-step logic. We further introduce EvoSOP, a framework that empowers agents to extract SOPs from execution trajectories and iteratively optimize the toolset through a systematic lifecycle of construction, merging, evaluation, and pruning. Extensive experiments demonstrate that EvoSOP significantly boosts task success rates while substantially reducing the number of interaction rounds compared to baselines. Our analysis also reveals that iterative tool optimization fosters reliable and efficient tool-use patterns, providing a scalable pathway for the development of self-evolving agents.

---


### 57. [BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning](https://arxiv.org/abs/2607.07361)

**<font color=#1a73e8>作者：</font>** Jiacheng Yang, Tongying Xiao, Yunkai Dang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Vision-Language Models (VLMs) often struggle to handle complex visual tasks that require consistent and fine-grained reasoning. Recent methods aim to train models to facilitate self-reflective reasoning, i.e., reviewing and improving the generated reasoning. However, they require large volumes of annotated data and lack explicit reflective behavior during test time. This work aims to bridge this gap through inspiration from neuroscience. The human brain exhibits efficient backward prediction, i.e., predicting which current states are likely to precede a given future state. In this work, we first verify that mainstream VLMs can perform backward prediction, similar to the human brain. Then, we propose Brain-inspired Unsupervised Self-reflection (BUS), a label-free training framework to enhance reflective reasoning capability in challenging image analysis. BUS enables VLMs to perform backward prediction and provide explicit learning signals on data without ground-truth labels. In this way, BUS eliminates reliance on annotated data while improving reasoning performance. Notably, BUS is compatible with popular fine-tuning methods, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). Finally, extensive experiments on 8 benchmarks demonstrate the effectiveness of BUS across a wide range of complex visual tasks. It achieves notable improvements over the base model while using only unlabeled training data. Our experimental findings validate that backward prediction capability is critical for VLM reasoning.

---


### 58. [On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces](https://arxiv.org/abs/2607.07375)

**<font color=#1a73e8>作者：</font>** Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial vulnerability in deep neural networks (DNNs) has been studied from the perspectives of decision-boundary geometry, feature robustness, input-output Jacobians, and the instability of inverse problems. Here, we focus on the spectral structure of intermediate linear transformations that propagate information through modern DNNs, an unexplored mechanism of adversarial vulnerability. Specifically, we investigate transformer-based vision-language models, whose linear layers admit interpretable spectral decompositions and whose widespread adoption makes understanding their robustness increasingly important. We propose a white-box spectral-subspace-guided attack (SSGRA) that aligns intermediate representations with the subspace spanned by the bottom right singular vectors. Our experiments show improved attack effectiveness over existing baselines. In addition, SSGRA offers a spectral interpretation of adversarial vulnerability in VLMs, providing insights for improving their robustness.

---


### 59. [Physics-Audited Agentic Discovery in Scientific Machine Learning](https://arxiv.org/abs/2607.07379)

**<font color=#1a73e8>作者：</font>** Diab W. Abueidda, Bilal Ahmed, Panos Pantidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes a scoring evaluator before search, derives reviewable machine-checkable physics requirements, checks each trained candidate on its outputs, and separately searches prescribed input ranges or measured load-history spans for high-violation cases without reference solution fields. A surrogate is reported as verified only under the stated checks. When enabled, the workflow also adds advisory numerical probes before training and tests one modeling change at a time to record which isolated edits are associated with score gains before reuse. In the reported computational-solid-mechanics numerical examples, the static elasticity run selects a surrogate with lower validation error than the error-only baseline while both selected models pass the common linear-elastic checks. In the transient elastodynamics run, an error-only baseline with similar mean error fails a stricter causality check by responding to future parts of the loading history, while the selected surrogate passes the stated checks. The main distinction is per-candidate physics evidence on predicted fields, not a richer aggregate score.

---


### 60. [Generalist Vision-Language Models for Fast Radio Burst detection: a zero-shot benchmark against a specialized detector](https://arxiv.org/abs/2607.07382)

**<font color=#1a73e8>作者：</font>** Raiff H. Santos, Amilcar R. Queiroz, Tharcisyo S. S. Duarte 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast Radio Bursts (FRBs) are millisecond-duration radio transients whose automated detection increasingly relies on highly specialized deep learning models. These detectors achieve exceptional performance, but they require large task-specific training datasets and cannot be redefined without retraining. In this work, we evaluate whether small, open-weight, locally run generalist Vision-Language Models (VLMs) can detect FRBs in dynamic spectra under a zero-shot, prompt-only regime, with no fine-tuning and no labeled examples, returning structured decisions with a natural-language justification. From a controlled set of 3000 simulated L-band dynamic spectra containing FRBs, structured Radio Frequency Interference (RFI), and noise, we draw a balanced binary benchmark of 2000 samples and compare two such VLMs (Gemma 4 2B and 4B), sample by sample, against the state-of-the-art specialized detector SwinYNet. At the default threshold, Gemma 4 2B reaches an accuracy of 93.65%, with no statistically significant difference from SwinYNet (92.90%), while showing a significantly lower false-positive rate on structured RFI (6.4% vs. 25.0%) and no false positives on pure noise. SwinYNet retains a perfect probabilistic ranking on this benchmark (ROC-AUC of 1.0000 vs. 0.9482), a ceiling that the zero-shot VLM approaches from general-purpose pretraining alone. Rewriting the prompt alone reconfigures the same models for three-class FRB/RFI/noise classification on the full set of 3000 spectra, where they reach up to 86% accuracy without a single false FRB.

---


### 61. [MMAgent-R$^2$: Learning to Rerank and Reject for Agentic mRAG](https://arxiv.org/abs/2607.07383)

**<font color=#1a73e8>作者：</font>** Tao Zhang, Ziqi Zhang, Zongyang Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-based Visual Question Answering (KB-VQA) requires models to retrieve visual entities matching the query image from large-scale encyclopedic knowledge bases and answer related questions. Existing multimodal Retrieval Augmented Generation (mRAG) methods rely on global visual features to match candidate entities, yet when the knowledge base contains numerous visually similar entities, the retriever struggles to distinguish them, populating the candidate set with visually similar but factually mismatched distractors. Since subsequent processing steps such as noise filtering are also confined to this fixed candidate set, errors from failed retrieval inevitably propagate to the final answer. To address these challenges, we propose MMAgent-R$^2$, an agentic mRAG framework that integrates visual reranking and active rejection as its internal verification mechanism. Visual reranking directly compares query and candidate images, capturing discriminative details beyond textual descriptions to precisely identify the target entity among similar candidates; active rejection discards unreliable results and retrieves additional candidates when no confident match is found, moving beyond the fixed candidate pool. We design a composite reward function with step-level verification rewards and achieve joint optimization of external retrieval, internal verification, and answer generation via GRPO training. Experiments on InfoSeek, E-VQA, and MMhops demonstrate that \ours{} achieves state-of-the-art performance, with particularly notable advantages in challenging retrieval scenarios and complex multi-image multi-hop reasoning tasks.

---


### 62. [A Large Language Model-Driven Agent-Based Modeling Framework with Multi-Round Communication for Simulating Vaccine Opinion Dynamics](https://arxiv.org/abs/2607.07387)

**<font color=#1a73e8>作者：</font>** Bo Zhang, Na Jiang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recently, Large Language Models (LLMs) have been utilized in various applications of computational social science and provide the possibility to integrate such models into agent-based modeling to explore the cognitive processes. However, how specific cognitive modules drive individual decisions and macro-level opinion dynamics remains unclear. Therefore, this study introduces a framework that integrates an LLM (Qwen3-8B) into agent-based modeling to investigate this problem, using vaccination opinion dynamics as a case study. We utilize this framework to simulate opinion dynamics among agents with heterogeneous profiles and social networks, evaluating scenarios by enabling different cognitive modules: a memory module and a prompt diversity module. The simulation results reveal that different cognitive modules have opposite impacts on our emergent opinion. Furthermore, the framework reproduces the non-linear behavior patterns of social influence observed in existing research, demonstrating our framework's validity and potential to reach the level 3 validation of agent-based models.

---


### 63. [TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models](https://arxiv.org/abs/2607.07388)

**<font color=#1a73e8>作者：</font>** Yutang Ma, Kecheng Huang, Xikun Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrieval augmentation, or longer contexts. Engram-style memory offers a compact hidden-state injection pathway, but existing GPU-resident designs often rely on hash-based compression, causing unrelated phrases to collide in shared slots and weakening phrase-level semantic fidelity. We present TF-Engram, a train-free Engram system that constructs phrase-specific semantic memory offline from external corpora, stores large memory tables across a GPU--DRAM--SSD hierarchy, and uses Early-Exit Guided Predictive Prefetching to hide external-memory latency during autoregressive decoding. On Qwen3-0.6B, TF-Engram improves the average downstream score from 57.6 to 59.4, outperforming both the frozen backbone and a parameter-matched LoRA baseline. System evaluation shows that large TF-Engram tables can be built with moderate offline cost, SSD-backed storage substantially reduces GPU memory demand, and predictive prefetching recovers much of the throughput loss caused by external memory access. These results demonstrate that static phrase memory can be integrated into LLM inference as a scalable, train-free, and low-overhead system component.

---


### 64. [When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs](https://arxiv.org/abs/2607.07395)

**<font color=#1a73e8>作者：</font>** Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable confidence estimation remains a key limitation of test-time adaptation in vision-language models (VLMs), where prompt tuning improves zero-shot accuracy but often degrades calibration due to entropy-driven overconfidence. Prior approaches mitigate this using LLM-derived class attributes and contrastive regularization, yet treat attributes independently, ignoring their relational structure. We propose ARGTCA, which represents (class, attribute) pairs as nodes in a Symbolic Attribute Graph and trains a Graph Attention Network (GAT) using contrastive objectives to produce structurally informed embeddings that capture inter-attribute dependencies. We introduce two attribute selection strategies: ARGTCA-DIV for intra-class diversity and ARGTCA-DISC for inter-class discrimination. Experiments across nine benchmarks show that ARGTCA-DIV reduces average Expected Calibration Error (ECE) by approximately ~37% over baselines, while ARGTCA-DISC consistently performs as the second-best variant, reducing average ECE by approximately ~17% over baselines. These results suggest that modeling symbolic attribute interactions provides a principled approach for reliable test-time adaptation in VLMs.

---


### 65. [Agentic Data Environments](https://arxiv.org/abs/2607.07397)

**<font color=#1a73e8>作者：</font>** Elaine Ang, Chenxi Huang, Georgios Liargkovas 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents promise substantial gains in speed, scale, and labor efficiency, but their failures can impose abrupt and often irreversible costs. The central challenge for agentic automation is therefore to increase the benefits of automation while bounding the consequences of failure.
While databases remain central to modern computing, agents operate over a broader data environment spanning files, APIs, applications, and system state. In this talk, I will outline early work on Agentic Data Environments -- the execution substrate in which agents operate -- that both amplify agent capabilities and enforce safety guarantees. This perspective reframes data systems from passive stores of state into active substrates for safe, reliable execution.

---


### 66. [Heterogeneity-Adaptive Diffusion Schrodinger Bridge for PET-Guided Whole-Body MRI Translation](https://arxiv.org/abs/2607.07401)

**<font color=#1a73e8>作者：</font>** Chengbo Wang, Jiacheng Yu, Linjie Bian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While whole-body multimodal medical imaging scanners have been increasingly recognized for more effective medical applications, the excessive long acquisition time in PET-MR scanning is a major obstacle in more efficient clinical practice. Deep learning-based MRI translation provides a potential solution to reduce scan duration. However, current models often focus on specific anatomical regions and face challenges for whole-body scans that consists of highly heterogeneous feature distributions mainly due to (1) different anatomical regions across whole-body, and (2) lesions or pathological tissues. This paper tackles the challenges through a novel Heterogeneity-Adaptive Diffusion Schrodinger Bridge (HA-DSB) framework. By explicitly modeling translation as stochastic transport between source and target distributions, HA-DSB incorporates region context embeddings derived from a vision-language model (VLM) to enable region-specific modeling. To enhance fidelity of the pathological tissue, lesion-aware metabolic prior from PET is integrated directly into the bridge dynamics through a dual-stage guidance mechanism. Specifically, a PET-guided noise modulation module adaptively scales spatial diffusion perturbations during the forward process, while PET features are leveraged during the reverse process to selectively amplify lesion-relevant structures via an attention mechanism. Experiments demonstrate the superiority of our method across different body regions in whole-body MRI translation and show improved translation quality in lesion areas under PET guidance. Our code is available at Github.

---


### 67. [Multi-Agent Robotic Control with Onboard Vision-Language Models](https://arxiv.org/abs/2607.07403)

**<font color=#1a73e8>作者：</font>** Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

---


### 68. [Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents](https://arxiv.org/abs/2607.07405)

**<font color=#1a73e8>作者：</font>** Vikas Reddy, Sumanth Reddy Challaram, Abhishek Basu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully. In policy-permissive environments, a tool may execute any well-formed call even when the corresponding state transition is forbidden by domain policy. The result is a silent wrong state (a booking cancelled, a passenger count changed, a claim acted on without verification) that neither the tool nor the agent's self-report exposes.
We study this failure mode in the $\tau^2$-bench airline domain. On a budget agent, 78% of observed failures are silent wrong-state failures with no tool error, and the aggregate failure rate is reproducible across disjoint seeds, not sampling noise. We then evaluate a lightweight intervention: deterministic, read-only pre-execution gates that inspect the proposed call and current state before allowing a write. A four-gate suite raises full-benchmark success from 29.6% to 42.0% on gpt-4o-mini (+12.4pp; paired task-level bootstrap P=0.0012), and the lift reproduces on a disjoint 15-seed set (+12.3pp; P=0.0008).
The effect is concentrated where the gates fire: on the 26/50 firing tasks, success rises by +19.2pp, while movement on the 24 non-firing tasks does not exclude zero. Two negative controls (a self-enforcing retail domain and BFCL) bound the mechanism: gates help when tools are policy-permissive and add little where tools already self-enforce. As suggestive evidence, not a central claim, the same failure mode persists at the frontier: gpt-5.2 at default reasoning still attempts policy-violating writes, and the same suite improves success from 61.2% to 71.6% (+10.4pp; P=0.020; n=5, no replication). The contribution is a bounded evaluation and reliability result: deterministic gates do not guarantee task success, but they can deterministically prevent a known class of silent policy-violating writes at the action boundary.

---


### 69. [SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis](https://arxiv.org/abs/2607.07467)

**<font color=#1a73e8>作者：</font>** Songhan Wang, Haoang Chi, He Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end spatiotemporal analysis and narrative generation. SpaCellAgent utilizes a multi-agent architecture for strategic workflow planning, a dynamic tool-orchestration engine for adaptive algorithm selection, and a self-evolution module that iteratively refines performance through feedback. We evaluate SpaCellAgent on six heterogeneous datasets encompassing complex temporal developmental trajectories, diverse sequencing platforms, and spatially-resolved tissue architectures. SpaCellAgent consistently demonstrates over 40\% improvement in analytical efficiency while maintaining expert-aligned performance. By converting natural language specifications into optimized analytical workflows and fully automating the pipeline, SpaCellAgent democratizes advanced spatiotemporal modeling and establishes a scalable, agent-driven paradigm for computational biology. The code and materials are available at this https URL.

---


### 70. [SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation](https://arxiv.org/abs/2607.07469)

**<font color=#1a73e8>作者：</font>** Andrea Scarinci, Virginia Negri, Brayan Impata 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) for e-commerce attribute extraction requires labeled data representative across thousands of product types, attributes, and multiple languages. This combinatorial scale translates to millions of annotations, rendering human labeling prohibitively costly. While recent work has demonstrated synthetic label generation using LLMs, deploying such approaches at industrial scale requires integrated quality control mechanisms. We present SynthAVE, a large-scale human-validated benchmark for attribute value extraction spanning 12,726 products across 229 product types, 792 attributes, and 4 languages (Spanish, French, Italian, German). To validate synthetic labels at scale, we introduce a multi-LLM arena framework where samples are independently evaluated by 21 judge configurations (7 model families $\times$ 3 prompts), with final labels determined via majority voting. The majority vote ensemble agrees with human experts at Cohen's $\kappa = 0.92$ (95.2% agreement), while individual judges show substantial inter-model agreement (Fleiss' $\kappa = 0.76$). This demonstrates that diverse models with varying individual judgments aggregate into highly reliable predictions, enabling cost-effective validation at scale while maintaining quality parity with human review.

---


### 71. [TimEE: End-to-end Time Series Classification via In-Context Learning](https://arxiv.org/abs/2607.07500)

**<font color=#1a73e8>作者：</font>** Jaris Küken, Shi Bin Hoo, Martin Mráz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification (TSC) is dominated by a two-stage paradigm: train a feature encoder -- either from scratch on the target dataset or via pretraining on large corpora -- and then fit a task-specific classifier on top. While effective, this decoupling optimizes representation learning independently of the classification objective, requires per-dataset training, and prevents the model from exploiting label information during inference. We introduce TimEE, a 4.5M-parameter foundation model for end-to-end TSC via in-context learning. Given a labeled support set and a query time series, TimEE directly outputs a predicted class distribution in a single forward pass with no per-dataset training required. Following the prior-data fitted network (PFN) framework, TimEE is meta-trained exclusively on synthetic TSC tasks, where each task contains time series with distinct class identities arising from structured distributional shifts in the generative process. Despite seeing no real time series during pre-training, TimEE ranks first in ROC AUC (and third on accuracy) on the UCR benchmark among all compared methods, which include both foundation models and supervised deep learning baselines. To our knowledge, TimEE is the first purely synthetic-pretrained model to reach state-of-the-art performance on the UCR benchmark. These results establish end-to-end ICL with synthetic priors as a compelling, largely unexplored direction for TSC, with scaling, prior design, and richer generation mechanisms as natural avenues for improvement. Code is publicly available at this http URL.

---


### 72. [Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows](https://arxiv.org/abs/2607.07504)

**<font color=#1a73e8>作者：</font>** Wei-Jung Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck. We ask whether LLM-generated skills offer a useful low-curation alternative: do they improve performance over the task prompt alone? We test this question across four lifecycle stages: data preparation, data extraction, statistical analysis, and reporting, using one generated skill per stage. We find no reliable improvement from full generated skills over No-Skill prompting. We then ask whether any part of the skill is useful by ablating different skill components. The main ablation covers 56 tasks, nine model configurations, and three providers, yielding 7,560 runs. Compared with prompting using the task alone, neither the full generated skill nor any ablated skill variant significantly improves performance; all p-values are at least 0.396, and the total spread across variants is only 1.2 pp. A supplemental token-matched control adds 1,512 runs and finds that Full skills perform similarly to task-irrelevant skill-formatted content. The results caution against using one LLM-generated skill per data-science workflow as a default single-shot prompting strategy.

---


### 73. [HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models](https://arxiv.org/abs/2607.07507)

**<font color=#1a73e8>作者：</font>** Feng He, Zhenting Wang, Qifan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hallucinations in vision language models (VLMs) are commonly treated as semantic errors, yet they often arise from partial or ambiguous visual evidence. Prior work mainly focuses on detecting or suppressing hallucinations at generation time, leaving the subsequent reasoning stage largely unexplored. In this work, we study Post Hallucination Reasoning (PHR), the stage in which hallucinated semantics enter the model's inference context and influence downstream predictions. To systematically investigate PHR, we introduce HIVE, Hallucination Inference and Verification Engine, an evaluation infrastructure that enables controlled comparisons between faithful and hallucinated captions. Across nine tasks and nine models, we observe structured modality dependent patterns: hallucinated captions often improve accuracy on vision language tasks, while text only tasks exhibit limited or unstable effects. Further analyses show that hallucinated cues broaden semantic coverage and reshape reasoning dynamics while preserving stable inference. These findings highlight that hallucinated semantics may influence downstream reasoning once they enter the model's inference context. Understanding this post hallucination stage is important for improving the reliability and interpretability of multimodal reasoning systems. Code is publicly available at this https URL.

---


### 74. [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508)

**<font color=#1a73e8>作者：</font>** Zhenyu Hou, Yujiang Li, Jie Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently, asynchronous RL has emerged as a more efficient alternative by updating the model as rollouts arrive. However, existing asynchronous RL systems often emphasize throughput, while leaving training stability and task effectiveness largely underexplored. For example, a key challenge is that group-wise sampling in the widely-used GRPO framework does not naturally fit asynchronous agentic training. In this paper, we present Single-rollout Asynchronous Optimization (SAO) to address the stability and off-policy challenges in asynchronous RL. To reduce off-policy effects and improve generalization, we replace group-wise sampling with single-rollout sampling, that is, using one rollout per prompt. We further improve this single-rollout strategy with practical value-model training designs. To improve optimization stability, we introduce a strict double-side token-level clipping strategy. SAO is able to train stably for one thousand steps and consistently outperform GRPO and its variants on agentic coding and reasoning benchmarks, such as SWE-Bench Verified, BeyondAIME, and IMOAnswerBench. We also demonstrate that single-rollout RL is particularly effective in a simulated online learning setting, where the model must adapt to changing evolving environments. To this end, SAO is successfully deployed in the agentic RL pipeline for training the open GLM-5.2 model (750B-A40B).

---


### 75. [Creativity from Friction: Human-AI Interaction for Exploratory Structural Design](https://arxiv.org/abs/2607.07521)

**<font color=#1a73e8>作者：</font>** Ricardo Maia Avelino, Rita Sevastjanova, Tom Van Mele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents that generate final answers based on user input often do not meet the needs of creative fields. Fields such as structural design and architecture need interactive systems that help users externalise and develop ideas, explore alternatives, and refine partial solutions. The final product of such designs needs to comply with many constraints concerning, e.g., spatial configuration, mechanical behaviour, material quantities, and costs. These constraints create friction in the design process, which can stimulate novel and creative solutions. In this paper, we discuss the misalignment between current generative AI goals to remove friction and provide final solutions and the needs of creators, such as structural designers, who develop ideas through iterative work. We present the design dimensions of systems allowing for constrained human-AI co-creation that rely on vision-language models making structural exploration conversational, multimodal, and responsive to evolving human intent in ways that follow and augment the discipline's creative process. Through a pilot design interface based on these principles and a study with experts in the field, this paper shows how structural designers perceive interactive AI systems and how such systems can support design space exploration by reducing repetitive modelling friction while preserving reflective design friction.

---


### 76. [PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning](https://arxiv.org/abs/2607.07557)

**<font color=#1a73e8>作者：</font>** Yazdan Jamshidi, Alexey Shvets  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexity versus 12.92 for uniform Wanda (mean over 9 runs, $p < 0.001$). The benefit is architecture-dependent: LLaMA-3-8B shows marginal gains and Mistral-7B shows none. We also find that gradient-based allocation -- the seemingly more principled approach -- produces results worse than random, suggesting that gradient magnitude does not predict the impact of discrete weight removal. PALS adds negligible cost to the pruning pipeline and requires no fine-tuning.

---


### 77. [Future Confidence Distillation in Large Language Models](https://arxiv.org/abs/2607.07626)

**<font color=#1a73e8>作者：</font>** Sahil Kale  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation depend on accurately estimating answer reliability. Existing approaches, however, largely treat confidence as a property of completed responses, overlooking how confidence-related information evolves throughout the answering process. In this work, we investigate confidence from a temporal perspective by comparing pre-solution Feeling-of-Knowing (FOK) and post-solution Judgement-of-Learning (JOL) confidence estimates across frontier and open-source LLMs. We show that post-solution confidence is consistently better calibrated and more discriminative than pre-solution confidence, while linear probes trained on hidden representations recover substantially richer confidence-related information than models explicitly verbalise. Building on this observation, we introduce future confidence distillation, which trains predictors operating on pre-solution hidden representations using teacher confidence estimates produced by post-solution correctness probes. Despite requiring only pre-solution representations for inference, distilled predictors recover much of the calibration improvement achieved by post-solution confidence, remain highly sample efficient, and transfer across datasets within the same domain. Together, our findings demonstrate that confidence-related information evolves throughout the answering process and can be anticipated before answer generation is complete, enabling significantly more reliable yet low-cost confidence estimation.

---


### 78. [RL Post-Training Builds Compositional Reasoning Strategies](https://arxiv.org/abs/2607.07646)

**<font color=#1a73e8>作者：</font>** Azwar Abdulsalam, Nishil Patel, Andrew Saxe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that remain rarely solved by the pretrained model even under much larger sampling budgets, while rejection fine-tuning improves early but plateaus. Trace analysis shows that RL reorganizes primitive competence through a phased compositional mechanism: it first strengthens primitive reductions, then discovers valid composed procedures. These include sequential compositions, which collapse ordered chains of primitive contractions, and parallel compositions, which combine independent primitive contractions in a single step. The composed procedures are not isolated samples; they are reused and consolidated into a stable repertoire. Comparing RL with rejection fine-tuning shows that the key difference is not exploration volume but selectivity: RFT produces many shortcut-like rewrites, much of them invalid, whereas RL concentrates exploration into valid reusable structure. Pretraining ablations show that the emergence of compositional strategies is gated not by primitive exposure alone, but by whether pretraining organizes primitive competence into reduction procedures that RL can later compress. The base model provides weak procedural ingredients; RL builds them into reliable higher-level strategies.

---


### 79. [DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation](https://arxiv.org/abs/2607.07669)

**<font color=#1a73e8>作者：</font>** Jordan Painter, Dipankar Srirag, Adarsh Kappiyath 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled comparison of these components across Australian, Indian, and Northern British English. Our results reveal that dialectal robustness and generation are \emph{dissociated}: benchmarks are shaped by continual pretraining and SFT, while alignment visibly reshapes generation in ways benchmarks do not capture. Explicit variety-targeted adaptation produces output reliably recognised as dialectal and preferred over broad alignment, yet the method that most aggressively optimises the dialectal reward is not preferred by human evaluators. Independent linguistic analysis corroborates this reward-quality gap, most clearly on two of the three families. No single alignment method dominates, and closing the gap will require richer reward designs and continued investment in dialectal resources. We release all code, checkpoints, and preference datasets.

---


### 80. [PeTeR: Post-Training Robustification of Probabilistic Circuits](https://arxiv.org/abs/2607.07671)

**<font color=#1a73e8>作者：</font>** Adrian Ciotinga, Yeming Dai, YooJung Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnerable to overfitting and fragile generalization when confronted with data noise, small sample sizes, or distribution shifts. This can be mitigated using distributionally-robust optimization which consider worst-case distributions within a Wasserstein ball of the empirical distribution, but current methods are limited to training a model from scratch in this framework. Instead, we propose PeTeR: a novel, data-free post-training framework designed to robustify pre-trained PCs against distribution shifts without retraining from scratch. Empirical evaluations across multiple density estimation benchmarks demonstrate that PeTeR effectively robustifies baseline models against both random and adversarial perturbations, achieving competitive or superior performance to data-dependent robust learning baselines.

---


### 81. [MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](https://arxiv.org/abs/2607.07673)

**<font color=#1a73e8>作者：</font>** Hyunjae Kim, Dain Kim, Pan Xiao 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable framework that transforms permissively licensed literature into high-fidelity infrastructure for medical multimodal models. Applied to 6.1 million PMC articles, MedPMC curated 11 million medical image-text pairs. Component evaluations showed strong performance for initial screening (F1 = 93.2), multi-panel figure detection (F1 = 96.5), figure separation (mAP = 89.8), caption separation and alignment (F1 = 81.4; ROUGE-L = 85.3), and medical figure classification (F1 = 96.5). Manual review by five annotators, three with medical training, found 95.3% of MedPMC images medically relevant, versus 19.7% in a prior PMC-derived dataset. Across 26 benchmarks spanning 11 specialties, a MedPMC-trained CLIP-style model improved average zero-shot AUC by 7.1 percentage points over the strongest architecture-matched biomedical CLIP baseline despite using fewer than half as many image-text pairs. As the vision encoder in a multimodal large language model, it improved medical visual question-answering by 1.9 and 16.9 percentage points across two benchmarks. In 10,524 Yale New Haven Health System dermatology photographs, it improved morphology-to-image retrieval Recall@5 by 11.7 percentage points. These findings show that high-fidelity literature curation strengthens medical multimodal foundation models across benchmark and clinical settings. We publicly release the framework, corpus, benchmarks, and pretrained models.

---


### 82. [Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF](https://arxiv.org/abs/2607.07693)

**<font color=#1a73e8>作者：</font>** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that substantially improve the feedback efficiency of diffusion RLHF while preserving generalization to unseen prompts. Our key observation is that reward information in diffusion trajectories is unevenly distributed: not all denoising timesteps or trajectories contribute equally to learning from a reward signal. By emphasizing informative timesteps and trajectories during optimization, we obtain more effective gradient updates. First, we introduce a per-timestep weighting scheme that reweights denoising steps during policy optimization. We theoretically connect this weighting to the optimal convergence properties of proximal policy optimization (PPO) and approximate the resulting weighting trend empirically. Second, we introduce a replay mechanism that prioritizes informative trajectories, enabling the model to reuse past samples instead of repeatedly querying new rewards. Together, these strategies significantly improve the feedback efficiency of diffusion RLHF. Under identical hyperparameter settings, our approach achieves up to a 6$\times$ improvement in sample efficiency compared to widely used diffusion RLHF baselines.

---


### 83. [Co-LMLM: Continuous-Query Limited Memory Language Models](https://arxiv.org/abs/2607.07707)

**<font color=#1a73e8>作者：</font>** Yair Feldman, Linxi Zhao, Nathan Godey 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant departure from prior reliance on relational KB and queries. CO-LMLM generates flexible vector queries at minimal cost, while still integrating human-readable and attributable retrieved knowledge into its generation. We pair this design with an annotation pipeline that tags free-form factual spans in arbitrary text, removing prior work's restriction to Wikipedia. Across pretraining on Wikipedia and FineWeb-Edu and at multiple model scales, CO-LMLM outperforms prior LMLMs and vanilla LLMs in both perplexity and factual precision. At 360M scale, this includes lower perplexity than models pretrained on 40x more data, and SimpleQA-verified performance that is in line with gpt-4o-mini and higher than Claude Sonnet 4.5.

---


### 84. [Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning](https://arxiv.org/abs/2607.07708)

**<font color=#1a73e8>作者：</font>** Chen Tang, Yizhou Wang, Jianyu Wu 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint challenge of representation and reasoning: models must preserve domain-native structural information while showing how specific evidence supports predictions under these constraints. Here we introduce SciReasoner, a multimodal scientific foundation model for native structural reasoning across proteins, small molecules and inorganic crystals. SciReasoner discretizes coordinates, topologies and periodic connectivities into a unified structure-aware vocabulary, treating structural tokens as addressable evidence units during reasoning. In homology-controlled Gene Ontology prediction, SciReasoner improves Cellular Component annotation for low-homology and orphan-like proteins, increasing $F_{\max}$ from 0.42 to 0.55. In chemistry, it raises single-step retrosynthesis accuracy from 0.63 to 0.72 while generating fragment-level disconnection and precursor-verification traces. In materials science, its representations separate elemental and compound phases and resolve high- and low-band-gap regimes. Across 86 benchmarks, SciReasoner achieves state-of-the-art performance on 67 tasks. Double-blind expert evaluation rates its reasoning traces as preferred or at least comparable to those of a frontier large language model in 98% of cases. By making structure an inspectable substrate for reasoning under scientific constraints, SciReasoner connects accurate prediction with interpretable scientific inference.

---


> [!TIP]
> 当前位于：**51-84**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-84**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
