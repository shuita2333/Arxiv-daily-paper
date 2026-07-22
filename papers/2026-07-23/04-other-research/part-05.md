# 📦 其他研究 | 2026年07月23日

> 本类共 **241** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-241**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-241**

---

### 201. [Predicting Activities in Aqueous Electrolyte Solutions with Hybrid Machine Learning](https://arxiv.org/abs/2607.19114)

**<font color=#1a73e8>作者：</font>** Zeno Romero, Maximilian Kohns, Fabian Jirasek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activities in aqueous electrolyte solutions, usually described by ionic activity and osmotic coefficients, are important properties for modeling many processes in industry and nature. Established activity models, such as those of Pitzer or Bromley, require fitting to experimental data for each electrolyte of interest and thus cannot predict properties for unstudied systems. While some predictive approaches exist, they are typically limited in scope and rely on additional ion-specific descriptors. In this work, we introduce a new hybrid model that combines the physics-based Bromley model with a matrix completion method (MCM) from machine learning. The MCM is employed to predict the electrolyte-specific parameters of the Bromley model, exploiting the fact that these parameters can be arranged in a matrix with cations and anions as rows and columns, respectively. Due to the lack of experimental data for many electrolytes, the initial parameter matrix is sparsely populated, making the prediction of the Bromley parameters for unstudied electrolytes a matrix completion problem. The hybrid model, Bromley-MCM, was trained end-to-end on experimental data for mean ionic activity coefficients and osmotic coefficients of aqueous solutions of 478 electrolytes at 298 K from the Dortmund Data Bank. As output, we obtain a completed matrix of Bromley parameters for 83 cations and 112 anions, enabling consistent prediction of concentration-dependent activities in aqueous solutions of 9,296 electrolytes at 298~K. This substantially extends the applicability of the Bromley model while maintaining high predictive accuracy, as demonstrated through evaluations on electrolytes excluded from model training.

---


### 202. [CR-Refiner: An Object-Centric Optimal Transport Reranker for Edit-Conditioned 3D Scene Retrieval](https://arxiv.org/abs/2607.19115)

**<font color=#1a73e8>作者：</font>** Hao Wu, Jinjing Zhu, Nanyu Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edit-conditioned 3D scene retrieval pairs a reference 3D room with a natural-language modification and retrieves rooms from a corpus that satisfy the edit. Three lines of prior work each fall short on this task. 2D composed image retrieval reasons over pixel-level edits and has no primitive for 3D object sets. 3D foundation encoders embed individual objects but cannot compose at the scene level. 3D scene-grounding methods localize references inside a static scene rather than rank modified rooms across a corpus. We present CR-Refiner, a training-free reranker that wraps any base retriever's top-K candidates with three components. A frozen LLM parses the edit into a structured query entity, and each candidate is scored by an unbalanced optimal-transport problem over a 1xG cost matrix coupling category, style, material, and geometry. The unbalanced solver lets the single-entity query drop mass on irrelevant objects, modelling the asymmetry directly. An axis-conditional structural prior adds size-keyword cues for geometric edits and subject-anchor direction cues for spatial edits. An LLM verifier refines the top three candidates with continuous confidence. Because no benchmark evaluates compositional matching over 3D object sets, we additionally release 3D-CER, 4,963 edit-conditioned queries over a 23,381-room indoor corpus across five edit axes, with multi-positive ground truth, CIRR-style hard subsets, and zero-target adversarials. Across three qualitatively distinct base retrievers, CR-Refiner consistently improves hard-subset R@1 and mAP@10 on every edit axis.

---


### 203. [Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning](https://arxiv.org/abs/2607.19117)

**<font color=#1a73e8>作者：</font>** Ubayd Ali Bapoo, Clement N Nyirenda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameterized action reinforcement learning has shown strong performance in environments requiring both discrete action selection and continuous parameterization. Prior work established the effectiveness of single-agent actor-critic algorithms - Greedy Actor-Critic (GAC), Soft Actor-Critic (SAC), and Truncated Quantile Critics (TQC) - on benchmark parameterized action tasks, but their extension to multi-agent settings remains largely unexplored. This paper presents a comparative study of shared-experience multi-agent extensions of these algorithms: Multi-Agent Greedy Actor-Critic (MAGAC), Multi-Agent Soft Actor-Critic (MASAC), and Multi-Agent Truncated Quantile Critics (MATQC). Rather than following the centralized training, decentralized execution (CTDE) paradigm, the proposed framework uses multiple independent actor-critic agents that share a replay buffer while maintaining separate policy and value networks. We evaluate the algorithms on the Platform-v0 and Goal-v0 benchmarks against their single-agent counterparts, using three-, five-, and ten-agent configurations to assess scalability. Performance is measured by average evaluation return and training time across ten independent runs, with one-way ANOVA and Tukey HSD post-hoc tests used to assess statistical significance. Results show that the multi-agent framework consistently improves Greedy Actor-Critic performance, while MASAC and MATQC show comparatively modest gains over their single-agent versions. Increasing the number of agents beyond five yields limited additional performance while substantially raising computational cost, particularly for MAGAC. These results highlight a trade-off between learning performance and computational efficiency, offering insight into the scalability of shared-experience multi-agent actor-critic methods for parameterized action reinforcement learning.

---


### 204. [Parallel Noising in Neural Markov Logic Networks](https://arxiv.org/abs/2607.19126)

**<font color=#1a73e8>作者：</font>** Peter Jung, Giuseppe Marra, Ondrej Kuzelka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Markov Logic Networks (NMLNs) are a flexible neurosymbolic relational model. Previous work has shown that, although NMLNs achieve strong performance as generative models for small relational structures, they underperform diffusion-based generative graph models on larger structures. In this paper, we strengthen NMLNs along two main dimensions: (i) we increase the expressive capacity of their potential functions using graph neural networks, and (ii) we develop a new training and inference algorithm inspired by parallel-tempering Markov chain Monte Carlo methods, which we name parallel noising. Together, these enhancements enable NMLNs to attain strong performance in graph generation relative to general diffusion-based generative graph models. Furthermore, they allow NMLNs to match the performance of specialized text-based recurrent models when generating small molecular structures.

---


### 205. [Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers](https://arxiv.org/abs/2607.19139)

**<font color=#1a73e8>作者：</font>** Maohua Li, Qirui Li, Yanke Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion transformers (DiTs) jointly process text and image tokens, yet their internal computation during denoising remains poorly understood. We introduce a causal interpretability framework for modern large-scale DiTs that combines attention decomposition with targeted interventions across token spans, heads, and layers. Using it to separate prompt-content tokens from structural template tokens, we find that the structural tokens carry little prompt-specific information at the encoder output. Yet surprisingly, they emerge as dominant image-to-text attention sinks and causally maintain object identity inside the DiT, acting as implicit semantic registers. We show that they acquire this identity indirectly, with prompt semantics first injected into the image latents and then read back into the template tokens rather than transferred directly from the prompt tokens. Inspired by the above findings, we design a training-free pruning rule for DiTs. Heads that attend most strongly to prompt tokens are dispensable, and pruning them removes $20\%$ of attention FLOPs with only a $1.4$-point drop on GenEval. We further reveal how generative computation in DiTs is organized across heads and depth, separating semantic routing from visual synthesis and progressing from identity formation to propagation and refinement. Our work not only reveals that the tokens encoding semantics at input need not be those that maintain it during generation, but also provides a causal view of internal mechanisms in DiTs.

---


### 206. [Sarus: Privacy-Preserving Multi-Vendor Perception Fusion via Homomorphic Encryption](https://arxiv.org/abs/2607.19146)

**<font color=#1a73e8>作者：</font>** Munawar Hasan, Apostol Vassilev  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cooperative perception enables autonomous vehicles (AVs) to improve situational awareness by aggregating detection outputs from multiple agents and sensing platforms, often via a shared fusion service in multi-vendor deployments. However, sharing such outputs at inference time exposes proprietary model behavior and sensitive environmental information, creating significant privacy and security concerns. In this paper, we present Sarus, a privacy-preserving framework for multi-vendor perception fusion via homomorphic encryption (HE), enabling aggregation without revealing individual vendor outputs. Each vendor encodes detections as compact Gaussian moment vectors over a shared spatial lattice and transmits encrypted payloads to a fusion server, which aggregates them directly in the encrypted domain. The fused result is then decrypted and reconstructed into final detections through class-wise bin merging.
We analyze the computational complexity, showing linear scaling for vendor payload construction and $O(BV)$ server-side fusion with the number of occupied bins $B$ and vendors $V$, while postprocessing scales as $O(B + \sum_{c\in \mathcal{C}} B_c^2)$, where $\mathcal{C}$ denotes the set of object classes and $B_c$ is the number of occupied bins for class $c$. Experiments demonstrate linear scaling in practice with only a bounded constant-factor overhead from HE, with decryption dominating postprocessing cost. Experiments on the KITTI dataset using camera (YOLOv8) and LiDAR (PointPillars, PV-RCNN) detectors show that Sarus improves scene-level coverage by effectively aggregating complementary detections, particularly in distance-dependent regimes where individual modalities degrade. These results indicate that privacy-preserving multi-vendor perception fusion is feasible for real-time deployment when statistical compression and spatial sparsity are jointly exploited.

---


### 207. [Incomplete Observations Boost Evolutionary Performance in Ocean Modeling](https://arxiv.org/abs/2607.19147)

**<font color=#1a73e8>作者：</font>** Yangyang Kong, Yutong Jiang, Yanhai Gan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven methods have revolutionized ocean modeling, yet current approaches rely heavily on complete reanalysis datasets, imposing computational constraints and limiting model performance to that of the training data. Here, we present a generative state-space model and an optimization framework that enable learning directly from sparse and noisy observations. The model is essentially a hidden Markov model with a continuous state space, where oceanic physical quantities are treated as hidden states and measurements as observations, enabling a unified representation of ocean fields and observational data. Both the initial-state and state-transition modules are implemented as neural networks to capture the complexity and temporal evolution of ocean states, while the emission module is formulated as a masked Gaussian distribution. To train the model from sparse observations, we derive an optimization framework based on the expectation-maximization (EM) algorithm. The framework alternately reconstructs high-fidelity ocean fields via Langevin dynamics and optimizes deep neural networks to capture temporal evolution. Theoretical analysis shows that the framework maximizes the likelihood of observations under the generative model. For efficiency, we assume that ocean-state evolution follows a stationary, ergodic, and Markovian stochastic process and adopt only length-two state sequences during optimization. Experiments on CMIP6 simulation data and FY-3D satellite data demonstrate high-fidelity reconstruction and accurate prediction, showing that sparse observations can directly improve the model's representation of ocean-state dynamics. This work offers a scalable pathway for next-generation Earth system models to learn directly from sparse, incomplete real-world observations.

---


### 208. [Breaking the Homogeneity Assumption: Specialized Multi-Generator Adversarial Learning for Rare Failure Detection in Predictive Maintenance](https://arxiv.org/abs/2607.19153)

**<font color=#1a73e8>作者：</font>** Alexis Lazanas, Georgios Kampouropoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised learning models in the predictive maintenance field are regularly trained on highly imbalanced industrial datasets: machine failures occur rarely but have a disproportionate effect on operations. In addition to the clear class disparity, failure data are typically non-homogeneous, with different failure modes arising from distinct physical processes and exhibiting a multimodal distribution across minorities and classes. Traditional imbalance-management methods, e.g., undersampling, SMOTE-based interpolation, or cost-sensitive learning, typically assume that the minority population is homogeneous. This means their effectiveness is severely limited in the multifaceted conditions encountered in industrial practice. This paper determines the possibility of a failure-type-conscious generative augmentation program to improve the identification of infrequent failures in predictive maintenance systems. An experimental design that is leakage-safe is used to compare five imbalance-handling methods: cost-sensitive learning, random undersampling, SMOTE oversampling, single-generator GAN augmentation, and a specialized multi-generator GAN architecture that has independent generators that are asked to learn individual failure subtypes. Precision/Recall-oriented measures are used to quantify model performance; the main evaluation measure is the PR-AUC. Experiments conducted on the AI4I 2020 predictive maintenance dataset indicate that the proposed multi-generator GAN framework produces more realistic minority samples, yielding higher PR-AUC and recall scores compared to traditional resampling methods and individual-generator GAN augmentation.

---


### 209. [Point Ladder Tuning: Parameter-Efficient Hierarchical Adaptation for 3D Point Cloud Understanding](https://arxiv.org/abs/2607.19171)

**<font color=#1a73e8>作者：</font>** Junlin Chang, Longhao Zou, Rui Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning pre-trained point-cloud backbones typically updates all parameters, resulting in substantial computation and memory overhead. More importantly, modern point backbones rely on aggressive tokenization and downsampling, which yields compact global tokens but irreversibly discards fine-grained local geometry, an inherent bottleneck for parameter-efficient adaptation. Consequently, existing PEFT methods that operate only on these coarsened tokens can modulate global semantics but struggle to recover the missing multi-scale locality. We present Point Ladder Tuning (PLT), a locality-aware PEFT framework that performs hierarchical, instance-conditioned adaptation while keeping the backbone frozen. PLT forms a lightweight closed loop: (i) a Hierarchical Ladder Network (HLN) constructs a multi-resolution local feature pyramid directly from raw points; (ii) a Local-Global Fusion (LGF) aligns and fuses local pyramids with intermediate backbone semantics; and (iii) a Dynamic Prompt Generator produces instance-aware multi-scale prompts to modulate the frozen backbone effectively. For dense prediction, we further introduce a lightweight segmentation head that progressively upsamples fused features and leverages backbone priors to refine fine structures. Extensive experiments on classification and dense prediction show that PLT consistently surpasses prior PEFT baselines with minimal tunable parameters. PLT achieves state-of-the-art performance using only 2.71% trainable parameters for classification and 7.69% for dense prediction, and scales favorably to larger backbones, requiring merely 0.36% parameters on PointGPT-L. The code is released at this https URL.

---


### 210. [Neural Kolmogorov Equations: Parallelizable Learning of Stochastic Dynamics under General Noise](https://arxiv.org/abs/2607.19173)

**<font color=#1a73e8>作者：</font>** Arthur Bizzi, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural stochastic differential equations (SDEs) have emerged as powerful tools for learning noisy or stochastic dynamics directly from data; however, existing approaches largely assume uncoupled and continuous noise, limiting their applicability to realistic stochastic drivers, and often scale poorly in time, requiring expensive autoregressive training. To address these limitations, we propose Neural Kolmogorov Equations (NKEs), a deterministic, infinite-dimensional reformulation of Neural SDEs based on the Kolmogorov Forward equation, transforming the learning problem from modelling individual stochastic trajectories to modelling the evolution of probability densities. NKEs learn general Lévy-type stochastic forcing directly through the operator structure of the KFE, and enable parallel-in-time training via a Lagrangian Galerkin projection and operator splitting. We evaluate NKEs on several stochastic benchmarks, including systems with coupled noise and jump processes, and verify that NKEs provide flexible models that accurately recover deterministic and stochastic dynamics with competitive predictive accuracy and improved training efficiency. Code and pretrained models will be released.

---


### 211. [Automated Extraction of Techno-Economic Data from 76,000 Energy System Studies](https://arxiv.org/abs/2607.19178)

**<font color=#1a73e8>作者：</font>** Maxime Gorres, Jan Göpfert, Patrick Kuckertz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Energy system models guide societally important decisions, but their credibility rests on quantitative assumptions that are difficult to source and audit. Meta-analyses can improve transparency and modeling practices, but the rapid growth of publications makes manual information extraction increasingly impractical. Consequently, databases are updated infrequently and efforts are often duplicated across research groups. Here, we demonstrate the highly accurate automated extraction of quantitative information from 76,000 energy system studies published since 2010. We compile 3.2 million structured quantitative data points together with 20 million associated metadata entries, spanning a broad spectrum of technologies, methodological approaches and system characteristics. Beyond providing input data for models, the resulting FAIR database make the energy systems literature itself analysable. We show where academic assumptions diverge from empirical observed data, and how research priorities vary at scale across technologies, regions and time. To facilitate broad use within the community, the database is provided through an interactive dashboard, enabling users to filter, analyse and download data according to their specific research needs.

---


### 212. [ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191)

**<font color=#1a73e8>作者：</font>** Fan Jiang, Zhaoxu Sun, Mengchao Wang 等 41 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

---


### 213. [Conservative Query and Adaptive Regularization for Offline RL Under Uncertainty Estimation](https://arxiv.org/abs/2607.19199)

**<font color=#1a73e8>作者：</font>** Li-Rong Zhou, Qin-Wen Luo, Sheng-Jun Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) aims to learn an effective policy from a static dataset, but its performance is fundamentally limited by dataset coverage. Action preference queries leverage expert feedback without additional environment interaction, enabling policy improvement during offline training. However, existing methods still face two key challenges: selecting informative preference queries and effectively exploiting the collected feedback. Current approaches typically rely only on the distance between policy actions and dataset actions for query selection, while enforcing fixed constraints that keep the policy close to queried preferences. Such strategies often lead to unstable policy updates and integrate poorly with value regularization. To address these limitations, we propose Conservative Query and Adaptive Regularization under Uncertainty Estimation, a lightweight framework that jointly improves preference querying and preference exploitation. Specifically, we employ a Morse network to estimate the uncertainty of policy actions with respect to the offline dataset. Based on this uncertainty, we introduce a conservative query strategy that selectively queries actions near the dataset to preserve Bellman-update stability, together with an uncertainty-aware adaptive regularization scheme that dynamically adjusts data-level constraints during policy optimization. We integrate our framework with CQL and evaluate it extensively on the D4RL benchmark. Experimental results demonstrate superior or competitive performance across a wide range of tasks.

---


### 214. [MIRA-Ev:A Benchmark for Granular Evidence Detection and Relational Reasoning in Clinical Exams](https://arxiv.org/abs/2607.19201)

**<font color=#1a73e8>作者：</font>** Iker De la Iglesia, Johanna Ramirez-Romero, Jose Maria Villa-Gonzalez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical NLP evaluation remains dominated by multiple-choice question answering (MCQA), which scores only final-answer accuracy and cannot detect when a model reaches the correct diagnosis while grounding it in irrelevant, absent, or contradictory evidence. We introduce MIRA-Ev, a clinical argument mining benchmark built on Spanish Médico Interno Residente (MIR) licensing-exam cases, re-annotated by expert clinicians with span-level premises, claims, and directed support/attack relations, and released in parallel Spanish (native), English, and Basque versions, the first clinical argumentation resource in Basque. MIRA-Ev organizes evaluation into a three-tier task hierarchy: evidence sentence retrieval, argumentative component extraction, and relation classification.

---


### 215. [Anatomy-Aware 3D Mesh Refinement of Pericardium Segmentations on Computed Tomography](https://arxiv.org/abs/2607.19210)

**<font color=#1a73e8>作者：</font>** Andreas W. Aspe, Jonas Jalili Loft, Michael Huy Cuong Pham 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate delineation of the pericardium in a cardiac CT scan is essential for quantifying epicardial adipose tissue, yet it remains one of the most challenging structures to segment due to its poor contrast boundaries. Instead of solely relying on image gradients, our framework leverages the anatomical context of surrounding anatomical structures to guide the segmentation. This work introduces a novel 3D iterative mesh refinement framework that balances anatomical and geometric forces derived from inherent anatomical rules to refine an initial, possibly ambiguous, segmentation into a high-precision, anatomically plausible result. Designed as a model-agnostic post-processing step, our method uses a 3D vector field to iteratively push the vertices to the correct anatomical locations. Evaluating the refinement on both a high-resolution in-house dataset and a coarse, sparsely annotated open-source dataset, our method consistently improves all volumetric, surface, and anatomical metrics. The framework demonstrates greater improvement when applied to weaker initial segmentations, highlighting its potential for improving segmentations for out-of-domain models and in limited-training-data scenarios. The method is formulated as a gradient-based, GPU-accelerated framework that can be easily extended to other anatomical use cases.

---


### 216. [AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters](https://arxiv.org/abs/2607.19223)

**<font color=#1a73e8>作者：</font>** Yu-Yang Qian, Hao-Cong Wu, Chen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding, in which a lightweight draft model first generates a draft sequence that is then verified in parallel by the target model, has become a prevalent paradigm for accelerating large language model inference. Recent work such as DFlash further boosts drafting efficiency by leveraging diffusion drafters, whose parallel denoising mechanism enables draft generation in a single forward pass. In this work, we uncover a central pitfall of diffusion drafters: bidirectional attention is a double-edged sword. On one hand, it endows the model with parallel generation and global contextual modeling capabilities; on the other hand, this inherent global dependency introduces high variance at both the domain-level and the token-level: acceptance rates fluctuate substantially across different domains, and draft token quality also varies heterogeneously at different token positions. To tackle this issue, we propose AdaFlash framework, comprising two components: (i) an on-policy distillation (OPD) algorithm with reverse-KL divergence tailored for diffusion drafters, bringing stable convergence and effectively reducing domain-level variance; and (ii) an adaptive length head that dynamically adjusts the candidate sequence length on the fly, substantially lowering the verification cost of the target model and handling token-level variance. Experiments demonstrate that AdaFlash consistently improves speedup rate during deployment, with especially significant gains in high-concurrency scenarios, achieving up to approximately 66% higher throughput than previous state-of-the-art methods.

---


### 217. [IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer](https://arxiv.org/abs/2607.19228)

**<font color=#1a73e8>作者：</font>** Zhengyu Zou, Hao Li, Kuixuan Jiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world spatial intelligence requires agents to understand scenes from continuous video streams, where objects move, persist, disappear, and reappear over time. While recent spatial foundation models have enabled generalizable feed-forward 3D reconstruction, most streaming methods remain geometry-centric and lack temporally consistent object-level understanding. Meanwhile, existing semantic reconstruction and 3D-aware vision-language methods largely rely on externally extracted 2D semantic cues or loosely coupled geometry inputs, limiting unified geometry-instance learning in long dynamic scenes. In this paper, we propose IGGT4D, a streaming instance-grounded geometry Transformer for online 4D scene understanding. IGGT4D processes video frames sequentially, reuses historical context through causal spatial-temporal modeling, and incrementally updates a unified representation of camera motion, geometry, and object identity. This enables long-sequence feed-forward reconstruction with geometry-instance consistency in dynamic environments. To address the lack of high-quality 4D supervision, we further construct InsScene4D-147K, a large-scale dataset spanning real/synthetic and static/dynamic scenes, with RGB images, depth, poses, and temporally consistent instance masks generated by an automated geometry-guided annotation pipeline. Experiments on 3D reconstruction, pose estimation, instance spatial tracking, and open-vocabulary segmentation demonstrate that IGGT4D outperforms existing streaming baselines while maintaining scalable online inference for long dynamic sequences.

---


### 218. [Selection Shapes the Boundary: A Preregistered Replication of Monotonicity and Label Agreement in Unselected NLI Populations](https://arxiv.org/abs/2607.19231)

**<font color=#1a73e8>作者：</font>** Haram Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work on human label variation (HLV) in natural language inference (NLI) has often relied on re-annotation resources that select items by disagreement level. An earlier study (arXiv:2607.15870) found that hypotheses containing non-upward monotonicity operators showed lower label agreement in ChaosNLI (Cliff's delta = -0.284), which is restricted to items whose majority label carries exactly three of five votes. We preregistered a replication of this boundary in the unselected populations that ChaosNLI was drawn from: the SNLI and MultiNLI development sets, using the same operator tagger and a four-level ordinal agreement outcome. The registered prediction fails. All seven contrasts return a positive Cliff's delta (non-upward items agree slightly more, not less), the only significant confirmatory contrast has the opposite sign to the registration, and every effect is far below our smallest effect size of interest (0.10). Robustness checks support the measurement: simulated tagger misclassification shrinks the effects rather than manufacturing them, and a manual re-tagging audit reaches four-class agreement of 0.875 on a fresh 200-item sample. We conclude that the earlier negative boundary is plausibly a structure conditional on low-agreement selection rather than a population-level property, and that HLV structure claims built on selected re-annotation resources should state their selection conditional explicitly.

---


### 219. [S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2607.19232)

**<font color=#1a73e8>作者：</font>** Kshitij Kumar Srivastava, Kshitij Jerath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical Reinforcement Learning (HRL) intends to separate strategic planning from primitive execution. It has been widely successful in solving long-horizon and complex tasks, where flat-RL algorithms have difficulty in learning. However, while the low-level agent in HRL benefits from dense feedback and abundant trial opportunities, the high-level agent receives sparse, delayed feedback from the environment and its performance depends on the low-level execution capability. In this paper, we study whether subgoal selection by the high-level agent can be performed more strategically, by providing it with dynamics-aware intrinsic motivation. Since motivation based on primitive transition dynamics would require broad coverage of the state-action space, we propose to use coarse dynamics, i.e., environment transitions aggregated over multiple steps at the temporal scale at which the high-level agent operates. This approach stabilizes the high-level policy by learning to minimize the predictive uncertainty associated with the coarse dynamics, and provides a guided structure for navigation. We model the predictive uncertainty by evaluating different dispersion metrics as approximated by a Mixture Density Network (MDN). Empirically, we observe that a dense, dynamics-aware intrinsic reward leads to risk-averse subgoal selection, enabling it to outperform state-of-the-art HRL methods in non-stationary long-horizon environments.

---


### 220. [In-Context Time Series Classification with Random Convolutional Features](https://arxiv.org/abs/2607.19234)

**<font color=#1a73e8>作者：</font>** Joscha Cüppers, Jilles Vreeken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification is central to domains like medical signal analysis, industrial monitoring, and sensor-based activity recognition, where class information manifests as localized shapes, specific frequencies, temporal shifts, or complex cross-channel interactions. Random convolutional transforms efficiently map these sequences to fixed-dimensional tabular features but are traditionally paired with simple linear classifiers. We investigate whether a pretrained tabular foundation model can more effectively harness these rich representations.
We propose MASHT, a pipeline that marries MultiRocket and Hydra features with the power of in-context tabular foundation models. By leveraging a pretrained tabular foundation model, our approach completely bypasses task-specific model training, requiring only feature extraction and direct inference. Extensive experiments demonstrate that MASHT matches state-of-the-art time series classification baselines on univariate tasks, achieving a lower average rank than HIVE-COTE 2.0. On multivariate datasets, MASHT remains highly competitive with the strongest reference methods.

---


### 221. [DBMol: Design of High-Affinity, Target-Specific Small Molecules through Structure Prediction Models](https://arxiv.org/abs/2607.19237)

**<font color=#1a73e8>作者：</font>** Yiming Qin, Kai Yi, Miruna Cretu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing small molecule ligands that bind with high affinity to specific protein pockets is a fundamental goal in drug discovery, as small molecules constitute a major fraction of approved therapeutics. Recent breakthroughs in structure prediction, such as AlphaFold-3 and Boltz-2, enable accurate biomolecular interaction prediction and show promise as foundation models for downstream tasks, including binding affinity prediction. We propose to leverage these models and introduce DBMol, a new structure predictor-guided framework for de novo small molecule design. DBMol formulates an alternating optimization and projection process. In the optimization stage, DBMol starts from an initial molecule and uses gradient-based optimization to improve pocket-specific interactions and predicted binding affinity using a structure prediction model. In the projection stage, a flow-matching model maps the optimized molecular graph to discrete and chemically valid molecules. Experiments show that DBMol effectively optimizes the Boltz-2 affinity proxy and generates molecules with strong predicted affinity and specificity under Boltz-2 evaluation. To reduce self-confirmation bias, we further evaluate generated molecules using held-out metrics, including AF3-based evaluation. DBMol substantially improves pocket coverage while maintaining molecular diversity over unconditional generation, and is competitive under held-out metrics despite the absence of reference-ligand supervision. These results support the promise of structure prediction models as effective optimization signals for de novo molecular design.

---


### 222. [Thermodynamics-Informed Input Reparameterization for Neural Prediction of Real-Fluid Thermodynamic Properties in Supercritical Combustion](https://arxiv.org/abs/2607.19241)

**<font color=#1a73e8>作者：</font>** Haoze Zhang, Han Li, Ke Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-fluid thermodynamic property evaluation is a major computational cost in supercritical combustion simulations. In the enthalpy-based pressure-correction formulation, the closure evaluates temperature T, density $\rho$, and compressibility coefficient $\psi$ from the solver state (h,p,Y) through enthalpy-temperature inversion and repeated real-fluid equation-of-state evaluations. Neural-network surrogates offer fixed-cost inference, but direct mapping from (h,p,Y) to $(T,\rho,\psi)$ must capture the enthalpy-temperature relation and non-ideal equation-of-state response, resulting in a complex regression problem. This work introduces a thermodynamics-informed input reparameterization strategy, termed target-aligned input reparameterization (TAIR). TAIR replaces the raw enthalpy coordinate of each property network with a target-matched thermodynamic coordinate: the temperature network uses a temperature estimate obtained by inverting a constant-$c_p$ ideal-gas mixture enthalpy approximation, whereas the density and compressibility networks use an ideal-gas density estimate. These algebraic transformations use only solver-available variables and species constants, guiding the networks to learn real-fluid departures from ideal-gas baselines rather than reconstructing the full closure from raw enthalpy. The method is assessed using supercritical methane-oxygen counterflow flame data against a raw-input baseline and target-inconsistent cross-reparameterization controls. TAIR reduces held-out RMSE by factors of about 1.5, 2.0, and 7.5 for T, $\rho$, and $\psi$, respectively. For an unseen strain-rate flame within the augmented thermodynamic envelope, the corresponding factors are 3.6, 14.5, and 6.0. The target-inconsistent controls perform worse, indicating that the gains arise from thermodynamically matched input design rather than generic preprocessing.

---


### 223. [PTSan: A Practical Memory Safety Sanitizer for C/C++ with Pointer-Object Authority](https://arxiv.org/abs/2607.19246)

**<font color=#1a73e8>作者：</font>** Eli Davis, Eric Lahtinen, Michael Gordon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory safety errors remain the dominant source of severe vulnerabilities in C and C++. Pointer-based sanitizers provide stronger guarantees than location-based tools such as LLVM's ASan, but their overhead and compatibility limitations have constrained production use. We present PTSan, an LLVM sanitizer that makes pointer-based checking practical by storing an object identifier in each pointer's high bits and its bounds in a fixed-size runtime table. This representation trades a finite live-object budget for low overhead, optimizer visibility, and commodity-hardware support. Because identity travels with the pointer value, ordinary LLVM dataflow propagates it without explicit per-pointer metadata instructions. Separating metadata lookup from check enforcement exposes both as LLVM IR, enabling check hoisting, elision, and merging, plus whole-function min-cut placement of compatibility tag strips. Intel Linear Address Masking eliminates the remaining strips in hardware when available.
On stock hardware PTSan runs at parity with the fastest published location-based sanitizer: 57.2% geomean overhead on SPEC CPU 2017 on x86-64 (46.4% with Intel LAM), 54.7% on ARM64, and 31.5% (x86-64) on the application-shaped LLVM MultiSource suite. This is roughly a third of the published overhead percentage of prior systems with similar pointer-object authority guarantees, while preserving the inter-object, non-object, and temporal detection coverage measured by an independent memory safety test suite. Its physical-memory overhead is effectively native, a critical property for production deployment as memory costs become a first-order constraint. We also demonstrate practical overhead on real-world server and security workloads. These results show that PTSan brings practical pointer-based memory safety into a recompile-only sanitizer deployment model.

---


### 224. [Sequential Learner Modeling Using Multi-Relational Graph Convolutional Networks](https://arxiv.org/abs/2607.19253)

**<font color=#1a73e8>作者：</font>** Rawaa Alatrash, Mohamed Amine Chatti, Hong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User modeling is a critical task in a variety of personalized systems. Recognizing their effectiveness in learning from graph-structured data, Graph Neural Networks (GNNs), particularly Graph Convolutional Networks (GCNs), are increasingly employed for user modeling. However, existing approaches typically treat different relation types in a graph as homogeneous, limiting their ability to capture richer semantics and construct more informative user models. While multi-relational GNNs (MR-GNNs) have been adopted for representation learning and recommendation, their application for user modeling remains unexplored. Moreover, existing GNN-based user modeling approaches ignore the user interaction sequence. To address these research gaps, in this work we propose MR-ConceptGCN, a novel fully unsupervised approach focused on concept-based sequential learner modeling using multi-relational GCNs (MR-GCNs). MR-ConceptGCN effecively combines Personal Knowledge Graphs (PKGs), MR-GCNs, and the pre-trained language model SBERT to obtain enhanced relation- and semantic-aware representations of the PKG items. The enriched embeddings of the knowledge concepts that a learner did not understand when interacting with learning materials in CourseMapper are then used to construct a sequential learner model that combines long-term and short-term learner interactions. We report the results of an online user study (n = 31), demonstrating the benefits of MR-ConceptGCN in terms of several important user-centric aspects including accuracy, usefulness, diversity, and satisfaction with an educational recommender system.

---


### 225. [BioSecBench-Surveillance: A Verifiable Benchmark for AI Agents in Pathogen Genomic Surveillance](https://arxiv.org/abs/2607.19262)

**<font color=#1a73e8>作者：</font>** Harmon Bhasin, Kevin Flyangolts, Dianzhuo Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As pathogen genomic surveillance scales, the bottleneck is shifting from data generation to analysis. We present BioSecBench-Surveillance, a verifiable benchmark of 100 evaluations testing whether AI agents can infer the right analysis pipeline from raw sequencing data and surveillance context. Each evaluation gives an agent only the data and context a human analyst would have, then grades its structured answer deterministically. The tasks span seven categories, from taxonomic classification to genetic-engineering detection, across diverse sample types and sequencing technologies. Across 3,962 gradable attempts from sixteen model-harness pairs, the strongest configuration cleared only about half. Opus 4.8 with PI led at 50.2 percent, with a 95 percent confidence interval of 40.1 to 60.3 percent across 83 evaluations, tied with GPT-5.5 with Codex at 50.2 percent, with a 95 percent confidence interval of 40.8 to 59.6 percent, followed by Opus 4.7 with PI at 49.6 percent, with a 95 percent confidence interval of 40.0 to 59.2 percent, and Sonnet 4.6 with PI at 48.6 percent, with a 95 percent confidence interval of 38.9 to 58.3 percent. Even when agents invoked the correct workflows, their mistakes came from the choices around them, such as which references, thresholds, filters, and normalization to apply. BioSecBench-Surveillance provides a standard for measuring whether agents can be trusted to perform genomic surveillance when the next outbreak arrives.

---


### 226. [GUIDED Network-Agnostic Feature Initialization for Spatial Transferability in GNN-based Models](https://arxiv.org/abs/2607.19270)

**<font color=#1a73e8>作者：</font>** Alessandro Scalese, Santhanakrishnan Narayanan, Constantinos Antoniou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Traffic Assignment Problem is a fundamental but computationally expensive component of transportation planning. While Graph Neural Networks have emerged as fast, data-driven surrogates, their practical deployment is severely constrained by a spatial generalization gap. Standard models rely on transductive feature initializations that tie travel demand to fixed network topologies, preventing seamless transfer to new urban environments. To overcome this structural limitation, this research proposes a network-agnostic initialization layer, termed Geometrically Unconstrained Inductive Demand EmbeDding (GUIDED). By injecting travel demand as a scalar attribute on auxiliary virtual links rather than as specific node features, this modular framework standardizes the input space regardless of network scale. Extensive experimental evaluation across multiple urban topologies demonstrates that a Heterogeneous Graph Attention Network (HetGAT) model integrated with the proposed GUIDED layer maintains state-of-the-art predictive accuracy on single-network tasks, while demonstrating superior robustness to out-of-distribution demand patterns and maintaining a distinct performance advantage over the baseline even under severe data scarcity. Notably, the proposed feature initialization enables highly parameter-efficient domain adaptation for inter-network transfer learning without artificial input homogenization, establishing a robust foundation for truly inductive models. At the same time, the optimized scatter operations of the initialization layer yield an approximate 50% reduction in training time per epoch compared to the baseline approach. Furthermore, while demonstrated on vehicular traffic, this fundamental abstraction of spatial topology provides a versatile blueprint for generalized origin-destination spatial problems, such as freight logistics and multimodal network optimization.

---


### 227. [A Reinforcement-Learning-Augmented Liquid-Fueled Reactor Network Model for Predicting Lean Blowout in Gas Turbine Combustors](https://arxiv.org/abs/2607.19281)

**<font color=#1a73e8>作者：</font>** Philip John, Eloghosa Ikponmwoba, Pinaki Pal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study introduces a reinforcement learning (RL) framework for generating optimal liquid-fueled reactors to improve lean blowout (LBO) predictions in gas turbine combustors. Existing approaches for determining cluster boundaries rely on manual heuristics or distance-based metrics in the input space. In contrast, the proposed method is goal-oriented, explicitly accounting for the target metric (e.g., LBO prediction accuracy) during cluster formation. The framework employs a multi-stage clustering--classification strategy: an initial clustering step (e.g., $k$-means clustering) generates a large set of homogeneous micro-clusters, followed by an actor-critic RL agent that merges them into optimal reactor zones. The validation study, performed using a Jet-A mechanism (119 species, 841 reactions), shows the RL framework offers improved predictive fidelity compared to $k$-means and captures the correct LBO trends, while achieving substantial speedups relative to the high-fidelity computational model. Overall, the RL-driven approach demonstrates strong potential as a computationally efficient reduced-order modeling technique that can complement high-fidelity simulations for rapid design-space exploration.

---


### 228. [No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation](https://arxiv.org/abs/2607.19288)

**<font color=#1a73e8>作者：</font>** Feinan Cheng, Dongliang Xu, Wenli Nong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling offers a promising method to improve the inference performance of Vision-Language Models (VLMs) without additional training. Existing approaches to vision-language navigation (VLN) for Unmanned Aerial Vehicle (UAV) typically relies on a single inference pass, which can falter in complex environments by producing suboptimal or unsafe trajectories. In this paper, we explore a simple and effective approach to apply test-time scaling to VLN for UAV. We enhance navigation reasoning through an iterative refinement process that requires no extra model training, guiding the model to re-evaluate its initial navigation plan for better accuracy and safety. Our method first prompts the model to generate multiple parallel candidates and then performs a self-correction step, achieving deeper and more robust planning without changing the underlying model. To further strengthen decision-making, we design a multi-criteria scoring function to evaluate the refined candidates based on safety, goal alignment, and forward-progress. This simple yet powerful combination enables a frozen UAV navigation VLMs to self-correct and generate more accurate and reliable flight plans, achieving SOTA performance in this task.

---


### 229. [Real-time optimal control with shallow recurrent decoder networks](https://arxiv.org/abs/2607.19302)

**<font color=#1a73e8>作者：</font>** Matteo Tomasetto, Francesco Braghin, J. Nathan Kutz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controlling dynamical systems in real-time across multiple scenarios is critical to enabling adaptive control strategies, ensuring stability and efficiency. However, to tailor control actions in response to varying scenarios, traditional optimal control problems typically require several system simulations, which are often computationally demanding due to the high-dimensionality of the underlying spatio-temporal dynamics. In this work, we exploit SHallow REcurrent Decoder networks-based Reduced Order Modeling (SHRED-ROM) to synthesize a real-time closed-loop controller for high-dimensional and parametric dynamics, relying solely on limited state sensor readings. After training the model on a few optimal examples given by an expert demonstrator, SHRED-ROM mimics the expert behavior with effective distributed control actions in new scenarios, alleviating the curse of dimensionality. Moreover, a sensor forecaster is synthesized and used to close the loop at the latent level, thus efficiently mitigating possible sensor failures or delays. The performance of the proposed optimal control strategy is finally assessed on three challenging high-dimensional cases dealing with either parametric density control or fluid flow control.

---


### 230. [Riemannian Deep Learning:Modules, Networks, and Geometries](https://arxiv.org/abs/2607.19305)

**<font color=#1a73e8>作者：</font>** Chen Ziheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks on manifold-valued representations have attracted growing interest, but many basic components remain tied to specific manifolds, rely on Euclidean approximations, or require costly and numerically fragile geometric operations. This thesis develops a unified framework for Riemannian deep learning from three complementary perspectives: reusable neural modules, manifold-specific network architectures, and the design of underlying geometries. It generalizes batch normalization from Euclidean spaces and individual manifolds to broad classes of Lie groups and gyrogroups, and extends multinomial logistic regression from Euclidean space to SPD manifolds and then to general Riemannian manifolds. It further develops neural networks for several important geometric representations, including an unconstrained model of hyperbolic space, Busemann-based hyperbolic learning, and full-rank correlation matrices. Finally, it introduces adaptive and computationally efficient Riemannian metrics on SPD manifolds, including learnable Log-Euclidean geometries and fast, stable Cholesky-based geometries. The proposed methods are supported by theoretical analysis and validated through numerical experiments and applications in vision, signal processing, graph learning, and genomics.

---


### 231. [Staypoint Detection from Noisy Trajectory Data [Experiment Paper]](https://arxiv.org/abs/2607.19312)

**<font color=#1a73e8>作者：</font>** Lance Kennedy, Hossein Amiri, Yueyang Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting staypoints from raw trajectory data is fundamental to numerous spatial computing applications. This process transforms raw numeric sequences of geolocations into semantically meaningful locations, such as homes, workplaces, or restaurants. Despite its importance for semantic trajectory analysis, staypoint detection lacks standard benchmarks, and existing algorithms have never been systematically evaluated. This gap persists because no publicly available datasets provide both raw individual trajectories and ground-truth staypoint annotations. This benchmark paper addresses this limitation with two key contributions: (1) we introduce 16 large-scale simulated datasets capturing thousands of agents with annotated staypoints across varying trajectory noise levels, and (2) we evaluate nine staypoint detection algorithms-including both state-of-the-art and novel methods-to analyze their robustness to noise. Our evaluation reveals that existing state-of-the-art algorithms perform poorly under realistic noise conditions. Conversely, our proposed unsupervised methods yield substantial improvements, while supervised approaches drastically outperform existing baselines. While these results are very promising, these datasets and methods are only meant as starting points for future research in staypoint detection.

---


### 232. [Off-Context GRPO: Learning to Reason on Hard Problems using Privileged Information](https://arxiv.org/abs/2607.19313)

**<font color=#1a73e8>作者：</font>** Priyank Agrawal, Ankur Samanta, Shervin Ghasemlou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves reasoning in large language models. Yet, typical RLVR approaches fail on difficult problems: when a model cannot generate any correct solutions, it receives \textit{zero} learning signal. Providing privileged guidance during training, such as solution prefixes, can help overcome this learning cliff by steering the model towards {correct solutions with non-zero reward}. {We call these rollouts \textit{off-context}: they are generated from a training prompt that contains privileged guidance, while the target objective is defined by the original prompt without that guidance.} {We introduce} Off-Context GRPO (OC-GRPO), a minimally modified variant of GRPO that uses guided rollouts but applies an importance-corrected objective to steer the update back toward the original unguided objective, avoiding the mismatch that destabilizes uncorrected guided training. Empirically, our algorithm achieves a 3.9\% absolute improvement (13.8\% relative gain) over vanilla GRPO on average across standard mathematical reasoning benchmarks with negligible additional cost.

---


### 233. [ERank in Latent Space as an Image-Complexity and Richness Measure](https://arxiv.org/abs/2607.19315)

**<font color=#1a73e8>作者：</font>** Maksim Smirnov, Grigory Kononov, Anastasiia Linich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose the effective rank (ERank) of the channel covariance of an image's deep feature map as a per-sample, label-free measure of visual richness, computed from a single forward pass through a frozen pretrained encoder. ERank counts how many decorrelated channel directions an image activates, and we characterize its properties, including its behavior under noise. Empirically, ERank orders images from plain to visually rich, correlates with codec bitrate, sharpness, and edge density, and correlates with human complexity annotations on IC9600 with $r = 0.72$. As a data-selection criterion, removing low-ERank samples improves super-resolution and removing high-ERank samples improves OCR, in both pretraining and finetuning, while selection does not help classification, segmentation, or denoising. ERank is thus a cheap richness signal, useful exactly when task difficulty is governed by input richness.

---


### 234. [CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability](https://arxiv.org/abs/2607.19317)

**<font color=#1a73e8>作者：</font>** Pratinav Seth, Hem Gosalia, Aditya Kasliwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Circuit analysis can support not only model explanation but also downstream interventions such as pruning, editing, steering, and selective fine-tuning. However, conducting such analyses currently requires stitching together separate implementations for discovery, evaluation, and intervention, as well as hand-authoring the contrastive prompts required by many discovery methods. This fragmentation makes methods difficult to compare and limits their application beyond canonical tasks. We introduce CircuitKIT, a source-available library that connects the circuit-analysis workflow through a typed, serializable representation. CircuitKIT provides a suite of discovery algorithms, declarative interfaces for mapping structured data into discovery tasks, complementary circuit diagnostics, and downstream application modules. Together, these components provide common infrastructure for conducting and comparing circuit analyses. The library, examples, notebooks, and documentation are released at this https URL .

---


### 235. [ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321)

**<font color=#1a73e8>作者：</font>** Lena Libon, Ben Rank, Jehyeok Yeon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents begin to automate AI R&D, we need ways to assess whether their outputs are safe to deploy, even when the agents themselves may be untrusted. AI control offers one such approach: rather than trusting the agent, it treats it as a potential adversary and uses a monitor to detect covert sabotage before deployment. We evaluate AI control for automated AI R&D with ResearchArena, a framework spanning four long-horizon tasks: safety post-training, capabilities post-training, CUDA-kernel optimization, and inference-server optimization. Because the deliverable in AI R&D is an artifact that will be deployed and run, we pair each main task with two kinds of hidden side task: an embedded side task that sabotages the submitted model, adapter, kernel, or server itself, and an independent side task that takes a covert out-of-scope action in the sandbox while leaving the artifact honest. We evaluate frontier agents at both sabotage and monitoring, across four monitor types that vary along two axes: whether the monitor may execute and probe the produced artifact, and whether it sees the agent's chain-of-thought. We find that sabotage hidden in the training data is the hardest to catch, flagged fewer than half the time. Letting the monitor run experiments on the artifact, rather than only read the trajectory, helps, but it is not enough: monitors still miss embedded sabotage by inspecting only the surface, by noticing the anomaly but explaining it away, or by probing the artifact with the wrong test. We release ResearchArena as a modular framework for evaluating sabotage and control in automated AI R&D.

---


### 236. [InstructMixup: Instruction-Guided Salient Patch Editing for Robust Data Augmentation](https://arxiv.org/abs/2607.19324)

**<font color=#1a73e8>作者：</font>** Khawar Islam, Arif Mahmood, Xin Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In image and video technologies, data augmentation is widely used to improve the generalization of deep visual models, and mixup-based strategies that interpolate between samples have become the dominant approach. However, computing informative mixing regions adds substantial overhead, and blending content across different images frequently disrupts the semantic integrity of the resulting sample. We propose \our{}, a data augmentation method that constructs challenging yet label-consistent training samples entirely within a single visual sample. \our{} first extracts multi-scale salient patches from the sample using a lightweight saliency detector, refines each patch with an instruction-guided generative model, and blends the edited patch back into the non-salient regions of the same sample; because the generative edits are computed once and cached offline, this step adds negligible training cost. To further diversify the learned representation, \our{} injects self-similar fractal structure into the same salient regions at an adaptive ratio, so each training sample carries both fractal and non-fractal structure. We derive a second-order approximation of the resulting vicinal risk, showing that the method simultaneously enforces invariance to the generative edit and suppresses curvature along the perturbed salient directions, and we verify both predictions empirically. We evaluate on small to large backbones for instance Convolutional Neural Networks (CNNs), Vision Transformers (ViTs) and Vision-Language Foundational Models (VLMs) across seven benchmarks covering coarse- and fine-grained classification, robustness to corruption and occlusion, calibration, and transfer and self-supervised learning, InstructMixup outperforms nine competing augmentation methods, surpassing the strongest baseline across all benchmarks.

---


### 237. [Associative Emotional Learning in Convolutional Neural Networks](https://arxiv.org/abs/2607.19327)

**<font color=#1a73e8>作者：</font>** Seowung Leem, Andreas Keil, Mingzhou Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Associative emotional learning enables organisms to adaptively link pleasant or unpleasant outcomes to the presence of predictive stimuli. Whereas computational models such as the Rescorla-Wagner model have shed light on this important function, the limitations of these models are also known, especially when they are applied to neural data. The advent of deep neural networks has opened another avenue for modeling associative emotional learning. In this work we proposed a deep neural network model of visual valence processing, consisting of a visual module that encodes complex natural scenes and a module that recognizes their emotional significance in terms of valence, a key dimension of emotion, and tested a novel Pavlovian learning paradigm on the model. The results showed that with learning, the model reproduced several observations from human associative learning studies, including association formation and generalization, and that the neural representations of the conditioned and the unconditioned stimuli became increasingly aligned both at the single unit and at the neural population level. Comparison between the model and human experimental data provided further validation of our approach. This study thus suggests that deep neural network models, when combined with appropriate learning algorithms, can be used to model behavioral and neural signatures of associative emotion/valence learning.

---


### 238. [ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling](https://arxiv.org/abs/2607.19332)

**<font color=#1a73e8>作者：</font>** Chirag Vashist, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have undergone many generations of evolution, from VAEs/GANs to diffusion/flow matching. Along the way, the underlying techniques have become more complicated and various beliefs about what drives strong empirical performance have taken hold. Due to the success of diffusion models and flow matching, one of the more common beliefs is the importance of transforming the noise distribution to the data distribution gradually through many small transformations. We ask whether this is truly necessary, and take a minimalist approach to designing a competitive generative model. We start with the bare-bones essentials, namely just a training objective and a model. We purposefully make both simple. For the training objective, we choose Implicit Maximum Likelihood Estimation (IMLE), and eschew more complicated alternatives such as variational inference, adversarial training and numerical integration. For the model, we eschew transformers and instead choose a moderately sized convolutional network. Then we judiciously added elements that are truly essential, which surprisingly do not include iterative denoising. The result is a single-step parameter-efficient generative model that produces high quality samples at fast speed: it achieves an FID of 2.56 on ImageNet 256 and simultaneously attains good precision and recall.

---


### 239. [Provable diffusion-based posterior sampling for linear inverse problems via DDIM](https://arxiv.org/abs/2607.19333)

**<font color=#1a73e8>作者：</font>** Yuchen Jiao, Na Li, Changxiao Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based methods have achieved remarkable empirical success in solving inverse problems. However, many existing posterior samplers either lack rigorous theoretical guarantees or incur substantial computational overhead. We propose a simple and efficient algorithm, called \pddim, for solving linear inverse problems with diffusion priors via a DDIM-type sampler. Our method requires only lightweight, coordinate-wise modifications to the standard DDIM update, while explicitly incorporating the measurement model. The key idea is to perform posterior sampling separately along each singular direction of the measurement operator: for each direction, the sampler follows the learned diffusion prior when the observation signal-to-noise ratio (SNR) is below the corresponding diffusion SNR, and switches to a calibrated measurement-based predictor otherwise. We prove that the proposed sampler converges to the Bayesian posterior conditioned on the measurements. Empirical results show that the proposed sampler performs favorably against existing diffusion-based posterior samplers across a range of image restoration tasks, achieving the best performance on the majority of evaluation metrics considered. Overall, our results convert posterior sampling for noisy linear inverse problems to simple coordinate-wise DDIM updates, yielding an efficient, easy-to-implement algorithm with provable posterior consistency.

---


### 240. [CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents](https://arxiv.org/abs/2607.19338)

**<font color=#1a73e8>作者：</font>** Qijia He, Jiayi Cheng, Chenqian Le 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents increasingly operate in executable environments where a failed attempt produces actionable feedback rather than merely an incorrect answer. Existing cost-aware systems typically treat such failures as cascade decisions: try a cheap model first, then escalate hard cases to a stronger and more expensive model. In coding, however, execution feedback can also make further cheap-model recovery worthwhile, raising a budgeted deployment question: when should an agent spend more cheap compute, and when should it escalate? We formulate this post-failure decision as recovery routing over heterogeneous actions and train a supervised router from execution rollouts. To make the same router usable under changing budgets, we add a Conformal Risk Control (CRC) layer that selects a deployment-time cost penalty without retraining and provides marginal expected-cost control under exchangeability. Across held-out failures from five coding benchmarks, cheap recovery and escalation exhibit complementary success patterns. The calibrated frontier improves over fixed actions, prompt-only routers, and a binary cascade baseline; in the main GPT-5.4-nano/GPT-5.4 setting, one CRC-calibrated frontier point exceeds always-escalate solve rate while using 35% of its mean recovery cost. Code is available at this https URL.

---


### 241. [ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis](https://arxiv.org/abs/2607.19341)

**<font color=#1a73e8>作者：</font>** Yuan Wang, Yongchao Du, Mengting Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal generative models have enabled instruction-based image generation to move beyond semantic manipulation to knowledge-driven visual reasoning. However, these methods focus on explicit commonsense reasoning, shallow causal understanding, and direct knowledge recall, failing at knowledge-intensive generation. We develop \textbf{ExpertVerse}, a capability-centric benchmark to evaluate generative models via knowledge-intensive lens. ExpertVerse stratifies reasoning generation across an orthogonal taxonomy of \textit{9 cognitive capabilities} and \textit{8 expert disciplines}, yielding \textit{58 sub-disciplines}. We curate 1,611 expert-annotated instances covering single-image editing, multi-image composition, and text-to-image generation. We further develop an automated workflow to produce \textbf{ExpertVerse-100K}, a large-scale dataset with reasoning traces and knowledge-anchored rationale annotations. Based on this, we train \textbf{KnowThinker} with RL fine-tuning, a VLM reasoning engine with world knowledge that jointly generates thinking processes and refined instructions. Towards the cross-modal credit misalignment and multi-objective gradient conflicts in multi-reward optimization, we propose a tailored Bootstrapped Pareto Policy Optimization (BPPO), which synergizes Bootstrapping Reward Rectification (BRR) and Conflict-Aware Pareto Advantage Fusion (CPAF). Extensive results of both open-source and proprietary models exposes critical reasoning deficits, highlighting imperative for knowledge-intensive benchmarks towards next-generation visual generation.

---


> [!TIP]
> 当前位于：**201-241**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-241**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
