# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 201. [Score $\times$ Decoder: A Unified View of Unsupervised Inference-Time Scaling for Hallucination Mitigation](https://arxiv.org/abs/2606.00739)

**<font color=#1a73e8>作者：</font>** Yun-Chen Cheng, Che-Yu Lin, Cheng-Lin Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate even when the answer lies within their parameters. While inference-time scaling can surface this latent knowledge, the most effective methods require supervision: a trained verifier or reward model. We ask what can be done with only a base language model: which intrinsic signal best identifies correct outputs, and how should it be decoded? We cast this as a score~$\times$~decoder grid pairing four scores (perplexity, contrastive, power-distribution likelihood, and self-verification) with three decoding families (optimization, sampling, consensus), and evaluate every cell on MATH500 with the base and instruction-tuned Qwen3-1.7B. While self-verification, which prompts the model to judge its own answer and is sharpened by a training-free virtual-thinking prefix, works well in most settings, no score has a fixed quality: its value depends on the decoder that consumes it and on model capability. When no supervision is available, the score and the decoding family must be chosen together.

---


### 202. [Quantum Tunneling-Aware Machine Learning: Physics-Derived Noise Models for Robust Deployment](https://arxiv.org/abs/2606.00741)

**<font color=#1a73e8>作者：</font>** Uiwon Hwang, Jaeho Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transistor scaling is approaching a quantum-mechanical limit, as thin gate oxides induce electron leakage through quantum tunneling. Unlike conventional digital systems, AI inference can tolerate such errors provided their structure is modeled correctly. In this paper, we introduce quantum tunneling-aware machine learning (QTAML). We derive the deployment-time weight-error distribution from first principles using the Wentzel-Kramers-Brillouin (WKB) approximation and show that it has structure that generic Gaussian noise models miss: an exact affine mean drift, a per-bit variance hierarchy dominated by the most-significant bit, and a per-layer dependence on $\|W_\ell\|_\infty$ and the trained-network Jacobian. We package these three structural properties into a single deployment-time algorithm, Tunneling-Aware Compensation (TAC), that combines closed-form mean correction with an optimal layer-adaptive bit-budget allocation derived from the WKB variance decomposition. Across four convolutional architectures at $p_\mathrm{flip}$=0.10 and a transformer encoder at $p_\mathrm{flip}$=0.05, TAC reaches $95\%$ of clean accuracy with 3.4$\times$ to 33.6$\times$ less ECC overhead than Uniform-MSP, the natural baseline derived from the same physics. The closed-form saturation ratio $\rho^*$ predicts these gains in advance, and on heterogeneous architectures WKB-derived scoring outperforms magnitude-based allocation by up to 24 percentage points at small budgets. The algorithm requires no retraining, no labels, and no inference-time overhead. We also verify the WKB-derived distributional theorems to Monte Carlo precision. These results connect WKB tunneling physics with noise-aware deep learning and suggest a principled path toward hardware--software co-design beyond conventional scaling limits.

---


### 203. [Scaling Parallel Sequence Models to Foundation-Scale Vision Encoders](https://arxiv.org/abs/2606.00746)

**<font color=#1a73e8>作者：</font>** Yitong Jiang, Hongjun Wang, Collin McCarthy 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models are bottlenecked by the quadratic cost of self-attention, which limits usable resolution and increases the cost of large-scale pretraining. Subquadratic alternatives such as linear attention and state-space models reduce this cost, but often serialize images into 1D token streams and weaken the 2D spatial structure important for vision. Generalized Spatial Propagation Networks (GSPN) instead propagate context directly on the 2D grid through line-scan recurrences, achieving near-linear complexity without positional embeddings, but have seen little use as foundation-scale encoders.
We present C-GSPN, a foundation-scale vision encoder based on 2D spatial propagation. C-GSPN makes the operator practical through three improvements: (1) a fast GSPN CUDA kernel that fuses per-step launches into a single warp-specialized implementation with shared-memory tiling, coalesced access, and a compact multi-channel propagation, reaching over 90% of peak memory bandwidth and running up to 40--52x faster than the original GSPN implementation; (2) a compressed latent-space propagation block with fused normalization, which turns kernel-level speed into block- and model-level efficiency; and (3) a two-stage cross-operator distillation recipe that trains the new architecture from an attention teacher without the cost of from-scratch foundation-scale training. Distilled with 600M image-text pairs, C-GSPN matches an isomorphic ViT baseline with 15% fewer parameters, improves ADE20K segmentation by +2.1%, transfers to high resolution with a fraction of the data needed from scratch, and delivers a 4x end-to-end block speedup at 2K with single-pass, tiling-free inference.

---


### 204. [SkyShield: Occupancy as a Safety Interface for Low-Altitude UAV Autonomy](https://arxiv.org/abs/2606.00747)

**<font color=#1a73e8>作者：</font>** Jie Gao, Jie Ma, Kaihui Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For low-altitude Unmanned Aerial Vehicle (UAV) autonomy, 3D spatial understanding is not merely a perception objective, but the safety interface between human instructions and physical flight. In human-scale urban airspace below 20 meters, thin geometry, occlusions, vegetation, and urban clutter define whether an aerial agent can safely enter the space ahead. However, existing UAV datasets mainly provide 2D annotations or 3D boxes, while driving-oriented occupancy benchmarks assume stable ground-level sensor rigs. Both miss the defining regime of low-altitude flight: a front-facing monocular camera observing occupied and free space from a moving aerial body with frame-wise changing 6-DoF pose and camera extrinsics. To bridge this gap, we introduce \textbf{SkyShield}, to the best of our knowledge the first front-view monocular semantic occupancy benchmark for urban UAV flight below 20 meters. Built on CARLA, SkyShield contains 36K front-view UAV samples across diverse urban scenes and weather conditions, pairing each image with frame-wise 6-DoF UAV pose, frame-wise dynamic camera geometry, UAV states, and front-frustum semantic occupancy labels. We further propose \textbf{KAR-mIoU}, a UAV-centric and dynamics-aware metric that re-weights voxel-level evaluation by kinematic reachability and time-to-collision, revealing safety-critical risks hidden by conventional mIoU. To tackle this challenging new setting, we provide \textbf{SkyOcc}, a geometry-first monocular baseline that integrates frame-wise UAV attitude into projection, fuses temporal occupancy features, and applies safety-prior optimization to preserve sparse collision-critical structures. Together, SkyShield, KAR-mIoU, and SkyOcc establish occupancy as a safety interface for low-altitude aerial autonomy. Code and dataset will be released publicly.

---


### 205. [Head-Pose-Aware Visual Speech Recognition with FiLM Modulation](https://arxiv.org/abs/2606.00751)

**<font color=#1a73e8>作者：</font>** Matthew Kit Khinn Teng, Haibo Zhang, Takeshi Saitoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Speech Recognition (VSR) aims to recognize speech from visual cues such as lip movements, but its performance is fundamentally limited by viseme ambiguity and pose-induced variations that introduce geometric distortions and occlusions. Existing approaches mainly rely on linguistic context or implicit invariance, leaving visual representations insufficiently robust under non-frontal views. In this work, we propose a pose-aware phoneme-level framework, termed HP-VSR-ResFiLM, that explicitly incorporates head-pose information into visual feature extraction. The proposed framework adopts a two-stage pipeline consisting of a pose-conditioned visual encoder in Stage 1 and a pretrained NLLB language model in Stage 2 for phoneme-to-text reconstruction. Specifically, Stage 1 incorporates a pose-conditioned residual Feature-wise Linear Modulation (FiLM) block after the 2D CNN frontend to adaptively refine visual representations using head-pose information. Experiments on LRS2 and LRS3 demonstrate that HP-VSR-ResFiLM achieves competitive performance under comparable training conditions, attaining word error rates (WER) of 25.0% and 33.2%, respectively, without relying on additional training data. Ablation studies further show that a single residual FiLM block consistently improves overall WER, while deeper modulation at Layers 3 and 4 provides larger gains for samples with yaw angles greater than 30° without degrading performance for smaller pose variations. These findings demonstrate that explicit pose-aware feature modulation offers an effective and computationally efficient solution for improving VSR robustness in unconstrained settings.

---


### 206. [Internalize the Temperature: On-Policy Self-Distillation as Policy Reheater for Reinforcement Learning](https://arxiv.org/abs/2606.00755)

**<font color=#1a73e8>作者：</font>** Xuewei Yang, Jiachen Yu, Jie Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards improves the reasoning ability of large language models, but often suffers from entropy collapse, in which increasingly concentrated policies reduce rollout diversity and useful learning signals. Existing remedies either constrain the RL objective (e.g., entropy regularization) or adjust sampling temperature during rollout collection, but these interventions remain external to the model parameters. We propose Temperature-Scaled On-Policy Self-Distillation (TS-OPSD), a lightweight policy reheating method that internalizes the exploratory effect of temperature into model parameters. Starting from an entropy-collapsed RL checkpoint, TS-OPSD constructs a self-teacher by applying high-temperature scaling to the model's own logits, then distills the resulting smoother distribution back into the student. This policy reheating requires no external teacher, privileged data, or additional inference cost. Experiments on Qwen3-4B-Base and Qwen3-8B-Base show that policy reheating yields a stronger initialization for continued RL than both standard continued RL and rollout-level temperature reheating. Further analyses show that TS-OPSD mainly reduces output sharpness while preserving intermediate representations, top candidate sets, and reasoning capability. These results suggest that entropy restoration can serve as a simple post-collapse intervention for extending reasoning-oriented RL.

---


### 207. [RADE: Random Add-Drop Edge as a Regularizer](https://arxiv.org/abs/2606.00757)

**<font color=#1a73e8>作者：</font>** Danial Saber, Amirali Salehi-Abari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) suffer from overfitting and over-squashing of long-range information. Stochastic graph augmentations (e.g., edge deletion) regularize training against overfitting but can introduce train-inference misalignment and do not improve over-squashing. In contrast, rewiring methods improve connectivity to mitigate over-squashing, but are not designed to regularize training. We propose Random Add-Drop Edge (RADE), a stochastic graph augmentation method that jointly drops and adds edges to address both overfitting and over-squashing simultaneously. RADE is provably designed to align training and inference so that random augmentations regularize training without distribution shift, while supporting long-range communication at inference. We further propose and study a mini-batch gradient-norm balancing algorithm that adapts deletion and addition rates during training, rendering RADE hyperparameter-free in practice. Experiments on node- and graph-classification benchmarks show that RADE is a strong regularizer and mitigates over-squashing. Ablations support the roles of train-inference alignment, adaptive rate selection, and the complementary effects of random edge deletion and edge addition.

---


### 208. [Distributed GNEP Algorithms without Multiplier Sharing and Applications to Multi-Robot Coordination and Contextual Bandit-Based Active Learning](https://arxiv.org/abs/2606.00759)

**<font color=#1a73e8>作者：</font>** Shao-An Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in artificial intelligence have expanded the focus from classical optimization to include equilibrium analysis in noncooperative games. Many such games involve shared constraints, leading to Generalized Nash Equilibrium Problems (GNEPs). Existing distributed algorithms typically require agents to exchange Lagrange multipliers to enforce consensus and compute variational-GNEs (v-GNEs).
This work introduces fully distributed continuous-time algorithms and establishes convergence without requiring multiplier exchange, thereby reducing information exchange per iteration while improving privacy preservation. The analysis focuses on strongly monotone games with convex individual constraints and linear shared constraints. I also propose several discretization schemes for the continuous-time algorithms. The proposed approach converges to general GNEs, rather than being restricted to v-GNEs, with the attained equilibrium depending on the initialization. The effectiveness of the proposed method is demonstrated through applications in multi-robot coordination and placement.
In the second part, this work includes research conducted in collaboration with Amazon scientists. One of the most challenging problems in real-world machine learning is labeled data collection, which typically requires substantial human effort and cost. Active learning aims to reduce this labeling requirement. Existing handcrafted active learning strategies, however, generally perform well only on specific types of datasets, which are often unknown in advance. In this work, I propose using contextual bandits to adaptively select the most suitable active learning strategy. The effectiveness of the proposed approach is demonstrated on publicly available external datasets.

---


### 209. [Confidence-Adaptive SwiGLU for Mixture-of-Experts](https://arxiv.org/abs/2606.00761)

**<font color=#1a73e8>作者：</font>** Shaohua Li, Xiuchao Sui, Xiaobing Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> SwiGLU has become a standard gated activation in modern Transformer MLPs, yet its gate sharpness -- the smoothness and selectivity of the gating function -- is typically fixed throughout training. In this work, we propose Confidence-Aware SwiGLU ($\kappa$-SwiGLU), a variant of SwiGLU for Mixture-of-Experts (MoE) models that adjusts expert gate sharpness according to token-level routing confidence. Specifically, $\kappa$-SwiGLU parameterizes the SiLU gate sharpness coefficient as a learnable function of the router logit, enabling each expert gate unit to interpolate between smooth, broadly active gating and sharp, selective gating. We evaluate $\kappa$-SwiGLU on the FineWeb-Edu dataset across MoE Transformer models ranging from 8 to 28 layers. Across these settings, $\kappa$-SwiGLU improves mean CORE performance while adding negligible parameters and incurring only a small computational overhead, demonstrating that confidence-aware gate sharpness is a promising mechanism for improving MoE MLPs. The code is available at this https URL.

---


### 210. [Logit Distillation on Manifolds: Mapping by Learning](https://arxiv.org/abs/2606.00771)

**<font color=#1a73e8>作者：</font>** Yiru Yang, Junling Wang, Nishant Kumar Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A simple way to improve the performance of almost any machine learning model is not to train a single but several models with diverse algorithms which will make slightly distinct kinds of predictions and errors on the same data, and thus improve the average predictions and robustness. However, making predictions using a whole ensemble of models is cumbersome and computationally too expensive to allow deployment to a large number of users, especially if the models are large neural nets. In response to this, we introduce a layer and point wise projection mapping, which maps student and teacher representations into an aligned high-dimensional embedding space during training process. The proposed approach combined with LoRA injection reduces the student model trainable parameters to less than 1% of the teacher model, while significantly improving word error rate (WER) compared to other distillation methods, as demonstrated in ablation studies. Unlike a mixture of experts, our method can be trained rapidly and in parallel.

---


### 211. [GIRL-DETR: Gradient-Isolated Reinforcement Learning for Video Moment Retrieval](https://arxiv.org/abs/2606.00775)

**<font color=#1a73e8>作者：</font>** Shihang Zhang, Mingjin Kuai, Ye Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Moment Retrieval (VMR) task requires accurately localizing temporal boundaries aligned with natural language queries, but many models suffer from a misalignment between continuous surrogate losses and non-differentiable metrics, leading to optimization stagnation during the late stages of training and trapping boundary predictions in suboptimal solutions. Although Reinforcement Learning (RL) post-training successfully optimizes localization results for large models, applying it directly to lightweight networks easily disrupts the fragile feature representations established during the supervised phase. To overcome this optimization bottleneck, we propose Gradient-Isolated Reinforcement Learning for DETR (GIRL-DETR), introducing RL post-training into a lightweight temporal localization framework for the first time. The input video and text features first establish early alignment through Cross-Modal Interaction (CMI) before entering the transformer encoder. Subsequently, a Text-Guided Gating (TGG) mechanism dynamically injects semantic priors into the queries before the transformer decoder generates candidate proposals, providing high signal-to-noise ratio inputs for temporal prediction. After the supervised training reaches convergence, the backbone network is frozen to protect the feature manifold, while the detection head directly optimizes the non-differentiable evaluation metric tIoU to enhance localization accuracy through a Three-stage Progressive Reinforcement Learning (TPRL) strategy. This approach achieves an orthogonal decoupling of state representation and metric optimization. Experiments on Charades-STA, QVHighlights, and TACoS demonstrate that GIRL-DETR effectively resolves surrogate loss degradation and achieves substantial accuracy improvements with minimal parameter updates, providing a robust new pathway for RL applications in lightweight VMR models.

---


### 212. [Latent Diffusion Pretraining for Crystal Property Prediction](https://arxiv.org/abs/2606.00776)

**<font color=#1a73e8>作者：</font>** Shrimon Mukherjee, Kishalay Das, Partha Basuchowdhuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast and accurate prediction of crystal properties is a central challenge in new materials design. Graph neural networks and Transformer-based models have emerged as powerful tools for this task due to their ability to encode the local structural environment of atoms within a crystal. However, these models are data-hungry, and in practice, labeled data for crystal properties are scarce. Pretraining-finetuning strategies, particularly those based on diffusion models, have shown promise in addressing these limitations. In this work, we introduce a novel latent diffusion based pretraining framework, CrysLDNet, designed to mitigate data scarcity. Our approach integrates a Variational Autoencoder (VAE) with a diffusion model during the pretraining stage. The VAE encoder maps 3D crystal structures into a smooth latent space within which the diffusion process is applied. This latent diffusion pretraining enables the graph encoder to effectively capture structural and chemical semantics from large-scale unlabeled data, which can then be finetuned for specific property prediction tasks. Comprehensive experiments on popular DFT datasets for property prediction reveal that CrysLDNet significantly outperforms both training-from-scratch and pretrained baselines, with improvements of 4.26% and 4.90% on the JARVIS and MP datasets, respectively. Additionally, the learned representations remain robust in sparse-data conditions and are expressive enough to correct DFT errors when finetuned with limited experimental data. Code is available at: this https URL.

---


### 213. [DINO-GFSA: Geo-Localization via Semantic Gated Fusion and Mamba-based Sequential Aggregation](https://arxiv.org/abs/2606.00784)

**<font color=#1a73e8>作者：</font>** Beier Hu, Yuanshen Guo, Jialu Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization (CVGL) is critical for Unmanned Aerial Vehicle (UAV) self-positioning and target localization in GNSS-denied environments. However, acquiring robust semantics while preserving finegrained spatial details remains challenging. To address this, we propose DINO-GFSA, a framework leveraging a LoRA (Low-Rank Adaptation) adapted DINOv3 (ViTL) backbone for parameter-efficient, high-capacity representation. Crucially, we introduce a Semantic Gated Residual Fusion module, which utilizes high-level semantics to selectively calibrate and integrate low-level spatial cues, effectively bridging the semantic gap. Furthermore, a Mamba-based Sequential Aggregation Head is designed to capture long-range spatial dependencies with linear complexity. Experiments demonstrate state-of-the-art performance on University-1652 and DenseUAV benchmarks, notably surpassing the previous best on DenseUAV by 3.48% on Recall@1. These results validate DINO-GFSA as a generalized, robust solution for UAV CVGL.

---


### 214. [Extending Causal Metamodeling to a non-Markovian Queue](https://arxiv.org/abs/2606.00795)

**<font color=#1a73e8>作者：</font>** Pracheta Amaranath, Anant Bhide, David Jensen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Metamodels for discrete-event simulations approximate the behavior of simulation models without running expensive simulations. Prior work introduced modular dynamic Bayesian networks (MDBNs) -- a class of metamodels that can estimate a range of probabilistic and causal queries (PCQs) using a single, trained model -- but the method was limited to Markovian systems. In this paper, we initiate an extension of MDBNs to non-Markovian queues by approximating non-exponential distributions using phase-type distributions. This approach raises novel challenges, including balancing metamodeling accuracy and tractability when choosing the number of phases, efficiently learning metamodel parameters, and choosing the sampling interval that is used to approximate a continuous-time simulation by a discrete-time MDBN. We provide preliminary solutions to these challenges, yielding the first causal metamodeling technique for non-Markovian systems. Experiments on a G/M/1 queue demonstrate that the MDBN can produce accurate answers to PCQs with orders-of-magnitude speedup of inference times relative to direct simulation.

---


### 215. [DASH: Dual-Branch Score Distillation for Guidance-Calibrated Compact Diffusion Models](https://arxiv.org/abs/2606.00798)

**<font color=#1a73e8>作者：</font>** Abdullah Al Shafi, Kazi Saeed Alam, Sk Imran Hossain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter compression of class-conditional diffusion models reveals an underexplored limitation in output-level distillation: the unconditional score branch remains unsupervised, leaving the classifier-free guidance gap underdetermined in the student. This gap, amplified at every denoising step, admits degenerate solutions where both branches collapse toward identical predictions, rendering guidance ineffective despite low output-level training loss. This paper introduces DASH, a dual-branch distillation framework that independently supervises both score branches, uniquely specifying target branch outputs for each training sample through independent branch constraints, with an anchor term regularising conditional predictions toward ground-truth noise. The framework further introduces TIRT Transfer, which copies the teacher's converged per-timestep importance curriculum into the student as a frozen prior, eliminating the need to relearn it within limited distillation budgets. Experiments on CIFAR-10 and CIFAR-100 demonstrate that 5.9x compression maintains quality within 4 FID points of the teacher at 50-step DDIM sampling, considerably outperforming training from scratch with guidance fidelity well preserved. Ablation studies confirm that unconditional supervision is the dominant contribution, accounting for over 60% of total distillation gain. Curriculum transfer and anchor regularisation provide complementary benefit, together validating dual-branch constraints as empirically essential for guidance-preserving compression.

---


### 216. [Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems](https://arxiv.org/abs/2606.00804)

**<font color=#1a73e8>作者：</font>** Thanh Luong Tuan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Enterprise multi-agent systems increasingly expose multiple coordination patterns, but deployments often lack evidence for when to use consensus, debate, synthesis, or a simpler single-agent workflow. This paper evaluates whether coordination strategy should be selected dynamically by problem class rather than fixed globally. We run a frozen matrix of 30 enterprise tasks spanning six industries, five problem classes, four execution conditions, three replications per cell, and four model arms: qwen_local, sonnet, gemma_openrouter, and an auxiliary openai cloud-validation arm. All 1,440 generated outputs are judged by a fixed Sonnet rubric.
The main finding is bounded and operationally useful, but it is not the original strict H1. The pre-registered exact-winner/CI criterion is not supported: exact winner identity is unstable across model arms, and several predicted strategies are close to, but not above, the best observed alternative. A weaker near-best routing claim is strongly supported. In every pre-registered model arm and problem class, and again in the auxiliary OpenAI validation arm, the predicted strategy is within 0.10 quality-score points of the best observed condition. Structured compliance verification is the clearest exception to the original mapping: all arms favor single_agent rather than consensus. A pre-registered Kendall's W test finds no reliable difference between Vietnamese-domain and English-domain tasks in how consistently the four coordination conditions are ranked (mean W of 0.20 in both strata; signed-rank p = .85), so H2 is not supported. We conclude that enterprise coordination policy should use dynamic routing as a calibrated default, not as a deterministic winner-selection law.

---


### 217. [Interaction-Centered Intelligence: Toward Interaction as the Primary Unit of Analysis in Co-Creative AI and Human-AI Systems](https://arxiv.org/abs/2606.00807)

**<font color=#1a73e8>作者：</font>** Nicholas Davis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional artificial intelligence has largely conceptualized intelligence as isolated computation occurring within bounded agents. Across classical AI, machine learning, and many generative systems, the dominant unit of analysis remains the individual model or autonomous system evaluated through outputs, benchmarks, prediction accuracy, or optimization performance. While these approaches have produced major advances, they often under-theorize the role of interaction in the emergence of intelligence, creativity, meaning, and adaptive behavior. This paper proposes interaction as the primary unit of analysis for co-creative AI and interaction-centered intelligence more broadly. Drawing from distributed cognition, embodied cognition, enaction, participatory sense-making, human-computer interaction, and computational creativity, the paper traces a historical progression toward increasingly relational accounts of intelligence. Building upon prior work in Creative Sense-Making, quantified co-creation, and co-creative systems such as the Drawing Apprentice and AI Drawing Partner, it argues that intelligence emerges through evolving interaction dynamics among agents, environments, and socio-technical systems rather than solely through internal computation. The paper introduces Interaction-Centered Intelligence as a framework for understanding human-AI co-creation, collaborative emergence, adaptive participation, and interactional dynamics. Rather than evaluating intelligence solely through generated outputs, the framework emphasizes interaction trajectories, coordination patterns, participatory engagement, adaptive regulation, and interactional drift unfolding through time. Implications for explainable co-creative AI, hybrid intelligence, enactive AI, and future human-AI systems are discussed.

---


### 218. [Safe-Subspace Pseudo-Label Refinement for Source-Free Graph Domain Adaptation](https://arxiv.org/abs/2606.00808)

**<font color=#1a73e8>作者：</font>** Yingxu Wang, Xinwang Liu, Siyang Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Source-free graph domain adaptation (SF-GDA) aims to adapt source-trained graph models to unlabeled target graphs when source graphs are no longer accessible. A central obstacle is pseudo-label reliability: under feature and topological shifts, source-induced predictions may become confidently wrong, and indiscriminate self-training can amplify systematic errors through graph message passing. This paper studies SF-GDA from a selective pseudo-labeling perspective. Instead of assuming globally bounded pseudo-label noise over the entire target domain, we identify a confidence-consistent safe subspace on which pseudo-label noise can be controlled under restricted posterior discrepancy, and derive a target-risk decomposition that separates safe-subspace fitting error, selected-label noise, and uncertain-set risk. Guided by this analysis, we propose SafeSubspace Pseudo-Label Refinement (S$^2$PLR), a source-free graph adaptation framework that applies hard pseudo-label supervision only to target graphs supported by both semantic and structural evidence. Specifically, S$^2$PLR estimates semantic reliability using source-committee confidence and disagreement, learns a targetintrinsic structural representation via graph contrastive learning, verifies pseudo-labels through neighborhood consistency, and exploits the remaining uncertain samples with noise-tolerant soft regularization rather than unreliable hard labels. Experiments on image and real-world graph benchmarks under different domain shifts demonstrate that S$^2$PLR achieves robust and competitive performance across diverse source-free transfer settings.

---


### 219. [NBQ: Next-Best-Question for Dynamic Profiling](https://arxiv.org/abs/2606.00809)

**<font color=#1a73e8>作者：</font>** Yimin Shi, Clarice Wang, Haixun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world conversational settings for knowledge discovery, including podcasts, hiring screens, and marketplaces, require a purpose-driven understanding of a person. We study the Next-Best-Question (NBQ) problem: at each turn, an interviewer should ask the question with the highest expected information gain given what has already been learned and the conversation goal. We propose NBQ, a plug-and-play framework that seeds a diverse pool of candidate questions, maintains a compact and continuously updated user state, adaptively selects the next question within a turn budget, and distills the resulting free-form dialogue into a structured vector-based user profile. As a demanding application, we instantiate NBQ for reciprocal matchmaking, where compatibility must be mutual and each person is modeled by both self-description and counterpart-preference representations. To support large-scale matching, we further introduce QuickMatch, an efficient retrieval layer that recasts reciprocal matching from quadratic pairwise scoring to approximate vector search. Experiments show that NBQ improves user profiling quality by up to 13.6% and 14.0% in AC@T and AR@T, respectively, while QuickMatch accelerates retrieval by up to 22.9x with recall up to 0.989.

---


### 220. [A Comparative Analysis of Machine Learning Algorithms for Multi-Task Prediction of the Parameters of the Pectin Hydrolysis--Extraction Process](https://arxiv.org/abs/2606.00821)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov, Shavkat Yo. Kholov, Zainiddin K. Muhiddin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study addresses the challenge of controlling a complex, multi-parameter technological process -- pectin hydrolysis--extraction -- using machine learning methods. The experimental foundation is a unique database comprising 1,000 laboratory experiments conducted under controlled conditions on seven types of plant raw material with four variable process factors (temperature 85--130 C, pressure 0.9--2.2 atm, holding time 3--10 min, pH 1.5--2.0). Four output characteristics were recorded: pectin yield, galacturonic acid content, molecular weight, and degree of esterification. To solve the multi-task regression problem, 11 algorithms were trained and compared: regularised linear models, ensemble methods (Random Forest, Gradient Boosting, XGBoost, CatBoost, Extra Trees), k-nearest neighbours, support vector regression, and a multilayer perceptron. The best results were demonstrated by CatBoost (average R-squared approximately 0.946 after hyperparameter optimisation). Feature importance analysis revealed the dominant role of the raw material type (63.6% of total importance), followed by temperature and holding time. The developed pipeline was exported in a production-ready format and deployed as an interactive web interface. The findings demonstrate that ensemble methods combined with rigorous statistical analysis and interpretable AI significantly reduce the need for physical experiments and form the basis for intelligent pectin production control.

---


### 221. [ErgoGlide: A Wearable Trackball Device for Ergonomic Text Entry in Virtual Reality](https://arxiv.org/abs/2606.00823)

**<font color=#1a73e8>作者：</font>** Muhammad Abu Bakar, Yu-Ting Tsai, Muhammad Imran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In virtual reality, it is challenging to achieve satisfactory text entry speed/accuracy, ergonomics, usability, and learnability. To address this issue, we developed ErgoGlide, a novel lightweight and compact wearable device that facilitates text entry tasks in virtual environments. The proposed ErgoGlide can be regarded as a small trackball that is wearable on a user's finger like a ring. By using ErgoGlide with a hive-like virtual keyboard, the user can rotate the ball for key selections, making text entry intuitive and accurate. We conducted three user studies to evaluate ErgoGlide and found that key confirmation techniques have significant effects on text entry speed and the hive-like keyboard design significantly reduced thumb movements. Furthermore, ErgoGlide can significantly improve typing accuracy, ergonomics, and usability over previous text entry methods. Experimental results also indicated that the typing speed of ErgoGlide can be notably improved after training.

---


### 222. [SuperMemory-VQA: An Egocentric Visual Question-Answering Benchmark for Long-Horizon Memory](https://arxiv.org/abs/2606.00825)

**<font color=#1a73e8>作者：</font>** Samiul Alam, Shakhrul Iman Siam, Michael J. Proulx 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI glasses present a compelling platform for AI agents to serve as personalized memory assistants. To be genuinely useful, such systems must move beyond short-term video comprehension and address memory gaps that humans experience for practical, personal, or social purposes over longitudinal egocentric video streams. However, existing egocentric datasets predominantly focus on action recognition or generic QAs from short clips, measuring perceptual capabilities rather than realistic human memory needs. We introduce SuperMemory-VQA, an egocentric visual question answering (VQA) dataset for evaluating AI assistants on practical, long-horizon memory tasks. It contains 52.9 hours of everyday activities recorded with AI glasses, including synchronized RGB video, audio transcription, eye gaze, IMU, and SLAM trajectories. Through a human-verified annotation pipeline, we construct grounded 4,853 question-answer pairs that span object and location memory, intent recall, visual scene recall, timeline reconstruction, conversational memory, and in-context retrieval. Each question is posed as multiple-choice with an explicit "unanswerable" option to test hallucination robustness. Benchmarking leading agentic frameworks and LLM backbones reveals that existing systems remain far from reliable on real-world memory tasks, highlighting the need for new architectures for grounded AI memory that can answer only when evidence is sufficient. A participant survey further supports that our questions are realistic, useful, and aligned with everyday memory needs.

---


### 223. [Partial Fairness Awareness: Belief-Guided Strategic Mechanism for Strategic Agents](https://arxiv.org/abs/2606.00826)

**<font color=#1a73e8>作者：</font>** Xinpeng Lv, Chunyuan Zheng, Yunxin Mao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strategic machine learning investigates scenarios where agents manipulate their features to receive favorable decisions from predictive models. To address fairness concerns intrinsic to strategic classification, recent work has introduced group-specific fairness constraints. However, current fairness-aware approaches face a fundamental dilemma in the issue of fairness exposure: making these constraints public enables strategic manipulation and can lead to fairness reversal, while keeping them hidden may reduce social welfare and discourage genuine improvement. To fill this gap, we subsequently propose the problem of partial fairness awareness (PFA), as our theoretical analysis informs that such a dilemma can be mitigated by releasing the candidate set of fairness constraints and concealing the grounding constraint. To be specific, we introduce a belief-guided strategic mechanism, wherein agents iteratively interact with the decision system and maintain a belief distribution over the candidate set of fairness constraints. This belief-guided process enables agents, through iterative interaction and feedback, to update their belief distribution over the candidate set, thereby gradually aligning their belief with the grounding fairness constraint employed by the system. Extensive experiments on real-world and synthetic datasets demonstrate that PFA achieves lower group fairness gaps, higher acceptance of truly qualified individuals, and more stable outcomes compared to fully public or private fairness regimes.

---


### 224. [Beyond Independent Manipulation: Individual Fairness-aware Strategic Classification with Peer Imitation](https://arxiv.org/abs/2606.00827)

**<font color=#1a73e8>作者：</font>** Xinpeng Lv, Chunyuan Zheng, Yunxin Mao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strategic classification (SC) investigates scenarios where agents manipulate their features to obtain favorable decisions from predictive models. Existing fairness-aware SC approaches primarily focus on group fairness and typically assume that agents respond independently. However, when individual fairness is required, ensuring similar individuals receive similar outcomes, agents' manipulation becomes interdependent: an agent's preferred manipulation depends on the neighborhoods' outcomes. This induces a mismatch between classical SC formulations and fairness-aware decision settings, where independent models no longer accurately characterize strategic manipulations. To address this issue, we introduce individual fairness-aware strategic classification (IFSC), a framework that models peer-driven manipulation arising from individual fairness, where agents imitate nearby positively decided peers to obtain favorable outcomes. IFSC characterizes strategic manipulation as similarity-based imitation toward visible accepted peers and learns classifiers under the resulting post-manipulation distributions. To account for uncertainty in peer observability, IFSC employs a robust learning process that introduces stochastic perturbations during manipulation simulation. Experiments on synthetic and real-world datasets demonstrate that IFSC improves individual-fairness consistency and mitigates imitation-induced distortions.

---


### 225. [RoboStressBench: Benchmarking VLM Robustness to Physical Visual Stress in Embodied Scenes](https://arxiv.org/abs/2606.00828)

**<font color=#1a73e8>作者：</font>** Leyi Wu, Yifan Zhao, Jinjie Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown strong visual understanding and are increasingly deployed in embodied AI systems, where reliable perception under real conditions is essential. However, existing benchmarks assess VLMs using clean images or isolated perturbations rather than stresses caused by physical scene formation. This design has two limitations: it covers only a narrow subset of everyday visual stresses, and some perturbations rarely appear in realistic embodied scenes. This gap raises a fundamental question: how can we define visual stress in a principled way that captures the diverse factors encountered in physical environments? To address this question, we formulate visual perception from an inverse graphics perspective and introduce RoboStressBench, a benchmark for evaluating VLM robustness to physical visual stress in embodied scenes. Inspired by the physical rendering equation, RoboStressBench decomposes visual stress into four physically grounded dimensions: Material (M), Viewpoint (V), Lighting (L), and Geometry (G). This design enables RoboStressBench to cover a broad range of visual stresses in real-world environments, while allowing controlled analysis of their effects on VLM capabilities such as visual recognition, reasoning, and planning. Through comprehensive evaluations of state-of-the-art VLMs, we identify stress-specific failure modes and reveal that different physical factors degrade different embodied capabilities, which are often obscured by aggregate accuracy. We further introduce a stress-aware agentic solver that detects visual stressors and invokes visual-editing skills before reasoning, improving robustness in high-stress scenarios. Overall, RoboStressBench provides a principled evaluation framework for diagnosing and improving VLM perception under real-world physical stress, supporting the development of more reliable embodied AI systems.

---


### 226. [Subliminal Learning is a LoRA Artifact](https://arxiv.org/abs/2606.00831)

**<font color=#1a73e8>作者：</font>** Todd Nief, Harvey Yiyun Fu, Mark Muchane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subliminal learning is a phenomenon where language models can transmit behavioral traits to other models through seemingly innocuous data (Cloud et al., 2025). In subliminal learning, a teacher model with a behavioral trait (e.g. obsession with cats) can transmit this cat obsession to a student model finetuned only on numerical sequences generated by the teacher. In this paper, we ask: how does this unexpected behavioral transmission occur? We show that subliminal learning is a LoRA artifact. When subliminal learning occurs, transmission has an inverted U-shaped relationship with LoRA rank; it also disappears with full finetuning. We show that subliminal learning is highly dependent on the context seen during finetuning and evaluation. For example, a Qwen model with the default system prompt during finetuning ("You are Qwen, created by Alibaba Cloud. You are a helpful assistant.") does not show subliminal learning during generation when no system prompt is included. We further demonstrate that subliminal behavior is localized to computation at tokens seen during both finetuning and evaluation (e.g. the model's default system prompt, the standard chat template tokens, etc.). Overall, subliminal learning seems to be a fragile artifact of LoRA hyperparameters and finetuning context, making it an unstable channel for behavioral transmission.

---


### 227. [Online Packet Scheduling with Deadlines and Learning](https://arxiv.org/abs/2606.00835)

**<font color=#1a73e8>作者：</font>** Gianmarco Genalti, Achraf Azize, Vianney Perchet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network routers that enforce Quality-of-Service (QoS) guarantees must decide, at every clock cycle, which expiring packet of information to transmit, even when the value of the packet is unknown until it is processed. We frame this problem as the Online Packet Scheduling with Deadlines (OPSD) problem under Partial Feedback: packets arrive at every clock cycle, with different deadlines, but the weights are only observed after execution. Under a stochastic assumption on the unknown weights, we explore different variants of the OPSD problem with bandit feedback. We establish a connection between our setting and the sleeping bandits problem, and set our learning goal to $\alpha$-regret minimization. We provide algorithms with provable $\alpha$-regret guarantees under different spans of slackness, distinguishing systems allowing for randomization and systems that do not. In every scenario, our algorithms achieve an $\alpha$-regret upper bound of $\widetilde{\mathcal{O}}\left(\sqrt{KT}\right)$, matching the lower bound for the standard bandit setting. In the practically relevant case of $2$-bounded deadline instances, where the deadline is set at most one clock cycle away from the arrival, our deterministic algorithm achieves the provably tightest possible competitive ratio. Remarkably, when the number of distinct packet types $K\ge 2$ is finite, it is possible to break the well-established $\Phi = \frac{1+\sqrt{5}}{2}$ competitive ratio barrier and attain a tighter competitive ratio $\theta_K$ ranging in $[\sqrt{2}, \Phi)$.

---


### 228. [Decoupled Behavioral Cloning for Scalable Inductive Generalization in RL from Specifications](https://arxiv.org/abs/2606.00838)

**<font color=#1a73e8>作者：</font>** Vignesh Subramanian, Subhajit Roy, Suguman Bansal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inductive generalization is a framework for reinforcement learning (RL) generalization in which inductively related task instances admit inductively related policies. Prior work captures this structure via a higher-order policy-evolution function learned directly with RL, but suffers from poor training scalability: as training tasks grow, aggregated reward feedback becomes noisy and conflicting, destabilizing training and weakening generalization. We propose DIBS, a decoupled behavioral cloning approach that separates learning task-specific policies from learning the evolution function. We first learn individual teacher policies per task via standard RL, then fit the evolution function via behavioral cloning on teacher-labeled state-action pairs. This replaces noisy reward aggregation with dense, stable supervision. DIBS achieves significant improvements in both training stability and zero-shot generalization against existing RL and meta-RL algorithms.

---


### 229. [Certificate-Guided Evaluation of Reinforcement Learning Generalization](https://arxiv.org/abs/2606.00840)

**<font color=#1a73e8>作者：</font>** Vignesh Subramanian, Đorđe Žikelić, Suguman Bansal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work presents a logic-driven framework to evaluate the performance of reinforcement learning (RL) algorithms in their ability to generalize to unseen tasks. Our framework defines a family of inductive reach-avoid tasks, characterized by structural similarities in task dynamics, enabling evaluation of generalization capabilities. We introduce a neural certificate function that validates trajectories generated by RL algorithms by enforcing key conditions, thereby serving as a litmus test for RL generalization. We empirically demonstrate our method's capability in certifying generalization for several state-of-the-art generalizable RL algorithms on challenging continuous environments.
Our results show that a lower percentage of certificate function violations correlates with a higher number of test tasks successfully solved, highlighting the effectiveness of our framework in evaluating and distinguishing generalization capabilities of RL algorithms. This work provides a principled approach for benchmarking RL generalization.

---


### 230. [RefDiffNet: Learning to Expose Subtle PCB Defects Before Detection](https://arxiv.org/abs/2606.00852)

**<font color=#1a73e8>作者：</font>** Vinay Edula, Nilesh Badwe, Priyanka Bagade  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Printed circuit board (PCB) defect detection is challenging because many defects are small and difficult to distinguish from complex background patterns. Most deep learning-based PCB inspection methods rely only on the inspected PCB image for defect detection, ignoring the defect-free reference image that encodes the expected layout of traces, pads, and other PCB structures. In this work, we propose RefDiffNet, a lightweight plug-and-play input enhancement block placed before the detector backbone to enhance the image before defect detection. RefDiffNet brings one proven idea from classical inspection into the deep learning era, using a defect-free reference image to reveal defects. RefDiffNet compares the defective image with the aligned reference, captures structural changes relative to the reference, and uses a lightweight encoder to output the original image with defective regions highlighted, thereby making the downstream detector's task easier. Results on HRIPCB and DeepPCB show that RefDiffNet consistently improves performance across detector families, including one-stage detectors from YOLOv8 to YOLOv26, the transformer-based RT-DETR, and the two-stage Faster R-CNN. It achieves up to 18% relative mAP50:95 gain with negligible overhead, introducing only 0.004 - 0.005M additional parameters and 0.7 - 0.8 GFLOPs, amounting to at most 0.25% of the parameter count of any evaluated detector. Results establish RefDiffNet as a lightweight, plug-and-play, detector-agnostic input enhancement module that substantially improves PCB defect detection with minimal computational cost.

---


### 231. [GCVE: A Decentralized Model for Vulnerability Identification, Publication, and Operational Enrichment](https://arxiv.org/abs/2606.00856)

**<font color=#1a73e8>作者：</font>** Alexandre Dulaunoy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Global CVE initiative (GCVE) proposes a decentralized, open, and extensible model for vulnerability identification, publication, and enrichment. It addresses a gap in today's vulnerability ecosystem: centralized systems provide rigorous control and widely recognized identifiers, while many producers publish advisories independently without a shared fabric for discovery, correlation, enrichment, and reuse.
This paper presents GCVE as a socio-technical standardization effort combining autonomous GCVE Numbering Authorities, lightweight allocation rules, distributed publication, open Best Current Practices, and practical reference implementations. The model preserves global uniqueness while allowing participants to publish according to their operational needs. It also broadens the concept of a vulnerability record to cover assignments, disclosures, sightings, rejected identifiers, observations, exploited vulnerability information, and enrichment records.
The paper describes how the GCVE BCP process supports technical interoperability and amendable operational practice, including practical guidance for vulnerability handling and disclosure. It also examines the extension mechanism, including AI-oriented extensions, as a way to evolve the standard without centralizing control.
A particular focus is placed on vulnerability-lookup as the reference implementation. It aggregates multiple sources, supports GCVE publication and consumption, implements distributed Known Exploited Vulnerability data, and enables automatically enriched vulnerability data streams. Building on lessons from the MISP ecosystem, GCVE frames vulnerability coordination not only as identifier allocation, but as open infrastructure for collective security knowledge production.

---


### 232. [Task diversity produces systematic transfer but inhibits continual reinforcement learning](https://arxiv.org/abs/2606.00880)

**<font color=#1a73e8>作者：</font>** Purab Seth, Neil Shah, Kunal Jha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual reinforcement learning aims to produce agents that learn not only to improve at their current tasks but also to adapt as task distributions change. Training an agent on many diverse tasks can induce zero-shot generalization, but previous work generally evaluates this generalization after training -- with frozen weights. Whether task diversity also improves an agent's ability to continue learning across distribution shifts remains unclear. We introduce Banyan, a GPU-accelerated continual RL domain in which task diversity factors into three independently controllable axes: the map layouts an agent must navigate, the objects it must interact with, and the hierarchical structures of sub-goal dependencies. Across individual distribution shifts, increasing diversity along each axis causes agents to begin training on the new tasks near the performance attained on the previous one, even when the shift changes the structure of the optimal policy. However, as the number of shifts increases, this local transfer does not by itself yield sustained continual learning: longer-horizon tasks plateau, and earlier task distributions are forgotten after later training. Banyan is a benchmark for studying when controlled task diversity produces transferable learning, when that transfer persists, and where it falls short of proper continual learning.

---


### 233. [Dive into Waves: Morlet Spectral Transformer for Cross-Subject Emotion Decoding from EEG](https://arxiv.org/abs/2606.00884)

**<font color=#1a73e8>作者：</font>** Jiaxin Qing, Lexin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study cross-subject emotion recognition from EEG, a practically important yet challenging problem in brain-computer interfaces. Unlike tasks with clear waveform signatures, emotion-related EEG signals are primarily encoded in spectral power and are weak, noisy, and highly variable across subjects. Existing approaches rely either on large pretrained EEG foundation models, which require massive data yet still struggle with cross-subject variability, or frequency-domain encoders, which better reflect spectral structure but suffer from mismatched representations, drift-dominated tokenization, and lack of band-specific spatial modeling. In this article, we propose the Morlet Spectral Transformer (MST), built around three key components and integrated with a spatiotemporal Transformer backbone. First, Morlet wavelet tokenization provides a time-frequency representation that matches the multi-scale structure of brain rhythms, and extends classical differential entropy features to a form suitable for Transformers. Second, long-context baseline removal acts as a simple temporal normalization that removes subject-specific drift and redundancy across nearby windows. Third, frequency-specific spatial projection learns a separate channel mixer for each frequency band, capturing interpretable band-specific patterns and reducing cross-channel mixing. We show that, even without pretraining, MST consistently outperforms both large pretrained EEG foundation models and frequency-based methods across all SEED-family datasets. These results suggest that careful representation design can yield an accurate, cost-effective, and interpretable alternative to large-scale pretraining.

---


### 234. [GABI: Geometry-Aware Boundary Integration for Spacecraft Segmentation](https://arxiv.org/abs/2606.00886)

**<font color=#1a73e8>作者：</font>** Iason Georgios Velentzas, Dhruv Ahuja, Panagiotis Tsiotras  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation is crucial for autonomous spacecraft, as it directly affects downstream tasks related to 3D situational awareness. The harsh illumination conditions of space, however, produce images with high variability in appearance, hindering the generalization of segmentation approaches across different spacecraft and environments. In this work, we propose GABI, a lightweight boundary-aware multi-task segmentation architecture that augments a convolutional backbone with an auxiliary distance-field prediction head. The distance field provides dense geometric supervision around object boundaries, encouraging the network to learn spatially consistent representations of spacecraft structures while maintaining low model complexity suitable for onboard perception systems. We evaluated GABI against both an established convolutional baseline and a heavier transformer-based architecture. On the SPARK benchmark, distance-field supervision improves the baseline by up to $5\%$ in Average Precision while achieving performance comparable to the transformer models. In generalization experiments, GABI improves Average Precision by more than $50\%$ over the baseline. In cross-domain evaluation, the lightweight GABI variant performs within $5\%$ in IoU and F1-score of the heavier transformer model while being approximately ten times smaller. At the same time, the heavier GABI variant surpasses the transformer architectures while remaining nearly three times lighter.

---


### 235. [A Lightweight Hybrid MLP-Based Framework for Real-Time Phishing URL Detection Using Structural URL Features](https://arxiv.org/abs/2606.00889)

**<font color=#1a73e8>作者：</font>** Uche Unoke Emmanuel, Gideon Francis Oghie  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing attacks remain a major cybersecurity threat, exploiting deceptive URLs to steal sensitive user information. Traditional blacklist and rule-based detection approaches are reactive and often fail to identify newly emerging phishing URLs. This paper proposes a lightweight hybrid framework for real-time phishing URL detection that combines blacklist-based screening with a Multi-Layer Perceptron (MLP) classifier operating solely on structural URL features. The framework extracts 16 URL-derived features capturing structural, domain-based, and security-related characteristics without requiring webpage content access, third-party APIs, or visual rendering, making it computationally efficient for real-time deployment. The system was trained and evaluated on the PhiUSIIL phishing dataset containing 235,795 labelled URLs. Experimental results show that the proposed MLP achieved 99.24% accuracy, 98.74% precision, 99.95% recall, 99.34% F1-score, and 99.65% ROC-AUC, outperforming Random Forest, Logistic Regression, XGBoost, LightGBM, and CatBoost under the same evaluation setting. The hybrid architecture achieved an average inference latency of 1.2 ms per URL and a peak throughput of 4,200 URLs per second under concurrent processing. A functional desktop application prototype, CyberGuard, further demonstrates deployment viability. The results indicate that the proposed framework provides an accurate and computationally efficient solution for real-time phishing URL detection in resource-constrained environments.

---


### 236. [Cohort-Scale Neural Atlases of Ultrasound Video](https://arxiv.org/abs/2606.00890)

**<font color=#1a73e8>作者：</font>** Zhuorui Zhang, Roger Pallarès-López, Xuan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound is the most widely used real-time imaging modality in clinical practice, yet per-frame video annotation remains a major bottleneck: expert labels are scarce and costly, and image appearance varies with speckle, shadowing, attenuation, and operator-dependent probe pose. This is especially limiting because clinically relevant information is often dynamic, from left-ventricular motion in echocardiography to muscle and bone kinematics in musculoskeletal imaging. Population atlases can amortize annotation cost by registering observations to a shared canonical coordinate system, but existing neural atlas methods mainly target single videos, small test-time image sets, or object-centric image collections. We introduce a cohort-scale neural atlas for ultrasound video: a single canonical chart with per-video Generative Latent Optimization embeddings, trained jointly over thousands of frames in DINOv3 feature space. Across five cardiac and musculoskeletal datasets with point landmarks and segmentation masks, our method learns coherent canonical templates and enables accurate atlas-space annotation transfer. On EchoNet-Dynamic and MSK-Bone, it supports single- and few-shot transfer with accuracy competitive with strong dense-correspondence baselines, while training in minutes on a single consumer GPU. The learned embeddings are interpretable: linear projections reveal structured cohort variation, image-decoder interpolation produces anatomically plausible intermediate frames, and test-time latent inversion reconstructs held-out frames through the atlas. These results suggest that cohort-scale neural atlases offer a practical, interpretable representation for reducing expert annotation burden in ultrasound video analysis.

---


### 237. [An Exploratory Study into using Machine-Learning for Fast Step-by-step Emulation of Numerical Mechanical Thrombectomy Simulations for Ischemic Stroke](https://arxiv.org/abs/2606.00892)

**<font color=#1a73e8>作者：</font>** Thijs Stessen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The treatment of ischemic stroke using mechanical thrombectomy involves difficult decisions under intense time constraints. Numerical physics simulations can in theory inform operators to make better decisions regarding treatment approaches and device selection, but are too slow to do so in practice. In this thesis, we investigate if current machine learning based surrogates can accurately emulate these simulations in a step-by-step manner while making them significantly faster. To do this we train three surrogate models on two simulations that involve a simplified aspiration procedure, with varying levels of geometric complexity. Our results show that two of our models accurately predict singular simulation steps and provide substantial speedups, especially when combined with specific data augmentations. However, the models showed a lack of stability when emulating simulations with complex geometries over longer time periods. Overall, this work provides a foundation for future studies to develop stable methods that scale to realistic numerical physics simulations of mechanical thrombectomy.

---


### 238. [Framework for Discovering GPS Spoofing Attacks in Drone Swarms](https://arxiv.org/abs/2606.00904)

**<font color=#1a73e8>作者：</font>** Yingao Elaine Yao, Pritam Dash, Karthik Pattabiraman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Swarm robotics, particularly drone swarms, are used in various safety-critical tasks. While a lot of attention has been given to improving swarm control algorithms for improved intelligence, the security implications of various design choices in swarm control algorithms have not been studied. We highlight how an attacker can exploit the vulnerabilities in swarm control algorithms to disrupt drone swarms. Specifically, we show that the attacker can target a swarm member (target drone) through GPS spoofing attacks, and indirectly cause other swarm members (victim drones) to veer from their course, resulting in collisions. We call these Swarm Propagation Vulnerabilities (SPVs).
In this paper, we introduce two fuzzing tools, SwarmFuzzGraph and SwarmFuzzBinary, to efficiently find SPVs in swarm control algorithms. SwarmFuzzGraph uses a combination of graph theory and gradient-guided optimization to find SPVs. Our evaluation on a popular swarm control algorithm shows that SwarmFuzzGraph achieves an average success rate of 48.8% in finding SPVs. However, SwarmFuzzGraph fails to find any SPVs in drone swarms with different topologies. We then propose SwarmFuzzBinary, which uses observation-based seed scheduling and binary search to find SPVs. The evaluation shows that SwarmFuzzBinary's success rate is comparable to SwarmFuzzGraph and work in all tested algorithms.

---


### 239. [hZACH-ViT: Curved Latent Geometry for Compact Vision Transformers in Low-Data Medical Imaging](https://arxiv.org/abs/2606.00906)

**<font color=#1a73e8>作者：</font>** Athanasios Angelakis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact Vision Transformers are attractive for medical imaging in low-data and resource-constrained settings, but most existing variants assume that Euclidean latent geometry is sufficient for organizing image representations. We introduce hZACH-ViT, a family of curved-geometry extensions of ZACH-ViT, a compact zero-token Vision Transformer that removes positional embeddings and the class token and relies on global average pooling over patch representations. To isolate the role of geometry, we preserve the verified ZACH-ViT backbone and modify only the final representation space and prototype-based classifier head, enabling a controlled comparison between Euclidean, hyperbolic, and spherical latent geometries.
We evaluate Poincaré, Klein, and spherical hZACH-ViT heads on seven MedMNIST datasets under an identical few-shot protocol with 50 samples per class and five random seeds. The completed benchmark contains 770 training runs spanning seven datasets, three non-Euclidean geometries, seven curvature magnitudes, and a Euclidean baseline. Across all seven datasets, the best non-Euclidean hZACH-ViT configuration improves over Euclidean ZACH-ViT, with an average gain of +0.021 in the dataset-specific primary metric and the largest improvement on OCTMNIST (+0.055 MacroF1). Fixed low-curvature configurations retain positive gains on the majority of datasets, and low curvature values (c = 0.1 or 0.2) account for six of the seven dataset-level winners.
Rather than identifying a universally optimal manifold, our results establish geometry and curvature as dataset-dependent model-selection variables, with fixed low-curvature analyses confirming that gains persist beyond exhaustive per-dataset tuning.

---


### 240. [One (Thread) Can Keep a (PRNG) Secret, but not Two](https://arxiv.org/abs/2606.00918)

**<font color=#1a73e8>作者：</font>** Ehood Porat, Amit Klein, Benny Pinkas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a novel, practical attack on the IPv6 Fragment ID generation algorithm of XNU, which is the kernel used by Apple products such as macOS and iOS. This attack exploits a race-condition vulnerability in the algorithm's pseudorandom number generator (PRNG) to cryptanalytically break, learn the internal state of the generator, and consequently predict fragment IDs, which, in turn, facilitates an IPv6 fragment spoofing attack. As far as we know, this is the first cryptanalytic attack that is based on exploiting race-conditions. With fragment spoofing, it is possible to partially manipulate UDP datagrams and TCP segments. We showcase a new type of attack on NFS (UDP) where an off-path attacker modifies a file as it is written, and an attack on HTTP (TCP) where an off-path attacker modifies an HTTP request. Apple assigned this vulnerability the CVE identifier CVE-2024-27823 and patched all its XNU-based products against the attack.

---


### 241. [Task Structure Reverses Layerwise State Encoding in Sequence Models](https://arxiv.org/abs/2606.00926)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic studies of sequence models often treat layerwise state encodings as architectural traits: recurrent models concentrate readable state, attention-based models distribute it. We find that the same architecture reverses this profile when the task changes. Across Transformers, Mamba, Mamba-2, LSTMs, and GRUs, Parity is concentrated late in Mamba and the recurrent baselines and built gradually by Transformer; on bounded-depth Dyck-k the pattern flips. The same flip appears in fine-tuned Mamba-130M and Pythia-160M, and the Pythia Dyck bottleneck persists at 410M. Two explanations are conflated in the literature: algebraic structure (commutativity) versus computational structure (prefix update vs. stack). To separate them we add a third task: non-commutative S_3 permutation composition. S_3 groups with Parity, not Dyck, on layerwise probing across all five architectures and on Mamba-specific Conv1D attribution, so the grouping tracks computational structure rather than commutativity.
Causal interventions show that, in the 4-layer formal models, linearly readable directions are often functionally necessary and can remain important at out-of-distribution lengths on Parity and Dyck. At pretrained scale the picture splits. Fine-tuned Pythia Dyck has a strong middle-layer bottleneck (L6-L7 ablation drops accuracy by roughly 81% at 160M; broader L4-L18 plateau at 410M), far weaker at the best-probe layer. Pretrained Mamba shows the complementary failure mode: its final layer is highly readable, no single probe direction breaks the task on Parity, Dyck, or S_3, yet mid-position activation patching there recovers about 97-98% of the clean-corrupted logit gap. Probing localizes where state is linearly available, not always where the computation is bottlenecked. Mechanistic signatures are properties of architecture and task together.

---


### 242. [Bridging Topology and Deep Representation Learning: A TDA-ViT Fusion Model for Four-Class Brain Tumor Classification](https://arxiv.org/abs/2606.00927)

**<font color=#1a73e8>作者：</font>** Faisal Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain tumor classification from magnetic resonance imaging (MRI) is a key requirement for early diagnosis and clinical decision-making. Vision Transformers (ViTs) have shown strong performance in medical image analysis by learning global contextual representations, but they often fail to capture intrinsic structural and topological patterns present in tumor regions. To address this limitation, we propose a fusion framework that combines Topological Data Analysis (TDA) features with pretrained Vision Transformer representations for four-class brain tumor classification.
In the proposed method, TDA is used to extract complementary topological descriptors that capture geometric structure, connectivity, and shape information from MRI images. In parallel, a pretrained ViT model learns high-level semantic representations from the same images. These two feature spaces are then fused to form a unified and more discriminative representation for classification.
The model is evaluated on the BRISC2025 dataset, which contains four brain tumor classes: glioma, meningioma, pituitary tumor, and non-tumor cases. Experimental results show that combining topological and transformer-based features significantly improves performance compared to using either approach alone. The proposed TDA-ViT fusion model achieves an accuracy of 99.10%, precision of 99.27%, recall of 99.15%, F1-score of 99.21%, and an AUC of 99.98%. It also outperforms several state-of-the-art models, including ResNet50, ResNet101, EfficientNetB2, and standalone Vision Transformers. These results demonstrate that topological features provide valuable complementary information that enhances deep representation learning, leading to a robust and highly accurate framework for automated brain tumor classification.

---


### 243. [Detection vs. Execution: Single-Bucket Probes Miss Half the Mamba-2 State Sink](https://arxiv.org/abs/2606.00930)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability often assumes that probes identifying a representational signature also identify the circuit executing the corresponding computation. We show that this assumption can fail systematically in Mamba-2. Studying the state sink (disproportionate Delta-gate activation on boundary tokens, analogous to the attention sink), we find that single-bucket probes recover only a small execution layer while missing a much larger detection layer with the same representational signature.
In Mamba-2, the state sink decomposes into two functional head sets. Single-bucket BOS-specialist heads (about 5% of heads at 2.7B) causally support both BOS-context and newline-target predictions across model scales and corpora. Dual heads (27-35% of heads, recovered by multi-class aggregation of the same probe) show stronger BOS-newline representational similarity but substantially weaker causal effects under ablation. Representational similarity does not imply functional equivalence.
This distinction matters for downstream behaviour: ablating BOS-specialist heads collapses RULER NIAH retrieval accuracy from 1.00 to 0.00 at 1024 context length in both Mamba-1 2.8B and Mamba-2 2.7B, while size-matched complements preserve baseline performance. A random channel-bucketing control rules out substrate granularity alone, implicating Mamba-2's head-shared Delta projection. Probe-derived specialty can identify execution circuits; at coarse granularity the same probe also recovers detection circuits, and separating them requires class-conditional ablation rather than class-conditional cosine.

---


### 244. [CV-Arena: An Open Benchmark for Instructional Computer Vision Problem Solving with Human-AI Collaborative Preferences](https://arxiv.org/abs/2606.00931)

**<font color=#1a73e8>作者：</font>** Fangzhou Lin, Peiran Li, Lingyu Xu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided image editing is becoming a general interface for visual work, yet existing benchmarks still focus largely on narrow appearance edits and do not fully capture the diversity of real-image tasks in professional workflows. Here, we define instructional computer vision problem solving as a broader formulation of image editing: given a real input image and a natural-language instruction, a system must produce an edited output that realizes the requested transformation while satisfying explicit preservation, geometric, physical, and usability constraints. We introduce CV-Arena, an open benchmark designed to evaluate this capability at professional scales. CV-Arena contains 12K high-resolution real-image instruction pairs spanning 16 instruction-based visual task types, constructed using CogRetriever, a dual-track retrieval-and-curation pipeline that combines targeted web search, agentic query refinement, verification, and traceability. To evaluate models at scale while preserving human fidelity, we propose Active Elo, a human-AI collaborative preference protocol that leverages CV-Judge, a logic-gated, multi-dimensional VLM evaluator, to reject clear failures and resolve high-confidence comparisons; and to route close, high-quality comparisons to expert raters. Mixed human and AI supervision is then aggregated through reliability-weighted Elo updates. Our comprehensive evaluation of 21 systems, including proprietary, open-source, and agentic models, on CV-Arena reveals persistent gaps in instruction adherence, physical reasoning, structural control, and fine-grained detail preservation. We further develop CV-Agent, a lightweight agentic model that combines planning, editing, and verification, and demonstrate that closed-loop reasoning is a promising direction for professional-grade instruction-following visual editing.

---


### 245. [One Channel to Rule Them All: Rethinking Input Representation for Visual Place Recognition](https://arxiv.org/abs/2606.00936)

**<font color=#1a73e8>作者：</font>** Timur Ismagilov, Shakaiba Majeed, Michael Milford 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Place Recognition (VPR) is fundamental to long-term robot localization and SLAM, yet current systems overwhelmingly rely on RGB input, implicitly assuming color is necessary for global place recognition. We challenge this assumption, investigating the role of chromatic information across training regimes, model architectures and standard benchmarks under real-world appearance variation. We find that grayscale matches RGB performance generally and outperforms it under severe appearance shifts where color invariance is insufficiently learned, while color provides meaningful gains only where persistent and discriminative chromatic cues are present. Across selected benchmarks, a fully gray-trained MixVPR model achieves an average 82.4% Recall@1 compared to 81.2% for its RGB counterpart. In some cases, lightweight grayscale variants with 60% fewer parameters can outperform heavier RGB models. Grayscale further offers practical advantages in storage, bandwidth and alignment with resource-constrained systems. We conclude that for global VPR where scenes vary across illumination, weather, season and setting, color contributes minimally, and grayscale alone is sufficient for reliable place recognition.

---


### 246. [Cellular Sheaf Neural Operators for Structure-Preserving Surrogate Modeling of Constrained PDEs](https://arxiv.org/abs/2606.00937)

**<font color=#1a73e8>作者：</font>** Lennon J. Shikhman, Shane Gilbertie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide fast surrogate models for PDE simulations, but standard architectures often treat geometry and discretization as secondary to field data. Physical states are usually represented as grid-channel stacks, even when different quantities naturally belong on vertices, edges, faces, cells, boundaries, or interfaces and must satisfy compatibility constraints. We propose Cellular Sheaf Neural Operators, a discretization-aware framework for structure-preserving neural PDE surrogates. The method represents PDE states on oriented cell complexes, couples local feature spaces through learned restriction maps, and uses incidence/Hodge-informed message passing to follow computational geometry. Learned update heads pass through coboundary or flux maps, allowing selected constraints to arise from cell-complex structure rather than only from loss penalties. For magnetohydrodynamics, this yields face-based magnetic-flux updates driven by edge electromotive fields and finite-volume-style fluid updates driven by learned face fluxes and cell sources. On turbulent MHD and fusion-equilibrium surrogate tasks, the method improves structure-sensitive diagnostics, including rollout behavior, divergence control, spectral error, and equilibrium-regression accuracy. These results indicate that cellular-sheaf structure is a useful inductive bias for neural PDE surrogates in constrained multiphysics systems.

---


### 247. [PRISM: Gauge-Invariant Tangent-Space Differentially Private LoRA](https://arxiv.org/abs/2606.00944)

**<font color=#1a73e8>作者：</font>** Shihao Wang, Xueru Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying differential privacy (DP) via DP-SGD to Low-Rank Adaptation (LoRA) is a natural approach for privacy-preserving fine-tuning. However, LoRA's low-rank parameterization poses a fundamental challenge. In LoRA, each trainable update is represented as a low-rank matrix $Z = AB^\top$, but this factorization is inherently non-identifiable: many factor pairs $(A,B)$ represent the same update $Z$. As a result, applying DP-SGD directly to the factors induces gauge-dependent perturbations on $Z$, and we show that this naive DP-LoRA can lead to unbounded noise amplification. We propose PRISM, an intrinsic DP mechanism for LoRA that is gauge invariant by construction, avoids bilinear noise amplification, and admits an efficient low-dimensional noise sampler. Moreover, PRISM yields a closed-form characterization of the effective intrinsic noise induced on $Z$, enabling stable privacy-utility trade-offs through bounded, gauge-invariant perturbations. We establish standard $(\epsilon,\delta)$-DP guarantees for PRISM and introduce a DP-aware, gauge-invariant adaptive update rule that prevents adaptive optimization from amplifying injected privacy noise, improving numerical stability in practice.

---


### 248. [COLLIE: Guiding Skill Discovery in Semantically Coherent Latent Space](https://arxiv.org/abs/2606.00950)

**<font color=#1a73e8>作者：</font>** Yao Luan, Ni Mu, Hanfei Ge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised skill discovery (USD) aims to learn diverse behaviors without reward functions, but often results in task-irrelevant or hazardous behaviors due to uniform exploration. Guided skill discovery (GSD) addresses this issue by incorporating human intent to focus exploration on meaningful regions. However, existing GSD methods typically require training additional guidance models, and rely on pre-defined rules or expert demonstration, which can be ineffective under sparse, online-collected human feedback. To overcome this, we propose COLLIE, a GSD framework that leverages dense unsupervised data to construct a semantically coherent skill latent space. This latent space is well-structured, enabling reliable guidance with sparse online feedback. Moreover, its semantic coherence property enables training-free construction of guidance signals, eliminating the need for additional model training beyond skill learning. Theoretical analysis justifies the effectiveness of our training-free guidance signal, while experiments across diverse state-based and pixel-based tasks show that COLLIE learns diverse, human-aligned skills, avoids hazardous behaviors, and achieves superior downstream performance with minimal human feedback.

---


### 249. [COLLAR: Cascaded Object-Level Latent Refinement for High-Fidelity Conditional Generation](https://arxiv.org/abs/2606.00954)

**<font color=#1a73e8>作者：</font>** Xinlong Zhang, Jia Wei, Xiaoyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving high-fidelity object-level control in Diffusion Transformers remains a significant challenge despite the introduction of structural priors like depth and Canny maps. Current object-level conditional generation methods frequently suffer from visual artifacts and struggle to maintain precise control over objects within small localized regions. To address these limitations, we propose Cascaded Object-Level Latent Refinement (COLLAR), a training-free framework that progressively optimizes object-level features via the Field-of-View (FoV) expansion. First, we propose the Cross-Scale Semantic Alignment (CSSA) module to address spatial-semantic gaps by injecting object-level features into extended-FoV branches via attention mechanisms. To further optimize these features, the Cyclic Feature Injection (CFI) module introduces a reciprocal background feedback mechanism. It leverages a frequency-based adaptive strategy to selectively update the global backbone with context-aligned local information. Finally, the extended-FoV branch serves as a hub for feature optimization, ensuring that object-level features are integrated into the global generation process without compromising final image quality. Extensive experiments on the COCO-MIG and COCO-POS benchmarks demonstrate that our approach consistently outperforms state-of-the-art methods across semantic alignment, image quality, and spatial fidelity.

---


### 250. [CryoProt: A Protein Pretraining Framework with Cross-Box Interactions on Cryo-EM Density Maps](https://arxiv.org/abs/2606.00955)

**<font color=#1a73e8>作者：</font>** Dan Luo, Xuan Lin, Peng Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the growing availability of cryo-electron microscopy (cryo-EM) density maps, effectively leveraging them for protein representation remains challenging. First, current methods lack a general-purpose protein pretraining framework tailored for cryo-EM density maps, designed for protein-related property prediction. Second, existing approaches typically partition density maps into local box regions and model them independently, overlooking interactions across boxes which are essential for capturing global structural context in cryo-EM density map. To address these challenges, we propose CryoProt, a protein pretraining framework designed for cryo-EM density maps. CryoProt introduces a Map Encoder based on multi-head latent attention (MLA), where box-level representations interact through a shared latent space, enabling explicit modeling of cross-box dependencies within the density map. Furthermore, we adopt a multi-task pretraining strategy to learn generalizable representations that can be effectively transferred to diverse downstream tasks, such as protein flexibility prediction, where cryo-EM density maps are not required and can be inferred implicitly by the pretrained model. Experimental results demonstrate that CryoProt consistently outperforms existing state-of-the-art methods across multiple benchmarks, achieving up to 12% improvement over the best-performing baselines, highlighting the importance of modeling cross-box interactions in cryo-EM data. The source code is publicly available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
