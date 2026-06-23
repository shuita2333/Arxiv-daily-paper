# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 451. [READ More than What You See: Reinforcement Learning for Accurate and Coherent Audio Description Generations](https://arxiv.org/abs/2606.22766)

**<font color=#1a73e8>作者：</font>** Bo Fang, Xinyao Zhang, Yuxin Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio Description aims to generate concise narrations of essential visual content in audio-visual media for blind and low-vision audiences. Existing methods either rely on prompting off-the-shelf multimodal models, which often mismatch AD style, or partially optimize training-based systems with next-token prediction, which under-explores model capacity and biases generation toward generic expressions. We present READ, the first reinforcement-learning (RL) framework for training-based AD generation. READ formulates AD as sequence-level optimization with reference-matching, length, and format rewards, and further introduces a dedicated coherence reward under context-aware supervision to promote narratively coherent descriptions. Experiments on MAD-Eval, CMD-AD, and TV-AD show that READ substantially outperforms prior methods across diverse evaluation metrics. Our results highlight RL as a promising paradigm for accurate and coherent AD generation. Our codes, models, and benchmark results will be publicly available.

---


### 452. [Factored Gossip DiLoCo: Reducing Blocking Communication in DiLoCo](https://arxiv.org/abs/2606.22768)

**<font color=#1a73e8>作者：</font>** Chamin Hewa Koneputugodage, Thalaiyasingam Ajanthan, Sameera Ramasinghe 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To make large-scale distributed training practical outside high-bandwidth datacenters, we must reduce blocking, high-volume synchronization. While DiLoCo communicates infrequently, its outer synchronization remains bandwidth-heavy and brittle to stragglers and transient failures. We relax exact synchronization to approximate synchronization via mixing/gossip, which degrades gracefully under delays and communication failures. This allows us to factorize DiLoCo synchronization into a non-blocking mixing step that overlaps computation with no staleness, and a blocking mixing step that tightens worker agreement, yielding a tunable trade-off between compute utilization and optimization stability. On up to billion-parameter language models in low-bandwidth settings, our framework substantially improves compute utilization compared to DiLoCo, with training progress ranging from comparable to closely matching it, and is more robust to failures.

---


### 453. [Noise is Signal: Density-Based Outliers as Leading Indicators of Occupational Emergence in Labor Market Text](https://arxiv.org/abs/2606.22769)

**<font color=#1a73e8>作者：</font>** Shreyash Rawat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard NLP pipelines for occupational clustering discard the 10-15% of job postings that density-based methods assign to noise. We argue this is an error: in rapidly evolving domains, low posting density signals novelty, not incoherence. We formalize this as the Emergence-Density Inversion (EDI) hypothesis and test it longitudinally on 84,988 job postings across eight quarters (Q4 2022-Q3 2024). EDI is partially confirmed: high-EOS outlier groups transition to stable clusters in 1.4 +/- 0.6 quarters vs. 4.1 +/- 1.2 for low-EOS groups (p < 0.001), though the signal fails in approximately 19% of cases, which we characterize as a failure analysis. We extend the Emerging Occupation Score (EOS) with Temporal Velocity and Cross-Platform Convergence, improving 2-quarter cluster-formation prediction from F1 = 0.61 to 0.74, outperforming Isolation Forest, LOF, GLOSH, and BERTrend baselines. A retrospective study on three now-established roles (MLOps Engineer, DevOps/SRE, Data Engineer) confirms EOS signalled 2-3 quarters before cluster formation, providing held-out validation. A held-out annotator panel (kappa = 0.74) rates EOS > 0.75 as coherent emerging occupations with 77% precision. Prompt Engineer, AI Safety Researcher, Foundation Model Engineer, and Agent Systems Engineer, all absent from O*NET, are top-4 in Q3 2024 and form stable clusters by Q1 2025.

---


### 454. [Statistical Matching via Schrödinger Bridge beyond Conditional Independence](https://arxiv.org/abs/2606.22770)

**<font color=#1a73e8>作者：</font>** Eunho Koo, Tongseok Lim, Jinwon Sohn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical matching combines partially overlapping datasets that share covariates $X$ but observe the target $Y$ and auxiliary variables $Z$ separately. Classical approaches typically invoke the conditional independence assumption (CIA), which makes the problem identifiable but fundamentally implies that the imported auxiliary variable provides no additional predictive power for $Y$ once $X$ is known. To capture this latent $Y$--$Z$ dependence, we propose a novel dependency-aware Schrödinger bridge for predictive statistical matching. Our approach couples the two separated databases by tilting the conservative CIA baseline with a transportation-based compatibility cost, recovering an informative joint distribution. The resulting statistical learning framework yields full probabilistic posterior rules for bidirectional imputation. Theoretically, we establish a sufficient condition under which the learned bridge strictly improves over the CIA baseline, alongside an exact joint recovery guarantee in the Gaussian setting under an appropriate cost. Across synthetic benchmarks and real-world datasets (CelebA and Adult), we demonstrate that our dependency-aware completion consistently improves downstream predictive utility, proving especially beneficial in settings like data recoding where the underlying population exhibits strong $Y$--$Z$ dependence.

---


### 455. [Learning Moral Diversity: Modelling Individual Perspectives in Moral Classification of Texts](https://arxiv.org/abs/2606.22771)

**<font color=#1a73e8>作者：</font>** Yi Ren, Lewis Mitchell, Matthew Roughan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding moral values in social media text offers insight into moral judgement formation, and supervised NLP models trained on crowdsourced data have achieved strong classification performance. However, most approaches simplify the problem by aggregating multiple annotators' labels into a single "ground truth", overlooking the inherent subjectivity of the task. In practice, there are disagreements between annotators caused by personal viewpoint or inherent ambiguities, particularly for short tweets. Here, we extend a pretrained language model with a layer that learns annotator-specific features. Our model improves predictions of individual annotations and yields representations that reveal meaningful insights into annotators' moral perspectives. We show that models trained on aggregated labels may hide variation and give a misleading impression of performance. Overall, we demonstrate that disagreement reflects the inherent subjectivity of the task and that modelling individual perspectives creates benefits for moral classification of texts.

---


### 456. [LoCC: Detection and Localization of Lip-Syncing Deepfakes via Counterfactual Frame Consistency](https://arxiv.org/abs/2606.22772)

**<font color=#1a73e8>作者：</font>** Soumyya Kanti Datta, Shan Jia, Siwei Lyu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lip-syncing deepfakes are among the most challenging forms of manipulated media because their artifacts are localized almost exclusively to the mouth region and evolve dynamically over time. Detecting such deepfakes requires precise temporal and spatial modeling of lip motion. In this paper, we propose LoCC, a novel detection framework that performs fine-grained detection and localization of lip-syncing deepfakes at both segment and frame levels. Unlike prior approaches that analyze videos holistically, our method evaluates whether each frame aligns with a counterfactual estimate generated from its temporal neighbors. Real videos exhibit strong and stable consistency, whereas lip-sync deepfakes introduce localized inconsistencies. Following a teacher-student learning paradigm, our model effectively captures these frame-level discrepancies and achieves superior performance over state-of-the-art methods on multiple benchmark lip-syncing deepfake datasets, including LAV-DF, AVDF1M, FakeAVCeleb, and KODF, and generalizes well across compression levels and datasets.

---


### 457. [GeoRouteNet: Geometry-Enhanced Non-Autoregressive Neural Solver for the Traveling Salesman Problem](https://arxiv.org/abs/2606.22776)

**<font color=#1a73e8>作者：</font>** Xiang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The traveling salesman problem (TSP) is a canonical NP-hard combinatorial optimization benchmark that tests the representational capacity and generalization of neural solvers. While non-autoregressive (NAR) approaches offer parallel inference, they often lack sufficient geometric inductive bias and stable training signals, leading to degraded performance under cross-scale and cross-distribution shifts. We propose GeoRouteNet, a geometry-enhanced NAR neural solver for Euclidean TSP. On the model side, GeoRouteNet incorporates centered node features, learnable radial distance basis functions, distance-aware graph attention with explicit edge messaging, LayerNorm-SwiGLU feed-forward blocks, and cross-layer attentive residual mixing. On the training side, we design multi-candidate self-comparison reinforcement learning (MCS-RL), which samples multiple candidate tours per instance, constructs adaptive baselines from greedy and peer candidates, and adds winner-candidate guidance with annealed entropy regularization. On 10,000 random TSP50 instances, GeoRouteNet achieves a 0.32% optimality gap under Beam-1000 decoding. On TSP100, the gap is 1.26%. On 27 stratified TSPLIB EUC_2D instances, the overall gap drops from 17.12% (NAR4TSP reproduction) to 3.60%, while batch inference throughput substantially exceeds that of Concorde and LKH3. Ablation studies confirm that geometric structure enhancement and multi-candidate training are complementary: structure improvements dominate cross-distribution gains, while MCS-RL further stabilizes solution quality when paired with a strong geometric encoder.

---


### 458. [DE-FIVE: Detecting Malicious Image Prompts via Fourier Features and Image Vector Embeddings](https://arxiv.org/abs/2606.22779)

**<font color=#1a73e8>作者：</font>** Xingwei Zhong, Varun Sharma, Kar Wai Fok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) employ both visual and textual modalities to enable advanced vision-language inference. However, incorporating visual modalities expands the attack surface of VLMs, making them more susceptible to security threats such as adversarial perturbations and indirect prompt injection, wherein crafted malicious image prompts can elicit unintended model outputs. Existing defense methods against malicious image prompts remain insufficient as they typically demand extensive datasets for retraining or the deployment of additional, complex classifiers. Most critically, there is a profound lack of specialized defense mechanisms specifically targeting indirect prompt injections, a gap that serves as a primary motivation for this work. To address these limitations, we introduce DE-FIVE, a novel training-free framework for detecting malicious image prompts by leveraging Fourier features and the hidden state representations of the visual encoder (image vector embeddings) across perturbations. Specifically, we develop a hybrid detection strategy consisting of a black-box detector that operates on Fourier-domain features and a white-box detector that exploits image vector embeddings derived from only a few-shot malicious set. Extensive experiments demonstrate that the proposed framework consistently outperforms state-of-the-art baselines against malicious image prompts.

---


### 459. [Towards Robust Personalized Federated Learning: Vulnerability Assessment and Defense Co-Design](https://arxiv.org/abs/2606.22782)

**<font color=#1a73e8>作者：</font>** Mingyuan Fan, Cen Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The proliferation of IoT devices has fueled distributed edge systems to collect vast amounts of sensitive data, creating fertile ground for on-device machine learning applications. While federated learning (FL) mitigates privacy concerns by exchanging model parameters instead of raw data, we identify a critical blind spot in current research. We examine the most commonly used personalized federated learning (PFL) methods, which allow clients to maintain private, personalized models to address data heterogeneity across clients. Through systematic analysis, we reveal that PFL methods exhibit heightened vulnerability to transfer-based adversarial attacks compared to centralized learning paradigms. Wherein, malicious clients can exploit local model knowledge to craft adversarial examples that can compromise peer clients' personalized models. We establish this vulnerability through both theoretical analysis and empirical evaluation across multiple benchmark datasets, demonstrating significant accuracy drops across various PFL methods. To address this challenge, we propose a defense framework combining stochastic input noise, input-scaled trace regularization, and parameter sensitivity maximization to improve FL's robustness. Our findings establish the first systematic study of adversarial threats in PFL systems, providing both diagnostic tools and practical countermeasures.

---


### 460. [Learning Filters with Certainty](https://arxiv.org/abs/2606.22786)

**<font color=#1a73e8>作者：</font>** Yuval Banoun, Daniel Sadoc Menasche, Ori Rottenstreich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hash-based data structures such as Bloom filters are widely used in network systems for tasks including caching, anomaly detection, and machine learning pipelines. They typically provide binary indications of whether an element belongs to a set of interest, e.g., the contents of a cache. When uncertainty arises due to hash collisions, a positive indication is returned to avoid false negatives. We argue that the certainty associated with such indications can itself be useful information. This work focuses on Counting Bloom Filters (CBFs), a Bloom-filter variant that maintains counters rather than bits. Besides supporting insertions and deletions, these counters provide additional information that can be used to estimate the certainty of positive membership indications. We show how this certainty signal can be exploited in architectures that combine Bloom Filters with machine learning (ML) models.

---


### 461. [Visual Geometry Transformer in the Wild: Distractor-Free 3D Reconstruction](https://arxiv.org/abs/2606.22787)

**<font color=#1a73e8>作者：</font>** Tianbo Pan, Xingyi Yang, Shizun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current end-to-end multi-view 3D reconstruction methods achieve impressive results, but rely on a restrictive static assumption: the scenes is entire distractor-free with perfect cross-view geometry. This reliance on idealized inputs causes even the most advanced methods to fail in real-world settings, where transient distractors and occlusions present. To address this, we propose Visual Geometry Transformer in the Wild (VGTW), an end-to-end framework for robust reconstruction from inconsistent views. At its core, we isolate and suppress distractor-affected regions while preserving the consistent components across views. Specifically, we introduce a Distractor-aware Training (DAT) strategy that separates clean features from distractor-contaminated ones in the attention mechanism while enforcing feature consistency across images. To enable this, we train the model with an auxiliary mask prediction head, using supervision from a new dataset we collected with pixel-level distractor masks. The resulting VGTW model is a feed-forward network that directly outputs clean, distractor-free point clouds. Remarkably, it requires no additional 3D supervision, remains computationally efficient, and is compatible with existing pipelines. Extensive experiments validate our approach, demonstrating state-of-the-art performance and robust generalization in diverse, real-world scenarios.

---


### 462. [A Formula-Driven Survey and Research Agenda for On-Policy Distillation](https://arxiv.org/abs/2606.22793)

**<font color=#1a73e8>作者：</font>** Bowen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains an LLM on states induced by the current or recent student policy: the student generates complete or partial rollouts, a teacher or self-teacher scores the resulting tokens under their generated contexts, and dense log-probability, logit, or distributional signals are converted into post-training updates. This survey studies OPD as a feedback-to-update problem rather than a single loss family. We develop a formula-driven taxonomy from two routes -- direct distributional losses and policy-gradient-style log-ratio updates -- and use it to organize core methods, verifier- or outcome-guided hybrids, industrial reports, framework implementations, failure modes, and stabilization recipes under explicit evidence boundaries. The taxonomy shows that OPD effectiveness depends not only on KL direction or teacher access, but also on state compatibility, support construction, temporal credit, vocabulary-level probability routing, gates and weights, and regularization. We further separate two mechanisms often conflated in sampled-token OPD stability discussions. Temporal credit asks how teacher-student log-ratio returns should weight sampled actions across a rollout; vocabulary routing asks where probability mass should move when negative feedback suppresses a sampled token. This distinction yields bias boundaries for immediate, return-to-go, discounted, and baseline-corrected estimators, motivates GAE-OPD as a value-based hypothesis for log-ratio returns, and motivates Counterfactual Routed OPD (CR-OPD) for routing probability mass toward teacher-supported, student-reachable alternatives. We close by mapping actionability diagnostics, failure mechanisms, case studies, open problems, and a reporting checklist onto the same feedback-to-update variables.

---


### 463. [Machine-knittable, Magnetically-Plug-n-Play E-Textile Prototyping](https://arxiv.org/abs/2606.22800)

**<font color=#1a73e8>作者：</font>** Yifan Li, Ryo Takahashi, Wakako Yukita 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electronic textiles (e-textiles) integrated with wearable sensors are essential for daily motion monitoring and long-term physiological sensing. For example, capturing optimal kinematic or bio-signals requires aligning sensors with specific anatomical parts, which vary significantly across individuals and application scenarios. This necessity for personalization makes e-textile prototyping inherently iterative, however current fabrication methods, such as manual conductive stitching, rely on permanent bonds that restrict rapid adjustment. This paper introduces Plug-n-play e-knit, a machine-knittable e-textile prototyping platform that enables repeatable, quick adjustment of sensor positions across garments. First, to cover the large area of the textile for prototyping, we use industrial digital knitting of conductive yarn to integrate power and communication buses directly into the large-scale textile. Then, to ensure plug-n-play attachment to the textile, we employ soft-magnetic connectors that enable sensors to be repeatedly plugged into the wiring without damaging the fabric. Furthermore, our LED-positioning system enables the automatic identification and localization of each sensor node. We demonstrate the platform's capabilities through forearm movement calibration and position-aware temperature mapping.

---


### 464. [Learning Adaptive Dynamical Features via Multi-$τ$ Liquid-Mamba for All-in-one Image Restoration](https://arxiv.org/abs/2606.22801)

**<font color=#1a73e8>作者：</font>** Hu Gao, Changshuo Wang, Yulong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration aims to recover high-quality images from degraded observations. Recent Mamba-based image restoration models have demonstrated strong potential in modeling long-range dependencies with linear complexity. However, most existing designs still rely on a single state-evolution timescale, which limits their adaptability to spatially heterogeneous and task-dependent degradation patterns in all-in-one image restoration. In this paper, we propose Multi-$\tau$ Liquid-Mamba, an adaptive state space module that introduces input-conditioned multi-timescale liquid discretization into selective state space modeling. Instead of changing the overall selective scan pipeline, the proposed module modulates the effective discretization steps of multiple dynamical branches and adaptively fuses their responses according to degradation-aware gating weights. This design allows the model to capture both fast-varying local details and slowly evolving global structures while preserving the linear scaling property of Mamba with respect to sequence length. Importantly, Multi-$\tau$ Liquid-Mamba modulates the effective transition dynamics while preserving the original selective parameterization and hardware-efficient selective scan mechanism, making it a plug-and-play module that can be seamlessly integrated into existing Mamba-based architectures. Built upon this framework, we develop a Multi-$\tau$ Liquid-Mamba Image Restoration Network (MLMIR) for all-in-one image restoration. Extensive experiments on a wide range of restoration benchmarks demonstrate that MLMIR consistently achieves state-of-the-art performance in all-in-one image restoration while remaining highly competitive in task-aligned restoration settings.

---


### 465. [CoVStream: Edge-Cloud Collaboration for Understanding of Long Video Streams](https://arxiv.org/abs/2606.22804)

**<font color=#1a73e8>作者：</font>** Xu Liu, Guikun Chen, Zihao Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long, continuous video streams are an increasingly critical driver of multimedia intelligence. Existing efforts often handle long videos with a sample-encode-reason approach using large models. However, they overlook a crucial deployment fact: the stream is often produced by computationally constrained devices. This forces an untenable compromise: cloud offloading unlocks strong reasoning but incurs prohibitive bandwidth overhead, while on-device processing remains limited by edge hardware capacity. Therefore, we propose CoVStream, the first edge-cloud collaborative framework for understanding long video streams. The edge node distills raw video streams into compact visual features and semantic captions for transmission to the cloud, minimizing bandwidth costs, while the cloud server integrates this data into an entity graph and global visual context, activating the heavy reasoning model only when a user query arrives. Experiments on VideoMME-Long, LVBench, and RTV-Bench show that CoVStream reduces bandwidth usage by 87.6% while retaining 99.2% of the cloud baseline accuracy on LVBench.

---


### 466. [Policy-as-Data: Learning Generalizable HOI Diffusion Models from Simulated Physics](https://arxiv.org/abs/2606.22806)

**<font color=#1a73e8>作者：</font>** Shujia Li, Jianshu Hu, Haiyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing realistic Human-Object Interactions (HOI) is critical for creating embodied avatars and functional virtual environments. However, current data-driven approaches primarily rely on motion capture datasets, which are expensive to scale and limited in functional diversity. Models trained with these datasets fail to generalize to unseen objects and maintain physical consistency over long horizons. In this paper, we propose a novel framework that leverages a physics simulator to overcome the data-scarcity bottleneck in HOI generation. Specifically, we propose a scalable pipeline, called \ours, which leverages policies trained with reinforcement learning in a physics simulator for task-oriented data generation and trains a generative model on the augmented dataset for generalizable HOI generation. To seamlessly utilize the synthetic data, we introduce a coarse-to-fine retargeting process that bridges the representation gap between the simplified model used in physics simulator and the standard parametric body models required for generative training. Validated through comprehensive experiments, our method demonstrates enhanced generalization to unseen objects and the capability of long-horizon generation, while exhibiting greater dynamic diversity and physical plausibility.

---


### 467. [KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking](https://arxiv.org/abs/2606.22807)

**<font color=#1a73e8>作者：</font>** Xinping Zhao, Jiaxin Xu, Ziqi Dai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As retrieval systems scale, high-quality reranking becomes increasingly important. However, most existing rerankers, whether encoder-based or decoder-based, jointly encode the query and passage, tightly coupling their computation and limiting deployment efficiency as well as flexibility. We present KaLM-Reranker-V1, a fast but not late-interaction (FBNL) reranker that decouples query and passage computation while retaining expressive relevance modeling. Built on an encoder-decoder architecture, KaLM-Reranker-V1 uses the encoder to pre-encode passages with Matryoshka embedding pooling, while the decoder models the system instruction, user instruction, and query intent; cross-attention then captures relevance between the query context and passage representations. This design makes KaLM-Reranker-V1 efficient through decoupled passage encoding, yet not late interaction, by preserving rich relevance modeling through cross-attention. We instantiate KaLM-Reranker-V1 in three sizes, Nano, Small, and Large, with 0.27B, 1B, and 4B activated parameters, respectively. Extensive experiments on BEIR, MIRACL, and LMEB demonstrate that KaLM-Reranker-V1 achieves strong reranking performance with superior efficiency. On BEIR, KaLM-Reranker-V1 achieves state-of-the-art performance, on par with strong industrial models such as the Qwen3-Reranker series; on MIRACL, despite not being extensively trained on multilingual data, KaLM-Reranker-V1 still shows excellent reranking performance. Moreover, on LMEB, reranking models demonstrate a clear advantage, with even the 0.27B Nano model remaining competitive with 7-12B embedding models.

---


### 468. [AI-Assisted Help-Seeking Trajectories in Programming Education from an SRL-Informed Perspective](https://arxiv.org/abs/2606.22809)

**<font color=#1a73e8>作者：</font>** Boxuan Ma, Huiyong Li, Gen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI tools provide novice programmers with instant, personalized support, but also raise concerns about whether AI use supports or bypasses students' regulation of problem-solving. Existing work has largely focused on correctness, usability, or overall usage frequency, with less attention to how student--AI help-seeking unfolds. This study addresses this gap by analyzing AI-assisted help-seeking trajectories in university-level programming. Using an SRL-informed analytical framework that links prompt-level help-seeking codes to conceptual, implementation, debugging, and reflective forms of support, we analyzed 1,290 task-specific student prompts linked to 17,190 code submissions from 71 students in introductory Python programming courses. Specifically, we examined how help-seeking interactions were structured across turns and attempts, and how trajectory patterns related to task scores and the number of code submissions. Results indicate that many students primarily used AI for reactive troubleshooting rather than for planned, self-regulated problem-solving. Although trajectory patterns were not associated with significant differences in task scores, they differed substantially in the number of code submissions required. These findings suggest that the educational significance of AI support lies not only in whether students use AI, but in how their help-seeking trajectories develop during programming problem-solving.

---


### 469. [Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis](https://arxiv.org/abs/2606.22811)

**<font color=#1a73e8>作者：</font>** Jinchuan Tian, Haoran Wang, Siddhant Arora 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classical TTS systems typically rely on rigid input formats and predefined metadata slots, limiting their ability to fulfill flexible user requirements. This paper introduces Bagpiper-TTS, a universal speech synthesis system that deals with diverse natural language user requests. Given a natural language prompt, Bagpiper-TTS first reasons over the users' intent to derive a rich caption, i.e., a comprehensive textual blueprint encompassing both transcription and nuanced metadata. Subsequently, this caption guides the synthesis of the target speech. Our model inherently supports a broad spectrum of tasks besides classical TTS applications, including multi-talker, intent-to-speech, role-play synthesis, singing voice synthesis, and more. Experimental results demonstrate that Bagpiper-TTS achieves an 1.7% Word Error Rate (WER) on the Seed-TTS-Eval benchmark and match the performance of dedicated models in both LLM-as-a-judge and human subjective evaluations across multiple applications.

---


### 470. [Active Inference as the Test-Time Scaling Law for Physical AI Agents](https://arxiv.org/abs/2606.22813)

**<font color=#1a73e8>作者：</font>** Omar Hashash, Christo Kurisummoottil Thomas, Walid Saad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, a novel test-time scaling law for physical artificial intelligence (AI) agents is introduced. This scaling law enables physical AI agents to reason with their world models to generalize in unforeseen scenarios at test time. The derived scaling law is grounded in the first principle of active inference, which equips agents with the general objective to survive in the real world, under which their specific task objectives are subsumed. Active inference achieves this by providing the reasoning to resolve prediction errors that arise when the agent encounters unforeseen situations outside its training distribution, enabling generalization in non-stationary environments. The proposed scaling law captures this by dynamically updating the agent's policy with this reasoning at test time. This policy update is modeled as a soft Bayesian inference process in which beliefs about the policy are updated using the reasoning that reduces expected prediction errors under allowable policies as a likelihood. The resulting posterior policy admits a biological interpretation, recovering the scaling mechanism that engages the brain's basal ganglia and prefrontal cortex at test time. To solve this analytically intractable problem, a variational inference solution minimizing free energy bounds is developed. This solution extends to enable learning beyond training by reinforcing new instances, resolved at test time, in both the policy and world model. Unlike existing scaling laws constrained by model size and training data, the derived solution scales with the continuous real-world experience of a physical AI agent. Simulation results on an autonomous driving task demonstrate that the proposed solution outperforms model-free Q-learning and model-based Bayesian reinforcement learning, achieving robust generalization to unforeseen scenarios while improving inference efficiency by over 36%.

---


### 471. [SelPE: Progressive Selection for Private Structured Text Synthesis](https://arxiv.org/abs/2606.22817)

**<font color=#1a73e8>作者：</font>** Xuancheng Zhu, Guoshun Nan, Han Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many data-driven applications rely on structured textual records, such as clinical triage notes and financial transaction logs, for downstream learning and decision-making. In privacy-sensitive domains, access to such records is strictly regulated, often resulting in only a small number of available private examples for model development and analysis. Yet existing differential privacy data synthesis methods fall short: tabular techniques cannot faithfully model free-form text, while text-based approaches often break structural constraints. We propose SelPE, a selection-guided progressive evolution framework for small-sample private structured text synthesis. Rather than relying on noisy aggregation or private model training, SelPE concentrates privacy budget on a sequence of multi-batch top-1 selections, enabling efficient guidance under tight privacy constraints. To support faithful and valid synthesis, SelPE decouples semantic abstraction from schema realization via a two-stage generation pipeline, and evaluates candidates using a multi-channel distance kernel that jointly models textual, categorical, and numeric fields in their native representations. A non-private contrastive expansion mechanism further promotes diversity without incurring additional privacy cost. Extensive Experiments demonstrate that SelPE consistently improves structural validity, fidelity, and downstream utility under strict differential privacy budgets, particularly in low-data regimes.

---


### 472. [BranchShine: Compact Raw-Audio-to-IPA Transcription with a RoPE E-Branchformer Encoder](https://arxiv.org/abs/2606.22824)

**<font color=#1a73e8>作者：</font>** Nikhil Navas, Sergio Chevtchenko, Talisson Damiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech-to-IPA transcription is useful when the desired output is pronunciation rather than orthographic text, but competitive multilingual systems are often large and evaluation is sensitive to normalization choices. This paper presents BranchShine, a 33M-parameter raw-audio CTC recognizer with a lightweight convolutional front end and a 19-block RoPE E-Branchformer encoder. We find that BranchShine provides a compact and competitive operating point for IPA transcription under matched normalization and scoring. On a 16,660-utterance multilingual test set covering 41 language labels, BranchShine obtains 9.19% whitespace-insensitive IPA character error rate, compared with 9.78% for the 575.00M-parameter PhoneticXEUS baseline. A secondary child speech reading analysis shows a complementary operating profile: BranchShine is more conservative on incorrect readings, while Whisper-Medium is stronger on exact acceptance of correct readings. Overall, the results indicate that a compact raw-audio-to-IPA model can approach much larger baselines on character-level IPA transcription.

---


### 473. [What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security](https://arxiv.org/abs/2606.22827)

**<font color=#1a73e8>作者：</font>** Hala Alia, Andrew Case, Irfan Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern software development relies heavily on third-party components from public repositories, expanding the software supply chain attack surface. In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. However, SBOMs built from metadata or filesystem artifacts fail to capture the components loaded and executed at runtime, especially in dynamic ecosystems such as Python. Moreover, generating runtime SBOMs through instrumentation requires monitoring to be deployed in advance and the system to remain observable throughout execution. Such conditions are difficult to satisfy in production environments and incident-response scenarios. Volatile memory, in contrast, provides a reliable source for recovering the actual runtime state of a running application without requiring prior instrumentation. Therefore, this paper presents MEM-SBOM, the first memory forensics framework that generates SBOMs directly from the runtime state of Python applications. It recovers the modules from the interpreter's internal structures, resolves package versions, and analyzes bytecode to build dependency graphs and identify vulnerable functions. We implemented MEM-SBOM as a suite of Volatility 3 plugins and evaluated it against 51 real-world Python applications. It achieves 100% extraction accuracy, identifies Streamlit as the only application that calls the vulnerable routines of the tornado dependency, and recovers all runtime packages missed by existing SBOM tools, providing more accurate dependency graphs and better vulnerability assessment. These capabilities make MEM-SBOM a practical foundation for software supply chain security and incident response by providing a forensically sound runtime view of what is executed on a system.

---


### 474. [DBT-Bleed: Dual-Branch Temporal Modeling with Key-Frame Selection for Surgical Bleeding Detection](https://arxiv.org/abs/2606.22829)

**<font color=#1a73e8>作者：</font>** Sudhanshu Mishra, Jialang Xu, Jensen Ang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intraoperative Adverse Events (IAEs) detection is critical for improving surgical safety, with bleeding being among the most frequent events across many surgery types. Existing methods struggle to distinguish bleeding IAE from visually similar residual blood due to limited temporal reasoning. Moreover, modeling long surgical videos while preserving fine-grained temporal dynamics remains computationally challenging. We propose DBT-Bleed, a dual-branch multi-scale temporal modeling framework disentangling bleeding and normal representations using layer-wise temporal adapters for short- and long-term bleeding progression. To efficiently process long surgical videos without sacrificing fine-grained temporal information, we introduce HiRED, a Hierarchical Entropy-Driven frame selection strategy that retains temporally informative segments while removing redundancy. Experiments on the MultiBypass dataset demonstrate gains of 6.53% in F1, 5.62% in Recall and 9% in MCC values for bleeding IAE detection, consistently outperforming video-level baselines. Additionally, we evaluate cross-procedure generalization on a newly curated dataset from a different surgical procedure type, where DBT-Bleed demonstrates robust transferability by achieving gain of 6% in F1 and 8% in MCC under zero-shot setting. To support this evaluation, we introduce EndoPit-IAE, an Endonasal Pituitary Surgery dataset annotated for IAEs, representing the first IAE-annotated dataset in neurosurgery. Code will be made publicly available upon acceptance.

---


### 475. [Finding the Evidence: Discovering Decision-Supporting Tokens for On-Policy Reasoning Distillation](https://arxiv.org/abs/2606.22830)

**<font color=#1a73e8>作者：</font>** Jinwei Xiao, Zhuowen Han, Yueqing Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation transfers reasoning ability through dense token-level supervision, yet the nature of the transferable signal remains unclear. We discover that reasoning chains contain two types of knowledge that require different discovery mechanisms: decisions (where to branch), which surface through student uncertainty, and evidence (intermediate steps that justify decisions), which hides in positions where the student is confident yet wrong. Current methods capture only decisions; the substantive knowledge in evidence tokens remains untransferred. We propose DEAR(Decision-Evidence Aware Reasoning Distillation), which first identifies decisions via student entropy, then discovers their supporting evidence through hidden-state cosine similarity to decision anchors, boosted by teacher-student divergence to prioritize the largest knowledge gaps. Across three student-teacher configurations on math and code benchmarks, DEAR consistently outperforms standard OPD, with up to +2.5pp on competition math and +5.7pp on code generation.

---


### 476. [Homographic Navigation: Geometry-Driven Camera Guidance for Deterministic Planar Capture](https://arxiv.org/abs/2606.22834)

**<font color=#1a73e8>作者：</font>** Dominik Kroupa, Marek Vaško, Muh Yuzril Ihza Baharuddin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present homographic navigation, a geometry-centric framework for guiding camera acquisition toward precise capture of planar regions. Rather than treating homography as an output, we use it as an organizing variable that unifies learning, alignment, and evaluation. From a single annotated reference image, we generate unlimited synthetic training data via homographic augmentation and train a single-shot model for joint recognition and localization of multiple artifacts (physical objects with a rectangular planar target) through sparse keypoint prediction. To address precision under limited model input resolution, we introduce a two-pass inference scheme with global detection followed by localized refinement, and a Stable Warp training strategy that significantly improves accuracy, particularly in the high-precision regime. The model also predicts confidence estimates per predicted keypoint and per the whole sample. Experimental results demonstrate that accurate planar alignment can be achieved from minimal supervision, providing a foundation for geometry-driven camera guidance and future learning from in-the-wild video data.

---


### 477. [OrthoMotion:Disentangling Camera and Subject Motion via Geometry Semantics Orthogonal Attention](https://arxiv.org/abs/2606.22835)

**<font color=#1a73e8>作者：</font>** Zijie Meng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable video generation demands independent command of the camera and the subject, yet 2D conditioning entangles them: camera- and object-induced optical flow share the same inverse-depth (1/Z) scaling and cannot be separated from image evidence alone. We first prove that this entanglement is representational, not architectural -- the 2D camera/object split is a non-identifiable inverse problem -- and therefore reframe decoupling as a question of operator design. We resolve it at the level of the attention operator. OrthoMotion routes camera motion into a geometric channel, a norm-preserving rotation of the rotary position embedding (RoPE) phase, and subject motion into a semantic channel, a gated value injection in cross-attention. Because these sub-operators are algebraically complementary -- a rotation versus a translation of the affine action on tokens -- a lightweight decoupling regularizer provably drives their response subspaces to orthogonality, so the two controls stop interfering. To our knowledge OrthoMotion is the first method to guarantee disentanglement by construction rather than hope for it to emerge. It attains state-of-the-art camera and subject accuracy at once while minimizing cross-talk, which we quantify with a new Cross-Talk Error (CTE) metric, cutting cross-talk by more than 2.4x with no loss in fidelity and generalizing across backbones.

---


### 478. [CLIP-guided Diffusion Model for Backdoor Generation in Sensor-based Human Activity Recognition](https://arxiv.org/abs/2606.22837)

**<font color=#1a73e8>作者：</font>** Toby Briston, Illya Kosyk, Kuniyih S  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensors are critical components of modern intelligent devices. The proliferation of the Internet of Things (IoT) and wearable mobile devices has enabled the integration of such sensors to monitor the environment and enable users to take predictive actions. Human activity recognition (HAR) is a popular application in which Inertial Measurement Unit (IMU)-based sensors, such as accelerometers and gyroscopes, are used to provide insights into health, training, and medical diagnosis. However, the accuracy of such a model is hindered by the lack of data. The diffusion model-based technique has proven successful in generating synthetic data for training HAR models. In this paper, we propose a backdoor training technique, IMU-DM-CLIP, that leverages a diffusion model to enable trigger-based attacks on HAR models. Our empirical analysis shows that the attack is successful even with a very small backdoor injection rate of 10\% and 10\% of the data guided for the diffusion model.

---


### 479. [G-MASt3R-SfM: Graph-based View Pruning and Multi-stage Optimization for Robust SfM](https://arxiv.org/abs/2606.22856)

**<font color=#1a73e8>作者：</font>** Toshiki Watanabe, Shintaro Ito, Natsuki Takama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structure from Motion (SfM) is essential for multi-view 3D reconstruction, however, its accuracy heavily relies on the accuracy of image matching. While the recent correspondence matching method, MASt3R, enables robust matching even under challenging conditions, it tends to generate incorrect correspondences for non-overlapping image pairs. Consequently, existing SfM methods using MASt3R, such as MASt3R-SfM, suffer from significant degradation in pose estimation accuracy as they incorporate these unreliable matches directly into optimization. To address this issue, we propose G-MASt3R-SfM, a novel SfM pipeline that enhances robustness through two key modules. First, the Graph-based View Pruning (GVP) module constructs a scene graph from matching confidence and geometrically prunes outlier views. Second, the Multi-Stage Optimization (MSO) module progressively refines camera parameters by expanding the optimization scope from local consistency to the global consistency. Experiments on the ETH3D dataset demonstrate that our method achieves state-of-the-art accuracy in both camera pose estimation and 3D reconstruction, effectively suppressing noise caused by outliers.

---


### 480. [The Unseen Hand: Manipulating Model Fairness and SHAP with Targeted Identity Re-Association Attacks](https://arxiv.org/abs/2606.22858)

**<font color=#1a73e8>作者：</font>** Sannaan Khan, Muhammad U. S. Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As machine learning models grow more influential and opaque, algorithmic fairness and explainability are critical for ensuring accountability. However, we demonstrate that these auditing mechanisms are themselves vulnerable to subtle manipulation, camouflaging the influence of protected features. While prior work on data-agnostic attacks has exposed this vulnerability, they leave behind detectable artifacts that compromise their stealth. We introduce Targeted Identity Re-Association (TIRA) attacks, a novel family of attacks that iteratively and probabilistically manipulate a model's outputs without requiring access to the model's internals or feature representations. We formalize two algorithms: Probabilistic Micro-Shuffling (PMiS), which applies localized adjacent swaps, and Probabilistic Rank-Shift Micro-Perturbation (PRSMP), which introduces small, randomized rank shifts. We empirically demonstrate that TIRA attacks are highly effective at pushing fairness metrics towards ideal values. Crucially, TIRA attacks successfully confound SHAP-based explanations, leaving effectively zero residual attribution for protected features, a major improvement over prior work.

---


### 481. [AI Scientists as Engines of Discovery: A Case for Development within Reformed Institutions](https://arxiv.org/abs/2606.22859)

**<font color=#1a73e8>作者：</font>** Raul Jimenez, Boris Bolliet, Francisco Villaescusa-Navarro 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence (AI) systems are beginning to assist, accelerate, and partially automate scientific discovery, performing tasks that span literature synthesis, code generation, data analysis, hypothesis proposal, and model criticism. We argue that this transition is qualitative rather than incremental, and that suitably designed multi-agent systems may evolve from passive computational tools into ``AI scientists'' that can expand the hypothesis-generating and verification capacity of science. Such systems must be developed and deployed within a scientific ecosystem fit for purpose: institutions must be redesigned for verification, accountability, interpretability, and dual-use safety. We sketch how multi-agent architectures, illustrated by the prototype framework \textit{Denario}, accelerate the discovery cycle and traverse model spaces beyond human reach; examine what this implies for authorship, peer review, and the enduring role of human scientists; and close with recommendations for governing AI as an epistemic actor rather than a mere instrument.

---


### 482. [Chains That See, Answers That Don't: A Multi-Aspect Evaluation Recipe for Forced Chain-of-Thought on Video-MME](https://arxiv.org/abs/2606.22862)

**<font color=#1a73e8>作者：</font>** Zhichao Fan, Yanhang Li, Zexin Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forced chain-of-thought (CoT) is widely assumed to make vision-language models more reliable on video question answering. We propose a small three-probe evaluation recipe to test that assumption: paired accuracy across direct, CoT, answer-first, and no-video conditions; a counterfactual video-swap diagnostic over the CoT chains; and a four-rung visual-degradation ladder. Each probe is reported under both a strict and a permissive regex scorer, with multiplicity correction over a manuscript-declared primary family. Applied to Qwen2.5-VL on Video-MME subsets, the recipe returns a two-part finding. The CoT chains are strongly video-conditioned: swapping the input video collapses chain overlap and flips most final letters, the opposite of what a "boilerplate-chain" null would predict. Yet on the same data, forced CoT does not improve MCQ accuracy, and on the smaller 7B model it produces a small but statistically supported drop under a post-hoc primary scorer choice. We do not claim this generalizes beyond the Qwen2.5-VL / Video-MME instantiation; the raw responses and a single recomputation script will be released with the supplementary material so every number can be re-derived.

---


### 483. [Discovering Crystal Structure Prediction Algorithms with an AI Co-Scientist](https://arxiv.org/abs/2606.22866)

**<font color=#1a73e8>作者：</font>** Kiyoung Seong, Nayoung Kim, Sungsoo Ahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Human-AI Co-discovery system (HACO) for scientific algorithm discovery through cross-domain search and sparse human steering. Starting from the goal of generating crystal structures from chemical compositions, HACO searched across generative modeling methodologies from multiple fields and identified MaskGIT, a masked generative model from vision, as a promising framework for crystal structure prediction (CSP). HACO instantiated this masked formulation as a discrete token model of crystal structure; guided by sparse high-level human objectives, it then added crystallographic symmetry tokens, space group stratified sampling for polymorph coverage, and sub-bin coordinate refinement, yielding the Masked Generative Crystal Transformer (MaskGXT). On the MP-20 polymorph split, MaskGXT reaches 79.06% match-everyone-to-reference (METRe) accuracy, compared with 70.87% for the strongest evaluated baseline. MaskGXT also attains the best match rate on standard MP-20 and MPTS-52 CSP benchmarks. These results provide evidence that, in domains offering cheap, fast, and well-aligned validation, transfer-guided interactive AI co-scientists can contribute to scientific algorithm discovery by identifying transferable modeling principles and combining them with targeted human domain guidance.

---


### 484. [SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers](https://arxiv.org/abs/2606.22874)

**<font color=#1a73e8>作者：</font>** Huzama Ahmad, Se-Young Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long contexts have become standard in pretrained LLMs, yet they remain expensive to run: prefill compute grows quadratically with sequence length, and every decode step re-reads a key-value cache that grows linearly with it. Sparse attention cuts these costs by attending only to a relevant subset of past tokens, but selecting that subset is itself expensive. We present SpotAttention, a lightweight selector that attaches to a frozen pretrained transformer and learns by KL distillation to estimate its attention distribution. The selector picks the top-K keys each query attends to, and because its estimate is a calibrated distribution, a dual top-p rule reads the per-query, per-layer budget directly from it. Across Qwen3 (dense, 4B-32B) and Qwen3.5 (hybrid linear/full attention, 4B-9B), SpotAttention matches dense accuracy at contexts up to 128K tokens, eight times the training length. Decode at L=128K runs 3.9x faster than FlashAttention and 1.8x faster than Twilight, the strongest training-free baseline. Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost.

---


### 485. [FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs](https://arxiv.org/abs/2606.22875)

**<font color=#1a73e8>作者：</font>** Wenlong Cheng, Yuan Gan, Yunqiu Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training Latent Diffusion Models (LDMs) within Federated Learning (FL) has attracted increasing attention due to its ability to combine the powerful generative capacity of LDMs with the privacy-preserving properties of FL. However, FL requires sharing the global model with multiple participants, which risks unauthorized model distribution or resale by malicious clients. While an intuitive approach is to adopt existing VAE-based watermarking techniques for LDMs in FL, this strategy falls short in addressing such threats due to two fundamental challenges: (1) Existing methods support ownership verification but lack the ability to trace model leakage to a specific malicious client; (2) VAE-based watermarks are vulnerable, as they can be removed simply by replacing the decoder with a clean counterpart. In this paper, we propose FedOT, the first framework for ownership verification and leakage tracing in federated LDMs. Specifically, to address the first challenge, we design a chunked watermark, where the first part is for ownership verification, and the second part is used for client identification. Furthermore, to overcome the second challenge and secure the model against VAE replacement attack, we introduce Latent Vector Transformation (LVT), which strengthens the connection between the VAE and U-Net latent spaces by modifying the original latent distribution of the VAE. Consequently, any attempt to replace the VAE for watermark removal leads to significant image quality degradation, making the LDM model unusable. Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. Project page: this https URL.

---


### 486. [Full-Body Golf Swing Kinematic Reconstruction From a Smartwatch IMU](https://arxiv.org/abs/2606.22876)

**<font color=#1a73e8>作者：</font>** Yuanshuo Tan, Kezhe Zhu, Xiujie Sun 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative measurement of the golf swing is critical for evaluating technique and enabling individualized feedback. However, existing methods are impractical to use on the golf course: optical motion capture is laboratory-bound, camera-based methods require impractical camera placement, and multi-sensor inertial measurement unit (IMU) systems require multi-segment setup and calibration. We thus propose a single wrist-worn IMU approach for estimating full-body joint angles during golf swings. The proposed Wrist-IMU Temporal Kinematic Network (WIT-KinNet) leverages modality-specific IMU embeddings and temporal kinematic encoding to learn wrist-to-body motion dependencies and estimate full-body joint angles during golf swings. Thirty-six golfers spanning beginner and skilled players, performed full, half, and quarter swings using seven club types: driver, 3-wood, 5-hybrid, 5-iron, 7-iron, 9-iron, and sand wedge. The proposed WIT-KinNet was evaluated under subject-wise cross-validation using synchronized smartwatch IMU data and ground-truth kinematics derived from an optical motion capture system. The proposed approach achieved a mean absolute error of 8.11 $\pm$ 1.84$^\circ$ across full-body joint angles. High temporal correlation was observed for pelvic rotation and upper torso rotation (r = 0.98 and 0.97, respectively), with X-factor and S-factor also showing strong correlation (r = 0.96 and 0.96). Linear mixed-effects models of the error revealed that swing amplitude, skill level, and club type all significantly affected measurement differences (p $<$ 0.05). The results establish the first single wrist-worn IMU approach for estimating full-body golf swing kinematics, enabling practical swing analysis during real gameplay.

---


### 487. [DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings](https://arxiv.org/abs/2606.22877)

**<font color=#1a73e8>作者：</font>** Wenya Xie, Shengming Zhou, Zelin Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated as jobs, routines, and tastes drift. Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. We introduce DynamicMem, a synthetic benchmark that constructs 15 months of activity per user, providing long-term multi-app data that real users' privacy keeps out of reach. It provides user-consistent trajectories averaging 2.2M tokens and 1,772 grounded events per user across 16 applications such as e-commerce, fitness, and social platforms. The profile evolves over this period and is never given explicitly: each attribute, habit, or preference must be inferred from small signals scattered across apps. We evaluate at five quarterly checkpoints to track how systems scale as history grows. Benchmarking five representative systems exposes problems a single accuracy score hides: (i) profile reconstruction degrades with history length while service-task accuracy stays flat, despite both drawing on the same memory; (ii) no system both keeps facts that stay true and replaces facts that change, with errors clustering on preferences and on naming the exact referent; and (iii) over 93% of failures trace to what the memory retrieves, not to the model writing the answer, so the largest room for improvement lies in memory itself. Code: this https URL

---


### 488. [CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents](https://arxiv.org/abs/2606.22883)

**<font color=#1a73e8>作者：</font>** Zhanbo Hua, Yifan Yao, Weihao Xie 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck. Existing synthesis pipelines typically scale by retrofitting surface-level artifacts into tasks, frequently yielding ambiguous instructions, shallow execution paths, and brittle tests that provide weak learning signals. To overcome this, we introduce CLI-Universe, a principled synthesis engine that constructs terminal-agent tasks. CLI-Universe generates candidate tasks by sampling combinations across a multi-dimensional capability taxonomy (domain, skill type, capability, and engineering pillar), then grounds each candidate through evidence-guided deep research over real-world technical materials. To ensure rigorous supervision, validated blueprints are instantiated into Dockerized environments and subjected to a multi-stage executable verification pipeline featuring rubric-gated test construction, hint-conditional filtering, and strict fail-to-pass checking. Across the full pipeline, from candidate generation to verification, approximately two-thirds of candidates are discarded, retaining only those that are genuine, verifiable, and non-trivially challenging. To validate our framework, we instantiate a highly distilled dataset of 6,000 trajectories called CLI-Universe-6K. Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. This sets a new state-of-the-art for models trained on open-source data at or below 32B parameters, and outperforms several models an order of magnitude larger, demonstrating the profound data efficiency of structured, high-fidelity synthesis.

---


### 489. [Explanation-Guided Medical Named Entity Recognition with Stability and Boundary Awareness for Atopic Dermatitis](https://arxiv.org/abs/2606.22886)

**<font color=#1a73e8>作者：</font>** Xueguang Li, Di Lin, Xue Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objective: This study aims to improve the reliability and robustness of medical named entity recognition (NER) in Chinese atopic dermatitis (AD) clinical texts through explanation-guided learning. Methods: We propose a stability and boundary-aware explanation-guided NER framework. Perturbation-based analysis is used to evaluate explanation stability and entity boundary sensitivity. An adaptive fusion strategy dynamically combines local and global explanation to generate more reliable token-level explanations. The fused explanation signals are further incorporated into model training through stability, boundary-aware, and consistency constraints. Results: Experiments on Chinese AD NER datasets show that the proposed framework improves explanation robustness and achieves consistent performance gains across multiple NER models. The adaptive fusion strategy also provides more stable explanations and stronger boundary perception than individual explanation methods. Conclusion: The proposed method effectively integrates reliable explanation signals into medical NER training, improving both recognition performance and explanation reliability. The framework provides a practical and generalizable solution for explainable medical NER and offers reliable support for downstream clinical decision-making and medical knowledge applications.

---


### 490. [PHOEBI: An Open-World Benchmark for Bacterial Identification in Phase-Contrast Microscopy](https://arxiv.org/abs/2606.22890)

**<font color=#1a73e8>作者：</font>** Aaditya Baranwal, Md Jahid Hasan, Shruti Vyas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical microscopy enables rapid, label-free imaging of live bacteria and is the standard instrument for species identification across clinical, environmental, and industrial microbiology. Yet field samples are routinely polymicrobial and may contain organisms that were never seen during system training, and no computer-vision benchmark tests multi-label species identification from phase-contrast microscopy (PCM) of such mixtures. We introduce Phase-contrast Optical bEnchmark for Bacterial Identification ($\textbf{PHOEBI}$), a wet-lab-prepared dataset of $120{,}000$ PCM images covering $40$ combinations of six rod-shaped species, paired with a leave-combinations-out (LCO) evaluation protocol that holds out entire species combinations to mirror the practical scenario of a model trained on catalogued mixtures that must generalise to unseen ones. On LCO, every gradient-trained per-image aggregator we test drops $0.39$ to $0.57$ F1 from the in-distribution to the held-out split, a systematic open-world recognition failure in the aggregator, not the visual representation. A linear probe of thirteen different encoders over the same features spreads only about six percentage points of F1 across general-purpose and biomedical pretraining objectives, confirming the representation is sound. We propose three lightweight $\textit{anchor-based}$ decoders that capture per-species presence geometrically over a shared frozen tile-feature pool, scoring $\textit{higher}$ on held-out combinations than on in-distribution validation.

---


### 491. [Learning Graphs through Continuous Information Entropy Fields](https://arxiv.org/abs/2606.22895)

**<font color=#1a73e8>作者：</font>** Hui Cong, Bo Sun, Ziheng Jiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph theory is inherently descriptive, capturing what relationships exist but not why they arise, because it treats edges as primitive constructs. This paper proposes a new explanatory framework for graph learning, where relationships emerge from latent continuous information entropy fields, and a graph becomes a discrete instantiation of an underlying field. To formalize this field, we introduce the Field-informed Graph Network (FGN). It learns a scalar field from node features and leverages it to modulate message passing. The information-theoretic objective balances structural fidelity with field smoothness, forming a self-reinforcing loop. In this loop, the field modulates information diffusion through field-modulated weighting, and the updated node representations iteratively refine the field. As a result, FGN learns by simulating its own co-evolution. Extensive experiments on node classification and graph classification benchmarks demonstrate superior performance, robustness to perturbations, and structurally coherent field representations.

---


### 492. [InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars](https://arxiv.org/abs/2606.22905)

**<font color=#1a73e8>作者：</font>** Quanyue Song, Yishan He, Yanfei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based models have enabled realistic audio-driven avatar generation in real-time streaming. However, existing approaches struggle to maintain visual temporal consistency and fail to explicitly perceive user intent in complex interactive streaming scenarios. To address these challenges, we propose InteractiveAvatar, a real-time infinite-streaming video generation framework that supports visually consistent avatar video generation and intent-aware interactions. With autoregressive distillation, InteractiveAvatar achieves real-time str-eaming generation of human avatars over arbitrarily long durations. For visual consistency, we introduce a Long-Short Visual Memory (LSVM) mechanism that flexibly compresses historical visual information into compact tokens, preserving both short-range coherence and long-term consistency. To generate avatars with speeches and actions aligned with user intent, we propose a Reasoning-Reaction Module (RRM), which incorporates a State-Cycling strategy and a Cache-Switching mechanism. Extensive experimental results over diverse scenarios demonstrate that our method achieves state-of-the-art visual consistency in long-duration generation, while enabling complex user-avatar interaction in real time.

---


### 493. [PromptDyG: Test-Time Prompt Adaptation on Dynamic Graphs](https://arxiv.org/abs/2606.22914)

**<font color=#1a73e8>作者：</font>** Guoguo Ai, Chaoxi Niu, Hui Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activities in numerous evolving systems can be represented as dynamic graphs in snapshot form at different time intervals, i.e., discrete-time dynamic graphs (DTDGs). Existing methods show impressive advances in capturing historical temporal evolution patterns in DTDGs, but they focus on addressing an offline learning setting, where models are trained using historical snapshots once and then evaluated to all subsequent graph snapshots without further updating. This fails to capture 1) the nature of evolving complexities across graph snapshots and 2) the distribution shift in the testing graph snapshots. To address these problems, we propose PromptDyG, a novel framework that leverages unsupervised test-time Prompt adaptation for Dynamic Graph learning under a live-update online setting. The key insight is that an expressive dynamic graph prompt can be learned on a frozen backbone via minimization of feature-wise, label-free entropy to efficiently and continuously model the evolving patterns. We show theoretically that this unsupervised prompt adaptation can guarantee a larger similarity margin between positive and negative pairs, facilitating more accurate dynamic predictions. It is further confirmed by our extensive empirical results on six benchmark datasets that show consistent and significant improvements of PromptDyG over state-of-the-art baselines.

---


### 494. [Intent-Governed Tool Authorization for AI Agents](https://arxiv.org/abs/2606.22916)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act through external tools: they read private data, construct structured payloads, submit write requests, export records, and coordinate workflows across application boundaries. Existing authorization mechanisms usually ask whether an integration credential, app, or token can call a tool. That question is necessary but incomplete. A tool call can be authorized by static credentials and still be unjustified by the user's current request. For example, a credential that can read and export records should not expose export authority when the user only asked for a bounded summary, and a model-generated delete call should not execute merely because the integration has a delete scope. This paper proposes Intent-Governed Access Control (IGAC), a server-side authorization layer that treats the user's expressed intent as a monotone, auditable policy attribute for AI-agent tool use. IGAC introduces intent certificates, session-scoped policy narrowing, intent-aware manifest filtering, and intent-tool-payload consistency checks. The central invariant is that user intent may only reduce the authority granted by static integration policy; it never expands scopes, data policy, tenant boundaries, or review requirements. We map IGAC onto OpenPort, an existing governance substrate that already implements authorization-dependent discovery, scope and ABAC-style policy checks, draft-first writes, preflight impact binding, state-witness checks, idempotency, stable reason codes, and audit.

---


### 495. [GRAIN: Group Aggregation via Min-Norm Objective](https://arxiv.org/abs/2606.22917)

**<font color=#1a73e8>作者：</font>** Nghia Bui, Jiarui Yao, Lijing Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning instability is a long-standing problem across machine learning, but it is especially acute in the overparameterized regime that defines modern deep learning: large models fine-tuned or trained on limited data traverse flat loss landscapes with many nearly-equivalent minima, and stochastic factors (initialization, data order, dropout, hardware non-determinism) can route optimization to very different solutions. The rise of large pretrained models (LPMs) makes the problem more urgent: training cost is high, downstream data is often small, and repeated runs for variance reduction are prohibitive. We introduce \textbf{GRAIN} (\textbf{G}roup \textbf{A}ggregation via m\textbf{IN}-norm objective), a lightweight training algorithm that replaces the mean aggregation used in mini-batch optimization (both across mini-batches and within a mini-batch) with a min-norm convex combination of group-wise gradients. \mName guarantees a non-negative inner product between the aggregated update and every group gradient, resolving intra- and inner-batch gradient conflict, and retains an $\mathcal{O}(1/T)$ convergence rate comparable to SGD. Under mild smoothness and absolute-continuity assumptions, the min-norm solution differs almost surely from the arithmetic mean, which yields a uniform-stability bound for \mName strictly tighter than the standard bound for SGD. Empirically across generation, classification, and regression at LPM scale, \mName delivers consistent improvements in mean performance and reductions in run-to-run variance over a broad suite of tasks, with no extra training-time or storage cost beyond a single backward pass.

---


### 496. [Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra](https://arxiv.org/abs/2606.22922)

**<font color=#1a73e8>作者：</font>** Giorgi Butbaia, Paul Orland, Coco Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying machine learning techniques to solving long-standing mathematical conjectures can be particularly challenging due to their extreme reward sparsity. As an illustrative example, we consider Kalai's algebraic Hirsch conjecture and recast the construction of its counterexamples as a sparse-reward reinforcement learning problem on graphs. We propose a constrained options-based HRL framework with an equivariant graph neural network policy, which allows us to learn useful temporal abstractions for this task. We evaluate our approach over a wide range of degrees and demonstrate that it consistently outperforms classical RL algorithms as well as greedy search. By exploiting the hierarchical structure of the problem, we effectively provide a first-of-its-kind application of HRL to a problem in commutative algebra.

---


### 497. [EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction](https://arxiv.org/abs/2606.22925)

**<font color=#1a73e8>作者：</font>** Chengxuan Qin, Zhige Chen, Shu Peng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. Existing standards organize files, metadata, and provenance, but they do not specify EEG tasks under a common language and rulebook, leaving critical task semantics scattered across papers, code, and manual interpretation. We investigate whether heterogeneous public EEG datasets can be standardized through a structured task specification language paired with a shared rulebook. Our methodology represents each benchmark entry as a task document synchronized with an executable task kernel, with the rulebook defining task fields, evidence requirements, document-kernel alignment, review states, and machine-checkable constraints. Using this methodology, we release a community-reviewed EEG benchmark corpus centered on 53 completed and reviewed entries with 245 task definitions spanning diverse paradigms, and we introduce NeuroDoc and NeuroAudit as the operational support layer for rulebook-guided drafting, upgrading, review, amendment, and release management. We further examine whether the resulting benchmark units can be instantiated in a shared downstream setting across four EEG foundation model backbones, providing execution-based evidence for reusable, auditable, and executable EEG benchmarking infrastructure.

---


### 498. [HADES: Privacy-Preserving Federated Learning via Selective Feature Encryption and Hybrid Model Fusion](https://arxiv.org/abs/2606.22928)

**<font color=#1a73e8>作者：</font>** Ergün Batuhan Kaynak, Kerem Bayramoglu, Sinem Sav  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we address the challenge of privacy-preserving training in federated learning (FL) by introducing a novel framework that selectively encrypts only the most privacy-sensitive features while leaving the remaining data and the corresponding model portion unencrypted. We propose HADES, a hybrid system that identifies and encrypts the most critical features, ensuring both privacy protection and computational efficiency. Unlike fully encrypted FL training pipelines, which suffer from high computational overhead, HADES integrates an encrypted and non-encrypted training pipeline via a fusion mechanism, enabling seamless interaction between encrypted and plaintext model representations. To achieve this, we use PCA to identify and encrypt the most privacy-sensitive features, which significantly reduces reconstruction attack success in FL. Building on this insight, we design a hybrid FL system that trains an end-to-end encrypted network via multiparty homomorphic encryption (MHE) on the selected features while simultaneously training a plaintext network on the remaining features. These two networks are then integrated using a fusion mechanism. We also introduce a general packing scheme that eliminates redundant rotations by considering the entire neural network architecture. Finally, we demonstrate that HADES matches the accuracy of vanilla FL while preserving privacy and achieving optimized runtime through selective encryption.

---


### 499. [BEV-Denoise: Learning Intrinsic Noise for Accurate Bird's-Eye-View Semantic Segmentation](https://arxiv.org/abs/2606.22931)

**<font color=#1a73e8>作者：</font>** Dooseop Choi, Kyounghwan An, Kyoung-Wook Min  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a framework dubbed \textbf{BEV-Denoise} that estimates and removes intrinsic noise from learned Bird's-Eye-View (BEV) features to achieve accurate BEV semantic segmentation. Inspired by the noise estimation capability of Denoising Diffusion Probabilistic Models (DDPM), we design a UNet-based noise estimation module that learns to estimate the noise from the learned BEV features. The estimated noise is then subtracted from the BEV features and fed to BEV map decoders for the final prediction results. To facilitate supervision for the noise estimation module, we follow a sequential learning paradigm called Task Decomposition (TD) where a pre-trained BEV map autoencoder is employed to train a view transformation (VT) encoder. We share three key insights learned from our intensive experiments that are critical for improved performance. We apply our framework to four existing models, encompassing the three major VT paradigms. Experimental results on a large-scale real-world dataset, nuScenes, demonstrate the effectiveness of our framework.

---


### 500. [Hybrid Compression: Integrating Pruning and Quantization for Optimized Neural Networks](https://arxiv.org/abs/2606.22935)

**<font color=#1a73e8>作者：</font>** Minh-Loi Nguyen, Long-Bao Nguyen, Van-Hieu Huynh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have witnessed remarkable advancements in recent years and have become integral to various applications. However, alongside these developments, training and deployment of neural network models on embedding and edge devices face significant challenges due to limited memory and computational resources. These problems can be addressed with deep neural network compression, which involves a trade-off between model size and performance. In this paper, we propose a novel method for model compression through two phases. First, we utilize model compression techniques, such as pruning and quantization, to significantly reduce the model size. Then, we use Mixture of Experts to route the previously compressed models to enhance performance while maintaining a balance in inference efficiency. MoEs consist of multiple expert models (i.e., compressed models) that are moderately sized and deliver stable performance. Experimental results on several benchmark datasets show that our method successfully compresses CNN models which achieves substantial reductions in FLOPs and parameters with a negligible accuracy drop.

---


> [!TIP]
> 当前位于：**451-500**（第 10/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
