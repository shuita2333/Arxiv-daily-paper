# 📦 其他研究 | 2026年10月23日

> 本类共 **232** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-232**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-232**

---

### 201. [CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion](https://arxiv.org/abs/2610.29915)

**<font color=#1a73e8>作者：</font>** Kai Zhu, Yintianrun Zhang, Shuwei Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based video generation models (VGMs) can produce visually plausible videos, yet their camera ego-motion often drifts over long horizons. Camera ego-motion determines how the viewpoint changes between frames and is essential for maintaining consistent geometry and trajectories. To address this problem, we propose CausalAlign, a causal alignment framework with two components. First, we diagnose how precise ego motion is represented, used, and retained within VGMs using linear probes and causal interventions, revealing a rise-and-fall pattern during denoising. Second, we strengthen ego-motion state in VGM by aligning the representations at the identified layers to a 3D foundation model through delta-token space. This space encodes the changes between consecutive frames, allowing the alignment to focus on ego-motion dynamics rather than static scene content. With Wan2.2 fine-tuned on DL3DV and RealEstate10K, CausalAlign can largely improve motion accuracy, geometric consistency, and temporal smoothness, while preserving visual quality. For example, it improves geometric consistency by more than 20% relative to the base model. Moreover, with the fine-tuned VGM, CausalAlign improves the success rate of world action models (WAMs) by 10 points on mobile manipulation tasks of RoboCasa365 benchmark. Overall, CausalAlign improves ego-motion consistency in diffusion-based VGMs and yields noticeable gains in embodied models.

---


### 202. [Preventing Model Extraction in Contextual Linear Optimization](https://arxiv.org/abs/2610.29918)

**<font color=#1a73e8>作者：</font>** Adam N. Elmachtoub, Tianyi Lin, Wenxuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consider a contextual linear optimization problem, where a predict-then-optimize (PTO) system returns optimal decisions without revealing the cost vectors used in its downstream linear program. Our focus is on how to prevent attackers, who can submit context queries, from extracting the underlying prediction model. Although the cost-to-decision map is many-to-one, observations across contexts can reveal the underlying prediction model. For linear models, we provide sufficient conditions where the attacker can learn the model up to positive scaling by only observing the decision. These conditions motivate an adaptive attack that alternates inverse optimization with boundary sampling, i.e., using context queries leading to decision boundaries of the current attacker model. To prevent extraction, we propose a mechanism that perturbs decisions only when the predicted cost vector is near a decision boundary. We establish a regret bound in terms of the perturbation radius. For the attackers that fit the defended responses as optimal decisions under the evaluation distribution, we also prove a lower bound on expected extraction error. Experiments on synthetic instances and real data quantify the security-performance trade-off of the defense mechanism and illustrate that our defense can increase the extraction error.

---


### 203. [Your Benchmark Is an Empirical Measure Over Difficulty](https://arxiv.org/abs/2610.29927)

**<font color=#1a73e8>作者：</font>** Yifan Sun, Naicheng Yu, Jiawen Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A benchmark is not merely a collection of test questions; it naturally induces an empirical measure over difficulty. In this work, we develop this measure-based view of benchmark evaluation. This perspective allows us to identify and formalize two central failure modes: measure mismatch, where the benchmark difficulty distribution differs from the intended difficulty distribution, and coverage gaps, where uncovered regions along the difficulty axis prevent benchmarks from detecting meaningful localized training progress. We propose two diagnostic metrics that capture these two failure modes and provide rigorous theoretical guarantees. Empirically, we analyze 25 popular benchmarks spanning 7 domains using carefully estimated item difficulties. Our results show that many benchmarks implicitly overweight certain difficulty regions, so their leaderboard conclusions should be interpreted with caution; others leave substantial portions of the difficulty axis uncovered, limiting their ability to monitor the model improvement process. Finally, we turn diagnosis into action by introducing BenchFill, a simple difficulty-targeted item rewriting algorithm that effectively reduces local coverage gaps.

---


### 204. [DewHand: Direct Metric World-Space Hand Motion Reconstruction from Egocentric Videos](https://arxiv.org/abs/2610.29936)

**<font color=#1a73e8>作者：</font>** Naru Suzuki, Satoshi Ikehata, Takehiko Ohkawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering metric world-space hand motion from egocentric video supports understanding human interactions and transferring them to embodied agents. Three challenges complicate this task: multi-stage pipelines propagate errors from independently estimated hand and camera motion; monocular observations leave physical scale ambiguous; and occlusion and out-of-view hands admit multiple plausible motion trajectories. We present DewHand, a unified model for direct joint reconstruction of world-space hand and camera motion. To avoid compounding errors from multi-stage estimation, DewHand jointly predicts hand and camera motion in a shared world coordinate system within a single-stage pipeline. To resolve metric-scale ambiguity, it combines scene-level geometric features from VGGT-$\Omega$ with metric-space supervision, while hand-specific features preserve fine-grained articulation. To handle occlusion and out-of-view hands, we formulate reconstruction as conditional motion generation with flow matching. Under the same architecture, this generative formulation outperforms direct regression in both accuracy and temporal smoothness with only two sampling steps. Experiments on HOT3D and ARCTIC demonstrate improved world-space accuracy and temporal consistency over state-of-the-art methods. DewHand reduces rigid-aligned world-space error relative to StableHand from 32.9 to 28.4 mm on HOT3D and from 76.2 to 36.2 mm on ARCTIC. It also recovers camera scale within 10% on two thirds of HOT3D clips, versus about a quarter for SLAM. Moreover, in zero-shot evaluations on HoloAssist, H2O, and TACO, captured with different devices, DewHand achieves the lowest rigid-aligned world-space error (WA-MPJPE) on each dataset.

---


### 205. [Towards English - Mizo Legal Machine Translation: Corpus Creation, Analysis, and Benchmarks](https://arxiv.org/abs/2610.29943)

**<font color=#1a73e8>作者：</font>** Telem Joyson Singh, Sanabam Boyshana, Sanasam Ranbir Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Indian court proceedings are held in English, so speakers of languages with limited translation technology have limited access to them. We present the first English Mizo parallel dataset of Indian court judgments. It contains 13,168 sentence pairs from the Gauhati High Court and the Supreme Court of India. Professional native Mizo translators translated complete documents; sentence pairs were manually aligned, and two independent reviewers checked the results. Our study finds that English words are borrowed in a very selective way: official and legal terms are almost always kept in English, but words for everyday things like actions, situations, and results are usually expressed in native Mizo. Mizo diacritics are also used inconsistently across the corpus. When we fine tune the NLLB 200 1.3B model on our training data, it scores 27.47 BLEU on a balanced legal test set of 1,000 sentence pairs, an improvement of 7.16 BLEU over the base model. However, it still uses English words about three times more often than a human translator does.

---


### 206. [Training-free Acceleration for Blind Compressed Image Restoration via Activation-Calibrated Singular Value Decomposition](https://arxiv.org/abs/2610.29959)

**<font color=#1a73e8>作者：</font>** Suhang Yao, Xin Li, Xijun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based models achieve strong performance on blind compressed image restoration (CIR) under unknown compression settings, but their densely stacked projection operators make deployment costly. We study training-free acceleration for such models through an empirical, operator-level analysis. Specifically, we profile where computation is concentrated, characterize channel-wise activation distributions under compressed inputs, and examine the singular-value decay of representative projection weights. These measurements identify the recurring projections in the attention, feed-forward, convolutional, and prompt-conditioning pathways as effective low-rank replacement targets that preserve the original inference graph. They further establish truncated SVD (TSVD) as a principled training-free baseline for blind CIR and reveal why a uniform low-rank objective is mismatched to the channel-imbalanced feature distributions of compressed images. Accordingly, we formulate Activation-Calibrated Singular Value Decomposition (ASVD) for this restoration setting, deriving low-rank factors entirely offline from pretrained weights and lightweight activation statistics gathered from only a few compressed calibration images. By weighting the decomposition with channel-wise activation magnitudes, our ASVD assigns larger penalties to errors on more active channels, requiring neither retraining nor online calibration and leaving the restoration pipeline intact. When instantiated on PromptCIR at rank 64, ASVD consistently improves PSNR-B over TSVD across four standard benchmarks under identical parameter and MAC budgets. At this operating point, the factorized model cuts parameters by 59% (34.75M to 14.34M) and computation by 16.1% (258.79 to 217.16 GMACs for a 256 x 256 input), enabling acceleration without retraining.

---


### 207. [CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents](https://arxiv.org/abs/2610.29965)

**<font color=#1a73e8>作者：</font>** Wenhao Yu, Zhengcheng Wang, Jiahong Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint reinforcement learning and self-distillation combines task rewards with dense teacher guidance for agent training, but their gradients can partly cancel. A mixing coefficient controls relative scale without selectively removing opposing components. We present CORD, a general framework for conflict-aware optimization of two objectives. CORD separates the choice of protected objective from the condition that triggers projection, and combines the gradients once per optimizer mini-batch. A nearest-point formulation yields a closed-form update and characterizes its first-order effect on the protected objective before optimizer transformations. Gradient diagnostics connect conflict in agent training to lost local optimization progress and motivate selective correction. As a gradient-combination mechanism, CORD can be added to different joint training recipes while retaining their objectives. Across three such recipes, it improves ALFWorld success by 1.5-15.9 percentage points. On WebShop, it improves two of the three pairs, with SDAR rising from 60.7% to 64.6% success. Our analyses explain why protection direction and projection gate must be chosen together, and why the distillation objective and its mixing weight remain consequential after projection.

---


### 208. [Free-XOR TFHE via Lazy Bootstrapping](https://arxiv.org/abs/2610.29983)

**<font color=#1a73e8>作者：</font>** Ali Ajorian, Osman Biçer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gate bootstrapping (GB) is a widely used technique in FHEW-like fully homomorphic encryption schemes, such as TFHE, for evaluating Boolean gates while simultaneously reducing the noise of the resulting ciphertext. However, the computational cost of GB is typically dominated by an expensive blind rotation (BR). \cite{chen2024free} proposed a gate bootstrapping framework in which $\txor$ gates can be evaluated simply by adding the two input ciphertexts, resulting in what they call \textit{free-XOR}. To obtain a functionally complete set of operations, they further designed a GB procedure for evaluating $\tand$ gates using two lightweight blind rotations. In this work, we propose a similar gate bootstrapping framework that supports free evaluation of $\txor$ gates while evaluating \textit{all symmetric binary Boolean gates}, i.e., the 8 gates whose output is identical for the inputs $(0,1)$ and $(1,0)$, using two blind rotations. In addition to providing broader gate support, our construction is substantially simpler than that of \cite{chen2024free}, both conceptually and in terms of implementation.

---


### 209. [GhostFaceMPC: Privacy-Preserving Face Recognition with Multi-Party Computation](https://arxiv.org/abs/2610.29987)

**<font color=#1a73e8>作者：</font>** Davide Carnemolla, Dario Catalano, Mario Di Raimondo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Facial recognition has become central to modern authentication systems, security frameworks, and personalized services. However, its widespread adoption is hindered by severe privacy risks, particularly surrounding unauthorized access to sensitive biometric data. To address these challenges, this paper presents GhostFaceMPC, the first end-to-end, privacy-preserving face recognition system to evaluate a deep convolutional neural network extractor and matching under secure multi-party computation. GhostFaceMPC enables secure processing of facial data across all stages of a face recognition process, from feature extraction and storage to matching, without exposing raw images or biometric embeddings at any stage. We introduce a multi-party computation-friendly quantization of the GhostFaceNet model and circuit optimizations that make face recognition under multi-party computation practical. The code is available at this https URL.

---


### 210. [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989)

**<font color=#1a73e8>作者：</font>** Ruopeng Gao, Yukun Huang, Jiarui Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, reducing the pressure to model visual evolution. We introduce Future Chunk Prediction (FCP), an auxiliary objective jointly optimized with teacher-forced denoising that predicts temporally separated chunks without access to the intervening visual context. Drawing supervision directly from training videos, FCP requires no additional pretrained visual encoder and leaves autoregressive inference unchanged. Our method achieves superior physical plausibility over standard teacher-forced autoregressive training with a lower overall training compute budget, highlighting the effectiveness and efficiency of future-chunk supervision for modeling visual evolution. Intriguingly, our visualizations suggest that FCP fosters a more structured representation space, which may be valuable for building autoregressive world models.

---


### 211. [SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning](https://arxiv.org/abs/2610.29992)

**<font color=#1a73e8>作者：</font>** Jingbo Wang, Kegeng Tang, Zihao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery from nonlinear multivariate time series is challenging in high-dimensional systems, where the number of candidate directed relations grows quadratically with the number of variables. Existing methods are often limited by target-wise model fitting, repeated conditional testing, or expensive graph-search procedures. We propose SCDM, a shared-parameter meta-learning framework for scalable temporal causal discovery. SCDM treats each target variable as a task while learning a shared temporal predictor and a shared causal-strength matrix across tasks. Each meta-episode updates only a subset of target-variable tasks, allowing the model to accumulate structural evidence across the full system without exhaustive target-wise optimization. After training, a post-training graph readout converts the learned predictor into continuous directed causal scores for threshold-independent evaluation. We also provide a finite-error recovery principle showing that, under fully observed delayed-system assumptions and a positive risk-gap condition, thresholding SCDM scores recovers the graph when statistical, meta-optimization, and readout errors are below the population margin. Experiments on controlled synthetic, neuroimaging-inspired, high-dimensional, and real-world temporal benchmarks demonstrate competitive causal recovery and improved scalability in large temporal systems.

---


### 212. [Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](https://arxiv.org/abs/2610.29995)

**<font color=#1a73e8>作者：</font>** Jielong Tang, Ling-An Zeng, Xujie Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas pixel-preserving memories retain raw observations but struggle to reliably associate diverse observations with persistent entity identities and track their evolving states. To address these limitations, we propose MHG-Mem, a multimodal hypergraph memory that jointly organizes entity identity, state evolution, and provenance to visual evidence. Specifically, MHG-Mem represents distinct entity mentions and their observed facts as individual nodes, grouping identity-consistent mentions and facts through occurrence hyperedges. It then synthesizes aspect-specific evolution states from these grouped observations and links them to supporting entities, facts, and source evidence through evolutionary and evidential hyperedges. To navigate this structured memory, we introduce hypergraph-based agentic search, which adaptively selects an entry layer, traverses typed hyperedges across memory levels, and inspects source observations when fine-grained verification is required. These designs support both detailed visual verification and reasoning over cross-session state changes. Extensive experiments across three benchmarks demonstrate the effectiveness of MHG-Mem, improving performance by 8.20-9.98% over the strongest baseline.

---


### 213. [Building Auditable AI Text Detectors with Sparse Autoencoders](https://arxiv.org/abs/2610.30006)

**<font color=#1a73e8>作者：</font>** Liam Dugan, Callum McDougall, Matthew Denton 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-generated text detectors are increasingly deployed in consequential settings---peer review, education, admissions, journalism, and content moderation---where their outputs directly affect individuals. Yet the strongest detectors are fine-tuned neural classifiers whose decisions are opaque, while transparent alternatives (stylometric and linguistic-feature classifiers) underperform them by wide margins. We present a pipeline that converts a fine-tuned neural detector into a classifier that operates on human-readable concepts. We accomplish this by training sparse autoencoders (SAEs) directly on a detector's residual stream, assigning auto-interpretation labels to each SAE feature, and retaining only features whose generated descriptions pass a global fidelity threshold. We then train a lightweight classifier on just the interpretable features. We find that our SAEs recover latent concepts that correspond to highly specific and predictive linguistic "tells" of AI-generated text. Classifiers built on these extracted features are not only highly interpretable but exhibit stronger performance on out-of-distribution texts than either neural or stylometric alternatives.

---


### 214. [Multiclass Boundary Refinement with Neural Cellular Automata for Remote Sensing Land Cover Segmentation](https://arxiv.org/abs/2610.30007)

**<font color=#1a73e8>作者：</font>** Pascoassis Souza Santos Meira, Gilson Antonio Giraldi, Rafael Duarte Coelho dos Santos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of remote sensing imagery often places class boundaries a few pixels away from where they truly lie, and this position error is concentrated in the thin band measured by Boundary IoU (BIoU). We treat boundary refinement as the iterated application of a small learned local rule: the Boundary Refinement Neural Cellular Automaton (BRNCA), that starts from the class probabilities of a frozen, pre-trained segmenter and corrects them cell by cell. We generalise the binary rNCA to the multiclass case by keeping the visible channels on the probability simplex through an Aitchison (log-space) update and by adding free hidden channels. The best configuration improves the mean BIoU over the base segmenter by 2.36 points (from 46.63 to 48.99). The gain is concentrated on the irregular woodland class (+8.5 points BIoU); this suggests that position error is correlated with the fractal dimension of the class boundaries.

---


### 215. [ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013)

**<font color=#1a73e8>作者：</font>** Jian Xu, Yi Li, Ying Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language 3D Gaussian Splatting enables open-vocabulary scene understanding by associating Gaussian primitives with language features. These semantic attributes increase model storage, while most existing 3DGS compression methods are designed mainly to preserve RGB rendering quality. One straightforward approach is to apply sparsification and quantization sequentially. However, pruning based only on rendering quality can remove Gaussians that have small RGB contributions but are important for semantic prediction. Once removed, their semantic information cannot be recovered by later quantization. We propose ClunoGS, a compact framework for Language 3DGS that combines semantics-aware Gaussian sparsification and vector quantization in a unified constrained objective. Semantic supervision is used during sparsification, and the objective jointly considers rendering quality, semantic accuracy, and compactness. We optimize the unified objective with alternating primal, sparsification, quantization, and dual updates. We evaluate ClunoGS on open-vocabulary localization and segmentation using the LERF and ScanNet-10 benchmarks. Under aggressive compression, our unified, semantics-aware formulation substantially alleviates the degradation of semantic representations caused by sequential compression and semantics-agnostic Gaussian sparsification. Ablations further show that jointly coordinating sparsification and quantization better preserves semantic accuracy than applying them independently.

---


### 216. [GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms](https://arxiv.org/abs/2610.30017)

**<font color=#1a73e8>作者：</font>** Meihong Jia, Yasemin Timar, Jonathan Taws  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study introduces GuideEvolve, a self-evolving agent framework incorporating expert guidance and three autonomous regulatory mechanisms, collectively termed the 3Ts: Think Fast and Slow, Throwback, and Termination by choice. The framework addresses critical limitations in extant self-evolving agent paradigms through dual innovations: (1) a task-specific expert-evaluation-driven evolutionary pipeline, and (2) the integration of 3Ts mechanisms to facilitate cognitive optimization, performance recovery via temporal rollback, and adaptive termination protocols. Empirical validation across the MGSM and MMLU benchmarks demonstrates that GuideEvolve attains performance metrics comparable to current state-of-the-art models (89.8% accuracy versus Gödel Agent's 90.6% on MGSM; 89.1% versus 87.9% on MMLU), while exhibiting notably reduced variance (25-59%) and enhanced robustness. Furthermore, the framework achieves a 100% evolution success rate, superior to the baseline's 82%, diminishes required optimization iterations by approximately 50% (from 30 iterations in baseline to 15.1 and 13.4 across tasks), and provides improved stability for production deployment.

---


### 217. [ExGrad: Beyond Suppression - Explicit Clean-Gradient Subtraction in Adversarial Training](https://arxiv.org/abs/2610.30018)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ye, Xiangyu Zhou, Ji Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial training derives updates from surrogate losses, but source-loss descent does not directly characterize an update's effect on adversarial margins. We introduce ExGrad (extrapolative gradient recomposition), which constructs clean-input, adversarial-input, and adversarial-weight-perturbed (AWP) gradients. Virtual steps measure their margin responses, and a globally solvable three-variable problem selects coefficients over a bounded affine domain without nonnegativity constraints. Across affine radii on CIFAR-10, negative clean coefficients rapidly predominate and increase in magnitude with the radius. Cross-zero interventions show that setting the clean coefficient to zero is insufficient: mild subtraction improves PGD-20, while stronger subtraction trades clean accuracy for further PGD-20 gains. In CIFAR-10 WRN-28-4 controls, none of the three candidate-removal variants matches full ExGrad. Projection diagnostics show that negative clean coefficients usually coexist with positive net clean-axis projections, although both decrease as the radius grows. Norm-matched controls indicate that update magnitude alone does not explain the moderate-radius gains. Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show radius-dependent improvements over AWP. On CIFAR-100, ExGrad at $R=0.8$ improves all five reported metrics, including clean and AutoAttack accuracy by 3.84 and 1.75 percentage points. On ImageNet-100, the same radius improves all four robust metrics over both AWP and PGD-AT. These results identify clean-gradient subtraction as a response-revealed update preference whose strength and clean-robust operating point are controlled by the affine radius.

---


### 218. [RealMe: Immersive Volumetric Video from Minimal Captures](https://arxiv.org/abs/2610.30023)

**<font color=#1a73e8>作者：</font>** Chenxu Zhou, Zhiyuan Yu, Yudong Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of creating immersive volumetric videos from sparse and low-resolution capture resources. Conventional dense multi-view reconstruction methods can produce high-quality volumetric videos, but their reliance on costly capture setups makes them impractical in real-world scenarios. Recent approaches use generative models to relax capture requirements, but still suffer from limited resolution and 4D inconsistency. To overcome these constraints, we propose RealMe, a unified framework built around a high-resolution video diffusion model that enhances limited captures into high-resolution (2K), 4D-consistent videos for volumetric video reconstruction. Specifically, RealMe constructs auxiliary data from capture videos and encodes them into latents along with layout-aware positional embeddings. The video diffusion model adapts factorized spatio-temporal attention to the multi-view capture layout, denoises these latents across viewpoints and time, and decodes them into enhanced videos to refine the 4D representation. This adaptation helps the model capture temporal dynamics and multi-view relationships, leading to more 4D-consistent generation. To reduce the data gap between generated videos and real captures, we apply a latent frequency loss that provides frequency-domain supervision in latent space. Extensive experiments on the public DNA-Rendering benchmark and our self-captured RealVV dataset demonstrate that RealMe is able to create immersive volumetric videos and outperforms state-of-the-art methods in visual fidelity and 4D consistency.

---


### 219. [Measurement-Guided Conversion of Laboratory Eye-Tracking Data for VR Authentication](https://arxiv.org/abs/2610.30032)

**<font color=#1a73e8>作者：</font>** Md Arif Shahriar, Mehedi Hasan Raju, Oleg V. Komogortsev  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Eye-movement authentication in virtual reality (VR) needs longitudinal training data, yet most such datasets come from lab trackers. We convert lab recordings to a VR headset's signal quality while keeping their eye movement, using only unpaired VR recordings of other people. Measurements show that the headset's added noise dominates above 7.8 Hz and that its quality is consistent within a person. A parametric device model re-creates the headset's sampling, a person-consistent calibration error and spectrally shaped noise, and a frequency-locked diffusion renderer re-textures that high-frequency noise. Converted GazeBase recordings match GazeBaseVR in noise level and accuracy, keep their source's saccade dynamics, and are harder to tell from real VR data than two prior conversions. An authenticator trained only on converted data verifies unseen VR users at a 5.9% equal error rate with 45 s of gaze, close to real VR training (5.8%); with 5 s, a gap remains.

---


### 220. [Attn-Forcing: Learning Full-Context Attention Proxies for Streaming Video Generation](https://arxiv.org/abs/2610.30036)

**<font color=#1a73e8>作者：</font>** Junyao Gao, Sibo Liu, Jiaxing Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Increasing the attention context length significantly improves streaming video generation quality, while incurring prohibitive memory and computational costs as the context grows. Existing methods attempt to capture this contextual information through attention selection or compression, but remain limited by bounded representations and lack explicit attention-level supervision to retain historical contributions to current queries. To address this, we introduce Attn-Forcing, a novel framework that preserves full-context attention contributions for streaming video generation under bounded memory and computation. We achieve this by introducing attention proxies that continuously approximate the attention responses induced by the historical context. Specifically, we implement the proxies as learnable visual latents and employ a Proxy Update Module to incorporate visual context from historical latents. Moreover, we propose an Attention Matching Loss to explicitly constrain the attention behavior of the learned proxies using full-context attention supervision. Extensive qualitative and quantitative experiments demonstrate that Attn-Forcing consistently improves streaming video generation quality and achieves state-of-the-art performance over existing baseline methods.

---


### 221. [Which Differences Matter? Controlled Tests of Rule Transfer, Joint Reliability, and Information Use in Decision Models](https://arxiv.org/abs/2610.30045)

**<font color=#1a73e8>作者：</font>** Tianyou Lai, Wentao Yue, Zhiwei Zuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models map stated rules and observed states to discrete answers. Aggregate accuracy leaves unresolved which rule and information changes guide those answers. We connect controlled input changes to transfer, joint reliability, and directed information use through executable arithmetic rules. Semantic rule separation and crossed rule and state tests make transfer and joint success separately measurable. We compare equivalent wordings, calibrate joint correctness through marginal-preserving reassociation, and alter tables to define alternative answer targets. Adaptation gains increase with nearest-source answer agreement; fully conflicting quartets yield small pooled gains and different gain signs across source splits. Equivalent rewrites have opposing task-level effects, linking transfer gains to rule presentation. Joint-score departures depend on which rule and state associations the reference preserves. A decision service changes answers more across equivalent wordings than across identical-text repeats and usually follows the answer targets implied by altered table values or mappings.

---


### 222. [Parallel AI Agent Collaboration as Graph-Structured Distributed Block Optimization](https://arxiv.org/abs/2610.30074)

**<font color=#1a73e8>作者：</font>** Hanmin Li, Yury Demidovich, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Parallel AI agents can produce useful local edits yet degrade a shared solution when their edits are combined. We model this coordination problem as discrete block optimization with an exactly evaluable objective and a known dependency graph. Independent sets certify compatible edits whose verified gains, measured against the same current solution, add exactly. A coordinator constructs a safe compatible candidate and can also evaluate interacting edits to capture favorable interactions. We prove that an optimal fractional coloring yields a merger that preserves a $1/\chi_f(G)$ fraction of the total verified local improvement, where $\chi_f(G)$ is the graph's fractional chromatic number. This guarantee is tight among mergers that select a subset of the same proposals. Under conditional local-improvement guarantees and a block error-bound condition, repeated collaboration converges geometrically in the objective gap. The rate separates task structure, agent allocation, and computation cost, yielding a linear program for agent assignment and an explicit time-cost trade-off. Code-repair experiments show that verified merging resolves conflicts between individually useful edits that cause naive merging to fail. On larger conflict-free tasks, parallel agents reduce modeled completion time at higher input-token-equivalent cost. On three public road networks, fractional integration retains 922 units of verified graph-cut improvement across 90 paired runs. For route-search agents sharing exclusive access to vehicle routes, fractional scheduling reduces measured wall time by a median of 15% across twelve paired runs, with route-cost changes varying across runs.

---


### 223. [From Classifier Heads to Encoder Prototypes: Personalized Federated Learning with Head-Derived Clustering](https://arxiv.org/abs/2610.30075)

**<font color=#1a73e8>作者：</font>** Amirardalan Dehghanpour, Arian Noori, Ehsan Tanghatari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning must decide which clients should share representations. We introduce HDC-FL (Head-Derived Clustering for Personalized Federated Learning), which reads that decision off a signal shared-encoder training already produces: the client-specific classifi- er heads. At periodic refresh rounds the server projects the cached heads into a normalized low-rank descriptor space, groups the descriptors, builds one encoder prototype per group from the cached client encoders, and returns to each client a soft mixture of those prototypes paired with its own unchanged head. Client-specific heads are never averaged or distributed to oth- er clients; the shared-encoder trajectory is left intact; and no second optimization trajectory, additional local objective, or post-training fine-tuning stage is required. Across 11 CIFAR-10 and CIFAR-100 configurations covering label-subset, Dirichlet and rotation heterogeneity with ResNet-18 and MobileNetV2 encoders, HDC-FL is competitive with the strongest personalized and clustered baselines in macro-averaged mean accuracy and attains the numerically highest macro-averaged worst-client and bottom-20% accuracy among the evaluated methods. The tail results distinguish methods that look similar when only their means are compared. A controlled donor-swap diagnostic further finds positive donor-ranking associations between head similarity and encoder compatibility in all three settings tested, most clearly under covariate shift.

---


### 224. [Orbitol: Crystal Generation on Wyckoff Orbits](https://arxiv.org/abs/2610.30086)

**<font color=#1a73e8>作者：</font>** Ivan Žugec, Joshua Rosenthal, Ivor Lončarić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models propose crystalline materials by learning composition and geometry, but unconditional sampling gives no direct control over the space group, which constrains whether responses such as piezoelectricity are symmetry-allowed. We present Orbitol, a crystal generator built on the Crystalite diffusion Transformer that replaces atom tokens with Wyckoff-orbit tokens. Given a space group and a collection of occupied Wyckoff positions, Orbitol generates the atom type and free coordinates of each orbit together with a compatible lattice, so every valid structure is invariant under the operations of the requested group. It generates structures two to three orders of magnitude faster than the symmetry-aware baselines at the evaluated settings. On MP-20, 13.8% of Orbitol's attempts yielded stable or metastable, unique and novel structures that retained the requested space group after relaxation, compared with 10.8% for SGFM, the next best model. We also introduce SPARC, a score that combines retention of the raw detected space group with agreement between the retained-group and training distributions. Finally, we used Orbitol to generate candidates in piezoelectric crystal classes. Of the structures selected by internal screening, 89% passed our density functional theory checks, and 79% also matched no Materials Project or Alexandria entry with the same space group. Their median figure of merit was nine times that of the piezoelectric materials computed in the Materials Project, and 24% of the new candidates ranked in that set's top 10%.

---


### 225. [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089)

**<font color=#1a73e8>作者：</font>** Ruotong Liao, Meikel Kokowski, Xiaoxiao Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Today's multimodal assistants are typically prompted to interpret the visual evidence presented to them. To offload the cognitive burden of remembering across long horizons, wearable assistants should instead proactively acquire and maintain useful memory as the user's surroundings evolve. Doing so on the user's behalf requires identifying what matters, understanding the scene in real time, and initiating memory maintenance in the background while the user stays focused on their activities. We introduce ProactEgoMem, a benchmark that evaluates proactive memory in streaming egocentric video. Three tasks ground the evaluation in ambient environmental needs: Information Capture (IC) preserves transient yet dense visual information, State Tracking (ST) follows changing object states, and Location Tracking (LT) records object movements. The benchmark defines its protocol at two levels of proactiveness: the Notification Level asks for a single timely notification that satisfies the user's intent, while the deeper Intervention Level asks the agent to maintain memory on the user's behalf through an active start-to-stop tool lifecycle. Parallel ProactEgoMem-Daily and ProactEgoMem-Sci tracks contain 300/100 clips covering daily and scientific use cases, paired with 1000/500 questions in ProactEgoMem-QA, which measures the quality of the proactively acquired memory. Across proprietary, open-source, video-language, and streaming baselines, even the strongest models fail to capture memory both timely and accurately. ProactEgoMem provides a rigorous evaluation foundation for proactive multimodal assistance and for video agents that co-exist with their users.

---


### 226. [VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift](https://arxiv.org/abs/2610.30090)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Perimeter triage faces a latency/semantics trade-off: signature engines are fast and format-safe but blind to unseen attacks, while generative models are semantic but slow and produce unparseable output. In late 2026 a class of commercial System One decision models (TypeSafe Jev; Microsoft-Decision-1) began selling typed decision primitives - binary gates, closed-set choices, ordinal scores - as product APIs, with no academic treatment. We present VX-One: a small multi-head network (100K-10M parameters) whose outputs are these primitives - a calibrated gate, a choice over a closed candidate set that always includes an explicit unknown option, and an ordinal score, trained multi-task, temperature-calibrated per head (~0.7-1.7 ms p50 on CPU). We evaluate it on UNSW-NB15, CIC-IDS2017, EMBER2024 against calibrated XGBoost, Random-Forest, MLP, Kitsune, and measure a two-phase cascade (Suricata with 52,674 Emerging-Threats rules -> VX-One) over five days of CIC-IDS2017. Findings: (i) VX-One wins detection (AUROC/FPR@95%TPR) on UNSW-NB15 and under temporal drift on CIC-IDS2017 (0.711 vs 0.637), but XGBoost wins multi-class attribution on all three benchmarks; (ii) leave-one-family-out gate detects never-seen families on 9/9 UNSW folds yet drops below chance on CIC recon family, and abstention threshold transfers poorly across benchmarks; (iii) on payload-less reconstructions signature engines resolve ~0.1% of flows - gray zone ~99.9% of traffic, recovered by Phase 2 (combined recall >=0.978); (iv) calibration collapses under temporal drift (ECE 0.04->0.40) for every method while ranking partially survives. We provide a measured account of where typed calibrated decisions help perimeter triage, and where they fail.

---


### 227. [BatchBench: Benchmarking AI Robustness to Batch Effects and Domain Shift in Biomedical Images - A JUMP Cell Painting Leaderboard](https://arxiv.org/abs/2610.30104)

**<font color=#1a73e8>作者：</font>** Sonja Topf, Ana Sanchez-Fernandez, Günter Klambauer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, current AI systems remain highly susceptible to domain shifts, particularly in biomedical imaging, where images are usually acquired under substantially different experimental conditions. Although recent domain adaptation methods have made substantial progress, significant performance gaps under domain shift persist. To measure progress in this regard, we introduce BatchBench, a leaderboard that evaluates and compares the robustness of AI systems on biomedical images from unseen experimental batches and data sources. BatchBench is built on JUMP-CP, one of the largest publicly available biomedical imaging datasets. Generated using the Cell Painting assay, JUMP-CP exhibits pronounced batch effects and domain shifts, making it a challenging testbed for evaluating robustness to distributional changes.

---


### 228. [Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching](https://arxiv.org/abs/2610.30107)

**<font color=#1a73e8>作者：</font>** Yunpeng Mei, Xiaowen Zhu, Chenyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching trains a continuum of velocity regression problems but usually reports a loss averaged over interpolation time, obscuring which regions are limited by intrinsic ambiguity and which remain data-limited. We introduce the Velocity Ambiguity Profile (VAP), $\mathcal{A}_v(t)$, the time-local Bayes-risk floor of velocity prediction, and decompose time-resolved loss as $L_N(t)=\mathcal{A}_v(t)+R(t;N)$, where only the excess term $R(t;N)$ is reducible by more data or a different estimator. For $N$ training samples and a $K$-component mixture in the structured example, we prove two statistical benchmarks. In an intrinsic local-regression benchmark, $\mathcal{A}_v(t)$ enters the time-dependent noise factor of the standard nonparametric rate. In separated isotropic Gaussian mixtures, the Bayes velocity becomes locally affine, and a label-oracle residual-regression benchmark has parametric excess-risk scale $K\mathcal{A}_v(t)/N$, matched within the same separated residual Gaussian-location subproblem. Controlled Gaussian-mixture experiments validate this diagnostic through a dense transition sweep, calibrated oracle-to-blind and empirical-proxy audits, and a local controlled time-sampler stress test in which a frozen reducible-error proxy reduces reducible loss while cross-cell sensitivity delimits aggressive sampling. On CIFAR-100 DINOv2 feature flow, guided time sampling reduces uniformly evaluated velocity loss by $6.78\%$ and global feature Fréchet distance (FD) by $23.6\%$, while class-conditional kernel inception distance (KID) shows no improvement. VAP turns an averaged flow-matching objective into a time-resolved diagnostic for locating ambiguity-limited and data-limited regions.

---


### 229. [The role of locality and weight sharing in convolutional neural networks](https://arxiv.org/abs/2610.30118)

**<font color=#1a73e8>作者：</font>** Francesco Mori, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatial correlations of natural images, remain poorly understood. We address these questions in a teacher-student model with a convolutional teacher acting on $P$ input positions with correlation $c$ between positions. We compare convolutional and locally connected students trained by online stochastic gradient descent, and derive ordinary differential equations that describe their dynamics exactly in the limit of large feature dimension $D$. For uncorrelated positions ($c = 0$), the two students follow the same learning trajectory, with the convolutional student learning exactly $P$ times faster. We also find that locality affects the sample complexity: a student that matches the kernel size of the teacher recovers it from $\mathcal{O}_{D}(D)$ samples, whereas $\mathcal{O}_{D}(D\log(D))$ samples are needed with a larger kernel. For $c > 0$, spatial correlations can reduce the advantage of weight sharing. The asymptotic error of the convolutional student grows with $c$, whereas that of the locally connected student is independent of $c$ and overall lower when evaluated at the same learning rate. When the learning rate is instead tuned to the training horizon, however, the locally connected student wins at early times and the convolutional student at late times, with a transition that we predict analytically.

---


### 230. [Self-normalized Bernstein Inequalities for Regenerative Processes and Applications to Learning Without Independence](https://arxiv.org/abs/2610.30119)

**<font color=#1a73e8>作者：</font>** Imon Banerjee, Pierre Alquier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove a self-normalized Bernstein inequality for bounded functions of a regenerative process with independent, identically distributed marked cycles of finite mean length. The bound uses observed cycle lengths and retains explicit terms for truncation and the cycle ending after the observation horizon. Selecting a tuning parameter from a finite deterministic collection gives a version of Bernstein inequality where all terms are empirical but one, related to the tails of the regeneration times. We then study this term in many regimes: it turns out that it is of second-order in many cases of interest. This is important for applications in machine learning: we prove generalization error bounds for classification with non-i.i.d., regenerative data. These bounds can be used to define learning objectives: by minimizing the first-order term only in the bound, we define agnostic classifiers that still satisfy oracle inequalities. We also show that the bound on the average deviation provided by our results is minimax-optimal in the sample size and in the expected regeneration time. Finally, we combine the Bernstein inequality with a regenerative strong approximation to obtain a Gaussian approximation using an observable block variance estimator.

---


### 231. [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120)

**<font color=#1a73e8>作者：</font>** Yanqing Liu, Letian Zhang, Chengzhi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment, and pixel reconstruction, so that a single representation can support prediction, instruction, and inspection. However, existing encoders typically specialize in only one or two of these capabilities; we therefore introduce ALPS, a pretrained visual state encoder that unifies all three in a single set of patch tokens. Using only still images and text, we pretrain a ViT-B/16 from scratch with language, reconstruction, and spatial correspondence objectives, and then refine it via cross-view self-distillation. In a unified evaluation across fifteen public encoders, ALPS achieves the lowest aggregate LIBERO state-probe error among ViT-B models (matching the 3.5x larger V-JEPA 2-L) while maintaining strong language alignment and accurate pixel reconstruction. Downstream, frozen ALPS tokens reach the highest mean policy success on LIBERO (85.5%) when paired with our native text tower, match or exceed leading encoders on world-model planning across PushT, Wall, and Granular, and allow predicted future tokens to be decoded directly into pixels for visual inspection. We hope this work helps establish visual pretraining as a shared foundation for understanding, prediction, and action in world models.

---


### 232. [Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129)

**<font color=#1a73e8>作者：</font>** Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models predict future frames from past frames and actions. They serve as simulators in which agents train, plan or are evaluated, and that humans can control interactively. They generate in the latent space of a video autoencoder, whose compression sets their cost per frame and how long each action waits to take effect. Yet world models often reuse the autoencoders of text-to-video generators, built for offline generation with no agent waiting and, without their training data and code, not retrainable at another compression. We therefore ask how, where and how much a world model should compress. We build CADRE, an open family of causal diffusion representation autoencoders spanning multiple spatio-temporal compressions. Its members differ only in a small bottleneck on frozen features and share a diffusion decoder self-distilled to one or a few steps. We train the same world model on each autoencoder in two domains, manipulation and navigation, with two environments each. CADRE forms most of the latency-quality frontier, especially with a moving camera. Our study also leads to four findings. At strong compression, a diffusion decoder is sharper than perceptual regression. In robot manipulation, temporal compression is more effective in the autoencoder than in the world model. Manipulation and navigation call for opposite compressions: temporal compression costs little when the camera is still, and spatial compression when it moves. Surprisingly, with a still camera, coarser spatial tokens hurt motion far more than image quality. Code, models and a live demo are at this https URL

---


> [!TIP]
> 当前位于：**201-232**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-232**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
