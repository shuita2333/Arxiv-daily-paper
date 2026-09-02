# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 251. [Uncertainty-Driven Replay Memory for Reinforcement Learning](https://arxiv.org/abs/2608.29860)

**<font color=#1a73e8>作者：</font>** Sheeraja Rajakrishnan, Alexander G. Ororbia, Travis Desell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation provides promising capabilities for reinforcement learning (RL) agents. Notably, estimating uncertainty can reduce the training time and enable agents to obtain greater rewards over time by exploiting information related to whether an action would facilitate exploration of portions of an environment that are well-known versus those that are relatively unknown. In this work, we propose a novel formulation of the experience replay buffer commonly used in RL that we call uncertainty-driven replay memory (UDRM), which entails an update scheme for internally stored memories based on uncertainty estimates obtained by an RL model during training. In contrast to existing forms of RL, which typically use temporal difference error or the distribution of transitions to update the replay memory buffer and train RL controllers, our scheme biases the memory buffer to store more uncertain transitions that will improve an RL agent's generalization throughout training. Experimental results demonstrate that our proposed uncertainty-aware replay buffer enables an RL agent to obtain higher rewards during training compared to other existing uncertainty-aware RL frameworks.

---


### 252. [ManGo: Manga Active Narrative Grounding Optimization](https://arxiv.org/abs/2608.29865)

**<font color=#1a73e8>作者：</font>** Hao Qiu, Junyan Wang, Zheyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Manga visual question answering requires models to answer questions over panel-based visual narratives, where relevant evidence is distributed across ordered panels, embedded text, recurring characters, and implicit event transitions. This structure makes passive page encoding insufficient, as the model must identify which panels to inspect, what clues to retain, and when the accumulated evidence is sufficient for answering. We propose ManGo (Manga Active Narrative Grounding Optimization), an unsupervised framework for active manga visual question answering. ManGo introduces Active Narrative Sketching (ANS), which iteratively selects panels, extracts concise grounded clues, and decides when to stop, forming a compact question-directed evidence sketch before answer generation. To optimize this behavior without human-annotated answers or rationale paths, ManGo samples multiple ANS rollouts and applies group-relative training with two rewards: answer preference from listwise self-ranking and path consistency from stable ordered panel trajectories. The combined reward is optimized with group-relative policy training, encouraging the model to improve both final answers and the panel-level evidence paths that support them. Experiments on standard manga understanding benchmarks show that ManGo achieves state-of-the-art performance across different settings.

---


### 253. [Partially Linear Autoencoders for Manifold Learning and Dimensionality Reduction](https://arxiv.org/abs/2608.29867)

**<font color=#1a73e8>作者：</font>** Louen Pottier, Louis Lesueur, Anders Thorin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoencoders are widely used for nonlinear dimensionality reduction and manifold learning. While most common implementations rely on both nonlinear encoders and decoders, we investigate the specific role of the encoder and the extent to which it can be constrained to be linear without reducing accuracy. We conduct a comparative study on four autoencoder architectures: standard fully nonlinear autoencoders (AE), linear-encoder autoencoders (Lenc-AE), linear-decoder autoencoders (Ldec-AE), and fully linear autoencoders (LAE), evaluated on synthetic manifolds, computational mechanics data sets, and real-world image data sets including MNIST. We demonstrate that imposing a linear encoder preserves most of the representational capacity of the autoencoder, provided the decoder remains nonlinear. In particular, Lenc-AE consistently outperforms both Ldec-AE and LAE, and achieves reconstruction quality comparable to fully nonlinear AE, while offering advantages in terms of parsimony and interpretability of the latent representation. These results suggest that the nonlinear decoder is the critical component for manifold learning, rather than the encoder. A geometric interpretation of this finding is developed, which identifies the precise conditions under which a linear encoder is sufficient, and the specific manifold configurations that expose its limitations.

---


### 254. [Towards an Expressivity-Normalized Energy-Demand Comparison of ANNs and SNNs](https://arxiv.org/abs/2608.29869)

**<font color=#1a73e8>作者：</font>** Miriam Kranzlmüller, Pascal Esser, Gitta Kutyniok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) are often regarded as energy-efficient alternatives to artificial neural networks (ANNs), yet their advantage depends critically on both network architecture and data properties. We develop an analytical framework to compare fully-connected ReLU ANNs and integrate-and-fire SNNs for time-series data with respect to their theoretical energy efficiency at matched expressive capacity. By relating an inference-energy model to theoretical bounds on representational expressivity, we derive an expressivity-normalized efficiency ratio and explicit thresholds in network width, spike sparsity, and ANN depth scaling. Our analysis characterizes the regimes in which event-driven computation offsets the temporal overhead of SNNs, providing capacity-aware principles for designing energy-efficient temporal networks. It shows that ANNs exceed SNNs in expressivity-normalized efficiency only in specific regimes.

---


### 255. [OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes](https://arxiv.org/abs/2608.29881)

**<font color=#1a73e8>作者：</font>** Muxin Liu, Tianbo Liu, Jing Xia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation has achieved strong open-domain generalization, yet reliable robotic deployment remains difficult in transparent, reflective, and specular environments, where depth sensors often produce missing or biased depth. Existing methods often handle such optical failures with scene-specific preprocessing, auxiliary modules, or post-hoc fine-tuning. While effective in constrained settings, these designs increase architectural redundancy and can over-specialize general geometry models to narrow optical scenarios. We revisit this problem as a localized failure mode within base-model training and identify sensor-induced supervision bias as a key bottleneck: models inherit sensor failure patterns from biased real-depth supervision in optically challenging regions. We then introduce OptiGeo, a bias-aware training framework that rehabilitates biased real supervision using a clean-geometry teacher and residual-trimmed alignment. We redefine transparency-targeted rendering as a compact source of clean optical geometry, rather than a large domain-specific fine-tuning set. With only a small targeted rendering set, OptiGeo learns the geometric structure of transparent objects and regions, correcting local geometry distortions that real sensors cannot reliably supervise. Despite only 30M parameters, OptiGeo outperforms substantially larger 300M-scale monocular models and billion-scale multi-view baselines on transparent-scene benchmarks, while remaining competitive on general zero-shot depth and boundary sharpness. Real-world navigation cases further validate its practicality as an efficient perception module in optically challenging scenes.

---


### 256. [Structural Hierarchy and Geometry in Molecular Representation Learning](https://arxiv.org/abs/2608.29886)

**<font color=#1a73e8>作者：</font>** David Sulu, Lorenzo Di Fruscia, Jana M. Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular self-supervised learning uses chemical structures to guide which molecular embeddings should be similar. We study whether explicitly encoding a molecule's Bemis-Murcko scaffold and using it to supervise the molecular embedding changes what the model learns. We further test whether this effect depends on the embedding geometry by comparing Euclidean and Lorentz contrastive objectives. Across two augmentation strengths, scaffold-supervised models consistently organize molecules according to both identical and structurally related scaffolds. The resulting embeddings also improve molecular property prediction on several tasks, while the exact gains depend on the predicted property. The effect of scaffold supervision on molecular organization is stronger under Lorentz objectives, but neither geometry provides a consistent overall advantage. These results show that explicitly teaching the relation between a molecule and its structural core can reliably shape the organization of molecular embedding space, while the extent of usefulness of this organization remains task dependent.

---


### 257. [Sensitivity-Constrained Neural Operators for Data-Efficient Forward and Inverse Modeling of Partial Differential Equation Systems](https://arxiv.org/abs/2608.29888)

**<font color=#1a73e8>作者：</font>** Abdolmehdi Behroozi, Chaopeng Shen, Daniel Kifer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide fast surrogates for partial differential equation (PDE) solvers, but their reliability can degrade for high-dimensional spatial inputs and inverse or repeated inference. State-only training constrains solution values but not the learned input--output response. We study sensitivity-constrained neural operators (SC-NOs), which augment standard training with sampled solver-derived Jacobian supervision. Selected sensitivities from differentiable solvers or discrete adjoints are matched during training, allowing response information to be amortized across minibatches without imposing the full Jacobian at every update. We evaluate SC-NO on advection--diffusion and RANS--Spalart--Allmaras benchmarks, input-dimensionality scaling tests, long-horizon autoregressive rollout, and a shallow-water Tohoku tsunami source-inversion case. Sensitivity supervision improves forward prediction and yields larger gains in gradient-based inverse reconstruction of distributed fields. Scaling experiments show an improved accuracy--cost tradeoff for high-dimensional gridded inputs, while ablations indicate that state values and Jacobian information provide complementary supervision. In the tsunami case, SC-FNO reconstructs gridded seafloor deformation from sparse early gauge observations and forecasts subsequent wave propagation in a near-real-time proof-of-concept workflow. These results support sampled sensitivity supervision as a practical way to improve neural PDE surrogates when forward accuracy, inverse stability, robustness, and computational cost must be considered together.

---


### 258. [MASQ: Mask-Aware Spatiotemporal Quantization for Unsupervised Skeleton Action Segmentation](https://arxiv.org/abs/2608.29891)

**<font color=#1a73e8>作者：</font>** Xinyao Qin, Linxiang Peng, Youbao Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised skeleton-based temporal action segmentation is a crucial task for understanding human behavior in long untrimmed sequences. Recent approaches often rely on discrete quantization to discover action boundaries from motion representations. However, when spatial masking is introduced for representation learning, it can introduce representation ambiguity, while discrete quantization further amplifies small fluctuations in the latent space. The interaction between these two factors often leads to unstable code switching and severe temporal jitter near action this http URL address these limitations, we propose a novel Mask-aware Action Spatiotemporal Quantization (MASQ) framework. Our framework decouples the conflicting tasks of spatial feature inference and temporal this http URL the spatial dimension, we introduce a Joint-Level Structured Dropout (JLSD) mechanism that masks the entire temporal trajectory of selected joints, to encourage the model to learn discriminative inter-joint coordination patterns. In the temporal dimension, we design a mask-aware velocity loss that enforces motion consistency only on visible joints, that prevents gradient conflicts caused by masked signals and stabilizing temporal predictions. Extensive experiments on three widely used skeleton datasets, including HuGaDB, LARa, and BABEL, demonstrate that the proposed MASQ framework significantly outperforms existing state-of-the-art unsupervised methods. In particular, our model establishes a comprehensive and substantial leading advantage in the Mean over Frames accuracy.

---


### 259. [Joint Spatiotemporal Spectral Neural Operators for Learning PDEs on Irregular Domains](https://arxiv.org/abs/2608.29892)

**<font color=#1a73e8>作者：</font>** Abdolmehdi Behroozi, Chaopeng Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning solution operators for partial differential equations (PDEs) on irregular and geometry-dependent domains remains a central challenge in scientific machine learning. While spectral methods provide strong inductive biases for modeling global interactions, they are typically limited to regular domains, and existing neural approaches often require domain warping, interpolation, or costly geometric embeddings. We introduce the \textbf{Graph Spectral Neural Operator (GSNO)}, a neural operator that combines spatial graph spectral decompositions with temporal Fourier transforms through a unified space--time spectral kernel. This formulation enables globally coherent operator learning on non-Cartesian discretizations without domain warping or autoregressive rollouts. By replacing learned geometric embeddings with a graph Laplacian spectral basis, GSNO provides geometry-aware spectral learning with low parameter complexity. Across steady and unsteady PDE benchmarks on irregular and geometry-dependent domains, GSNO achieves strong accuracy with reduced runtime and parameter counts, while demonstrating robust zero-shot generalization across mesh resolutions and geometry families.

---


### 260. [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.29897)

**<font color=#1a73e8>作者：</font>** Jiaqi Su, Cong Pang, Jiawei Hong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents need a context manager to compress growing interaction histories into a bounded working context, via passive strategies or active strategies that decide how memory is accessed and reorganized. Meanwhile, prior optical-memory work mainly treats pixels as a dense codec for textualized histories, often presupposing that rendering context into optical memory incurs a significant performance drop relative to text, thus coupling this representation with SFT, self-distillation, or reinforcement learning to close this gap, leaving unresolved (i) how visual rendering performs as a context manager under a fair, controlled comparison, and (ii) whether this carrier offers a native advantage when history is inherently multimodal. In this paper, we formulate context management as a budget-constrained history transformation and introduce Visual Rendering (VR) as a representational context manager. Under a shared harness, policy model, trigger, and task domain, we evaluate VR on four text-centric and three multimodal benchmarks against four baselines (No Compression, Discard-All, Sliding Window, Summarization), finding visual memory is a natural carrier of native visual evidence. Building on this finding, we propose VERA (Visual Evidence-Retaining strategy for long-horizon Agents), a training-free context manager built on deterministic rendering with no exposed memory operations: on text-centric benchmarks it renders textual history as VR does, while on multimodal benchmarks it retains native visual observations instead of translating them into text. Across nearly all benchmarks, VERA cuts cumulative non-cache tokens by 31.5%-63.1% versus No Compression, matches existing managers on text-centric tasks, and achieves the highest accuracy among all baselines on multimodal tasks, supporting a modality-preserving view of long-horizon context management.

---


### 261. [INTERVenE: Temporal-Abstraction-Interval Based Transformers for Short-Horizon Medical Event Prediction](https://arxiv.org/abs/2608.29901)

**<font color=#1a73e8>作者：</font>** Shahar Oded, Yuval Shahar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electronic Health Record (EHR) prediction models in the intensive care unit must learn from sparse and irregular measurements while preserving the clinical meaning of time and supporting transparent decision-making. We present INTERVenE, a family of Transformer architectures whose input is an interval-based, knowledge-based temporal abstraction (KBTA), a token stream of named clinical concepts (states, trends, events, contexts) drawn from a curated medical ontology, rather than an unnamed bin index or a raw measurement triplet. This naming layer is what we ask KBTA to do: it makes the model's per-token attributions resolve to clinical concepts by construction. INTERVenE offers two complementary variants: an auto-regressive decoder that generates future abstraction trajectories with a per-step risk readout (localizing \emph{when} and \emph{after which events} risk rises), and a bidirectional encoder for single-pass joint risk and time-to-event prediction. Evaluated on 57,078 MIMIC-IV admissions against GRU-D, STraTS, and KarmaLego, INTERVenE-Enc reaches a support-weighted AUPRC$_w$ of 0.672, improving by 0.041 over the strongest neural baseline with non-overlapping 95\% bootstrap CIs, while also taking the best AUROC$_w$ (0.901) and length-of-stay MAE (44.4\,h). INTERVenE-Ar (AUROC$_w$ $0.854$, AUPRC$_w$ $0.587$ under the same evaluation contract - a strictly harder generative readout) provides a complementary token-level risk trajectory. An input-representation ablation confirms the lift transfers across structured discretizations, positioning KBTA-based intervals as the interpretable substrate that makes per-token attributions resolve to meaningful clinical concepts within the deployed model.

---


### 262. [Off-Manifold Refinement: Guiding Video Generators with a Frozen World Model](https://arxiv.org/abs/2608.29904)

**<font color=#1a73e8>作者：</font>** Hai Nguyen-Truong, Tuan-Anh Vu, Dang Huynh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video generators routinely fail at physical dynamics: objects float, trajectories violate gravity, contacts vanish. Standard denoising and flow-matching objectives fit visual data distributions but do not explicitly penalize such physical violations. Existing remedies can improve physical consistency, but typically add substantial inference or training cost. Candidate-selection methods generate and score multiple videos, while gradient-based world-model guidance repeatedly decodes and re-encodes intermediate estimates. Generator-internal refinement adds perturbation and re-denoising loops, whereas post-training requires curated data and additional optimization. We propose Off-Manifold Refinement (OMR), an inference-time method that instead injects world-model feedback directly into a single sampling trajectory. During scheduled middle ODE steps, we augment the generator velocity with the gradient of an adapter-space V-JEPA 2.1 surprise energy. This external correction can move the latent away from the uncorrected sampling trajectory and toward regions ranked as more physically plausible by the frozen predictor, after which the generator continues rendering from the corrected state. A small trained latent-to-embedding adapter keeps the gradient tractable at inference, and both the video generator and the world model remain frozen. On our fixed 400-prompt VideoPhy-2 detailed subset, OMR lifts the joint Semantic-Adherence-and-Physical-Commonsense metric from 47.0% to 52.0% (+5.0pp absolute, +10.6% relative) over the base Wan2.2-T2V-A14B sampler. On a separate fixed 50-prompt efficiency subset, it requires $1.71 \times$ the base runtime rather than the multiplicative cost of reward/search alternatives. Project page: this https URL.

---


### 263. [OrnaStyler: Ornament-Aware Latent Editing for Content-Preserving 3D Stylization](https://arxiv.org/abs/2608.29905)

**<font color=#1a73e8>作者：</font>** Tomohiro Aizawa, Shigeru Kuriyama, Chunzhi Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided style editing of 3D assets is essential for adapting existing objects to diverse visual aesthetics in digital content creation. Despite rapid progress in 3D shape modeling, faithfully stylizing an existing asset remains challenging when the desired stylization involves fine-grained structural ornamentation, which requires the model to preserve the source geometry and object identity, while coherently integrating new style-specific details. We propose \textbf{OrnaStyler}, a zero-shot framework for text-guided ornament-aware 3D stylization. Built upon rectified flow-based generative modeling, OrnaStyler introduces an inversion-guided editing strategy that recovers content-aware latent representations at both geometry and appearance levels in a staged manner to facilitate faithful editing. Our core idea is to explicitly model the spatial configuration of stylistic elements, thereby mitigating the fundamental tension between content preservation and style expression in the voxel space. Specifically, at the geometry level, we manipulate voxel representations through flow inversion to synthesize ornament-enhanced structures while preserving the spatial identity of the source asset. Then, at the appearance level, we introduce an adjacency-aware feature inpainting mechanism to harmonize newly generated ornaments with the original content, yielding coherent geometry-appearance integration. Our approach operates solely in the inference phase and enables selective editing over geometric augmentation or appearance stylization. Extensive experiments on both generated and real-world 3D assets against prior methods demonstrate that OrnaStyler achieves state-of-the-art editing performance in terms of content preservation, style fidelity, and overall visual realism. Code is available at: this https URL

---


### 264. [Diffusion-Based Inverse Design of Dielectric Resonator Metasurfaces for Shaping Smart Electromagnetic Environments](https://arxiv.org/abs/2608.29907)

**<font color=#1a73e8>作者：</font>** M. Tsukerman, K. Grotov, D. Vovchuk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future wireless systems are expected to transform the surrounding space from a passive propagation medium into a smart electromagnetic environment, where engineered surfaces control wave propagation, support wireless sensing, and create programmable electromagnetic fingerprints. A key challenge in realizing this vision is the inverse design of metasurfaces for tailored electromagnetic propagation. While forward analysis evaluates the response of a known geometry, the inverse task starts from a prescribed scattering signature and seeks a physically realizable structure that produces it. This inverse task is inherently nonlinear and often high-dimensional, while candidate solutions may be non-unique and provide no direct indication of practical realizability. Here, we introduce a conditional diffusion framework for inverse design of dielectric resonator metasurfaces from target angular scattering patterns. Trained on T-matrix simulated geometry-response pairs, the model learns a conditional distribution of geometries instead of a deterministic mapping, enabling multiple candidate designs for the ill-posed inverse problem. The best generated metasurface achieves a mean percentage error of 1.39%, outperforming CMA-ES optimization (4.1% after 10 h) while requiring only about one minute for after-training inference. The model also produces lower error distributions than deterministic neural baselines for out-of-distribution spectra, highlighting the potential of diffusion models for efficient metasurface design.

---


### 265. [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](https://arxiv.org/abs/2608.29910)

**<font color=#1a73e8>作者：</font>** Runjia Qian, Zile Wang, Jihai Zhang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR. Achieving stable long-horizon interactive generation, however, remains challenging, as the model must simultaneously preserve scene geometry, dynamic consistency, and camera control while supporting real-time autoregressive generation. Building upon Matrix-Game 3.0, we present Matrix-Game 3.5, as shown in Figure 1, which advances real-time interactive world generation toward geometry-aware and long-horizon consistent simulation through three key improvements. First, we propose a unified geometry-aware memory framework, whose patch-memory and tiled-PRoPE components introduce no additional learnable parameters, combining explicit 3D patch retrieval with projective camera conditioning to enable geometry-consistent camera control and faithful long-horizon scene recall. Second, we introduce a static-dynamic disentangled world representation that separately models static scene geometry and dynamic subjects, preserving both geometric consistency and subject identity throughout long-horizon generation. Third, we develop a two-stage progressive real-time distillation framework that converts a bidirectional diffusion model into a few-step causal generator through Perceptual Flow Matching and curriculum based Self-Rollout DMD, enabling minute-long real-time interactive generation. Extensive experiments demonstrate that, with a unified training corpus spanning Unreal simulation environments, open-world games, and internet videos, MatrixGame 3.5 achieves strong performance in long-horizon scene recall, precise camera control, subject consistency, prompt-driven world generation, and stable real-time open-world interaction.

---


### 266. [On the Instance Hardness as a Decision Criterion in TinyML Systems](https://arxiv.org/abs/2608.29913)

**<font color=#1a73e8>作者：</font>** Tobiasz Puslecki, Krzysztof Walkowiak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TinyML includes the implementation of machine learning on devices with limited memory and computing resources. With the development of technology, AI systems continue to scale in terms of size and computational requirements. This forces researchers to adapt methods to be environmentally sustainable by designing techniques for reducing computational costs and energy consumption in inferring AI models, even in small devices. In this work, we present preliminary findings on a novel application of the tree depth prune instance hardness method to the TinyML system. The results indicate that threshold control can change energy consumption with limited classification quality changes. This method allows us to adjust classification accuracy, thereby influencing computational complexity and energy consumption for inference. We present a work in progress with initial results as a proof of concept.

---


### 267. [FoundYou: A Unified Model for Personalized Segmentation and Retrieval](https://arxiv.org/abs/2608.29917)

**<font color=#1a73e8>作者：</font>** Gabriele Trivigno, Marcos Alfaro, Claudia Cuttano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized segmentation and personalized retrieval both aim to identify the same physical object across different images. While the former localizes the object within a target image, the latter retrieves images where it appears. Despite this shared instance-level objective, the two tasks have largely evolved separately and are addressed with distinct solutions. In this work, we introduce FoundYou, a unified framework built on the observation that Segment Anything 2 (SAM 2), trained to preserve object identity across video frames, inherently captures instance-level cues. We leverage this property to match objects across independent images, enabling segmentation and retrieval to emerge as two outcomes of the same instance alignment process. This unified view unlocks new capabilities beyond traditional benchmarks, including few-shot personalized retrieval and promptable personalized segmentation with flexible prompts. Extensive experiments show consistent gains over unified and task-specific methods, including +18.4 mIoU on PerMIS and +17.8 mAP on ILIAS. Performance scales with additional references and remains robust to weaker prompts. Beyond personalization, FoundYou achieves state-of-the-art results on category-level retrieval benchmarks. Notably, our approach keeps the SAM 2-small model entirely frozen and adds only 5.9 M trainable parameters, yielding a 52 M-parameter model that is over 75x faster and 20x smaller than the only prior unified solution. Code is available at this https URL .

---


### 268. [Continual Test-Time Adaptation via Entropy Sensitivity-Guidance in Strict Online Setting](https://arxiv.org/abs/2608.29920)

**<font color=#1a73e8>作者：</font>** Chandler Timm C. Doloriel, Yunbei Zhang, Muhammad Salman Siddiqui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) promises robustness under distribution shift by updating a pretrained model on unlabeled test data, but strict online TTA with batch size one and no access to source data is especially prone to drift or collapse. We introduce Sensitivity-Guided Erasing Adaptation (SEGA), a method for strict online continual TTA (CTTA) on corruption-style streams. SEGA uses a small number of structured erasures to probe how predictive entropy changes as information is removed, and uses the resulting per-sample sensitivity trajectories to coordinate recovery and sample selection rather than relying on raw entropy or batch statistics. This yields a practical feedback signal for long-horizon batch-size-one adaptation without periodic resets or model reservoirs. In experiments on ImageNet-C, CIFAR10/100-C, and corruption-generated aquaculture streams treated as controlled corruption-style proxies, SEGA yields consistent robustness and stability gains over strong CTTA baselines while reducing backward passes through sensitivity-based gating.

---


### 269. [Dior: Drawing the Light of Image via Material-Decoupled Illumination Representation](https://arxiv.org/abs/2608.29925)

**<font color=#1a73e8>作者：</font>** Xuanpu Zhang, Xuesong Niu, Haoxiang Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable image relighting is an important problem in image editing, and hand-drawn scribbles provide an intuitive interface for specifying the desired illumination. However, existing methods do not establish a consistent and effective mapping between scribble inputs and relighting results, limiting their ability to control illumination intensity, chromaticity, and complex spatial distributions. We address this limitation by introducing a material-decoupled illumination representation, termed the Lumi Map, which establishes an explicit mapping between user scribbles and the resulting illumination, thereby improving both relighting accuracy and controllability. Specifically, we use a renderer to synthesize source image-Lumi Map-relit image triplets and train the model to predict the target relighting result conditioned on the Lumi Map. To mitigate the domain gap introduced by synthetic data, we further perform reconstruction training on real relighting pairs, improving the model's generalization to real-world images. Finally, we present Dior-Light, an image relighting method controlled by hand-drawn strokes. Extensive experiments demonstrate that our method outperforms existing approaches in relighting accuracy and enables effective control over illumination intensity and chromaticity on in-the-wild images.

---


### 270. [Everybody Tracking Every Body](https://arxiv.org/abs/2608.29927)

**<font color=#1a73e8>作者：</font>** Daeyun Shin, Yunhan Zhao, Shu Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of 3D body pose estimation of multiple interacting people from their egocentric views with centralized coordination. Each individual wears a camera recording egocentric video and IMU data. Processing this video with VIO SLAM provides high-quality tracking of each egocentric camera through space. The first-person view from one individual provides third-person observations of other people, although these exocentric observations are sparse, intermittent, and of highly variable reliability as both cameras and subjects move. To integrate these synchronized data streams, we propose a diffusion-based approach that fuses estimates of pose based on head motion derived from egocentric camera motion with exocentric pose observations, conditioning on both observation content and reliability. Our model is trained on a mixture of single-person motion-capture data and multi-person video in order to learn rich priors for body motion trajectories and video observation reliability. Evaluation on challenging multi-person datasets suggests our fusion approach improves over motion-only and vision-only baselines in terms of both absolute and relative pose accuracy.

---


### 271. [On the Role of MRI Sequences in Cross-Dataset Generalization for Brain Tumor Segmentation](https://arxiv.org/abs/2608.29944)

**<font color=#1a73e8>作者：</font>** Henrique Zan Grande, João G. Pitol, Lucas B. Schuck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain tumor segmentation in magnetic resonance imaging (MRI) is a critical task for diagnosis and treatment planning. Despite the success of deep learning architectures such as U-Net and its variants, performance degradation across datasets remains a major challenge, particularly under domain shift and limited annotated data. To address this issue, this study systematically evaluates how individual MRI sequences influence model robustness across two well-known datasets. A ResUNet-based framework is employed, where each modality is trained independently to isolate its effect under a controlled cross-dataset evaluation protocol with tumor size stratification, without target-domain training, or with limited domain adaptation. Results show that the T2f/FLAIR sequence achieves the best cross-dataset performance, with Dice scores exceeding 75%. It consistently outperforms other modalities across most tumor size ranges, while multi-sequence training further improves performance. Additionally, even limited target-domain adaptation yields rapid initial gains, reducing the need for extensive annotations and costly retraining. Our source code is publicly available at this https URL.

---


### 272. [The Policy Deficit in AI x Social-Emotional Learning Research](https://arxiv.org/abs/2608.29950)

**<font color=#1a73e8>作者：</font>** Tran Van Cuong, Liu Yihan, Nguyen Van Tuong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) is increasingly integrated into social-emotional learning (SEL) initiatives, the need for evidence-based policy has become paramount. We systematically reviewed 65 peer-reviewed papers that examine the intersection of AI and SEL to investigate how these studies articulate policy implications. Our analysis revealed a substantial "policy deficit" in the current AI x SEL literature: nearly three-quarters of the studies did not mention policy implications at all. Using the "WH-question" framework (Who, What, Why, When/Where, and How), we map the policy implications narratives present in the literature and show that they often lack the specificity and actor-oriented guidance required for effective evidence-informed policymaking. We find a significant association between publication venue and policy engagement, suggesting that current academic incentive structures may prioritize technical innovation and pedagogical feasibility over explicit engagement with governance and regulation. This study identifies a "techno-solutionist" trap, where technical potential is foregrounded while the institutional conditions for responsible implementation remain under-specified. We conclude by proposing a shift from "implication-as-afterthought" to "implication-as-methodology" and offer a set of actionable guidelines for researchers, editors, reviewers, and policymakers to bridge the gap between AI innovation and educational governance. Rather than presenting policy as a generic ethical horizon, we argue that AI-SEL studies should systematically specify Who should act, What actions are recommended, Why these actions are needed, When and Where they apply, and How strongly they are framed, thereby strengthening the translation of AI x SEL innovation into educational policy and practice.

---


### 273. [Spatial Matryoshka Training for Multi-Granularity Visual Document Retrieval](https://arxiv.org/abs/2608.29951)

**<font color=#1a73e8>作者：</font>** Trishan Singha Roy, Arkadeep Acharya, Vishwajeet Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-modal late-interaction retrievers achieve strong retrieval on visually rich documents by representing each page as per patch embeddings and matching at the token level. However, this approach incurs high storage costs. Existing compression methods typically fix a single compression level at indexing time, limiting flexibility. We present ColSNAP (Spatial Nested Average Pooling)1, a training method that generates a nested hierarchy of compression levels directly from a backbone's patch grid. By spatially pooling patch embeddings into pro- gressively coarser tiers and training all tiers simultaneously, a single model learns to support retrieval at multiple compression levels without architectural changes. Crucially, a single encoding pass yields every tier, enabling the accuracy-storage trade-off to be configured at indexing time to match avail- able storage budgets, rather than being fixed during training. We demonstrate that models trained using ColSNAP maintain near full-resolution retrieval performance under substantial compression and that ColSNAP transfers effectively across multiple late-interaction backbones, and achieves most of its improvements via a lightweight adaptation stage applied to a pre-trained retriever.

---


### 274. [How Prolific Sellers Self-Present: Dissecting the Communication Patterns of 1.6 Million Reverb Listings](https://arxiv.org/abs/2608.29952)

**<font color=#1a73e8>作者：</font>** David M. Markowitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The current paper draws on self-presentation theory and warranting theory to evaluate how the language patterns in an online marketplace reflect seller status (i.e., a prolific seller versus an everyday seller). Using 1.6 million musical instrument listings from this http URL in search of content, style, and structural differences in seller product descriptions, the evidence suggested prolific sellers tend to focus more on objective and functional aspects of a product (e.g., its features and specifications) and less on subjective characteristics like tone, relative to everyday sellers. Prolific sellers also communicated in a more narrative-like style, which was driven by an elevated use of personal pronouns, and they used longer descriptions than everyday sellers. Therefore, what prolific sellers focus on tends to be quite technical, but how they communicate this information is typical of a story that is told to potential buyers. Implications for self-presentation theory and warranting theory are discussed.

---


### 275. [A Cyber-Physical Machine Tool Framework with a Real-Time Machining Process Digital Twin](https://arxiv.org/abs/2608.29955)

**<font color=#1a73e8>作者：</font>** Khalil Chakal, Tero Kaarlela, Jose Outeiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital Twins (DTs) have emerged as a key technology for improving the monitoring, optimization, and automation of manufacturing systems. However, existing Cyber-Physical Machine Tool (CPMT) implementations primarily represent the machine tool, while the machining process remains only partially synchronized with its physical counterpart. This paper extends a previously presented CPMT framework by introducing a hierarchical DT framework that simultaneously maintains DTs of both the machine tool and the machining process. The proposed framework integrates real-time CNC operational data, a voxel-based workpiece representation, synchronized process vibration measurements, and a persistent part DT repository for process replay, traceability, and future synthetic data generation.
Experimental evaluation demonstrated real-time operation at a 20 Hz machining-state update rate, interactive visualization exceeding 100 frames per second, and a mean depth reconstruction error of 0.16 mm. The implementation provides a foundation for AI-assisted machining applications while preserving the machine tool monitoring and teleoperation capabilities.

---


### 276. [Confidence-Aware Ensemble and Long-Word Refinement for Artistic Text Recognition](https://arxiv.org/abs/2608.29970)

**<font color=#1a73e8>作者：</font>** Lucas A. Dias, Henrique A. Schulz, Rafaela de Miranda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artistic Text Recognition (ATR) remains challenging because word images often combine decorative fonts, curved layouts, object-like characters, clutter, and severe distortions. This paper studies WordArt-V1.5 as a standardized benchmark for this setting and evaluates recent scene and artistic text recognizers under a common protocol. We propose a confidence-aware ensemble that combines SVTRv2, PARSeq, and MAERec after fine-tuning on the official training split. The ensemble selects predictions using the minimum confidence over disagreement positions, emphasizing characters that separate competing hypotheses. For long words, where a single character error can invalidate the whole prediction, we add a targeted refinement stage based on Needleman-Wunsch alignment and lexicon-guided correction. On the WordArt-V1.5 Test B split, the proposed system reaches 89.90% Word Recognition Accuracy, improving the best individual fine-tuned model by 1.77 percentage points. The long-word refinement produces a modest global gain, but improves the targeted long-word subset by 2.72 percentage points. Finally, an error analysis of all remaining mistakes shows that 48.8% are associated with labeling issues, visual ambiguity, or illegible samples, highlighting the value of diagnostic reporting for future ATR benchmarks and models. Our source code is available at this https URL.

---


### 277. [EDGE: Engine for Deterministic Graph Evaluation through Conversation Simulation from Graph Structured DSL Configuration](https://arxiv.org/abs/2608.29971)

**<font color=#1a73e8>作者：</font>** Ram Kulathumani, Regunathan Radhakrishnan, Anupam Tripathi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic systems evolve into complex multi agent orchestration workflows, there is a growing and critical need for systematic frameworks that measures an agent's behavioral consistency and determinism. In this paper, we introduce a formal evaluation methodology that is grounded in AgentGraph, a planner powered by a domain specific language that represents agent reasoning through a dynamically adjustable directed graph. We leverage this structural formalism and utilize graph traversal algorithms that exhaustively enumerate conversational paths, forming a comprehensive evaluation set that captures the agent's complete behavioral space. We then systematically replay these reproducible trajectories to compare observed outputs and state transitions against the intended DSL specification. To quantify reliability, we define novel metrics that measure response and trajectory determinism, structural adherence and semantic consistency across both exact replays and their linguistic variants. Our system's results demonstrate that agents configured using frameworks like AgentGraph and LangGraph with explicitly structured node transitions show superior determinism over agents that are not configured with controlled transitions.

---


### 278. [A New Algebraic Algorithm for LWE](https://arxiv.org/abs/2608.29977)

**<font color=#1a73e8>作者：</font>** Luca Campa, Massimo Fumiani, Arnab Roy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Learning With Errors (LWE) problem, introduced by Regev in 2005, is central to modern cryptography and post-quantum security. The algorithms to solve the search version of the problem, Search-LWE, can be broadly categorised into algebraic, combinatorial and lattice-based.
In this work we propose a new algebraic algorithm for the Search-LWE problem. At a high level, the algorithm combines linear-algebraic techniques with S-polynomial-based methods from Groebner basis computation. We provide a direct complexity analysis of our algorithm, avoiding semi-regularity assumptions and complexity bounds derived from the degree of regularity. Our algorithm achieves a polynomial improvement in complexity over prior results that use Groebner basis methods to solve Search-LWE.

---


### 279. [Breaking Ambient Trust: In-Network Per-Process Access Control Against Lateral Movement](https://arxiv.org/abs/2608.29979)

**<font color=#1a73e8>作者：</font>** Osama Bajaber, Bo Ji, Peng Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise networks remain vulnerable to Advanced Persistent Threats (APTs), where adversaries gain an initial foothold and move laterally across the network, accumulating access permissions hop by hop to reach critical targets. Existing network defenses cannot track user movement at the process level across the network; instead, they grant ambient trust to all processes within a host. As a result, once a host is compromised, malicious processes inherit the victim's permissions, thereby expanding the attacker's access scope and enabling further lateral movement. To address this gap, we present NetZone, an in-network access control that confines each user process to a fixed access scope that persists as the user moves across the network. NetZone introduces a new abstraction, called AccessScope, which represents a lightweight access capability bound to the user's processes. Each AccessScope encodes the set of hosts a user identity is authorized to access and is embedded in the process's outgoing network traffic for validation before reaching its destination. As users pivot across hosts, AccessScope propagates with their traffic, rebinds to the receiving process, and persists across hosts. This ensures that regardless of network location, the user's processes are consistently governed by their bound AccessScope and their access permissions remain unchanged. To handle the high volume of network traffic generated by processes, we develop a data-plane co-design that integrates programmable switches with eBPF. NetZone employs a set of in-network optimizations and lightweight AccessScope persistence techniques to inspect the embedded AccessScope on the fly, enabling line-rate processing of high traffic volumes with negligible latency overhead. Our extensive evaluations show that NetZone can effectively defend against sophisticated attack scenarios without introducing noticeable overhead.

---


### 280. [FIS-OT: Feature-Induced Optimal Transport for Unsupervised Action Segmentation](https://arxiv.org/abs/2608.29980)

**<font color=#1a73e8>作者：</font>** Linxiang Peng, Xinyao Qin, Jinhan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised action segmentation is a challenging task. It involves finding action categories and boundaries in videos without labels. Existing Optimal Transport (OT) methods use global constraints. This causes them to overlook the use of local information. Furthermore, existing Optimal transport architectures are prone to confirmation bias because they overly trust the pseudo-labels they generate. This causes models to learn from noise in the early training stages. To address these issues, we propose FIS-OT. It is a novel Feature-Induced Structured Optimal Transport framework. First, we introduce a Feature Enhanced Generator (FEG) module. It serves as an internal regularizer. By using triplet loss, FEG captures local consistency. It provides robust supervision that is independent of noisy pseudo-labels. Second, we propose a Feature-Induced Residual Structural Prior. This combines a fixed temporal backbone with dynamic feature similarities. This design ensures temporal continuity. It also allows the solver to adapt to complex action structures. Finally, we establish a cyclic optimization loop. This aligns local feature learning with global structural alignment. Extensive experiments on the three datasets show the effectiveness of our method.

---


### 281. [Robust Broad Learning System with Wave Loss for Classification under Data Uncertainty](https://arxiv.org/abs/2608.29983)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, A. Varshney, A. Quadir 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Broad Learning System (BLS) offers an efficient alternative to deep architectures by enabling fast learning through randomized feature mapping and closed-form solutions. However, its reliance on squared error loss makes it highly sensitive to noise, outliers, and corrupted labels, limiting its reliability in real-world scenarios. To address this limitation, we propose Wave-BLS, a robust broad learning framework that integrates the wave loss function, which is asymmetric, bounded, and smooth, enabling controlled penalization of large errors. The proposed formulation replaces the standard least-squares objective with a wave-loss-based optimization problem, solved efficiently using a Nesterov accelerated gradient (NAG)-based scheme without requiring matrix inversion, thereby improving scalability. Extensive experiments on 30 UCI benchmark datasets demonstrate that Wave-BLS consistently outperforms classical BLS and several robust variants. Statistical validation using Friedman and Nemenyi post-hoc tests confirms the significance of the observed improvements. Furthermore, robustness evaluations under controlled noise and outlier injection reveal that Wave-BLS exhibits substantially slower performance degradation compared to BLS, even in challenging contamination settings. These results establish Wave-BLS as a stable and robust alternative to existing broad learning models for learning under data uncertainty.

---


### 282. [SVI2LoD3: Agent-Driven Reconstruction of LoD3 Facade Openings in Semantic 3D City Models from Volunteered Street View Imagery using Large Language and Visual Models](https://arxiv.org/abs/2608.29992)

**<font color=#1a73e8>作者：</font>** Elmehdi Kanna, Lukas Arzoumanidis, Huynh Duc An Son Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an end-to-end, agent-driven pipeline for the LoD3 reconstruction of facade openings in 3D city models, producing directly usable CityGML-conform outputs. In contrast to existing approaches that rely on supervised semantic segmentation and therefore require large amounts of manually annotated training data, the proposed method employs a zero-shot segmentation strategy. This substantially reduces the annotation effort while still achieving strong performance in our benchmark on the eTRIMS dataset. A further key contribution is the enforcement of correct partonomic hierarchies, thereby producing CityGML-conform LoD3 building models. Beyond the reconstruction pipeline itself, this work also introduces a novel evaluation metric for facade reconstruction, termed Facade Feature Distance (FFD). Unlike conventional metrics such as mIoU or FRDS, which assess similarity primarily through pixel-wise overlap, FFD measures distance in a high-level feature space derived from a vision transformer. In doing so, it captures both semantic correctness and architectural layout, providing a more suitable assessment of facade reconstruction quality. The proposed pipeline and evaluation strategy together offer a practical and scalable contribution toward the automated generation and analysis of semantically enriched 3D city models. The developed code is published at: this https URL.

---


### 283. [Discrete Diffusion Bridges for Spatiotemporally Aligned Image Translation and Generation](https://arxiv.org/abs/2608.29997)

**<font color=#1a73e8>作者：</font>** Xing Xie, Jiawei Liu, Shijun Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Discrete Diffusion Bridges (DDB), a novel framework designed to resolve the fundamental spatiotemporal misalignment of standard discrete diffusion in image translation and generation. By corrupting data into a pure mask state via a random schedule, the conventional forward process induces a twofold misalignment: spatially, this pure-mask destination entirely discards the rich structural priors of the source image; temporally, the random masking order inherently contradicts the ``easy-first, hard-last'' decoding mechanism used during inference. To address this, DDB constructs a direct and efficient trajectory between domains. Spatially, we introduce a hybrid absorption mechanism that redefines the absorbing state to a stochastic mixture of mask and source tokens, effectively injecting source prior as spatial anchors into the latent space. Temporally, we design an information-guided noise schedule that quantifies semantic variation to prioritize the corruption of high-information regions at earlier timesteps. This ensures the model learns to resolve difficult semantic changes using robust context from invariant regions. Extensive experiments validate the versatility and robustness of our framework across diverse generative paradigms. DDB effectively balances edit alignment with structural fidelity across both text-guided semantic manipulation and pure structural image translation, while inherently complementing text-to-image generation and guaranteeing robust high-quality decoding under extremely low sampling steps. Code and models are available at \href{this https URL}{this https URL}.

---


### 284. [The Intervention Gap in Latent World Models](https://arxiv.org/abs/2608.29998)

**<font color=#1a73e8>作者：</font>** Donna Vakalis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning-time intervention fidelity is a distinct, measurable property of a learned world model: whether the model's own open-loop transitions move task variables the way matched environment interventions do. In the settings we test, it is neither revealed by reward fit nor ensured by task-anchored training. Across released TD-MPC2 checkpoint sizes, episode return falls as an operator-error diagnostic on task observables grows, while reward-prediction error stays small and nearly flat, and a self-supervised world model trained without task signal preserves the same operator substantially better than a task-anchored model on the shared task. A capture-gated matched-intervention audit then localizes what fails. On Cheetah, three LeWorldModel checkpoints capture the current task query and support decodable real intervention effects; however, their imagined five-step effects are worse than predicting no effect and worse than an environment-endpoint oracle. The failure is task-direction rotation with excess gain, not feature collapse. This severe pattern is conditional: five PreJEPA seeds retain an oracle-relative deficit without it, Finger Spin experiments extend the deficit beyond locomotion with heterogeneous severity across seeds, and shared-bank effect geometry is both candidate- and support-dependent. We also test practice-side questions. In DreamerV3 the posterior distribution, not its sample, carries the current query; ensemble disagreement ranks error only near training support; and a frozen support-aware score degrades held-out error ranking in both tested transfer directions while native disagreement remains informative in both. We conclude that intervention fidelity must be audited directly, capture-first, on the model's native interface.

---


### 285. [OPAL: Orthonormal Prototype Alignment Learning for Interpretable Image Classification](https://arxiv.org/abs/2608.30003)

**<font color=#1a73e8>作者：</font>** Ilán Carretero, Gustavo Jesús Angulo, Rocío del Amor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototypical part-based models provide explainable predictions by comparing input regions to learned prototypes. However, current approaches are burdened by complex, multi-stage training pipelines and heavily rely on auxiliary regularization to prevent prototype collapse. To overcome these limitations, we introduce Orthonormal Prototype Alignment Learning (OPAL), a single-stage, end-to-end framework that simplifies interpretable classification. Our approach anchors the latent space using predefined orthonormal bases, embedding each class within a dedicated subspace spanned by fixed part-prototypes. To achieve precise part localization, OPAL enforces spatial competition across feature maps. This mechanism isolates sparse, discriminative regions, directing each prototype to consistently attend to the same semantic concept across different images. By framing classification as a direct representation alignment task, our method eliminates the need for auxiliary losses. Extensive experiments on fine-grained benchmarks demonstrate that OPAL outperforms both its non-interpretable counterparts and state-of-the-art part-prototype methods, delivering granular visual explanations by explicitly revealing the specific image regions driving every prediction. Code is available at this https URL.

---


### 286. [Beyond Object Authentication: Context-Closed Post-Quantum Authentication for the WebPKI](https://arxiv.org/abs/2608.30004)

**<font color=#1a73e8>作者：</font>** Anis Bkakria  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum migration increases WebPKI authentication cost, but authenticating a compressed certificate object does not by itself preserve the mutable authorization context under which a relying party accepts it. We formalize \emph{context closure}: the authenticated projection accepted by a verifier must determine the selected authorization semantics it claims, relative to declared source contracts and event-coverage witnesses. We instantiate this idea with \LRp, a two-plane post-quantum construction that authenticates mutable CA-context state in an update plane while the warm path carries only state-local dependency references selected by explicit profile negotiation.
In a pinned CCADB reconstruction, we obtain 44,912 path/view contexts and 16,858 physical CA lineages across Apple, Chrome, Microsoft, and Mozilla views. The core compiler yields $m_{50}=6$, $m_{95}=16$, and $m_{\max}=18$ typed dependencies. A warm LR+ selector therefore costs 296, 776, and 872 bytes at median, p95, and maximum, compared with 3,842, 5,932, and 6,350 bytes for a one-signature stateless bundle carrying the same dependency vector. The retained all-view closure state is 16.15 MB, and per-view lifecycle crossovers range from 19.60 to 50.41 median-path warm authentications/day under the stated checkpoint and update model. The implementation and evaluation artifact are available at this https URL

---


### 287. [Multimodal Takeover Requests for Drivers with Hearing Loss: Implications for AI-Enabled Communication in Automated Vehicles](https://arxiv.org/abs/2608.30013)

**<font color=#1a73e8>作者：</font>** Aries Chu, Wei-Hsiang Lo, Gaojian Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> More than 430 million people worldwide live with disabling hearing loss. Although people with hearing loss are legally permitted to drive and may benefit from conditionally automated vehicles, SAE Level 3 systems still require drivers to respond to takeover requests when automation reaches its limits. Existing takeover requests often rely on auditory information, yet little evidence addresses visual and tactile designs for drivers who cannot rely on sound. This driving-simulator study with 40 participants examined the effects of information type (instructional, informative, and baseline), signal type (visual, tactile, and visual-tactile), and hearing condition (normal hearing and simulated hearing impairment) on takeover performance. Information type significantly affected reaction time, with baseline displays producing the shortest times. Signal type significantly affected reaction and takeover time, with visual-tactile displays producing the shortest times. The interaction between signal type and information type was significant for all three measures. Visual-tactile displays produced the shortest reaction times within every information type. With visual-tactile signaling, simple baseline alerts prompted the fastest reactions and the most abrupt maneuvers, whereas informative content produced the lowest mean maximum resulting acceleration. Hearing condition showed no significant main effect on any measure. These findings suggest that AI-enabled vehicles can support urgent takeover communication through visual-tactile displays and can adapt message content to the time available and the maneuver quality required, with implications for drivers across hearing abilities.

---


### 288. [Looking Around by Looking Around: Omnidirectional Gaze-based VR Viewport Control](https://arxiv.org/abs/2608.30014)

**<font color=#1a73e8>作者：</font>** Hock Siang Lee, Jinghui Hu, Florian Weidner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional VR viewport control primarily relies on head and torso movement, which can be effortful and limiting in both constrained and extended-use settings. We introduce Looking Around by Looking Around (LALA), a gaze-based VR pitch-and-yaw viewport control technique designed for natural and effortless omnidirectional exploration via eye movements, without requiring or obstructing movement of the head, hand, or body, offering a low-effort and highly accessible interaction method. Because gaze is primarily used for perception and exhibits oculomotor and perceptual asymmetries, using it directly for control is difficult. To address this, we designed an asymmetric omnidirectional control profile for the eye, then built on it to exploit tendencies for eyes to stay within comfortable regions for viewport control. We evaluated LALA in a user study (N=18) featuring two contrasting tasks: alignment towards known directions and open-ended visual search towards unknown directions. LALA was strongly preferred over the traditional baseline, achieving competitive performance while enabling fully hands-free interaction with minimal physical movement.

---


### 289. [Multiclass Linear Perceptrons with Multiplicative Margins](https://arxiv.org/abs/2608.30028)

**<font color=#1a73e8>作者：</font>** Dmitri Rachkovskij, Evgeny Osipov, Olexander Volkov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a family of multiclass linear Perceptron classifiers with a multiplicative margin mechanism (MMPerc), as an alternative to standard margin-free and additive margin Perceptrons. The multiplicative formulation enforces classification confidence by requiring the true class score to exceed that of competing classes by a specified fraction of itself, rather than by a fixed additive threshold. This avoids dependence on score magnitudes arising from varied norms of data and class weight vectors. We propose several architectural and algorithmic variants of MMPerc, derive associated loss functions and mistake bounds for both linearly separable and non-separable data, and analyze key design considerations, including bias, margin threshold selection, and training modes. Extensive experiments on synthetic and real datasets show that MMPerc classifiers typically outperform the standard Perceptron, as well as classic baselines such as Support Vector Machines and Ridge classifiers. Owing to their simplicity, minimalistic design, and computational efficiency, MMPerc classifiers are promising candidates for conventional machine learning tasks, linear evaluation of Deep Neural Networks, integration with Hyperdimensional Computing / Vector Symbolic Architecture representations, and deployment in resource-constrained applications.

---


### 290. [Input-Adaptive Gating of a Dehazing Front-End for On-Device Perception in Smoke-Obscured Environments](https://arxiv.org/abs/2608.30034)

**<font color=#1a73e8>作者：</font>** Seongjun Kang, Ishaan Garg, Vishnu Bharadwaj  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two-stage vision pipelines often place an enhancement network before a task network, on the assumption that a cleaner input produces a better output. We evaluate this in a firefighter assistance pipeline, where a dehazer precedes an edge detector that renders smoke-filled rooms as structural outlines. Both were designed for a Raspberry Pi 4, at 355K and 23K parameters, and quantized to UINT8 via TensorFlow Lite. The float dehazer reaches 18.60 dB peak signal-to-noise ratio (PSNR) on held-out real smoke against 13.60 dB unprocessed and 17.08 dB for an AOD-Net trained on the same data, and the edge detector reaches an F-measure at optimal dataset scale (ODS) of 0.738, outperforming an optimized Canny's result of 0.692. Dehazing improves edge extraction under dense smoke but degrades it on clear and lightly hazed frames, where the dehazer discards more detail than the haze obscures. We therefore run the dehazer only when a dark channel haze estimate exceeds a threshold, a 10.1 ms test that lets the pipeline save 469.6 ms on the dehazing stage. Averaged over four haze levels, gating is more accurate than either fixed decision, at 0.675 mean ODS against 0.664 for always dehazing and 0.630 for never dehazing. It reduces the mean per-frame time on the Raspberry Pi from 569 ms to 321 ms, and on clear frames increases the frame rate fivefold, from 1.8 to 9 frames per second.

---


### 291. [ActReal: System-Level Mobile Agents Challenge Mobile Automation Detection](https://arxiv.org/abs/2608.30038)

**<font color=#1a73e8>作者：</font>** Mingshuo Wang, Hanqing Guo, Huining Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System-level mobile agents are evolving from fixed scripts into adaptive systems that continuously observe interfaces, reason, and adjust their actions, allowing automated attacks to navigate dynamic UIs and complete complex tasks. Existing applications detect automation using touch trajectories, action timing, and the physical coupling between touch and inertial measurement unit (IMU) signals. However, a privileged system-level agent executor can control both touchscreen input and application-visible sensor delivery, enabling it to jointly generate time-aligned touch and six-axis IMU signals and evade these defenses. We present ActReal, a physical-action attack framework for system-level mobile agents. ActReal converts semantic agent actions into task-valid touch and IMU events using genuine-trajectory adaptation and physics-guided IMU generation. ActReal achieves a mean event-level attack success rate of 77.5\%; even when detectors jointly observe touch and IMU, its attack success rate remains 71.1\%.

---


### 292. [Forget or Fine-tune? A Comparative Study of Machine Unlearning Strategies for Noisy Label Correction](https://arxiv.org/abs/2608.30046)

**<font color=#1a73e8>作者：</font>** João L. P. Santana, Filipe R. Cordeiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noisy labels remain a critical challenge for training deep neural networks, since memorizing incorrect labels degrades generalization. Once noisy samples are identified after training, the standard solution is to retrain the model from scratch on the cleaned dataset, which is increasingly expensive as datasets and models grow. Machine Unlearning (MU) has recently emerged as a computationally efficient alternative, but the relative effectiveness of different MU strategies for noisy-label correction remains poorly understood. In this work, we conduct a comparative empirical study of five MU methods (NegGrad, Fine-Tuning (FT), Random Labeling (RL), SalUn, and MUNBa) across symmetric, asymmetric, instance-dependent, and open-set noise on CIFAR-10, CIFAR-100, and the real-world noisy dataset Food-101N. Our central finding is that the appropriate unlearning strategy is conditioned on the noise structure. Simple FT is a strong baseline across most closed-set scenarios; RL and SalUn are the most consistently robust methods and, under instance-dependent noise, approach retraining accuracy at a fraction of the computational cost; MUNBa shows advantages mainly under extreme symmetric noise. Under open-set noise, in contrast, we show that retraining on the cleaned subset degrades accuracy relative to the noisy baseline, so approximating the retrained model is not an adequate objective in this regime. On Food-101N, all MU methods remain competitive and achieve accuracies close to retraining despite reducing runtime by an order of magnitude. These findings provide practical guidelines for selecting MU strategies for post-training noisy-label correction.

---


### 293. [Mitigating Over-Optimization in PRM-Guided Search in Mathematical Reasoning by Optimizing the Guide](https://arxiv.org/abs/2608.30051)

**<font color=#1a73e8>作者：</font>** Taejong Joo, Diego Klabjan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) provide dense step-level guidance for search-based reasoning, enabling inference-time compute to be allocated toward promising partial solutions. However, recent evidence suggests that PRM-guided search can over-optimize imperfect process rewards, pruning viable trajectories while expanding spurious ones. In this work, we theoretically show that directly leveraging PRM score is vulnerable to verifier noise through an extreme-value effect: non-viable prefixes become more likely to receive spuriously high scores as reasoning depth increase. Therefore, we formulate the PRM-guided search as a robust optimization problem over plausible reward perturbations, termed maximin PRM-guided search, leading to a training-free robust process supervision method that preserves promising alternatives when step-level scores are noisy. Maximin PRM-guided search mitigates this failure mode by reducing sensitivity to over-optimized PRM outliers. Without fine-tuning or online adaptation, maximin search consistently improves the PRM-guided search by 17-35\% on average, outperforming outcome- and step-level baselines in 14 out of 16 settings. Our source code is available at this https URL.

---


### 294. [When 3D Gaussian Splatting Recovers Real Surfaces](https://arxiv.org/abs/2608.30054)

**<font color=#1a73e8>作者：</font>** Songhe Wang, David Johnathan Miller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When does 3D Gaussian Splatting (3DGS) recover the true scene surface rather than just overfitting view-dependent appearance? We answer this by developing a mathematical framework based on a first-hit rendering abstraction that cleanly isolates geometry from appearance. We prove that geometric misalignment forcefully converts spatial textures into high-frequency angular signals via parallax. This establishes a strict identifiability window: if angular capacity is bounded, surface-consistent solutions are mathematically preferred; if unrestricted, the same images can be perfectly explained by an incorrect, opaque billboard geometry. Experiments on synthetic stress tests confirm this prediction, showing billboard failures emerge precisely at high angular capacities. Conversely, in the real-world datasets we evaluate under standard capture protocols, reconstructions remain surface-consistent even at high SH degrees, which is consistent with the prediction that rich spatial texture can push billboard solutions outside the tested angular-capacity range.

---


### 295. [Game-Agnostic Value Functions through Automatic JSON Feature Extraction](https://arxiv.org/abs/2608.30056)

**<font color=#1a73e8>作者：</font>** Dien Nguyen, Diego Perez-Liebana  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> JSON Bag-of-Tokens (JSON-Bag) is a recently proposed method to generically represent game trajectories by tokenizing their JSON descriptions. We introduce JSON-Bag VF, a game-agnostic approach to training value functions for game-playing agents using JSON-Bag prototypes. We show that this approach can be enhanced with Random Forest-based feature selection and a method to select game-stage-specific features. We evaluate JSON-Bag VF with One-step-look-ahead (JSON-Bag OSLA) on six tabletop games over different combinations of prototype-tokenization and feature selections. JSON-Bag OSLA outperforms baseline OSLA agents in most games. Our analysis also shows that feature selection significantly improves JSON-Bag VF and that feature selection is the most important factor in JSON-Bag VF performance, over prototype-tokenization.

---


### 296. [Occlusion-induced risk and interventions in pedestrian-autonomous truck interactions on multi-lane roads: A virtual reality study](https://arxiv.org/abs/2608.30066)

**<font color=#1a73e8>作者：</font>** Yun Ye, Yuan Che, S.C. Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous trucks (ATs) may introduce distinct pedestrian-safety risks because of their large physical dimensions, constrained braking capability, limited driver-based communication cues, and potential to occlude surrounding traffic. This study employed a controlled virtual reality experiment with 54 participants to investigate pedestrian-AT interaction risk in an unsignalized multi-lane crossing scenario and to evaluate occlusion-targeted risk mitigation strategies. The experiment examined the effects of near-side vehicle type, weather condition, and far-side vehicle yielding strategy on pedestrian behavior, perceived risk, and objective safety. Based on a representative high-risk scenario, three targeted interventions were designed and tested: an environment-aware external human-machine interface (eHMI), a projected eHMI, and an auditory warning. The results showed that ATs increased perceived risk and encouraged more cautious crossing behavior, suggesting a risk-compensation effect. However, this compensation was weakened under rainy conditions, where braking-related safety margins were reduced. AT-induced occlusion further increased far-side interaction risk by limiting pedestrians' recognition of hidden vehicles. Among the three interventions, the projected eHMI showed the best overall performance, improving objective safety margins, enhancing risk awareness, and supporting behavioral adjustment. These findings highlight the need for AT-specific interface and warning strategies that address both intention communication and risk localization.

---


### 297. [Selection, Representation, and Execution in Sparse Fourier Neural Operators](https://arxiv.org/abs/2608.30070)

**<font color=#1a73e8>作者：</font>** Abdul Qadir Ibrahim, Martin Burger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse representations are often expected to make models smaller and also reduce inference cost. For Fourier Neural Operators (FNOs), these objectives are not equivalent or do not always align: removing parts of the learned operator can leave the underlying transforms and dense computations unchanged, while changing the grid on which the model is evaluated can introduce overhead of its own. We therefore distinguish sparsity in the representation, in the stored parameters, in the theoretical operation count, and in measured runtime, and present an empirical study of several routes toward sparse FNOs that tests each transition between them separately. Coarsening the execution grid reduces the theoretical cost without reducing measured latency, and adding a correction term recovers accuracy at the cost of making the model slower. Even an 83\% parameter reduction remains slower than the dense baseline under ordinary execution. These results motivate a stricter definition of useful sparsity: the deployed operator must preserve solution accuracy and map its reduced support to a genuinely cheaper execution path.

---


### 298. [Tracing Generated Samples to Training-Data Clusters in Flow-Matching Models](https://arxiv.org/abs/2608.30081)

**<font color=#1a73e8>作者：</font>** Rania Briq, Ohad Fried, Michael Kamp 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding which training samples influence a generated image is an important problem in generative modeling. In flow matching, training samples influence the generated image through the velocity field along the generation trajectory. Removing samples to examine their counterfactual influence changes the velocity field, and the resulting effect on the final image depends on how the change propagates through the trajectory. Consequently, local changes in the velocity field do not necessarily predict the final counterfactual effect.
This work investigates attribution in flow-matching models through a hybrid analytical--learned approach, and uses it to derive trajectory-based attribution scores at the cluster level. We evaluate these attribution scores using independently retrained leave-one-cluster-out (LOO) models, and compare with several attribution baselines using two different flow-matching latent spaces. Our experiments show that semantic similarity constitutes a strong baseline, while the closed-form trajectory-based attribution is competitive in some metrics without requiring counterfactual retraining or model gradients.
Our results show that attribution in flow matching depends not only on semantic similarity to training samples, but also on the latent representation, trajectory dynamics, and how influence is propagated to the final output.

---


### 299. [The Nearest Target Is the Wrong One: Target Separation in Arc2Face Identity Unlearning](https://arxiv.org/abs/2608.30087)

**<font color=#1a73e8>作者：</font>** Zeynel Tok  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlearning an identity from a face-conditioned generator by redirecting its conditioning embedding can silently fail if the redirected output is still verified as the original person. We show that this failure depends on a controllable choice of how far the redirection target lies from the forget identity in recognition space, and that the most intuitive target, the nearest neighbour, is the one most likely to cause it. We audit Arc2Face with a locked ArcFace protocol and a projection adapter that redirects identity conditioning before generation. On a hard-neighbour stress test built from the hardest 0.5% of eligible identities, four target-selection policies show a monotonic response: clean forgetting rises from 9/30 groups under the nearest hard target to 30/30 under the least similar one. Mean forget-identity re-identification falls from 51.9 to 0.0 while mean retention stays flat. This reflects successful redirection rather than outputs becoming unverifiable: 710 of 720 least-sim-hard generations arrive at the chosen target, with no leakage to unrelated identities. Re-verifying identical images with an independent recogniser (AdaFace) preserves that trend, correlating at r=0.94, arguing against a verifier artefact. Target separation is thus a first-order, reportable design variable for identity unlearning.

---


### 300. [A Lightweight Phenology-Aware YOLOv5 Framework for Tomato Growth Stage Detection in Resource-Constrained Bhutanese Greenhouse Environments](https://arxiv.org/abs/2608.30088)

**<font color=#1a73e8>作者：</font>** Sherab Gocha, Sou Nobukawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate detection of tomato growth stages is essential for stage-specific greenhouse management and precision agriculture. In Bhutan, greenhouse cultivation is affected by altitude variability, large diurnal temperature fluctuations, diffuse illumination, limited automation, and a scarcity of locally annotated datasets, limiting the applicability of conventional deep learning models. This work proposes Pheno-Lite + Efficient Channel Attention (ECA), a lightweight, phenology-aware object detection architecture derived from Ultralytics YOLOv5 for tomato growth stage recognition. A balanced dataset of 2,464 annotated images was constructed from locally collected greenhouse images in Bhutan and publicly available tomato images, with augmentation designed to simulate local greenhouse conditions. The dataset includes vegetative (820), flowering (824), fruiting (820), and background (26) samples. The proposed architecture introduces two customized backbone modules: C3 PhenoLite, which enhances spatial and texture feature extraction using depthwise residual refinement, and C3 ECA, which strengthens inter-channel feature interactions through efficient channel attention. The proposed model achieves 90.6% precision, 88.8% recall, and 92.6% mAP@50, with 4.0 million parameters and 10.9 GFLOPs at 640 x 640 resolution. These results demonstrate its potential for real-time and climate-resilient greenhouse deployment in Bhutan.

---


> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
