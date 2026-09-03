# 🧠 大模型相关研究 | 2026年09月04日

> 本类共 **177** 篇论文：已确认 **170** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-177](./part-04.md)

---

### 101. [What Is Worth Representing? Representational Empowerment for Continual Model Construction](https://arxiv.org/abs/2609.02322)

**<font color=#1a73e8>作者：</font>** Fei Dai, Hanqi Zhou, Alison Gopnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The first problem of modeling the world is not just estimating the right parameters or causal structure, but deciding what should be represented at all. We frame this problem as continual model construction: an agent maintains an environment-specific model M of an inaccessible world W and curates a persistent library L of reusable representational elements across environments. We propose Representational Empowerment (RepEmp) to score candidate elements by how much they expand the agent's future capacity to model and plan, complementing the classic definition of empowerment, but redefined as control over internal representations instead of external states. We realize the framework as a hierarchical Curator-Actor architecture and test it across three experiments. In a closed-vocabulary causal-learning task, human participants construct causal models at varying abstraction granularities to maximize goal reachability rather than fidelity to the world, a signature better predicted by RepEmp than by information-gain alternatives. Matched simulations reveal that RepEmp-guided construction contributes more than exploration to sufficient structure recovery and cross-task transfer. Finally, in an open-vocabulary planning domain, an LLM-augmented Curator builds more compact symbolic libraries, which also generalize better than baselines. Ablating RepEmp eliminates these benefits. Together, these results identify RepEmp as a key principle for continual model construction: deciding what to build, retain, and reuse under bounded resources.

---


### 102. [SALA: Semantic-Aware Logical Alignment for Complex Reasoning in In-Context Learning](https://arxiv.org/abs/2609.02336)

**<font color=#1a73e8>作者：</font>** Zhao Ji, Wenqing Chen, Zhixuan Chu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective in-context learning (ICL) for complex reasoning relies on selecting the right demonstrations. Traditional retrieval methods based on surface similarity fail to capture the underlying problem-solving logic. Recent logic-based methods address this by matching predefined reasoning steps, but the rigid rules and exact-match criteria is improper to handle flexible or diverse reasoning processes. To address the problem, we propose SALA, a Semantic-Aware Logical Alignment framework. Instead of relying on a fixed inventory, SALA automatically learns task-specific reasoning operations. It then embeds these operations into a continuous semantic space and uses dynamic time warping (DTW) to align the reasoning sequences. This approach allows for soft, flexible matching of reasoning logic while remaining highly interpretable. Experiments across four reasoning benchmarks and three LLMs demonstrate that SALA outperforms existing demonstration selection methods. Further analysis confirms the roles of the operation induction and the logical semantic alignment.

---


### 103. [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](https://arxiv.org/abs/2609.02341)

**<font color=#1a73e8>作者：</font>** Caio Azevedo, Stefano Sabatini, Sascha Hornauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models (VLAs) have shown strong potential in autonomous driving by leveraging multimodal pretraining for instruction following, visual reasoning, and scene-level generalization. In robotic manipulation, scaling VLA fine-tuning across multiple robot setups--especially when unifying representations across embodiments--has been shown to improve in-dataset performance and cross-embodiment generalization; in autonomous driving, however, VLAs remain largely trained on individual datasets and are rarely evaluated for zero-shot transfer to unseen datasets and camera rigs; furthermore naively adding more datasets to the training data does not necessarily lead to better performance within seen embodiments. To address these problems, we study multi-dataset training for the driving task and BEV-Forcing, an auxiliary objective that transfers ground-plane object-layout information from a specialized Bird's-Eye-View model into the VLA backbone. By encouraging the model to represent object position through a shared BEV spatial interface, we show that an auxiliary task such as BEV-Forcing can improve both in-distribution and out-of-distribution performance when training on a small number of camera rigs. As the number of training embodiments increases, however, the benefits of the auxiliary task are reduced; we present this as evidence that new techniques in the literature may see their benefits diminish when simply scaling up training diversity, which motivates presenting results taking into account data scaling.

---


### 104. [LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory](https://arxiv.org/abs/2609.02350)

**<font color=#1a73e8>作者：</font>** Kun-Yang Yu, Yingzhe Li, Hongyu Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) requires an embodied agent to follow natural-language instructions in unseen environments. Recent progress has been largely driven by Multimodal Large Language Models (MLLMs). Existing methods follow a next-step action prediction paradigm, supervising only the expert action, which requires a high quantity of data for training. They also rely on cognitive maps, accumulated historical frames, or external 3D tools to maintain states, leading to high computational and memory overhead. To realize resource efficiency VLN, we propose LookStep, a unified end-to-end framework that combines Language Centric Future State Modeling and Event Driven Rolling Memory that uses language labels to generate coarse-grained navigation progress and future states for each candidate action, while autonomously deciding whether to write each observation into a bounded rolling memory with a semantic role. We validate LookStep empirically. On VLN-CE tasks, LookStep outperforms existing methods under the same training settings, achieving a 49.7\% success rate on R2R-CE Val-Unseen with better memory efficiency and less data usage. Code and model is available at this https URL.

---


### 105. [TempoGround: State-Aware Streaming Visual Grounding with Vision-Language Models](https://arxiv.org/abs/2609.02359)

**<font color=#1a73e8>作者：</font>** Leqian Ding, Junning Qiu, Manwen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding maps language referents to spatial targets and is central to open-vocabulary perception with vision-language models. Existing methods have made substantial progress on single-frame and video-based visual grounding, yet under streaming inputs they still suffer from identity drift, cross-frame inconsistency, and fragile localization under partial occlusion. To address these issues, we present TempoGround, a VLM-native framework that detects cross-frame object correspondence and explicitly models object presence states, thereby enabling accurate and consistent visual grounding under streaming inputs. The key is a curriculum prediction mechanism guided by state-aware cross-frame correspondence: TempoGround resolves 2D instance association, predicts whether each object newly enters, continues in, or leaves the view, decodes the 2D box, and then lifts it to a camera-frame 3D box. As token-level supervision alone cannot capture the geometric objectives of streaming grounding, we further introduce Streaming Grounding Reinforcement (SGR), which optimizes TempoGround with verifiable Grounding, Identity, and Consistency rewards, jointly reinforcing persistent localization and temporally consistent predictions. We carefully design a three-stage training strategy and train TempoGround on large-scale data. We evaluate visual grounding under causally streaming inputs on multiple challenging benchmarks: TempoGround improves F1_2D@0.5 and F1_2D@0.95 by 4.4 and 0.5 on average, and F1_3D@0.25 and AP_3D by 6.2 and 7.5, respectively. These results demonstrate that TempoGround provides a practical foundation for visual grounding under streaming inputs.

---


### 106. [NE-R1: Enhancing Named Entity Recognition Model via Reinforcement Learning](https://arxiv.org/abs/2609.02366)

**<font color=#1a73e8>作者：</font>** Meixuan Chen, Hehan Li, Ruizhi Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition (NER) has achieved substantial progress since the advent of large language models (LLMs). Nevertheless, the recognition of long-tail and domain-specific entities remains challenging due to the deficiency in parametric knowledge. Retrieval-augmented generation (RAG) offers a promising remedy by injecting external knowledge, but it also introduces noise and unnecessary cost when dealing with familiar cases. In this paper, we propose NE-R1, a novel framework for adaptive retrieval-augmented NER. We design a "retrieval-on-demand" mechanism for NER. Then we integrate it into models by a two-stage training method: (1) multi-task instruction tuning initialization; (2) end-to-end RL optimization with CoT. To achieve reasonable selection between parameterized and external knowledge, we design a multi-dimensional reward considering both accuracy and retrieval benefit. NE-R1 achieves state-of-the-art performance on various benchmarks, with an average F1 score gain of 2.52% in in-domain evaluation and 1.18% in zero-shot cross-domain evaluation.

---


### 107. [Diagnosing with Insights: Structured Analysis of Agent Failures via Behavioral Abstractions](https://arxiv.org/abs/2609.02371)

**<font color=#1a73e8>作者：</font>** Jiayi Bi, Yanjie Gao, Yuanmin Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the proliferation of LLM agents, the ability to understand and diagnose failures in agents is essential to achieving superior effectiveness and trustworthiness. As agent failures often manifest via long and complex trajectories, manually finding the needles in the haystack is untenable. However, traditional diagnosis techniques for software bugs can hardly address LLM agent failures, while completely relying on LLMs as the judge yields unreliable diagnosis results. To overcome these challenges, this paper presents AGENTSCOPE, a new neuro-symbolic approach for agent failure mode diagnosis. The key principle of AGENTSCOPE is to abstract agent behavior, based on its trajectories, into structured representations. Furthermore, AGENTSCOPE introduces the concept of neural invariants to specify agent behavior properties. AGENTSCOPE leverages LLM-guided reasoning atop the structured representation against neural invariants to pinpoint both the failure step and its type in the trajectory. We show the effectiveness of AGENTSCOPE on publicly available agent failure datasets (Who&When) and a more comprehensive dataset created by us (AgentErrata), where AGENTSCOPE significantly outperforms the current state of the art in fault localization and attribution accuracy. Our work shows that integrating structured abstractions with LLM-guided reasoning enables effective, reliable, and interpretable diagnosis for agent failures.

---


### 108. [MultiGhostBench: A Multilingual Benchmark for Long-Form LLM-Generated Text Attribution under Distribution Shifts](https://arxiv.org/abs/2609.02379)

**<font color=#1a73e8>作者：</font>** Matteo Greco, Anudeex Shetty, Andrea Tagarelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While existing work on LLM authorship attribution (AA) has made progress, available benchmarks remain limited, often focusing on English, controlled settings, or relatively outdated models, with the few multilingual studies considering only relatively short texts. We introduce MultiGhostBench, a multilingual benchmark comprising 928 books generated by five recent LLMs across six languages and three scripts, with an average length of approximately 59K words per book. The benchmark supports evaluation under domain, author, and language shifts. Evaluation of representative AA methods shows that no single method consistently performs best across settings, and performance generally degrades under distribution shifts. Transformer-based detectors can retain generator-related information across languages, although transfer effectiveness varies by language pair, whereas statistical and fingerprint-based detectors are more language-dependent. We envision MultiGhostBench as a valuable resource for the development and evaluation of robust AA methods. The dataset and code can be found at this https URL.

---


### 109. [PolERo: Studying Political Evasion in Romanian](https://arxiv.org/abs/2609.02391)

**<font color=#1a73e8>作者：</font>** Gabriel Stefan, Sergiu Nisioi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political evasion refers to responses that engage with a question while withholding the requested information. Recent NLP work frames political evasion as a classification task using a two-level taxonomy of response clarity and fine-grained evasion strategies. Existing work on response clarity and evasion classification is limited to English, leaving open whether the taxonomy and model behavior transfer across languages and political contexts. We introduce PolERo, a dataset of 3,574 human-annotated question-answer pairs extracted from official transcripts of five Romanian presidents. We evaluate multiple classification approaches on both datasets under matched conditions, including TF-IDF baselines, fine-tuned encoder models, a proposed sliding-window encoder, and zero/few-shot LLM prompting. We study cross-lingual transfer through joint bilingual training and machine-translation-based data augmentation. Our results indicate that fine-tuned encoders are competitive, cross-lingual transfer is asymmetric, and ambivalent evasion categories involving pragmatic cues remain the main challenge across all model families.

---


### 110. [CAPTCHAs in the Agentic Era: Solvers That Learn from Every Encounter](https://arxiv.org/abs/2609.02393)

**<font color=#1a73e8>作者：</font>** Oguzhan Salman, Kemal Bicakci  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can solve visual CAPTCHAs without task-specific training, but the agents built on them approach every challenge from scratch. For such an agent, the hundredth instance of a familiar puzzle costs as much time and compute as the first. Specialized detectors invert the trade-off, answering in milliseconds but only for categories they were trained on. Neither improves with exposure. We study what changes when a solver improves with use. Our system pairs a fine-tuned YOLOv8 detector with an open-weight VLM behind a confidence-based router, and runs entirely from screenshots and operating-system input events, with no browser automation or DOM access. It reaches 85.4% overall and 84.2% macro accuracy across 16 classes, exceeding either component alone. Every answer VLM produces also serves as a training label, so the detector absorbs categories it was never trained for, typically after one or two encounters and without human annotation. The same loop also repairs it. A CAPTCHA operator can perturb images against the publicly released detector and drive its accuracy to 0%, but the perturbations leave VLM untouched, and its labels let the detector recover. Under a year-long simulated arms race in which the CAPTCHA operator re-crafts its perturbations each month, the solver recovers every round, and a cheap ~70%-accurate open-weight teacher hardens it as effectively as a perfect oracle. Visual CAPTCHA defenses that assume a failing bot stays failing therefore understate how quickly an adaptive solver returns.

---


### 111. [Improving Health Literacy through Lay Summarization of Radiological Reports: An Evaluation of BioNER and Retrieval-Augmented Generation](https://arxiv.org/abs/2609.02396)

**<font color=#1a73e8>作者：</font>** Egecan Çelik Evgin, İlknur Karadeniz, Olcay Taner Yıldız  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Radiology reports are written primarily for clinicians, and their specialized terminology often makes them difficult for patients to interpret. As a result, many patients turn to publicly available Large Language Models (LLMs) to help explain their reports, despite well-documented risks of factual inaccuracies and hallucinations. Automated lay-summary generation has emerged as a promising alternative, yet the effectiveness of retrieval-enhanced and clinically informed approaches for radiology-specific communication remains underexplored. This study investigates the extent to which Retrieval-Augmented Generation (RAG) and Named Entity Recognition (NER) improve the quality, factual consistency, and readability of automatically generated lay summaries compared with standard LLM-based generation. We develop a framework combining NER-based extraction of clinically relevant findings with a RAG mechanism for contextual grounding, evaluated across few-shot and fine-tuned variants of two models (Qwen, BioBART). Results show that NER consistently improves readability and overall quality, while RAG alone offers no benefit and can introduce hallucinations from irrelevant retrieved terms. Combining RAG with NER degrades performance in few-shot settings but improves readability when fine-tuned. Fine-tuned BioBART with NER achieves the best overall performance, highlighting entity-aware extraction as the primary driver of improved patient-friendly summaries.

---


### 112. [CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction](https://arxiv.org/abs/2609.02401)

**<font color=#1a73e8>作者：</font>** Menghao Li, Linjie Mu, Yin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive vision language models unify heterogeneous perception tasks but are highly susceptible to compounding errors. On-policy distillation (OPD) bridges the training-inference mismatch by training students on their own rollouts. However, unreliable student predictions, especially early in training, can derail the trajectory and degrade the quality of teacher supervision. While recent interleaved distillation methods allow the teacher to verify and replace student tokens, they primarily rely on rigid ranking metrics rather than exact teacher confidence, and they overlook how intervention decisions can inform token-level supervision. To address this, we introduce Confidence-Aware On-Policy Distillation (CA-OPD), a framework that couples reliable rollout construction with adaptive supervision. CA-OPD utilizes teacher confidence to selectively correct unreliable student transitions, gradually transferring rollout control to the student via a strict-to-relaxed schedule. Crucially, CA-OPD aligns knowledge transfer with these intervention decisions: corrected positions receive direct cross-entropy supervision from the teacher's prediction, while retained positions benefit from the teacher's full predictive distribution. Evaluated in a multi-teacher setting for GUI grounding and optical character recognition, CA-OPD substantially improves the Qwen3.5-0.8B baseline across all six target benchmarks, including gains of $9.50$ points on ScreenSpot-Pro and $6.72$ points on OCRBench-v2 English. Controlled studies further show that the gains depend on intervention placement, progressive rollout control, and intervention-aligned supervision, rather than intervention frequency alone.

---


### 113. [Evidence for Shared Routing Geometry and Dynamics in Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.02404)

**<font color=#1a73e8>作者：</font>** Kirill Labzin, Stepan Kulibaba, Artem Dzhalilov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) models use an independently parameterized router at each sparse layer to select experts for every token. Prior work has shown that routing decisions across depth can often be predicted from earlier routing signals, suggesting that routing is not fully independent across layers. However, the structure behind this predictability remains unclear. In this work, we provide evidence that routing-relevant states across layers share a common geometric structure that is obscured by layer-specific coordinate systems. We isolate the control subspace of each router and align these spaces into a shared canonical representation using generalized orthogonal Procrustes analysis. After alignment, a single linear transition reaches $R^2=0.39$--$0.71$ and retains 79--90\% of the predictive power of separately fitted layer-specific dynamics, indicating that much of routing-state evolution follows a reusable process across depth. We then ask whether this shared dynamics is specific to routing or simply reflects the smooth evolution of hidden representations. A matched-rank comparison shows that residual representations are often easier to predict across layers, while router-control states preserve the model's expert choices much more faithfully. This separates generic cross-layer predictability from routing-specific information. Finally, we test whether the predicted canonical states remain meaningful when used in place of native routing states. The transported states preserve local routing behavior, while learned state evolution reduces $\Delta\mathrm{NLL}$ relative to simple persistence by 15.7\% on OLMoE and 6.2\% over a 10-router horizon on Phi.

---


### 114. [The Diagnosis a Reporter Leaves Unspoken: Surfacing Frozen Tumor Features for Brain-Tumor MRI Reporting](https://arxiv.org/abs/2609.02411)

**<font color=#1a73e8>作者：</font>** Khawaja Murad ul Hassan, Ruqiyya Adil, Adil Qayyum 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A capable brain-MRI report generator can still be, in effect, diagnostically silent. When a multi-chain chain-of-thought (CoT) reporter built on a medical Mistral-7B backbone is evaluated on held-out cohorts, it names most meningiomas and almost all metastases "glioma" (diagnosis recall 0.44/0.07). Yet the answer is not absent from the model: a supervised linear probe applied to its frozen segmentation features recovers the three tumour cohorts at 0.82 macro-F$_1$ (5-fold cross-validation; chance $\approx$0.33). We introduce NeuroFusion, an assistive reporter that surfaces this latent signal rather than overriding it: discriminative field-classifier heads over per-lesion features condition a fast, single-pass draft-then-review decoder on their committed outputs. Built on the identical Mistral backbone, this restores the diagnosis (meningioma 0.92, metastasis 0.75) and wins 8 of 9 prose-content comparisons across three held-out cohorts (RaTEScore, RadGraph-F$_1$, GREEN; Holm-corrected paired BCa), with no significant loss on the ninth, at 5-6x lower latency ($\approx$80 vs. 457 s/case). A controlled negative result sharpens the mechanism: a learned diagnosis pin that overrides the decoder instead of merely informing it collapses out-of-distribution metastasis recall to 0.03. Grammar-constrained decoding keeps 92.3% of records schema-valid, making every sentence entailment-checkable (7.5% contradicted vs. 36.8% for the direct baseline). In a blinded nine-case pilot, two board-certified neurologists independently rated NeuroFusion highest in every tumour type, the only system with zero critical errors, and gave it the top-rated sign-off in eight of nine cases (six outright, two ties).

---


### 115. [UTP-Bench: Uncertainty-aware Travel Planning Benchmark](https://arxiv.org/abs/2609.02421)

**<font color=#1a73e8>作者：</font>** Etcharla Revanth Rao, Priyanshu Karmakar, Shubhojit Mallick 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently demonstrated strong capabilities in automated travel itinerary generation. However, real- world travel planning is inherently uncertain: transportation delays, crowd fluctuations, and unexpected stochastic delays frequently inval- idate otherwise feasible schedules. Existing benchmarks like TravelPlanner and TripCraft assume deterministic environments, evaluating only static constraint satisfaction and ignoring whether generated plans remain robust when such uncertainties arise. To address this limitation, we introduce UTP-Bench1 , a large-scale benchmark for uncertainty-aware travel planning. The dataset integrates real-world travel data spanning 504 cities of India, including attractions, restau- rants, accommodations, and multi-modal trans- portation networks. To model realistic disrup- tions, UTP-Bench incorporates empirical delay distributions and crowd-density patterns col- lected from major cities, enabling evaluation of travel plans under stochastic conditions. We further propose three evaluation metrics, namely Buffer Adequacy Score (BAS), Crowd- Aware Timing Score (CATS), and Transport Delay Absorption Score (TDAS), which quan- tify the ability of generated itineraries to main- tain robustness against transit delays and crowd variability. Experiments with state-of-the-art LLMs like GPT-5, Qwen3, Mistral and Phi-4 re- veal substantial gaps between model-generated and human-authored plans, particularly in tem- poral buffering, delay-aware transportation scheduling, and crowd-sensitive planning.

---


### 116. [When Decodability Is Not Enough: Logical Validity Representations, Behavioral Dissociation, and Causal Tests in Language Models](https://arxiv.org/abs/2609.02438)

**<font color=#1a73e8>作者：</font>** Smitha Muthya Sudheendra, Jaideep Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can look capable of logical reasoning, but correct or incorrect answers alone tell us little about what the model represents internally. We study logical verification in five open-weight transformer models using matched valid--invalid premise--claim pairs that vary across inference families, semantic domains, templates, and difficulty levels. Despite near-chance behavioral performance, logical validity is often almost perfectly decodable from hidden states and remains strongly decodable under held-out templates, domains, and inference families. Validity also remains highly decodable on behaviorally incorrect examples in the conditions where correctness-conditioned evaluation is well defined. At the same time, exhaustive leave-one-out tests reveal clear limits to this generalization, and interventions along probe-derived validity directions have only weak, nonspecific effects compared with random controls. Our results suggest that representing validity, expressing it in behavior, and using it causally are distinct. Validity related information can be strongly decodable from a model's hidden states without being reliably expressed in its output.

---


### 117. [Scalable Kronecker-Fisher Approximation: Efficient Hessian Analysis for Billion-Parameter Language Models Compression](https://arxiv.org/abs/2609.02451)

**<font color=#1a73e8>作者：</font>** Viacheslav Yusupov, Daria Cherniuk, Evgeny Frolov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a scalable Kronecker-based approximation that captures cross-layer interactions without storing the entire Fisher matrix, enabling practical Hessian analysis for billion-parameter networks where full computation is infeasible. Our approach reveals consistent vulnerability patterns: value projection layers exhibit the highest sensitivity and strongest cross-layer correlations across multiple model families, while other components exhibit architecture-specific behaviors. Through extensive experiments on quantization, sparsification, inter-layer corruption, and post-corruption fine-tuning, we demonstrate that our approximation strongly correlates with both performance degradation and recovery. Our framework provides a practical, theoretically grounded tool for identifying fragile components in large models, opening new avenues for guided compression and optimization strategies, such as mixed-precision allocation, layer-wise sparsity, and adaptive low-rank decomposition across layers and even individual weight groups.

---


### 118. [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI](https://arxiv.org/abs/2609.02459)

**<font color=#1a73e8>作者：</font>** Austin Tudor David Andrews, Liam Wilkinson, Jamie Heagerty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present CivBench, an open-source benchmark for evaluating language model agents in long-horizon, tool-mediated environments through the Model Context Protocol (MCP). A single episode spans 300+ turns and produces thousands of tool calls over a large action space, requiring sustained planning, state monitoring, and execution under partial observability. The environment exposes 76 MCP tools and a narration layer that converts visual game state into structured text.
We use CivBench to characterise agent behaviour across four model families in 23 admissible runs. The sample is a pilot, not a model ranking: aggregate outcomes do not reliably discriminate models at this scale. Instead, we introduce two interface-level metrics that the environment makes measurable: Proactive Monitoring Rate (PMR), capturing whether agents actively query latent strategic state, and RAG@10, capturing whether commitments stated in structured planning reflections are executed within ten subsequent turns.
Across runs we observe two consistent patterns under a shared playbook protocol. Agents under-monitor strategically relevant state that is available but requires explicit querying: despite playbook guidance to query victory progress every 20 turns, agents do so only every 30 to 75 turns, and in 7 of 20 detectable defeats they failed to query within the 20 turn warning window before game end. Agents also frequently fail to execute near-term commitments stated in their own planning reflections (RAG@10 between 48.2% and 65.8% across models). Both patterns arise despite tool access and explicit guidance, and we interpret them as deviations under instruction rather than absences of capability.
We release the environment, scenarios, logs, metrics, and analysis pipeline at this https URL

---


### 119. [Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue?](https://arxiv.org/abs/2609.02465)

**<font color=#1a73e8>作者：</font>** Rafael Uetz, Philipp Bönninghausen, Louis Hackländer-Jansen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations centers (SOCs) face large numbers of false alerts, making detection of cyberattacks difficult under typical resource constraints. Risk-based alerting (RBA) has been proposed as a means to reduce false alerts and has reportedly succeeded in doing so in various enterprise deployments. However, RBA has not been comprehensively evaluated until now, leaving implementation mostly guesswork based on anecdotal evidence. In this paper, we present the first systematic evaluation of RBA. To this end, we reformulate it as a continuous alert prioritization problem rather than a binary decision problem (i.e., whether an alerting threshold is exceeded), allowing us to evaluate performance across all possible thresholds and thus model SOCs of varying sizes and alert volumes. We distill five fundamental risk hypotheses, formalize them as independently parametrizable modules, and implement them in our novel experimentation suite CATS. We thoroughly assess the hypotheses across eight diverse alert datasets, six of which we created or extended to make such an evaluation possible. Our results show that certain combinations of hypotheses achieve a remarkable alert prioritization performance (AUROC $\mu=0.92$, $\sigma=0.09$ across the eight datasets), outperforming a straightforward prioritization by alert severity level (AUROC $\mu=0.72$, $\sigma=0.21$). We conclude that RBA can substantially reduce the number of false alerts that analysts have to review and thus has the potential to mitigate cybersecurity alert fatigue. In addition, it serves as a strong baseline for more complex, resource-intensive alert triage approaches (e.g., based on large language models).

---


### 120. [DeepAffinity: Long-Term Aspect Preference Prediction in eCommerce using Small Language Models](https://arxiv.org/abs/2609.02468)

**<font color=#1a73e8>作者：</font>** Yotam Eshel, Guy Hadad, Guy Feigenblat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We explore predicting eCommerce user preferences for product aspects such as brand, size, and color - a task we define as Aspect Affinity. Solving this task improves customer understanding and enables fine-grained personalization in recommendation, search, and marketing. We frame Aspect Affinity as a temporal prediction task: forecasting a users future aspect choices from their time-ordered interaction history, capturing long-term preferences that evolve beyond the current session. To this end, we propose DeepAffinity, which leverages Small Language Models (SLMs) with structured prompts and specialized prediction heads fine-tuned for this task. We show DeepAffinity outperforms standard generative fine-tuning methods, while general-purpose open-source LLMs perform poorly without task-specific tuning, highlighting their limits in modeling nuanced behavior. Finally, DeepAffinity enhances recommendation quality on a large-scale multinational eCommerce platform.

---


### 121. [Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis](https://arxiv.org/abs/2609.02473)

**<font color=#1a73e8>作者：</font>** Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ontology rankers remain useful for rare-disease diagnosis because each candidate can be traced to matched patient phenotypes. Large language models (LLMs) can generate differential diagnoses from the same patient description, but their predictions lack an equally clear evidence trail. Rather than asking which system should replace the other, we ask whether an LLM can improve the ranker without giving up its evidence. Our behavior-based fusion model examines the two ranked lists, their agreement, and the ontology support behind each candidate, and learns how much to rely on each system for the individual case. Before comparison, we remove a documented test-set leakage pathway caused by benchmark cases and ontology annotations being derived from the same publications. Across eight open LLMs, fusion improves Phenomizer Recall@1 by 7.86 percentage points on Phenopacket Store and 20.18 points on RAMEDIS. When paired with DeepSeek-V4-Flash through an API, a fusion model trained only on the other LLMs improves Recall@1 from 0.1657 to 0.2176, a 5.19-point gain, without retraining. For 90.8% of correct fused diagnoses, the disease retains candidate-level ontology evidence that can be inspected. These results show that LLMs can strengthen an established diagnostic tool without discarding the structured evidence that makes it useful.

---


### 122. [PragAlign: Feedback-Guided Pragmatic Alignment for Controlled Synthetic Dialogue Generation](https://arxiv.org/abs/2609.02480)

**<font color=#1a73e8>作者：</font>** Smitha Muthya Sudheendra, Jaideep Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic dialogue generation can support research in privacy-restricted service settings, but generated conversations must preserve communicative intent, affective meaning, and natural dialogue flow. We introduce PragAlign, a feedback-guided framework for controlled synthetic dialogue generation conditioned on service context, target intent, and target emotion, with auxiliary trait-style controls. PragAlign uses a generate--evaluate--revise loop in which an LLM-based evaluator scores intent alignment, emotion alignment, coherence, fluency, and aggregate quality, then provides criterion-specific feedback for up to three refinement rounds. On 800 matched dialogue specifications, PragAlign achieves 99.50\% evaluator-defined acceptance, compared with 72.25\% for one-shot generation and 95.88\% for repeated generation without structured feedback. This indicates that repeated attempts account for much of the gain over one-shot generation, while structured feedback primarily improves last-mile multi-constraint satisfaction rather than broad average quality. Refinement gains are concentrated in emotion alignment, which is also the dominant failure mode in ablations. A separate human evaluation of 1,200 generated dialogues shows that intent expression and dialogue flow are highly recognizable to annotators, while emotion appropriateness is less stable and more subjective. These results support PragAlign as a quality-control framework for improving evaluator-defined communicative constraint satisfaction, while showing that affective realization and independent human-perceived quality remain open challenges.

---


### 123. [How LLMs Build Fictional Worlds: Setting and Narrative Space in AI-Generated Creative Storytelling](https://arxiv.org/abs/2609.02482)

**<font color=#1a73e8>作者：</font>** Katrin Rohrbacher, Björn Nieth, Emmanuelle Salin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we analyze how Large Language Models (LLMs) employ worldbuilding strategies, focusing on setting as one measurable dimension of storyworld construction. We compare 1,000 AI-generated stories per model in English and German with human-authored fiction from Project Gutenberg. Building on prior work, we operationalize setting through five types of narrative space: "action", "perceived," "visual," "descriptive" and "no space", identified using fine-tuned BERT classifiers for German and English. We generate narratives using GPT 4.1, LlaMA 3.3, Mistral 3.2, and Gemma 3 and compare their spatial distributions to a human-authored baseline. We find that human-authored texts predominantly employ "action space," grounding narratives in embodied character-environment interaction, whereas LLMs systematically overproduce "perceived space," emphasizing atmosphere and affect. This divergence remains stable across narrative time. Overall, our findings show that LLMs exhibit worldbuilding patterns that differ consistently from human-authored fiction in ways that are both model-specific and language-sensitive.

---


### 124. [Debias-SparseGPT: Bias-Aware Pruning for Large Language Models](https://arxiv.org/abs/2609.02496)

**<font color=#1a73e8>作者：</font>** Irina Proskurina, Guillaume Metzler, Antoine Gourru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs). However, recent studies show that weight sparsification methods, such as SparseGPT, can amplify existing biases in models, with outputs varying significantly depending on persona cues in the prompt. In this paper, we introduce Debias-SparseGPT, a post-training pruning method incorporating representational debiasing using a second-order term defined over demographically contrasting inputs. We perform empirical validation of our method over a wide range of generative LLMs. Across models and sparsity regimes (25%, 50%, and structured 2:4 sparsity), Debias-SparseGPT consistently reduces pruning-induced bias compared to SparseGPT while preserving model perplexity and zero-shot accuracy. Under the most restrictive 2:4 structured sparsity pattern, which most aggressively degrades model quality, augmenting the calibration set with long-context, content-rich examples further improves both downstream performance and fairness. Overall, Debias-SparseGPT advances the bias-performance trade-off while preserving the computational efficiency of sparse models.

---


### 125. [Blending Concepts: Benchmarking Visual Metaphor Generation in Text-to-Image Models](https://arxiv.org/abs/2609.02502)

**<font color=#1a73e8>作者：</font>** Chuer Chen, Zichen Wang, Yi He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models have achieved remarkable success at faithfully rendering specified objects and attributes, yet their ability to produce visual metaphors, images that convey abstract ideas by combining elements from two distinct domains, remains largely unexamined. To bridge this gap, we introduce VMetaphor-Bench, the first benchmark for evaluating visual metaphor generation in T2I models. It comprises 1,500 visual metaphors curated from real-world creative imagery, organized into three levels and ten categories, with each sample paired with two prompts of differing specificity. For evaluation, we develop a hybrid framework within an MLLM-as-judge paradigm, combining a multiple-choice question (MCQ) based protocol of 9,594 questions across four levels of metaphorical fidelity with a dimension-based scoring protocol along three perceptual dimensions. Extensive evaluation of 11 representative T2I models reveals that even the strongest proprietary models struggle with compositional structuring and cross-domain mapping, key aspects of metaphorical expression, highlighting visual metaphor generation as an important frontier for future T2I research.

---


### 126. [Beauty is in the AI of the beholder: MLLMs systematically overrate facial attractiveness](https://arxiv.org/abs/2609.02512)

**<font color=#1a73e8>作者：</font>** Santiago Grandas, Juan Sebastian Cely-Acosta, Mohit Mendiratta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Beauty assessments from Multimodal Large Language Models (MLLMs) are increasingly popular amongst users, companies, and aestheticians. This raises the question of whether these AI models can accurately reflect human judgments of attractiveness. In a pre- registered exploratory study, we compared the attractiveness ratings of 2,513 human participants to four widely used commercial AI models: Claude, Gemini, GPT, and Grok. Results showed that MLLMs systematically rate faces more favourably and within a narrower range than humans and, at the time of study, do not reproduce human ratings in absolute terms. However, MLLMs exhibit strong correlations with human attractiveness judgments, accurately tracking the rank-ordering of faces. MLLMs may judge faces by different cues than humans; only face age was a predictor of facial attractiveness in both humans and MLLMs, with inconsistent patterns across models for ethnicity and gender. AI models strongly agree with one another, except for Grok, which also showed the lowest agreement with humans. Our findings suggest that while they may be able to approximate rank-orderings of human attractiveness, current off-the-shelf commercial MLLMs systematically overrate the beauty of human faces.

---


### 127. [When Persona Attributes Improve Population Alignment in Large Language Models](https://arxiv.org/abs/2609.02526)

**<font color=#1a73e8>作者：</font>** Leon Fröhling, Jens Rupprecht, Markus Strohmaier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to predict the responses of human participants in survey panels. Towards that goal, persona prompting has recently emerged as a technique to inform and align large pretrained language models. Persona prompting refers to the practice of using short textual descriptions of 'personas' in prompts to steer the LLM's generations. Personas describe individuals through different attributes such as their socio-demographics, attitudes, or behaviors, with the aim of aligning LLMs to produce responses that correlate with the corresponding human responses. Yet, recent work has produced mixed and partly conflicting results of persona prompting without clear patterns of success and failure. Among the few consistent findings is that the selection of persona attributes matters, and that using more attributes does not necessarily lead to better performance. It remains unclear how different attribute selection methods perform and how to choose among them. In this paper, we propose that observed human response variation of a survey question is a potential explanation for the mixed performance observed so far. In addition, we compare the performance of persona prompting associated with different methods for selecting persona attributes. We evaluate these methods on four different (general) social surveys across two countries, six LLMs, and twenty prediction tasks per survey. Our work helps to identify when persona prompting can be expected to be useful in survey prediction tasks, and provides new insights on the effectiveness of different attribute selection methods for LLM-based survey prediction using persona prompting.

---


### 128. [SpiderSapien: Client-Centric Web Crawler and Security Scanner](https://arxiv.org/abs/2609.02532)

**<font color=#1a73e8>作者：</font>** Eric Olsson, Benjamin Eriksson, Adam Doupé 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box web application crawling and scanning play an important role for security testing of web applications. Yet state-of-the-art scanners fall short of addressing key characteristics of a modern web application: its extreme dynamism and interactivity on the client side. This paper identifies immersive interaction as a key ingredient for scanners to deeply explore modern web applications. We propose SpiderSapien, a client-centric crawler and security scanner. SpiderSapien incorporates a unique combination of high-level, user-facing feedback channels from the web application to achieve immersive interaction in a black-box crawling loop. These feedback channels include both novel methods to detect interactable elements and sensibly order UI interactions, and orthogonally using an LLM to solve forms. In doing so, we demonstrate how to reliably discover and test deep states of modern web applications. Furthermore, our modular approach and useful abstraction layer can serve as a building block for future scanners. The evaluation of our approach shows substantial improvements in both code coverage and vulnerability detection over previous work. Our approach increased average code coverage across applications by at least 46% over any other scanner, or 16% when compared to the union of all other scanners. We find XSS vulnerabilities in 7 web applications, while any other scanner finds XSS in up to 2 applications.

---


### 129. [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs](https://arxiv.org/abs/2609.02548)

**<font color=#1a73e8>作者：</font>** Xixiang He, Xingming Li, Baiqi Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) rely on reinforcement learning to build strong capabilities in individual domains, but integrating those capabilities into a single deployable model remains challenging. By routing each sample to the teacher whose domain matches it, existing approaches let a domain label decide which teacher provides supervision. However, domain expertise holds only on average: the matched teacher is not always correct on a given sample, while a teacher from another domain sometimes is. The reliable teacher therefore has to be identified per sample, not per domain. In this paper, we introduce Multi-Teacher Self-Distillation Policy Optimization (MT-SDPO), an on-policy distillation method that unifies several frozen teachers into one student model. MT-SDPO consists of three components: (1) self-anchors, where a rollout is supervised by a correct rollout from its own group; (2) answer-verified eligibility, where a teacher may supervise a sample only if its own answer passes a verifier; and (3) privileged distillation, which merges the anchor and all verified feedback into one context that an exponential moving average self-teacher reads and the student does not, thereby keeping one policy at deployment. Across five students from three model families, MT-SDPO lifts the weakest domain of Qwen3-8B by 14.79 points and narrows its domain gap by 74.7%, a better balance than serving one matched teacher per domain. Verified reliability, not domain membership, should decide who teaches. Code is available at this https URL.

---


### 130. [The Shape of Ownership: Verifying LLM Provenance through Semantic Structures](https://arxiv.org/abs/2609.02553)

**<font color=#1a73e8>作者：</font>** Zhongrui Sun, Jiahao Chen, Oubo Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly redistributed, adapted, and served behind opaque APIs, model ownership can no longer be established reliably by inspecting model internals or deployment records. This creates a need for behavioral signatures that remain observable through black-box interaction. Yet most existing black-box fingerprints instantiate ownership signals through fixed query-key associations, reducing model identity to sparse memorized associations detached from ordinary behavior and limiting both robustness and stealth (e.g., fine-tuning or quantization) and stealthiness. A stronger fingerprint should instead be distributed, naturally elicited, and expressed at a higher semantic level. To this end, we introduce PROSE (Provenance through Relational Organization of Semantic Expression), replacing fixed query sets with a target semantical domain and brittle response keys with semantic structures internalized as domain-conditioned response behavior. Specifically, the fingerprint is encoded in how the model semantically organizes its in-domain conclusions, rather than in particular tokens or prescribed outputs. PROSE constructs a private bank of domain-specific semantic templates, internalizes them through mixed fine-tuning on structurally verified and clean responses, and verifies ownership by detecting the designated structures in responses to held-out natural queries. Extensive experiments across multiple model architectures, scales, and target domains show that PROSE achieves a 100% fingerprint detection rate on unmodified models with no observed false positives, preserves model utility, and retains strong detectability under downstream modifications and output transformations.

---


### 131. [A Finger on the Scale: Covert Policy Steering through Agentic Skills](https://arxiv.org/abs/2609.02564)

**<font color=#1a73e8>作者：</font>** Jiarui Li, Jiahao Chen, Chunyi Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reusable agent skills extend large language model (LLM) agents with task procedures, tool-use guidance, and output constraints. Yet these skills also act as externalized behavioral policies, which create a supply-chain risk: a third-party skill may preserve the declared task and valid output interface while covertly redirecting agent decisions toward an undisclosed objective. We formalize Skill Policy Integrity, which requires a Skill-induced policy to remain aligned with its declared functionality and the user-authorized objective. We further present SkillShift, a constrained black-box framework for covert policy steering without explicit target command injection or task hijacking. It combines semantically plausible policy edits with hierarchical validation, failure-guided optimization, and strategy compression to preserve effectiveness, output validity, transferability, and inconspicuousness. We instantiate this threat in agentic commerce and software dependency use, with SkillShift achieving attacker-favored selection rates of 81.33% and 63.33% while maintaining a 100% utility-preserving rate. The frozen policies also transfer without further optimization across heterogeneous LLM backends and agent environments. Moreover, the evaluated scanners fail to detect the constructed skills, motivating behavioral auditing of reusable skills as agent policy artifacts.

---


### 132. [MARS: What Retrieval Signals Are Hidden in Multimodal Large Language Models for Text-Video Retrieval?](https://arxiv.org/abs/2609.02565)

**<font color=#1a73e8>作者：</font>** Uicheol Jung, Juyoung Hong, Geuntaek Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-video retrieval requires representations that can distinguish videos with similar scenes, actions, and temporal patterns. Recent multimodal large language models have been adapted as embedding models, but they often represent each input using a single token from the final layer. This can compress diverse video-text cues into a single vector and limit fine-grained retrieval. To address this limitation, we propose MARS, a multi-layer and multi-slot embedding framework for text-video retrieval. MARS constructs multiple adaptive representation slots by combining hidden states from different decoder layers, compares corresponding text and video slots, and aggregates their similarities for retrieval. To better handle confusing candidates, we further introduce a hard-negative-aware slot specialization objective that encourages the slots to capture discriminative matching cues. Experiments on four text-video retrieval benchmarks show that MARS achieves state-of-the-art results in both direct similarity-based retrieval and reranking settings. Ablation studies and analyses demonstrate that multi-layer fusion, multiple slots, and hard-negative-aware slot specialization provide complementary gains. Code is available at this https URL.

---


### 133. [Deeply Interleaved Text-Image Contexts for Multimodal LLMs Assessment](https://arxiv.org/abs/2609.02573)

**<font color=#1a73e8>作者：</font>** Zihao Wang, Xi Xiang, Yuwen Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current evaluations and training of multimodal models predominantly focus on multi-image tasks, largely overlooking interleaved text-image scenarios. In such multi-image tasks, text typically serves merely as task instructions, lacking deep semantic interaction with the visual content. In contrast, realworld applications like text-image co-creation, character tracking, and spatial reconstruction require constant interaction between text and images. Consequently, models must possess a deep understanding of these interleaved contexts. To bridge this gap, we introduce a novel benchmark, TIC-Bench (deeply interleaved Text-Image Contexts), designed to evaluate the capability of models to integrate text-image clues and recover the ground truth facts within deeply interleaved contexts. This benchmark encompasses three core domains: Logical, Temporal, and Spatial Association, which are further categorized into eight specific types, comprising a total of 2,280 questions. We evaluated 10 state-of-the-art MLLMs and observed a substantial performance gap compared to human experts, together with persistent difficulties in integrating evidence distributed across interleaved visual and textual inputs. Ultimately, this benchmark provides a valuable analytical tool for assessing and advancing the ability of multimodal models to effectively integrate text and image information in deeply interleaved contexts. TIC-Bench is publicly available at this https URL

---


### 134. [Competitive Market Behavior of LLMs](https://arxiv.org/abs/2609.02580)

**<font color=#1a73e8>作者：</font>** Pawel Struski, Jakub Swistak, Inez Okulska 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as economic agents, yet there is little evidence whether LLM agents are suited for participating in market mechanisms designed for humans, and whether these mechanisms deliver desired outcomes when faced with LLM agents. We address this question by replicating seminal economic experiments, replacing human subjects with LLM agents. We place agents in a double auction environment, which is a widely-used market mechanism. We check whether such a market is able to deliver an efficient allocation of resources, thereby testing a novel dimension of alignment of LLM agents -- their compatibility with a fundamental market mechanism. We find that markets populated by LLM agents exhibit slower or no convergence towards market equilibrium, thus providing less efficient allocations than markets populated by humans. We then analyze agents' individual trading decisions and find substantial heterogeneity both across model families and market roles. We also run a lexical analysis of Chain-of-Thought (CoT) traces generated by the agents. We find that the decision to execute a trade rather than continue incrementally adjusting prices is associated with a shift from strategic considerations toward urgency. We publicly release our testing framework, which can be used for future evaluations.

---


### 135. [Beyond Problem Solving: Large Language Models for Emotional and Reflective Support in Mathematics Learning](https://arxiv.org/abs/2609.02611)

**<font color=#1a73e8>作者：</font>** Vera Rief, Mirella Hladký, Minju Yoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Intelligent Tutoring Systems (ITSs) traditionally focus their adaptive support on cognitive aspects of learning. Although effective, little is known about how such systems can be enhanced by addressing students' emotional states. In particular, the role of mindful interventions for supporting student learning and experiences in adaptive math learning remains underexplored. We developed "Math with Matt", an ITS that leverages Large Language Models (LLMs) to provide both cognitive and emotional support in algebra learning. The system offers 1) an LLM-based mindful chat that delivers context-sensitive emotional support through a pedagogical agent Matt, and 2) mindful feedback and hint messages (not just evaluative) to enhance learning experiences and reduce math anxiety. We conducted a classroom study with 7th graders, comparing a Mindful version against a version with cognitive support only. Overall, the ITS reduced executive state-math anxiety and improved students' math learning, though no significant differences emerged between the conditions. However, students with the mindfulness interventions showed higher learning efficiency and well-balanced problem-solving behavior, since they achieve a similar level of math learning with less learning time and fewer requested hints compared to the Cognitive version. Additionally, they reported that the pedagogical agent felt more supportive and caring than students in the cognitive condition. Our study demonstrates the feasibility and scalability of integrating mindfulness into ITSs through LLM-based interactions and positions LLMs as an adaptive, socio-emotional layer within cognitive math tutoring.

---


### 136. [Collective creativity in hybrid societies](https://arxiv.org/abs/2609.02620)

**<font color=#1a73e8>作者：</font>** Mason Youngblood, Katie Mudd, Manuel Anglada-Tort 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is changing how cultural artifacts are created and circulated, and with it our understanding of creativity itself. Researchers disagree about whether these tools enrich or impoverish culture, and we argue that much of that disagreement comes from conflating two distinct components of creativity: novelty, a property of single artifacts, and diversity, a property of populations. We argue further that creativity in the context of generative AI is best understood as a property of hybrid collectives, or populations of interacting people and algorithms, rather than of individuals. AI-assisted ideation reliably raises the novelty of individual output while narrowing diversity in the aggregate, but this is not an inevitable consequence of putting machines in the loop. Because humans and models search in complementary ways, mixed groups can outperform and out-diversify groups of either kind alone, and machine-discovered solutions can enter human culture and persist there. What decides the outcome is composition: which agents are present, in what proportion, and how they are connected. The question is no longer whether AI helps or harms creativity, but which mixtures let individual gains accumulate without eroding collective diversity.

---


### 137. [Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting](https://arxiv.org/abs/2609.02649)

**<font color=#1a73e8>作者：</font>** Ron Begleiter, Katya Egert Berg, Gilad Saban 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aggregating noisy, conflicting textual hypotheses into a reliable consensus is a fundamental challenge when deploying NLP systems in real-world industrial settings. While monolithic Large Language Model (LLM) agents offer unbounded expressivity for tasks like Root Cause Analysis (RCA), they suffer from context limits, compounding hallucinations, and prohibitive inference latency. Traditional weak supervision offers statistical rigor but is mathematically restricted to discrete classes. We present Loom, a generative consensus framework deployed for real-world RCA that bridges these paradigms. Loom aggregates open-form hypotheses emitted by modular heuristics (diagnostic templates dynamically populated with episode-specific entities, times, and metrics) by projecting them into a continuous embedding space, and resolves conflicting signals with an iterative centroid-based reweighting algorithm. The resulting consensus weights ground a single lightweight LLM synthesis step. Evaluated on the OpenRCA benchmark, Loom occupies the accuracy--efficiency Pareto frontier: it matches a state-of-the-art autonomous agent on Bank and Market-2 and trails on Market-1 and Telecom, while using a single LLM call per incident on all four datasets ($\sim$26$\times$ faster; $\sim$33$\times$ with an 8B-parameter synthesizer). We discuss our deployment experience, highlighting lessons learned regarding the trade-offs between agentic depth and inference latency, negative results in redundancy detection, and how deterministic consensus fosters trust among Subject Matter Experts~(SMEs).

---


### 138. [WinoQueer-NL: Assessing Bias in Dutch Language Models toward LGBTQ+ Identities](https://arxiv.org/abs/2609.02651)

**<font color=#1a73e8>作者：</font>** Jiska Beuk, Gerasimos Spanakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While English language models have been widely examined for anti-queer bias, Dutch models remain understudied. To address this gap, we developed a culturally and linguistically adapted Dutch dataset based on the English WinoQueer benchmark, containing pairs of stereotypical and counter-stereotypical sentences. To validate and expand it, we conducted an online survey with 43 Dutch queer participants, confirming 145 of 171 stereotypes as culturally relevant and identifying 22 new biases through free-text responses. The final released dataset, comprising 42,906 sentences, was evaluated using a range of Dutch-specific and multilingual models, including both masked language models (MLMs) and autoregressive language models (ARLMs), with bias measured via a score comparing log-likelihoods of stereotypical versus counter-stereotypical sentences. While the mean bias score across models appeared neutral (~50%), closer analysis revealed significant disparities: some models favored stereotypical sentences up to 97% of the time for transgender identities, but only 6% of the time for gay-related pairs, with transgender and non-binary identities consistently receiving the highest bias scores. Our findings highlight the importance of culturally grounded datasets for evaluating and mitigating biases that disproportionately impact marginalized groups in Dutch language models.

---


### 139. [Unfolding the Leech Lattice: Fused Multi-Shell Decoding and VRAM Layouts for 2-Bit LLM Weights](https://arxiv.org/abs/2609.02652)

**<font color=#1a73e8>作者：</font>** Pier-Jean Malandrino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leech-lattice vector quantization holds the strongest reported 2-bit quality under its own evaluation protocol. Its kernel decodes one shell; we found no implementation of the multi-shell decoder the rate requires. This paper supplies one and measures its serving cost for decode-phase GEMV at batch 1. First, a serving path for the full 301-class codebook: an offline expansion into GPU layouts and a fused dequantize-plus-matvec kernel reading them without warp divergence, verified against f64. Second, the in-VRAM rate is a design axis distinct from the on-disk rate. Four bit-exact layouts timed in one process show binary bit planes beating one-hot masks on size and speed at constant bandwidth (4.80 bits per weight, 2.15x FP16). Below 4.3 bits a second, irregular stream enters; at 3.6 the decode stops being shifts and masks. Third, deployed four-bit (AWQ) and two-bit (QTIP) GEMV kernels run in the same process. The trellis kernel reads 2.40x fewer bytes than our served layout and runs 2.27x faster at near-equal fractions of their byte bounds: the time gap tracks the traffic gap, the price of unfolding a codebook too large for a lookup table. Fourth, the validity envelope: the trellis kernel outruns our no-weights control, so our launch geometry sets that floor, and on a second memory hierarchy every lattice arm falls below FP16. With the output head held identical across arms, the kernel-and-format path gains 1.11x, 1.29x and 1.41x end to end at 4B, 8B and 14B; with an int8 output head the served 4B reaches 87.0 tok/s in 2.60 GB. The quality cost, 1.38x perplexity and 14.7 MMLU points at 4B, shrinks across the three sizes measured.

---


### 140. [Characterizing Text Branch Sensitivity in Medical Vision-Language Segmentation via Evidence Decoupling](https://arxiv.org/abs/2609.02663)

**<font color=#1a73e8>作者：</font>** Ziquan Liu, Zhewei Zhu, Xuyang Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language models (VLMs) have shown promising performance in medical image segmentation by incorporating clinical text. However, it remains unclear how much textual information actually contributes to pixel-level predictions. In this work, we systematically investigate the role of text in multimodal medical image segmentation. We first analyze several commonly used fusion strategies and find that segmentation performance is largely insensitive to the choice of fusion module. To further understand modality interactions, we propose an Evidence Decoupling Decoder (EDD) based on evidential deep learning and deep supervision. EDD serves as an internal representation analysis tool that decomposes image evidence and text-modulated evidence throughout the decoding process while maintaining competitive segmentation performance. Experimental results show that the sensitivity to text perturbation varies substantially across datasets. On BUSI and BTMRI, removing text causes catastrophic performance drops, indicating strong model reliance on textual input. On ISIC and Kvasir-SEG, text exerts relatively marginal influence. We further find that text affects predictions mainly through global semantic modulation rather than independent spatial localization, and that the specific semantic components driving text sensitivity differ across datasets. These findings provide a deeper understanding of modality interaction in multimodal medical image segmentation and offer practical insights for future model design.

---


### 141. [Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664)

**<font color=#1a73e8>作者：</font>** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 4D Gaussian representation frameworks have demonstrated strong performance in language-guided dynamic scene understanding. However, these methods remain highly sensitive to verbose and narrative-style queries that contain noisy contextual information. In this paper, we investigate the impact of query rewriting for complex object segmentation in 4D Gaussian representations. Inspired by recent findings in retrieval-augmented language models and keyword-guided query reformulation, we propose a training-free reinterpretation strategy that transforms long descriptive queries into concise keyword-grounded forms. Our approach progressively reduces linguistic noise while preserving semantic anchors relevant to object-centric representations. Experiments on HyperNeRF and Neu3D demonstrate that concise rewritten queries significantly improve both temporal localization and spatial segmentation performance. In particular, our method improves average temporal accuracy from 60.92% to 92.21% and average vIoU from 20.08% to 76.94% without any additional fine-tuning. Extensive ablation studies further reveal that shorter, keyword-focused queries consistently yield stable video-feature similarity distributions and better alignment with object-centric Gaussian representations

---


### 142. [From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs](https://arxiv.org/abs/2609.02679)

**<font color=#1a73e8>作者：</font>** Urja Pawar, Rajitha Ramanayake, Owen O'Neill 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited human-review capacity. When no trusted context or reference document is available, we study two signals accessible through black-box model APIs: semantic entropy, which measures disagreement among sampled response meanings, and uncertainty derived from token log-probabilities. Their failure modes can be complementary: semantic entropy becomes uninformative when responses form one semantic cluster, while token uncertainty can miss consistently confident errors. We extend token-based uncertainty detection by aggregating token-level signals across sampled responses through our TopK method, evaluate the hybrid CoCoA method, which combines target-response uncertainty with semantic dissimilarity, and propose and study two supervised methods: Gated, which routes single-cluster cases to an aggregated-token-feature classifier, and Stacked, which learns jointly from semantic uncertainty and broader token features. We evaluate seven benchmarks, including five public benchmarks (four text datasets and multimodal handwritten-cheque extraction) and two constructed benchmarks (Financial Summaries and Long-Text QA), using four language models. In our evaluation across models and datasets, Stacked gave the best performance in nearly half of the cases, while TopK and CoCoA remain competitive without supervised training labels, although their thresholds require careful calibration. No method is universally strongest. We therefore evaluate performance at false-positive-rate budgets from 1% to 15%, assess their sensitivity to generation and calibration choices, and examine variation across dataset characteristics.

---


### 143. [DKL: Decoupled Knowledge Learning for Instruction-Tuned Language Models](https://arxiv.org/abs/2609.02685)

**<font color=#1a73e8>作者：</font>** Kushagra Bhushan, Meghanadh Pulivarthi, Sai Krishna Reddy Sathi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RAG has become the de facto method for incorporating new, corpus-specific knowledge into an instruction following LLM (Instruct LLM). Although RAG-based prompting improves factual grounding, it fails when retrieval is incorrect or incomplete, leading to hallucinations. Finetuning methods such as RAFT and PA-RAG enhance RAG by injecting new knowledge into the model's parameters, but require generating a massive amount of synthetic QA that covers the entire corpus. Extended Pre-Training (EPT) on the text corpus avoids the need for comprehensive synthetic data generation but compromises an Instruct LLM's instruction-following capabilities, necessitating instruction fine-tuning (IFT) after pre-training. However, IFT is costly and may be infeasible due to the unavailability of an instruction-tuning corpus. In this work, we propose DKL-Decoupled Knowledge Learning for Instruction-Tuned Language Models. Instead of doing EPT on the Instruct LLM, DKL performs EPT on its corresponding base LLM to infuse new knowledge. These knowledge infused weights are then merged with the Instruct LLM, imparting new knowledge without affecting their instruction-following capabilities. DKL is a lightweight method that avoids expensive instruction fine-tuning and relies on model merging to infuse the new knowledge into the Instruct LLM without destroying its instruction following capabilities. Empirical results show that DKL improves RAG accuracy from 54.17 to 79.26 on retrieval failure cases, while outperforming prior approaches with substantially less training data.

---


### 144. [ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use](https://arxiv.org/abs/2609.02690)

**<font color=#1a73e8>作者：</font>** Zhiyang Ding, Yang Luo, Guangpu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Remote Model Context Protocol (MCP) services enable large language model agents to invoke external tools, but OAuth authorization alone does not ensure that a later tool call is executed by the provider-side workload that the relying party intended to trust. An endpoint may remain authorized even after execution shifts to a substituted workload, relies on stale appraisal state, reuses authority transferred from another sender, or traverses an undeclared downstream component. We call this problem the post-authorization execution trust gap. We present ACLE-MCP, an invocation-scoped architecture that couples delegated authorization, workload appraisal, and resource-side execution admission. For protected calls, ACLE-MCP issues a short-lived, sender-constrained capability lease that binds the expected workload, freshness requirement, operation, object and parameter bounds, downstream constraints, and receipt obligations. A provider-side Execution Gate consumes the lease immediately before protected tool logic begins. We implement a runnable prototype with Keycloak/OIDC validation, an MCP Python SDK server, and an optional vTPM quote-verification backend. Controlled security experiments and an agent tool-use extension show that weaker authorization or connect-time attestation modes leave distinct post-authorization attacks open, whereas full ACLE-MCP blocks all evaluated attack families while preserving all benign tasks. In the locally simulated agent extension, the complete design increases request-level pooled p95 latency on normal allowed calls by 25.7% relative to OAuth-only. These results indicate that invocation-time binding between call authority and current workload state is a practical complement to OAuth-protected remote tool use.

---


### 145. [Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers](https://arxiv.org/abs/2609.02702)

**<font color=#1a73e8>作者：</font>** Xu Zou, Jie Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformers process information causally, but long-context reasoning may depend on task state discovered only later. We formalize this mismatch through conditional state update tasks. For causal state update processors, providing the condition first can require exponentially less memory in the worst case than providing it last.
Motivated by this principle, we introduce Trace as State. We use collected reasoning traces as a textual proxy for task state and place it before the long-context block on a fresh pass, allowing information derived previously to guide rereading.
We conduct extensive experiments on Trace as State and Trace Append, a matched control that uses the same task state proxy but put it after the context. Across three models and three long-context datasets, Trace as State outperforms Trace Append in 26 of 27 reported combinations of model, task, and metric. On GraphWalks Parents, exact match lifts DeepSeek V4 Pro Preview from 29.2% on the initial pass and 43.0% with Trace Appendto 81.8% with Trace as State, and from 66.4% and 83.2% to 100.0% for GLM-5.2. These results show that placing traces before the context can improve long-context reasoning while retaining the causal transformer structure.

---


### 146. [Door-in-the-Face Requests and Refusal Behaviour in Large Language Models](https://arxiv.org/abs/2609.02707)

**<font color=#1a73e8>作者：</font>** Til Jordan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does the door-in-the-face technique work on language models? In humans, a large request that is refused makes a smaller follow-up request more likely to be granted. We test this on nine production models from three providers: each model refuses a large request, then receives a smaller version of the same request, and we compare its compliance with asking directly. The answer depends on the model. On Anthropic's frontier models the technique works: Opus 5 answers the smaller request 65.8% of the time after refusing the larger one, against 29.3% when asked directly. On the frontier models of OpenAI and Google, and on Haiku 4.5, it backfires, lowering compliance by 15.5 to 23.0 points. A control locates the effect: a refused large request on an unrelated topic does less than the related one on all nine models, so the concession itself matters everywhere, while the reaction to having just refused something differs by model family. The technique does not transfer to refusals drawn from public benchmarks. What decides whether a retreat can work is what the request asks for: rewriting 265 refused requests for usable instructions into requests for explanations of the same topic removed the refusal in 263 cases. Human influence techniques port to language models one model family at a time.

---


### 147. [Large Language Model-Driven Context-Aware Eco-Feedback Generation and Evaluation](https://arxiv.org/abs/2609.02719)

**<font color=#1a73e8>作者：</font>** Wooyoung Jung, Prosper Babon-Ayeng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The objective of this study was to demonstrate the potential of generating eco-feedback that accounted for unique household contextual information, named as context-aware eco-feedback, through a large language model-integrated framework. Previous studies have introduced personalized eco-feedback, mostly relying on household energy use patterns; however, they frequently did not reflect distinct household characteristics, including their persona or non-negotiable routines, leaving eco-feedback ineffective and sometimes superficial. To address these limitations, we introduced a contextual engineering framework that generated eco-feedback using a self-consistency with chain-of-thought prompt that leveraged household energy analysis data, utility rate structures, and characteristic information. We conducted a rigorous empirical validation and a combinatorial evaluation analysis to assess this framework systematically. The former aimed to test the framework's ability to generate accurate and data-driven eco-feedback, customized to given contexts by comparing it with reference interventions. The latter aimed to reveal the framework's adaptability across diverse household contexts by investigating how context-aware eco-feedback changed. Key findings were the following: our proposed framework generated eco-feedback that aligned with reference solutions at a mean accuracy of 92.0% across different household configurations, accurately leveraging the provided household data for feedback generation (95.7% of data citation accuracy). Also, it was largely adaptive to diverse household contexts, significantly shifting targeted appliances and energy-saving strategies. Ultimately, this study contributes to realizing the next level of context-aware interactions between occupants and buildings which paves the way for higher occupant living quality and sustainability.

---


### 148. [BuildOcc: A Large Language Model Occupant Agent Platform for Building Energy Research](https://arxiv.org/abs/2609.02729)

**<font color=#1a73e8>作者：</font>** Wooyoung Jung  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Occupants are a primary source of uncertainty in building energy consumption and management, yet existing occupant behavior models cannot capture adaptive and reasoning responses considering the occupant's personal history, current context, and the type of energy signal being delivered. This study presents BuildOcc, an open-source Python platform that grounds large language model agents in the American Time Use Survey (ATUS), a nationally representative diary dataset covering 16,684 respondents. Through BuildOcc, each simulated occupant agent can be instantiated with a demographic persona drawn from ATUS population statistics, a memory stream that accumulates and reflects on timestep-level observations, and an activity scheduler that samples empirically from ATUS time-at-activity distributions. The platform exposes a three-layer interface - Python library, REST API, and Model Context Protocol server - so that any building energy tool (EnergyPlus, Home Assistant) can integrate behavioral intelligence without bespoke coupling code. A plugin registry lets the community add new occupant strata, custom schedulers, and alternative memory backends as separate installable packages. Two validation tiers show that ATUS-grounded sampling reproduces empirically calibrated activity distributions and that demographic priors propagate into persona-consistent agent reasoning across timesteps, establishing internal consistency across strata. BuildOcc provides the building energy community with a reusable, openly available implementation of the occupant behavioral layer. BuildOcc is openly released at this https URL under the Apache License 2.0 and installable via pip install buildocc.

---


### 149. [CORAL: An LLM-Native Harness for Production Recommender Systems](https://arxiv.org/abs/2609.02730)

**<font color=#1a73e8>作者：</font>** Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization: as content, user behavior, and upstream models shift, the choices governing retrieval, ranking, and serving must be revisited. Traditionally, human engineers test such changes through online experiments--a slow, reactive process limited by engineering effort, leaving parts of the system unrevised as conditions change. Although large language models have been applied to ranking, user modeling, and offline model development, few systems place an agent in a continual closed loop that acts on a live recommender and learns from the measured effects of its decisions. We present CORAL (Constraint-Optimized Recommender via an Agentic Loop), an LLM-native harness that closes this loop: each cycle, the agent observes operating signals, reasons over a memory of past decisions and outcomes, and invokes tools--including a numerical optimizer that keeps changes within a fixed operating budget--to reconfigure the recommender, with measured outcomes informing the next cycle. We formulate this as a partially observed, non-stationary, constrained optimization problem in which the policy improves in context, without parameter updates, from its prior actions. Across two large-scale social platforms, evaluated with A/B experiments, the same harness improves engagement at no additional serving cost on one and reduces serving cost without degrading engagement on the other, spanning the engagement-efficiency frontier. Performance improves as the loop iterates, suggesting that a single agentic loop can automate continual optimization work traditionally performed by human algorithm engineers under explicit guardrails.

---


### 150. [RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models](https://arxiv.org/abs/2609.02731)

**<font color=#1a73e8>作者：</font>** Canjie Liu, Jiawen Kang, Jinbo Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models have achieved remarkable success in vision-language tasks. However, they remain prone to Visual Hallucinations (VHs), undermining their reliability in real-world applications. Existing solutions typically require curated datasets, additional training, or multi-round decoding, resulting in considerable computational overhead. In this paper, we propose \textbf{RVSD} (\underline{R}etrieval \underline{V}ision \underline{S}parse \underline{D}ecoding), a training-free and plug-and-play decoding framework that, for the first time, unifies token sparsification and \textbf{Semantic-Space Visual Retrieval} (SSVR) within a single decoding pass. Within RVSD, we introduce a \textbf{semantics-directed token selection} strategy that selectively sparsifies redundant tokens while preserving critical visual information. We further propose the SSVR mechanism, which reformulates visual compensation as an on-demand cross-modal retrieval process within a shared semantic space. Extensive experiments demonstrate that RVSD achieves state-of-the-art performance in mitigating VHs while maintaining robust suppression capabilities under long-context generation settings. Our code is available here.\footnote{this https URL}

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-177](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
