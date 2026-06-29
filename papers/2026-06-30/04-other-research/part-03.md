# 📦 其他研究 | 2026年06月30日

> 本类共 **160** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-160](./part-04.md)

---

### 101. [Graph Dimensionality Reduction for Contextual Bandits: Structure-Specific Regret Bounds under Approximate Smoothness and Noisy Eigenspaces](https://arxiv.org/abs/2606.27917)

**<font color=#1a73e8>作者：</font>** Joyanta Jyoti Mondal, Ibne Farabi Shihab, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandits with graph-structured arms arise in recommendation, citation retrieval, and social advertising, where arms connected on a graph tend to share reward signal. Standard dimensionality reduction ignores this structure, inflating exploration cost by a factor of $d/k$. We propose GraphDR-LinUCB, which projects arm features onto the graph's low-frequency spectral subspace and runs linear UCB in the resulting $k$-dimensional space. We prove the first $\wtO(k\sqrt{T})$ regret bound for spectral-projection-based contextual bandits, reducing dimension dependence from $d$ to $k$; a perturbation argument extends this to noisy graphs, with an explicit penalty for reward-smoothness mismatch and graph-estimation error. Our central theoretical finding is that the high-frequency reward component need not incur a worst-case linear-in-$T$ penalty: its actual cost depends on its realized impact along the played path, not on its total energy. A simple spectral comparison between subspaces ($\Gamma_k$) predicts which reducer wins on a given dataset, correctly calling five of six real-dataset outcomes without any fitted threshold. Across a synthetic benchmark and six real datasets (MovieLens, Amazon, LastFM, ogbn-arxiv, MIND), GraphDR-LinUCB reduces cumulative regret by $15\times$ over full-dimensional LinUCB and outperforms competing graph-aware methods on five of six; the single failure is precisely where the graph's spectral subspace is misaligned with the reward.

---


### 102. [Every Step of the Way: Video-based Parkinsonian Turning Step Counting](https://arxiv.org/abs/2606.27918)

**<font color=#1a73e8>作者：</font>** Qiushuo Cheng, Jingjing Liu, Catherine Morgan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a prominent symptom of Parkinson's disease (PD), turning impairment is evaluated through parameters such as turning angle, duration, and particularly, the number of steps required to complete a turn, which directly reflects motor dysfunction. Accurate step counting is challenging due to variability in real-world turning movements and atypical shuffling patterns in parkinsonian gait. Existing methods are predominantly wearable-based, requiring users to wear and manage dedicated devices, which can be inconvenient for continuous daily use. To address this, we propose a passive, video-based framework that estimates step count in a coarse-to-fine manner using diverse motion representations. Specifically, an initial step count is estimated from foot movement signals derived from 3D human mesh recovery, providing high-level motion structures. To incorporate fine-grained motion details, a motion encoder learns complementary gait dynamics from mesh and optical flow to refine the initial estimate. In this process, coarse foot movement signals query the pixel-level motion cues via cross attention to capture subtle parkinsonian gait dynamics. To handle varying video lengths, we partition each video into clips and integrate clip-wise motion embeddings via multiple instance learning (MIL) for step count residual prediction. Extensive experiments show our method consistently outperforms existing step counting methods on real-world PD turning datasets.

---


### 103. [Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding](https://arxiv.org/abs/2606.27922)

**<font color=#1a73e8>作者：</font>** Shuimu Chen, Yuteng Chen, Yuanshen Guan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current multimodal reflection mechanisms for long video understanding predominantly rely on closed-loop self-reflection within internal parameters. Lacking objective external evidence, models are frequently trapped in blind confidence and often fail to correct errors. Furthermore, applying reinforcement learning to multi-stage reflection pipelines introduces severe policy coupling, which is exacerbated by a critical scarcity of dedicated training data. To address these limitations, this work proposes Reflect-R1, the first Evidence-Driven self-correction framework for long video understanding. The framework constructs a three-stage pipeline consisting of intuition, verification, and arbitration. By dynamically retrieving objective visual evidence to verify initial intuitions and autonomously executing multiple temporal searches to resolve conflicts, it completely breaks the hallucination loop. To overcome policy coupling, we design a stage-decoupled reinforcement learning algorithm named SD-GRPO that independently computes advantage functions across different reasoning stages. Concurrently, we construct a dataset of 120K samples to bridge the training data gap. Extensive experiments on benchmarks such as VideoMME and LongVideoBench demonstrate that Reflect-R1 achieves state-of-the-art performance. Our method significantly improves the genuine rectification rate and enables authentic self-correction strictly grounded in objective evidence.

---


### 104. [Home3D 1.0: A High-Fidelity Image-to-3D Asset Generation System for Interior Design](https://arxiv.org/abs/2606.27923)

**<font color=#1a73e8>作者：</font>** Yiyun Fei, Guoqiu Li, Jin Song 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Home3D 1.0, a modular image-to-3D generation system that produces high-quality 3D assets from a single reference image, targeting interior design and e-commerce applications. Given a photograph of a furniture or decor item, the system outputs a mesh with physically-based rendering (PBR) materials, and the mesh can be decomposed into material-specific components. The pipeline is organized into four tightly coupled modules: Geometry reconstructs a watertight mesh through latent SDF modelling with a geometry VAE and a coarse-to-fine flow-matching DiT; Texture predicts multiview albedo observations, reprojects them onto the mesh, and completes unseen surface regions with a 3D texture field; Material uses MatWeaver to obtain component masks through video-based segmentation and UV-space voting, then retrieves and bakes PBR maps from a curated material library through hierarchical multi-modal matching; and Parts generates material-editable semantic part meshes with a PartVAE and PartDiT, decoding multi-head part-specific SDF fields in one pass. Each module is evaluated independently with dedicated metrics, highlighting both the current system capability and the remaining gaps toward broader deployment.

---


### 105. [Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking](https://arxiv.org/abs/2606.27934)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Baris Basaran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Performance numbers reported for hardware are accepted on trust: the reader cannot recompute them, the apparatus is gone, and the silicon itself can be silently wrong, with fleet studies reporting on the order of one core in a thousand returning incorrect arithmetic with no error raised. We make a reported hardware measurement a tamper-evident, independently checkable record. Every quantity in the text, a table, or a figure is bound, by its content hash, to the observation and the verification behind it; the whole is a hash-linked, append-only structure (a transparency log for measurement) that a verifier audits offline without trusting its producer. Matrix products are verified by a probabilistic identity (Freivalds) at O(k n^2) cost under a tolerance we derive from floating-point error analysis and calibrate to the device's own measured residual floor, so a wrong product is rejected with probability 1 - 2^(-k); quantities with no such identity carry an algebraic checksum and a measured reproducibility class. We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this. Driving the device from an unprivileged tenant's reach, with a di/dt power virus and a thermal soak, neither moves the calibrated tolerance nor produces a silent error, placing the physical-fault threat at the rare defective part or the privileged attacker and marking the boundary at which the record must compose with a hardware root of trust. We demonstrate the construction across Blackwell and Hopper GPUs and report a residual-floor and reproducibility map by precision, size, and device.

---


### 106. [Controllable Histopathology Image Synthesis with Training-free Structural Initialization and Textural Modulation](https://arxiv.org/abs/2606.27935)

**<font color=#1a73e8>作者：</font>** Yuheng Qiu, Jingyi Luo, Chenfei Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has demonstrated remarkable success in high-throughput histopathology image analysis. However, the performance of learning-based models critically depends on the quality and size of annotations by expert pathologists, which is a resource-intensive and time-consuming process. To address the limitations of data scarcity and annotation burden, several methods have been proposed to synthesize paired histopathology data. Nevertheless, these frameworks typically still require annotation data, albeit in reduced quantities, to impose structural constraints during training.
In this work, we present CHIS, a plug-in framework that guides the sampling trajectory of a pretrained diffusion model through two key stages: structural initialization at the start and textural modulation during generation. The initial noise state is refined by fusing the phase information from a prior mask with the amplitude of Gaussian noise in the frequency domain, yielding a structurally informed starting point. During the reverse diffusion process, we adaptively modulate both coarse-grained and fine-grained textures at different wavelet decomposition levels. This enables a diffusion model pretrained solely on unlabeled images to generate outputs that align with prior structural masks while preserving the reference tissue style.
We conducted extensive experiments demonstrating the superiority of CHIS in generation fidelity and its substantial benefits for downstream segmentation tasks. Code is available at this https URL.

---


### 107. [VASAE: Naming SAE Dictionary Directions with Vocabulary-Aligned Anchoring](https://arxiv.org/abs/2606.27941)

**<font color=#1a73e8>作者：</font>** Kairui Zhang, Ziwen Yu, Zahraa S. Abdallah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) provide useful decompositions of Transformer residual streams, but their learned features are usually named post hoc rather than directly connected to the Transformer's token vocabulary. We introduce Vocabulary-Aligned Sparse Autoencoder (VASAE), a method that trains SAE features under vocabulary-aligned anchoring and assigns each feature an intrinsic token name: the token string whose embedding is nearest to that feature. Without reducing reconstruction quality compared with a standard SAE, VASAE produces dictionaries with vocabulary-aligned features. Using a 0.8 cutoff on the nearest-token alignment score, dictionaries trained on GPT-2-small post-residual streams align about 90% of features in layers 0--10. In Llama-3.1-8B, representative shallow and middle-layer dictionaries contain strongly aligned features, including 92.8% in the shallow layer, while the representative final-layer dictionary shows limited alignment. After subtracting the sentence-level mean sparse code, case studies show that many remaining intrinsic token names are relevant to nearby input tokens. These results suggest that vocabulary-aligned anchoring can connect learned features to intrinsic token names during training, complementing post hoc interpretation of learned dictionaries.

---


### 108. [RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry under Limited Data](https://arxiv.org/abs/2606.27948)

**<font color=#1a73e8>作者：</font>** Xuan Zhao, Lena Krieger, Zhuo Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations (CFs) help understand machine learning models by identifying minimal input changes that would lead to alternative model outcomes. Recent work demonstrates their utility for reconstructing black-box models, enabling third-party auditing of opaque decision systems for fairness and accountability. Still, CF-based reconstruction may suffer from decision boundary shifts, overfitting, and restrictive assumptions requiring online query access to target platforms. We propose REconstruction via Counterfactual-Aware waSserstein opTimization (RECAST) under limited data and restricted access, a behavioral surrogate model based on Wasserstein barycentric prototypes. Our approach addresses decision boundary shifts by incorporating CFs as informative, though less representative, samples for both classes, maintaining high surrogate fidelity in low-sample regimes without requiring online access during reconstruction. To enhance fairness auditing, our method enables systematic group fairness diagnostics. Experiments on real-world datasets and various setups show that RECAST effectively achieves high fidelity and query efficiency, as well as stable results even when the access is limited and noisy.

---


### 109. [Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control](https://arxiv.org/abs/2606.27964)

**<font color=#1a73e8>作者：</font>** Haoyuan Wang, Yabo Chen, Haibin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building interactive world models requires generating realistic videos while maintaining controllable dynamics over long horizons. Autoregressive video generation offers a scalable foundation, but suffers from error accumulation and temporal degradation during extended rollouts. This issue is further amplified under heterogeneous controls such as human motion and camera trajectories, which may interfere and destabilize a pretrained video prior, while existing methods often trade off controllability and visual quality. We propose "Directing the World", a fast autoregressive framework for controllable world-model video generation with compositional human-motion and camera-trajectory control. Our key idea is to decouple control learning while preserving a unified autoregressive video prior. We introduce a Fast-Slow Memory training strategy to stabilize long-horizon rollout learning and improve convergence. For human motion control, we design a t-guided Dynamic Projection mechanism and a refined Motion-CFG strategy, enabling temporally smooth and accurate motion alignment without degrading visual fidelity, and supporting multi-person this http URL learning a robust motion prior, we introduce a second-stage camera-trajectory control module to compose human dynamics with viewpoint changes for coherent world exploration. We further construct a large-scale dataset with synchronized video, text, human-motion, and camera-trajectory annotations, organized into motion-centric and camera-centric subsets for decoupled training. Extensive experiments show stable long-horizon generation with precise controllability and high visual quality. See more at this https URL.

---


### 110. [Decoys Cannot Go Everywhere: Mapping the Deception Surface in MITRE ATT&CK](https://arxiv.org/abs/2606.27966)

**<font color=#1a73e8>作者：</font>** Veronica Valeros, Carlos Catania, Viliam Lisý 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber deception research often assumes that a decoy can be placed wherever there is attacker behavior. This work tests that assumption across MITRE ATT&CK v18.1. We introduce a four-criterion rubric for infrastructure deception and apply it to all 250 ATT&CK techniques. The rubric evaluates whether a defender-controlled decoy can be placed, whether an attacker is likely to interact with it, what intelligence that interaction can yield, and whether the interaction reliably indicates malice. The resulting deception surface is sparse: only 80 techniques (32%) admit a decoy the attacker could plausibly reach. For the remaining 170 techniques, there is no defender-controlled asset in the attacker's path that can be fabricated as a decoy. Decoy placement across those 80 techniques falls into two patterns we call Sweep and Seek. In Sweep, the attacker moves broadly through assets in range and encounters the decoy as part of that activity. In Seek, the attacker looks for a specific kind of asset and interacts with a fabricated version of it. These patterns give a simple placement rule: a decoy must either sit on a sweep path or imitate a sought asset. We also show that decoys usually have useful intelligence potential, but whether an attacker interacts with them at all, and whether that interaction reliably indicates malice, both vary. We release the rubric, decision rules, and per-technique assessment as an auditable baseline for future deception research and deployment planning, and show that infrastructure decoys cannot be assumed to apply to all attacker behavior.

---


### 111. [RelBall: Relation Ball with Quaternion Rotation for Knowledge Graph Completion](https://arxiv.org/abs/2606.27967)

**<font color=#1a73e8>作者：</font>** Yike Liu, Peijia Xie, Chao He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world knowledge graphs are often incomplete, lacking many valid facts. Knowledge Graph Completion (KGC) aims to predict missing links using known triples, thereby enhancing graph coverage. A key challenge is modeling diverse relational patterns such as symmetry, antisymmetry, inversion, composition and semantic hierarchy. Existing models such as RotatE can capture symmetric, antisymmetric, inverse, and commutative composition patterns, yet struggle with non-commutative composition. Rotate3D addresses this by introducing non-commutativity via three-dimensional rotations, but still fails to capture the semantic hierarchies prevalent in knowledge graphs. Moreover, both models cannot effectively model one-to-many relations. To overcome these limitations, we propose RelBall, which extends Rotate3D with two innovations. First, our model introduces modulus transformation to model hierarchies, driving abstract concepts toward smaller moduli and concrete instances toward larger ones. Second, it introduces a tail-centric relation ball to model one-to-one, one-to-many, many-to-one, and many-to-many relations. RelBall offers the following advantages: (1) coverage of all relational patterns, including the ones mentioned above; (2) an interpretable hierarchical representation where the modulus directly reflect semantic levels; (3) support for one-to-one, one-to-many, many-to-one, and many-to-many relations. Experiments on multiple datasets demonstrate RelBall's competitive link prediction performance against various baselines.

---


### 112. [Parallel Rollout Approximation for Pixel-Space Autoregressive Image Generation](https://arxiv.org/abs/2606.27978)

**<font color=#1a73e8>作者：</font>** Jiayi Xu, Di He, Guolin Ke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space continuous-token autoregressive (AR) generation directly models images as sequences of raw pixel patches, avoiding discrete tokenization or a separately pretrained tokenizer. However, it faces coupled challenges: high-dimensional patch generation causes large single-step errors, and teacher-forced training creates a train--inference gap that makes these errors accumulate across AR steps. Existing fixes such as $x$-prediction and input noise injection only partially mitigate these issues. Exact rollout training better matches inference-time conditions, but is impractical due to prohibitively slow sequential sampling. We propose \emph{Parallel Rollout Approximation} (PRA), a scalable framework that addresses both challenges jointly. PRA generates low-dimensional intermediate states instead of high-dimensional pixel patches, then maps them back to pixel-space tokens with a pixel decoder, preserving a pixel-in, pixel-out AR interface. It also constructs inference-like pixel inputs through the same intermediate-state-to-pixel path used at inference, independently across positions, approximating the pixel-feedback interface encountered during inference-time rollout while retaining parallel teacher-forced training. On class-conditional ImageNet-1K generation at $256\times256$ resolution, PRA-S with 135M parameters achieves an FID of 2.58, surpassing the previous billion-scale pixel-space AR result of 3.60. Scaling to PRA-L with 511M parameters further improves FID to 1.94, establishing a new state of the art among pixel-space AR models. Beyond generation, PRA achieves higher ImageNet classification probing accuracy than other AR and diffusion baselines, suggesting its potential for unified pixel-space image generation and understanding.

---


### 113. [ToxiREX: A Dataset on Toxic REasoning in ConteXt](https://arxiv.org/abs/2606.27981)

**<font color=#1a73e8>作者：</font>** Stefan F. Schouten, Ilia Markov, Piek Vossen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a new, contextual, multilingual dataset called ToxiREX: Toxic REasoning in ConteXt. The dataset consists of threads of Reddit comments and structured characterizations of what the comments imply, following a systematic toxic reasoning schema developed in a previous paper. Using the schema allows us to capture and explain implicit and context-dependent toxicity, while supporting mappings to existing toxicity taxonomies. The dataset includes comments in six languages (English, Arabic, Turkish, Spanish, German, and Dutch), collected from posts connected to specific major events (e.g. the 2023 Turkey earthquakes; the Russian invasion of Ukraine). We describe the context-preserving preprocessing of the threads. We create a training set of 125 thousand comments which is annotated by a commercially available LLM, and a test set of just under three thousand comments that is annotated by native speakers. We show that apparent disagreements in the test set annotations often reflect defensible alternative interpretations rather than noise. Finally, we provide baseline results by prompting and fine-tuning language models. To produce these results, we develop evaluation strategies for our hierarchical, schema-based predictions. While models perform better than random, there remains a lot of room for improvement, showing the task to be challenging. ToxiREX is the first dataset to simultaneously incorporate multiple languages, conversational context, and implicit toxicity, while using the toxic reasoning schema for rich, structured annotations. Dataset available at: this https URL

---


### 114. [Dual-Learning based Penalized Multi-Align Clustering for Multi-View Incomplete and Disorderly Data](https://arxiv.org/abs/2606.27984)

**<font color=#1a73e8>作者：</font>** Liang Zhao, Shubin Ma, Bo Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal feature fusion can effectively capture complex patterns in real-world data by integrating complementary information from different modalities. However, in many applications, such as boiler combustion monitoring, equipment failure, inconsistent sensor sampling frequencies, and network delays often cause missing modalities and temporal asynchrony. These issues lead to incomplete and disorderly multimodal data. To address them, previous studies have proposed several data fusion methods that align cluster centers before fusion. However, these methods have two key limitations. First, they cannot guarantee accurate sample-level alignment of data pairs. Second, they do not address significant discrepancies in data sizes across different classes, which may affect subsequent fusion performance.
To address these problems, we propose a dual-learning based penalized multi-align clustering model, named DLPMAC. The dual-learning mechanism enables the model to learn prior knowledge from each modality, including semantic and structural information. This helps preserve semantic consistency and structural similarity across modalities at both local and global levels. In addition, the penalized multi-align module performs multi-to-multi data alignment through a penalty mechanism. It allows one sample to form data pairs with different samples from other modalities, thereby improving data-pair alignment accuracy. The penalty mechanism also prevents data aggregation, avoiding the case where excessive samples are linked to a single sample. Experimental results demonstrate the effectiveness of DLPMAC in addressing data alignment and fusion challenges from both sampling and clustering perspectives.

---


### 115. [Latent Visual Diffusion Reasoning with Monte Carlo Tree Search](https://arxiv.org/abs/2606.27988)

**<font color=#1a73e8>作者：</font>** Xirui Teng, Nan Xi, Junsong Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analyzing fine-grained skill activities (e.g., sports, surgery) requires not only recognizing visual patterns but also performing step-by-step visual reasoning that leads to the final judgment. While recent advances in action quality assessment have achieved remarkable progress in evaluating performance, existing models remain black boxes, where they lack the ability to explicitly reveal the reasoning processes underlying their judgments. To address this limitation, we propose Latent Visual Diffusion Reasoning (LVDR), a novel framework that integrates keypoint-guided Monte Carlo Tree Search (MCTS) to model and visualize the latent visual reasoning process. LVDR not only produces more accurate skill assessments but also uncovers the critical visual reasoning sequences that contribute to the final evaluation. Extensive experiments across four datasets spanning diverse sports and surgical domains demonstrate that LVDR achieves competitive quantitative performance while providing interpretable visual reasoning trajectories leading to the final predictions. Source codes and models can be found through the following link: this https URL.

---


### 116. [Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings](https://arxiv.org/abs/2606.27997)

**<font color=#1a73e8>作者：</font>** Rostislav Gusev, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks of machine learning models often include many datasets, making evaluation expensive. For efficiency, it is preferable to perform evaluations on small, representative datasets instead. The selection of such subsets typically relies on heuristics and is rarely analyzed for the robustness of the resulting model rankings.
We introduce a framework to perform the task of selecting datasets subsets with an evaluation of how different selection strategies preserve the global model rankings. Our framework includes bootstrap aggregation, which provides valid confidence intervals, allowing a principled comparison of selection strategies. We consider clustering, design criteria (A/D-optimality), random baselines, and greedy farthest-first (FAFI). For the latter, we derive upper bounds on selection quality in terms of ranking errors as a function of the number of selected datasets.
Empirically, in time series classification (TSC, 112 datasets) and in a supplementary natural language processing benchmark derived from MTEB (57 tasks), several selection strategies improve rank preservation compared with random subsets, including simple FAFI. In contrast, in recommender systems (30 datasets), the improvement of strategies over random selection is small and typically statistically insignificant. For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets. Additional experiments indicate that the effectiveness of selection approaches depends on both the quality of dataset representations and the scale of the benchmarking regime.

---


### 117. [Ghost Without Shell: Measuring Non-Interactive SSH Attacks on Honeypots](https://arxiv.org/abs/2606.28006)

**<font color=#1a73e8>作者：</font>** Veronica Valeros, Muris Sladić, Sebastian Garcia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber deception research has focused on improving honeypot deception capabilities to increase attacker engagement and extend their interactions to collect more and better intelligence. For SSH honeypots, this relies on the assumption that attackers log in, open a shell, and type. We tested whether this still held by deploying eleven SSH honeypots that served both interactive and non-interactive session requests for fifteen days. We collected 177,622 authenticated sessions and validated our results against an independent Cowrie dataset over the same time window. We found that 99.23% of sessions were non-interactive. Interactive sessions account for only 0.10%. The same pattern held in the comparative third-party dataset used for evaluation. This finding is important because a honeypot that focuses on interactive shells or evaluates success based on session length and the number of commands can miss most authenticated attacks and draw the wrong conclusions about what attackers do after login.

---


### 118. [Curriculum-guided Change Detection Training: Toward Accurate Serac Fall Monitoring](https://arxiv.org/abs/2606.28012)

**<font color=#1a73e8>作者：</font>** Arthur Dérédel, Carlos Crispim-Junior, Pierre Lemaire 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change Detection (CD) aims to identify semantic or structural changes from nearly registered multi-temporal images. While recent advances in training methodologies have largely focused on semi-supervised learning and consistency regularization, alternative training paradigms remain underexplored. In particular, most deep CD methods rely on uniform sampling during training, implicitly assuming that all training samples contribute equally to the optimization process. However, such naive sampling can introduce noisy gradients and hinder robust representation learning. To address this limitation, we propose a curriculum learning framework tailored for change detection. Our approach investigates two complementary difficulty measures: the Solar Angular Gap (SAG), a physically grounded proxy for acquisition-condition variability, and the Structural Similarity Index Measure (SSIM), which evaluates appearance similarity between image pairs. Based on these criteria, the framework progressively introduces challenging samples during training, enabling models to learn robust representations in a coarse-to-fine manner. We evaluate our method on the challenging SeracFallDet benchmark, where results demonstrate consistent improvements of the proposed approach over standard uniform-sampling strategies for both pixel-based and object-based approaches. These results highlight the potential of curriculum learning to improve robustness in deep change detection. Importantly, our training framework is orthogonal to existing CD architectures, making it readily applicable to a broad range of methods.

---


### 119. [TempAct: Advancing Temporal Plausibility in Autoregressive Video Generation via Planner-Executor RL](https://arxiv.org/abs/2606.28016)

**<font color=#1a73e8>作者：</font>** Jing Wang, Xiangxin Zhou, Jiajun Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion models enable low-latency streaming generation by synthesizing videos chunk by chunk with cached visual context, but this chunk-wise formulation makes temporal instruction following ambiguous. A single global prompt does not specify which sub-event should be realized in each chunk, while naively switching to step-wise prompts often leads to delayed reactions, blended step semantics, and error propagation across prompt transitions. These failures are difficult to address with supervised fine-tuning or distillation alone: SFT suffers from exposure bias, while rollout-based distillation still optimizes low-level denoising or teacher-distribution matching rather than directly enforcing action ordering and prompt-transition correctness. We address these challenges with TempAct, a planner--executor reinforcement learning framework that jointly optimizes temporal decomposition and step-conditioned execution for temporally plausible AR video generation. TempAct uses an LLM planner to explore span-aware step prompts that are executable by the video model, and trains an AR diffusion executor to follow these prompts under its own generated histories. Its key mechanism is hierarchical group exploration: candidate plans form planning groups, and each plan induces an execution group of multiple continuations from a shared visual context, enabling plan-level credit assignment for long-horizon temporal outcomes and executor-level credit assignment for prompt-switch behavior. We further design hierarchical rewards that combine plan-quality and full-video temporal feedback for the planner with local transition-level step-following rewards, aesthetic regularization, and KL constraints for the executor. Experiments on Self-Forcing and LongLive show that TempAct improves temporal consistency while preserving overall visual quality.

---


### 120. [Lifted Causal Inference](https://arxiv.org/abs/2606.28024)

**<font color=#1a73e8>作者：</font>** Malte Luttermann, Tanya Braun, Ralf Möller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifted inference exploits indistinguishabilities in probabilistic graphical models by using a representative for indistinguishable objects, thereby speeding up query answering while maintaining exact answers. In this article, we show how lifting can be applied to efficiently compute causal effects in relational domains. More specifically, we introduce parametric causal factor graphs (PCFGs) to incorporate causal knowledge in lifted models and give a formal semantics of interventions therein. We further present the Lifted Causal Inference (LCI) algorithm to compute causal effects on a lifted level, thereby drastically speeding up causal inference compared to propositional inference, e.g., in causal Bayesian networks. In addition, we present partially directed parametric causal factor graphs (PD-PCFGs) as a generalisation of PCFGs to handle partial causal knowledge and extend LCI to perform lifted causal inference in a PD-PCFG, thereby extending the applicability of lifted causal inference to a broader range of models requiring less prior knowledge about causal relationships.

---


### 121. [EMOSH: Expressive Motion and Shape Disentanglement for Human Animation](https://arxiv.org/abs/2606.28026)

**<font color=#1a73e8>作者：</font>** Dongbin Zhang, Hao Liu, Binquan Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity and expressive controllable human animation is essential for content creation and digital avatar applications. However, existing methods face a dilemma between expressiveness and disentanglement. Mainstream 2D pose-conditioned approaches suffer from "motion-shape entanglement", leading to the leakage of the driving subject's body shape. Conversely, methods relying on 3D priors (e.g., SMPL) achieve geometric disentanglement but struggle to capture facial expressions and complex gestures, resulting in rigid animations. To this end, we propose EMOSH, a novel framework for high-fidelity controllable human video generation. First, an Expressive Human Model (EHM) is introduced as the core control representation. By explicitly disentangling shape and pose parameters, we fundamentally resolve the body shape leakage issue. Alongside this, a robust motion tracker is designed to accurately estimate EHM parameters from video. Second, we propose a Coarse-to-Fine Hybrid Motion Injection strategy, enabling more fine-grained control over expressions and gestures. Furthermore, we introduce a Spatially-Aligned Conditioning mechanism to bridge the domain gap between training and inference, improving identity consistency. Extensive experiments demonstrate that EMOSH outperforms previous methods in both self-driven and cross-driven scenarios, producing high-fidelity videos with vivid expressions while maintaining shape disentanglement.

---


### 122. [Mind the Gap: Quantifying the Domain Gap in Cross-Sensor Diffusion Super-Resolution](https://arxiv.org/abs/2606.28039)

**<font color=#1a73e8>作者：</font>** Dawid Kopeć, Katarzyna Jabłońska, Wojciech Kozłowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Demand for high-resolution satellite imagery has increased interest in super-resolution (SR) to bridge the spatial resolution gap between freely available missions such as Sentinel-2 and commercial systems like PlanetScope. Because no sensor provides true paired low- and high-resolution observations, SR models are usually trained on synthetically degraded data, creating a domain gap on real cross-sensor imagery. In this work, we provide the first systematic study of how this synthetic-to-real mismatch affects the performance of modern diffusion-based SR models. Using a large, geometrically and temporally aligned dataset of Sentinel-2 and PlanetScope imagery, we evaluate five state-of-the-art diffusion architectures under controlled experimental settings. We also introduce LPIPS-Sat, a domain-adapted perceptual metric based on Sentinel-2 self-supervised features. Our results show two persistent challenges: synthetically trained models degrade sharply on real pairs, while models trained on real cross-sensor data exhibit optimisation difficulties and struggle to adapt to the physical and radiometric diversity. These findings highlight a key limitation of current SR and motivate methods that disentangle super-resolution from domain adaptation.

---


### 123. [OperatorSHAP: Fast and Accurate Shapley Value Estimation for Neural Operators](https://arxiv.org/abs/2606.28065)

**<font color=#1a73e8>作者：</font>** Joshua Stiller, Santo M. A. R. Thies, Felix Czaja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding model predictions is essential for physical applications, where outputs often inform safety-critical decisions, such as structural load assessment, weather warnings, and clinical diagnosis. Shapley values satisfy many desirable properties as an attribution method, but their computational cost during inference hinders their practical use. Current amortized explainers, such as FastSHAP, are limited to homogeneous inputs, which is problematic for physical applications where data often comes from irregular grids and geometries. We introduce OperatorSHAP, a grid-agnostic attribution method and training procedure that allows us to train FastSHAP-like explainers for neural operators. We establish a theoretical framework for attributions in function space, connecting to Aumann-Shapley values. We further show that OperatorSHAP's explanations are consistent with state-of-the-art discrete Shapley values across resolutions and transfer across grid sizes without retraining.

---


### 124. [Ontology-Guided Evidence Path Inference for Multi-hop Knowledge Graph Question Answering](https://arxiv.org/abs/2606.28076)

**<font color=#1a73e8>作者：</font>** Yongxue Shan, Meihan Wu, Cundi Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering (KGQA) aims to answer natural-language questions by reasoning over structured facts. Existing multi-hop KGQA methods mainly rely on topic-centered expansion, which faces two key challenges: the search space rapidly grows with noisy mixed-type paths, and retrieved paths may fail to satisfy the semantic constraints of complex questions. To address these challenges, we propose OPI, an ontology-guided evidence path inference framework for multi-hop KGQA. OPI introduces a relation-centric ontology graph to capture the head-tail type constraints of relations, providing a compact interface for answer-side constraints. Based on this ontology graph, OPI first introduces a bidirectional retrieval mechanism by mapping the predicted answer type to compatible final-hop relations and combining topic-side prefix expansion with answer-side final-hop matching, thereby suppressing noisy mixed-type expansion. OPI further adopts an iterative refinement strategy to reassess retrieved paths and candidate answers under the question context, filtering type-compatible but question-irrelevant evidence for more reliable answer prediction. Experiments on WebQSP, CWQ, and MetaQA show that OPI substantially reduces the search space, improves Hit@1/F1 by 4.6/5.0 points on WebQSP and 8.9/3.3 points on CWQ over the strongest prior results, and achieves near-saturated Hit@1 on MetaQA with the retrieval module alone.

---


### 125. [GTI-mSEMP Framework : A Proposed Framework to Stimulate Malware Propagation with Inclusion of Attacker-Defender Strategy](https://arxiv.org/abs/2606.28079)

**<font color=#1a73e8>作者：</font>** Shadeeb Hossain, Kristopher Wilson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of automated, multi-vector malware threats poses a significant risk to heterogeneous, resource constrained cyber-physical networks. Conventional epidemiological models often treat security defenses as static parameters, failing to capture the strategic, asymmetric maneuvers between an attacker and a defender. To address the gap, this paper proposes a Game-Theory-Integrated Modified Multi- Wireless Sensor Epidemic Malware Propagation (GTI-mSEMP) framework. This paper analyzed and compared the operational trajectories of Susceptible (S) and Recovered (R) node populations across three different operational regimes: Balanced Matchup, Exploit Surge and Hardened Defense. Numerical simulation results capture the real-time transient dynamics of the network state variables, demonstrating how the epidemic curve shifts when either the defensive or offensive scaling vectors hold an efficiency advantage. The proposed mathematical and numerical framework provides a rigorous foundation that can be deployed in highly adversarial network environments to evaluate dynamic malware propagation and predict localized node population states.

---


### 126. [Context-Aware Explanations for Spatialized Document Layouts](https://arxiv.org/abs/2606.28081)

**<font color=#1a73e8>作者：</font>** Wei Liu, John Wenskovitch, Chris North 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spatialized document layouts are widely used for exploratory analysis of text corpora, but interpreting the spatial organization of documents and the relationships between regions remains challenging. Existing approaches primarily summarize document content or explain how layouts are generated, providing limited support for understanding spatial relationships within the layout itself. We present CAPE, a context-aware explanation framework that generates natural-language explanations grounded in both document semantics and layout-derived spatial context. CAPE identifies salient spatial patterns (e.g., clusters, subgroups, outliers, and bridging documents) and constructs multi-level contextual representations to guide LLM-based explanation generation. It supports both AI-guided overview and user-driven exploration, with explanations available at multiple levels of detail. We demonstrate CAPE on news and scholarly document layouts and evaluate it in a controlled user study against keyword-based and content-only LLM baselines. Our results suggest that spatially grounded explanations are perceived as more helpful than content-only baselines for interpreting the spatial organization of document layouts.

---


### 127. [STAG: Spatio-temporal Evolving Structural Representation of Action Units for Micro-expression Recognition](https://arxiv.org/abs/2606.28083)

**<font color=#1a73e8>作者：</font>** Nandani Sharma, Varun Sharma, Dinesh Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-expression recognition is challenging due to subtle and short-lived facial muscle movements. Existing methods rely heavily on apex-onset frames, overlook fine-grained inter-frame dynamics, and separately model spatial and temporal information, limiting generalization across datasets. To address these challenges, we propose STAG, a dynamic ROI-AU-coupled spatial-temporal network that jointly models motion flow and adaptive facial connectivity. The framework extracts optical flow from discriminative frames using magnitude-based selection and temporal attention. A dual-branch architecture combines an enhanced graph attention network for structured spatial reasoning with a transformer encoder for temporal modeling. A bidirectional cross-attention module enables mutual refinement of spatial and temporal features, while AU-guided dynamic connectivity adapts facial region interactions according to muscle activation patterns. The transformer captures subtle temporal dynamics beyond apex-based approaches, improving semantic consistency and interpretability for explainable micro-expression recognition. The fused representation is optimized using focal loss and evaluated on CASME II, 4DME, DFME, NaME, SAMM, and SMIC-HS. Extensive experiments demonstrate improved robustness, generalization, interpretability, and computational efficiency, confirming the effectiveness of adaptive relational reasoning, AU-guided dynamic connectivity, and deep spatial-temporal feature fusion for accurate cross-dataset micro-expression recognition.

---


### 128. [RPM-Distill: Physiology-guided Adaptive Cross-modal Distillation for Robust Remote Physiological Measurement](https://arxiv.org/abs/2606.28089)

**<font color=#1a73e8>作者：</font>** Jiyao Wang, Qingyong Hu, Duoxun Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based remote physiological measurement (RPM) is highly accessible but remains fragile under varying illumination, skin tones, and motion. Radio frequency (RF) radar is largely invariant to illumination and appearance, providing complementary cardio-respiratory micro-motion cues; however, requiring radar at inference is often impractical due to its limited ubiquity and deployment overhead. We propose RPM-Distill, a physiology-guided cross-modal distillation framework that leverages synchronized radar only during training while retaining video-only inference. Our key observation is that although RGB and RF waveforms differ in sensing physics and time-domain morphology, they share similar latent periodic rhythm in the frequency domain. We thus distill physiology-structured spectral evidence to improve robustness, via losses that (i) anchor the fundamental peak, (ii) match the off-peak background distribution, and (iii) preserve spectral morphology and sharpness. To avoid negative transfer under sample-level teacher quality and alignment uncertainty, a spectral policy network predicts sample-level distillation gates and component weights from the student--teacher spectral relation map, learned with a meta bilevel objective on a small labeled validation split. Through extensive experiments in challenging conditions and cross-dataset settings, RPM-Distill brings 81\% MAE and 21\% correlation improvement over unimodal baselines. Code is at this https URL.

---


### 129. [Diffusion Model Attribution via Spectral Coupling of Denoiser Responses](https://arxiv.org/abs/2606.28092)

**<font color=#1a73e8>作者：</font>** Pragati Shuddhodhan Meshram, Varun Chandrasekaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attributing a generated image to its source diffusion model is a fundamental challenge in provenance verification and intellectual property protection. This problem is particularly difficult because diffusion models trained on different datasets can converge to similar score functions and thus similar output distributions, making the generated images themselves unreliable as attribution evidence. Existing non-invasive methods either fail on architecturally similar variants or rely on signals that vanish when models share the same autoencoder. We propose Spectral Denoising Signatures (SDS), a non-invasive attribution method that identifies the source model by fingerprinting each candidate model's denoising behavior. Our key insight is that a model's denoising score function exhibits a distinctive spectral geometry, reflected in how it redistributes energy across spatial frequency bands during denoising. By probing this behavior with frequency-controlled perturbations, SDS extracts a stable signature that is intrinsic to the model, requiring only standard forward passes with no inversion, optimization, or generation-time enrollment. Our results demonstrate that SDS achieves approximately 99.9% accuracy across eight diverse diffusion models and 96.2% under cross-domain prompt shift, outperforming non-invasive baselines across variations in training data, architecture, and training procedure, establishing spectral geometry as a principled and practical basis for diffusion model attribution. Code is available at: this https URL

---


### 130. [OSOR: One-Step Diffusion Inpainting for Effect-Aware Object Removal](https://arxiv.org/abs/2606.28094)

**<font color=#1a73e8>作者：</font>** Qinming Zhou, Chenxi Sun, Deyang Kong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world object removal is challenging due to two key difficulties: the target object's non-local effects, such as shadows and reflections, which are difficult to model, and the fact that user-provided masks are often inaccurate or incomplete. With billions of parameters and tens of denoising steps, diffusion-based models achieve strong removal performance at the expense of substantial computational cost, limiting their use in interactive applications and on edge devices. To address these challenges, we present OSOR (One-Step Object Removal), which simultaneously achieves efficient, effect-aware, and mask-robust object removal. Concretely, OSOR introduces: (1) an occupancy-guided discriminator for precise boundary supervision, enabling stable single-step diffusion training; (2) an alpha head that leverages knowledge from pretrained diffusion models to predict appropriate removal regions with minimal overhead, thereby handling imperfect masks; and (3) a semantic-anchored verification pipeline (SAVP) that filters noisy instruction-based triplets to produce effect-aware supervision at scale. Using SAVP, we curate CORNE, which contains 280K verified removal pairs, and further annotate AnimeEraseBench and TextEraseBench to evaluate performance on more complex removal tasks. Experiments show that OSOR surpasses strong multi-step diffusion baselines in perceptual quality while achieving $4\times$ to $30\times$ faster inference.

---


### 131. [Fair Classification with Efficient and Post-hoc Controllable Fairness-Accuracy Trade-off](https://arxiv.org/abs/2606.28097)

**<font color=#1a73e8>作者：</font>** Maaya Sakata, Kazuto Fukuchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc controllability of fair machine learning models, the ability to control the trade-off between fairness and accuracy after training, is valuable for practical deployment. Existing post-processing methods provide such post-hoc controllability but often suffer from significant accuracy degradation, whereas in-processing methods achieve efficient trade-offs but require computationally expensive retraining for each change in trade-off ratio. To achieve both post-hoc controllability and efficient trade-offs, we propose a novel fair classification algorithm that learns effective feature representations to improve the trade-off efficiency of post-processing fair classifiers, by a gradient-based optimization approach. Experimental results on real-world datasets demonstrate that our method achieves trade-off efficiency comparable to, or even surpassing, in-processing methods, without requiring any retraining.

---


### 132. [BiDeMem: Bidirectional Degradation Memory for Explainable Image Restoration](https://arxiv.org/abs/2606.28112)

**<font color=#1a73e8>作者：</font>** Xinrui Wu, Lichen Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Degradation-aware prompts, conditions, and latent priors are increasingly used in image restoration, yet they are usually judged by a single endpoint: whether the restored image obtains higher PSNR. This is a weak test of semantics. A condition can help by adding capacity, acting as a global correction bias, or exploiting dataset shortcuts, without becoming an interpretable degradation prior. We propose BiDeMem, a bidirectional degradation memory for explainable image restoration. A query built from restoration features and input statistics retrieves a compact top-k subset of memory slots. The same selected slot identity supports the restoration path at inference time and a training-only forward-degradation explanation path. The study centers on verifiability in a controlled multi-degradation NAFNet setting. New controls separate the gain from a correction head alone, a dense query prior, and a static global prior: these variants are 0.2588, 0.2586, and 0.2839 dB below BiRank, respectively. Strong residual supervision and a wider degradation head also remain below the full bidirectional memory model. Intervention probes show that BiRank preserves restoration quality while increasing wrong-prior and native-prior sensitivity, framing degradation memory as both a restoration module and a falsifiable explanation mechanism.

---


### 133. [Dangerous Liaisons of Convex Learning and Non-Affine Aggregation](https://arxiv.org/abs/2606.28123)

**<font color=#1a73e8>作者：</font>** Thomas Boudou, Batiste Le Bars, Nirupam Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Last-iterate convergence and generalization guarantees in first-order convex learning hinge on the monotonicity of the update operator. While linear averaging preserves the monotonicity of gradient updates, this property is often violated when gradients are aggregated non-affinely, as in modern pipelines enforcing constraints like adaptivity, privacy, robustness or fairness. Whether it is possible to design non-affine aggregation rules that maintain monotonicity has remained an open question. We answer this question negatively: we prove that the monotonicity of aggregated gradients is preserved if and only if the aggregation rule is positively affine. Consequently, non-affine aggregation prevents steady convergence and substantially degrade algorithmic stability. We quantify these drawbacks and propose a path forward by identifying sufficient conditions under which monotonicity can be restored. Our results provide a unified theoretical framework explaining the disparate failure modes observed in modern learning systems.

---


### 134. [AI-Driven Synthesis for High-Tech System Design: Automating Innovation](https://arxiv.org/abs/2606.28126)

**<font color=#1a73e8>作者：</font>** Luuk Oerlemans, Steven Westerhof, Theo Hofman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article addresses the combinatorial complexity inherent in modern high-tech system design by presenting automation-in-design (AiD) as a transformative paradigm. We propose computational design synthesis (CDS), a framework utilising deep learning and generative AI to automate the creation of novel systems. Two case studies (e-drive system design and spatial dimensioning problem) serve as proof-points for this approach. The AI-driven methods used in the case studies represent a fundamental shift in engineering, advancing from simulation-based optimisation towards autonomous design with minimal human supervision.

---


### 135. [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128)

**<font color=#1a73e8>作者：</font>** Peiwen Zhang, Yufan Deng, Shangkun Sun 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. Through extensive experiments, we find that such physical instability mainly arises from two factors: deformation of moving objects and implausible spatio-temporal correlations among interacting entities, particularly during contact. Building on this observation, we propose PhysisForcing, a scalable training framework that strengthens physical consistency by focusing supervision on physics-informative regions through joint optimization of pixel-level and semantic-level features. The framework consists of a pixel-level trajectory alignment loss, which supervises DiT features using reference point trajectories, and a semantic-level relational alignment loss, which aligns DiT features with inter-region relations extracted from a frozen video understanding encoder. Extensive experiments on R-Bench, PAI-Bench, and EZS-Bench show that PhysisForcing consistently improves embodied video generation over strong baselines, improving the Wan2.2-I2V-A14B and Cosmos3-Nano base models on R-Bench by 22.3\% and 9.2\% (7.1\% and 3.7\% over vanilla finetuning), with the Cosmos3-Nano variant attaining the best overall score. Beyond generation, as a world model under the WorldArena action-planner protocol it raises the closed-loop success rate from 16.0\% to 24.0\% and further improves downstream policy success, indicating that physically aligned video models yield stronger representations for robotic manipulation.

---


### 136. [Beyond Sparse Supervision: Diffusion-Guided Learning for Few-Shot Graph Fraud Detection](https://arxiv.org/abs/2606.28134)

**<font color=#1a73e8>作者：</font>** Liming Liu, Chao Hu, Mingfei Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based fraud detection is essential for safeguarding large-scale transaction systems, where undetected anomalies may lead to substantial financial losses and security risks. Real-world fraud graphs pose two coupled challenges: sparse and imbalanced supervision, where verified fraudulent labels are scarce and heavily skewed toward benign accounts, and representation dilution, where spatial message passing may oversmooth camouflaged anomalies while spectral filters may suppress fraud-relevant mid- and high-frequency irregularities. To address these challenges, we propose ADC-GNN, short for Attention-guided Diffusion-Contrastive Graph Neural Network, a unified framework that combines diffusion-guided feature augmentation, contrastive representation learning, and multi-hop spectral attention for few-shot graph fraud detection. The diffusion component is formulated as a feature-space denoising augmentation mechanism rather than a full topology-generative graph diffusion model: it constructs noise-perturbed node-feature views under a cosine schedule and uses contrastive learning to stabilize node representations across perturbations. The spectral attention module further adaptively emphasizes fraud-relevant hop-level and relation-level cues. We evaluate ADC-GNN primarily on three public benchmarks and additionally report a proprietary real-world telecom transaction dataset with approximately 60,000 records as a private case study. Under the 1% training setting, ADC-GNN achieves consistent improvements over original graph fraud baselines and four protocol-consistent recent graph anomaly/fraud baselines on the public benchmarks. Additional analyses on split stability, training ratios, oversampling alternatives, module-level ablations, diffusion schedules, and runtime and memory-consumption comparisons further characterize the effective operating regime of ADC-GNN.

---


### 137. [MixTTA: Low-Rank Cross-Channel Mixing for Reliable Test-Time Adaptation](https://arxiv.org/abs/2606.28142)

**<font color=#1a73e8>作者：</font>** Mansoo Jung, Youngwook Kim, Jungwoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) methods commonly update the affine parameters of normalization layers to adapt deployed models under distribution shifts. However, per-channel affine parameters perform axis-aligned scaling and shifting, making them geometrically incapable of correcting cross-channel structural changes induced by distribution shift. To address this limitation, we propose MixTTA, a lightweight plug-in module that equips normalization layers with a low-rank cross-channel transformation, enabling inter-channel mixing at each layer. To ensure that the low-rank branch captures only cross-channel interactions, we also propose Decoupling Projection that enforces strict separation from the diagonal affine path, along with Spectral Projection that prevents rank-1 collapse under non-stationary test streams. MixTTA can be seamlessly integrated into any existing normalization-based TTA method. Experiments in both standard and wild TTA settings show consistent improvements over strong baselines while mitigating adaptation failure under challenging conditions. The source code is publicly available at this https URL.

---


### 138. [Monocular Avatar Reconstruction via Cascaded Diffusion Priors and UV-Space Differentiable Shading](https://arxiv.org/abs/2606.28144)

**<font color=#1a73e8>作者：</font>** Hong Li, Minqi Meng, Yanjun Liang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing high-fidelity, relightable 3D avatars from a single in-the-wild image is a challenging ill-posed problem, primarily hindered by the scarcity of high-quality PBR data and the complexity of disentangling illumination from intrinsic materials. In this paper, we present a data-efficient framework that leverages the robust priors of a unified pre-trained diffusion backbone to sequentially address texture completion, delighting, and material decomposition. Unlike existing methods that rely on fragmented pipelines or extensive proprietary datasets, we utilize cascaded Low-Rank Adaptations (LoRAs) to adapt the strong generative prior of the diffusion model for each sub-task in UV space. Specifically, we first employ an Inpainting LoRA to complete missing UV textures caused by occlusion, leveraging the model's semantic understanding to generate semantically and photometrically coherent details. Subsequently, a Light-Homogenization LoRA and a novel Cross-Intrinsic Attention mechanism are introduced to remove baked-in lighting and collaboratively synthesize pixel-aligned PBR maps (Albedo, Normal, Roughness, Specular, and Displacement). To ensure physical plausibility, we impose a UV-space differentiable BRDF shading loss during the decomposition stage, forcing the generative process to adhere to the rendering equation without the artifacts typical of rasterization-based supervision. Extensive experiments demonstrate that our method, trained on fewer than 100 real 3D scans, generates comprehensive, 4K-resolution PBR assets with superior realism and generalization compared to state-of-the-art methods, and all training code and model weights will be released upon acceptance.

---


### 139. [Autoencoder Architectures for Athlete Performance Scoring from Wearable Telemetry](https://arxiv.org/abs/2606.28145)

**<font color=#1a73e8>作者：</font>** Mateusz Kubita, Jan Zubalewicz, Krzysztof Siwek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable devices produce large, high dimensional training logs for everyday runners, and interpretation rather than data collection is now the limiting step. This paper evaluates five dimensionality reduction models, three autoencoder variants, PCA, and a Variational Autoencoder, on their ability to compress nine sensor runner profiles into a single scalar performance indicator, the latent score. Because the setting is fully unsupervised, model quality is assessed along two complementary axes: reconstruction error (Mean Squared Error) and latent score interpretability, measured via Spearman and Kendall rank correlations, Mutual Information, and Permutation Importance. These are combined into a composite selection criterion that prevents selecting models on reconstruction accuracy alone. Feature rankings from the four metrics are aggregated via a modified Borda count, and their stability is confirmed by bootstrap validation. A two feature linear baseline is included to anchor the comparison. Deep autoencoder achieved the lowest reconstruction error and the highest composite score. Once the PCA hidden layers were widened, the deeper variants became closely competitive with Deep AE on the composite criterion, indicating that the limiting factor was hidden layer capacity rather than the one dimensional bottleneck. Running pace, aerobic decoupling, and average heart rate emerged as the dominant latent score drivers across all models and resampling runs, consistent with established physiology.

---


### 140. [Toward Robust In-Context Segmentation via Concept Guidance](https://arxiv.org/abs/2606.28149)

**<font color=#1a73e8>作者：</font>** Zhigang Chen, Xiawu Zheng, Rongrong Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context segmentation (ICS) requires a model to segment target regions in a query image using only a few reference images and their corresponding masks, without updating any parameters. Despite recent progress, prior ICS studies have largely overlooked a critical aspect: system robustness, ie, whether the model can produce stable segmentation results for the same query under different references. In this work, we revisit ICS from the robustness perspective and introduce a novel paradigm, Concept-Guided In-Context Segmentation (CG-ICS), which performs segmentation by extracting high-level semantic concepts from references rather than relying solely on low-level visual matching. Specifically, CG-ICS introduces a concept reasoning module that uses an MLLM to propose candidates and a SAM3-driven scoring function with tree-search refinement to select reliable textual concepts, together with a parallel visual exemplar route that provides query-side spatial grounding via a simple context construction. Both the textual concept and the visual exemplar are then used to activate the segmentation capability of a frozen SAM3 backbone. Extensive experiments on standard ICS benchmarks demonstrate that CG-ICS not only achieves state-of-the-art accuracy but also substantially improves robustness, yielding a more reliable ICS system with significantly reduced variance across diverse reference choices.

---


### 141. [Regularized Reward-Punishment Reinforcement Learning](https://arxiv.org/abs/2606.28152)

**<font color=#1a73e8>作者：</font>** Jiexin Wang, Eiji Uchibe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose KL-Coupled Policy Regularization (KCPR), a policy coordination framework for Reward-Punishment Reinforcement Learning (RPRL). Based on KCPR, we derive KL-Coupled Soft Optimality (KCSO) and develop its deep realization, klDMP. Unlike existing RPRL approaches that optimize reward-seeking and punishment-related policies largely independently, KCPR enables direct interactions between companion policies by treating each as a dynamically learned prior for the other. KCSO yields coupled soft-optimal policies and KL-regularized Bellman operators, allowing reward and punishment information to jointly influence value propagation. To improve learning stability, we introduce a companion-prior softening mechanism and evaluate separate replay-buffer designs for balancing reward- and punishment-related experience. Experiments in grid-world and Gazebo robotic navigation tasks demonstrate that klDMP improves safety and learning stability while maintaining competitive task performance compared with DQN, SQL and softDMP. These results suggest that policy-level coordination provides an effective mechanism for integrating multiple behavioral objectives and may serve as a useful design principle for reinforcement learning systems with interacting motivational processes.

---


### 142. [Recovering Sharp Conductivity Features in the Finite-Data Calderón Problem with Physics-Informed Neural Networks](https://arxiv.org/abs/2606.28158)

**<font color=#1a73e8>作者：</font>** Ali AlHadi Kalout, Pablo Tejerina-Pérez, Konstantin Karchev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have recently emerged as a promising framework for addressing the Calderón inverse problem from limited boundary data. In this work, we revisit neural Calderón inversion by introducing multiscale boundary excitations based on randomized wavelet functions and investigating the role of Fourier-feature encoding (FFE) for representing sharp conductivity variations. We propose a physics-informed reconstruction framework that represents the unknown conductivity and the associated family of electric potentials with separate neural networks conditioned on the applied boundary excitations. The governing elliptic PDE is enforced through physics-informed residuals, while finite Dirichlet-to-Neumann (DtN) data are incorporated through boundary losses. Using synthetic data from a finite-difference forward solver, we evaluate the method on conductivity fields with inclusions, sharp interfaces, smooth profiles, and heterogeneous media. Results show that the framework recovers dominant conductivity structures from finite boundary measurements with relative errors between $3\%-12\%$ approximately. We show that FFE improves the reconstruction of localized sharp features, particularly for inclusions and interfaces, but are not universally optimal, with raw-coordinate networks performing competitively for smoother fields. These results highlight coordinate representations and boundary excitation design as key factors in neural Calderón inversion.

---


### 143. [Tandem Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2606.28166)

**<font color=#1a73e8>作者：</font>** Difan Jiao, Raghav Singhal, Robert West 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has significantly improved the reasoning capability of large language models, reaching expert or even superhuman performance in domains such as competition math. However, whether weaker agents and humans can actually harness this capability is far less certain, with RLVR documented to drift reasoning toward idiosyncratic patterns such as poor readability and language mixing. Tandem training is a recently introduced paradigm that targets this compatibility problem: a trained, stronger senior co-generates each rollout with a frozen, weaker junior, and the two are rewarded as a team, so the senior is pushed to reason in ways the junior can follow. Yet this paradigm has so far been demonstrated only in proof-of-concept settings, leaving open whether it scales to the long chains of thought of the modern RLVR pipeline. In this work, we propose Tandem Reinforcement Learning (TRL), which carries the tandem training paradigm into RLVR. In TRL, the senior and a frozen junior alternate stochastically to co-generate the reasoning, the resulting generation is rewarded, and the standard GRPO loss is applied to the senior. Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior. Our results demonstrate a promising route for RLVR with practical payoffs in multi-model communication and human compatibility.

---


### 144. [The Remittance Blueprint: Data-driven Intelligence for Sri Lanka](https://arxiv.org/abs/2606.28190)

**<font color=#1a73e8>作者：</font>** Dhinanjaya Fernando, Dinura Ginige, Kalana Lakshan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study analyzes Sri Lankan migration and remittances over 32 years (1994-2025). Using a 384-month harmonized dataset, we apply exploratory data analysis, stationarity corrected time-series modeling (ADF, Johansen, VAR/VECM), and supervised learning. Results reveal remittance inflows are primarily driven by external macroeconomic variables, specifically exchange rate dynamics and global oil prices, rather than domestic indicators. Impulse response analysis confirms the asymmetric impact of currency depreciation and oil price shocks. Predictively, multivariate machine learning models outperform traditional univariate approaches; Ridge Regression achieves a 73.8% accuracy improvement over SARIMA (Annualized RMSE: USD 494.8 Mn). The optimized framework projects 2026 remittances at USD 9,001 million under stable conditions. These findings highlight the structural dependence of remittances on global economies, emphasizing the need for robust exchange rate policies, skilled migration, and formal financial channels to enhance long-term economic resilience.

---


### 145. [COCOLogic-V2: Identifying Logical Inconsistencies via Truly Hard-Negatives](https://arxiv.org/abs/2606.28194)

**<font color=#1a73e8>作者：</font>** David Steinmann, Antonia Wüst, Kristian Kersting 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While interpretable models such as concept bottleneck models (CBMs) and program synthesis methods enable verification of model decisions, their evaluation is typically limited to simple tasks, leaving complex reasoning on real-world images largely unexplored. We introduce COCOLogic-V2, an object-centric dataset for visual inductive reasoning on real-world images covering a broad subset of first-order logic. By categorizing samples into positive variants, near-boundary (NB), and far-from-boundary (FB) negatives, COCOLogic-V2 enables fine-grained diagnosis of model accountability. Our evaluations show that models tend to separate positive and FB samples well but fail on NB samples, while perceptual noise and large rule-induced search spaces pose additional challenges in few-shot settings. Together, these results highlight that visual inductive reasoning remains an open challenge and COCOLogic-V2 provides a concrete foundation for advancing methods in this direction.

---


### 146. [HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration](https://arxiv.org/abs/2606.28215)

**<font color=#1a73e8>作者：</font>** Jiaxin Li, Yuxiang Wu, Zhenkai Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a multi-level human-in-the-loop feedback mechanism, HAT-4D efficiently resolves depth ambiguities and interaction-induced occlusions during 3D generation and 4D propagation, yielding physically plausible assets without relying on expensive multicamera rigs. As a scalable data engine, HAT-4D facilitates the creation of MVOIK-4D, an open-world benchmark for monocular 4D interaction reconstruction, accompanied by a novel multi-dimensional evaluation protocol focused on physical plausibility and temporal consistency. Extensive experiments demonstrate that HAT-4D achieves SOTA performance on most evaluation metrics, while maintaining competitive semantic alignment. Ablation studies show that introducing a small amount of human feedback improves interaction reconstruction. Moreover, the data produced by HAT-4D effectively improves baseline performance when used for fine-tuning. Our data and code are available at this https URL

---


### 147. [Towards Value-Constrained Credit Assignment in Fully Delegated AI Cooperatives](https://arxiv.org/abs/2606.28217)

**<font color=#1a73e8>作者：</font>** Young Yoon, Jimin Kim, Soyeon Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a framework for reward allocation in fully delegated AI cooperatives where humans are represented by agents that contribute data and participate in model updates under heterogeneous value constraints. The key idea is to credit only those updates that remain admissible after screening them against each principal's value profile. We formulate value-conditioned gradient filtering, online marginal contribution signals, and cumulative revenue settlement within a traversal learning (TL) substrate. TL is especially attractive here because it performs decentralized backpropagation without the quality loss associated with aggregation-centric distributed learning and, we argue, offers a finer attribution substrate than FedAvg-style federated learning by preserving explicit traversal and gradient paths. The framework is positioned against data valuation, federated contribution estimation, personalized federated learning, and pluralistic alignment.

---


### 148. [Physics-Informed Neural Network with Transfer Learning for State Estimation in Lithium-Ion Batteries using the Single Particle Model with Electrolyte](https://arxiv.org/abs/2606.28220)

**<font color=#1a73e8>作者：</font>** Gift Modekwe, Qiugang Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have emerged as a powerful tool for solving nonlinear partial differential equations (PDEs), including battery electrochemical models. They typically en-force conservation laws within the loss function to ensure physically consistent solutions. Tradi-tional numerical methods such as finite difference, finite volume, and finite element techniques, re-ly on discretization and can be computationally expensive for nonlinear systems. To address this challenge, PINNs offer improved scalability, particularly for reduced-order models like the single particle model with electrolyte (SPMe). The SPMe describes lithium-ion battery dynamics through coupled diffusion, transport, reaction kinetics, and voltage equations. Despite these advantages, training SPMe-based PINNs from scratch for different battery chemistries or operating conditions is demanding and often leads to slow convergence. To overcome this limitation, this work introduces a transfer learning framework for SPMe-PINNs. The model is first pretrained to learn general elec-trochemical dynamics and then adapted to a target battery by transferring weights, freezing se-lected layers, and fine tuning the remaining parameters, including estimating key electrochemical variables. Validation using PyBaMM demonstrates accurate voltage prediction, indicating that the proposed approach preserves electrochemical consistency while reducing training time and ena-bling efficient generalization across batteries.

---


### 149. [Estimation--Prediction Tradeoff in Causal Probabilistic Temporal Graphs](https://arxiv.org/abs/2606.28225)

**<font color=#1a73e8>作者：</font>** Aniq Ur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal link prediction is usually evaluated by predictive performance on unseen edges, but in probabilistic temporal graphs this criterion can conflate model error with irreducible uncertainty. We study this issue by characterising an inherent estimation--prediction tradeoff in binary logistic models where regimes that maximise Fisher information and improve parameter recoverability are also those with the highest entropy, making individual predictions intrinsically harder even under perfect parameter recovery. We propose a probabilistic causal framework for generating temporal graphs with transient edges and known ground-truth causal structure, allowing temporal link prediction to be evaluated jointly with causal parameter recovery. For the proposed binary logistic parametrisation, we derive the Cramér--Rao bound and validate the tradeoff between parameter estimation error and irreducible predictive loss. Our results show that predictive accuracy alone may not reflect whether a model has learned the underlying causal mechanism, motivating benchmarks that distinguish reducible model error from intrinsic process uncertainty.

---


### 150. [Exposure Bias Can Alleviate Itself via Directional and Frequency Rectification in Flow Matching](https://arxiv.org/abs/2606.28226)

**<font color=#1a73e8>作者：</font>** Guanbo Huang, Jingjia Mao, Fanding Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow Matching (FM) has achieved remarkable generative performance, yet it suffers from exposure bias due to discrepancies between training and inference. Existing mitigation strategies typically rely on static constraints or external heuristics. In this work, we propose that exposure bias itself inherently contains dynamic signals that can guide its own rectification. To leverage this, we introduce DEFAR (DirEctional-Frequency Adaptive Rectification). This framework simulates the single-step inference process during training to identify exposure bias. It utilizes directional and frequency-adaptive feedback signals from the bias itself to enhance the model's bias tolerance. It consists of two key components: (1) Anti-Drift Rectification (ADR). ADR treats inference-time drift as a signal to learn the direction to steer deviated states back toward the target. ADR endows the model with intrinsic active self-rectification capabilities; (2) Frequency Compensation (FC). Empirically, we observe that accumulated bias often stems from a lack of low-frequency components in high-noise stages, and exposure bias carries the missing frequency. FC leverages the bias itself as a self-feedback weighting factor to reinforce the missing frequency components. Experiments on CIFAR-10, CelebA-64, and ImageNet-256/512 show that DEFAR outperforms prior baselines and further demonstrates favorable scalability, compatibility, and inference robustness.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-160](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
