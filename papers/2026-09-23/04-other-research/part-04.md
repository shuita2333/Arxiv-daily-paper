# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 151. [HDMamba-YOLO: Efficient State-Space Perception and Local Spatial Reconstruction for UAV Small Object](https://arxiv.org/abs/2609.23061)

**<font color=#1a73e8>作者：</font>** Linduo Wei, Junjie Fan, Yijun Mai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small-object detection in UAV imagery is challenged by weak visual evidence, ambiguous boundaries, dense object distributions, and complex backgrounds. Effective detection therefore requires long-range contextual information for target-background discrimination while preserving explicit local two-dimensional structures for accurate localization. These requirements arise at different stages of the detection pipeline and are not naturally addressed by a uniform feature-processing strategy. We propose Hybrid Dual-domain Mamba-YOLO (HDMamba-YOLO), a stage-wise heterogeneous SSM-CNN detector organized according to a perception-reconstruction-alignment-interaction rationale. EfficientVMamba-based EVSS establishes long-range contextual perception in the backbone, while PhasePatchMerging2D provides phase-aware hierarchical transitions. DST-Wrapper and Native C3k2-ASSAF then perform perception-to-reconstruction transition and repeated local two-dimensional reconstruction during FPN/PAN aggregation. DySample provides content-adaptive cross-scale resampling, while OS-CVTIA introduces macro-micro interaction and task-specific modulation for localization and classification. On VisDrone2019, HDMamba-YOLO-B achieves 42.737% mAP50 and 25.713% mAP50:95 with 10.042M parameters and 29.879 corrected GFLOPs. HDMamba-YOLO-Lite achieves 41.140% mAP50 and 24.741% mAP50:95 with 5.344M parameters. Under the unified AI-TOD evaluation protocol, HDMamba-YOLO-B obtains 21.621% AP and 47.881% AP50. Controlled ablations further support the stage-wise allocation of state-space perception, convolutional reconstruction, dynamic alignment, and task interaction for UAV small-object detection.

---


### 152. [LD-RSVIS: A Large-Scale and Diverse Benchmark for Referring Surgical Video Instrument Segmentation](https://arxiv.org/abs/2609.23067)

**<font color=#1a73e8>作者：</font>** Zan Wang, Yunhe Feng, Dong Nie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring surgical video instrument segmentation (RSVIS) aims at segmenting the instrument in a surgical video, given a textual description. Despite recent progress, current models are trained and assessed on relatively small-scale benchmarks, hindering the development of more general RSVIS. In addition, existing benchmarks support only the single-target expression that refers to one instrument in the video, while overlooking multi-target and no-target referring expressions, restricting the applicability of RSVIS in practical scenarios. Addressing these issues, we propose LD-RSVIS, a new benchmark aiming to facilitate more robust and general RSVIS. Specifically, LD-RSVIS consists of 3,536 surgical videos with 1.09 million frames and covers a broad set of 30 instrument classes from 25 various procedures. By including abundant videos and classes, LD-RSVIS could benefit large-scale training and evaluation of more general RSVIS methods. Besides, unlike existing datasets, LD-RSVIS offers diverse referring settings, including no-target, single-target, and multi-target expressions, which enables the development of more practical RSVIS models in real applications. In order to ensure high-quality annotations, all videos in LD-RSVIS are manually labeled with multiple rounds of inspection and refinement. To our knowledge, LD-RSVIS is the largest and most diverse benchmark for RSVIS. To analyze LD-RSVIS and to provide comparison for future research, we evaluate 12 representative methods, and the results reveal that more efforts are required for improvements. To encourage future research, we present a simple yet effective RSVIS method, dubbed Cascade-RSVIS, that first mines target-specific cues using the complementary multi-cue text information and then employs such cues and textual information for segmentation, achieving promising performance. Our benchmark and code will be released.

---


### 153. [Event Signature Transfer: Model-Agnostic Forecast Scenario Construction from Historical Events](https://arxiv.org/abs/2609.23074)

**<font color=#1a73e8>作者：</font>** Karthik Sridhar, Aaditya Jain, Murari Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasters often know an event is imminent but not the shape, size, or timing of its effect. We introduce Event Signature Transfer (EST), a training-free, model-agnostic operator that turns a completed past event into an explicit forecast scenario. EST removes a source event's own trend and seasonality, then scales and retimes the remaining event signature onto a native forecast, preserving the forecast's linked structure and reducing to it exactly at zero strength. Because it reads only output quantiles, EST applies to any quantile forecaster, with no training, no model internals, at transfer time. Across twelve real episodes and ten synthetic scenarios on Chronos-2, TimesFM-2.5 and Toto-2.0, manually configured EST reduces real-episode WQL by 21.7-90\% in-sample. On Chronos-2, it leads eleven of twelve matched comparisons against covariate conditioning, activation editing and raw replay. The operator builds a scenario; it does not estimate its likelihood.

---


### 154. [AirGC-CD: Gaussian-Circulant Precoding for Exactly Debiasable PAPR Reduction in Over-the-Air Federated Learning](https://arxiv.org/abs/2609.23084)

**<font color=#1a73e8>作者：</font>** Jonggyu Jang, Hyeonsu Lyu, Hyun Jong Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over-the-air federated learning lets edge devices transmit their local updates simultaneously, reducing the communication overhead. The resulting waveform, however, has a peak-to-average power ratio (PAPR) that grows with the model dimension, and keeping the amplifier in its linear range leaves two remedies: clipping the peaks or backing off the transmit power. Neither remedy is without cost: i) the clipping distortion appears at the receiver as a bias that cannot be removed, and ii) back-off keeps the signal intact but degrades the average signal-to-noise ratio (SNR). Independent of this trade-off, the transmission remains uncompressed, spending one channel use per model parameter, which keeps large-model training out of reach. To address these challenges, we propose AirGC-CD, an over-the-air scheme that precodes each local update with a partial Gaussian circulant matrix before clipping. In AirGC-CD, the precoder's output is exactly Gaussian regardless of the update's sparsity, so the clipping function is designed for a known distribution instead of inheriting it from the data. This enables the clipping to be inverted on average by a single scalar Bussgang gain in closed form, and we prove that the resulting aggregate is exactly unbiased, with clipping adding only variance. The clipping ratio is then the only free parameter left, trading the variance of the clipping against the SNR loss from back-off, and we derive its near-optimum in closed form. Since the precoder is linear, it also acts as a compressor, reducing the transmission from the model dimension d to the sketch dimension m at a cost of only O(dlog d) via two fast Fourier transforms, whereas a Gaussian sketch costs O(md). Experiments on five image datasets show that AirGC-CD outperforms baseline over-the-air FL schemes in most settings, particularly at low SNR, while using fewer channel uses per round.

---


### 155. [The Role of Coordinates in Pareto Regret for Adversarial Multi-Objective Bandits](https://arxiv.org/abs/2609.23092)

**<font color=#1a73e8>作者：</font>** Changkun Guan, Mengfan Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial multi-objective bandits hold the potential to help us optimize choices (arms) whose reward is a multidimensional vector chosen by an adversary and whose performance is measured by Pareto regret. We define loss as one minus reward and measure the easiness of a coordinate by the smallest cumulative loss of the arms on it, and call the coordinate easier when this quantity is smaller. Existing work suggests that in theory an easier coordinate may reduce Pareto regret. However, in practice, one may not know which coordinate is easier. On the negative side, we show that this lack of information eliminates the possibility: a smaller cumulative loss does not improve the worst-case order of Pareto regret. Precisely, let \(L_d\) be the smallest cumulative loss along coordinate $d$ over $T$ rounds. For \(K\ge4\) arms, \(T\ge6\) rounds, and at least 2 coordinates, we prove that the minimax expected Pareto regret is \(\Omega(\min\{T-L_0,\sqrt{K(T-L_0)}\})\). It is monotonically decreasing in \(L_0\), even when \(L_0=\min_d L_d\) itself is known. On the positive side, this result motivates the possibility that other coordinates, not just the easy one, may suffice to attain the optimal rate of Pareto regret. When $L_0$ is known, we apply Poly-INF to a fixed coordinate and obtain an upper bound on Pareto regret that exhibits the same order and thus matches the lower bound. Without such knowledge, we develop a reward-doubling version of Poly-INF that adapts to this unknown quantity while still attaining the matching minimax rate. Another implication is that it has no extra \(\log T\) factor and is independent of the number of coordinates.

---


### 156. [Measuring Smartphone User Experience through a Hierarchical Metric Framework via Social Media Reviews](https://arxiv.org/abs/2609.23101)

**<font color=#1a73e8>作者：</font>** Xiaoteng Pan, Mingang Lan, Chenrui Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smartphone user experience (UX) is widely expressed in user-generated online discourse across platforms, creating opportunities for in-the-wild measurement at scale. However, existing UX instruments and review-mining approaches do not provide a smartphone-oriented, theory-grounded hierarchical measurement specification that supports consistent aggregation and comparison across heterogeneous platforms. In this research, we propose a hierarchical smartphone UX measurement framework and an interpretable computational pipeline that translates cross-platform reviews into structured UX metrics. The pipeline extracts localized experience evidence units, maps them to the hierarchy via coarse-to-fine classification, and quantifies evaluations with a unified five-level satisfaction sentiment model. We apply the approach to a stratified subset of approximately 20,000 Chinese social media reviews covering four major smartphone brands across three platforms. The resulting metrics separate what users discuss, captured by normalized mention frequency, from how they evaluate it, captured by mean five-level sentiment scores. This work provides a scalable and interpretable evidence base for cross-brand comparison and metric-level interpretation beyond raw review volume or single-platform observations.

---


### 157. [When Does Adversarial Refinement Help? A Negative Result and Open Problem in Adapting R3GAN to Time Series Imputation](https://arxiv.org/abs/2609.23102)

**<font color=#1a73e8>作者：</font>** Yufeng He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models and transformers have supplanted GANs for multivariate time series imputation, largely on grounds of GAN training instability. R3GAN (NeurIPS 2024) removes that instability via regularized relativistic losses with provable convergence, raising a natural question: do stable, modern GANs revive adversarial imputation? We adapt R3GAN to 1D temporal data with a coarse-to-fine refinement framework and a frequency-domain discriminator, and audit 14 saved configurations across 3 datasets. Because these are heterogeneous single runs, the evidence is descriptive rather than a matched causal ablation. We report a negative result. All five saved mean/zero-start configurations improve by 48.4-70.2%. Among eight eligible non-legacy linear-start configurations, the mean change is -0.7% (range -3.0% to +1.1%); a separate -21.9% legacy logging anomaly is retained for provenance but excluded from that aggregate. In a saved Weather comparison, standalone R3GAN-1D underperforms BRITS by 5.8x. Crucially, we argue the common explanation (that GANs optimize distributional rather than point-wise objectives) cannot be the whole story, since diffusion models also optimize distributional objectives yet achieve state-of-the-art imputation. Our saved reconstruction-weight sweep is consistent with the adversarial signal being inert or harmful, but cannot identify its causal contribution; a matched discriminator-removed ablation is the key next experiment. We frame the precise reason a learned discriminator fails to provide useful refinement gradients (where a learned diffusion denoiser succeeds) as an open problem, and offer practical guidance on when adversarial refinement is worthwhile.

---


### 158. [Whitening Inverts the Hierarchy: What the Norm of a Whitened Embedding Measures](https://arxiv.org/abs/2609.23117)

**<font color=#1a73e8>作者：</font>** Mohammed Ahnouch, Lotfi Elaachak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whitening a foundation-model embedding and using its squared norm as a training-free likelihood surrogate is motivated by the observation that whitened coordinates often appear approximately standard normal. We show that this observation follows from the projection central limit theorem and therefore does not imply a Gaussian joint distribution. Across multiple encoders and three training objectives, we find systematic over-dispersion of the whitened radius relative to the Gaussian reference, including against distributional clones with identical mean and covariance. We further show that the commonly reported agreement between empirical and theoretical norm statistics is an algebraic consequence of in-sample whitening and does not constitute evidence for Gaussianity.
We identify the mechanism behind this behavior: whitening reverses the encoder's spectral hierarchy, shifting the contribution to the squared norm toward near-degenerate directions that encode predominantly noise. In these directions, the dominant variability is governed by a single input-dependent scale. We estimate this scale from two moments and use it to predict, without additional free parameters, the cross-dependence between disjoint spectral halves. These results indicate that the squared whitened norm is better interpreted as a Mahalanobis measure of semantic atypicality than as a log-likelihood. This interpretation explains both its practical effectiveness and its calibration failures: the statistic can rank and detect atypical samples consistently with nonparametric density estimates and across encoders trained with different objectives, while Gaussian tail thresholds can be inaccurate by orders of magnitude. etc.

---


### 159. [MM-ContextFold: Context Folding for Multimodal Agentic Retrieval](https://arxiv.org/abs/2609.23121)

**<font color=#1a73e8>作者：</font>** Yang Tian, Fan Liu, Jingyuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Agentic Retrieval (MAR) requires agents to solve complex information-seeking tasks by iteratively invoking external tools. Typical frameworks such as ReAct maintain raw multimodal inputs and the accumulating interaction history in a single, ever-growing context, leading to the context explosion problem. While existing methods alleviate this issue by compressing redundant text, effective strategies for managing token-intensive visual content remain largely underexplored. To address this gap, we first conduct a systematic empirical study of approximately 10,000 trajectories. The results show that as visual cues are progressively extracted through external tools and textualized into the context, raw images become increasingly redundant. Continued image retention is associated with higher output entropy and can even degrade task accuracy. Motivated by these findings, we propose MM-ContextFold, a training-free framework that loads raw images only when needed. It maintains a persistent, text-only main context for high-level planning and spawns ephemeral branch contexts for image-dependent subtasks. Within each branch, the agent loads the relevant images, completes the subtask, and folds the result back into the main context as a concise textual summary; the images and branch trace are then discarded. Experiments on seven MAR benchmarks across five backbone models show that MM-ContextFold improves average accuracy by 6.3 percentage points over ReAct while reducing the working context length by 27.5\%.

---


### 160. [Perplexity Cost Understates What Activation Quantisation Breaks](https://arxiv.org/abs/2609.23125)

**<font color=#1a73e8>作者：</font>** Anish Sathyanarayanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation quantisation is usually evaluated with an aggregate metric, perplexity, averaged over every token a model predicts. We ask whether that average identifies which computations a quantiser damages. Perplexity turns out to be a reliable aggregate signal: across 12 models from four families and 780 within-model comparisons, the arm perplexity prefers also retains more induction and more retrieval in all but 2.1 and 4.0 percent of cases respectively. But where perplexity has risen by only a factor of 1.2 to 1.5, induction still keeps 0.959 of its intact accuracy while retrieval has already fallen to 0.554, a gap the aggregate number does not surface. This gap has structure, not just size: a matched Gaussian-noise control of the same per-channel magnitude leaves it largely intact, and randomising only the sign of the quantisation error, every magnitude held fixed, is nearly as harmless, so magnitude alone does not explain the damage. Quantising in a rotated basis, which changes coordinate alignment without changing error magnitude, restores induction from 0.001 to 0.980 at three average bits per token in a single-block intervention, though retrieval recovers less completely at the same setting (0.694); end-to-end at four average bits, induction reaches 0.968 and retrieval 0.534. The pattern holds on two further models up to 32B parameters and, in the deployed configurations we tested, under AWQ once activations are pushed to 4 bits. A perplexity target bounds the average cost of a transformation applied to the activation; it does not, by itself, show which computations survived.

---


### 161. [Provably Efficient Reinforcement Learning in Continuous-Time Episodic MDPs with Poisson Decision Epochs](https://arxiv.org/abs/2609.23127)

**<font color=#1a73e8>作者：</font>** Kenny Guo, Valentio Iverson, Sahan Wijetunga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world reinforcement learning (RL) problems evolve in continuous time, where decisions occur at irregular, event-driven intervals rather than at fixed discrete steps. We study episodic continuous-time Markov Decision Processes (MDPs) in which decision epochs are governed by a homogeneous Poisson process and the reward and transition dynamics vary smoothly over time. We consider both a fixed number of jumps per episode and a fixed time budget with a random number of Poisson decision epochs. Under a Lipschitz continuity assumption in time, we exploit local smoothness through discretization and extend both UCRL (Auer and Ortner 2006) and Q-learning (Jin et al. 2018) to this setting, proving $\widetilde{O}(T^{2/3})$ regret bounds for both model-based and model-free algorithms. Finally, we establish matching $\widetilde{\Omega}(T^{2/3})$ minimax lower bounds, showing that the rate is optimal up to logarithmic factors. These results provide the first tight regret guarantees for Lipschitz-smooth continuous-time episodic MDPs with Poisson decision epochs.

---


### 162. [Evaluative Dynamics of AI Integration and Expert Performance under Epistemic Dependence across Heterogeneous Stakes](https://arxiv.org/abs/2609.23135)

**<font color=#1a73e8>作者：</font>** Dennis Kim, Roya Daneshi, Nikhil Krishnaswamy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI is increasingly integrated into expert workflows, yet how integration affects perceptions of the expert, AI, and their combination remains unclear in domains where lay users are epistemically dependent on AI-assisted experts. We examine this through a novel controlled medical study (N = 166) and a direct cross-domain analysis with pre-existing academic-advising data (n = 157, combined N = 323). Expert errors reduced evaluations of the human expert across domains. Perceived expertise, however, varied by AI integration strategy in the higher-stakes medical task, where automatic AI oversight produced higher ratings than expert-only or expert-initiated AI. Exploratory ordinal sensitivity analyses identified a performance-contingent reuse pattern, with automatic oversight producing greater intended reuse after successful medical performance. Overall, performance-related recalibration appeared comparatively portable, while integration-structure effects were more selective and context-sensitive. These findings suggest that system designers should consider how AI enters expert workflows, not only whether it is present.

---


### 163. [SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](https://arxiv.org/abs/2609.23153)

**<font color=#1a73e8>作者：</font>** Yuxi Liu, Haoyu Li, Zekun Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers are expensive because attention dominates long spatiotemporal token sequences. We identify the \emph{high-sparsity trap}: at extreme attention sparsity, step-local training losses keep decreasing while terminal generation quality stagnates or degrades. The trap is one of supervision: the dominant terminal errors originate in the high-noise structure-generation stage, and terminal-aligned training corrects terminal errors that substantially extended step-local training cannot. This yields a simple staging principle: \emph{first adapt the sparse architecture into a coarse prior, then correct the terminal distribution}. We instantiate the principle as \method, a unified acceleration framework for visual generation that combines a short sparse warm-up, few-step trajectory-mixed distillation, and FP8 quantization with fused kernels. \method sustains $97\%$ attention sparsity with strong visual quality on long-sequence 720P generation across Wan2.1/Wan2.2 backbones and T2V/I2V tasks, and $90\%$ sparsity on Wan2.1-T2V-1.3B-480P. With 3-step CFG-free inference, \method achieves a $265\times$ end-to-end speedup over the 50-step CFG dense baseline for Wan2.1-T2V-14B-720P on a single RTX~5090 ($220\times$ on H100), and denoises a Wan2.1-T2V-1.3B-480P video in $1.3$s.

---


### 164. [An Eternal Irradiance Camera](https://arxiv.org/abs/2609.23161)

**<font color=#1a73e8>作者：</font>** Jeremy Klotz, Shree K. Nayar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A conventional camera uses millions of pixels to measure radiance from all directions within its field of view. We present an omnidirectional irradiance camera that measures the irradiance function---the illumination incident upon every point on a sphere. The irradiance function varies smoothly over the sphere and hence is bandlimited. We have analyzed this function in the frequency domain and have shown that it is well approximated by a weighted sum of the first seven degrees of spherical harmonics. As a result, the irradiance function can be accurately reconstructed from a small number of samples. This implies that an irradiance camera does not need millions of detectors (pixels)---just a handful of measurements suffice. This brings two major benefits. First, the camera consumes such little energy that it can be completely powered by the light falling on its detectors. Second, it does not capture the visual details needed to identify an individual, and hence privacy is preserved. We have built a prototype irradiance camera, called FluxCam, using 49 detectors arranged on the surface of a sphere. In a well-lit indoor environment, FluxCam can read out and wirelessly transmit its measurements at 30 frames per second using energy harvested from the light falling on it (i.e., without a battery, cable, or external power supply). We show how FluxCam can be used as an optical gyroscope for computing rotation, to monitor a workspace, as an untethered light probe for diffuse relighting, and as an omnidirectional pyranometer for estimating sky conditions and determining the best orientation of a solar panel.

---


### 165. [UltraTex: Unleashing 2K Multi-View Diffusion for 3D Texturing](https://arxiv.org/abs/2609.23169)

**<font color=#1a73e8>作者：</font>** Yibo Zhang, Ze Yuan, Nan Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality texture generation is essential for creating realistic and production-ready 3D assets. Recent multi-view diffusion methods have shown promising results for image-guided 3D texturing, but they are typically constrained to low operating resolutions such as 512 or 768, making it difficult to preserve high-frequency details from high-resolution reference images. Scaling this paradigm to 2048 resolution is computationally prohibitive, as the unified multi-view sequence exceeds 212K tokens and incurs excessive memory and latency. In this paper, we present UltraTex, an efficient end-to-end framework for high-resolution multi-view diffusion-based 3D texturing. Our key observation is that object-centric multi-view renderings contain two major sources of redundancy: background-induced sequence redundancy and sparse token interactions within the foreground. To address them, we introduce Background Token Dropping, which removes background tokens before the DiT backbone, and Block-Sparse Attention, which reduces attention computation over the retained foreground sequence. To enable efficient foreground-only inference while avoiding reconstruction artifacts, we further design Foreground-Aware VAE Decoding to ensure the quality of the final high-resolution views. To satisfy the demanding data requirements of 2K-resolution multi-view diffusion training, we construct G-buffer TexVerse, a large-scale, ultra-high-resolution multi-view rendering dataset covering over 268,000 3D assets. Extensive experiments show that UltraTex generates visually faithful textures with rich fine-grained details, while substantially improving efficiency, achieving $20.6\times$--$91.1\times$ training speedup and $22.3\times$--$74.6\times$ end-to-end inference speedup over the baseline on common samples in our dataset. Code and data is at this https URL.

---


### 166. [Exploiting Software-level Abstractions To Support Practical Hardware Trojan Attacks](https://arxiv.org/abs/2609.23173)

**<font color=#1a73e8>作者：</font>** Athanasios Moschos, Kevin Valakuzhy, Georgios Kokolakis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware trojan (HT) attacks against CPUs typically assume threat scenarios where an attacker targeting a system with a trojanized CPU is able to execute arbitrary code (i.e. machine-level instructions) to reliably interact with the implanted trojan. On end-user devices (i.e., mobiles, laptops), achieving arbitrary code execution in practice requires software exploits tailored to each specific target. Such strong adversarial premises reduce the generality of existing threat models casting doubt on CPU trojan attacks as a pragmatic threat vector. To push the envelope on HT attacks against client devices, we introduce the SURF class of CPU-trojans that can be activated without arbitrary code execution. Our key insight is that integer operations expressed in a high-level language can be mapped to microarchitectural side-effects distinguishable by a SURF trigger circuit. This observation unlocks HT activation via runtime engines, constrained environments executing untrusted high-level code. We demonstrate a SURF trojan inside a RISC-V processor and exploit JavaScript-level memory indexing operations inside Google's V8 engine to perform a code injection attack. Importantly, we show that SURF trojans remain effective across multiple JavaScript engine versions, enabling long-term compromise of endpoint devices. To facilitate research, we opensource SURF's design and supporting software.

---


### 167. [GrapeSplat: Geometry-Grounded Reconstruction via Amalgamated Pose-Free Encoding for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2609.23182)

**<font color=#1a73e8>作者：</font>** Si-Yu Lu, Yung-Yao Chen, Yi Jan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting now reconstructs renderable scenes from unposed, uncalibrated images. Yet, most models supervise only photometric consistency and predict Gaussians pixel by pixel, which leaves global structure fragile and ties primitive count to image resolution and view count. To this end, GrapeSplat amalgamates multi-view cues into a voxel-aligned scene representation and decodes Gaussians directly from the learned grid, requiring no per-scene optimization or post-processing. An Atlas Encoder lifts all views into pixel-wise geometry-and-appearance features anchored at predicted 3D points. PEACH-Vox compands the unbounded scene into a bounded sparse grid through a smooth per-axis map with an exact closed-form inverse. The Sparse Decoder then consolidates the grid with sparse convolutions and decodes the full scene as multiple Gaussians per occupied cell. This amalgamated representation exploits sparse voxel occupancy, where the Gaussian count follows the occupied cells and saturates as views cover the scene, while grid resolution sets its ceiling. GrapeSplat turns unposed images into a renderable Gaussian scene in a single forward pass. Trained with 2D and 3D supervision on 8-view sequences, it generalizes zero-shot from 4 to 64 views across indoor and unbounded scenes. Code and trained weights are available at this https URL

---


### 168. [K-TRAIL: Simulator-Guided Generative Design of EM/RF Circuits](https://arxiv.org/abs/2609.23183)

**<font color=#1a73e8>作者：</font>** Piyush Saha, Evan Newell, Hanna O'Leary 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design of RF and electromagnetic (EM) circuits is challenging because the relationship between circuit layout and electrical response is non-unique, and full-wave simulation is computationally expensive. This paper presents K-TRAIL, a simulator-guided generative framework for automated EM/RF circuit synthesis. K-TRAIL combines diffusion-based layout generation with derivative-free ensemble Kalman guidance, allowing feedback from a black-box EM simulator to refine candidate layouts during generation without requiring adjoint sensitivities or differentiable solver models. The framework supports both synthesis from prescribed S-parameter responses and synthesis directly from RF performance constraints. Experiments on multi-layer RFIC structures show that simulator-guided generation improves agreement with target responses and can identify structurally distinct layouts that satisfy circuit-level design requirements. The proposed approach provides a practical path toward generative, verification-aware RF circuit design while retaining the flexibility to explore diverse layout topologies.

---


### 169. [Neural Residual Modeling for Scientific Data Compression under Guaranteed Error Bounds](https://arxiv.org/abs/2609.23185)

**<font color=#1a73e8>作者：</font>** Surya Majumder, Liangji Zhu, Sanjay Ranka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lossy compression of scientific simulation data increasingly relies on learned, latent-space architectures such as Residual Vector Quantization (RVQ), which iteratively quantize a base representation and its residuals to progressively reduce reconstruction error. While effective, RVQ performs this residual modeling entirely in latent space, leaving the pixel-space error structure of the reconstruction largely unaddressed. In this work, we propose a post-processing pipeline that augments an RVQ-based compressor with a U-Net trained to predict and correct pixel-space residuals between the original volume and its RVQ reconstruction. We show that these residuals are spatially structured rather than driven by local intensity or gradient features, motivating the need for a deep spatial model rather than simple statistical correction. The U-Net-corrected reconstruction is then passed through a Guaranteed Autoencoder (GAE) stage, which projects the remaining residual onto a per-block PCA basis to enforce a user-specified block-wise error bound. To the best of our knowledge, this is the first pipeline to combine latent-space RVQ, explicit pixel-space residual correction via a deep spatial post-processing network, and GAE-based error-bound guarantees within a single framework for scientific data compression. We evaluate our approach on S3D, JHTDB and E3SM datasets, demonstrating consistent improvements in NRMSE, compression ratio] over RVQ-only and standard residual-correction baselines, while maintaining strict error guarantees required for scientific data fidelity.

---


### 170. [Assessing Runtime Electromagnetic Detection of CPU Hardware Trojans Targeting Kernel Memory](https://arxiv.org/abs/2609.23186)

**<font color=#1a73e8>作者：</font>** Athanasios Moschos, Baki Berkay Yilmaz, Kevin Valakuzhy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Side-channels are a promising approach for hardware trojan detection, as they can passively reveal malicious hardware activity without requiring additional circuitry or destructive analysis of the device under test. This work investigates the use of electromagnetic (EM) emanations for runtime detection of hardware trojan attacks. Using an open-source hardware trojan that implements an arbitrary memory-write primitive, we tamper with the kernel memory of a Linux system running on a RISC-V microarchitecture and perform a real-time baseline detection using the processor's EM emissions. Our results indicate that, under certain conditions, hardware trojans can be detected indirectly through the anomalous software behavior they enable.

---


### 171. [Low resource cross-modal alignment using HGNN to enhance speech representation](https://arxiv.org/abs/2609.23191)

**<font color=#1a73e8>作者：</font>** Yannick Yomie Nzeuhang, Marie Tahon, Paulin Melatagia Yonta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-text space alignment is a multimodal representation learning method consisting to map different speech and text into a shared representation space, leading to enrichment of the representation of each modality. Proposed architectures, such as SAMU-XLSR, typically follow a student/teacher framework, with the goal of fine-tuning an audio encoder to produce representations that closely match those of the text. In this way a speech representation is semantically enriched. However, such systems generally require large amounts of training data and considerable computational resource, making them difficult to apply to low resources languages under frugal constraints. The present work proposes a data-efficient space alignment method based on Heterogeneous Graph Neural Networks and link prediction. The core idea is to leverage message passing to explicitly transfer information from the text modality to the speech modality, thereby reducing the need for large training datasets and intrinsically enriching the acoustic representations, all in a more interpretable manner. Although thoroughly explored for high-resource languages, word-level tasks in speech remain relevant for certain low-resource languages. Therefore, we conducted experiments on speech-text alignment at the word level using the TIMIT (English) dataset and Yemba (a Cameroonian language). Our approach yields results comparable to those of SAMU-XLSR, a state-of-the-art method, and even surpasses it for the Yemba language in the task of word retrieval, while using far fewer resources, demonstrating its power, frugality, and efficiency.

---


### 172. [Enhancing speech representation learning with cross-modal knowledge transfer with HGNN under low resource settings: the case study of Yemba](https://arxiv.org/abs/2609.23194)

**<font color=#1a73e8>作者：</font>** Yannick Yomie Nzeuhang, Paulin Melatagia Yonta, Marie Tahon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Acoustic representation learning is crucial for speech processing, yet low-resource languages (LRLs) face severe data scarcity, limiting the effectiveness of traditional and self-supervised methods. As a promising alternative, in this work, we propose to enhance acoustic representation trough a cross-modal transfer knowledge approach, based on heterogeneous graph neural networks (HGNNs), where acoustic and linguistic entities are modeled as distinct node types within a unified graph. Through message-passing mechanisms, linguistic nodes explicitly transfer knowledge to acoustic nodes, enabling structured and interpretable cross-modal information flow. To highlight this knowledge transfer and its benefits, we measured standard clustering metrics as an intrinsic evaluation of acoustic representation, and to emphasize applicability, we performed isolated-word recognition tasks using an English benchmark and a Cameroonian language dataset in low resources settings . Results demonstrate that acoustic representations consistently benefit from linguistic knowledge propagated through the graph. To our knowledge, this is the first demonstration of explicit cross-modal knowledge transfer for acoustic representation learning using HGNNs, highlighting a promising direction for speech representation in low-resource settings.

---


### 173. [SoK: From Finding to Deployment: Systematizing the OS Kernel Bug Lifecycle](https://arxiv.org/abs/2609.23218)

**<font color=#1a73e8>作者：</font>** Luyao bai, Gengda She, Kenan Alghythee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated kernel bug discovery has advanced rapidly. Continuous fuzzing and static analysis systems, such as syzbot, now expose Linux kernel bugs at a scale that downstream processes struggle to absorb. Yet a crash report is only the beginning. Before a bug is eliminated, it must be triaged, understood, patched, validated, reviewed, integrated, and often backported. These later stages remain far less automated, creating a persistent gap between bug discovery and patch deployment.
This SoK systematizes the Linux kernel bug lifecycle from discovery to deployment. We organize prior work and production systems into five stages: discovery, triage, patch generation, patch validation, and integration. We explain the resulting automation gradient through kernel-specific challenges such as concurrency, implicit invariants, cross-syscall state, hardware dependence, lack of fault isolation, and architecture/configuration multiplicity. We further ground the analysis in a measurement of real syzbot-fixed bugs. The data shows that the crash-to-patch gap is not merely a backlog of unfixed reports but a structural failure mode of the repair pipeline: even after being fixed, bugs often remain open for weeks, require review-driven patch revisions, or lack reproducers that current repair and validation systems assume. This exposes a mismatch between where kernel-security automation is mature and where bug closure actually breaks down. These findings expose a deeper mismatch: today's repair and validation techniques often assume reliable reproducers, localized root causes, and checkable correctness oracles, yet these are precisely the artifacts missing from many real kernel bug reports. Closing the crash-to-patch gap, therefore, requires treating such artifacts as outputs to be produced, not prerequisites to be assumed.

---


### 174. [Causal Inference with Unobserved Confounding: A Mixture Learning Perspective](https://arxiv.org/abs/2609.23219)

**<font color=#1a73e8>作者：</font>** Mansi Sood, Devavrat Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unobserved confounding is a fundamental challenge in causal inference from observational data. This article develops a mixture-learning perspective, viewing latent confounders as sources of heterogeneity that induce mixture structure in observed data. Under suitable structural and identifiability assumptions, recovering the mixing distribution and component mechanisms enables estimation of interventional distributions and causal estimands. Using variants of Bernoulli mixtures as a running example, we contextualize mixture-learning techniques and their structural assumptions, and connect them to causal inference in panel-data settings, including latent factor models and synthetic this http URL then consider high-dimensional exponential-family mixtures with dependent outcome trajectories, moving beyond counterfactual means to model counterfactual distributions. We situate this perspective relative to complementary approaches for unobserved confounding. Together, these ideas provide a bridge between mixture learning and causal inference, connecting recent advances in high-dimensional mixture learning to scalable identification and estimation of causal effects while raising new challenges for mixture learning.

---


### 175. [Security of Agent-Integrated Software: When Human Operations and Agent Actions Coexist](https://arxiv.org/abs/2609.23226)

**<font color=#1a73e8>作者：</font>** Ding Yang, Yuchen Ling, Shengcheng Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent-Integrated Software (AIS) embeds an intelligent agent in a conventional application, supporting both human operations and agent actions. Human operations let users make precise changes and inspect results, while agent actions carry out routine or multi-step tasks. These complementary roles make coexistence a likely long-term feature of many software systems. Human operations and agent actions affect the same software state and can use one another's results. Therefore, security policies must remain effective across both paths. We argue that AIS security must be assessed at the level of the whole software system. Protecting the agent and the conventional software core separately does not establish that they are secure together. To guide security analysis of AIS as a whole, we organize the problems arising from this coexistence into four categories: context misuse, authorization violation, execution control, and effect integrity. Using these categories, we examine how current practices address the security problems in AIS and where their protection remains limited. Building on this analysis, we identify research opportunities in preserving information provenance, enforcing policy across operation paths, maintaining valid authorization over time, and managing persistent effects and recovery. This resulting perspective provides a conceptual framework for understanding and improving the security of AIS.

---


### 176. [ChemCLIR-Bench: Benchmarking Cross-Lingual Information Retrieval in Multilingual Chemical Patents](https://arxiv.org/abs/2609.23231)

**<font color=#1a73e8>作者：</font>** Mahdi Astaraki, Mohammad Khodadad, Reza Namazi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual information retrieval (CLIR) is increasingly important in multi-national industries, where critical technical evidence may exist in a different language than the query. However, existing benchmarks do not adequately capture domain-specific cross-lingual retrieval or the retrieval-depth and recoverability failures that aggregate recall hides.
In this work, we benchmark CLIR in the chemical domain, with a focus on patent data. We construct a multilingual dataset from Google Patents and the European Patent Office (EPO) data, spanning five languages (covering major Eastern and Western languages) and reflecting the diversity and complexity of real-world industrial documentation.
Using this dataset, we systematically evaluate eight state-of-the-art embedding models for cross-lingual retrieval. Our results show a substantial performance gap between monolingual and cross-lingual settings: for the best-performing model, Recall@10 drops from 0.72 to 0.53 in cross-lingual setting. Retrieval depth also degrades significantly, with relevant documents ranked lower across languages in cross-lingual scenarios. Furthermore, some multilingual embedding models that perform strongly in monolingual settings exhibit sharp declines when queries and documents are in different languages, providing practical insights for model selection in cross-lingual use cases.
These findings highlight critical limitations of current approaches and emphasize the need for more robust cross-lingual retrieval methods in domain-specific settings. Our benchmark provides actionable insights for model selection and establishes a controlled diagnostic evaluation framework for CLIR over industrial technical text. Data and code are publicly available at this https URL.

---


### 177. [SoK: Formal Methods for Fact-Checking and Information Integrity](https://arxiv.org/abs/2609.23239)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Theodoros Nestoridis, Charalampos Bratsas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An automated fact-checking system returns a label: the claim is true, or it is false. In many such systems the verdict remains the primary output. What is generally missing is a record of which document settled the question, of what would have had to be different for the verdict to change, or of whether the same claim, reworded, would have been judged the same way. We call the missing piece a warrant: a separate statement of what was guaranteed and on what grounds. Formal methods produce evidence of this kind, and regulation is beginning to ask for it, since the Digital Services Act and the AI Act both call for auditable evidence about how systems behave. Surveys of automated fact-checking are usually organised by pipeline stage, and treat logic as one technique among many. We organise the field by what is being formalised instead, which gives five levels: the claim, the reasoning, the system doing the checking, the ecosystem the claim spreads through, and the regulatory obligation. Sorting 121 works into those levels, two patterns stand out. Most of the relevant formal machinery already exists, but it was built for other domains and has rarely been applied here, and the gap is widest for verifying the checking system itself. Several stages of the routine professional fact-checkers follow also have no stated correctness criterion, and two of them, writing a claim in checkable form and correcting a verdict already published, are not formally specified in any work we coded. We close with open problems, each with a suggested first step.

---


### 178. [Proximal Residual Value Functions for Consistent Planning and Real-Time Execution](https://arxiv.org/abs/2609.23242)

**<font color=#1a73e8>作者：</font>** Harrison Waldon, Carson Eisenach, Akhil Bagaria 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study two-timescale decision systems in which a planning layer periodically supplies a continuation-value function to a real-time optimizer that allocates arriving resources, with inventory placement as our motivating application. We propose an end-to-end reinforcement learning (RL) method for learning this function using \emph{proximal residual value functions}, which combine a strictly convex potential of post-decision inventory with a learned convex residual. This general form yields a well-posed optimization layer that supports end-to-end differentiation while preserving an explicit convex objective for real-time execution. We characterize the necessary and sufficient conditions under which a smooth value function yields decisions that are consistent across the planning and execution timescales. In an offline simulation using historical inventory arrival and demand patterns from a large e-commerce retailer, learned proximal residual value functions reduce total routing and transfer cost relative to a historical-production-system proxy by 5.0%.

---


### 179. [SPACE: Semantic Projection and Alignment of CLIP Embeddings for Domain Adaptation](https://arxiv.org/abs/2609.23248)

**<font color=#1a73e8>作者：</font>** João Renato Ribeiro Manesco, Danilo Samuel Jodas, Douglas Rodrigues 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in deploying vision models is domain shift, which arises when training and test data follow different distributions, leading to degraded performance. This challenge is amplified when the same semantic concept appears under distinct visual forms, such as photographs and sketches, where visual similarity is weak despite semantic correspondence. Existing unsupervised domain-adaptation methods aim to align distributions across domains but often ignore semantic relationships among samples of the same class. To address this issue, this paper introduces SPACE, a method that exploits the semantic structure of CLIP's vision-language space for domain adaptation. The key idea is to use text descriptions as semantic anchors by applying Singular Value Decomposition to CLIP embeddings of class descriptions, yielding an orthogonal basis that captures semantic relationships among categories. Visual features from both domains are projected into this semantic subspace, aligning images based on meaning rather than appearance.

---


### 180. [Exact Quotients of Fresnel-Kummer Surfaces and Certified Biaxial Refraction](https://arxiv.org/abs/2609.23249)

**<font color=#1a73e8>作者：</font>** Tanush Shaska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Fresnel wave surface governs the propagation of light in a transparent biaxial crystal. It is a special Kummer quartic, and we identify it exactly. Over the complex numbers the wave surface of a crystal is the Kummer surface of the Jacobian of an explicit genus-two curve branched at the signed square roots of the three principal permittivities. This Jacobian is isogenous, by an isogeny with kernel of order four, to a product of two elliptic curves. One elliptic curve carries the three permittivities, and the other carries the optic-axis angle. The physical family is Zariski dense in the locus of genus-two curves with an extra involution, and its automorphism strata are explicit. The identification instantiates a task-aware quotient, which identifies parameters that differ by a nuisance transformation and carries invariant coordinates and explicit strata. For biaxial crystals, two ratios of the permittivities form a complete invariant of the wave surface up to rotation and rescaling, and the four real nodes are given in closed form. At an interface the candidate transmitted waves are the roots of a quartic of exact degree four. Its real-root count, root order, and repeated-root events are decided by exact algebraic predicates, and along the generic single-node encounters of the paper its discriminant vanishes to second order. Floating-point solvers drop forward transmitted modes near the optic axes, and the certified solver does not. On exact equivalence classes, learned models on quotient coordinates are invariant and more accurate than models on raw tensors, while learned root-count predicates fail near the optic axes.

---


### 181. [The Price of Self-Calibration: Exact Evidence Budgets and Manufactured Blind Sets in Adaptive Monitoring](https://arxiv.org/abs/2609.23254)

**<font color=#1a73e8>作者：</font>** Abdou-Raouf Atarmla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-calibrating monitors adapt their threshold online to guarantee a prescribed long-run false-alarm rate under arbitrary drift. We compute the price of that guarantee, stating every law with its exact domain of validity. First, the guarantee is an accounting identity, insensitive to what the monitor is meant to detect. Two evidence identities make the cost exact for the online quantile tracker: a persistent step of height $\delta$ yields excess alarm mass within one alarm of $\delta/\eta$, and exactly $\delta/\eta$ pathwise when $\delta$ is a lattice multiple of the gain $\eta$; a ramp of slope $c$ yields a stationary excess rate of exactly $c/\eta$, independent of accumulated size, up to a boundary $c=\eta(1-\alpha)$ coinciding with the alarm-rate cap. Second, the certificate's own fluctuation obeys an exact law: the windowed alarm rate has standard deviation of order $1/L$, not the binomial $1/\sqrt{L}$, since the windowed mass telescopes to a difference of a tight internal state; the closed-form constant is validated with no fitted parameter. Detectors calibrated on the binomial scale are miscalibrated by $\sqrt{\eta\varphi(q_0)L}$, and correct calibration turns detection windows from quadratic to linear in the inverse fault speed. Third, any monitor required to tolerate a drift class $\mathcal{D}$ is blind, at any horizon and for any rule, to every fault in $\mathcal{D}-\mathcal{D}$; the proof is a deliberately elementary two-point argument and the contribution is the object it identifies: for speed-bounded classes the blind set is exactly the doubled-speed class, and the tracker absorbs a speed class fixed by its own gain, so that under a certification regime declaring absorbed drift normal, the monitor manufactures $\mathcal{D}$. An exact Gaussian projection bound, sharper than Pinsker and never vacuous, quantifies power outside it.

---


### 182. [Why Ghost Outputs Teach: A Kernel-Based Understanding of Subliminal Learning](https://arxiv.org/abs/2609.23260)

**<font color=#1a73e8>作者：</font>** Zhe Li, Bicheng Ying, Chaosheng Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal Learning (SL) is a recently identified phenomenon in which a student model acquires downstream task capabilities by matching seemingly unrelated auxiliary outputs from a teacher, despite never observing task labels, task-specific outputs, or the original training data. While recent studies have identified where subliminal signals may reside, the optimization mechanism underlying this phenomenon remains poorly understood. In this work, we provide a mechanistic understanding of SL through the lens of learning dynamics. Specifically, we derive a chained cross-task kernel that explicitly links ghost-output supervision to changes in task predictions through shared backbone representations. Our unified analytical framework provides a rigorous mathematical explanation for three central empirical puzzles in SL: (i) under shared initialization, the transfer operator forms a strictly Positive Semi-Definite (PSD) structure, guaranteeing that ghost-output optimization aligns the student with the teacher's true task objective without explicit label exposure; (ii) the ghost-output dimensionality acts as an explicit rank bottleneck governing the transfer of task-relevant features; and (iii) synthetic, high-entropy inputs function as broadband probes that maximize cross-task kernel overlap, explaining why random noise consistently outperforms structured data for subliminal transfer. Experiments on the canonical ghost-output setting validate all three theoretical predictions, providing the first learning-dynamics-based theoretical explanation of how ghost-output supervision gives rise to subliminal learning.

---


### 183. [Optimal No-Regret Learning for Repeated Prophet Inequality](https://arxiv.org/abs/2609.23265)

**<font color=#1a73e8>作者：</font>** Kun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study repeated prophet inequalities under prefix feedback. In each of $T$ rounds, a learner encounters fresh values drawn independently from $n$ boxes with unknown $[0,1]$-supported distributions in a fixed order and must irrevocably accept one, observing only the prefix up to its stopping box. Regret is measured against the optimal stopping policy that knows the distributions. We give an efficient algorithm achieving $\widetilde O(\sqrt{T})$ expected regret, matching the lower bound up to logarithmic factors. Our algorithm explores directly through near-optimal policies, combining empirical backward induction with box-specific reach bonuses. A relative-drop aggregation rule then exploits the nesting structure of observed prefixes to preserve exploration, thereby removing the polynomial dependence on the box number $n$. This resolves an open question posed by Liu et al. (2025).

---


### 184. [Knowing When to Trust Images: Reliability-Aware Multi-modal Entity Alignment](https://arxiv.org/abs/2609.23267)

**<font color=#1a73e8>作者：</font>** Chenxiao Li, Yunhe Feng, Dongfang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The visual modality, i.e., images, plays a key role in multi-modal entity alignment (MMEA). Existing approaches often directly fuse the image with other modalities to align different entities. Although simple, such strategies overlook the potential noise in the images and their semantic misalignment with corresponding entities, resulting in suboptimal fusion and degraded performance. Addressing this, we propose a novel Reliability-Aware framework for MMEA (RA-MMEA), which assesses visual reliability and adaptively improves unreliable visual representations for robust entity alignment. The core lies in two modules, including dependency-aware visual reliability prediction (DA-VRP) and stability-regularized visual embedding generation (SR-VEG). The former aims to estimate the reliability of an image by leveraging multi-modal dependency within the entity, while the latter focuses on producing alternative visual representation conditioned on semantics encoded in textual modalities for multi-modal fusion. Compared to current methods, RA-MMEA enables more reliable visual representations for modality fusion, thereby improving performance. In extensive experiments, RA-MMEA achieves state-of-the-art results, verifying the importance of reliable visual modality for entity alignment and the effectiveness of RA-MMEA. The code and results will be released.

---


### 185. [Blind Deconvolution of Binary and Pattern Images with Pixel Intensity Constraints and Sparse Gradient Prior](https://arxiv.org/abs/2609.23268)

**<font color=#1a73e8>作者：</font>** Qinghua Zhang, Xuesong Yang, Liangtian He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image deconvolution (BID) is a prominent research topic in the field of imaging sciences, given its significant practical applications. Most existing model-based BID methods focus on natural images, incorporating appropriate prior knowledge about both the underlying image and the blur kernel. However, for certain classes of images, such as barcodes, text, and patterns, pixels can only take very limited values, a specific prior that is often overlooked in the literature. In this article, we introduce a novel pixel intensity constraint to leverage this important information, improving recovery performance for these specialized image classes. Specifically, we propose a unified framework for blind binary and pattern image deconvolution that incorporates both the pixel intensity constraint and a gradient sparsity regularizer. Numerical experiments demonstrate that our method outperforms many existing BID techniques, achieving superior results in terms of both visual quality and quantitative metrics.

---


### 186. [RegVGGT: Sustainable Visual Geometry Grounding for Streaming via Regulated Memory](https://arxiv.org/abs/2609.23286)

**<font color=#1a73e8>作者：</font>** Hongbo Mao, Junjun Jiang, Youyu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction from a lengthy video stream input poses a dilemma for feed-forward reconstruction models (FFRMs), that a whole-stream inference context cannot be retained under limited GPU this http URL studies seek to resolve this problem via a trade-off between the integrity of inference context and GPU memory usage, which either suffer from a rapid memory inflation or degraded context integrity due to artificially capping memory this http URL by our key observation that the initial saliency of a token reliably dictates its long-term importance across the stream, we propose RegVGGT, a training-free token regulation method which aggressively regulates the tokens of incoming this http URL admitting at most 1% of tokens per frame to update the context memory, our method dramatically suppresses memory inflation as the stream this http URL with a FlashAttention-compatible token saliency estimation scheme, RegVGGT is capable of processing thousands of frames on a consumer-grade GPU with negligible compromise to reconstruction this http URL experiments demonstrate that RegVGGT achieves state-of-the-art performance on long-horizon benchmarks across diverse FFRM prediction tasks, surpassing prior FFRM-based stream reconstruction baselines by a large margin.

---


### 187. [Expansion Counts under Standard A* Tie-Breaking Strategies on the Final Plateau](https://arxiv.org/abs/2609.23293)

**<font color=#1a73e8>作者：</font>** Alex Fukunaga  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the A* search algorithm, the tie-breaking strategies for nodes with the same $f$-value determines which states A* expands on the final $f$-layer. For nine standard tie-breaking strategies, we show that under a consistent heuristic, every pair has positive-cost instances favoring each strategy over the other by an arbitrarily large additive expansion gap. A parameterized unit-cost grid example also gives unbounded expansion-count ratios between low-$h$ with FIFO and LIFO. In unit-cost search with $h > 0$ at non-goals, exact heuristic values near the goal lead to complementary extremal results: low-$h$ minimizes the number of remaining expansions from a common configuration within the perfect region, while high-$h$ maximizes the total number of expansions when every final-plateau state with $h=1$ is a goal predecessor. Finally, with the evaluation function $f_{\alpha} = g + \alpha h$, when $h>0$ at non-goals, every heuristic weight $0 \leq \alpha<1$ eliminates tie-breaking sensitivity, and all tie-breaking strategies expand the same set of states.

---


### 188. [Optimal Multi-way Decision Trees for Stratified Sampling in Online Controlled Experiments](https://arxiv.org/abs/2609.23308)

**<font color=#1a73e8>作者：</font>** Tomoka Takei, Shunnosuke Ikeda, Yuichi Takano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online controlled experiments, or A/B tests, are widely used to estimate causal effects on digital platforms. A central challenge is to improve experimental sensitivity, or statistical power, without increasing the experimental sample size. Stratified sampling is a classical variance reduction technique; however, its effectiveness depends critically on how the strata are constructed. We thus propose an optimization-based stratification framework for stratified sampling using optimal multi-way decision trees. Our method, called Optimal Multi-way Stratification Trees (OMST), formulates stratification as a path-selection problem over a feature graph. The selected paths define interpretable stratification rules and are optimized using an exact variance-minimizing binary optimization formulation under continuous proportional allocation and a Neyman-type optimal allocation. We incorporate supervised optimal binning to generate outcome-relevant candidate splits for numerical features. Furthermore, we introduce reduction procedures for redundant candidate paths and assignment constraints, substantially reducing the optimization problem size. Experiments on both a real-world and a simulated dataset demonstrate that OMST achieves comparable or superior variance reduction to existing methods while maintaining shallow and interpretable stratification trees.

---


### 189. [Learner-Centered Design of Educational Tools for Cross-Expertise Technical Communication in Computing Contexts](https://arxiv.org/abs/2609.23309)

**<font color=#1a73e8>作者：</font>** Jinyoung Hur, Yoshee Jain, Yuxuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cross-expertise technical communication (i.e., communicating about computing topics across levels of computing expertise) is important for workplace collaboration. However, students are underprepared because computing education rarely explicitly teaches communication, and available practice tends to occur among peers with similar expertise. We take a learner-centered design approach to inform technologies for developing these skills. We interviewed 12 industry professionals and conducted focus group and co-design sessions with 14 college students preparing for computing-related roles. Professionals emphasized adapting communication, negotiating expectations, building shared understanding, and using multiple modalities and artifacts. Students anticipated challenges adapting communication, navigating unfamiliar workplace dynamics, and communicating under fear of judgment, and valued rich, realistic practice environments that preserved their psychological safety. Synthesizing professional and learner perspectives with educational theory, we conclude that building self-efficacy through authentic mastery experiences and changing attitudes related to help-seeking are critical elements for educational technology design in this context.

---


### 190. [When Does Communication Help? Beyond Spectral Descriptions of Collective Intelligence](https://arxiv.org/abs/2609.23310)

**<font color=#1a73e8>作者：</font>** Xuening Wu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Communication can bring agents into agreement while making their decisions worse. We identify two limits of aggregate descriptions of communication gain in distributed inference. First, stable linear systems with fixed evidence, network and readout can have interaction and finite-time state operators with identical eigenvalue and singular-value spectra, yet produce gains of opposite sign. Changing only message orientation raises accuracy from 72.6% to 91.2% or lowers it to 65.9%. A standard task-projected local-response approximation retains the directional information missing from spectral summaries. Using labeled calibration data separate from the test set, it predicts multi-round gains in small trained nonlinear agents with a root-mean-square error of 0.45 percentage points on two synthetic tasks; tests with natural edge changes and handwritten digits extend the evaluation. Second, under community-shared bias, higher mean individual accuracy can coexist with harm to unaffected communities or lower global-vote accuracy. At fixed communication rounds, calibration constraints reduce observed community harm while retaining much of the mean benefit, but do not guarantee protection. Full direct calibration performs similarly. The results connect spectral insufficiency, task-aware prediction and the distribution of communication benefits, while leaving broad transfer and practical superiority open.

---


### 191. [A Patient World Model for Early Forecasting of Digital Health Campaign Outcomes: Capabilities and Limits](https://arxiv.org/abs/2609.23333)

**<font color=#1a73e8>作者：</font>** Yunlong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital direct-to-consumer (DTC) health campaigns are usually measured after the fact. In-flight forecasting commonly relies on a separate classifier for every cutoff and horizon. We treat this task as a dynamic-system problem and build a compact patient world model. The architecture maintains a latent state per patient, learns exposure-conditioned state dynamics jointly with a weekly conversion hazard, and rolls forward into future conversion curves. We evaluate it on a US campaign dataset with 147{,}173 patients and 5.2 million at-risk person-weeks. In a retrospective evaluation conditioned on recorded future exposures, the model forecasts the remaining new-to-brand prescription volume through week 52 with a relative error of 2.9\% from a week-4 cutoff and 0.8--2.6\% from cutoffs at weeks 8--26. The strongest non-recurrent baseline, a pooled-hazard gradient boosting model given the same survival rollout and information, has relative errors of 13.6--33.1\%. Per-horizon classifiers perform substantially worse. A Fisher-information analysis motivates dense next-exposure supervision when conversions are rare. Removing this auxiliary objective increases prescription-volume error by approximately $2$--$14\times$, while providing no consistent disadvantage on the more common specialist-visit outcome. We also evaluate scenario simulation. Switching all future exposure off raises predicted conversion from 0.31 to 0.89, a pattern consistent with selection effects in observational exposure data. This result highlights the limits of interpreting exposure-conditioned rollouts causally.

---


### 192. [BiView-Touch: Learning Bimanual Tactile Representations by Cross-Hand Completion](https://arxiv.org/abs/2609.23352)

**<font color=#1a73e8>作者：</font>** Chenxin Liang, Youchen Lai, Chuqiao Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bimanual interaction produces complementary tactile views of the same physical process, yet existing tactile representation learning largely models the two hands independently or combines them only for downstream prediction, leaving their cross-hand relationship unexplored. To exploit this overlooked structure, we introduce BiView-Touch, a tactile-only framework that completes masked target-hand latents from the remaining visible target-hand regions and the synchronized full contralateral hand. A student encoder with a geometry-conditioned directional decoder predicts full-view EMA latent targets, while temporal and layout counterfactuals encourage sensitivity to synchronized and anatomically organized source information. Controlled ablations and source-context interventions show that BiView-Touch learns structured cross-hand dependence on temporally aligned and anatomically organized contralateral tactile context, rather than benefiting from bilateral input alone. On the public HumanTouch dataset, its frozen representations consistently outperform representative self-supervised baselines across low-label settings. With only 5\% downstream labels, BiView-Touch achieves relative balanced-accuracy gains of 7.1\% on bilateral wrist-motion recognition and 14.1\% on force-derived interaction-phase recognition. We further introduce BVT-20, a 20-task bilateral tactile dataset, and demonstrate transfer across recording sessions and pretraining corpora, including transfer to a held-out bimanual task. Our code and dataset details are available on the anonymous project page: this https URL.

---


### 193. [Identity Continuity in Long-Term Embodied AI Relationships: From Agent-Specific Identity Representation to Identity-Continuity Appraisal](https://arxiv.org/abs/2609.23356)

**<font color=#1a73e8>作者：</font>** Zijian Ru  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Long-term embodied AI will undergo learning, model updates, memory compression, hardware repair, and migration across embodiments. For users who have formed sustained relationships with such systems, these changes raise not only a problem of product consistency but also one of identity continuity: whether the changed system is still experienced as the same particular agent. Existing research suggests that human-AI relationships may develop relational particularity, that robotics and artificial-identity research has identified identity and migration signals across embodiments, and that major updates or platform disruptions can be accompanied by relational loss and restoration desire. This article proposes a user-side framework in which long-term embodied AI is represented through an agent-specific identity representation organized by at least three open identity-content domains: embodied-perceptual, psychological-behavioral, and relational-autobiographical. Information from these domains is not equally weighted; shared history, relational roles, and contingent responsiveness may make some information more identity-diagnostic than others. After system change, users may integrate continuity and discontinuity evidence in a weighted manner, yielding judgments along a continuum from relatively strong identity continuity through ambiguity or partial continuity to clear identity discontinuity. Causal-historical provenance and user participation are treated as contextual evidence rather than a fourth identity-content domain. The framework also proposes identity continuity as a psychological objective for lifecycle design, including memory selection, model updating, and migration across embodiments, under constraints of privacy and user control.

---


### 194. [What Can a Recurrent State Safely Forget?](https://arxiv.org/abs/2609.23366)

**<font color=#1a73e8>作者：</font>** Linzhe Zhang, Changming Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent models must preserve information that changes future behavior while suppressing hidden-state error. These objectives conflict: contraction improves stability, but contraction along a future-distinguishing direction destroys memory. We formalize this boundary through the predictive quotient of a recurrent state space. Two hidden states are equivalent when they induce the same conditional future; their equivalence classes form predictive fibers. Every exact semantics-preserving corrector acts as the identity on this quotient. At a regular point with hidden dimension d and predictive dimension k, it can eliminate at most d - k independent directions. This establishes a discrete-continuous boundary: finite predictive states admit positive-radius exact correction basins, whereas an uncountable continuum of future-distinguishable states cannot be decoded after arbitrary positive-radius perturbations in finite-dimensional Euclidean space.
To operationalize this principle, we develop an auditable finite-future framework. A compact deployment bank W is evaluated against an independent audit bank A (W subseteq A) on a declared correction domain. Under generative probe access and audit-metric coverage, finite stochastic rollouts furnish a high-probability certificate for the separation margin Omega_{W|A}(delta). Preserving learned W-predictions within this certified margin guarantees bounded audit-semantic distortion. For intrinsic audit dimension k, the required probe outcomes scale as O(M * Omega^{-(k+2)}), where M = |A|; a matching minimax lower bound proves this exponent is optimal. Extending guarantees to continuous futures is achieved via an explicit completeness modulus. Controlled experiments validate the certified margins, scaling laws, and automated probe refinement under a safety-first evaluation paradigm.

---


### 195. [The Right Future for Action: Learning Action-Relevant Predictive States in World Action Models](https://arxiv.org/abs/2609.23369)

**<font color=#1a73e8>作者：</font>** Qiwen Gu, Jifan Li, Bingjie Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generation-free world action models (WAMs) retain future-video prediction during training but act from internal video features at inference, leaving unclear what these features should preserve for control. Our representation diagnostics show that representations with more predictable future changes need not make linear action decoding easier. Observed future changes provide additional action information beyond the present, and linearly readable action information is spatially concentrated. These findings motivate Action-Relevant Predictive States (ARPS), a compact predictive interface between the video and action experts. ARPS uses a horizon-conditioned state predictor to aggregate intermediate video features into a compact state that supplies all visual context to the action expert. Future-representation supervision trains different parts of this state to predict visual representations at different future times, together with their changes relative to the present. At inference, the supervision branch is removed, and the action expert only uses the learned predictive state computed from current observations. Controlled ablations show that future supervision substantially improves generalization under distribution shift. ARPS achieves 99.2% success on LIBERO and transfers to LIBERO-Plus without adaptation, reaching 87.3% and exceeding Fast-WAM by 39.2 percentage points.

---


### 196. [Vision-Wireless Fusion for Multi-User Localization: A Cross-Modal Transformer Approach](https://arxiv.org/abs/2609.23372)

**<font color=#1a73e8>作者：</font>** Can Zheng, Jiguang He, Guofa Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate multi-user localization is challenging in complex urban environments, where wireless measurements can become ambiguous under noise, blockage, and multipath, while visual observations provide complementary spatial context. This paper presents a vision-wireless fusion framework for multi-user localization using pilot-indexed channel state information (CSI). Orthogonal pilot indices preserve the identities of the communicating UEs in the CSI token sequence and localization outputs. The model encodes each pilot-indexed CSI observation as a query token and uses cross-attention to retrieve user-specific information from spatial visual memory. Self-attention among CSI tokens further captures inter-user interactions, while the resulting multimodal representations are used for user-wise localization. Experiments on different datasets show consistent improvements over model-based, CSI-only, and multimodal-fusion baselines. Further experiments evaluate the model under different wireless and visual conditions.

---


### 197. [The Evidence Ladder for Reinforcement Learning in Healthcare: From Retrospective Policies to Trusted Interventions](https://arxiv.org/abs/2609.23374)

**<font color=#1a73e8>作者：</font>** Yunfan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) offers a natural language for healthcare decisions whose conse- quences unfold over time, yet most reported progress remains far from routine intervention. Ex- isting surveys organize the field by algorithm or clinical application. We instead review healthcare RL through an evidence ladder: problem formulation, retrospective identification, policy estima- tion, stress testing, prospective evaluation, and lifecycle monitoring. This view connects clinical treatment, patient engagement, and health-system operations while exposing a recurring gap: evi- dence that a policy scores well in a historical dataset is not evidence that it will improve care. We synthesize the assumptions and failure modes at each rung, identify what evidence can and can- not transfer across settings, and propose reporting practices for cumulative evaluation. Restless bandits are included as one special case, not as the organizing framework. The central lesson is that healthcare RL should be evaluated as an intervention embedded in a changing sociotechnical system, rather than only as an optimizer of a retrospective reward.

---


### 198. [Leaky-integrator reconstruction: taming error accumulation in recursive differenced time-series forecasting](https://arxiv.org/abs/2609.23378)

**<font color=#1a73e8>作者：</font>** Zijiang Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce leaky-integrator reconstruction, a training-free method that cures the error accumulation of recursive differenced forecasting. Our first contribution is diagnostic: predicting one-step changes and integrating them by cumulative summation, the standard remedy for non-stationarity, is a discrete integrator with a pole on the unit circle, and we show this makes recursive rollout of a nonlinear model diverge, its 336-step error reaching several times that of a well-behaved forecaster (normalised MAE 1.6-3.8 versus about 0.8) across every neural architecture tested. Our second, central contribution is the fix: move the pole inside the unit circle with a leaky integrator H(z) = 1/(1 - gamma z^-1), gamma < 1, which provably bounds the accumulated error variance. Applied at reconstruction time with a single fixed gamma=0.9 (no retraining, a two-line change to any deployed one-step or foundation-model forecaster), it shrinks error at every horizon, the mean gain over seven diverging architectures and twenty datasets growing from ~3% at H=24 to 23% at H=96, 37% at H=192 and 51% (43-74% across those architectures) at H=336 (78% with an oracle pole). Crucially, it is provably inert where no pathology exists (stable or joint predictors already at the irreducible rate), making it a safe, general default.

---


### 199. [LiteTex-GS: Fast and Lightweight Texturing for Gaussian Splatting](https://arxiv.org/abs/2609.23380)

**<font color=#1a73e8>作者：</font>** Zhiwei Li, Yijia Guo, Yishi Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has enabled real-time novel view synthesis, but its tightly coupled geometry and appearance representation often require a large number of primitives to reproduce high-frequency texture details, leading to substantial memory and optimization costs. Recent textured 2D Gaussian methods alleviate this limitation by attaching texture maps to Gaussian primitives. However, bridging the fundamental structural gap between discrete Gaussians and continuous 2D grids requires complex parameterizations that introduce severe computational overhead. This overhead fundamentally compromises the original efficiency of Gaussian Splatting, making the balance between detailed texturing and computational agility an unresolved challenge. To address these challenges, we propose LiteTex-GS, a fast and lightweight texturing framework for Gaussian Splatting. Our method initializes an extremely compact representation, assigning minimal local texture to each Gaussian and progressively allocates higher resolution only to primitives with significant reconstruction errors. To maintain a streamlined geometric scaffold, we introduce a contribution- and area-aware pruning strategy that eliminates low-utility Gaussians. Furthermore, to mitigate the gradient dilution caused by texture upsampling, we design a resolution-aware update rule that preserves rapid and stable convergence. Extensive experiments on standard novel view synthesis benchmarks demonstrate that our method achieves competitive or superior rendering quality while using substantially fewer parameters and less training time than existing textured Gaussian baselines.

---


### 200. [Discovering Physical Representation Languages](https://arxiv.org/abs/2609.23381)

**<font color=#1a73e8>作者：</font>** Linzhe Zhang, Changming Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Before a machine can discover a physical law, it must discover what its measurements are: which observations live on cells, which are intensive or extensive, which sectors are dual, and which distinctions are merely gauge. We introduce physical representation-language discovery, the problem of recovering this hidden ontology directly from anonymous controlled experiments. We give an identifiability theory and constructive polynomial-time procedure that recovers a carrier and differential sequence, measurement types and orientation twist, noninvertible refinement semantics, primal-dual Maxwell diagrams, and the residual equivalences that no permitted experiment can break. The theory turns material nuisance into a commutant, uses refinement to separate quantities from coordinates, and selects physics only after its representation has been recovered. For a certified finite experiment family, we prove an end-to-end two-stage measurement bound and a matching minimax rate in dimension, accuracy, and confidence. Blind Maxwell experiments recover complete primal/relative-dual ontologies on regular and unstructured carriers under jointly corrupted observations; an independent unstructured RLC system demonstrates that the result is not specific to Maxwell. The framework scales to tens of thousands of cells per carrier, while stress audits demonstrate robustness across severe physical regimes - including non-Markovian memory, nonlinearities, nonlocality, and complex constitutive hysteresis. A public FDTD audit demonstrates the emergence of anonymous curl structure from incomplete field data, while characterizing the informational prerequisites for complete recovery. The goal is to move scientific ML from learning laws in a human-supplied language to discovering the language in which laws become expressible, establishing exact theoretical limits on observational identifiability.

---


> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
