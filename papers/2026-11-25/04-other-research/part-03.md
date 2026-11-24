# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 101. [Centerline-Guided Multi-Class Road Surface Segmentation](https://arxiv.org/abs/2611.28544)

**<font color=#1a73e8>作者：</font>** Xu Ouyang, Lin Gan, Di Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road-surface extraction from satellite imagery supports geo- graphic mapping, but a binary mask leaves road axes, transverse extent, and junction structure implicit. Learning these proper- ties together is challenging because narrow corridors, merging roads, and occlusions require different geometric cues. We present a centerline-guided multi-class segmentation framework that makes these dependencies explicit. A hierarchical encoder sup- plies shared features, while predicted centerline features and soft probabilities condition specialized regular, intersection, and over- pass decoders. A two-component width branch supplies transverse geometry to regular-surface decoding, and learned feature fusion produces the complete road mask. Unlike independent prediction heads or a fixed union of component masks, this design exchanges geometric information during decoding while retaining separately inspectable outputs. Evaluation of the four-semantic-output con- figuration on CHN6-CUG achieves 65.53% complete-surface IoU, improving on a binary SegFormer-B4 baseline by 1.01 percentage points and reducing false-positive pixels by 11.94%. The results support geometry-aware surface refinement and a richer raster representation for road-map inspection.

---


### 102. [Reconstruction-Guided Dual-Branch Learning for LiDAR Anomalous Object Detection](https://arxiv.org/abs/2611.28545)

**<font color=#1a73e8>作者：</font>** Guanyu Jiang, Junjie Cao, Jinshan Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting unexpected objects is essential for autonomous driving safety. Most existing LiDAR anomaly detectors rely on semantic discrimination, which primarily captures category-discriminative features but may overlook deviations from broader feature relationships in normal scenes. Reconstruction offers a complementary perspective by assessing consistency with learned normal patterns. However, pointwise reconstruction errors alone struggle to distinguish anomalies from normal variability in complex outdoor point clouds. We propose Structured Residual Reasoning (SRR) to extract additional anomaly evidence from residual structure across feature channels, time sequences, and geometric space. We further establish that semantic discrimination and normal-pattern reconstruction capture fundamentally different yet complementary anomaly evidence: category compatibility and consistency with learned normal patterns, respectively. At matched background false-positive rates, SRR recovers more objects missed entirely by the semantic branch while producing fewer false positives in normal-only scenes. Building on this finding, we propose Reconstruction-Guided Dual-Branch (RGDB) learning, in which SRR-derived normal-pattern consistency cues guide a semantic-conditioned anomaly decoder to complement reconstruction-based predictions during training. At inference, the two branches jointly exploit their complementary anomaly evidence. Experiments show that standalone SRR establishes a strong reconstruction-based baseline without semantic labels from the target-scene training data, while RGDB achieves state-of-the-art performance on the STU validation set.

---


### 103. [Analyzing Atypical Local Features in Museum Artifacts using Generative Image Inpainting](https://arxiv.org/abs/2611.28549)

**<font color=#1a73e8>作者：</font>** Maho Kinoshita, Wakana Kuwata, Ryota Mibayashi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study proposes a method for analyzing local visual features in museum artifacts that may appear atypical or unexpected. Objects in the same category often share a similar overall shape, while local details such as patterns, decorations, and facial expressions may reflect regional or cultural characteristics. We use the appearance distribution learned by an image generation model as a reference for what is generally expected within an artifact category. For each target region, we exclude images from that region and fine-tune a generative model using only images from the remaining regions. We then mask selected parts of artifact images from the target region and ask the region-excluded model to complete them. If the completed result differs greatly from the original image, the masked part may contain features that are difficult to predict from the appearance learned from other regions. We measure this difference using LPIPS and treat it as reconstruction difficulty for the generative model. We conduct experiments on images of kokeshi dolls, drums, and masks from the collection of the National Museum of Ethnology. For each category, we select several target regions, build region-excluded LoRA models, and perform inpainting on predefined local parts. The results show that typical shapes and simple decorations are often reconstructed consistently, whereas some region-specific colors, patterns, cord arrangements, and painted details are replaced with more common appearances. These results suggest that region-excluded inpainting can serve as an exploratory tool for finding region-specific local visual features in museum artifact images.

---


### 104. [Praxis: Practical Witness Encryption for NP](https://arxiv.org/abs/2611.28552)

**<font color=#1a73e8>作者：</font>** David Tse, Nikhil Vanjani, Psi Vesely  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Witness encryption encrypts a message to an NP statement so that whoever holds a witness can decrypt. Over a decade after its introduction, known constructions for general NP statements are far from practical or rest on heuristic or broken assumptions. We propose Praxis, a practical scheme for NP, and prove it extractable in the bilinear generic group and random oracle models under Module-SIS. Our instantiation encrypts to a Groth16 verifier on BN254, set up honestly, which serves every NP relation at the same cost: at $100$-bit security, its ciphertext is $7.88$ GiB, encryption takes $2^{34.2}$ base-field multiplications, and decryption with a Groth16 proof $2^{33.0}$ on average. We give Lean 4 proofs of correctness and extraction at this instantiation's parameters.
Praxis starts from the rank-gap template of the recent feasibility result [Hair and Sahai, arXiv 2026]. Where they raise the gap to keep decryption polynomial, we fix it, so decryption ends with a search that is exponential but concretely fast: $O(2^{\lambda/4} N^{1/4})$ expected operations for a statement in $N$ Boolean unknowns at $\lambda$-bit security. A quadratic arithmetic program makes our hidden matrix low rank, so where their ciphertext encodes a basis of a matrix space, ours holds factors of width two, which a pairing multiplies. Weights and identities from an extension field tie copies of this matrix, so an adversary telling encryptions apart yields a witness or a Module-SIS solution. For the same Groth16 statement and $100$-bit security level, Praxis reduces the ciphertext size and the cost of encryption of either of their constructions by over ten orders of magnitude, and that of decryption by over six.

---


### 105. [WorldWeave: Rethinking Embodied Navigation through Cross-Task World Modeling](https://arxiv.org/abs/2611.28553)

**<font color=#1a73e8>作者：</font>** Xuan Yao, Jiahao Zhang, Rongjunchen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile embodied agents continuously alter their observations through their own motion, while external dynamics further shape future interactions. Different mobile embodied tasks therefore capture complementary patterns of state evolution, yet jointly learning world dynamics across such interactions remains less explored. We investigate this problem through Vision-and-Language Navigation (VLN) and Embodied Visual Tracking (EVT), which respectively involve navigation toward a stationary goal and interaction with a moving target. We propose WorldWeave, a cross-task world model that couples shared predictive dynamics with task-specific adaptation. Instead of conditioning state transitions on heterogeneous physical actions, WorldWeave learns latent actions from observed state changes via inverse-forward dynamics, establishing a shared transition representation across tasks. The resulting future-state predictions are adaptively integrated into task-specific representations for downstream decision making. Experiments across multiple VLN and EVT benchmarks demonstrate consistent improvements over specialized baselines.

---


### 106. [From atomic events to material degradation across metre and year scales](https://arxiv.org/abs/2611.28559)

**<font color=#1a73e8>作者：</font>** Kun Li, Tian Luo, Haozhi Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Material degradation emerges from microscopic events whose consequences accumulate over years, yet mechanism-resolved simulations remain confined below engineering timescales. The challenge is not just the sheer number of events: atomistic evolution is dominated by recurrent local motion, with only a tiny fraction driving lasting structural change. This distinction is not encoded in an instantaneous atomic configuration. Locally indistinguishable states can exhibit different event competition, escape times, and long-horizon outcomes, revealing missing kinetic context as a critical information bottleneck. This context spans space and time: the future consequence of a local transition depends on its surrounding defect environment and the kinetic history leading to its current state. To solve this, AtomWorld reconstructs a predictive kinetic state from multiscale structural observations and trajectory history, distinguishing transient fluctuations from microscopic pathways that drive persistent structural evolution. Learning operates only over transitions admitted by the underlying kinetic Monte Carlo (KMC) process, preserving event legality, state evolution, and physical time. Across BCC Fe-Cu precipitation, FCC Ni-Cr-Al ordering, and HCP Zr-H interstitial transport, restoring kinetic context consistently advances persistent evolution while maintaining physical fidelity and transferring to unseen conditions. In irradiated reactor-pressure-vessel steel, this approach achieves up to 420-fold greater persistent evolution under matched event budgets. Combined with scalable execution, it successfully extends mechanism-resolved trajectories to service-year timescales across metre-scale heterogeneous domains.

---


### 107. [SAFE-DRIFT: Data Selection for Supervised Fine-tuning with Controllable Off-Target Drifts](https://arxiv.org/abs/2611.28560)

**<font color=#1a73e8>作者：</font>** Yeo Jin Jung, Yating Liu, Lalchand Pandia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose SAFE-DRIFT, a data-selection framework for supervised fine-tuning that improves a target capability while controlling unwanted drift in the model's other behaviors. We formalize this as a constrained optimization problem that maximizes alignment with the target gradient, subject to a budget on off-target drift which we quantify using the Fisher information of a reference distribution. Under this objective, the optimal, closed-form update is a damped natural-gradient step that downweights reference-sensitive directions. To estimate these high-dimensional gradients and work within the right geometry, we further derive a scalable algorithm that approximates the Fisher information and the target gradient in a shared low-dimensional subspace and analyze how entanglement of the target and reference task can affect the update. We evaluate SAFE-DRIFT against state-of-the-art data selection methods across diverse domains including coding and medical question answering, yielding competitive target performance while reducing degradation on specified off-target behaviors.

---


### 108. [Modeling Perceived Promptness in Simultaneous Interpreting from Quality, Structure, and Timing Signals](https://arxiv.org/abs/2611.28566)

**<font color=#1a73e8>作者：</font>** Ziyu Zhang, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous interpreting requires interpreters to convey the source accurately while keeping pace with it in real time. Timing measures such as segment-onset delay capture part of this requirement, but may not fully reflect how professional evaluators judge promptness. We investigate whether these judgments can be explained by timing alone or whether the interpreted output provides additional information. Our dataset contains 622 Chinese-English and English-Chinese segments from 16 source speeches and seven interpreters. Two senior professional interpreters rated each segment for language quality (LQ), expressiveness (EXP), and perceived latency (LAT), which we also refer to as professional promptness. On held-out source speeches, onset delay alone achieves a Pearson correlation of r = .318 with LAT ratings. Combining predicted LQ and EXP with delay improves the correlation to r = .475. Lexical and structural features provide a stronger signal, reaching r = .632 when combined with delay and r = .658 when predicted quality is also included. These results suggest that professional promptness judgments reflect properties of the interpreted output beyond when the interpreter begins speaking. The additional contribution of predicted quality over structural features, however, is modest. Although the two evaluators differ in how strongly quality relates to LAT, cross-evaluator predictions remain positively correlated with LAT ratings. The overall pattern also holds when each interpreter is held out in turn.

---


### 109. [LoopSight: Looped Vision Transformers with Gated Prediction Memory](https://arxiv.org/abs/2611.28575)

**<font color=#1a73e8>作者：</font>** Zhaozhi Wang, Mingrui Wu, Jiaming Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Looped vision transformers extend computation for visual reasoning by repeatedly applying a shared Transformer core. A challenge is to preserve useful prediction information across loop iterations while allowing the computation state to evolve. In this paper we introduce LoopSight, a looped vision transformer that uses Gated Prediction Memory (GPM) to maintain a persistent prediction state for readout, separate from the core's evolving computation state. At each iteration, a cross-attention gate uses the core's candidate features, the previous prediction state, and the current task state to control writes at the patch and channel level. The model decodes its prediction from the updated memory. We condition the shared core on the current iteration using asymptotic loop encoding and train the model by supervising its prediction at loop counts sampled from a truncated Gaussian distribution. LoopSight outperforms LoopViT across three model scales on ARC-AGI-1 and ARC-AGI-2. On ARC-AGI-1, LoopSight-Small achieves 67.4% pass@2, a gain of 6.6 percentage points over LoopViT-Small with comparable parameter counts and FLOPs. LoopSight also outperforms LoopViT on Visual Sudoku and ImageNet classification. Further analyses on ARC-AGI-1 show that LoopSight preserves more already-correct predictions and maintains more stable readout features as its computation state continues to evolve. The code will be released at this https URL.

---


### 110. [Tight Mistake-Abstention Tradeoffs for Sequential Prediction under Adversarial Injections](https://arxiv.org/abs/2611.28579)

**<font color=#1a73e8>作者：</font>** Moïse Blanchard, Ezra Edelman, Surbhi Goel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sequential prediction problem introduced by Goel et al. (2023), where an adversary can inject arbitrarily many corrupted instances in an i.i.d. stream from a clean distribution $\mu$, while the learner is allowed to abstain from making a prediction at no cost if the current instance was indeed injected. When $\mu$ is unknown, Yu and Blanchard (2026) show a polynomial tradeoff between mistakes and false abstentions for classes with finite VC dimension and oblivious adversaries, but still leave open a significant gap between upper and lower bounds in their tradeoff landscape. In this paper, we propose the weighted shattering potential, and based on variants of this potential, provide gap-closing algorithms that essentially characterize the tradeoffs under various settings of interest: When $\mu$ is known, our algorithm improves over Goel et al. (2023) and achieves their conjectured $O(d\log T)$ mistake bound; When $\mu$ is unknown, for oblivious adversary, our guarantees are tight both in $T$ and in terms of the VC dimension $d$, which completely characterizes the abstention-mistake tradeoff in this setting and gives an $O(\sqrt{dT})$ balanced rate. For adaptive adversary, our results are tight up to $\operatorname{poly}(dD\log T)$ factors for structured classes with finite so-called reduction dimension $D$. Our guarantees also extend to censored feedback, where the label is hidden after an abstention.

---


### 111. [CAR3T: Generalizable Calibration-Guided Reference-View Attention Reuse for Multi-View 3D Transformers](https://arxiv.org/abs/2611.28591)

**<font color=#1a73e8>作者：</font>** Lan Wei, Haosong Peng, Sicheng Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward multi-view 3D reconstruction relies on global attention for cross-view aggregation, but the attention cost grows quadratically with the number of views, making inference increasingly expensive for larger inputs. Existing acceleration methods compress tokens or sparsify attention, potentially losing geometric detail or restricting cross-view aggregation while leaving redundancy among attention outputs underexploited. We observe similar cross-view attention distributions in certain layers, revealing an opportunity to reduce repeated global aggregation through output reuse. However, the layers suitable for reuse vary with the input, and reusing one layer alters the features received by later layers. Similarity at individual layers therefore cannot characterize the combined effect of multiple reuse decisions on output drift. To address these challenges, we propose CAR3T, a training-free framework combining reference-view attention output reuse with offline risk calibration and online dynamic layer selection. Calibration models cumulative reuse risk, while online selection adapts reuse to each input under a calibrated budget. CAR3T retains all input tokens and attends to the keys and values of all views, reducing the core attention computation in selected layers from quadratic to linear. Experiments on VGGT, DA3, and $\pi^3$ show forward speedups up to $1.41\times$ with at most 100 views and $1.75\times$ on longer sequences, with accuracy trade-offs across backbones and datasets.

---


### 112. [DRAM: Memory-Efficient Muon via Rank Reallocation in Principal-Random Subspaces](https://arxiv.org/abs/2611.28595)

**<font color=#1a73e8>作者：</font>** Haomin Bai, Dingzhi Yu, Xuling Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-efficient Muon methods aim to reduce storage overhead while preserving strong performance, yet existing approaches compromise either convergence guarantees or practical efficiency. In this paper, we focus on subspace optimization for Muon, where the choice of subspace determines the gradient information retained for updating. To preserve dominant information while providing the coverage needed for stochastic convergence guarantees, we construct a principal-random subspace that combines leading singular directions of the stochastic gradient with random directions sampled from their orthogonal complement. Under a fixed rank budget, there is a trade-off between principal exploitation and complementary coverage, making rank allocation important for practical optimization. Our key observation is that the preferred balance shifts from principal-heavy early in training to random-heavy later. Motivated by this shift, we propose \dram, a memory-efficient Muon optimizer that reallocates principal and random ranks across stages while maintaining momentum and performing matrix-sign normalization entirely in the subspace. Theoretically, we establish convergence guarantees for general rank-allocation schedules with nondecreasing coverage factors, obtaining rates of $O(T^{-1/4})$ in the stochastic setting and $O(T^{-1/2})$ in the deterministic setting, with fixed allocation as a special case. Using a simple linear reallocation schedule, \dram achieves the best low-memory performance across three pre-training scales and nine fine-tuning settings.

---


### 113. [OKB-CFM: Observation-Keyed Barycentric Conditional Flow Matching for Unpaired Sparse-to-Dense Cardiac Shape Completion](https://arxiv.org/abs/2611.28600)

**<font color=#1a73e8>作者：</font>** Kangneng Zhou, Shuang Song, Yitian Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Completing cardiac segmentations from sparse cine magnetic resonance labels is challenging because acquired planes do not uniquely determine the underlying anatomy and patient-matched dense annotations are rarely available. We propose observation-keyed barycentric conditional flow matching for completion between clinically unpaired cohorts. Independently trained variational autoencoders represent sparse observations and dense shapes. A fixed memory associates simulated sparse keys with their source dense encodings, enabling candidate retrieval within the sparse latent space. A matching network aggregates the retrieved values into a query-dependent barycentric endpoint, toward which an endpoint-conditioned flow transports the sparse encoding. Individual candidate values provide alternative completion endpoints. On 327 real unpaired inputs, the method obtains encoder-feature Fréchet and squared maximum mean discrepancy scores of 7.93 and 2.02 after scaling by 10,000 and 10,000,000, respectively, corresponding to reductions of 47.0\% and 94.2\% relative to contrastive unpaired translation. On a 34-file simulated test partition, evaluation against dense-VAE-reconstructed references yields a five-class mean Dice of 0.889, squared Chamfer distance of 6.15 square voxels, 95th-percentile surface distance of 3.88 voxels, and average symmetric surface distance of 1.50 voxels. These results characterize cohort-level feature agreement, observed-label consistency, and reconstruction under the stated reference construction. By complementing routine cine-based functional assessment with inferred multi-chamber anatomical context, this framework provides a basis for investigating how chamber morphology and spatial relationships relate to cardiac function.

---


### 114. [A Model Obfuscation and Controllable Authorization Scheme for Deep Learning as a Service](https://arxiv.org/abs/2611.28602)

**<font color=#1a73e8>作者：</font>** Nianyun Song, Haodi Wang, Yu Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developing deep learning models requires substantial computational and data resources, making them core intellectual assets for enterprises. As Deep Learning as a Service (DLaaS) increasingly extends to edge computing environments, models deployed on third-party devices face growing threats from reverse engineering. Existing model protection methods often depend on specialized hardware or incur substantial computational overhead, while lacking effective mechanisms for controlling model usage. There is therefore a need for lightweight solutions that combine model protection with controllable authorization. To address this challenge, we propose KeyObf, a model obfuscation and controllable authorization scheme for DLaaS. KeyObf efficiently protects model parameters and architecture through model obfuscation while binding parameter recovery to user keys, ensuring that only authorized users can perform inference correctly. By integrating a key-based mechanism into the obfuscation framework, KeyObf unifies model protection and controllable authorization. Experimental results demonstrate that KeyObf preserves the inference accuracy of authorized users, rejects inference requests when credential authentication fails, and increases the difficulty of recovering model information under the evaluated reverse-engineering conditions. These results demonstrate the feasibility of a lightweight approach to model protection and controllable authorization in third-party deployment scenarios.

---


### 115. [VUOD: A Versatile Unsupervised Outlier Detection Framework for Natural, Industrial, Medical Images and Beyond](https://arxiv.org/abs/2611.28608)

**<font color=#1a73e8>作者：</font>** Zhonghang Liu, Siyuan Chen, Jingwen Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised outlier detection that automatically identifies whether visual systems involve anomalous images is a significant research topic. However, most approaches are limited to natural images because they rely on frozen and pre-trained feature extractors. So that their performance cannot be maintained in practical scenarios, especially for industrial inspection and medical imaging. In this work, we first revisit this task and then introduce a versatile unsupervised outlier detection framework to enrich the application domains. The core idea of this framework is to improve feature discriminativess via exploiting intrinsic distribution priors. Evaluated on 3 domains and 14 benchmark datasets, our proposed solution achieves state-of-the-art performance and significantly outperforms existing methods. More importantly, we show its plug-and-play property that can be integrated into diverse visual applications to improve their robustness, such as image classification and 3D reconstruction.

---


### 116. [Action-Conditioned Transition Irreversibility for Out-of-Distribution Detection in Reinforcement Learning](https://arxiv.org/abs/2611.28611)

**<font color=#1a73e8>作者：</font>** Emil Mittag, Richard Dazeley, Peter Vamplew  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning agents shape the observations they encounter; consequently, detecting out-of-distribution (OOD) states requires analysing action-conditioned trajectories rather than treating inputs as independent samples. We propose Action-Conditioned Transition Irreversibility (ACTI), a detector that evaluates forward and backward transition likelihoods, calibrates this comparison against the in-distribution profile at each timestep, and smooths the score over a short window, using no future information. We tested ACTI across six environments and fifteen detectors within OOD-RL-Bench, using the four anomaly mechanisms that qualified in every environment, with ten policy replicates per environment. All primary metrics are matched-time: each score after anomaly onset is compared with a clean twin rollout's score at the same timestep. Our method secured the top macro matched-time AUROC, outperforming the dynamics-model baseline (PEDM), while scoring transitions roughly two orders of magnitude faster. Compared to the state-only variant, ACTI achieved a small but consistent AUROC gain and a shorter detection delay. The capacity-matched forward-only baseline, ACTI-Forward, secured a statistically significant advantage in AUPRC alongside a reduced detection delay. The discrepancy in AUROC did not reach statistical significance. Ablation studies suggest instead that performance improvements stem from action conditioning, calibration at each timestep, and smoothing of the transition-likelihood scores. Based on these results, we recommend using ACTI-Forward.

---


### 117. [Nearly Minimax-Optimal Sample Complexity of Natural Policy Gradient with a Matching Information-Theoretic Lower Bound](https://arxiv.org/abs/2611.28628)

**<font color=#1a73e8>作者：</font>** Asha Barua, Sajad Khodadadian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental question in reinforcement learning is how many sampled transitions are needed to learn a near-optimal policy, and whether direct policy optimization can attain this statistical limit. To answer this question, we consider natural policy gradient (NPG), a widely used policy optimization method. We study tabular finite-horizon Markov decision processes (MDPs) with known rewards and unknown horizon-dependent transition kernels, accessed through a generative model. Our sample-based NPG algorithms update the policy by backward sweeps and do not estimate transition probabilities. Under three different batch-size and step size schedules, we establish last-iterate guarantees with sample complexity $\widetilde O(SAH^4/\varepsilon^2)$, where $S$, $A$, and $H$ denote the number of states, the number of actions, and the horizon length, respectively. In this setting, horizon-dependent transition kernels contribute a factor of $H$ to our transition-query bound. Our information-theoretic lower bound of $\Omega(SAH^4/\varepsilon^2)$ shows that the resulting $H^4$ dependence is unavoidable in the worst case, even for agents that select their queries adaptively. To the best of our knowledge, these are the first last-iterate guarantees for NPG whose sample complexity matches an information-theoretic lower bound up to logarithmic factors. Consequently, our results demonstrate that direct policy-space optimization through NPG can achieve the fundamental statistical limits of reinforcement learning while guaranteeing the performance of the final policy. Furthermore, for known kernels, we prove that exact NPG with a constant step size $\eta=1/H$ requires $\Omega(H^2/\varepsilon)$ iterations in the worst case, matching the known upper bound for that step size.

---


### 118. [Seeing 3D Occupancy Through Scene-Adaptive Projection](https://arxiv.org/abs/2611.28629)

**<font color=#1a73e8>作者：</font>** Yuan Wu, Zhiqiang Yan, Zhengxue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based 3D occupancy prediction infers voxel-wise geometry and semantics from multi-view images, where 2D-to-3D view transformation is a crucial step. Many existing methods adopt a backward-projection paradigm, projecting uniformly distributed 3D reference points onto image planes to aggregate multi-view features. However, their scene-agnostic sampling patterns overlook the non-uniform distribution of scene geometry, allocating many references to empty space and reducing sampling efficiency under a fixed sampling budget. To address this challenge, we propose SAP, a scene-adaptive projection framework that leverages depth-based geometric priors to guide view transformation. Specifically, we back-project metric depth maps predicted by a frozen depth model into 3D space to obtain geometric priors. To leverage these priors, we design a Scene-Adaptive Projection Encoder comprising two complementary components. First, Prior-Guided Reference Generation constructs a hybrid reference set for feature sampling, allocating references within prior-supported height regions and retaining full-range sampling where valid support is unavailable. Furthermore, to account for potential spatial misalignment caused by depth estimation errors, Radial-Structured Feature Aggregation explores multiple candidate locations through learned radial offsets to aggregate potentially displaced feature evidence. Extensive experiments on Occ3D demonstrate that SAP achieves state-of-the-art performance and consistently improves results across diverse occupancy frameworks.

---


### 119. [SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting](https://arxiv.org/abs/2611.28636)

**<font color=#1a73e8>作者：</font>** Yingying Shi, Zhong Zhou, Bin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting provides an efficient representation for high-fidelity rendering of static and dynamic 3D scenes, motivating the copyright protection of Gaussian assets. In CLIP-guided Gaussian watermarking, a universal message decoder pretrained on textual watermark representations is subsequently applied to visual features containing both watermark information and scene-dependent semantics. However, text-only pretraining does not explicitly account for the semantic interference encountered during watermark extraction. To address this challenge, we propose SemGuard, a simple yet effective semantics-decoupled watermarking framework that learns to suppress scene-dependent semantic interference during universal message decoder pretraining. Specifically, SemGuard combines message-related CLIP text features with message-independent visual features extracted from unwatermarked scene images, constructing training representations with controllable semantic interference relevant to the target Gaussian assets. A progressive semantic interference curriculum gradually increases the contribution of visual features, allowing the decoder to first learn reliable message representations and then adapt to increasingly strong scene-dependent semantic interference. After pretraining for a given message length and semantic image pool, the decoder is frozen and reused across multiple Gaussian assets whose visual semantics are covered by the pretraining data. Experiments on static and dynamic Gaussian Splatting assets demonstrate improved rendering fidelity alongside reliable watermark extraction, while evaluations on static assets further show enhanced robustness against image-space distortions.

---


### 120. [OrthoLatentCAD: Orthographic Spatial Latents for Hand-Drawn CAD Program Generation](https://arxiv.org/abs/2611.28646)

**<font color=#1a73e8>作者：</font>** Xiaolei Zhou, Xinjie Zhu, Chuangjie Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Freehand orthographic drawings capture early design intent, yet recovering executable sketch--extrude CAD programs from raster front, right, and top views remains challenging: noisy, dimension-free 2D layouts must be reconciled into an ordered construction history. We introduce Hand2CAD, a benchmark of 215K ABC-derived synthetic orthographic-drawing--CAD program pairs and 1,000 real three-view sets drawn by CAD-trained participants. Recovering CAD programs from orthographic drawings requires both cross-view geometric reasoning and alignment between visual features and program representations. We propose OrthoLatentCAD to address these two challenges. It fuses local geometry with global context on canonical planes, exchanges evidence between paired plane lines indexed by the same shared-axis coordinate, and maps the spatial representation to ordered program latents through queries inherited from a frozen CAD autoencoder. Across the evaluated one- to three-view configurations, OrthoLatentCAD outperforms protocol-matched baselines in procedural accuracy, compiled geometry, and CAD-kernel validity while benefiting from additional views. Without real-data fine-tuning, it also outperforms the baselines on held-out real drawings. We will release the dataset, code, and evaluation scripts.

---


### 121. [Beyond Full-Context Accuracy: Context-Marginalized Evaluation of Test-Time Structure-Aware Inference in EEG-to-Image Retrieval](https://arxiv.org/abs/2611.28648)

**<font color=#1a73e8>作者：</font>** Ke Xiao, Banghua Yang, Yingjie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time structure-aware inference can improve cross-subject EEG-to-image retrieval by exploiting relations among unlabeled test queries, but it also makes predictions depend on query-set composition. Existing evaluations typically report accuracy under a single full-query context, leaving unclear whether gains and comparative conclusions hold as context changes. We introduce Context-Marginalized Retrieval Evaluation (CMRE), which repeatedly evaluates each target query in sampled contexts using the corresponding rows of a fixed query-gallery similarity matrix. CMRE distinguishes structural exploitability, quantified by gains over independent retrieval, from context robustness, measured by same-query Top-1 context consistency. Under leave-one-subject-out evaluation on THINGS-EEG2 across six frozen representations and six structure-aware inference rules, structure-aware inference improves full-context Top-1 accuracy by up to 20.40 percentage points over independent retrieval. However, the rule selected under full-context evaluation is no longer optimal in 17 of 24 representation-context-size conditions (70.8%). Selecting the full-context winner incurs an average loss of 2.70 percentage points and a maximum loss of 8.29 percentage points under reduced contexts. Representation rankings are likewise inference- and context-dependent: the ordering under independent retrieval is not consistently preserved under structure-aware inference. Moreover, larger retrieval gains do not necessarily imply greater context robustness, showing that retrieval effectiveness and prediction stability provide complementary views of structure-aware inference. Full-context accuracy captures one operating point of context-dependent inference. CMRE complements it by characterizing how structural gains, context consistency, and comparisons of rules and representations change with query context.

---


### 122. [Anti OS Fingerprinting, Revisited: A Loadable Kernel Module for FreeBSD and What Twenty-Five Years Changed](https://arxiv.org/abs/2611.28651)

**<font color=#1a73e8>作者：</font>** Daisuke Miyamoto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2001 we published a paper on an Anti OS Detection (AoD) system: a modified FreeBSD 4.3 kernel that makes a host answer the probes of an OS fingerprinting tool as if it ran another operating system. This report revisits that work on FreeBSD 15.1. We do not claim a new method. We report three things. First, the same goal is now reachable from a loadable module of about 800 lines that uses the packet filter hook interface and sets one kernel variable, without changing the kernel source. Second, the module covers both active and passive fingerprinting: Nmap 7.98 reports an exact match for Linux and for Windows 10/11, and p0f 3 reports the same systems from the connections the host opens. Third, an exact match in Nmap was not enough: a passive tool, plain FIN scans and a comparison with real hosts each exposed a mismatch that the previous step could not see. A real Windows 11 host and the final Windows personality get the same verdict from Nmap and the same signatures from p0f and JA4T; a real Linux 7.0 host is not an exact match in Nmap at all, while the personality built from Nmap's database is. We describe those mismatches, how we removed them, what the module costs, and what it still cannot hide.

---


### 123. [InstantCoFFEA: Fast and accurate Tor flow correlation at realistic scale](https://arxiv.org/abs/2611.28653)

**<font color=#1a73e8>作者：</font>** Saeyeon Hong, Hyewon Kim, Mohammad Saidur Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tor end-to-end correlation attacks can link a client to its destination by matching traffic observed at both ends of a Tor circuit. However, their practical threat remains unclear for two reasons: existing correlation methods rely on O(N^2) pairwise processing, and prior works do not reflect the flow counts and base rates seen by realistic adversaries. We present InstantCoFFEA, which replaces exhaustive pairwise search with approximate nearest neighbor (ANN) retrieval using CAGRA and introduces ranked voting. At N = 200k, InstantCoFFEA is 14.56x faster than DeepCoFFEA and improves PR-AUC from 0.94 to 0.96. We also use TorPS to estimate the flow counts and matching-pair base rates observed by relay-level and network-level adversaries. Our simulations show that realistic attacks involve substantially more candidate flows and much lower base rates than those used in prior evaluations. Under a low-base-rate setting, PR-AUC drops for all methods, but InstantCoFFEA achieves 0.53 compared with 0.42 for DeepCoFFEA. These results show that evaluating correlation attacks requires considering both computational scale and the sparsity of true matching pairs.

---


### 124. [Stein Guidance without Gradients: Discretization Uniform Diffusion Inference Time Scaling beyond Particle SMC](https://arxiv.org/abs/2611.28654)

**<font color=#1a73e8>作者：</font>** Youheng Zhu, Chenyang Wang, Minshuo Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-guided diffusion requires effective steering and correction of the bias introduced by approximate value functions. A Brownian example shows that SMC with full multinomial resampling at every step can require particle counts to grow linearly with guidance depth to maintain accuracy. We propose Stein Guidance, which combines derivative-free guidance with whole-path independence Metropolis-Hastings correction. Value-weighted selection from centered Gaussian candidates approximates gradient guidance in expectation, using as few as two queries per step. Centering stabilizes the local normalizer estimates, and the same queries yield an explicit path weight for correction. Under uniform value and spatial regularity bounds, we prove superpolynomial decay of finite-grid total variation error in the number of MH updates, with constants that do not grow with guidance depth. The error prefactor tends to zero as the value functions approach exact Doob values and the time grid is refined.

---


### 125. [UACR: Uncertainty-Aware Collaborative Routing for Explainable Industrial Anomaly Inspection](https://arxiv.org/abs/2611.28655)

**<font color=#1a73e8>作者：</font>** Yiwei Li, Qiyang Chen, Zheming Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly inspection requires not only accurate anomaly discrimination but also trustworthy explanations for operators, while satisfying the strict latency constraints of online inspection. Existing methods, however, typically apply a fixed computational path to all samples, making it difficult to strike a good balance among detection accuracy, inference efficiency, and interpretability. To address this issue, we propose UACR, an uncertainty-aware collaborative routing framework for explainable industrial anomaly inspection. UACR aims to deliver reliable anomaly decisions together with operator-facing explanations under the online inspection budget, while adaptively allocating computation so that ambiguous cases receive deeper scrutiny. The framework consists of two stages. Stage I, Offline Training and Routing Hyperparameter Search, learns the anomaly inspection modules and calibrates the uncertainty estimator that drives routing. Stage II, Uncertainty-Aware Adaptive Routing, collaboratively dispatches each input across inspection paths according to its estimated uncertainty. Experimental results on multiple public datasets show that UACR achieves over 5.16% improvement in accuracy compared to the baseline method, while reducing latency by over 31.5%. It also enhances the interpretability of industrial detection by over 15%.

---


### 126. [Dual-Stream Event-to-Video Reconstruction](https://arxiv.org/abs/2611.28656)

**<font color=#1a73e8>作者：</font>** Lei Sun, Zhendong Li, Chenxin Shao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras capture brightness changes with high temporal resolution and dynamic range, but converting event streams into videos remains fundamentally ill-posed due to the lack of absolute intensity information. Resolving this ambiguity calls for a brightness reference that complements the intensity changes recorded by events. Inspired by the complementary spatial and temporal processing of the parvocellular and magnocellular pathways in human vision, we propose EvDualDiff, a dual-stream framework that combines a brightness reference from temporal-mapping events with motion-event cues for video reconstruction. Conditioned on both streams, our video diffusion model autoregressively reconstructs long sequences from a single temporal map. Photometric constraints and finetuning on self-generated rollouts reduce accumulated drift. At the hardware level, our approach requires only a minimal light-modulation mechanism on the lens of an event camera. We build this setup and collect a dataset comprising temporal-mapping events, motion events and synchronised ground-truth RGB frames. Experiments on a public benchmark and on our collected EvDual dataset demonstrate that EvDualDiff outperforms existing event-to-video reconstruction methods in fidelity, perceptual quality and video-level realism. The code and dataset will be released.

---


### 127. [RecallWorld: Episodic Memory for Persistent Embodied Video World Models](https://arxiv.org/abs/2611.28666)

**<font color=#1a73e8>作者：</font>** Sarosij Bose, Gitika Karumuri, Chenqi Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models generate plausible novel views but often lack persistent memory, failing to preserve a place's geometry and appearance when an agent revisits a scene. A central challenge is how previous views should be effectively used for creating memory. Reconstructing them independently underutilizes geometric constraints between nearby views, while repeatedly reconstructing a growing history can propagate later prediction errors into earlier geometry. We introduce RecallWorld, a persistent embodied video world model that jointly reconstructs short multi-view episodes into Scenelets while keeping geometry independent across episodes. Starting from a single source image, camera-aware ray lifting places perspective and native fisheye images in a common world frame, retaining wide-field content for perspective generation. Each generated segment extends the Scenelet memory and conditions subsequent generation. Coverage-based retrieval selects complementary Scenelets from the full history, while target-view visibility is resolved geometrically before appearance fusion, providing consistent memory conditioning for guiding subsequent generation. Across four datasets, RecallWorld improves revisit PSNR over the strongest evaluated baseline by 2.6 dB on partial revisits and 3.9 dB on full cycles, demonstrating substantially stronger preservation of scene identity across exploration and return.

---


### 128. [Learning Continuous Scene Depth Representations via Cross-Modal Gaussian Rendering](https://arxiv.org/abs/2611.28670)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhong, Lingyu Zhu, Baoliang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth super-resolution with color guidance is a fundamental problem in geometric scene understanding that aims to reconstruct high-resolution depth using structural cues from color images. In practical RGB-D systems, the resolution gap between depth and color images often varies, requiring flexible upsampling factors. However, many existing methods are designed for predefined integer scales. Although implicit methods support arbitrary-scale reconstruction, they typically rely on computationally demanding per-pixel neural decoding and may struggle to recover sharp depth boundaries and fine structures. To this end, we propose a cross-modal Gaussian rendering framework that learns continuous depth representations for arbitrary-scale depth super-resolution. Specifically, we first construct hierarchical Gaussian representations for progressive depth reconstruction, with explicit spatial support defined by learnable Gaussian primitives. Building on this representation, we design a Structure-Aware Gaussian Aggregation module that combines spatial weights with cross-modal feature affinities to reduce aggregation across depth discontinuities. We then develop a Scale-Adaptive Gaussian Rendering module that adapts Gaussian spatial kernels to the target pixel footprint. To further facilitate cross-modal learning, we propose a training strategy that gradually introduces higher-frequency guidance information during training. Extensive experiments on benchmark datasets demonstrate the effectiveness of the proposed method at both in-distribution and out-of-distribution upsampling scales.

---


### 129. [ViewAgent3D: A Training-Free Multi-View Pipeline for 3D Scene Understanding](https://arxiv.org/abs/2611.28673)

**<font color=#1a73e8>作者：</font>** Sarosij Bose, Arindam Dutta, Konstantinos Karydis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene understanding tasks are often approached by building explicit 3D scene representations or by training specialized multi-modal models over point clouds, voxels, or scene graphs. We take a complementary view: for many queries, the main bottleneck is not the absence of a stronger 3D representation but the selection of a small subset of multi-view RGB views that actually makes the query answerable. We present a training-free, query-conditioned multi-view pipeline that performs diverse tasks using only 2D images and a set of tools used purely for inference. Our method first decomposes each query into a set of concepts that identify unique attributes that assist with reasoning. This drives a coarse-to-fine evidence selection process: a coarse retrieval selects and scores all views, a diversity-aware selector reduces redundancy, and a reranking stage helps shortlist views by target visibility or answerability. The resulting evidence is optionally grounded for queries that benefit from explicit localization, and a self-verification step helps refine the final response, especially for open-ended cases. Despite using no task-specific training and no explicit 3D representations at inference time, our approach provides approximately 10% gain on 3D VQA and 5% gain on dense captioning and Embodied QA while being applicable across different scenarios. We further propose a unique judge-based evaluation system, motivating a judge who takes into account many semantically correct or partially correct answers, thereby improving holistic scene understanding.

---


### 130. [CHORD: Closed-loop Human-Object Rectified-flow Decomposition](https://arxiv.org/abs/2611.28682)

**<font color=#1a73e8>作者：</font>** Yi Wang, Yubo Zhao, Chi-Keung Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D human-object interaction (HOI) generation requires synthesizing whole-body human and object motions that stay coupled through contact. Yet existing generators either entangle the core variables that govern an interaction (object pose, contacting regions, and limb posture) with dozens of subordinate joints, or plan only end-effectors or coarse trajectories. No stage of generation holds the interaction in a form that is both settled and observed, which leaves contact to external guidance, post-hoc refiners, or internal guidance without a surface measurement. We present CHORD, a two-stage rectified-flow framework that settles the interaction in a compact plan and observes that plan against the object surface while it is being generated. First, Draft uses twelve part tokens per temporal patch to jointly plan the 6-DoF object trajectory, contact states, and the end and middle joints of every kinematic chain. At each flow step, Draft decodes the expected interaction from the closed-form clean estimate, measures it against the object surface, and routes this feedback to the responsible part token with zero extra network evaluations. Second, Full keeps this plan unchanged and infills the remaining body and finger joints. On InterAct, CHORD reduces FID by 33% and lifts hand contact F1 from 0.730 to 0.834, while its feedback improves contact on unseen objects and transfers plug-and-play to existing HOI generators.

---


### 131. [DeCo: Decoupled Traffic State Modeling with Cross-Variable Coordination](https://arxiv.org/abs/2611.28685)

**<font color=#1a73e8>作者：</font>** Du Yin, Lindong Xie, Xiachong Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate forecasts of traffic flow, occupancy, and speed are essential for congestion management and travel planning. These variables exhibit distinct spatiotemporal patterns, and their coupled dynamics characterize the evolution of traffic conditions, such as the onset and dissipation of congestion. Existing methods often either neglect this coupling or struggle to capture the distinct dynamics of all three variables within a unified model. In this paper, we propose DeCo, a decoupled traffic state modeling framework with cross-variable coordination for forecasting flow, occupancy, and speed. Specifically, DeCo first trains a dedicated forecaster for each variable to specialize in its unique spatiotemporal dynamics. It then estimates a residual correction for each forecast by jointly leveraging the predicted trajectories and recent observations of all three variables, thereby exploiting cross-variable coupling and mitigating systematic prediction errors. We extend the flow-only PeMS03 and PeMS07 benchmarks to all three variables on their original sensors and release the aligned data. Experiments on PeMS03, PeMS04, PeMS07, and PeMS08 show that DeCo achieves the lowest mean absolute error for every variable on every dataset, up to 4.9% below RAGC, the strongest baseline. Code is available at this https URL.

---


### 132. [QUISA: A Compact, Flexible and Unified Instruction-Set Coprocessor for QR-UOV Signature](https://arxiv.org/abs/2611.28687)

**<font color=#1a73e8>作者：</font>** Malik Imran, Ciara Rafferty, Ayesha Khalid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> QR-UOV is a Quotient Ring Unbalanced Oil and Vinegar (UOV) multivariate quadratic (MQ) signature scheme that has progressed to round-3 of the post-quantum cryptography (PQC) additional signatures call by the National Institute of Standards and Technology (NIST). Until now, for architectural efficiency and performance trade-offs, QR-UOV has been evaluated only on software platforms and has never been considered on hardware, such as field-programmable gate arrays (FPGAs). To address this, we are the first to provide a complete QR-UOV hardware implementation through a flexible and unified QUISA coprocessor design, which supports instruction-driven execution for key generation, signing, and verification across all three NIST security levels (SL-I, SL-III, SL-V). The proposed architecture features extensive throughput optimizations by parallelizing key QR-UOV module operations, such as the pseudorandom byte generator, hashing, and rejection sampling. To minimize hardware resources, we propose a modular arithmetic unit with finite-field reduction based on the shift-add folding method. The design introduces a linear system solver for QUISA based on LU decomposition with partial pivoting and a sample solution module, operating over the prime field Fq (q = 127). We comprehensively evaluate QUISA on an Artix-7 FPGA at 80 MHz up to the post-place-and-route stage, utilizing 11,144 slices and 35,248 look-up tables. For higher SL-V security levels, it completes key generation, signing, and verification in 30.4M, 3.8M, and 2.8M clock cycles, respectively.

---


### 133. [Peel, Don't Whack: Partial Coverage, Imperfect Validators, and Intervention Based Shortcut Mitigation](https://arxiv.org/abs/2611.28701)

**<font color=#1a73e8>作者：</font>** Ali Alavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Without group labels, shortcut mitigation increasingly relies on interventions : label-preserving edits, such as background or watermark replacement, that are proposed automatically and accepted by a validator. Invariance to a complete family of valid edits yields robustness, but in practice coverage is partial and validators err.
We analyze both in a stylized linear model. For the population logistic solution and the max-margin limit of gradient descent, the decision on every shortcut-flip group follows one additive rule. Hence worst-group accuracy never decreases with coverage, while individual groups can provably degrade, a mechanism for the Whac-a-Mole effect; full coverage is not always needed. In the logistic regime the validator's false-accept rate must stay below a closed-form tolerance that grows with coverage. With noiseless training data, one false accept can make the max-margin solution ignore the core. In this model, sensitivity-based discovery removes shortcuts in decreasing salience. We also give a model-agnostic certificate, valid under content-independent validation, whose validator-error term comes from an audit.
Simulations match the theory, and deep networks on synthetic and real images show the predicted Whac-a-Mole signs, monotone worst-group accuracy and validator fragility. The resulting procedure, Peel (Propose-Edit-Evaluate-Learn), can propose candidate edits from the model's own mistakes. Given an oracle library of the benchmarks' intervention operators, it selects the right ones and beats group-label methods on Waterbirds and UrbanCars. With fully generated edits, run end to end from three discovery seeds, it improves on empirical risk minimization (ERM) on five of six benchmarks but trails exact edits.

---


### 134. [CoopOcc: Cooperative 3D Semantic Occupancy Perception via Multi-Agent and Cross-Modal Fusion](https://arxiv.org/abs/2611.28710)

**<font color=#1a73e8>作者：</font>** Zengle Zhu, Zhen Li, Tianyi Huai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic occupancy perception has emerged as a promising paradigm for jointly modeling 3D scene geometry and semantic information. However, this unified representation cannot compensate for missing information caused by occlusion and sensor coverage. Multi-agent cooperation alleviates this limitation, but information from different agents is not equally useful across spatial regions. Meanwhile, feature representations from each agent form the basis of reliable multi-agent fusion. Cross?modal fusion constructs such representations by integrating complementary semantic and geometric information. Despite this complementarity, jointly establishing reliable 3D correspondence across agents and preserving modality-specific structures remains challenging. To address these limitations, we propose CoopOcc, which performs cooperative 3D semantic occupancy perception through multi-agent and cross-modal fusion. CoopOcc uses ego?query cross-agent attention (EQCA) to selectively aggregate aligned features across agents, and anchor-based bidirectional feature interaction (ABFI) for cross-modal exchange at matched coordinates. We further construct SemanticVVSim, a simulation dataset, and establish a unified benchmark. For simulation-to-real transfer, we propose confidence-aware hierarchical occupancy and relational distillation (CHORD). CoopOcc performs best overall among ten evaluated methods on SemanticVVSim. On Occ3D-nuScenes, CHORD improves performance using knowledge from SemanticVVSim. The code is available at this https URL.

---


### 135. [When Local Semantics Disagree: Learning to Detect Fake News through Weakly Supervised Cross-Modal Reasoning](https://arxiv.org/abs/2611.28711)

**<font color=#1a73e8>作者：</font>** Zeheng Wang, Hao Zhang, Yige Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of multimodal social media content has made fake news detection a pressing challenge for the vision-language community. Most existing approaches rely on coarse global similarity between text and images, which overlooks subtle, uneven cross-modal inconsistencies -- such as sentiment-scene mismatches, object-level manipulations, or semantic dissonance between visual and textual cues. Moreover, these models treat all inconsistencies as equally informative, ignoring domain-specific variation in how such conflicts manifest, which limits both generalization and interpretability. To address these challenges, we propose DMIL, a dual-branch multiple instance learning framework that formulates multimodal fake news detection as a weakly supervised learning problem. Each news article is treated as a bag of visual and textual instances processed through two complementary branches: an embedding-space branch that aggregates global semantics via expert-guided modality fusion, and an instance-space branch that models cross-modal inconsistencies across local-to-global granularities. A retrieval-augmented, domain-adaptive router further contextualizes inconsistencies using retrieved domain exemplars and dynamically fuses multi-level cues. Extensive experiments on public misinformation benchmarks demonstrate that DMIL achieves competitive state-of-the-art performance and demonstrates strong discriminative capability against fake news across different domains.

---


### 136. [Domain-Specific Self-Supervised Learning for Cuneiform Sign Representation](https://arxiv.org/abs/2611.28712)

**<font color=#1a73e8>作者：</font>** Asim Niaz, Morris Alper, Shai Gordin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing cuneiform signs is challenging: sign shapes vary across historical periods, scribal practices, and preservation conditions, while expert annotations are scarce. We study whether domain-specific self-supervised pretraining yields better cuneiform sign representations than generic natural-image pretraining. We pretrain a masked autoencoder, CuneiMAE, on over 900K unlabeled sign crops and compare it with ImageNet-pretrained MAE, CLIP, and DINOv2 on a 218-class sign recognition benchmark. CuneiMAE learns substantially stronger frozen representations (43.7% linear-probe accuracy vs. 25.2% for ImageNet-MAE), with gains over ImageNet-MAE on cross-period transfer. Under fine-tuning, CuneiMAE outperforms ImageNet-pretrained baselines on our internal benchmark, with the largest gains when labels are scarce (+20.4 pp over ImageNet-MAE with 1% of labels). On an external benchmark, CuneiMAE reaches 69.9% top-1 accuracy after fine-tuning, about 8 pp above the ResNet-18 baseline from prior work. Explicit structural priors, such as edge-guided masking and part bottlenecks, do not improve over standard masked reconstruction. Overall, domain-specific self-supervision shows strong performance on cuneiform recognition tasks, particularly when labels are limited.

---


### 137. [DynFlux: Learning to Dynamically Balance Consensus and Conflict in Multimodal Emotion Recognition](https://arxiv.org/abs/2611.28716)

**<font color=#1a73e8>作者：</font>** Zeheng Wang, Hao Zhang, Yige Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition remains challenging due to the intrinsic heterogeneity of different modalities. Effectively leveraging both cross-modal consensus (consistency) and conflict (inconsistency) is essential, as they jointly provide complementary cues that enhance emotion understanding from diverse perspectives. Traditional multimodal methods often suffer from semantic ambiguity and rarely explicitly model the interplay between cross-modal consensus and conflict. Moreover, existing approaches struggle to capture and exploit the dynamic interactions between these two complementary factors. To overcome these limitations, we propose DynFlux, a model guided by a temporal heterogeneous graph that encodes both consensus and conflict relationships across modalities. DynFlux introduces a dedicated graph branch that explicitly captures cross-modal dependencies through sparse temporal graphs, and modulates the conventional multimodal emotion recognition pipeline at three hierarchical stages: adaptive feature modulation during feature extraction, guided aggregation modulation during feature integration, and fusion strategy modulation at the multimodal fusion stage. Through this design, DynFlux dynamically balances cross-modal consensus and conflict, enabling richer and more robust emotion understanding. Extensive experiments on benchmark datasets confirm that DynFlux consistently outperforms state-of-the-art methods, and its generality is further validated on multimodal intent recognition and multimodal sarcasm detection tasks.

---


### 138. [ReCoRain: Reliability-Coupled Content and Noise Conditioning for Event-Guided Video Deraining](https://arxiv.org/abs/2611.28717)

**<font color=#1a73e8>作者：</font>** Runzhe Li, Zhaocheng Yu, Binbin Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-guided video deraining depends on reliable cross-frame correspondences, yet events generated by scene motion, rain, and sensor noise can provide ambiguous matching evidence. In diffusion-based restoration, an incorrect match can transfer unrelated content and correlate initial noise between unrelated scene locations. We propose ReCoRain, an event-guided residual video diffusion framework that couples temporal content transfer and noise correlation through a common assessment of correspondence reliability. This assessment combines RGB appearance, interval-event evidence, and forward-backward motion consistency. The content path aggregates neighboring features according to alignment reliability, while the noise path uses composed backward motion fields and their associated reliability estimates to regulate initial-noise sharing across the latent sequence. We use the same conditional noise construction during residual flow-matching training and inference, incorporating temporal noise coordination into the learned restoration process. Temporal supervision matches motion-compensated inter-frame differences in restored and clean videos under the same teacher-estimated flow and visibility mask, accommodating legitimate appearance changes. ReCoRain achieves 32.09 dB PSNR on NTURain-Syn and 28.73 dB on RainSynLight25. Enabling reliability gates in both paths reduces warping error by 33.0% relative to disabling both gates.

---


### 139. [AERIN: Aerial Instance Navigation with a Visual World Model](https://arxiv.org/abs/2611.28723)

**<font color=#1a73e8>作者：</font>** Zhenzhen Jiao, Rui Tian, Zhineng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Searching from high altitude and navigating to a target instance specified by a reference image is a common application for UAVs. In such tasks, high-altitude observations provide broad ground coverage for efficient search, but targets occupy fewer pixels, making instance verification and action selection more difficult. We present AERIN, a visual world model that uses action-conditioned prediction to guide the UAV toward the target while adjusting its viewpoint to obtain higherquality observations for subsequent instance verification. Highaltitude navigation requires fine-grained target details and scene context relevant to visibility, but repeatedly predicting dense visual representations of this information is computationally expensive. AERIN addresses this challenge with a compact, fixedsize, target-conditioned latent state that separately represents both for efficient action evaluation. Experiments demonstrate that AERIN outperforms the evaluated baselines in target approach and observation quality, while requiring substantially less decision time than similar world models.

---


### 140. [How many mistakes does it take to learn an interval? Exact Littlestone dimensions of intervals and their unions](https://arxiv.org/abs/2611.28727)

**<font color=#1a73e8>作者：</font>** Miit Daga, Swarna Priya Ramu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Littlestone dimension of a hypothesis class equals the smallest number of mistakes an online learner can guarantee against an adaptive adversary. For discrete intervals and unions of $j$ intervals on $m$ points, only its order of growth was known. We determine it exactly. For every switch budget $k$ (with both end labels fixed when $k$ is odd), the smallest size on which $d$ mistakes can be forced follows a three-regime law: $d+1$ while $d\le k$, then $2d-k+1$, and beyond $d=\lceil 3k/2\rceil+k-1$ doubling the size adds exactly $k$ mistakes. Unions of $j$ intervals on $m$ points correspond to $k=2j$ and size $m+1$, and a single interval gives the thresholds $1,2,3,5,7,10,14,20,\dots$. The natural learner that waits for a positive example and binary-searches both endpoints is not optimal: it can be forced into one extra mistake for 50,847 of the domain sizes below $10^5$. Upper bounds come from a gap potential and a block-pairing learner, and lower bounds from adversary strategies and a refinement step. These tools give an explicit optimal learner with $O(\log m)$ time per round, which on random streams makes more mistakes on average than the natural learner. For randomised learners, we compute the randomised Littlestone dimension of thresholds exactly and prove that a greedy adversary forces an explicit closed-form number of expected mistakes on intervals; this bound is within $0.64$ of optimal and, we conjecture, exact (confirmed for $m\le70$). Exact computation tests every result, and the formulas for every switch budget are machine-checked in Lean 4.

---


### 141. [Dynamic Spectrum Re-parameterized Convolution for Cost-free Image Enhancement](https://arxiv.org/abs/2611.28736)

**<font color=#1a73e8>作者：</font>** Zhiyan Zhou, Hailong Yan, Hanlin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image enhancement spans degradations with distinct spectral characteristics. Standard convolutions use fixed kernels, whereas dynamic convolutions gain adaptability at additional inference cost. We propose Dynamic Spectrum Re-parameterized Convolution (DSRC), a plug-and-play module that learns task-adaptive spectral responses during training while retaining standard convolution at inference. DSRC decomposes convolution kernels into frequency bands, applies learnable high/low-pass modulation, and incorporates lightweight residual branches. Owing to the linearity of these operations, all training-time components are analytically fused into a single kernel for inference. Experiments on low-light enhancement, underwater enhancement, and image super-resolution show consistent PSNR gains and generally improved or preserved SSIM and LPIPS across twelve backbone-task configurations, with unchanged deployed parameter counts and theoretical FLOPs, and no additional inference operators.

---


### 142. [Learning Optical Flow with Task-Oriented Feature Adaptation](https://arxiv.org/abs/2611.28744)

**<font color=#1a73e8>作者：</font>** Mengtan Zhang, Dazhong Wang, Haoran Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based optical flow estimation approaches generally rely on both inter-frame correspondence evidence and intra-frame contextual guidance, yet features from general-purpose image encoders may not fully support these roles. Strongly activated but weakly discriminative channels can outweigh more informative ones when computing inter-frame feature similarity, while context feature affinities can be low within motion-coherent regions yet high across motion boundaries. To address these mismatches, this study proposes TO-Flow, a task-oriented feature adaptation framework that aligns matching and context features with their respective requirements through dedicated channel modulation and spatial reorganization approaches. An affinity-based soft partition distinguishes motion-region interiors from boundary-adjacent regions to guide both processes. Channel modulation uses simulated flow refinement to assess whether each channel assigns higher similarity to estimated correspondences than to nearby competing candidates. The resulting similarity differences are aggregated within each region type and averaged across iterations to derive channel weights that emphasize informative channels and suppress ambiguous ones. Spatial reorganization combines affinity-guided feature attraction and repulsion from coarse to fine to simultaneously improve consistency within motion-coherent regions and distinctiveness across motion boundaries, with feature resampling mitigating boundary blurring during cross-scale fusion. Extensive experiments on the MPI Sintel, KITTI 2015, Spring, and LayeredFlow datasets demonstrate the effectiveness and general applicability of TO-Flow across diverse iterative refinement architectures as well as supervised and unsupervised training paradigms. The source code will be publicly available at this https URL upon publication.

---


### 143. [UNIFY: Unified Learning with One Model via Batch Norm Switching](https://arxiv.org/abs/2611.28746)

**<font color=#1a73e8>作者：</font>** Shaharyar Ahmed Khan Tareen, Xiaojing Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural networks are typically trained separately for individual datasets or tasks, resulting in many task-specific models. This redundancy increases memory footprint, deployment costs, and energy consumption limiting their scalability. We propose UNIFY, a unified learning framework that enables a single model to jointly learn and perform inference across multiple datasets via Batch Normalization Switching (BNS). Instead of maintaining separate models for each dataset, UNIFY shares the parameter-intensive backbone while maintaining dataset-specific BN statistics and parameters, along with dataset-specific classification heads. We validate our framework using five datasets (MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100, Tiny-ImageNet) across six Convolutional Neural Networks (CNNs) of different sizes (SqueezeNet 1.1, WideResNet-40-2, WideResNet-16-8, ResNet-18, ResNet-34, ResNet-50). Notably, a single UNIFIED ResNet-34 trained on these datasets achieves accuracies of 99.53%, 94.84%, 96.12%, 80.32%, and 67.67%, respectively, outperforming the average performance of the corresponding independently trained task-specific models while reducing the memory footprint by approximately 4.94x, from 428.30 MB (five separate models) to 86.71 MB (one unified model). UNIFY aims not only to consolidate (K) models into a single model but also to enhance model-effectiveness by leveraging complementary knowledge across datasets. It paves the way for scalable, efficient, and unified learning capable of handling diverse image classification tasks. Code is available at: this https URL.

---


### 144. [From Pairwise to Collective: Encoder Collections Make Unpaired Vision-Language Alignment Reliable](https://arxiv.org/abs/2611.28753)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Shunqi Mao, Chuanzhi Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Strong vision and text encoders can be trained independently, but their representations are not directly comparable. Connecting them usually requires paired image-text data, which may be unavailable. Unpaired alignment instead fits a map between a vision and a text encoder from feature-space geometry alone, enabling text-based retrieval and zero-shot classification without paired data. Treating each pair independently leads to fragile searches, repeated fitting, and uncertain map quality. A collection of encoders supplies additional supervision: all vision encoders embed the same images and all text encoders the same texts. Correspondences within each modality are therefore known exactly, while the cross-modal correspondence remains hidden. ConsensusAlign pools each modality into a shared space, fits one unpaired cross-modal bridge, and transfers it in closed form to every encoder pair. New encoders join through same-modality fitting without repeating the cross-modal search. On 21 vision-text encoder pairs and five seeds, pooled fitting aligns every pair, whereas pairwise fits fail in 68 of 105 pair-seed cells. Mean alignment error (FOSCTTM) falls from 0.1457 to 0.0099, and zero-shot accuracy nearly doubles on ten datasets. Gains persist across the tested within-modality pooling constructions with a WP bridge. New corpora reuse the bridge through native maps fitted to unlabeled target features from every source encoder. Agreement with separately fitted reference maps detects failures on COCO.

---


### 145. [PSC-Gen: Physical Sequence Conditioning for Video Generation via Agentic Visual Planning](https://arxiv.org/abs/2611.28756)

**<font color=#1a73e8>作者：</font>** Wonsik Shin, Jinju Jang, Junhoo Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models have enabled the synthesis of high-fidelity, visually compelling videos. However, despite being trained on internet-scale video data, understanding underlying physical laws and generating physically plausible dynamics remain challenging. To mitigate this, conditioning video generators on explicit physical reasoning has emerged as a promising direction. Nevertheless, existing conditioning approaches often fail to incorporate detailed physical guidance into generation, resulting in physically implausible motion or visual artifacts. We propose PSC-Gen, a training-free framework that employs an agentic approach to synthesize visual conditions and inject their core dynamics via low-frequency filtering. By iteratively planning physical states and verifying generated keyframes, our Physics Agent constructs visually and physically consistent keyframe sequences. We then interpolate these keyframes into a continuous physical sequence and inject only its low-frequency components, steering the video model to preserve physical dynamics while synthesizing fine visual details. Qualitative and quantitative evaluations across physics-informed and robotic manipulation benchmarks demonstrate that PSC-Gen faithfully follows instructions and generates physically plausible videos.

---


### 146. [The Complexity of Oracle-Efficient Realizable Transductive Learning](https://arxiv.org/abs/2611.28757)

**<font color=#1a73e8>作者：</font>** Changlong Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In realizable transductive online learning, the learner knows the entire sequence of $T$ instances in advance, and the labels are consistent with one of $N$ hypotheses. With explicit access to the hypothesis class, the halving algorithm makes at most $\log_2 N$ mistakes. Can a comparable guarantee be achieved using only polynomially many empirical risk minimization (ERM) queries? We answer this question negatively, even for a weighted-ERM oracle that optimizes arbitrary real-valued linear objectives and returns a complete maximizing hypothesis. For every fixed $\beta\in(0,1)$ and every randomized learner making polynomially many oracle queries, there exists a fixed realizable instance with exactly $N=2^{\lfloor T^\beta\rfloor}$ hypotheses on which the learner makes $\Omega_\beta(\sqrt{T\log N})$ mistakes in expectation. This matches the agnostic-rate upper bound achieved by random playout using $O(T)$ oracle calls. The separation persists for much smaller classes as well: along a sequence with $\log N=\Theta((\log T)^2)$, we establish a mistake lower bound of $\exp(\Omega(\log T/\log\log T))$. Our main technical contribution is a composition lemma that combines two realizable prediction problems such that their mistake lower bounds add, up to a small loss, while their hypothesis class sizes grow only additively. Iterating this lemma yields a family of hard instances spanning the desired parameter regimes, establishing a sharp separation between information-theoretic and oracle-efficient mistake guarantees.

---


### 147. [Operating-Condition Normalization in C-MAPSS: Matched Historical Baselines, Multi-Seed Robustness, and Prognostic-Score Trade-offs](https://arxiv.org/abs/2611.28759)

**<font color=#1a73e8>作者：</font>** Mohammad Adeel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operating-state changes can obscure turbofan degradation signals, but a reduction in remaining-useful-life (RUL) error after condition-wise standardization may reflect weaknesses of the comparison features instead of a unique benefit of normalization. A controlled retrospective audit examines NASA C-MAPSS FD002 and FD004 with engine-disjoint folds, raw condition identifiers, two constructions of causal history, early-life baselines, and continuous operating-setting correction. Ridge regression, random forests and XGBoost are compared under explicit training-engine-only fitting rules. The previously reported XGBoost FD004 terminal RMSE decreased from 30.38 to 29.08 cycles following six-condition standardization; however, raw sensor values accompanied by condition-matched histories and condition identifiers achieved 28.09 cycles, reversing the naive point estimate ranking, although the paired-engine interval spans zero. For FD002, normalized XGBoost reduced terminal RMSE yet increased the asymmetric NASA score (12,616 to 13,289). Additional model-seed, condition count, RUL-cap, grouped-validation and explanation checks test sensitivity rather than postulating a universally optimal representation. The six clusters reproduce known simulator operating regimes; no new condition discovery algorithm, causal diagnostic method, or field ready prognostic system is claimed. Since the official test endpoints were also used in earlier exploratory comparisons, all newly examined alternatives are reported as retrospective benchmark evidence, not as results from a pristine confirmatory holdout.

---


### 148. [Frozen by the Mean: Early Temporal Guidance Unfreezes Motion in Video Diffusion Models](https://arxiv.org/abs/2611.28762)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Boyu Wei, Chengkun Yue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models can render convincing frames while failing to produce the requested action. Increasing classifier-free guidance (CFG) can strengthen motion, but also saturates and shifts colors. Scalar CFG assigns the same coefficient to the averaged and frame-varying components of its prediction difference, limiting independent control of temporal variation. THAW, Temporal Harmonic Amplification during Warm-up, retains stock CFG and adds a separately weighted residual during an initial denoising window. Its dose specifies the added norm relative to the current CFG difference, giving the extra guidance a consistent relative budget across sampling steps. THAW is training-free and reuses CFG's two model predictions with an unchanged network evaluation count. It improves cost-matched motion over scalar and scheduled CFG on five video models, with positive point estimates against existing guidance methods on three of them. On VBench, THAW raises dynamic degree by about 14 to 15 points over stock CFG while increasing total scores on a different set of three models.

---


### 149. [Contrastive Gradient Guidance for Test-Time Multi-Preference Alignment of Diffusion Models](https://arxiv.org/abs/2611.28764)

**<font color=#1a73e8>作者：</font>** Po-Yi Lu, Jui-Chao Lu, Paul Kuo-Ming Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning pre-trained diffusion models with multiple context-dependent preferences requires adapting generation at test time rather than relying on offline fine-tuning, which requires hyperparameter tuning and a new training run for each preference trade-off. Existing approaches compress diverse preferences into a single scalar reward objective for fine-tuning or test-time guidance rather than directly reusing existing generative experts released for different purposes and obtained through different fine-tuning methods. In this work, we propose Contrastive Gradient Guidance (CGG), a test-time compositional generative framework that reformulates multi-preference alignment as a composition of distributions. CGG represents each preference as a contrastive preference pair of favored experts and unfavored anti-experts, whose score difference forms a contrastive gradient guidance signal that combines denoising directions (gradients) from off-the-shelf diffusion models during sampling. Experiments show that CGG reuses pre-trained and fine-tuned models as favored experts or anti-experts to control output style and safety, and that it can be combined with existing sampling-based reward guidance. With a single fixed scale per pair, CGG composes five preferences at once and gives a more balanced trade-off across text-image preference, concept control, photographic fidelity, and safety than offline fine-tuning, weight-space merging, and reward steering.

---


### 150. [AdapToC: A Unified Framework for Multi-Task Visual Token Communication](https://arxiv.org/abs/2611.28775)

**<font color=#1a73e8>作者：</font>** Zhicheng Liu, Chenliang Wu, Zhouxiang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained discrete visual tokenizers supply compact latents for synthesis, recognition, and embodied perception, yet wireless token streaming remains fragile. Under fading and noisy pilots, hard cyclic redundancy check (CRC) erasures turn corrupted blocks into missing tokens while frozen decoders amplify edge errors, which can collapse unequal error protection (UEP) into a binary choice between strong coding and omission under severe fading. Soft bit posteriors break this collapse. We present AdapToC, a single-pass transceiver that restores multi-tier rate-distortion tradeoffs without altering tokenizer weights or differentiating through pixel decoders. We align codebook geometry to the channel via offline frequency-weighted Pseudo-Gray relabeling and Halton dispersion to contract bit and burst errors with zero overhead. Because soft recovery pulls intermediate rates onto the three-tier convex hull, our unit-gated AdaLN sender schedules protection tiers across channel budgets, while our pilot-calibrated receiver feeds factorized codebook posteriors into a ConvNeXt-attention restorer with CRC bypass. We co-train AdapToC solely in latent space via counterfactual utility estimation and codebook cross-entropy regularization. On identical VQGAN-f16 tokens, AdapToC outperforms TONIC and adaptive TokenCom+AMC, cuts multi-SNR Rayleigh LPIPS from 0.6551 to 0.3312 within the frozen-tokenizer PSNR ceiling, and saves 43.8% Rician-K6 symbols at matched quality. Our single-pass restorer runs 8.3x faster than iterative resampling, raises accuracy while accelerating decoder-free recognition 20.6x, and improves fidelity plug-and-play across TiTok, VAR, and zero-shot NuPlan.

---


> [!TIP]
> 当前位于：**101-150**（第 3/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
