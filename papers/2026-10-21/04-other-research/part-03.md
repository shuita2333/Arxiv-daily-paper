# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 101. [Revisiting Smoothed Online Learning: Competitive Ratio, Dynamic Regret with Switching Cost, and Best of Both Worlds](https://arxiv.org/abs/2610.24370)

**<font color=#1a73e8>作者：</font>** Lijun Zhang, Linzhe He, Wei Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit smoothed online learning and develop algorithms with improved competitive ratios, optimal dynamic regret with switching cost, and best-of-both-worlds guarantees. Surprisingly, minimizing the hitting cost alone is $\max(1,\frac{2}{\alpha})$-competitive for $\alpha$-polyhedral functions under the $\ell_2$-norm switching cost and $1+\frac{4}{\lambda}$-competitive for $\lambda$-quadratic growth functions under the squared $\ell_2$-norm switching cost, significantly improving existing guarantees. The polyhedral bound is tight for this naive algorithm, and we establish a matching lower bound for $\alpha\geq1$. For convex $\lambda$-quadratic growth hitting costs, minimizing a suitably weighted sum of hitting and squared $\ell_2$-norm switching costs yields a competitive ratio of $1+\frac{2}{\sqrt{\lambda}}$. For dynamic regret with the $\ell_2$-norm switching cost, we develop Smoothed Ader (SAder), which achieves the optimal $O(\sqrt{T(1+P_T)})$ rate in the standard online convex optimization setting, where $P_T$ is the comparator's path-length. Its lookahead version removes the bounded-gradient assumption, and a matching lower bound establishes optimality in this setting. Finally, for convex hitting costs on a bounded convex domain, we develop UDNP to aggregate any two experts in the lookahead setting under both switching costs. Its additional cumulative cost is at most $O(1)$ relative to the first expert and $O(\sqrt{T\log T})$ relative to the second, yielding best-of-both-worlds guarantees without bounded gradients.

---


### 102. [Beyond Next-Screen Prediction: The Decision Value of GUI World Models](https://arxiv.org/abs/2610.24372)

**<font color=#1a73e8>作者：</font>** Sizhe Tang, Hanhan Zhou, Jeffrey Svajlenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI world models are increasingly used to improve action selection by predicting the consequences of candidate actions, but it is unclear how much of the resulting gain comes from prediction itself rather than from the evaluator that interprets those predictions. We study this attribution problem through controlled interventions on GUI action selection. With candidates and predictions held fixed, lookahead gains can change with how the prediction is presented to the evaluator, so end-to-end gains cannot be attributed to prediction alone. We then introduce Direct Action Ranking (DAR), which learns from reference actions to score candidates without generating future screens, and compare it with a prediction-augmented variant under matched supervision. Predicted successors add no detectable ranking signal once evaluation is learned directly. Without retraining, DAR improves AndroidWorld task success by 5.8--16.4 points across three proposers, outperforms world-model lookahead, and transfers zero-shot to unseen apps, where every prediction-conditioned configuration falls below proposer confidence. These results suggest that GUI world models should be evaluated by their decision value, the incremental action-selection value of their predictions beyond a strong direct evaluator, rather than by prediction fidelity or end-to-end lookahead gain alone.

---


### 103. [Learning from the Right Regions: Class-Conditioned Explanation Guidance for Medical Imaging](https://arxiv.org/abs/2610.24381)

**<font color=#1a73e8>作者：</font>** Zubair Faruqui, Rahul Dubey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks can achieve strong predictive performance in medical imaging while relying on regions unrelated to the predicted finding. Explanation-guided learning can address this problem, but multi-label classification introduces a key challenge: multiple abnormalities may coexist in an image, requiring each prediction to align with its corresponding spatial evidence. We propose a class-conditioned explanation-guided learning framework that constructs a separate explanation for each positive class and penalizes evidence outside its class-specific annotated regions. We instantiate the framework using Gradient-weighted Class Activation Mapping (Grad-CAM) and evaluate it on 14 abnormalities using EfficientNet-B1, ViT-B/16, ViT-B/32, and Swin-B. Explanation guidance substantially improves annotation alignment across all architectures: All-Saliency Precision increases from 0.140 to 0.625, 0.052 to 0.551, 0.060 to 0.403, and 0.095 to 0.570, respectively. These improvements are accompanied by smaller, architecture-dependent changes in classification performance. Our results show that class-conditioned explanation guidance can substantially improve where multi-label classifiers concentrate their explanatory evidence while largely preserving predictive performance.

---


### 104. [Is This Your Agent? Identity Watermarking for Agent Systems in Dynamic Environments](https://arxiv.org/abs/2610.24382)

**<font color=#1a73e8>作者：</font>** Yuwei Zhong, Yu Cheng, Jiuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent systems deployed in dynamic environments continuously update their memories, skills, and runtime configurations, leading to evolving trajectories and challenges for persistent identity authentication. Existing text and agent watermarking methods struggle to achieve stable watermark embedding under dynamic environments, while embedded watermarks may become difficult to recover due to environmental changes. This paper proposes DASMark, an identity watermarking framework for dynamic agent systems. DASMark introduces Action-Preserving Embedding (APE), which learns semantically similar but distinguishable decision-expression channels from diverse interaction trajectories to enable stable watermark embedding in dynamic systems. It further introduces Shift-Robust Recovery (SRR) to mitigate context-induced shifts and improve watermark recovery stability under dynamic environments. In dynamic settings, DASMark achieves 98.5% bit-decoding accuracy and maintains 95.2% accuracy under attack scenarios, while preserving task utility comparable to unwatermarked agents.

---


### 105. [From Neglect to Resignation: Understanding the Evolution of Mobile Privacy](https://arxiv.org/abs/2610.24389)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Ziqi Liu, Lionel Z. Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This decade-long longitudinal qualitative study follows 31 smartphone users in China across four interview waves (2014-2023) to examine how mobile privacy understanding evolves alongside shifting computing infrastructures. Findings reveal three stages shaped by distinct interactional mechanisms: early functional acceptance of permission-based data access, growing vigilance triggered by behavioral tracking feedback loops, and eventual resignation as AI-driven inference made ecosystem-level profiling feel inescapable. Rather than a stable attitude, digital resignation emerges through cumulative infrastructure exposure, as each new system layer retroactively reinterpreted earlier permissions and exhausted users' capacity for self-management. The study challenges permission-centric design assumptions and proposes inference visibility, context isolation, and automated privacy agency as system-level responses.

---


### 106. [MSCR: Jointly Balancing Utilization Across Modalities and Discovering Synergistic Information](https://arxiv.org/abs/2610.24395)

**<font color=#1a73e8>作者：</font>** Xinyu Chen, Liangjian Wen, Jiang Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multimodal learning, modality imbalance often lets one modality dominate optimization and keeps the model from fully exploiting cross-modal interactions. Balance-oriented methods such as the Multimodal Competition Regularizer (MCR) perform well by alleviating this imbalance during training. These dynamic balancing methods, however, mainly adjust modality contributions and do not consider how imbalance affects the formation of synergistic information during fusion. Synergy is a major source of multimodal advantage, because it is predictive gain that cannot be recovered from unimodal evidence alone. We propose the Multimodal Synergistic Competition Regularizer (MSCR), a fusion method that jointly promotes balanced modality utilization and the discovery of synergistic information. MSCR has two complementary objectives. An anti-dominance objective suppresses excessive unimodal influence and leaves room for synergistic information, and a synergy objective encourages the fused predictor to outperform a non-synergistic unimodal reference. An adaptive gate further concentrates the regularization on samples that need stronger collaborative modeling. Experiments on five benchmarks show that MSCR consistently improves performance over MCR and strengthens synergistic capability. It raises conditional recovery, the accuracy of the fused prediction on samples that the unimodal predictors misclassify, as well as the share of the model's output that InterSHAP attributes to cross-modal interactions. Its gain in conditional recovery persists when the fusion module is Transformer-based. Code is available at this https URL.

---


### 107. [Spatons: Spatiotonally Localized Building Blocks for Efficient XR Predistortion](https://arxiv.org/abs/2610.24400)

**<font color=#1a73e8>作者：</font>** Mohammadjavad Maheronnaghsh, Sushant Kondguli, Steve Mann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Spatons, a family of compositional, spatially localized neural operators for computationally efficient XR (extended reality) predistortion and distortion compensation. XR displays (AR, VR, and MR) suffer from spatial (e.g., geometric) and tonal (e.g., colour) distortions. Frames can be pre-distorted so that the projected image looks as intended. Distortions vary with manufacturing tolerances and projection systems, motivating programmable compensation. Untethered, battery-operated XR systems also require low energy and latency. A Spaton is a hybrid patch-to-pixel block combining tiny Multi-Layer Perceptrons (MLPs) with fixed-function interpolation. Using Spatons, we build programmable, computationally efficient pipelines for varied distortion scenarios. On the full spatiotonal Scenario 5, Sequential-5' matches CompenNet++ in SSIM (0.944 vs. 0.944) and closely matches its PSNR (27.5 vs. 27.7 dB), with substantially lower complexity. We demonstrate a flexible Spaton solution with 6 times fewer FLOPs and 106 times fewer parameters than CompenNet++, and 4-10 times fewer memory transfers than UNet++. We characterize software implementations and analytical hardware estimates, including optimizations across target XR platforms. The distortions considered are drawn mostly from see-through, near-eye displays, where the spatial light path governs local intensity and spectral response. This early systems-level exploration uses closed-form differentiable distortions and one real projector-camera capture set for training and evaluation, rather than through-the-optics measurements. Testing on a wider range of real XR devices remains future work. Chromatic dispersion (color fringes) remains the main artifact where Spatons trail monolithic baselines.

---


### 108. [S3D-Mosaic: Subgradient-Guided Cross-Band Structure Transfer for Spectral Demosaicing](https://arxiv.org/abs/2610.24414)

**<font color=#1a73e8>作者：</font>** Weiqiang Zhao, Xian Li, Yuzhe Gui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral filter array (MSFA) imaging enables snapshot spectral acquisition, but its per-band sparse sampling causes severe spatial aliasing. Although missing spatial structures can be inferred across bands, wavelength-dependent contrast variations make direct cross-band transfer unreliable. Existing model-based methods lack explicit magnitude-invariant mechanisms, and learning-based methods require layout-specific training or per-image tuning, limiting generalization. To address these issues, we propose S3D-Mosaic, a model-based spectral demosaicing method built upon a subgradient-guided cross-band structure transfer framework. We first establish a subgradient-guided regularization framework with a generalized cosine-similarity interpretation, providing a convex mechanism for magnitude-invariant information transfer. Then we design a compact Directional Sparse Equivariant Difference Convolution (DSE-DConv) for band-level extraction of orientation-selective, high-frequency structure features at low computational cost. Instantiating the framework with DSE-DConv on spectrally adjacent bands yields a cross-band self-structure similarity regularizer for spectral demosaicing, which we optimize via a dual-scan ADMM algorithm that decouples the bidirectional dependency while propagating magnitude-robust structural information across bands. With DSE-DConv's two parameters trained once via self-supervision, S3D-Mosaic outperforms state-of-the-art unsupervised methods on CAVE and NTIRE 2022, and generalizes robustly to varying MSFA layouts, pan-mosaic fusion, and real-world UAV data with fixed reconstruction hyperparameters. The source code is available at \url{this https URL}.

---


### 109. [Cross-Dimension and Cross-Modality Relational Tensor Representation Learning for Multimodal Health Data Modeling](https://arxiv.org/abs/2610.24419)

**<font color=#1a73e8>作者：</font>** Jiawei Guo, Meng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal health data integrate information from heterogeneous clinical sources, creating substantial opportunities for data-driven decision support. Realizing these opportunities, however, requires effectively modeling complex dependencies that arise both within individual modalities and across modalities. This paper proposes Relational Tensor Representation (RTR), a unified framework that jointly learns dimension-specific tensor representations and cross-dimensional and cross-modality relationships. RTR introduces learnable relational bridge matrices that maintain relational information while preserving the structural identities of tensor dimensions and modalities. A structured fusion mechanism further integrates factor-level and relationship-level information into compact representations for downstream prediction. Experiments on simulated data and two multimodal neurophysiological datasets, covering emotion recognition and brain activity classification, demonstrate that RTR consistently outperforms representative tensor learning, multimodal fusion, and Transformer-based baselines. These results highlight the value of explicitly modeling cross-dimensional and cross-modality relationships for learning informative representations from heterogeneous multimodal tensor data. The source code is planned for public release to support reproducibility and future research.

---


### 110. [Toward a Universal Local Speech Feature Extractor Through Distillation](https://arxiv.org/abs/2610.24424)

**<font color=#1a73e8>作者：</font>** Jessica Yang, Marcelo Beramendi Caballero, Ju-Chieh Chou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised speech models commonly consist of a set of convolutional neural network (CNN) layers used as a local feature extractor, followed by transformer layers. The CNN layers are computationally demanding, and are also similar across models and resemble the much simpler mel spectral features. We hypothesize that the CNN layers can be replaced by a simple, universal model. To test this hypothesis, we learn a two-layer feature extractor via distillation from one or more teacher models (HuBERT, data2vec, and WavLM). Experiments on SUPERB(-SG) benchmark tasks show that our model largely retains the performance of the teacher models and can also be used in an unseen model (wav2vec 2.0). Our feature extractor requires only 3% of the MACs of the CNNs, resulting in a $>$20% overall inference runtime reduction.

---


### 111. [When Opposite Premises Translate Identically: A Source-Conditioned Diagnostic for Multilingual Commonsense Items](https://arxiv.org/abs/2610.24428)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Rui Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual reasoning comparisons depend on translated premises preserving the relations in their English sources. Automatic translation scores can rank source-target pairs, but an acceptance decision alone cannot certify a counterfactual benchmark field. We test a source-contrast diagnostic for ACCORD premises: reverse the English polarity, translate both arms independently, count identical target outputs, and score each arm against its own source. Across 71 matched question identities at two containing-item depths, five target languages, and three translation checkpoints, Swahili has 63, 113, and 67 exact collisions among 710 pairs per checkpoint. At a human-reference-calibrated threshold, round-trip NLI passes both arms of 3 of the 113 NLLB-3.3B collisions, while LaBSE passes 78. Each collision proves at least one unfaithful translation, but does not identify its arm. These controlled measurements do not establish screening accuracy on spontaneous translation errors or a language-by-hop reasoning effect; the study has no native equivalence labels or answer-model evaluation.

---


### 112. [Transport What Shares the Conduction Pathway: Normal-Anchored SPD Geometric Transport for Source-Free Patient Adaptation of Holter and Patch ECG](https://arxiv.org/abs/2610.24430)

**<font color=#1a73e8>作者：</font>** JinKook Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) beat classifiers lose accuracy on new patients and devices, and source-free adaptation methods that assume class-balanced target batches fail on real recordings, whose label-free prefix is 87.9--98.6% normal beats. We propose Normal-Anchored Geometric Transport (NAGT, GA_NS), which estimates a closed-form symmetric positive-definite congruence map from label-free normal anchors in the first 5 min of each recording and applies it only to the normal and supraventricular prototypes, keeping the ventricular and fusion prototypes fixed. The score offsets and decision rules were set on MIT-BIH only; the rate-invariant RR head (relA) was adopted after the development databases (INCART, SVDB) had been opened; the frozen model was then evaluated once on Icentia11k chest-patch recordings under a pre-registered protocol. In 493 patients (973 recordings, 3,615,388 evaluated beats), NAGT reached an arrhythmia macro-$F_1$ $J = \frac{1}{2}(\text{S-}F_1 + \text{V-}F_1) = 48.7\%$ [95% CI 42.1, 54.7] versus 34.5% without adaptation ($\Delta J = +14.1$ [+8.6, +19.3] pp; 59.8% versus 43.9% in non-AF) and outperformed all five Holm-adjusted comparators, including AdaBN, Tent and T3A. In the 75-patient test subgroup of the historical split (73 analyzed), the gain was not significant (+6.1 [-8.5, +23.4] pp). Adaptation takes a median of 5.8 ms per record without back-propagation.

---


### 113. [BodyBridge: Grounded Body Layers for Sim-to-Real Translation of Vulnerable Road Users](https://arxiv.org/abs/2610.24436)

**<font color=#1a73e8>作者：</font>** Mark Azer, Fabian B. Flohr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simulation-to-real driving video diffusion models can translate photorealistic scenes, but they typically represent pedestrians and cyclists, vulnerable road users (VRUs), as generic object classes. This is insufficient for vulnerable road users whose safety-relevant appearance depends on articulated pose and identity. We present BodyBridge and Grounded Body Layers (GBL), a simulator-derived, pixel-aligned representation that combines scene geometry, canonical per-pixel body correspondence, and exact VRU masks. GBL provides explicit articulation to the video diffusion model, emphasizes VRU regions during control-branch post-training, and supports additive composition with scene-geometry control at inference. It also enables per-joint evaluation of generated VRUs and a failure taxonomy for identity errors. On CARLA-to-real translation, BodyBridge improves near-range PCK@0.5 by 22% over the released depth-conditioned baseline. Replacing normal-map body control with canonical correspondence reduces body flips by 18%, while composition reduces near-range facing flips by 27%. These results show that explicit body grounding complements scene-level control and improves pose-faithful VRU generation. All code, data, and model checkpoints will be made publicly available to support reproducible, pedestrian-aware autonomous driving research.

---


### 114. [Near-Optimal Regret for Semi-Bandit Learning of Monotone Stochastic Problems](https://arxiv.org/abs/2610.24446)

**<font color=#1a73e8>作者：</font>** Zhengjia Zhuo, Viswanath Nagarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the task of learning an (approximately) optimal policy for stochastic optimization problems where the true distributions are unknown. In each period, the algorithm plays a policy for the stochastic problem and observes semi-bandit feedback, i.e., it only receives new samples from the random variables that were selected by the policy. We obtain an algorithm that works for a large class of ``monotone'' stochastic problems, including prophet inequality, Pandora's box, series testing, stochastic knapsack and stochastic matching. We obtain $\tilde{O}(\sqrt{nkT})$ regret for ``weakly'' monotone problems and $\tilde{O}(\sqrt{nT})$ regret for ``strongly'' monotone problems, where $T$ is the number of periods, $n$ is the problem dimension (number of random variables) and $k$ is the maximum support size of any random variable. This improves over previous regret bounds by a $\sqrt{n}$ factor. In fact, our dependence on $n$ and $T$ is the best-possible due the $\Omega(\sqrt{nT})$ lower bound for multi-armed-bandits. Our main technique is the use of Hellinger distance in bounding the ``error'' between the true and learned distributions, and the use of a constant-factor chain rule for the Hellinger distance of dependent random variables.

---


### 115. [Measuring Empowerment from Offline Data for Intrinsically Motivated Exploration](https://arxiv.org/abs/2610.24461)

**<font color=#1a73e8>作者：</font>** Ishir Garg, Vivek Myers, Qiyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large, unlabeled datasets of prior experience have become increasingly available for agentic tasks in domains such as robotics and coding. A common recipe for these tasks is to train a policy using the prior data, and then further improve it with online rollouts. But while much work has studied how to use both the offline and online data for policy extraction, far less work has been done to understand how the prior data can be used to efficiently \textit{explore} during the online learning phase. Previous work has attempted to formalize this idea by defining the \textit{empowerment}, a measure of how many future states an agent can realize; states with higher empowerment require more exploration as there are more futures to explore. However, existing methods for estimating empowerment require online policy rollouts in the environment. We propose the first method for estimating empowerment from unlabeled prior data, without any environment interaction. By jointly learning an empowerment-maximizing policy together with its discounted state-occupancy measure, our estimator can be trained on unlabeled trajectories generated from any unknown policy. We demonstrate that our empowerment estimator qualitatively gives intuitive empowerment measures and show that the pretrained estimator can be used to improve exploration in the online goal-conditioned reinforcement learning setting. Code is available at \url{this https URL}.

---


### 116. [O-SCD++: Replay-Free Online Scene Change Detection via Recursive Evidence Fusion](https://arxiv.org/abs/2610.24462)

**<font color=#1a73e8>作者：</font>** Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online scene change detection requires an agent to detect what has changed in a previously mapped environment while it is still on site, observing from unconstrained viewpoints and without access to future observations. This causal setting is strictly harder than its offline counterpart, and online methods have consistently trailed offline accuracy. O-SCD closed that gap by treating change as a persistent property of a 3D Gaussian splatting map of the reference scene, surpassing the strongest offline methods in change detection accuracy while operating at over 10 frames per second. O-SCD optimizes a change field over the Gaussians of the reference map, refitting it to all past cue maps at every frame, a step that consumes more than half of the per-frame budget and forces accuracy to be traded against speed. We present a replay-free formulation that eliminates this trade-off. Because the reference map stays fixed, rendering the change field is a linear operation. Each new observation can therefore be carried onto the map's Gaussians directly, by a single backward pass of the renderer, which reduces multi-view fusion to an exact two-scalar recursion per Gaussian. Past observations are never stored or revisited. The self-supervised objective that O-SCD minimizes by descent also determines the decision threshold exactly, by sorting, yielding a label-free per-frame cutoff whose margin provides a selective-prediction signal. On PASLCD, our method improves mean intersection over union from 0.489 to 0.575 and throughput from 11.8 to 25.6 frames per second, even exceeding O-SCD's offline result while remaining strictly causal.

---


### 117. [Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation](https://arxiv.org/abs/2610.24464)

**<font color=#1a73e8>作者：</font>** Yangzhi Chen, Feiran Liu, Zishuo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Individually competent robot skills can fail when composed: tools may lack a required capability, completion signals may misrepresent physical progress, and one skill may leave a state that violates its successor's prerequisites. We introduce Recursia, a recursive self-improvement framework that treats the shared executable stack, rather than individual task programs, as the persistent unit of improvement. The stack integrates tools, skills with execution contracts, handoffs, and verifiers. Source-side execution traces guide failure attribution and the generation of missing tools or repairs to existing shared components. Generality checks, mechanism tests, and paired selection and regression gates determine which changes become the next parent. The resulting stack is frozen and reused through declarative task adapters, allowing source-derived changes to support new compositions without target-side code repair. Experiments cover LIBERO-Pro Long simulation and a physical Franka FR3 equipped with a Franka Hand. In simulation, Recursia improves success over ASPIRE by 5.8 percentage points under Pos perturbations and 15.1 points under Task perturbations. Across three physical compositional target tasks, it improves mean success over the Skill Document Only baseline by 40 percentage points. Analyses of constituent execution, candidate rejection, and inference drivers distinguish local mechanism improvements from complete task success and characterize the cost of feedback-conditioned orchestration. These results examine shared executable interfaces as a concrete mechanism for compositional transfer in robot programming.

---


### 118. [Unifying Amplitude-Phase Coupling and Reliable Endogenous Priors for Low-Light Image Enhancement](https://arxiv.org/abs/2610.24467)

**<font color=#1a73e8>作者：</font>** Tongshun Zhang, Zixuan Zhong, Pingping Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frequency-domain methods have shown strong potential for low-light image enhancement (LLIE) because they can effectively regulate global illumination. However, most existing methods assume that amplitude and phase can be restored independently, while overlooking their inherent spectral coupling. This artificial decoupling often leads to information inconsistency and structural distortions. To address this issue, we propose a frequency-spatial framework that jointly models spectral interaction and reliable prior guidance. We first empirically analyze the coupling between amplitude and phase and develop an Amplitude-Phase Adaptive Compensation Fusion (APACF) module. Instead of enforcing a hard separation between the two components, APACF enables their bidirectional interaction, resulting in spectrally coherent restoration. In addition, directly extracting priors from raw low-light inputs is unreliable, since severe noise and underexposure destroy critical visual content. To alleviate this problem, we introduce an Endogenous Reliability Prior (ERP). Specifically, we treat an intermediate result, preliminarily restored in the frequency domain and already close to the ground-truth illumination, as a high-fidelity source for extracting complementary pseudo-infrared and gradient cues. Based on ERP, we further design a Dual-Modal Guided Refinement Network (DGRN) to inject these purified structural cues into the decoder, thereby recovering missing fine textures more accurately. Extensive experiments on benchmark datasets show that our method achieves state-of-the-art performance and consistently surpasses existing methods in both quantitative metrics and visual quality. Our code is available at this https URL.

---


### 119. [Beyond Recall Saturation: Scaling Hard-Negative Reranker Training for Industrial Legal Retrieval](https://arxiv.org/abs/2610.24478)

**<font color=#1a73e8>作者：</font>** Yunhan Li, Mingjie Xie, Zeyang Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Industrial retrieval systems often improve quality by enlarging embedding candidate pools or adopting complex training pipelines. We show that, under a sufficiently large but practical candidate pool, embedding recall exhibits diminishing returns, motivating a closer examination of reranker quality. On Chinese legal retrieval benchmarks, embedding top-300 reaches a high-recall operating region, while relevant evidence may still be ranked below the output cutoff. We compare hard-negative strategies for reranker training, including embedding-mined, self-mined, and dynamic-negative variants, under aligned retrieval protocols that evaluate reranking after candidate retrieval. Among the evaluated staged configurations, an embedding-to-self-mined pipeline provides a favorable trade-off; additional dynamic stages do not improve all held-out metrics. The selected pipeline scales from a 0.6B to a 4B reranker. Relative to the native 4B reranker, the trained 4B Stage2 model improves reported metrics on the STARD and CSAID benchmarks and on an internal development set, and is preferred in 72.4\% of non-tied comparisons on 410 de-identified, reconstructed internal operational-query inputs in a latency-sensitive offline preference evaluation. These results support evaluating the retrieval and reranking stages separately when selecting an optimization target for industrial retrieval systems.

---


### 120. [RiSE: Residual Subspace Expert for Generalizable Text-Centric Image Forgery Localization](https://arxiv.org/abs/2610.24480)

**<font color=#1a73e8>作者：</font>** Kahim Wong, Kemou Li, Yiming Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI-assisted image editing becomes increasingly prevalent, Text-Centric Image Forgery Localization (TFL) is essential for protecting trust in financial and legal records. However, we observe that existing TFL detectors predominantly rely on Full-Parameter Fine-Tuning (FPFT) and fail to generalize to unseen forgery types because FPFT can induce low-rank feature collapse and overfit training artifacts. Meanwhile, prior detectors capture diverse forgery traces with a single unified representation, making subtle traces entangled and difficult to learn. To address these challenges, we propose RiSE, a Residual Subspace Expert model that preserves pre-trained priors by freezing principal SVD components and adapting only the residual subspaces with a ViT-only segmentor to avoid feature collapse. RiSE introduces forgery-aware residual experts, where each expert is trained independently on a training subset with a particular forgery type, and we show that cross-domain localization performance improves consistently as more experts are added. At inference, we introduce Latent Perturbation Confidence (LPC), which selects the most confident expert by analytically computing the latent-perturbed output. LPC enables efficient confidence estimation with a single forward pass, avoiding repeated forward passes on perturbed samples and improving expert selection. By training on synthetic forgery data, RiSE with 1 expert outperforms prior methods on real-world forgery images by 20.4% while reducing training steps by 10 times. Scaling the number of experts to 9 yields a 35.8% gain. RiSE remains effective with DCT feature, even when the majority of the parameters is frozen with RGB-only pretraining. Code: this https URL.

---


### 121. [Vocal-Tract Acoustics, Aerodynamics, and Overlap-and-Add Synthesis in DYNARTmo](https://arxiv.org/abs/2610.24490)

**<font color=#1a73e8>作者：</font>** Bernd J. Kröger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the acoustic and aerodynamic extension of DYNARTmo, a dynamic articulatory model for visualizing and synthesizing speech production. Gestural control trajectories determine vocal-tract geometry, which is converted into an acoustic tube with nasal branching and effective lateral passages. A lumped aerodynamic network relates prescribed glottal motion and pulmonary pressure to airflow and supraglottal pressure storage. Phonatory excitation, oral friction, and glottal aspiration are synthesized as separate contributions. Frame-specific acoustic responses are combined by overlap-and-add, preserving response tails beyond individual control frames. Three German words, ``Tasse'', ``Muse'', and ``Lade'', illustrate the coordination of articulation, pressure, flow, and acoustic sources across vowels, nasals, laterals, fricatives, and plosives. The implementation has been optimized by the author primarily for sound recognizability; independent perceptual evaluation remains outstanding, and fricative-noise naturalness requires further refinement. The model provides an inspectable, articulatorily controlled production plant for future neural simulations of babbling, imitation, and early word acquisition. Further work will improve acoustic realism, reduce empirical source corrections, and extend the sensory information available to developmental learning models.

---


### 122. [VBO-MI: A Differentiable Black-Box Optimization Framework via Variational Mutual Information Estimation](https://arxiv.org/abs/2610.24491)

**<font color=#1a73e8>作者：</font>** Farhad Mirkarimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world tasks require optimizing expensive black-box functions accessible only through noisy evaluations, a setting commonly addressed with Bayesian optimization. While Gaussian processes(GPs) and Bayesian neural networks have driven significant progress, GP-based methods scale cubically with observations, and BNN-based approaches remain burdened by expensive posterior sampling such as Hamiltonian Monte Carlo, and inner-loop acquisition optimization in high-dimensional setting. In this work, we propose VBO-MI, a fully gradient-based BO framework that requires no assumptions on a Gaussian prior or a variational posterior family over $f$. While our framework uses gradient-based updates to train the internal action and information-estimation networks, it treats the objective function $f$ as a strict black box, requiring only zeroth-order evaluations. To enable end-to-end gradient flow, we employ an actor-critic architecture consisting of an action-net to navigate the input space and a variational critic to estimate a surrogate information signal for exploration. Additionally, we design a lightweight surrogate that approximates the objective from observed data using a replay buffer, which reduces the total required real function queries to one batch per iteration. We provide theoretical analysis for our framework, establishing convergence of its training objective and surrogate estimator, and showing, that near-optimal solutions exist. We evaluate our method on a diverse suite of benchmarks, including high-dimensional synthetic function and complex real-world tasks such as Rover Trajectory planning optimization, the Lunar Lander, and Pest Control problems. Our experiments demonstrate that VBO-MI provides the same or superior optimization performance over the various baselines.

---


### 123. [Backend-Frontend Converter: Component-Based Conversion of .NET Computational Models to TypeScript](https://arxiv.org/abs/2610.24492)

**<font color=#1a73e8>作者：</font>** Petr Ivankov, Max Shestov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational models developed in .NET often need to run locally within web applications. We present Backend--Frontend Converter, an architecture for generating TypeScript implementations of component-based models. The converter maps components, connections, aliases, and formula trees to model-specific TypeScript code. Reusable runtime libraries provide numerical integration, data access, and state handling. We evaluate stored generated implementations through four orbital scenarios and a recorded trading-strategy comparison. Orbital calculations execute in a browser and are paired with C\# results by crossing event and timestamp; trading outputs are aligned by date. Analytic scheduler tests and deliberately perturbed outputs assess the validation procedure. Each orbital scenario produces 91 paired events with identical timestamps. Position and velocity differences remain below $(10^{-6}\)~km$ and $(10^{-9}\)~km/s$. All 20 analytic scheduler checks pass, and the comparator detects each of three prescribed state and time perturbations. The trading comparison contains 501 aligned daily records with matching indicator values, positions, and order events. The evaluated implementations preserve the compared outputs across the C#/TypeScript boundary. Component-specific generation and reusable execution libraries provide a practical route from supported .NET computational models to TypeScript applications.

---


### 124. [HiPPO Functional Memory: Coordinate-Queryable Attention for Irregular Time Series](https://arxiv.org/abs/2610.24501)

**<font color=#1a73e8>作者：</font>** Zhaodong Guo, Haoyun Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular time series require models to answer temporal queries at arbitrary coordinates, yet existing approaches typically retain observation-dependent representations that must be repeatedly resolved for each query. We introduce HiPPO Functional Memory (HiPPO-FM), a functional-memory attention operator that compiles an irregular history into a reusable coordinate-addressable state. Instead of storing observation-indexed tokens or latent trajectories, HiPPO-FM writes observations into a fixed-rank functional space and performs direct coordinate evaluation through matched functional geometry. Kernel-smoothed HiPPO coordinates and Gram-based readout define a shared write/read mechanism, while observed-support self-attention enables content-dependent representations before compression. We characterize the induced finite-dimensional query space and derive an error decomposition separating functional geometry approximation from learned-memory mismatch. Across continuous-coordinate reconstruction, irregular representation learning, real-world extrapolation, and event-sequence prediction, HiPPO-FM consistently improves strong irregular time-series baselines, achieving strong reconstruction accuracy on Spiral, competitive performance across 20 UEA datasets, improved real-world extrapolation, and superior results on several irregular event benchmarks. After encoding, the compact functional state can be reused across different query sets without reprocessing the observation history.

---


### 125. [SAP-Depth: Scene-Adaptive Probability Framework for Self-Supervised Monocular Depth Estimation](https://arxiv.org/abs/2610.24506)

**<font color=#1a73e8>作者：</font>** Bowen He, Li Zhang, Yujie Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised monocular depth estimation remains challenging due to the loss of fine-grained details and limited adaptability to varying scene structures. In this paper, we propose SAP-Depth, a novel architecture based on Scene-Adaptive Probabilistic. Unlike traditional methods, we introduce a Dynamic Bins mechanism powered by a Learnable Parameter Predictor, which adaptively estimates scene-specific depth distributions conditioned on the input image context. Furthermore, a Bin-wise Probability Distribution Decoder is designed to effectively fuse multi-scale representations to predict dense depth probability distributions, significantly enhancing boundary sharpness and structural recovery. Through the collaborative coupling of these proposed modules, our model achieves dynamic prediction of scene-specific depth distributions. Extensive experiments on the KITTI dataset show that SAP-Depth outperforms existing state-of-the-art methods in accuracy, particularly in its ability to better preserve complex edge details. Further, tests on the Make3D dataset validate the model's excellent generalization capability and robustness.

---


### 126. [BEM: Learning Bregman Divergences for Concept Erasure in Flow Matching Models](https://arxiv.org/abs/2610.24508)

**<font color=#1a73e8>作者：</font>** Mohamed-Hicham Leghettas, Markus Püschel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept erasure removes harmful, private, or copyrighted concepts from text-to-image models while preserving their other abilities. Leading models such as FLUX and Stable Diffusion 3 are trained with flow matching, and erasure methods for them fine-tune the model toward a guided teacher's velocities under a Euclidean loss. Yet the squared distance is only one member of a larger family: Bregman divergences are exactly the losses under which flow matching recovers the correct velocity field, and each member shapes differently what is erased and what is preserved. We introduce BEM (Bregman erasure matching), which is, to our knowledge, the first to learn this divergence through bi-level optimization, so that the fine-tuned model forgets the concept on unseen prompts while its unrelated generations stay unchanged. In the experiments we target the suppression of nudity, violence, real identities, and copyrighted characters. Under the evaluation protocol of GEM, BEM removes more of the concept than GEM on most settings, cutting the unsafe rate on bloody gore from 53.9% to 14.4% and the FID on nudity from 8.64 to 6.64, while retention holds on some concepts and degrades on others.

---


### 127. [What "Form'' of Uncertainty Does Conformal Prediction Quantify?](https://arxiv.org/abs/2610.24510)

**<font color=#1a73e8>作者：</font>** Soroush H.Zargarbashi, Mohammad Sadegh Akhondzadeh, Rebekka Burkholz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) is a post-hoc calibration method that returns prediction sets with distribution-free coverage guarantees, and the size of the output set is often interpreted as a notion of uncertainty. We show that the difference in set size between full and split CP is directly connected to Bayesian posterior variance, which is the epistemic uncertainty of the model. Essentially, this difference in set size is an aggregation of two opposite effects: (1) better model accuracy and therefore smaller set size achieved by training over extra calibration points, and (2) the "formability" of the model at test point towards every possible label. The latter effect vanishes with stronger models or more calibration data (as epistemic uncertainty is known for that behavior). It turns out that the model's formability itself (without the quantization effect of prediction sets, and through estimating the posterior variance) is a useful tool to quantify the epistemic uncertainty. In our empirical evaluation it performs on par with the state of the art in many setups.

---


### 128. [TopoCompile: Molecular Generation with Exact Global Count Constraints](https://arxiv.org/abs/2610.24511)

**<font color=#1a73e8>作者：</font>** Xiang Wu, Rong-Hua Li, Quanqing Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular generation designs novel molecules with desired structures and properties. Global count constraints specify molecular size, elemental composition, and ring content without prescribing detailed structure. Property-conditioned generators steer generation toward such targets but do not guarantee exact satisfaction. We introduce TopoCompile, which combines an autoregressive component-tree generator with a dynamic-programming compiler for supported component-additive integer counts. TopoCompile represents molecules as trees of intact ring systems and individual atoms, making each supported count additive over components. At each step, an autoregressive Transformer scores component and attachment actions, while the compiler masks actions with no target-satisfying completion. Within the fixed component vocabulary and typed attachment rules, constrained decoding guarantees exact equality for supported non-negative, component-additive integer counts. Applied at inference time, these checks let the same trained generator support different targets and count combinations without retraining. Across four benchmarks, TopoCompile achieves 100% Exact-valid yield for Common and Rare four-count target groups; the strongest baseline within each dataset reaches 44.9% or less on Rare targets. In unconditional generation, it achieves the highest validity or valid-unique-novel (V.U.N.) among the compared methods across all four benchmark datasets.

---


### 129. [$M^2Net$: Unifying Scale-Specific Structures and Prototype Decomposition for Spatial-Temporal Forecasting](https://arxiv.org/abs/2610.24516)

**<font color=#1a73e8>作者：</font>** Chengyang Zhou, Zijian Zhang, Hao Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial-temporal forecasting is pivotal for intelligent urban management yet remains challenging due to the intricate coupling of spatial dynamics and temporal non-stationarity. Existing approaches, while effective, often overlook two fundamental characteristics of real-world data: (1) Granularity-dependence, where dominant spatial correlations shift significantly across different time scales, and (2) Signal entanglement, where global common patterns are inextricably mixed with node-specific disturbances. In this paper, we propose a novel framework named $M^2Net$ (Multi-Scale Masked attention and Prototype network) to unify scale-specific structural learning and semantic decomposition. First, to capture the evolution of spatial dependencies, we introduce a Multi-Scale Masked attention mechanism. By downsampling temporal features into multiple resolutions, we dynamically generate scale-adaptive spatial masks, allowing the model to distinguish between micro-scale physical neighbors and macro-scale functional correlations. Second, to disentangle unique variations from shared trends, we propose a Prototype Residual Learning module. It retrieves global common patterns from a momentum-updated prototype bank and subtracts them from node representations, explicitly forcing the network to model the residual unique deviations. By integrating these two orthogonal views, i.e., structural multiscaling and semantic decomposition, our approach effectively isolates valid spatial-temporal signals from noise. Extensive experiments on real-world datasets demonstrate that $M^2Net$ outperforms state-of-the-art baselines on extensive empirical verifications.

---


### 130. [MOMO: Human Motion from Moving Sounds](https://arxiv.org/abs/2610.24522)

**<font color=#1a73e8>作者：</font>** Deli Cai, Shuyang Xu, Zhiyang Dou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human responses to sound depend not only on its semantic content, but also on the evolving spatial relationship between source and listener, conveyed through spatial audio and its temporal dynamics. Modeling human reactions to such dynamic spatial audio is important for character animation, human behavior analysis, and robotics. As of yet, existing audio-driven motion generation methods primarily focus on non-spatial or static acoustic conditions, leaving this important problem largely underexplored. To bridge this gap, we formulate the novel task of dynamic spatial-audio-driven human motion generation and introduce two motion-captured datasets. We introduce the Dynamic Spatial Audio and Motion dataset (DySAM) as the first dataset and benchmark for this task, providing synchronized binaural audio, 3D human motions, and moving sound source trajectories. Given the importance of dynamic spatial cues of sound sources, we further provide the Dynamic Spatial Audio Localization dataset (DySAL), an auxiliary binaural localization dataset that pairs diverse acoustic events with head poses and moving source trajectories to support spatial audio perception. For benchmarking, we propose MOMO for human Motion generation from Moving Sounds, a diffusion-based framework guided by three coupled principles: localization, understanding, and generation. MOMO performs localization by estimating head-centric spatial direction cues of the moving source directly from raw binaural audio, avoiding reliance on ground-truth source coordinates. It performs understanding by extracting frame-wise audio-content representations, and performs generation by conditioning motion diffusion on both semantic features and dynamic spatial cues. Experiments show that MOMO outperforms existing baselines in motion fidelity, audio-motion alignment, and physical plausibility.

---


### 131. [Rethinking EEG Spatial Super-Resolution as Dynamic State Decomposition and Filtering](https://arxiv.org/abs/2610.24528)

**<font color=#1a73e8>作者：</font>** Hongjun Liu, Leyu Zhou, Chang Ge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EEG spatial super-resolution aims to recover high-density neural signals from sparse electrode observations. Existing methods have achieved substantial progress through spatial modeling, generative reconstruction, and temporal representation learning. However, the current EEG state contains two different sources of information: predictable evolution inherited from preceding states and newly emerging changes revealed by the current observation. Most approaches typically do not model these two components explicitly. In this work, we formulate streaming EEG spatial super-resolution as a sequential state filtering problem and propose Dynamic State Filtering (DSF). Rather than relying on a single temporal reconstruction pathway, DSF combines a history-aware dynamical branch with an innovation-filtering branch that explicitly decomposes waveform-state estimation into prediction and observation-driven correction. To infer how spatially incomplete innovations should affect missing locations, DSF routes the observed innovations across electrodes through a mask-constrained, topology-aware transition operator and incorporates them through uncertainty-aware state correction. The two complementary estimates are finally fused to reconstruct the dense EEG signal. Experiments on SEED, SEED-IV and BCI2000 demonstrate that DSF improves reconstruction fidelity and downstream utility while maintaining robustness under dynamically changing and unreliable sparse observations.

---


### 132. [An Optical Music Recognition Tool for String Quartets](https://arxiv.org/abs/2610.24530)

**<font color=#1a73e8>作者：</font>** Jin-Shiang Hu, Bo-Yuan Cheng, Li Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an optical music recognition (OMR) system tailored for PDF scores of string quartet pieces. The approach begins with a SegNet-based segmentation model to localize musical regions, followed by convolutional neural networks and image processing techniques to classify and extract musical symbols. To improve rhythmic precision, dynamic programming methods enforce time signature constraints and explicitly handle tuplets. Evaluation using a longest common subsequence metric across multiple feature matrices demonstrates robust accuracy in recognizing pitch, onset, duration, and accidentals on a benchmark dataset. Code and data are available at this https URL.

---


### 133. [Contrastive Hypergraph Source-free Domain Adaptive Object Detection in Adverse Weather Conditions--Extended Version](https://arxiv.org/abs/2610.24532)

**<font color=#1a73e8>作者：</font>** Jicheng Yuan, Tung Kieu, Manh Nguyen-Duc 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather conditions such as fog, rain, snow, and low illumination introduce structured visibility degradations that severely impair object detectors trained on clear-weather data. When source data are inaccessible due to privacy or trans- mission constraints, source-free domain adaptation (SFDA) becomes necessary. However, existing SFDA methods based on pairwise contrastive learning struggle to capture high-order semantics and often suffer from agreement collapse under severe corruption. We propose REUNION, a hypergraph-guided SFDA framework for object detection in adverse weather conditions. REUNION constructs a contrastive hypergraph over target-domain object proposals, encoding high-order relations through intra-image context, weather-aware grouping, prototype-based semantic anchors, and uncertainty-aware connections between reliable and low-confidence instances. To effectively exploit these structured relations, we introduce a group-wise Hyper-InfoNCE objective that optimizes representations at the hyperedge level, enabling semantic information to propagate from confident proposals to corrupted or low-contrast instances. Experiments with diverse benchmarks demonstrate that REUNION effectively mitigates domain shifts and achieves state-of-the-art performance in SFDA settings.

---


### 134. [Structured Latent Dynamics for Long-Horizon Embodied World Models](https://arxiv.org/abs/2610.24534)

**<font color=#1a73e8>作者：</font>** Kevin Chen, Yu-Wei Zhan, Haoran Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable long-horizon prediction remains a central challenge for embodied world models. Although recent generative models can synthesize visually plausible action-conditioned futures, their latent dynamics are typically learned through unconstrained transition modules, which may gradually deviate from coherent physical evolution as predictions are recursively rolled forward. We investigate whether explicitly structuring latent state evolution can improve the stability and utility of such imagined trajectories. To this end, we introduce HWM, a structured dynamics framework that represents backbone latents in a learned phase space consisting of generalized coordinates and momenta. Future states are propagated through dissipative Hamiltonian dynamics and mapped back to the original latent representation through a learnable inverse interface. The resulting formulation can be integrated into existing world-model architectures without redesigning their perception or decoding components, while multi-step transition supervision encourages the structured rollout to remain aligned with the latent trajectories induced by real observations. Controlled simulation experiments show that HWM produces more accurate estimates of velocity, acceleration, and jerk and substantially reduces long-horizon energy drift relative to unstructured latent dynamics. We further evaluate the approach across three distinct embodied world-model settings, covering single-arm multi-view prediction with Ctrl-World, dual-arm single-view prediction with EVAC, and task-oriented single-arm prediction with Cosmos-Predict2.5-2B. On RoboCasa, incorporating HWM into Cosmos-Predict2.5-2B yields a 2.7% relative improvement in task success. On real-world AgiBot World trajectories, it improves nDTW by 9.7% with Ctrl-World and Logic by 8.4% with EVAC.

---


### 135. [A Multi-Step Inertial ADMM Algorithm for Federated Learning](https://arxiv.org/abs/2610.24536)

**<font color=#1a73e8>作者：</font>** Hao Li, Qingsong Wang, Xihong Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning has recently emerged as an important paradigm for large-scale distributed model training, which can be naturally formulated as a class of distributed learning problems. The alternating direction method of multipliers (ADMM) is a widely used approach for solving such problems. However, its practical performance is often hindered by significant communication overhead and system heterogeneity. In this paper, we propose a multi-step inertial ADMM algorithm, called MiFedADMM, for federated learning. The proposed method leverages multiple historical iterates on the server side to construct a higher-order extrapolation after each aggregation to accelerate the convergence behavior. Under mild assumptions, we establish convergence results for the single-step variant of the proposed method and derive an O(1/K) convergence rate. Numerical experiments on both synthetic and real-world datasets demonstrate the effectiveness and improved performance of the proposed method compared with existing approaches.

---


### 136. [Theory-Guided Instance-Dependent Early Stopping via Second-Order Loss Dynamics](https://arxiv.org/abs/2610.24540)

**<font color=#1a73e8>作者：</font>** Ahad Bin Islam Shoeb, Jamal Uddin Tanvin, Kamrul Hasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instance-dependent early stopping (IES) reduces training computation by skipping backpropagation for examples whose losses have stabilized, but the second-order loss-difference criterion used by IES lacks a theoretical justification. We develop Theory-Guided Instance-Dependent Early Stopping (TG-IES), which analyzes this criterion under explicit assumptions and derives a noise-calibrated mastery threshold and a conditional stability bound for instance exclusion. We show that second-order differencing has a favorable bias-variance trade-off over first- and third-order differences in a specific signal-to-noise regime, and that its signal contains both gradient-drift and curvature terms. TG-IES derives its stopping threshold and patience from training-run statistics rather than using the manually selected threshold of IES. Across CIFAR-10 and CIFAR-100, TG-IES saves 53-58% of backpropagation instances in its main convolutional settings while keeping accuracy within 0.1-0.9 percentage points of full training; in the primary ResNet-18/CIFAR-10 setting, this corresponds to 35.7% FLOP-normalized savings. The method also transfers to ViT-Tiny, where it achieves smaller savings and incurs a modest accuracy cost. These results provide a theoretical basis for second-order instance-dependent early stopping and show that theory-guided calibration can substantially reduce training computation under the assumptions and experimental settings studied.

---


### 137. [Cross-polarization pairing for label-free few-shot thin-section classification](https://arxiv.org/abs/2610.24546)

**<font color=#1a73e8>作者：</font>** Bingchen Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot classifiers of rock thin sections are meta-trained on many rock types that a petrographer has identified slide by slide, and this identification is the costly step that new collections lack. We study few-shot recognition of unseen rock types when no training slide is identified, and the only information available is what the microscope records anyway: which slide an image comes from, and whether it was taken in plane-polarized (PPL) or cross-polarized (XPL) light. We first show why generic unsupervised pseudo-tasks fit this setting poorly: the positives they find without labels are either wrong or near-duplicates of the anchor, so they teach the model little. Polarized-light microscopy provides positives that avoid both problems. The PPL and XPL views of one field show the same grains, so they are correct by construction, yet they look very different. We propose cross-polarization pairing (XPP), which treats each slide as a pseudo-class and pairs its PPL and XPL views of the same field location, so that matching must rely on grain shape and texture rather than on colour. On the Nanjing University collection of 108 rock types, with support and query images taken from different slides, XPP is the best label-free method on average over three random splits, and matches a supervised model trained on 78 identified rock types. Controls show that colour augmentation and other acquisition positives do not reproduce the gain. We also show that the image-level protocol of earlier work is saturated, and propose a cross-slide protocol in its place.

---


### 138. [CARVS: A Congestion-Aware Algorithm for Online Multi-Agent Pickup-and-Delivery in Human-Collaborative Warehouses](https://arxiv.org/abs/2610.24549)

**<font color=#1a73e8>作者：</font>** Chaoran Li, Zeyuan Zhao, Shao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Intelligent warehouse systems have transformed logistics by integrating robots with minimal infrastructure changes, boosting efficiency and optimizing workflows compared to traditional human-only operations. However, human-robot collaboration introduces new challenges, particularly due to human uncertainty, which leads to dynamic interactions and unpredictable behavior. To address these complexities, this paper presents the Multi-Agent Pickup-and-Delivery with Human Collaboration (MAPDwHC) problem, an extension of the Multi-Agent Pickup-and-Delivery (MAPD) problem that incorporates human unpredictability. This problem adds key constraints, such as dynamic obstacles caused by robots temporarily blocking paths when interacting with humans, and the need for real-time responsiveness. We formalize the MAPDwHC problem with additional constraints and properties. Based on this problem setting, we propose the CARVS algorithm, which improves task assignment and path planning by integrating task swapping, validation checks, and random initialization. CARVS reduces congestion, enhances adaptability to human-robot interactions, and ensures real-time responsiveness. Simulation results show that CARVS significantly reduces timeouts of path planning in large-scale scenarios where traditional MAPD algorithms fail, improving both efficiency and scalability.

---


### 139. [No-Regret Revenue Maximization in Sequential Market Making Under Inventory Constraints](https://arxiv.org/abs/2610.24562)

**<font color=#1a73e8>作者：</font>** Davide Maran, Marcello Restelli, Francesco Emanuele Stradi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Market makers keep trading efficient by setting bid and ask prices for buyers and sellers. In sequential market making, trades happen independently based on price thresholds, requiring the market maker to maintain balanced, low-risk inventory over T rounds. This paper studies how to maximize revenue with unknown buyer and seller valuations using regret minimization. When the market maker only sees trade success or failure, an algorithm achieves regret and inventory bounds proportional to T to the power of 2/3. When full order book data is available for failed trades, regret and inventory limits improve significantly to the square root of T. We also establish a fundamental trade-off via a lower bound, by proving that tighter round-by-round inventory limits strictly force higher minimum regret.

---


### 140. [Representations Have Trajectories: Characterizing Temporal Representation Dynamics in Neural Networks](https://arxiv.org/abs/2610.24571)

**<font color=#1a73e8>作者：</font>** Shivaprasad B. Gowda, Sparsh Mittal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that deep neural networks exhibit an implicit low-rank simplicity bias. In this paper, we investigate the questions that naturally arise from this observation. What are the temporal consequences of low-rank simplicity bias during optimization? How does representation geometry evolve throughout optimization rather than only at convergence? Do different neural architectures exhibit distinct geometric optimization behaviors? To answer these questions, we conduct a large-scale empirical study tracking representational geometry throughout training. We find that neural networks follow three recurring geometric trajectories: persistent high-rank, collapse-and-recovery, and persistent low-rank. We further identify Destructive Representation Collapse (DRC) as a pathological regime in which representations collapse to rank-one and fail to recover, leading to a sustained loss of representational capacity. While collapse-and-recovery is consistently associated with successful optimization in controlled settings, experiments on real-world models show that the relationship between geometric trajectories and optimization outcomes is configuration dependent. Overall, our findings suggest that representation geometry evolves dynamically during training and provide a new perspective on how deep neural networks learn.

---


### 141. [Concordance Plausibility Check for Intervention-Conditioned Human Digital Twins](https://arxiv.org/abs/2610.24577)

**<font color=#1a73e8>作者：</font>** Saeed Farzi, Christopher Kipps, John McBeth 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intervention-conditioned human digital twins predict treatment alternatives that cannot be observed in the same patient. Ordinary predictive accuracy therefore cannot establish counterfactual credibility. We propose the Concordance Plausibility Check (CPC), a claim-centered framework combining real-world evidence, qualified simulation and clinical knowledge. CPC matches evidence to the causal claim, audits contradictions and shared dependencies, and reports Pass, Fail or reason-coded Indeterminate.

---


### 142. [DeliMF: Gated Cross-Attention Fusion of Structured Time Series and Clinical Text for Early Intensive Care Delirium Prediction](https://arxiv.org/abs/2610.24585)

**<font color=#1a73e8>作者：</font>** Yibo Yang, Zerui Huang, Haomiao Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Delirium affects a large fraction of intensive care unit (ICU) patients and foreshadows longer stays, lasting cognitive decline, and higher mortality. Flagging the patients who will become delirious within the first day of admission would give clinicians a window to intervene. Yet state-of-the-art predictors rely only on the structured electronic health record (EHR) of vital signs, laboratory values, and medications, while overlooking the free-text clinical notes written in the same window, which carry information the numbers cannot encode. To this end, we present DeliMF, a multimodal framework that fuses the structured time series with clinical text. It encodes the structured signals with a temporal Transformer and the time-stamped radiology reports with a clinical text encoder, and fuses the two through a gated cross-attention module. The gate learns a per-patient weight on the text; when a patient has no note the gate closes and DeliMF reduces to its structured-only form, giving robustness to missing text by construction. On an incident-only MIMIC-IV cohort, DeliMF improves significantly over the baselines, particularly on patients who carry clinical text, while losing nothing on those without. Ablation studies confirm the contribution of multimodal fusion and gated cross-attention, and a case study further shows that fusing clinical text with the structured stream recovers delirium cases that the structured data alone misses. We hope DeliMF encourages early ICU prediction to make fuller use of the overlooked clinical text and contributes to the early identification and timely intervention of delirium.

---


### 143. [Dynamic self-ensemble on multi-exit residual vision transformer for small-data image classification](https://arxiv.org/abs/2610.24602)

**<font color=#1a73e8>作者：</font>** Stephen Ekaputra Limantoro, Yan-Kai Wang, Ching-Chun Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT) has garnered increased attention for image classification in recent years. However, ViT is notorious for its data-hungry problem as it achieves high-performance results when only trained on large-size datasets. In this paper, we study how ViT specifically works on small-scale datasets with limited data where the availability of image data is often constrained in practice, especially in fields such as medical imaging. To mitigate the issue, we designed a multi-stage residual ViT, dubbed ReSEViT, with the self-ensemble method to utilize multi-level information from intermediate features. Due to the complex decision boundaries for classifications, relying on a single classifier can lead to prediction errors. Hence, we propose a new learning method for ViT, named self-ensemble learning, which ensembles multi-stage classifiers in a single model. Our self-ensemble comprises a novel approach, Dynamic Learner Selection (DLS), to adaptively select the importance of different stages. ReSEViT incorporates residual token embeddings which is a ResNet-like block to model effective local structures alongside with transformer blocks in each stage. The integration of residual tokens and self-ensemble learning into a multi-stage ViT highlights the reduction in redundancy, prediction error and variance while maintaining an efficient model size for small-scale image datasets.

---


### 144. [SCOPE-VSR: A Broad-Coverage Training Dataset for Video Super-Resolution](https://arxiv.org/abs/2610.24604)

**<font color=#1a73e8>作者：</font>** Gengyu Liao, Yechun Yong, Zheng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-domain video super-resolution (VSR) requires temporally coherent details across widely varying scenes and subjects. However, existing training datasets are often semantically imbalanced and insufficiently diverse. We address this data bottleneck with a structured curation pipeline for open-domain VSR, SCOPE. In this pipeline, we combine task-oriented video selection with hierarchical semantic rebalancing. Applying this pipeline to a large-scale collection of data sources, we construct the SCOPE-VSR dataset for training and SCOPE-test for testing. SCOPE-VSR has approximately 27k videos and provides balanced and diverse coverage of various real-world scenarios and subjects. We further develop GraCo-VSR, a novel framework for one-step video restoration. GraCo-VSR adopts a reliability-aware design with explicit supervision to reduce degradation-induced distortions in motion and texture guidance, allowing the model to benefit more effectively from the diverse training content in SCOPE-VSR. Evaluations show that our model achieves strong reconstruction fidelity and perceptual quality. Our code is available at: this https URL.

---


### 145. [IntriAdapt: Generalizable Intrinsic-Guided Test-Time Adaptation for Metric Geometry Estimation](https://arxiv.org/abs/2610.24607)

**<font color=#1a73e8>作者：</font>** Jiaxing Chen, Zizheng Yan, Jingyu Zhuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering metric 3D geometry from images is fundamentally ill-posed due to perspective projection ambiguity. Current geometry models incorporate supplied or predicted intrinsics during inference, but do not use them to supervise model adaptation. To refine these predictions, test-time adaptation (TTA) typically relies on external depth measurements. In this paper, we instead use camera intrinsics as an output-side geometric verifier. Comparing the point cloud's viewing rays with those defined by the known intrinsics yields a direct measure of geometric inconsistency. We propose \textit{IntriAdapt}, a TTA framework that minimizes this closed-form geometric residual. By optimizing a lightweight LoRA adapter on a frozen geometry foundation model, our method aligns the prediction with the specific camera model without depth sensors or external priors. We further extend this approach to video sequences, demonstrating that adapting a short sequence generalizes to other sequences captured by the same camera. The adapted model processes held-out images in a feed-forward pass, without repeating optimization for each frame. Experiments on ten single-image and seven sequence benchmarks across multiple base models show that \textit{IntriAdapt} consistently outperforms both unadapted and oracle-intrinsics baselines in metric accuracy and relative geometry.

---


### 146. [HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference](https://arxiv.org/abs/2610.24611)

**<font color=#1a73e8>作者：</font>** Wanyi Chen, Wanqin Shen, Yuanchen Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating software agents on a full benchmark is expensive. A small task subset can preserve agent rankings while yielding inaccurate scores. Historical responses provide useful structure, but tasks with identical source responses can have different outcomes for a new target agent. We introduce Hierarchical Score Posterior Recovery (HSPR), which combines source-fitted response factors with uncertain group success rates. Observed target outcomes update the posteriors over the target latent state and group rates; posterior-guided acquisition selects subsequent tasks. Its score-based criterion equals the expected one-step reduction in full-score posterior variance. Observed successes and posterior-predictive counts for unqueried tasks yield a full-score posterior. The final estimate uses its median with source-selected calibration. At a 10% task budget on four task banks from the SWE-bench family, HSPR achieves the lowest mean absolute error (MAE) on three banks and the lowest maximum absolute error (MaxErr) on all four among the methods compared. Removing group uncertainty or replacing adaptive queries increases macro MAE in the respective controls. Macro MAE decreases across 5-20% budgets.

---


### 147. [How Much Do Activation Monitors Benefit from Original Model Computations?](https://arxiv.org/abs/2610.24613)

**<font color=#1a73e8>作者：</font>** James Oldfield, Shawn Im, Jay J Culligan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One powerful way to safeguard AI systems is to monitor their internal computations--where signs of undesirable behavior might be more easily detectable than from models' inputs and outputs alone. However, recent studies begin to question the premise that activations provide a unique window into model behavior. In this paper, we study how much of activation monitors' success depends on access to the original behavior-generating computations. Within a fixed choice of target model and monitoring architecture, we compare how well monitors trained and evaluated on trajectories that differ in computational context can predict the behavior of the original execution, after the transcript is changed in a controlled manner (e.g., its exact text, or chat formatting). We first find that much performance can be recovered without access to the original behavior-generating trace (in up to 4 models across 2 counterfactual monitoring tasks), but a mild yet consistent advantage to native-trained monitors remains, outperforming strongest controls by up to 0.014 AUROC. Interestingly, we find monitors trained with native access have notable uplift on original examples whose behavioral label changes under paraphrasing. We further find this a useful lens to expose limitations of baselines that use simple forms of privileged information (i.e., answer logit margins). While our results show the advantage of native monitor access is modest in aggregate, they highlight the importance of evaluations that identify if and when original model computations provide additional predictive value.

---


### 148. [Beyond Geometric Closure: Measuring and Diagnosing Mechanical Consistency in Visual Dynamics](https://arxiv.org/abs/2610.24619)

**<font color=#1a73e8>作者：</font>** Qibin Gu, Yunfeng Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual accuracy leaves open whether predicted motion obeys dynamics. We introduce a framework for measuring and diagnosing mechanical consistency in visual dynamics. An independent SI audit of rigid closed chains separates geometric admissibility, reaction-free actuator effort, and work--energy balance. Continuous scoring measures progress against fixed engineering targets, while reference replay quantifies measurement error. With three seeds per setting, we evaluate KeyCLD and CON across 343 planar assemblies at 64/256 pixels and V-JEPA + AC and LingBot-VA on 100 shared spatial test assemblies. CON reduces image MSE by 37.6%/37.2% relative to persistence, yet neither planar model attains valid native geometry. At 256 pixels, calibrated RGB replay places forecast errors far above measurement error. With exact states, KeyCLD preserves geometry and RK4 training raises its score from 52.65 to 64.30. In both spatial pathways, CAD/IK reconstruction restores geometry while mean actuator residuals exceed five times the engineering targets. The interventions distinguish gains in visual prediction and geometric admissibility from remaining force and energy errors.

---


### 149. [Say It or Grab It? Conversational Control of UI Adaptations in Mixed Reality](https://arxiv.org/abs/2610.24640)

**<font color=#1a73e8>作者：</font>** Sina Elahimanesh, Joao Marcelo Evangelista Belo, Isidora Jeknic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mixed reality interfaces must continuously adapt to a user's changing task and environment, yet adaptation policies are fixed in advance, either preset by the system or configured by the user. Natural language offers a way to state changing needs mid-task, but whether users can express interface behavior this way, and what it gains over direct manipulation, is unknown. We first elicited how users verbalize adaptation needs (N=19). We then built ConverseMR, which translates a spoken request into adaptation objectives and constraints and satisfies them continuously as the user's context changes. In a within-subjects study (N=24), conversational and direct control proved complementary: direct manipulation for precision, ConverseMR for reach and expressive breadth, with their combination rated highest. Spoken commands were rarely final and users frequently refined and replaced them upon experiencing the result, characteristic of, what we call, user-led adaptation, where users communicate adaption needs and the system identifies a solution.

---


### 150. [Spectral-Aware Proposal Enhancement for Diffusion-Based Multispectral UAV Multi-Object Tracking](https://arxiv.org/abs/2610.24642)

**<font color=#1a73e8>作者：</font>** Xu Lin, Tingfa Xu, Tianhao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral UAV multi-object tracking (MOT) with oriented bounding boxes remains challenging due to small targets, cluttered backgrounds, and unstable inter-frame associations. Although diffusion-based MOT provides an effective iterative proposal refinement paradigm, existing diffusion-based trackers lack dedicated designs for exploiting multispectral cues in proposal initialization and confidence calibration, limiting tracking robustness in complex UAV scenarios. This letter proposes DSATrack, a diffusion-guided spectral-aware tracking framework for multispectral UAV MOT. Specifically, a lightweight spectral encoder injects multispectral information into the RPN branch through feature fusion, enabling the RPN head to generate high-quality object-aware proposals. These proposals are then injected into the initial proposal set to provide reliable spatial priors for diffusion refinement. Furthermore, a spectral-saliency confidence modulation strategy recalibrates refined tracking confidence according to local multispectral saliency contrast before score thresholding, enhancing spectrally reliable candidates while suppressing unreliable ones. Without modifying the original diffusion refinement head, DSATrack improves both proposal quality and post-refinement candidate selection. Experiments on the MMOT benchmark demonstrate that DSATrack outperforms the adapted DiffusionTrack baseline by 4.6 HOTA, 9.0 MOTA, and 7.7 IDF1 points, showing its effectiveness for multispectral UAV MOT.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
