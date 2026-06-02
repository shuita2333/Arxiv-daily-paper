# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 151. [A Four-Tier Communication Architecture and Sim-to-Real Validation of a Graphical Open-Source Platform for Robotic Engineering Education](https://arxiv.org/abs/2606.00550)

**<font color=#1a73e8>作者：</font>** Thien Tran, Khang Duong, Minh Tran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The persistent challenge in scaling authentic manipulator education within university laboratories is a structural dichotomy: commercial digital twins are often cost-prohibitive and rigidly scripted, whereas open-source robotics middleware (ROS) imposes steep technical and syntax barriers for novices. To resolve this logistical and educational friction, this Work-in-Progress (WiP) paper proposes a scalable four-tier communication architecture tailored for sustainable robotic curricula. Rather than focusing on software application design, our study examines the underlying data exchange mechanisms required to bridge visual conceptual environments with physical robotic endpoints, utilizing the Graphical Open-Source Platform (GOSP) as a foundational instantiation. This WiP details the framework's technical integration of 3D visual armature modeling with a robust ROS middleware backend, emphasizing the serialization, routing, and encapsulation of intricate communication routines. Preliminary sim-to-real validation using multi-axis spatial trajectories confirms that encapsulating these communication pipelines provides a sufficient fidelity hardware-agnostic pathway. By bridging virtual design and physical execution, this architectural blueprint offers a viable infrastructure for engineering education.

---


### 152. [Improving Visual Grounding in Remote Sensing via Cluster-Guided Refinement and Model Ensemble Voting](https://arxiv.org/abs/2606.00556)

**<font color=#1a73e8>作者：</font>** Panav Shah, Geet Sethi, Ashutosh Gandhe  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding aims to locate image regions that correspond to natural language descriptions and is a key component of interpretable vision systems. In remote sensing imagery, grounding is particularly challenging due to complex scenes, small objects, and large variations in scale. Relying on a single model is often insufficient to address these diverse challenges. In this work, we propose two grounding pipelines, Sequential Grounding Refinement (SGR) and Cluster-Aware Grounding Refinement (CGR), that combine the complementary strengths of RemoteSAM, a visual grounding model specialized for remote sensing, and SAM3, a powerful general-purpose segmentation model. Our approach first uses RemoteSAM to obtain an initial estimate of object location, which is then refined using SAM3 to produce more accurate and spatially consistent segmentations. Additionally, we explore an ensemble strategy based on majority voting across six diverse grounding pipelines, each with distinct capabilities. This multi-model framework improves robustness and significantly enhances localization accuracy. Experimental results demonstrate that the proposed pipelines and ensemble approach outperform individual models, leading to more reliable and precise visual grounding predictions.

---


### 153. [Normalized Relevance Measure as a Unifying Framework to Explain Neural Network Latent Structures](https://arxiv.org/abs/2606.00557)

**<font color=#1a73e8>作者：</font>** Ping Xiong, Thomas Schnake, Grégoire Montavon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To understand how a neural network (NN) functions and makes predictions, it has become increasingly clear that analyzing only the input domain is insufficient -- one must also examine its internal inference mechanisms to capture the complete picture. To explain the internal inference mechanisms of such models, it is essential to analyze the importance of latent representations for a given task. In this paper, we propose the \emph{normalized relevance measure} (NRM) framework -- a novel general explanation procedure that attributes relevance to \emph{arbitrary sets of neurons across layers of arbitrary architectures}. In the NRM framework, relevance of selected neurons is explicitly defined as a normalized signed measure, constructed using simple operations -- marginalization and conditioning based on additive and multiplicative laws -- in analogy to the probability measures. The normalization property further guarantees comparability across layers. The NRM framework subsumes existing propagation-based explanation algorithms by explicitly identifying the underlying quantity being computed. We demonstrate the utility of the framework in computer vision applications, where joint relevance analysis across multiple layers reveals key information flows in VGG16 networks. Overall, the NRM framework provides a general, mathematically grounded approach to understanding how modern NNs propagate information, offering a versatile and broadly applicable foundation for explainable artificial intelligence.

---


### 154. [Semi-Supervised Noise Adaptation: Transferring Knowledge from Noise Domain](https://arxiv.org/abs/2606.00558)

**<font color=#1a73e8>作者：</font>** Yuan Yao, Jin Song, Huixia Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning aims to facilitate the learning of a target domain by transferring knowledge from a source domain. The source domain typically contains semantically meaningful samples (*e.g.*, images) to facilitate effective knowledge transfer. However, a recent study observes that the noise domain constructed from simple distributions (*e.g.*, Gaussian distributions) can serve as a surrogate source domain in the semi-supervised setting, where only a small proportion of target samples are labeled while most remain unlabeled. Based on this surprising observation, we formulate a novel problem termed *Semi-Supervised Noise Adaptation* (SSNA), which aims to leverage a synthetic noise domain to improve the generalization of the target domain. To address this problem, we first establish a generalization bound characterizing the effect of the noise domain on generalization, based on which we propose a Noise Adaptation Framework (NAF). Extensive experiments demonstrate that NAF effectively leverages the noise domain to tighten the generalization bound of the target domain, leading to improved performance. The codes are available at this https URL.

---


### 155. [Richer Representations for Neural Algorithmic Reasoning via Auxiliary Reconstruction](https://arxiv.org/abs/2606.00559)

**<font color=#1a73e8>作者：</font>** Jiafu Huang, Chao Peng, Chenyang Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural algorithmic reasoning has emerged as a popular research direction. It aims to train neural networks to mimic the step-by-step behavior of classical rule-based algorithms. More specifically, the execution of such algorithms can be abstracted as a sequence of states, where each state represents the intermediate outcome after an execution step. The training objective is to generate state sequences that replicate the underlying algorithmic process. A common framework for this task adopts an encoder-processor-decoder architecture, where the encoder learns representations of states, the processor simulates algorithmic steps, and the decoder reconstructs output states. While prior work has focused on improving the processor, the role of the encoder in representation learning has received little attention. Most methods rely on simple MLP encoders, raising the question of whether such representations are sufficiently informative for supporting algorithmic reasoning. This paper investigates how to improve encoder representations for neural algorithmic reasoning. We propose a reconstruction module that aims to recover the input state from its encoded representation. This auxiliary reconstruction task encourages the encoder to retain critical information about the input. We demonstrate that incorporating this task during training improves the performance of existing neural architectures on standard benchmarks. Furthermore, we observe that current encoders often underutilize the correlations among features within a state. To address this, we draw inspiration from self-supervised learning and design an enhanced variant of the auxiliary task that encourages the encoder to capture intra-state feature dependencies. Experimental results show that our method enables the encoder to learn richer representations, thereby enhancing the performance of existing processors on algorithmic reasoning tasks.

---


### 156. [Interpretable Policy Distillation for Power Grid Topology Control](https://arxiv.org/abs/2606.00561)

**<font color=#1a73e8>作者：</font>** Aleksandra Dmitruka, Karlis Freivalds  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (RL) offers a promising route to real-time power grid operation, yet large neural policies are costly to evaluate, hard to deploy on constrained hardware, and opaque to operators. We ask whether a Proximal Policy Optimization (PPO) agent for grid topology control can be compressed into compact tree-based surrogates without losing operational performance. A PPO teacher is trained on Grid2Op's standard 14-bus environment with a stability-oriented reward, using stress-focused data collection on critical, high-loading states. The policy is then distilled into a decision tree and a random forest. Across held-out validation episodes, both surrogates exceed the teacher in mean reward and survival length at a fraction of the inference cost. The decision tree shows high exact-action agreement with the PPO argmax and near-complete agreement within its top-ranked actions, while remaining small enough to be inspected directly. Feature-importance analysis reveals a representational shift: the PPO policy relies mainly on line-loading signals, while the distilled tree is driven primarily by bus-topology variables. These results suggest that stress-focused distillation can convert a black-box neural controller into a lightweight, auditable rule-like surrogate suited for real-time deployment, while also surfacing risks tied to deterministic actions and topology-specific generalization.

---


### 157. [DeepLatent: Think with Images via Parallel Latent Visual Reasoning](https://arxiv.org/abs/2606.00562)

**<font color=#1a73e8>作者：</font>** Dongchen Lu, Zhimo Li, Mao Shu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The emerging paradigm of "thinking with images" embeds visual states into intermediate reasoning steps, defining a new frontier for Vision-Language Models. Existing approaches diverge along two lines. Tool-assisted methods apply explicit visual operations but suffer from high latency and restricted manipulation types. Latent reasoning methods autoregressively produce implicit visual states, but underperform tool-assisted methods, and their latent tokens fail to capture effective visual information. In this work, we propose DeepLatent, a parallel framework for latent visual reasoning. First, we introduce LatentFormer. It uses learnable 2D tokens to generate context-conditioned latent states in parallel, anchoring every visual update directly in the original image features. Second, we design a continuous-space reinforcement learning algorithm. It optimizes latent modulation parameters directly in the embedding space, significantly improving latent representation quality. The framework is trained via knowledge distillation followed by this continuous-space RL algorithm. Furthermore, we contribute DeepLatent-180K, a large-scale dataset tailored for latent visual reasoning. Extensive evaluations across multiple benchmarks demonstrate that DeepLatent achieves state-of-the-art performance.

---


### 158. [A Practical Upper Bound on Selection Bias Effects in Medical Prediction Models](https://arxiv.org/abs/2606.00563)

**<font color=#1a73e8>作者：</font>** Kara Liu, Maggie Wang, Russ B. Altman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selection bias is a common and often unavoidable aspect of real-world data that challenges the generalizability of machine learning models. When models trained on biased data are deployed in the broader target population, poor model generalization may lead to real harm, particularly in high-risk settings such as healthcare. This risk highlights the need for practitioners to reliably assess model generalizability prior to deployment. However, existing methods for predicting model performance rely on unrealistic access to the target distribution or knowledge of the selection mechanism causing bias. To address these limitations, we propose a novel upper bound on the worst-case model performance on the target population under the realistic setting where the selection mechanism and the target population data are only partially observed. We demonstrate the validity and practical utility of our method through experiments on fully synthetic data, semi-synthetic data derived from the All of Us Research Program, and real-world selection bias in MIMIC-IV. Our work offers a principled and practical tool to estimate the impact of selection bias in an otherwise intractable setting, thereby enabling practitioners to build safer and more generalizable models in healthcare and beyond.

---


### 159. [On the Recoverability of Causal Relations from Bulk Gene Expression Data](https://arxiv.org/abs/2606.00568)

**<font color=#1a73e8>作者：</font>** Gongxu Luo, Boyang Sun, Kun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bulk gene expression profiling, which aggregates pooled RNA across cells within a biological sample, remains important in the single-cell era because it is typically less noisy, more sensitive, and more cost-effective than single-cell assays. Accordingly, a growing body of computational methods seeks to recover causal relations among genes from bulk expression data. However, aggregation is a lossy, non-invertible coarsening of the underlying cellular system, and it remains unclear whether and under what conditions causal relations are recoverable from aggregated bulk gene expression data. To answer this, we formalize recoverability under aggregation through two notions of consistency: functional-form consistency and conditional-independence consistency. We then derive necessary and sufficient conditions for recoverability, showing that these properties are preserved only under linear aggregations (e.g., sum/mean) coupled with affine structural equations. To assess the practical plausibility of these conditions, analyses of four bulk and four single-cell gene expression datasets further reveal that the estimated pairwise regulatory functions among genes deviate from linearity in both data types, providing limited empirical support for the linearity assumptions required for recoverability. Together, these results caution against recovering causal relations from aggregated bulk expression data without strong additional assumptions.

---


### 160. [On the Difficulty of Learning a Meta-network for Training Data Selection](https://arxiv.org/abs/2606.00571)

**<font color=#1a73e8>作者：</font>** Zilin Du, Junqi Zhao, Boyang Albert Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data are increasingly used to train neural networks, yet distributional mismatch with real data limits their effectiveness when used indiscriminately. A common strategy is to learn data weights via bi-level optimization, which we refer to as Meta-learning for Training-data Selection (MTS). Interestingly, in practice, MTS often performs below expectation. We identify two obstacles in properly training MTS: a poor gradient signal-to-noise ratio (GSNR), which causes optimization difficulties, and lack of informative features that correlates with data quality. We present a mathematical analysis of MTS, which reveals the dynamics of normalized data weights and the relation between disparate data quality and poor GSNR. The analysis suggests a a simple yet effective solution: increasing the batch size. Further, we propose a set of informative features that capture the positions of training data in their distributions and training dynamics. Experiments across four benchmarks show consistent improvements, achieving average gains of 5.49% over training without selection and 2.89% over the strongest baseline.

---


### 161. [Spatiotemporal Multi-Task Graph Transformer for Trip-Level Transit Prediction](https://arxiv.org/abs/2606.00572)

**<font color=#1a73e8>作者：</font>** Oluwaleke Yusuf, Adil Rasheed, Frank Lindseth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Passenger count data from public transit systems reveals urban mobility patterns and is essential for planning, operation, and optimisation. However, non-linear spatiotemporal interdependencies across stops and lines make modelling and prediction challenging. Existing approaches often rely on fixed temporal, spatial, or stop-level formulations, limiting their ability to capture within-trip evolution and network context. This study proposes SMT-GraphFormer, a spatiotemporal multi-task graph transformer that frames trip-level transit prediction as sequence-to-sequence modelling. Given a line's stop sequence and trip-level context, the model predicts successive boarding and alighting counts, with delay and dwell time treated as encoder-side surrogate tasks. Key components include graph embeddings for multi-relational stop similarity, a context encoder for weather and temporal information, and a multi-gate mixture-of-experts module that produces task-specific decoder representations for boarding and alighting predictions. Evaluation on public bus transit data from Trondheim, Norway, shows that SMT-GraphFormer outperforms stop-level tabular benchmarks, with ablation studies examining each component's contribution. The sequential formulation yields substantial gains on alighting prediction ($+$0.24 in $R^2$) and consistent improvements on boarding, delay, and dwell, confirming the value of explicit trip-level sequential bias and inter-target dependencies. These findings demonstrate the potential of transformer-based sequence modelling for capturing complex spatiotemporal dynamics in public transit and underscore the value of architectures tailored to transit data rather than off-the-shelf tabular models. The proposed framework provides a horizon-agnostic basis for scenario analysis in digital twin environments, supporting informed decision-making by planners and transit operators.

---


### 162. [Sandboxed Coding Agents are Competitive Omni-modal Task Solvers](https://arxiv.org/abs/2606.00579)

**<font color=#1a73e8>作者：</font>** Dongping Chen, Xuanao Huang, Zhihan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As multimodal LLMs increasingly target video and audio, it is often assumed that such tasks require native omnimodal models. We show that this is not always the case: coding agents with only text+image access and a sandboxed tool-use interface can match, and in several settings outperform, SOTA native omnimodal models and predefined multimodal agent scaffolds across multiple audio-video benchmarks. Our trajectory analysis suggests that their strength comes from writing code and orchestrating tools to extract relevant evidence from transcripts, frames, and other modality signals, thereby converting omnimodal tasks into retrieval and information-processing problems rather than ingesting entire media streams. We further characterize their limitations through a failure taxonomy and process-level trace analysis, and show that simple skill injection, including human-written and self-distilled skills, substantially improves performance. To explore open-source elicitation, we introduce Code-X, a training recipe with the OmniCoding trajectory dataset and verifiable reward, and provide baselines on Qwen-3.5-9B and Qwen-3.6-27B. Finally, we argue that the next frontier is many-modality processing, and introduce TerminalBench-O, a process-level benchmark for real-world omnimodal processing tasks. Code will be available at this https URL.

---


### 163. [Looped Transformers with Layer Normalization Provably Learn the Power Method](https://arxiv.org/abs/2606.00605)

**<font color=#1a73e8>作者：</font>** Lyumin Wu, Chenyang Zhang, Yuan Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have achieved remarkable success across a wide range of applications, and a growing body of work suggests that part of their strength comes from their ability to learn and execute algorithmic procedures. However, our understanding of how transformers learn such algorithms remains limited, especially in the presence of layer normalization (LN). In this work, we study principal component prediction as a concrete testbed for understanding the training dynamics of transformers with LN. We prove that a looped linear transformer with LN, trained by gradient descent, converges to a solution that implements the power method, with each self-attention layer performing one power iteration. Notably, the model is trained only for principal component prediction, rather than being explicitly supervised to implement the power method. Our finding thus reveals an "algorithmic implicit bias" of looped transformers with LN: principal-component prediction can in principle be achieved by many mechanisms, yet gradient descent selects one that realizes the power method. We further provide a concrete comparison between transformers with and without LN: even with layerwise guidance from power iterations, a transformer without LN cannot exactly learn the power method, whereas the corresponding transformer with LN can, leading to a provable performance gap in principal component prediction. Our results provide, to our knowledge, the first theoretical analysis of the training dynamics of looped and single-layer transformers with LN, and shed light on the role of LN in transformer models.

---


### 164. [FiSeR: Fine-Grained Source Representations for Cross-Domain AI Image Detection](https://arxiv.org/abs/2606.00606)

**<font color=#1a73e8>作者：</font>** Shan Zhang, Yongxin He, Mingming Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world synthetic image detectors often generalize poorly under domain shift despite strong in-domain performance. Using unsupervised UMAP projections, we find that natural and synthetic features remain partially separable on unseen datasets, yet performance still drops, suggesting that the classification head overfits to training-domain artifacts. Therefore, the key is to learn more transferable representations so that the decision criterion is more stable and robust to domain shifts. Based on the structural fact that synthetic images are produced by diverse generators, we propose a hierarchical contrastive learning framework that improves the separability between natural and synthetic images while preserving generator identity information. It jointly optimizes (i) a coarse contrastive objective between natural and synthetic images and (ii) a fine contrastive objective among synthetic images using generator identities. Trained on WildFake, our method achieves an average AUROC gain of +10.22 on cross-domain evaluation over Chameleon, AIGIBench, Community Forensics, and GenImage under the same settings as the strong baseline DIRE. For few-shot adaptation, we freeze the backbone and fit an SVM head on 10 labeled samples per class, improving AUROC by +10.64 on AIGIBench and +17.41 on Chameleon, averaged over 12 widely used detectors. Our code is publicly available at: this https URL.

---


### 165. [CARE-RL: Capability-Aware Reinforcement Learning for Mitigating Cross-Domain Conflicts](https://arxiv.org/abs/2606.00609)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Xinle Wu, Yao Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) with verifiable rewards has achieved strong progress in reasoning-oriented LLMs, but extending it to multi-domain RL remains challenging due to reward unreliability in non-verifiable tasks and capability interference across domains. We propose CARE-RL to combine protocol-aware reward generation with capability-aware optimization for mitigating cross-domain conflicts. For non-verifiable tasks, the Protocol-Aware Generative Reward Model (PA-GRM) constructs prompt-level evaluation protocols and schemas before producing trace-conditioned rewards, enabling task-adaptive yet comparable evaluation of open-ended responses. For multi-domain optimization, Direction-Aware Capability Subspace Projection (DACSP) extracts historical capability directions from previous RL stages and modulates later updates by amplifying aligned components, suppressing conflicting components, and preserving orthogonal updates. Experiments across math, chat, and instruction-following benchmarks show that CARE-RL consistently outperforms standard multi-domain RL baselines, achieving Total Avg scores of 47.9 and 50.7 on Qwen2.5-7B and Qwen3-4B, respectively.

---


### 166. [TRACE: Trajectory Risk-Aware Compression for Long-Horizon Agent Safety](https://arxiv.org/abs/2606.00611)

**<font color=#1a73e8>作者：</font>** Zhepei Hong, Lin Wang, Liting Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents produce safety evidence across long trajectories, where sparse, delayed, and compositional risk signals often escape local moderation. Existing turn-level or short-context detectors struggle to reliably retain and aggregate such evidence over extended horizons. We reframe long-horizon agent safety detection as trajectory-level evidence compression and propose Trajectory Risk-Aware Compression for Long-Horizon Agent Safety (TRACE). TRACE uses a Compressor-Reader design: the Compressor encodes the full trajectory into a compact latent evidence state under trajectory-level supervision, and the Reader judges the raw trajectory with this latent evidence state as a safety reference. This design helps aggregate dispersed risk cues and reduce premature evidence loss. Across ASSEBench, Pre-Ex-Bench, and R-Judge, TRACE achieves the best accuracy on all evaluated backbones, improving over strong baselines by up to 12.6 percentage points. On LongSafety, TRACE shows smaller performance degradation as context length grows. Attention visualizations and case studies suggest that the compressed reference helps the Reader focus on risk-critical segments and recover cross-step evidence. Code is available at this https URL.

---


### 167. [Efficient Test-time Inference for Generative Planning Models](https://arxiv.org/abs/2606.00618)

**<font color=#1a73e8>作者：</font>** Robert Gieselmann, Mihai Samson, Federico Pecora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models have emerged as a powerful paradigm for AI planning, yet their performance remains constrained by the training data distribution. One approach is to improve generated solutions during inference by scaling test-time compute. A more efficient alternative is to optimize the inference process itself. In this paper, we show that a modified version of a classical Open-Closed List (OCL) search provides just such an efficient inference procedure. Our algorithm synergizes two learned components: a generative model that performs fast rollouts from intermediate states and a heuristic model that prioritizes among candidate reasoning paths. Key contributions include novel exploration control mechanisms and integration of learned models within the OCL framework. Across multiple combinatorial planning domains, our approach outperforms both neurosymbolic search baselines and classical solvers in computational efficiency and solution quality.

---


### 168. [FlowNar: Scalable Streaming Narration for Long-Form Videos](https://arxiv.org/abs/2606.00620)

**<font color=#1a73e8>作者：</font>** Zeyun Zhong, Manuel Martin, Chengzhi Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Large Multimodal Models (LMMs), primarily designed for offline settings, are ill-suited for the dynamic requirements of streaming video. While recent online adaptations improve real-time processing, they still face critical scalability challenges, with resource demands typically growing at least linearly with video duration. To overcome this bottleneck, we propose FlowNar, a novel framework for scalable streaming video narration. The core of FlowNar is a dynamic context management strategy for historical visual context removal, combined with our CLAM (Cross Linear Attentive Memory) module for streaming visual history retention, ensuring bounded visual memory usage and computational complexity, crucial for efficient streaming. We also introduce a realistic self-conditioned evaluation protocol and complementary evaluation metrics to assess streaming narration models under deployment-like conditions. Experiments on the Ego4D, EgoExo4D, and EpicKitchens100 datasets demonstrate that FlowNar substantially improves narration quality over strong baselines while being highly efficient, supporting processing of 10$\times$ longer videos and achieving 3$\times$ higher throughput (FPS). The code is available at this https URL.

---


### 169. [Authenticity Debt and the Synthetic Content Threat Landscape: A Layered Framework for Trust, Provenance, and IP Governance in the Generative AI Era](https://arxiv.org/abs/2606.00621)

**<font color=#1a73e8>作者：</font>** Shubhashis Sengupta, Benjamin McCarty, Milind Savagaonkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence has fundamentally changed how content is now produced. It has enabled how high-fidelity text, images, audio, and videos are created, modified, and redistributed at near-zero marginal cost. This shift exposes enterprises and ecosystems to a number of risks across four reinforcing authenticity layers -- authenticity, provenance, integrity, and accountability -- that traditional controls are inadequate to address in isolation. We introduce the concept of authenticity debt: the cumulative institutional liability that accumulates when organizations deploy AI-generated content without preserving verifiable origin, integrity, and accountability, deferring exposure that surfaces under regulatory, legal, or market scrutiny. This paper presents a comprehensive, multi-dimensional taxonomy of generative AI harms and attack vectors, surveys the capabilities and failure modes of technical controls including digital watermarking, provenance frameworks (C2PA, Adobe CAI), and detection technologies, and argues that no single mechanism is sufficient in open, adversarial, and evolving environments. Drawing on Zero Trust Architecture principles and enterprise governance frameworks, we propose a layered reference architecture that integrates cryptographic provenance, human-in-the-loop verification, and continuous governance to sustain defensible authenticity at scale. We further examine the regulatory landscape (EU AI Act, U.S.\ FTC, NIST AI RMF) and identify practical guiding principles for organizations seeking to build authenticity as institutional infrastructure rather than an afterthought.

---


### 170. [NICE: A Framework for Declarative and Machine-Checkable Vulnerability Reproduction](https://arxiv.org/abs/2606.00625)

**<font color=#1a73e8>作者：</font>** Minh-Luân Nguyen, Olivier Levillain, Julien Malka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reproducing software vulnerabilities is fundamental to security researchers, open-source maintainers, and educators. Yet, vulnerabilities remain hard to reproduce today, and even when they can be reproduced, recreating a software environment where the vulnerability can be exploited becomes harder and harder over time. We present NICE, the NIx CvE reproduction framework, which uses declarative recipes to build and automatically validate vulnerable environments. In NICE, a reproduced CVE comprises one or more NixOS virtual machine configurations, a scripted exploitation scenario, and machine-checkable assertions that provide factual evidence of exploitation. This design facilitates sharing, validation, review, and long-term reproducibility.
We evaluate NICE on 19 diverse real-world CVEs spanning multiple CWE categories, attack vectors, and target types (user-space, system software, kernel, and graphical applications). We show that NICE allows to produce concise recipes and integration tests that reproduce vulnerable environments and provide proofs of exploitation.
NICE is applicable to security education and training (e.g., creating cyber ranges), but also to vulnerability reporting, where its reproducibility and reviewability properties can make reports easier to audit and verify.

---


### 171. [Robust Reasoning via Dynamic Token Selection for Distribution-Aligned Self-Distillation](https://arxiv.org/abs/2606.00628)

**<font color=#1a73e8>作者：</font>** Ruiqi Zhang, Lingxiang Wang, Hainan Zhang Zhiming Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-distillation improves learning efficiency by rewriting reference answers as training data that better matches the model's own distribution. However, reference answers also introduce strong stylistic biases, causing the generative model to imitate surface forms rather than learn useful reasoning patterns. We observe that the rewriting data contains a large number of high-perplexity (PPL) tokens, coming from two distinct sources: beneficial knowledge-enhancing logical corrections, and harmful stylistic drift induced by reference imitation. Treating all such tokens equally can disrupt the base model's original distribution and degrade performance, especially on difficult reasoning tasks. To address this, we propose Distribution-Aligned Self-Distillation (DASD), which uses an answer-aware reference model to generate candidate tokens and dynamically filters them according to the base model's confidence. DASD preserves tokens that encode useful logical knowledge while suppressing distributionally misaligned style noise. Experiments on math, code, and commonsense reasoning benchmarks show that DASD consistently outperforms competitive baselines, reduces high-PPL tokens, and improves robustness across tasks of varying difficulty.

---


### 172. [A Systematic Benchmark of Intraoperative Ultrasound-to-MR Synthesis for Brain Tumour Surgery](https://arxiv.org/abs/2606.00630)

**<font color=#1a73e8>作者：</font>** Olga Esteban-Sinovas, Santiago Cepeda, Ignacio Arrese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intraoperative ultrasound (ioUS) is a versatile, cost-effective modality in brain tumour surgery, but its interpretation is difficult: acquisition planes are non-standard, artefacts are modality-specific, and its appearance differs markedly from the preoperative MRI on which surgical-planning tools, segmentation models and the surgeon's experience rely. Synthesising MRI-like images from ioUS could let this MRI-based infrastructure be reused intraoperatively without an extra scan. Most prior work evaluates a single architecture in isolation; to our knowledge, no benchmark has spanned architectural paradigms, inference regimes and downstream-task endpoints under a common protocol. We address this gap on the public ReMIND data set (76 patients; 153 paired ioUS/T2w and 104 paired ioUS/FLAIR studies; 60/16 patient-level train/held-out split). Six generators (four GAN baselines: Pix2Pix, SwinPix2Pix, CycleGAN, CUT; the transformer-augmented ResViT; and the few-step diffusion model SynDiff) were each trained under four inference regimes (2D, 2.5D, 2D + 3D-refinement, full-3D) and two targets (T2w only; T2w + FLAIR multi-task), yielding 48 experiments. Image-fidelity metrics (SSIM, PSNR, MAE, LPIPS) were complemented by an nnU-Net v2 downstream segmentation evaluation (tumour and resection cavity) and by subgroup analyses by histological grade and reoperation. No architecture dominated every axis, and, critically, perceptual quality tracked downstream utility most closely (LPIPS, r=-0.66, p<0.001), whereas higher SSIM was associated with worse utility (r=-0.64, p<0.001); SynDiff-2.5D best preserved downstream segmentation (U_Dice=0.55). Perceptual and downstream-task metrics should therefore be reported alongside or in preference to global SSIM, and architecture choice conditioned on surgical phase, patient history and clinical objective.

---


### 173. [French parsing enhanced with a word clustering method based on a syntactic lexicon](https://arxiv.org/abs/2606.00634)

**<font color=#1a73e8>作者：</font>** Anthony Sigogne, Matthieu Constant, Eric Laporte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article evaluates the integration of data extracted from a French syntactic lexicon, the Lexicon-Grammar (Gross, 1994), into a probabilistic parser. We show that by applying clustering methods on verbs of the French Treebank (Abeillé et al., 2003), we obtain accurate performances on French with a parser based on a Probabilistic Context-Free Grammar (Petrov et al., 2006).

---


### 174. [How Neural Losses Shape VAE Latents](https://arxiv.org/abs/2606.00635)

**<font color=#1a73e8>作者：</font>** Giorgio Strano, Luca Cerovaz, Michele Mancusi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern VAEs are rarely trained with the pointwise likelihood implied by the standard $\beta$-VAE objective. In practice, pointwise reconstruction is often combined with perceptual and adversarial losses, despite a lack of understanding of how this changes the latent dynamics of the model. We show that the choice of reconstruction loss reshapes the rate-distortion problem itself, altering both the information content and the geometry of the learned latent space in ways that may be invisible from reconstructions alone. First, we prove and verify empirically that augmenting pointwise reconstruction with neural terms, such as perceptual and adversarial objectives, reduces the amount of information stored in the latent representations. Second, we show that neural reconstruction losses systematically change the geometry of the latent space: they make representations more isotropic and distribute uncertainty more evenly across latent dimensions, producing different posterior variance profiles. These findings highlight how the rate-distortion tradeoff is not a comprehensive lens to understand the behavior of VAEs, and we propose a more mechanistic approach to investigate how the choice of a distortion metric reshapes the optimization problem.

---


### 175. [An Attribute-Based Measure of Video Complexity](https://arxiv.org/abs/2606.00640)

**<font color=#1a73e8>作者：</font>** Aditya Sarkar, Yi Li, Zihao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A new framework for the estimation of the complexity posed by video-question pairs to video-LLMs, Video Attribute-Based Complexity (VideoABC), is proposed. Video complexity is defined as the probability of failure of a video-LLM for a given video-question pair. VideoABC is a non-parametric complexity measure, using a reference video dataset and a pre-defined vocabulary of video attributes informative of complexity, \eg the scene complexity or the speed of the video event informative of the question. In a training phase, reference videos are projected into the space of these attributes, which is then quantized. The expected ABC of each quantization cell is then computed. Given a new video and its projection into the attribute space, complexity is estimated by the expected ABC of the associated quantization cell. To enable the use of VideoABC with small reference video datasets, two quantizers are combined: a k-means quantizer that enables accurate complexity estimates for samples in the distribution of the reference dataset and a universal lattice quantizer that guarantees generalization to out-of-distribution samples. A synthetic video generation procedure, inspired by target-distractor manipulations of psychophysics studies, is proposed to populate the cells of the lattice quantizer during training, enabling the computation of their expected ABCs. Experimental results show that VideoABCis effective even with very low-dimensional attribute representations, substantially outperforming approaches like `video-LLM as judge' with much less complexity. Finally, the explainable nature of the VideoABC score, in terms of well-defined attributes, is shown to provide insights on how the attribute composition of benchmarks affects their complexity.

---


### 176. [Demystifying the Optimal Fair Classifier in Multi-Class Classification](https://arxiv.org/abs/2606.00656)

**<font color=#1a73e8>作者：</font>** Li Zhang, Yuyuan Li, XiaoHua Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring fair and equitable treatment across diverse groups, particularly in multi-class classification tasks, poses a significant challenge due to the persistent biases inherent in machine learning models. Most existing bias mitigation techniques are tailored to binary settings, and the presence of multi-dimensional outputs and complex fairness mechanisms makes their extension to multi-class scenarios neither straightforward nor effective. In this paper, we investigate two fundamental, unresolved challenges in fair classification: (i) characterizing the optimal accuracy-fairness frontier in multi-class settings, and (ii) designing practical algorithms that attain this optimum in different training phases. To tackle these challenges, we first specify an analytically tractable probabilistic formulation of the optimal classifier under fairness constraints. Building upon this, we propose two attribute-blind algorithms to enforce fairness requirements in practice: an in-processing approach for fairness intervention during training via the reduction approach, and a post-processing approach for fine-tuning output probabilities with plug-in estimation. Theoretical analysis reveals that both methods converge to the optimal accuracy-fairness Pareto frontier. Experiments conducted on multiple datasets demonstrate the superior performance of our methods in balancing accuracy and fairness.

---


### 177. [Collaborative Few-Step Distillation and Low-Bit Quantization for Wan2.2 Dual-Expert Video Diffusion Models](https://arxiv.org/abs/2606.00658)

**<font color=#1a73e8>作者：</font>** Jinyang Du, Shenghao Jin, Ziqian Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large video diffusion models achieve strong visual quality but remain expensive to deploy because each sample requires many denoising steps and a large resident parameter footprint. This paper studies a deployment-oriented compression pipeline for Wan2.2-T2V-A14B by combining few-step distribution-matching distillation with low-bit quantization. The pipeline follows the model's dual-expert denoising route, calibrates the high-noise and low-noise branches separately, protects sensitive entrance layers, and uses HiF4-style low-bit representation to improve dynamic-range coverage. Quantization is calibrated on the distilled few-step student rather than on the original long-step trajectory, reducing activation-distribution mismatch during inference. The proposed co-design keeps the quantized model close to the same-step full-precision model and surpasses the original full-precision baseline at 8 and 20 steps on average. The 20-step setting gives the best quality-efficiency trade-off in the tested configurations.

---


### 178. [TAP-JEPA: Frozen Future-Latent Probing and Two-Stage Score Fusion for EPIC-KITCHENS-100 Action Anticipation](https://arxiv.org/abs/2606.00662)

**<font color=#1a73e8>作者：</font>** Chaoyang Wang, Lexuan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents TAP-JEPA, our runner-up submission to the EPIC-KITCHENS-100 (EK-100) Action Anticipation Challenge at EgoVis 2026. The task is to anticipate the next verb, noun, and verb-noun action from an egocentric clip that ends before the target action begins. Instead of fine-tuning a large video backbone, TAP-JEPA builds a compact anticipation model on frozen V-JEPA 2.1 features: a ViT-G/384 encoder extracts visible pre-action tokens, the pre-trained latent predictor estimates near-future tokens from the observed context, and both token groups are fused by attentive probes with task-specific queries for verbs, nouns, and action pairs. For the final submission, we expand supervised training with the official training split and most of the validation split, reserving a small subset for sanity checks and qualitative inspection, and adopt a two-stage score fusion that first averages eight independently initialized probe replicas within each epoch and then merges candidates from epochs 12-20 with field-dependent weights. On the official open-testing leaderboard, our sunshinesky entry achieves 27.91 percent overall action Mean Top-5 Recall (MT5R), ranking second and only 0.04 percentage points behind the top score.

---


### 179. [AXIOM: A Trust-First Neuro-Symbolic Execution Architecture for Verifiable Mathematical Reasoning](https://arxiv.org/abs/2606.00671)

**<font color=#1a73e8>作者：</font>** Alessio Bruno  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AXIOM, a trust-first neuro-symbolic execution architecture for natural-language mathematical reasoning. In AXIOM, the language model functions strictly as a canonicalizer: it rewrites informal problem text into a narrow schema consumed by a deterministic Computer-Algebra-System (CAS) pipeline, which derives and verifies the answer or abstains as a first-class output. Routing follows a 1:1:1 alignment between problem-shape regex, schema-specific prompt, and closed-form CAS handler, with 3,100+ such routes shipped and zero LOST_CORRECT regressions across 250+ consecutive ship commits. We report empirical results on 4 MATH categories with a cumulative correctness of 94.36% (2,592/2,747) at 100.00% trust on parseable (zero confident-wrong answers across the full 2,747-record benchmark), all four domains above the per-domain 70/90/70 floor with per-domain trust at 100.0%, and median latency of 1 ms on rule-only handlers (88% of records on the lm-eval arithmetic 20,000-record benchmark). The architecture has served ~30,000 production queries through a public deployment. The contribution we emphasize is not a final accuracy figure but the forward dynamic the architecture establishes: every logged abstain in production is a candidate correct after one ship cycle, since new tasks compose without regressing the registry. The operational discipline behind this property -- math-template bucketing, LOST_CORRECT scan as regression oracle, parseable-first onboarding, and abstain as first-class output -- constitutes a transferable framework for trustworthy neuro-symbolic systems beyond mathematics.

---


### 180. [Medication-Aware Financial Exploitation Detection for Alzheimer's Patients Using Edge-Aware Interaction Risk Modeling](https://arxiv.org/abs/2606.00672)

**<font color=#1a73e8>作者：</font>** Farzana Akter, Lisan Al Amin, Rakib Hossain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial exploitation is a growing concern for people with Alzheimer's disease, especially during periods of reduced cognitive stability. Conventional fraud detection systems usually rely on financial behavior alone and ignore clinically relevant factors that may alter vulnerability. This paper proposes a medication-aware framework that synchronizes medication adherence with transaction-level monitoring to improve detection of cognitively risky financial events. A hybrid simulation dataset was constructed for 180 patients across 45 days, producing 8,100 medication records and 30,855 transactions. The framework evaluates amount anomaly, vendor novelty, transaction frequency, time deviation, and medication adherence through financial-only, additive medication-aware, and interaction-aware logistic models. Results show that the financial-only baseline obtained the highest global F1-score of 0.5000, but the interaction-aware model improved recall during medication-induced vulnerability windows from 0.7442 to 0.9070 and achieved the highest average precision for ranked high-risk cases. The findings suggest that medication adherence is most useful as a contextual modifier of financial risk rather than as an isolated predictor.

---


### 181. [T-CLIP: Enabling Thermal Perception for Contrastive Language-Image Pretraining](https://arxiv.org/abs/2606.00673)

**<font color=#1a73e8>作者：</font>** Tayeba Qazi, Ayush Maheshwari, Prerana Mukherjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal imaging offers a powerful alternative to visible-spectrum vision under challenging conditions such as low illumination and adverse weather, yet foundational vision-language models like CLIP fail to align thermal images with textual descriptions due to a fundamental thermal perception gap. We identify three major challenges: the lack of captioned thermal datasets, the inability of standard LLMs to reason about thermal phenomena, and a key representational challenge in thermal imaging where global scene context and object-level heat signatures conflict when learned together in a single embedding space. To address these, we introduce IR-Cap, the first physics-aware thermal captioning pipeline and dataset providing complementary global and fine-grained thermal descriptions across three public benchmarks, and T-CLIP, a decoupled dual-LoRA framework that independently adapts CLIP for scene-level and object-level thermal understanding. T-CLIP achieves consistent improvements over all baselines across three thermal benchmarks in cross-modal retrieval, and we provide an exploratory demonstration of its applicability to text-conditioned thermal image generation.

---


### 182. [Mapping the evolution of small reservoirs in Brazil from 1984 to 2025 using deep learning](https://arxiv.org/abs/2606.00675)

**<font color=#1a73e8>作者：</font>** Kylen Solvik, Luis Gustavo Carvalho, Marcia N. Macedo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Water research in Brazil largely overlooks the widespread damming of small streams for agricultural uses such as watering cattle, farm-scale hydropower, irrigation, and aquaculture. These ubiquitous dams and their reservoirs can alter water temperature, stream connectivity, aquatic habitats, greenhouse gas emissions, and evaporative water losses. Mapping small reservoirs is challenging because it requires reliably detecting small water bodies and distinguishing artificial reservoirs from natural lakes. As a result, most regional and global datasets exclude them. To address this gap, we trained a deep learning computer vision model to accurately segment small ($< 1 km^2$), stream-fed, surface water reservoirs in Brazil leveraging data from Landsat 5-9. Applying our model from 1984 to 2025, we created annual reservoir maps for the entire country to evaluate how their count, size, and distribution have changed over time. The number of detected reservoirs grew nearly fourfold from 263,913 to 996,245, while their total surface area increased from 3510 $km^2$ to 8550 $km^2$. To our knowledge, this is the first country-wide annual dataset representing the evolution of small reservoirs over four decades. The publicly available annual maps highlight the extent and cumulative impacts of the small stream impoundments across Brazil, providing actionable insights for managing freshwater ecosystems and water resources.

---


### 183. [A Modelling and Evaluation Framework for EuroCrops-Driven Sentinel-2 Crop Segmentation](https://arxiv.org/abs/2606.00676)

**<font color=#1a73e8>作者：</font>** Alexandra Nicoleta Scarlat, Ioana Cristina Plajer, Alexandra Baicoianu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a configurable pipeline for generating semantic-segmentation-ready agricultural datasets from Sentinel-2 imagery and EuroCrops parcel-level annotations. The workflow transforms heterogeneous vector crop annotations into aligned multispectral image--mask pairs through label harmonization, Sentinel-2 product selection, spatial alignment, rasterization, patch extraction, quality filtering, and class-aware sample selection. The generated dataset contains 67,337 patches from five European countries and uses a reduced taxonomy of ten crop classes plus background.
A four-level U-Net with Group Normalization was trained using 10 Sentinel-2 spectral bands and a composite loss combining class-weighted cross-entropy and Dice loss. On the internal EuroCrops-based test split, the model achieved a mean Intersection over Union (mIoU) of 0.7665, a pixel accuracy of 0.8693, and a mean class accuracy of 0.9072. Compared with spectral and spatial-context Random Forest baselines, the U-Net showed the importance of learned multi-scale spatial representations for crop segmentation.
External evaluation was performed on unseen Belgian EuroCrops subsets, DACIA5, and PASTIS. The results show a clear performance gap under external and cross-dataset evaluation, especially for benchmarks with different taxonomies, annotation protocols, spatial coverage, or temporal organization. The model transfers more reliably to dominant and taxonomically aligned classes such as maize and wheat, while performance remains limited for several minority classes and for the adapted single-date PASTIS setting. These findings highlight both the potential and the limitations of using EuroCrops-derived supervision for Sentinel-2 crop segmentation under realistic domain shifts.

---


### 184. [Limits of Resolution Equivariance in Fourier Neural Operators](https://arxiv.org/abs/2606.00677)

**<font color=#1a73e8>作者：</font>** Alex Colagrande, Paul Caillon, Eva Feillet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fourier Neural Operators are often assumed to generalize across spatial resolutions, enabling training on a coarse grid and deployment on a finer grid. We test this assumption by contrasting two inference-time choices when moving from training resolution $s$ to test resolution $S>s$: running FNO directly at $S$, or running at $s$ and upsampling the prediction to $S$ via Fourier zero-padding. On Darcy flow, we observe that direct fine-grid inference is not reliably beneficial and can be worse than the low-grid-plus-upsampling baseline. We further analyze layerwise spectra and find that, under Fourier truncation, intermediate representations increasingly concentrate energy in low frequencies, with high-frequency output produced mainly by late nonlinear/decoder stages. This offers a mechanistic explanation for why FNO can perform well while retaining few modes, yet remain sensitive under resolution shifts. Our findings highlight a simple but strong baseline for cross-resolution evaluation and point to nonlinear aliasing as a key obstacle to zero-shot resolution equivariance.

---


### 185. [Regularized Offline Policy Optimization with Posterior Hybrid Bayesian Belief](https://arxiv.org/abs/2606.00680)

**<font color=#1a73e8>作者：</font>** Hongqiang Lin, Pengfei Wang, Nenggan Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) aims to optimize policies from pre-collected datasets. A bottleneck of this paradigm is managing epistemic uncertainty, which arises from limited data coverage (sample-level) and the ambiguity in identifying transition dynamics from finite data (model-level). To provide a unified quantification of these uncertainties, Bayesian RL has been proposed by treating the dynamics model as a random variable and maintaining a corresponding belief. Despite its theoretical appeal, policy optimization in Bayesian RL remains computationally challenging as it requires solving composite objectives with expectations. Prior methods either employ search-based techniques with poor computational scalability or impose restrictive posterior assumptions that sacrifice the adaptability of Bayesian RL. To address these limitations, we propose Posterior Hybrid Bayesian Belief (PhyB), which reformulates the expectation as a convex combination over a subset of dynamics models. Theoretical analysis demonstrates that the objective discrepancy induced by this approximation remains bounded. Based on PhyB, we develop an iterative regularized policy optimization algorithm that provides metric-agnostic guarantees for monotonic improvement until convergence. Empirical results demonstrate that PhyB achieves state-of-the-art performance on various benchmarks.

---


### 186. [Prior-Guided Multi-Omic Transformers for Single-Cell Gene Regulatory Network Inference](https://arxiv.org/abs/2606.00685)

**<font color=#1a73e8>作者：</font>** Tianyang Xu, Tianci Liu, Niraj Rayamajhi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gene regulatory networks (GRNs) capture transcription factor-target interactions and are central to understanding cell-state regulation and disease. Reconstructing GRNs from paired single-cell transcriptomic and chromatin accessibility data is promising but challenging: scATAC is extremely sparse, and most methods rely on fixed peak-to-gene links and weak supervision. We present EpiAwareNet, a prior-guided multi-omic Transformer framework that reconstructs GRNs from paired single-cell data using only lightweight biological priors. In Stage 1, EpiAwareNet learns joint gene-peak representations with a gene-peak cross-attention module, enabling data-driven, gene-specific aggregation of accessibility signals rather than hard-coded peak-to-gene assignments. In Stage 2, EpiAwareNet incorporates a bulk-derived GRN prior as noisy positive edges to provide weak supervision under label scarcity, refining regulatory scores while remaining robust to prior noise. In our experiments, EpiAwareNet improves GRN reconstruction over representative single- and multi-omic baselines and yields GRNs with greater biological plausibility, such as improved recovery of known regulatory interactions, suggesting that lightweight biological priors from bulk data can effectively guide single-cell GRN inference when combined with adaptive cross-modal representation learning. Code and data will be available at this https URL.

---


### 187. [Shape-Prior-Based Point Cloud Completion for Single-Stage Fully Sparse 3D Object Detection](https://arxiv.org/abs/2606.00688)

**<font color=#1a73e8>作者：</font>** Kaizheng Wang, Mingqian Ji, Jian Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-stage fully sparse 3D object detectors rely on point clouds data to detect objects in autonomous driving scenarios. However, the sparsity and incompleteness of point clouds significantly limit the performance of 3D object detection. To address this issue, this paper proposes a point clouds completion method specifically designed for single-stage fully sparse detectors. The entire shape-prior-based completion process consists of two consecutive steps. In the first step, we design a novel Instance Selection module, which is capable of identifying point clouds corresponding to foreground objects even when the baseline model does not generate proposals, while effectively ignoring the point clouds of background regions. In the second step, we introduce a novel Alignment-Based Point Completion module, which aligns the point clouds of foreground objects with prototypes in terms of both their centers and orientations. Subsequently, points are selected from the prototype to fill in the missing parts of the foreground object. We evaluated our method on two single-stage fully sparse detectors using the KITTI dataset. The experimental results demonstrate that the proposed method significantly improves the detection performance, confirming its effectiveness and generalizability.

---


### 188. [DistMatch: Adaptive Binning via Distribution Matching for Robust Sequential Conformal Prediction](https://arxiv.org/abs/2606.00690)

**<font color=#1a73e8>作者：</font>** Enver Menadjiev, Jihyeon Seong, Jisu Yeo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential conformal prediction (CP) provides valid uncertainty quantification under the assumption of residual exchangeability. However, this assumption is often violated in real-world time series due to temporal dependencies and distributional shifts. While recent methods attempt to approximate exchangeability through reweighting, identifying optimal weights remains an open challenge. To address this limitation, we propose DistMatch, a binning-based method that recursively partitions residuals within a binary tree using the Kolmogorov-Smirnov (KS) statistic. We theoretically show that this partitioning induces approximately exchangeable leaves, thereby avoiding the need for reweighting. By applying quantile regression with online updates within each leaf, DistMatch enables locally adaptive inference and improves robustness to distributional shifts. Extensive experiments demonstrate that DistMatch outperforms existing sequential CP methods.

---


### 189. [FROST-STA: Frozen Dense Features for the Ego4D Short-Term Object Interaction Anticipation](https://arxiv.org/abs/2606.00694)

**<font color=#1a73e8>作者：</font>** Chaoyang Wang, Lexuan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short-term anticipation in egocentric video requires more than recognizing the current scene: a system must infer which object the camera wearer will contact, which action will follow, and how soon the contact will happen. This report describes FROST-STA, our submission to the Ego4D Short-Term Object Interaction Anticipation (STA) Challenge at EgoVis 2026. For each query time, the model produces a ranked set of structured hypotheses containing an active-object box, noun label, verb label, time-to-contact (TTC), and confidence. FROST-STA builds on the V-JEPA 2.1 STA evaluation protocol, but adapts it to the challenge by using object-centric decoding, multi-head prediction, and a submission-oriented training and ensembling recipe. We keep the V-JEPA 2.1 ViT-G backbone fixed and extract two dense token streams: video tokens from a short clip resized to 384 pixels before the query, and image tokens from the last observed high-resolution frame. A compact alignment module, consisting of an attentive probe and frame-guided temporal pooling, maps the clip representation onto the spatial reference of the final frame before fusing it with image features. The fused maps are decoded by Faster R-CNN-style STA heads that estimate box offsets, nouns, verbs, TTC values, and interaction quality. For the final leaderboard entry, we train for 25 epochs with the official training split plus additional permitted validation annotations, and combine predictions across eight heads and checkpoints from epochs 15-25. FROST-STA obtains 5.13 Overall Top-5 mAP on the official test server, ranking second in the challenge and showing that frozen dense image-video features can serve as a strong basis for object-level interaction forecasting.

---


### 190. [COPF: An Online Framework for Deployment-Stable Counterfactual Fairness in Evolving Graphs](https://arxiv.org/abs/2606.00700)

**<font color=#1a73e8>作者：</font>** Sheng'en Li, Dongmian Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online link recommendation on evolving graphs is performative: by choosing which candidate links to show users, the system changes which links form and what feedback it later observes. Consequently, fairness estimates from logged outcomes can be misleading and may drift after deployment when the recommendation policy is updated. We introduce COPF (Counterfactual Online Performative Fairness), a decision-layer framework for deployment-stable fairness monitoring and control in online link recommendation. COPF (i) defines group-level opportunity gaps over exposure (shown vs. not shown) counterfactuals, (ii) makes them estimable by explicit exploration and by logging the probability (propensity) that each candidate is shown, and (iii) audits and controls fairness using residual outcome indistinguishability (OI) over a configurable auditor family with graph-aware doubly robust (GA-DR) estimators. We provide a noisy transfer theorem showing that Residual-OI on estimated GA-DR residuals implies bounds on exposure-counterfactual group gaps under temporal mixing and bounded local interference, and we instantiate an online multicalibration auditor together with a primal-dual controller. Experiments on two TGB streams and a controlled synthetic bipartite stream show that COPF reduces worst-case spikes in exposure-counterfactual group disparities with modest impact on ranking utility. Our code is available at this https URL.

---


### 191. [VICR: Visual In-Context Restoration for Real-World Image Super-Resolution](https://arxiv.org/abs/2606.00704)

**<font color=#1a73e8>作者：</font>** Qichang Zhang, Hailong Wang, Baiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image super-resolution (Real-ISR) requires balancing structural fidelity to degraded observations with realistic detail synthesis. However, existing generative Real-ISR methods often rely on entangled conditioning mechanisms, leading to structural drift or semantically inconsistent details. To address this issue, we propose Visual In-Context Restoration (VICR), a Diffusion Transformer (DiT)-based framework that formulates Real-ISR as image completion. Specifically, we introduce a decoupled visual prior injection mechanism that derives local and global cues from the low-quality (LQ) image: local cues help recover image structures and support high-frequency detail synthesis, while global cues guide overall generation and promote semantic consistency. For ambiguous regions under severe degradation, VICR employs an inference-time agent to refine semantic prompts using visual evidence from the LQ input while keeping model parameters fixed. Experiments show that VICR achieves state-of-the-art performance across multiple Real-ISR benchmarks with only 127M trainable parameters.

---


### 192. [CR-JEPA: Cross-Modal Joint-Embedding Predictive Learning for Remote Sensing Image Retrieval](https://arxiv.org/abs/2606.00706)

**<font color=#1a73e8>作者：</font>** Md Aminur Hossain, Ayush V. Patel, Nitant Dube 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal remote sensing image retrieval aims to retrieve semantically related scenes across heterogeneous sensing modalities. This remains challenging because paired observations may differ substantially in imaging physics, spatial resolution, spectral configuration, and visual appearance. Moreover, a single retrieval projection trained with one objective may be insufficient to jointly support cross-modal semantic alignment and same-modal neighbourhood preservation. We propose CR-JEPA, a Cross-modal Retrieval Joint-Embedding Predictive Architecture for dual-modality remote sensing retrieval. The model uses modality-specific stems, a shared transformer trunk, and JEPA-style predictive objectives to estimate masked latent target features within and across modalities. Inspired by LeJEPA, we apply Sketched Isotropic Gaussian Regularization to raw retrieval projections to stabilize embeddings and mitigate collapse. CR-JEPA further employs a decoupled-head design with a unified retrieval head for same-modal retrieval and a cross-modal retrieval head for cross-modal search. We evaluate CR-JEPA on BEN-14K, CBRSIR_VS, and DSRSID. On BEN-14K, CR-JEPA improves S1 to S2 retrieval from 61.23% to 75.82% and S2 to S1 retrieval from 63.73% to 75.40% over X-JEPA, while also achieving competitive same-modal retrieval with fewer parameters.

---


### 193. [CASTLE2026 Team WDL Technical Report](https://arxiv.org/abs/2606.00712)

**<font color=#1a73e8>作者：</font>** Zhengyang Li, Zhenglin Du, Yi Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The CASTLE Challenge @ EgoVis 2026 evaluates long-form egocentric video question answering over 600+ hours of multi-perspective recordings. Each four-choice question requires evidence from videos, transcripts, auxiliary photos, people, days, rooms, and temporal context. We propose an evidence-aware multimodal reasoning pipeline based on Qwen. Our system parses question hints, retrieves ASR chunks, attaches auxiliary images, samples candidate video frames, and routes questions into static visual, speech/text, temporal, and mixed types with specialized prompts. Multiple inference passes are aggregated by confidence-weighted voting and converted into the official Codabench format. In ablation, LoRA improves the score from 0.21 to 0.50, and more sampled frames further raise it to 0.58. Our final system ranks first in the CASTLE Challenge @ EgoVis 2026.

---


### 194. [Graph Transfer Learning via Shared Latent Geometry: Theory and Applications](https://arxiv.org/abs/2606.00716)

**<font color=#1a73e8>作者：</font>** Tong Wu, Andrew Campbell, Anna Scaglione  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference and control in engineered physical systems pay a heavy physics cost at deployment: state estimators, inverse-problem solvers, model-predictive controllers, schedulers, and observers are often not closed-form and must re-solve a numerical optimization per instance, with the operator re-supplied each time. Physics-informed learning moves this cost to training, but uses a single encoder pathway whose latent geometry de-learns under fine-tuning and admits no quantitative transfer guarantee. We propose an asymmetric two-pathway architecture that resolves both issues. A teacher encoder consumes privileged dense states from a high-fidelity simulator and represents the system through operator-polynomial features stable under spectral perturbation; a student encoder learns the same latent geometry from sparse field data and operator descriptors. At deployment the teacher is discarded, and the frozen student runs in a single forward pass with a transfer certificate. The design connects to privileged-information learning, knowledge distillation, and cross-modal distillation, but targets cross-instance transfer rather than fixed-instance prediction: topology and operator may change, while the latent task does not. We establish sufficient and near-necessary transfer conditions via Wasserstein proximity between latent laws, yielding a zero-shot error bound, and develop a finite-sample certification protocol with active expansion when coverage is incomplete. The framework applies wherever a system admits an operator with reportable spectrum. On power-system estimation, it achieves zero-shot transfer to 100 unseen topologies, a 95% certificate pass rate, accuracy competitive with topology-aware Newton--Raphson, and sub-millisecond inference. These results suggest asymmetric pathways plus operator-anchored latent geometry provide a foundation for certified zero-shot inference and control.

---


### 195. [Multi-Agent Conformal Prediction with Personalized Statistical Validity](https://arxiv.org/abs/2606.00717)

**<font color=#1a73e8>作者：</font>** Martin V. Vejling, Christophe A. N. Biscio, Adrien Mazoyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is essential in high-stakes machine learning tasks. However, one of the principled solutions, conformal prediction, faces challenges under limited local calibration data, privacy constraints, and data heterogeneity. In multi-agent settings, existing works do not simultaneously and satisfactorily address these challenges with guarantees either limited to averages across agents or losing validity in heterogeneous settings. Hence, we propose personalized federated weighted conformal prediction (PFWCP), a framework that combines local density ratio weighting with weighted quantile aggregation to correct for heterogeneity while preserving privacy. The method yields asymptotically valid marginal and calibration-conditional coverage guarantees for each participating agent and supports protocols with one-shot communication. Theoretical analysis presents an adjustment to the coverage variance, governed by an effective sample size expression, which is necessary in the context of weighted conformal prediction, and experiments on synthetic and real datasets show improved calibration quality over state-of-the-art federated conformal baselines.

---


### 196. [Knowing When to Move: Evidence Accumulation Models of Human Behavior in Traffic](https://arxiv.org/abs/2606.00727)

**<font color=#1a73e8>作者：</font>** Floor Bontje, Felix van Waveren, Leendert van Maanen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evidence accumulation models provide a formal framework for studying decision making as a dynamic process unfolding over time. While these models have been extensively developed and reviewed in laboratory paradigms, their structured application in complex, ecologically valid domains has received comparatively little attention. Road traffic is a particularly relevant context for studying sustained, embodied perception action behavior, where decisions unfold under time pressure and involve continuous control and ongoing perception-action coupling. Examining how EAMs have been applied in this domain may therefore offer insights beyond discrete laboratory tasks toward decision making in real-world behavior. This semi-systematic review synthesizes 28 studies (2014-2026) applying EAMs to traffic-related behavior. We organize the literature along two dimensions: 1) modelling level, distinguishing models at the level of discrete decision-making and models at the level of continuous action control, and 2) model architecture, distinguishing evidence accumulation as either a stand-alone decision model or an embedded component within broader perception-action or interaction frameworks. These distinctions are associated with systematic differences in model architecture, parameterization, data usage, and validation strategies, reflecting task specific demands. By providing a structured overview of these patterns, this review clarifies how EAMs are currently instantiated in traffic contexts and highlights methodological challenges and future directions both in traffic modelling and in modelling of decision-making more broadly. Promising directions include laboratory work on evidence accumulation in sustained and time-varying tasks, interactive multi-individual decision-making, and the use of neurophysiological measures to identify the perceptual evidence underlying complex perception-action behavior.

---


### 197. [From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users](https://arxiv.org/abs/2606.00728)

**<font color=#1a73e8>作者：</font>** Wuqiang Zheng, Chengbing Wang, Yilin Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed in long-term interactions with users, empathy has become an increasingly important capability. However, existing research overlooks the influence of users' personality traits on empathetic strategies during long-term interactions. To address this gap, we introduce the task of personalized empathy, which focuses on adapting empathetic strategies according to users' personalized characteristics derived from history. To study and enhance this capability, we construct PersonaEmp, a personalized empathy dataset built from long-term user-AI interactions, featuring rich user histories, persona information, and empathy-seeking queries. We further propose PereGRM, a reward modeling framework that combines the empathy evaluation structure with dynamic evaluation criteria generation for fine-grained reward modeling. Experimental results across different settings and multiple judge models show that PereGRM consistently achieves the strongest performance improvements, indicating its effectiveness for enhancing personalized empathetic capabilities.

---


### 198. [AI Sovereignty as National Learning Capacity: A Human-Centered Learning Mechanics Viewpoint on France, the United States, and China](https://arxiv.org/abs/2606.00729)

**<font color=#1a73e8>作者：</font>** Kim Phuc Tran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence is often discussed in France in terms of investment, compute capacity, regulation, employment, sovereignty, and education. These dimensions are usually treated separately. This viewpoint paper proposes a unified interpretation: France should be understood as a \emph{national AI learning system}. Building on Human-Centered Learning Mechanics (HCLM), recently formulated as a dynamical framework for entropy-regulated representation learning, we interpret national AI development as a controlled balance between information injection and entropy dissipation. Information injection corresponds to compute, data, talent, research, capital, industrial deployment, and institutional experimentation. Entropy dissipation corresponds to organizational complexity, coordination frictions, energy constraints, regulatory uncertainty, talent mobility pressures, and opportunities to strengthen industrial absorption. The central claim is that AI sovereignty does not emerge from scale alone but from a country's capacity to regulate its own information dynamics. This paper connects HCLM with neural scaling laws, endogenous growth theory, creative destruction, and game theory. It argues that the French AI debate should move beyond the binary opposition between techno-optimism and regulation-first caution. A competitive and human-centered AI strategy requires a controlled regime in which information injection grows faster than institutional dissipation, while avoiding unstable, unequal, or energy-intensive expansion. We provide a mathematical model, measurable policy indicators, game-theoretic propositions, illustrative simulations of national AI regimes, and concrete policy implications for France. The proposed viewpoint reframes AI policy as the governance of an open, strategic, non-equilibrium learning system.

---


### 199. [SHARP: Sleep-based Hierarchical Accelerated Replay for Long Range Non-Stationary Temporal Pattern Recognition](https://arxiv.org/abs/2606.00732)

**<font color=#1a73e8>作者：</font>** Jayanta Dey, Shikhar Srivastava, Itamar Lerner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning long-range non-stationary temporal patterns remains a core challenge for modern sequence models, particularly in strict streaming settings. In these settings, data arrive sequentially and must be processed in a single pass without simultaneously revisiting past observations. Standard architectures, including recurrent neural networks and transformers, are constrained by either truncated backpropagation through time horizon or explicit input window length for long range credit assignment. To address these limitations, we propose SHARP (Sleep-based Hierarchical Accelerated Replay), a framework that decomposes temporal learning into two complementary components: a memory module that accumulates a structured history of past inputs, and a pattern-recognition module that operates over this memory. This separation enables resource- and compute-efficient adaptation to non-stationary dynamics by eliminating the need for backpropagation through time across many steps for long-range credit assignment. Inspired by the accelerated replay observed in rodents during slow-wave sleep, SHARP incorporates offline (sleep) phases in which temporally structured memory traces are replayed in an accelerated form and integrated into higher-level memory representations, improving long-range context retention. Through controlled simulations and ablation studies, we characterize the key properties of the proposed framework. In benchmark datasets such as text8 and PG-19, we demonstrate that SHARP improves over recurrent baselines by retaining next-token predictive performance on previously seen data while continuing to learn from the current stream and generalizing to future unseen data. These gains are enabled by its hierarchical structure, which yields an exponentially increasing effective temporal context with only linear-time computational cost.

---


### 200. [SORA: Free Second-Order Attacks in Fast Adversarial Training](https://arxiv.org/abs/2606.00738)

**<font color=#1a73e8>作者：</font>** Mazdak Teymourian, Ramtin Moslemi, Farzan Rahmani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial Training (AT) is a leading defense against adversarial examples but often suffers from Catastrophic Overfitting (CO) in efficient single-step variants, where robustness to multi-step attacks collapses despite high single-step performance. We address this failure mode with two contributions. First, we formalize Epsilon Overfitting (EO), a perspective in which fixed perturbation magnitudes and directions exacerbate CO, and show that introducing perturbation variability significantly improves robust generalization across different architectures and datasets. Second, we propose PertAlign (Perturbation Alignment), a theoretically grounded, computationally negligible metric that predicts CO onset by measuring gradient alignment across attack stages. Leveraging these insights, we introduce SORA, an adaptive step-size AT method that dynamically adjusts perturbations based on loss surface geometry. SORA consistently prevents CO, achieves state-of-the-art robustness and clean accuracy, and generalizes across datasets and architectures using a single fixed set of hyperparameters, which is essential for applicability in fast AT. Extensive experiments on diverse datasets and architectures show that SORA matches or surpasses the robustness of prior methods while delivering higher clean accuracy and superior efficiency. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
