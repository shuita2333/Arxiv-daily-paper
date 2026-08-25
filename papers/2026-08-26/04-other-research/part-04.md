# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

---

### 151. [When Does Visual Generation Help Visual Understanding in Unified Multimodal Models?](https://arxiv.org/abs/2608.22174)

**<font color=#1a73e8>作者：</font>** Yubo Zhu, Zhehan Kan, Jingyi Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) can perform both understanding and generation, raising a central question: can visual generation improve understanding? Existing evaluations provide mixed evidence, but confound task difficulty, reasoning paradigms, and the closed-loop interaction between generation and understanding. We introduce VGAU-Diag, a fine-grained evaluation framework for vision generation-assisted understanding. It stratifies samples by difficulty, enables unified evaluation of multiple reasoning paradigms, and uses Oracle-Assisted Reference Protocols. Our analysis shows that generated visual aids help on easier instances but become unreliable as reasoning complexity increases. Oracle-assisted diagnosis further reveals that the main bottleneck often lies on the visual-understanding side rather than the visual-generation side, as current UMMs struggle to leverage even faithful visual aids. We also show that effective visual generation should target visual-understanding bottlenecks rather than add more reasoning steps, and identify a three-stage transition from task-irrelevant noise, to misleading plausible guidance, and finally to useful assistance. These findings would be useful to guide the development of better this http URL code is available at this https URL.

---


### 152. [VERDICT: Agreement Beats Pixel-Space Verification in Real-Document OCSR](https://arxiv.org/abs/2608.22183)

**<font color=#1a73e8>作者：</font>** Yani Guan, Dengpan Dong, Shuang Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Chemical Structure Recognition (OCSR) converts 2D molecular depictions in the published literature into SMILES, and is increasingly important for constructing large-scale chemical training datasets. Automation at that scale requires identifying unreliable predictions in the absence of ground truth. Three families of label-free signals were compared on $263$ ACS journal depictions with verified ground truth: model confidence, re-rendering similarity, and agreement among recognizers. Pixel-space re-rendering performed little better than chance (AUROC $0.547$, $95\%$ CI $[0.465,0.629]$), and an oracle-tuned threshold on it reduced correct labels per image from $0.745$ to $0.205$. Agreement among four architecturally distinct recognizers instead reached an AUROC of $0.916$ ($[0.880,0.952]$). The two-of-four rule accepted $81.7\%$ of images at $88.8\%$ precision, the three-of-four rule $52.1\%$ at $98.5\%$. The same pattern held on CLEF-IP, UOB, and USPTO. This distinction is obscured on synthetic benchmarks, where re-rendered predictions naturally resemble their inputs. A substance filter removed $2{,}193$ false agreements on wildcards and R-group fragments, after which the three-of-four rule rejected all $68$ generic depictions. VERDICT was then applied to PMC Open Access, producing $6{,}146$ structure labels for $4{,}833$ molecules; chemist adjudication of $400$ released labels in two independent samples yielded precisions of $0.995$ for the three-of-four tier and $0.958$ for the two-of-four tier. VERDICT therefore enables validated labels for multimodal molecular databases linking structure images, machine-readable representations, and source-publication information. In SES AI's Molecular Universe platform, VERDICT further serves as an image-based interface for searching and retrieving molecular records.

---


### 153. [SAM3Dual: A 3rd Place Solution to the MOSEv2 Track, 8th LSVOS Challenge](https://arxiv.org/abs/2608.22193)

**<font color=#1a73e8>作者：</font>** JeongRae Kim, Chaehyun Kim, Changwon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SAM3Dual, our third-place solution to the MOSEv2 track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge at ECCV 2026. SAM3Dual is a training-free inference extension of pretrained SAM 3 that explicitly separates temporal memory into a short-term branch for recent observations and a long-term branch for interval-sampled historical representations. The two memory responses are combined using a deterministic sequence-relative fusion schedule and conservatively modulated by the previous-frame object confidence. All pretrained SAM 3 parameters remain frozen, requiring no task-specific training, fine-tuning, test-time training, or online parameter optimization. The complete system achieved an official J&F score of 64.37 and ranked third in the MOSEv2 track. This result highlights the potential of reorganizing temporal memory entirely at inference time to obtain competitive long-term VOS performance while preserving the pretrained model.

---


### 154. [On the Capability Separation Between World-Model Policy Learning and Imitated World-Action Models](https://arxiv.org/abs/2608.22197)

**<font color=#1a73e8>作者：</font>** Yang Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World-action models predict a future outcome and then infer an associated action. Although this factorization can improve representation learning and data efficiency, it is unclear whether it provides stronger control capability than direct behavior cloning when both are trained from the same observational demonstrations.
We compare a direct behavior-cloning policy, an imitation-trained world-action policy, and a policy optimized with an action-conditioned world model. At the controller-class level, every world-action policy can be flattened into a direct stochastic policy with the same closed-loop trajectory distribution. At the population level, under realizability, exact optimization, common deployment information, and distribution-preserving deployment, direct behavior cloning and world-action imitation both recover the observational behavior policy. Thus, future prediction changes the learning factorization but not the unrestricted external policy class or ideal imitation target.
Action-conditioned world-model learning differs by predicting outcomes under specified actions and comparing them through a control objective. We characterize the irreducible action-specific prediction error of future models that do not condition on the candidate action, identify conditions under which a world-action joint can recover an interventional forward model, and show that observational demonstrations do not identify action effects in general. Finally, we construct an environment family in which every observational learner has positive worst-case regret, whereas one informative intervention permits zero regret. The key distinction is therefore between predicting futures associated with observed behavior and predicting consequences of specified actions for policy optimization.

---


### 155. [Joint Causal Structure and Cluster Discovery Using Variational Inference](https://arxiv.org/abs/2608.22212)

**<font color=#1a73e8>作者：</font>** Avni Rajpal, Anubhav Kumar, Rishabh Karnad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery aims to understand the relationships between individual random variables. In many applications, such as brain imaging and climate modeling, it is more meaningful to consider interactions among groups of variables. Existing methods assume that knowledge of such groups or clusters is explicitly available when modeling interactions. However, in practice, these clusters as well as the causal relationships among them, are latent. In this paper, we present a novel approach based on variational inference to simultaneously infer both the latent clusters and causal structures. We learn an approximate posterior over clusters and graph-structure by considering variational distributions based on categorical and Bernoulli models respectively. We derive variational lower bounds and estimation techniques to learn variational and model parameters. The effectiveness of our proposed methods for cluster and causal discovery are demonstrated on both synthetic and real data sets.

---


### 156. [PURA: Provably Unbiased and Robust Multi-Bit Text Attribution](https://arxiv.org/abs/2608.22218)

**<font color=#1a73e8>作者：</font>** Yaofei Wang, Jinyang Guo, Shuchao Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-grained attribution of AI-generated text is becoming increasingly important for accountability and auditing, yet existing multi-bit watermarking methods still struggle to simultaneously preserve the base generation distribution, support high-capacity payloads, and remain recoverable after editing. We present PURA, a provably unbiased and robust multi-bit watermarking method for text attribution. Instead of perturbing token probabilities directly, PURA embeds payloads in the latent sampling space via keyed inverse transform sampling, and recovers them by treating observed tokens as soft interval evidence and aggregating such evidence across the sequence. This design preserves the base generation distribution exactly while substantially improving recovery stability under post-editing and channel perturbations. Building on this recovery paradigm, we further develop a unified robustness analysis and show that, under bounded attack strength, the per-bit error probability decays exponentially with sequence length. Extensive experiments show that PURA substantially outperforms existing unbiased baselines in the high-payload regime. For example, when embedding 36 bits in 200 tokens, PURA achieves a 91.7\% message match rate, more than three times that of the strongest unbiased baseline, while preserving text quality and remaining statistically close to unwatermarked text, and incurring only millisecond-level verification overhead. Our code is available at

---


### 157. [Counterfactual Evaluation of Temporal Observation Protocols](https://arxiv.org/abs/2608.22221)

**<font color=#1a73e8>作者：</font>** Xizhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study counterfactual protocol evaluation: whether data collected under a realised observation protocol determine the predictive value of alternatives that were never deployed. Protocol value is the population $R^2$ of the Bayes-optimal predictor of a fixed trajectory-level target from the measurements an alternative would collect. We show that even infinite benchmark data need not determine this value: distinct latent covariance structures can induce the same benchmark measurement--target law while assigning different values to the same alternative. We develop a value-specific identification theory in which only latent ambiguity that changes the alternative's value matters. For linear targets, invisible covariance directions certify non-identification, while targeted measurements can restore identification without recovering the full latent covariance; an exact permutation construction extends the result to nonlinear aggregate targets. With finite dense calibration data, uniform error bounds control protocol-selection regret and distinguishable value gaps. Exact marginal gains then support cost-constrained, target-aware observation design. Simulations and retrospective analyses of Sleep-EDF and Long-Term AF show that broad temporal-layout differences can be more reliably distinguished than fine placements selected from finite data. Together, these results connect identification, calibration resolution and observation design for undeployed protocols.

---


### 158. [FreKoo++: Learning Continuous Spectral Dynamics for Temporal Domain Generalization](https://arxiv.org/abs/2608.22224)

**<font color=#1a73e8>作者：</font>** En Yu, Xiaoyu Yang, Wei Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Domain Generalization (TDG) aims to learn from historical domains and generalize to unseen future distributions under concept drift. Nevertheless, prevailing TDG methods struggle with complex real-world streaming scenarios involving both multi-scale drift patterns (e.g., long-term periodicity intertwined with short-term incremental changes) and local uncertainties, especially in continuous settings where observations arrive irregularly. To address this limitation, we propose FreKoo++, a novel continuous spectral-dynamical framework that pioneers the unification of continuous Koopman modal dynamics with adaptive spectral disentanglement. Specifically, FreKoo++ maps source-domain parameters into a compact latent space, modeling their evolution as a superposition of learnable continuous modes where complex eigenvalues jointly encode oscillatory frequency and temporal growth or decay. This formulation naturally accommodates irregular timestamps and supports arbitrary horizon extrapolation without rigid discrete stepping. Furthermore, we propose a new adaptive soft spectral weighting mechanism backed by stability and spectral regularization, which automatically isolates persistent dominant dynamics from transient noise without relying on manual frequency thresholds. We derive modal approximation and generalization bounds that characterize how amplitude and eigenvalue estimation errors propagate with the prediction horizon. Extensive experiments on both discrete and continuous TDG benchmarks demonstrate that FreKoo++ achieves state-of-the-art performance under complex multi-scale drifts and irregular sampling.

---


### 159. [Risk-Sensitive Reinforcement Learning with Smoothed Quantile Objectives](https://arxiv.org/abs/2608.22227)

**<font color=#1a73e8>作者：</font>** Mohammad Alipour-Vaezi, Huaiyang Zhong, Sajad Khodadadian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has achieved tremendous success in recent years. However, the classical foundations of RL do not account for the risk sensitivity of the objective function, which is critical in various fields, including healthcare, finance, etc. A popular approach to incorporate risk sensitivity is to optimize a specific quantile of the cumulative reward distribution. However, exact quantile objectives are non-smooth and can change abruptly under small perturbations of the return distribution, making them difficult to optimize reliably when the transition model must be learned from data. Motivated by this instability, we develop UCB-BQRL, a model-based optimistic learning algorithm that maintains confidence sets for the transition kernel and plans using a lower-buffered quantile criterion. The buffered criterion smooths the exact quantile objective by averaging nearby lower quantiles, thereby improving stability under transition-estimation error. To compute the buffered-quantile policy at each episode, we introduce EVI-BQ, an exact dynamic-programming procedure. We establish a high-probability regret bound for UCB-BQRL, which up to logarithmic factors scales as $\mathcal{O}(\mathrm{e}^{\tau/\rho_\tau}+H^2\sqrt{SAT})$, where $\rho_\tau$ is denoted as the root-level left-plateau threshold, which is a problem-dependent constant. Further, we establish an information-theoretic lower bound of $\Omega(H/\rho_\tau\sqrt{AT})$ for the regret of any algorithm dealing with a quantile objective function. Finally, we prove that the exact point-quantile evaluation and exact lower-buffered quantile evaluation are PP-hard under polynomial-time Turing reductions, even for a fixed policy in a two-state, one-action finite-horizon MDP.

---


### 160. [When Test-Time Adaptation Helps, Harms, or Becomes Inactive: A Condition-Level Study on CIFAR-10-C](https://arxiv.org/abs/2608.22233)

**<font color=#1a73e8>作者：</font>** Sreeja Guha Majumdar, Aratrika Saha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) aims to improve model robustness under distribution shift by adapting a source model using unlabeled test data. Although methods such as TENT and EATA have demonstrated gains on corrupted data, aggregate accuracy can obscure the conditions under which adaptation fails or provides little benefit. We present a controlled comparison of three TTA strategies---BatchNorm-statistics adaptation (BN-Adapt), entropy-minimization adaptation (TENT), and reliability-filtered adaptation (a scoped re-implementation of EATA)---against an unadapted source model on the full CIFAR-10-C benchmark, covering 15 corruption types and 5 severity levels. All three methods improve mean accuracy over the source model by 12.2--13.3 percentage points (Wilcoxon signed-rank $p < 10^{-12}$). However, each method underperforms the source model on 8.0--9.3\% of conditions, with failures concentrated in low-severity corruptions where the source model already performs near ceiling, particularly brightness, fog, contrast, and defocus blur. We further find that EATA closely tracks the gradient-free BN-Adapt baseline, with a mean absolute difference of 0.09 percentage points, compared with 1.08 percentage points relative to TENT. This suggests that reliability filtering can substantially restrict effective adaptation, causing EATA to behave more like a BatchNorm-statistics baseline than an entropy-minimization method. These results show that aggregate accuracy alone can mask systematic TTA failure modes and motivate condition-level evaluation of when adaptation helps, harms, or becomes effectively inactive.

---


### 161. [A Query-Time Framework for Transient 2D Pore-Scale Flow Prediction and Generative Design](https://arxiv.org/abs/2608.22235)

**<font color=#1a73e8>作者：</font>** Yiming Wang, Jiale Zhu, Zhichen Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pore-scale flow governs transport and permeability behaviour in porous media engineering applications, yet repeated lattice Boltzmann method (LBM) simulation across many geometries and design queries remains costly for repeated deployment. This study formulates transient pore-scale flow prediction as a geometry-conditioned query-time operator and introduces QSGS-Transient-7606, a benchmark of 7,606 two-dimensional porous structures each paired with 30 logarithmically sampled LBM states. The proposed continuous-time pore-scale flow surrogate model (CT-PoreFlow) integrates topology-aware geometry encoding, compressed spectral mixing, and log-time conditioning with a late-time flux-calibration objective. On unseen test geometries, CT-PoreFlow achieves a velocity relative L2 of 0.2248 and a terminal permeability error of 12.81%. Frozen morphology and computed tomography image audits confirm reasonable cross-geometry robustness without fine-tuning. The surrogate is then embedded in an inverse design workflow, screening 9,216 generative adversarial network and diffusion candidates across 18 property targets prior to LBM verification. Guided GAN sampling attains 98.11% through-connectivity and 72.28% conditional design success, exceeding diffusion-based generation. The framework unifies transient flow prediction, transport-aware screening, and LBM-verified inverse design for porous media.

---


### 162. [Hyper^2: Unleashing Hyperbolic Geometry's Full Potential via Dual-Space Consistency](https://arxiv.org/abs/2608.22238)

**<font color=#1a73e8>作者：</font>** Guantian Zheng, Haiyang Xu, Tianyu Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> HyperbolicCD pioneered hyperbolic geometry for point cloud completion by replacing the Euclidean Chamfer distance with arcosh(1+alpha||x-y||^2), but the reported gains are modest (3-7% Chamfer reduction across SeedFormer, PointAttN and PMP-Net backbones on PCN and ShapeNet-55). We argue the bottleneck lies elsewhere: the loss is hyperbolic but the encoder it back-propagates through is Euclidean, so the position-dependent supervision of the loss is averaged away by the chain rule before it reaches the parameters. We call this a cross-geometry mismatch, and make it testable through two model-agnostic indicators, feature-loss correlation r_FL and effective gradient utilisation u_G. On an SVDFormer backbone trained with HyperbolicCD's loss alone we measure (r_FL, u_G) = (0.68, 39%). We propose Hyper^2, a dual-space consistency framework that extends HyperbolicCD by reusing the identical arcosh(1+alpha d^2) functional form as a positional bias on the refinement attention (a hyperbolic distance encoding), paired with HyperbolicCD's hyperbolic Chamfer loss under a single shared curvature alpha. Both operators are O(N log N) scalar non-linearities on Euclidean distances and together add only ~1.6% FLOPs over SVDFormer. Hyper^2 delivers -22.9% Chamfer on ShapeNet-55 over SVDFormer (well above the 13.2% linear sum of the -12.0% loss-only and -1.2% encoding-only single-space ablations) and -37.5% on the 21 unseen ShapeNet-34 categories. The two indicators remain essentially flat for any single-space configuration but jump together to (0.95, 87%) only when both encoder and loss are hyperbolic, supporting the claim that geometric consistency across encoder and loss, rather than either operator alone, is what enables hyperbolic supervision in point cloud completion. Code is available at this https URL.

---


### 163. [Correctness Is Not Homogeneous Evidence: A Correctness-conditioned Evidence-aware Knowledge Tracing Model](https://arxiv.org/abs/2608.22267)

**<font color=#1a73e8>作者：</font>** Fuzheng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing models usually use response correctness as a central observation for estimating students' latent knowledge states. However, the same correct or incorrect response may arise from different behavioral contexts, such as rapid guessing, hint use, or repeated attempts. Treating correctness as uniformly informative may therefore introduce ambiguity into recurrent state updates. This study proposes Correctness-conditioned Evidence-aware Knowledge Tracing (CE-KT), which uses observable response-process features to condition how correctness is written into recurrent states. CE-KT derives weakly supervised behavioral proxy scores from response time, hint use, attempt count, and behavioral history. These scores are used as behavioral signals, not as direct measures of mastery, response quality, or cognitive state. CE-KT then uses current correctness to select a correct-response or incorrect-response gate. The selected gate modulates both the LSTM hidden state and cell state, and the modulated states are fed back into later recurrent updates. Experiments on ASSISTments data show that behavioral condition scores are associated with future same-skill performance within fixed correctness groups, especially for incorrect interactions. CE-KT generally outperforms several behavior-fusion alternatives on the main predictive metrics, although its calibration advantage is not consistent. Ablation analyses provide partial support for correctness-specific recurrent modulation and recurrent feedback. These findings suggest that behavioral information can help condition the interpretation of response correctness in knowledge tracing, but the proposed proxy scores should not be treated as direct evidence of true mastery or causal learning effects.

---


### 164. [GAN-Diff : Coupling Pretrained WGAN-GP Features with Conditional Diffusion U-Nets](https://arxiv.org/abs/2608.22272)

**<font color=#1a73e8>作者：</font>** Saif Ahmed, Ashadulla Hil Galib, S.M. Riaz Rahman Antu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative adversarial networks (GANs) can provide efficient image generation, while diffusion models offer high-quality image restoration but require iterative sampling. This paper presents a hybrid GAN-guided diffusion framework that uses a pretrained Wasserstein GAN with gradient penalty (WGAN-GP) as a feature prior for conditional diffusion-based image restoration. Intermediate features from the frozen WGAN-GP generator are incorporated into a diffusion U-Net through cross-attention and remain fixed during the DDIM sampling process. The framework is evaluated on two restoration tasks, Gaussian denoising and 2Xsuper-resolution, using CelebA face images. During development, several sources of instability were identified and addressed, including adversarial learning-rate imbalance, inappropriate diffusion initialization, excessive corruption, and insufficient parameter averaging. The resulting framework consistently improves the quality of both degraded and low-resolution images. In particular, it improves denoising performance by 4.40 dB in PSNR and super-resolution performance by 3.70 dB over their respective input baselines. These results demonstrate the potential of a frozen GAN feature prior to guide diffusion models toward stable and effective image restoration.

---


### 165. [DAW: Dynamics-Aware Weighting for Deep Learning Forecasts of Chaotic Systems](https://arxiv.org/abs/2608.22277)

**<font color=#1a73e8>作者：</font>** Zhou Fang, Gianmarco Mengaldo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning surrogates for forecasting chaotic dynamical systems suffer from catastrophic error accumulation over long-term autoregressive rollouts. This behavior is partly tied to the underlying systems: chaotic spatiotemporal systems, such as the Kuramoto-Sivashinsky (KS) equation, visit phase space unevenly - dominated by recurrent, low-dimensional quiescent states (e.g., near-laminar flows) and punctuated by rare, dynamically complex topological transitions (e.g., wave-merging events). Under a sample-wise uniform objective, standard neural surrogates allocate their finite capacity to the statistically numerous quiescent states, under-representing the transient regimes that trigger disproportionate, localized errors. Existing imbalanced-regression methods reweight samples by target-space density. However, statistical target-space rarity need not coincide with the intrinsic dynamical rarity - the recurrence geometry of the attractor that is the source of the imbalance. To address this, we introduce Dynamics-Aware Weighting (DAW), a data-centric objective reweighting framework. Using the local dimension $d$ from dynamical systems theory as an a priori measure of a state's active degrees of freedom, DAW reshapes the loss landscape to allocate representational capacity toward the sparse, high-$d$ regimes where forecast errors are systematically large. On the chaotic KS equation, DAW consistently outperforms uniform training, purely statistical density weighting, and its randomly permuted ablation, reducing long-term autoregressive error relative to all baselines. Event-level analysis shows that DAW achieves this by suppressing the localized error amplifications incurred during sharp jumps in $d$, which accompany complex physical processes such as wave-merging in the KS system.

---


### 166. [DECO: Depth-Guided Co-Visibility Reasoning for Low-Altitude UAV Visual Localization](https://arxiv.org/abs/2608.22289)

**<font color=#1a73e8>作者：</font>** Yibin Ye, Xichao Teng, Shuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) increasingly require robust visual localization in GNSS-denied environments. A common solution estimates UAV poses by matching keypoints between UAV images and geo-tagged orthographic reference maps derived from satellite or aerial imagery, followed by Perspective-\(n\)-Point (PnP) pose solving. However, such reference maps mainly record top-down surfaces such as roofs and ground planes, while vertical structures such as facades and walls are often compressed or missing. Consequently, many visually distinctive keypoints in low-altitude UAV images have no valid counterparts in the reference map, leading to redundant matches and inaccurate pose estimation. To address this issue, we propose DECO, a DEpth-guided CO-visibility reasoning framework for low-altitude UAV visual localization. DECO uses monocular depth priors to infer local surface geometry and estimate co-visible regions between UAV images and the reference map. Based on this prior, a Geometry-Saliency Coupled Co-visibility Score is introduced to jointly consider geometric co-visibility and detector saliency for keypoint ranking. In this way, DECO retains keypoints that are both visually distinctive and geometrically co-visible, improving feature matching and PnP-based pose estimation. Extensive experiments demonstrate that DECO achieves superior localization performance and can be integrated with different depth models, feature detectors, and matchers. The source code will be available at this https URL.

---


### 167. [Targeted Iterative Filtering](https://arxiv.org/abs/2608.22299)

**<font color=#1a73e8>作者：</font>** Freddie Åström, Michael Felsberg, George Baravdish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The assessment of image denoising results depends on the respective application area, i.e. image compression, still-image acquisition, and medical images require entirely different behavior of the applied denoising method. In this paper we propose a novel, nonlinear diffusion scheme that is derived from a linear diffusion process in a value space determined by the application. We show that application-driven linear diffusion in the transformed space compares favorably with existing nonlinear diffusion techniques.

---


### 168. [Self-Calibrating Dense Displacement Fields for Reliable Co-Registration of Large Optical Satellite Imagery](https://arxiv.org/abs/2608.22300)

**<font color=#1a73e8>作者：</font>** Shoukun Sun, Zhe Wang, Sanaz Salati 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-registration underlies nearly every multi-temporal and multi-sensor use of optical satellite imagery, and operational products still carry documented offsets well above the fraction-of-a-pixel scale at which change detection, time series, and data fusion degrade. Real image pairs differ along several axes at once (sensor response, scene content, viewing geometry, resolution, mosaic seams), and the last of these is not a single global motion. Existing tools embed a motion model and constants tuned to their development data; a pair that fits is registered precisely, while one that does not either fails to match or returns a result wrong by tens of pixels with no failure reported. Learned matchers add a GPU requirement and carry no accuracy guarantee outside their training distribution. We present SCDF (self-calibrating displacement fields), a training-free, GPU-free estimator whose motion model is the dense per-pixel displacement field itself, so no scene motion falls outside the model. A single predict--measure--filter loop runs over a resolution pyramid: the accumulated field predicts where each patch of the moving image falls in the reference, RootSIFT matching and a correlation pass measure the displacement there to sub-pixel precision, and filters whose thresholds are all calibrated on the image pair itself decide what survives. One configuration, with no per-dataset tuning, processes full $8192^2$ scenes on a single CPU core. On 584 constructed-ground-truth pairs built from real Sentinel-2, Landsat-8/9, and NAIP imagery, against seven classical baselines and two zero-shot pretrained matchers, SCDF registers every pair with zero failures, reduces the best baseline's real-pair median end-point error from 6.83 to 4.17m, and cuts its 90th percentile from 17.8 to 7.77m.

---


### 169. [On Tensor-Based PDEs and their Corresponding Variational Formulations with Application to Color Image Denoising](https://arxiv.org/abs/2608.22302)

**<font color=#1a73e8>作者：</font>** Freddie Åström, George Baravdish, Michael Felsberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The case when a partial differential equation (PDE) can be considered as an Euler-Lagrange (E-L) equation of an energy functional, consisting of a data term and a smoothness term is investigated. We show the necessary conditions for a PDE to be the E-L equation for a corresponding functional. This energy functional is applied to a color image denoising problem and it is shown that the method compares favorably to current state-of-the-art color image denoising techniques.

---


### 170. [ThreatLens: Evidence-Guided Ranking of High-Priority CVEs](https://arxiv.org/abs/2608.22306)

**<font color=#1a73e8>作者：</font>** Soroush Motamedi Sedeh, Panteha Shahrivar, Malaika Qureshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security teams must prioritize vulnerabilities before exploitation evidence is complete. Existing signals, such as CVSS, EPSS, advisories, and public exploits, are useful but fragmented and time-sensitive; retrospective rankings can therefore overstate performance by using evidence unavailable at decision time. We present ThreatLens, a simple yet effective and deployment-realistic framework for CVE prioritization. ThreatLens ranks vulnerabilities at each review point using only cutoff-valid evidence and learns from future CISA KEV entries as weak supervision for exploitation relevance. Under forward-in-time, CVE-disjoint evaluation, ThreatLens significantly outperforms CVSS, EPSS, and rule-based evidence-fusion baselines. On the held-out test split, ThreatLens surfaces 80.0% of future KEV CVEs in the top 20, over three times EPSS at the same budget, and reaches 95.9% in the top 50. Early-warning analysis further shows that ThreatLens identifies a substantial fraction of subsequent KEV entries before formal catalog inclusion, supporting timely, evidence-grounded triage.

---


### 171. [StocBench: A Benchmark for Generative Modeling of Stochastic Dynamics](https://arxiv.org/abs/2608.22309)

**<font color=#1a73e8>作者：</font>** Sebastian Pfister, Benjamin Holzschuh, Nils Thuerey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We benchmark transport-based generative models as well as distillation-based few-step methods for the probabilistic forecasting of stochastic fluid flows, with a particular focus on performance under limited inference budgets. All methods are evaluated on a two-dimensional Kolmogorov flow with stochastic forcing. We measure one-step distributional accuracy against large simulated reference ensembles and assess whether the invariant measure is preserved during autoregressive rollouts via the enstrophy spectrum. On the stochastic task, flow matching achieves the most accurate one-step conditional distribution at high inference budgets, while the second-order exponential integrator DPM-2 is strongest at very low NFE. Few-step distillation methods are competitive with the multi-step methods and preserve the enstrophy spectrum particularly well. A deterministic control task, in which the forcing over the prediction interval is observed, separates aleatoric from epistemic uncertainty. Model performance does not translate between the two settings: the distilled models are competitive on the stochastic task but least accurate on the control task. While stochastic diffusion samplers such as DDPM better preserve the enstrophy spectrum during rollouts in the stochastic setting, deterministic samplers such as DDIM and DPM-2 show better spectral preservation in the deterministic setting.

---


### 172. [Adapting Dense Vision-Language Relationships for Multi-label Classification with Partial Label](https://arxiv.org/abs/2608.22313)

**<font color=#1a73e8>作者：</font>** Cheng Chen, Yifan Zhao, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning multi-label image classification with incomplete annotations is a challenging task that has been widely studied for its superior trade-off between high efficiency and less labor consumption on large-scale datasets. Predominant methods rely on strong prior assumptions to recover the missing semantics from partial annotations. However, these statistic priors suffer from unstable semantic mistakes and thus lead to catastrophic overfitting. Toward this end, we propose a Language-driven Dense Semantic Adaptor (LDSA) that excavates prior-adaptive relationships from multimodal pretrained CLIP models. In our approach, the densely contrastive adaptor is first proposed to construct dense visual contrastive constraints, transferring the task-specific knowledge to visual domains. We then propose a language-driven interactive decoder with the help of class-specific prompt tuning, which adapts language proxies with visual domains. With the collaborative learning of proposed modules, experimental results demonstrate our proposed LDSA achieves a new state of the art on public multi-label classification benchmarks, and interpretable analyses reveal that our LDSA discovers implicit semantic relationships with the prior-adaptive learning scheme.

---


### 173. [On the Choice of Tensor Estimation for Corner Detection, Optical Flow and Denoising](https://arxiv.org/abs/2608.22314)

**<font color=#1a73e8>作者：</font>** Freddie Åström, Michael Felsberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many image processing methods such as corner detection, optical flow and iterative enhancement make use of image tensors. Generally, these tensors are estimated using the structure tensor. In this work we show that the gradient energy tensor can be used as an alternative to the structure tensor in several cases. We apply the gradient energy tensor to common image problem applications such as corner detection, optical flow and image enhancement. Our experimental results suggest that the gradient energy tensor enables real-time tensor-based image enhancement using the graphical processing unit (GPU) and we obtain 40% increase of frame rate without loss of image quality.

---


### 174. [Semantics or Structure? Auditing Text Sensitivity in Multimodal Time-Series Forecasting](https://arxiv.org/abs/2608.22321)

**<font color=#1a73e8>作者：</font>** Karthik Sridhar, Atharva Gupta, Nishant Pradhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal time-series forecasting has emerged as a promising paradigm in which natural-language context is expected to improve predictive performance. Recent multimodal foundation models, including Aurora, as well as early- and late-fusion approaches such as MM-TSFlib and TaTS, report substantial gains over unimodal baselines on the Time-MMD benchmark, attributing these improvements to textual information. However, whether these models are actually sensitive to the semantic content of the text remains unverified. We address this question through controlled text perturbations, attribution analyses, and probes of Aurora's text pathway. On Time-MMD, swapping each row's text for any other real text (empty, constant, within-domain shuffled, or cross-domain) moves mean MSE by less than $0.5\%$ on all three architectures. The improvement reported in the literature is recovered when a co-shipped numeric column is removed without touching text. We conclude that, on this benchmark and within this family of frozen-encoder architectures, text content is not the operative signal behind the reported gains. To support future work on text integration in multimodal foundation models for structured data, we release our perturbation protocol and evaluation harness as a reusable diagnostic toolkit.

---


### 175. [Gaussian process learning with flow map refinement for parameter estimation in dynamical systems](https://arxiv.org/abs/2608.22324)

**<font color=#1a73e8>作者：</font>** Yue Hao, Dongwei Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter estimation is a central task in data-driven learning of dynamical systems. It aims to recover the underlying physical parameters from observed time-series data, thereby providing interpretable insights into the physical mechanisms governing the system. Gradient/derivative matching methods based on Gaussian process provide an efficient way to perform parameter estimation. Those methods avoid repeated numerical integration and enforce local derivative consistency. However, such local matching may result in global inconsistency with the governing flow map, particularly under scarce and noisy observations. To address this limitation, we propose a framework based on Gaussian process learning with flow map refinement (GPL-FMR), a two-stage parameter estimation framework. The first stage is based on Gaussian process learning algorithm and the posterior obtained from which is transferred as an informative prior to the second stage based on flow-map refinement. The second stage further improves the parameter estimation via optimisation based on global dynamical constraints. We demonstrate and analyse its performance on multiple numerical examples, including the Van der Pol oscillator, the Lotka-Volterra model, and the Lorenz-63 system. The results show that the proposed framework consistently improves parameter estimation accuracy, particularly under scarce and noisy observations.

---


### 176. [AcroMELD: Recovering Interactive PDF Forms with Structure-Aware Graph Set Transformers](https://arxiv.org/abs/2608.22338)

**<font color=#1a73e8>作者：</font>** Samuel Abramov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive PDF form fields are often absent from documents that visually resemble forms, leaving users unable to enter data without printing or external editing tools. Detecting the missing widgets is difficult because a field may be indicated by several overlapping cues, born-digital PDFs expose useful but incomplete drawing structure, and dense pages can contain hundreds of fields. We introduce AcroMELD (AcroForm Multi-source Evidence Linking Decoder), a 39.4M-parameter detector that combines a high-resolution visual transformer with label-free PDF primitives. Its 896-query set comprises 384 visual proposals, 384 structure-seeded proposals, and 128 learned recovery queries. Four graph-set layers exchange information over geometry-biased sparse neighborhoods and cross-attend to PDF structure. A learned same-field relation links co-referent candidates, while a localization-quality head is trained on the containment-aware overlap used by the downstream recovery decision. We define a hash-bound evaluation protocol with disjoint development, calibration, internal-test, and quarantined external-holdout roles. The sealed, single-seed candidate reaches native containment micro-$F_1$ 0.9344 on the internal test and 0.8477 on the one-shot external holdout (95% PDF-cluster bootstrap interval [0.8339, 0.8605]). This passes the registered historical FFGBT-v8 reference by 0.0186 absolute $F_1$. Under the stricter external adapter, however, performance is 0.7786 IoU-$0.5$ $F_1$ and 0.2900 COCO mAP, below a locally evaluated CommonForms-L reference; the signature class receives no prediction at the selected threshold. Thus the result supports the registered operational gate while exposing substantial domain and rare-class limitations.

---


### 177. [TransHands: Repurposing Human Pose Encoders as Hand Pose Encoders](https://arxiv.org/abs/2608.22341)

**<font color=#1a73e8>作者：</font>** Milo Piccioli, Gianluca Amprimo, Claudia Ferraris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifting 3D hand poses from 2D monocular representations remains challenging due to the limited availability of large-scale, diverse 3D-annotated hand datasets, in contrast to the abundance of human body motion data. We address this limitation by transferring motion representations learned from large body pose corpora to the hand domain. We introduce TransHands, a backbone-agnostic transfer learning framework that enables pre-trained human motion encoders to be effectively adapted for 3D hand pose estimation from 2D pose inputs. Rather than training hand-specific biomechanical models from scratch, TransHands combines a two-stage training and fine-tuning strategy with a lightweight hand-specific input adaptation module that aligns hand kinematics with the representation space learned for full-body motion. We evaluate TransHands across four state-of-the-art motion modeling architectures, including transformer-based, graph-based, and frequency- domain models. Results demonstrate that motion priors learned from body pose data transfer consistently across architectures, yielding consistent accuracy gains, strong cross-domain generalization, particularly in challenging egocentric settings, and applicability for downstream tasks in real-world contexts.

---


### 178. [Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior](https://arxiv.org/abs/2608.22344)

**<font color=#1a73e8>作者：</font>** Zi-Ming Wang, Kai-Wen Duan, Kowei Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) achieves state-of-the-art rendering quality at real-time speeds but suffers from "model bloat" - a large number of redundant, low-opacity Gaussians that inflate memory usage and training costs. This inefficiency stems from the standard "densify-then-prune" paradigm, which expands the model aggressively before relying on pruning to achieve compactness. To mitigate this problem, we present an efficient training framework that builds an intrinsically compact representation, replacing the conventional densify-then-prune cycle. Our method leverages a synergistic design: an L2 reconstruction loss to provide error-proportional gradients that stabilize optimization, and a novel Polarized Opacity Prior (POP) to actively manage the Gaussian population. POP steers informative primitives toward full opacity and uninformative ones toward transparency, enabling natural pruning and accelerating rendering through Early Ray Termination. Experiments on three public datasets demonstrate that our approach consistently achieves accelerated 3DGS training with significantly fewer Gaussians while maintaining comparable visual reconstruction quality. These results show that the proposed framework provides a simple and effective path toward fast and inherently compact 3DGS training.

---


### 179. [Multimodal examination answer data with expert-designed Outcome-Based Education rubrics for criterion-level assessment](https://arxiv.org/abs/2608.22346)

**<font color=#1a73e8>作者：</font>** Jahangir Alam SM, Md Khalid Syfullah, Saad Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This data article describes a multimodal collection of scanned examination answers paired with expert-designed Outcome-Based Education (OBE) grading metadata. The collection contains 485 answer submissions from 415 consenting students at four academic institutions. Eight faculty contributors supplied examination materials covering nine subjects and 12 distinct question templates. Each answer-level item links a scanned PDF to a randomized identifier, subject label, question, model answer, criterion definitions, performance-level descriptions, criterion marks, and a total mark. The 12 rubrics contain 47 criteria in total. The scans retain realistic academic content, including handwriting, printed text, equations, tables, code, figures, sketches, and diagrams. CamScanner, Adobe Scan, and conventional scanners contributed variation in illumination, contrast, orientation, compression, and resolution. Diverse handwriting, crossed-out work, revised calculations, and inserted corrections add further visual variability for robustness and generalization studies. Preparation involved heterogeneous-source consolidation, label and text standardization, score validation, identifier randomization, filename randomization, and JSON-to-PDF integrity checks. An answer-level audit confirmed 485 unique identifiers, 485 unique PDF filenames, agreement between each total mark and its criterion-mark sum, and scores within the applicable rubric maximum. The data can support rubric-aware automated evaluation, multimodal document understanding, criterion-level feedback, score prediction, and privacy-aware OBE assessment research. Access is restricted to research use and is available from the corresponding author upon reasonable request.

---


### 180. [SANE: State Anomaly Neutralization for Stable Extreme-Context Delta-Rule Models](https://arxiv.org/abs/2608.22354)

**<font color=#1a73e8>作者：</font>** Qingwen Lin, Boyan Xu, Xiao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Delta-Rule recurrent models maintain a fixed-size state, enabling $O(1)$ inference memory but potentially becoming unstable under extreme-context extrapolation. By tracking RWKV-7 over sequences of up to 100M tokens, we empirically identify a distinct failure pattern: \textbf{localized norm explosion atop a relatively sparse substrate}, rather than global state saturation. Analysis of the recurrent update suggests that persistent decay keeps weakly updated entries small, whereas uneven injections allow a few channels to accumulate extreme values. Motivated by this diagnosis, we propose \textbf{State Anomaly Neutralization (SANE)}, which applies adaptive $\tanh$ compression at chunk boundaries while preserving the intra-chunk parallel structure. Within a safe threshold range ($3 \le \alpha \le 5$), SANE matches the baseline on 11 short-context reasoning benchmarks with no statistically significant degradation. After a 100M-token prefix, which exceeds the training length by over $24{,}000\times$, SANE retains functional reasoning ($33.46$--$35.56$) while the baseline encounters numerical overflow. In contrast, overly permissive thresholds ($\alpha \ge 8$) remain numerically stable but lose reasoning capability entirely, showing that numerical stabilization alone does not guarantee functional reasoning and revealing a capacity--stability trade-off in state compression.

---


### 181. [Tracing the Unlabeled Storm: Cross-Variable Transfer in a Lagrangian Atmospheric JEPA Framework](https://arxiv.org/abs/2608.22358)

**<font color=#1a73e8>作者：</font>** K M Anirudh, S Sandeep, Hariprasad Kodamana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep atmospheric convection governs South Asian monsoon variability, yet attempting to learn its latent world model directly from zero-inflated, heavy-tailed precipitation yields suboptimal predictive representations. Continuous atmospheric proxies, such as outgoing longwave radiation (OLR), express this convective organization far more coherently. We address this mismatch with \emph{cross-variable proxy learning}: M-JEPA, a multiscale Monsoon Joint-Embedding Predictive Architecture, is pretrained on five continuous proxy fields over Lagrangian patches tracking moving convective systems---without rainfall supervision at any point. The resulting frozen representation is transferred to daily precipitation forecasts through a shared decoder trunk featuring parallel probabilistic and deterministic branches. Because rainfall is strictly unobserved during pretraining, downstream skill directly measures the predictive information captured in the latent rollout. A frozen-backbone probing framework with two controls (an identical architecture trained on rainfall alone, and a randomly initialized backbone) attributes the transfer specifically to proxy pretraining: direct rainfall training exhibits $36\%$ higher CRPS error ($7.52$ vs.\ $5.54$\,mm/day). Against the 51-member operational ECMWF ensemble, the transferred model attains a statistically resolved CRPS advantage ($6.81$ vs.\ $6.89$\,mm/day) and higher Brier skill ($+0.05$ vs.\ $-0.04$) using $15.4$M parameters on a single consumer GPU, concentrated at heavy-rain thresholds and fine spatial scales, while the ensemble retains an advantage in neighborhood skill and deterministic references on point metrics. The result provides a competitive monsoon precipitation forecast grounded in intraseasonal dynamics and a diagnostic framework for evaluating transferred atmospheric representations.

---


### 182. [MCSI: A Masked Commutative Supersingular Isogeny Key Exchange with Blinded Ephemeral Keys](https://arxiv.org/abs/2608.22360)

**<font color=#1a73e8>作者：</font>** Furkan Cifci, Osman Emre Donder, Reyyan Cifci  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce MCSI, a two message key exchange we design over the CSIDH class group action, in which each party sends its ephemeral public element under an authenticated encryption keyed by the value the two static keys determine. The design gives implicit mutual authentication, hides the ephemeral element from an eavesdropper, and lets a recipient discard an unauthenticated message after one tag check rather than after an evaluation of the group action, which is four orders of magnitude more expensive.
On the analytic side, we prove that our protocol is correct with zero error, and prove three statements in the random oracle model, all reducing to the strong parallelisation problem: indistinguishability of the session key against a passive adversary, confidentiality of the blinded ephemeral element, and integrity of the blinded transport. None uses the decisional group action assumption, which is false for class group actions of non-prime discriminant. We also show that a blinding key cannot come from the session secret it is meant to establish.
To instantiate the design we select parameters and show that a prime chosen for elliptic curve discrete logarithms is unusable: for $p = 2^{521}-1$, the NIST P-521 prime, the action admits no efficiently evaluable generator.
On the practical side, we build and test the design. We implement the protocol twice, in C and independently in Python, cross check the two, and measure what a session costs in field operations, time and memory. We also audit our code for secret dependent control flow: the field arithmetic and the symmetric layer show none, while the group action leaks the key by construction, and two hundred timings separate two keys whose one-norms differ by five out of 370.
Finally, we state what we do not prove, among them security under ephemeral key reveal, forward secrecy of the blinding, and constant time execution.

---


### 183. [DiD It in 87 Minutes: A Label-Free Softmax-to-Linear Adaptation of Vision Transformers for Object Detection](https://arxiv.org/abs/2608.22368)

**<font color=#1a73e8>作者：</font>** Huaiyuan Qin, Gabriel James Goenawan, Zihang Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While linear attention is a compelling mechanism for high-resolution object detection due to its reduced cost for global token mixing, converting the Softmax-attention ViT backbone of a trained detector into a linear-attention one is not a trivial drop-in replacement. Directly swapping the attention operator leads to severe performance degradation, and generic label-free distillation, though effective for classification, often fails on detection tasks. We argue that the central challenge is \textit{detector-interface preservation}: the converted backbone must reproduce the exact feature tensors expected by the fixed downstream detector, rather than merely imitating internal Softmax hidden states. To address this, we introduce Detector-Interface Distillation (DiD), a label-free conversion method that exclusively trains the linear-attention backbone by aligning detector-facing interface tensors with those of a frozen Softmax teacher. On DOTA-v1.5, DiD substantially outperforms established baselines and matches supervised, fully trained linear models. Adaptation completes in roughly 87 minutes on 4 GPUs, and the linearized backbone cuts inference latency by ~62% and peak memory by ~49%. We hope our findings offer the community a simple, label-free route to reusing trained Softmax detectors as efficient linear ones, and encourage interface-aware objectives in future architecture-conversion work.

---


### 184. [Self-Supervised Graph Representation Learning for In-The-Wild Wearable and Smartphone based Emotion Recognition](https://arxiv.org/abs/2608.22387)

**<font color=#1a73e8>作者：</font>** Ioannis N. Ziogas, Leontios J. Hadjileontiadis, Ahsan H. Khandoker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable and smartphone-based emotion recognition (WER) remains a challenging setting in affective computing, due to the notorious difficulty and bias associated with in-the-wild label collection. The high inter-and intra-subject emotional variability motivates us to explore WER modeling through graph node classification in a limited resources learning scheme powered by Self-Supervised Learning (SSL) graph masking augmentation tasks. We employ a subgraph sampling approach during training, utilizing labeled and unlabeled data, along with supervised, semi-supervised, and SSL mechanisms in a multi-task inductive graph neural network architecture. Our evaluations on K-EmoPhone through leave-one-group-out cross-validation in the binary arousal and valence tasks yield average accuracy gains of 4.3% and 7.8%, compared to the full resource setting, utilizing only 20% and 25% of the labels, respectively. Our model analysis sheds light on the relation of SSL graph augmentations to emotional arousal and valence and justifies the approach of SSL-driven subgraph training for in-the-wild WER.

---


### 185. [ProBel: Propaganda Detection with Techniques, Spans, and Explanations](https://arxiv.org/abs/2608.22388)

**<font color=#1a73e8>作者：</font>** Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Elisa Sartori 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Propaganda detection includes several related prediction levels, ranging from sentence-level decisions to technique classification and span identification. However, it remains unclear how supervision at these levels interacts when learned jointly across Arabic and English. We present ProBel, an Arabic and English resource that aligns binary labels, multi-label annotations over 23 propaganda techniques grouped into six coarse categories, technique-labeled spans, and reference explanations for the same news sentences. It includes a substantially larger English collection and supports matched binary, coarse-grained, multi-label, and span-level tasks in both languages. We evaluate zero-shot prompting, task-specific fine-tuning, and joint training under a shared setup. A single bilingual multi-task model achieves the best overall performance and remains competitive across tasks and languages. Cross-task analysis shows that transfer depends on the supervision level. Joint classification training preserves binary performance, whereas span-only training can weaken sentence-level prediction. Joint bilingual training yields the most stable results, while monolingual fine-tuning can reduce transfer to the other language. We will release the data, code, and evaluation scripts.

---


### 186. [KONTOGRAPH: Verified Point-in-Time Feature Consistency and Amortised Explanation for Real-Time Anti-Money Laundering under a 200 ms Decision Budget](https://arxiv.org/abs/2608.22389)

**<font color=#1a73e8>作者：</font>** Ahmed Abolfadl  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Regulation (EU) 2024/886 obliges European payment service providers to settle euro credit transfers in under ten seconds, around the clock. This removes both the overnight batch window in which anti-money-laundering (AML) analytics traditionally ran and the settlement delay that made recovery possible, forcing detection, explanation and decision inside a single-digit-second envelope. We present KONTOGRAPH, an end-to-end AML pipeline for the SEPA Instant rail built under a self-imposed 200 ms 99th-percentile budget, and report an empirical study on 1,562,860 simulated payments with injected typologies and deliberately incomplete labels. Three findings are of interest beyond the system itself. First, a temporal graph network with per-node memory improves PR-AUC over a gradient-boosted tabular baseline from 0.0053 to 0.1717, a paired day-blocked bootstrap difference of +0.166 with 95% CI [0.105, 0.241]; per-node memory alone more than doubles the score. Second, expressing each feature once and compiling it to three execution backends, with equivalence enforced by property-based tests that perturb the future, surfaced three point-in-time violations that code review had passed--each of which would have inflated reported performance. Third, and most consequential for practice, exporting the deployed tree ensemble to ONNX changed only $7.4 \times 10^{-8}$ in mean score yet altered 0.26% of decisions and inflated the alert volume by 12%, because 32-bit accumulation perturbs scores across a cost-optimal threshold of $3.98 \times 10^{-4}$. We argue that a serving-format conversion must be treated as a model change until measured, and that fidelity metrics for subgraph explainers can be vacuous when candidate neighbourhoods are small--a null result we report in full.

---


### 187. [Dual-Scale State-Space Modeling with Speaker-Wise Dynamic CRF for Speech Emotion Recognition in Conversation](https://arxiv.org/abs/2608.22399)

**<font color=#1a73e8>作者：</font>** Guan-Hua Wen, Kuan-Yu Chen, Hou-Chiang Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conversational speech emotion recognition must reconcile acoustic evidence across temporal scales with two interaction processes: cross-speaker contextual influence and within-speaker emotion evolution. We propose DSSM-CRF, an audio-only architecture that explicitly separates these processes. Bidirectional state-space models encode fused self-supervised speech representations at frame and dialogue scales, so each utterance representation captures local prosody and context from all speakers. The decoder then orders each speaker's utterances into an independent dynamic conditional random field chain. Consecutive utterances in a speaker's chain form a transition pair whose score combines a corpus-level transition matrix with a residual predicted from the two contextualized utterances. An auxiliary objective supervises whether each pair changes emotion but does not participate in Viterbi inference. Thus, interlocutor turns affect contextual emotion scores without being treated as transitions in another speaker's emotion trajectory. DSSM-CRF achieves 75.81% UA and 74.90% WA on IEMOCAP, and 54.72% WA and 49.31% WF1 on MELD. Matched controls demonstrate complementary gains from speaker-wise factorization and CRF modeling.

---


### 188. [Where World Models Break: Natural-Input Failure Discovery](https://arxiv.org/abs/2608.22421)

**<font color=#1a73e8>作者：</font>** Zhanpeng Shi, Zi Liang, Rong Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from general queries, they fail to stress-test the model against catastrophic collapses under rare or unobserved condition-action combinations. To bridge this gap, we formalize the natural-input failure discovery problem: under a finite query budget, finding environment-valid conditions and action prefixes that induce severe prediction risk, verifying whether these failures reproduce on fresh seeds, and testing their persistence under nearby valid edits. Discovering such critical failures is computationally challenging, as valid condition-action combinations explode exponentially, rendering exhaustive search or standard sampling infeasible given the high cost of noisy rollouts. To tackle this, we propose BasinLens, which exploits the underlying structure of valid inputs, where each coordinate possesses environment-defined semantic types and admissible domains, by pairing uncertainty-guided global search with typed local replacements. Across diverse benchmarks and world-model families, BasinLens exposes reproducible and locally persistent failure modes that conventional evaluations fail to reveal, showing that average-case benchmarks can mask important vulnerabilities in world-model-driven control.

---


### 189. [Probing How Users Interact with Turn-Level Design Frictions for AI Chatbots](https://arxiv.org/abs/2608.22427)

**<font color=#1a73e8>作者：</font>** Helen Weixu Chen, Katy Ilonka Gero  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI chatbots can help people write faster, but they can also encourage overreliance by making it easy to turn minimal input into usable text. We study turn-level design friction: intentional constraints added to each chatbot exchange that slow, limit, or redirect how users request, access, or use model responses. We designed six friction probes, organized around three mechanisms: eliciting user contribution, restricting access to generated content, and reshaping system output. In a within-subject study with 24 participants, all six probes increased workload, task duration, and perceived ownership relative to a conventional AI chatbot, while their effects on recall and recognition were more selective. We further found that participants adapted to friction in different ways, and that the same constraint could support or obstruct involvement depending on users' goals and workflows.

---


### 190. [Figurative Justice: Detecting metaphors in Hindi judgements with qualitative assessment and transformers](https://arxiv.org/abs/2608.22446)

**<font color=#1a73e8>作者：</font>** Bhumika Bhattacharyya, Shouvik Kumar Guha, Indranil Dutta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphors are figurative use of words for conceptual mapping. Metaphor detection in the legal context has been crucial as metaphors are persuasive juridical means of creating legal meaning and concepts resulting in significant consequences. Metaphorical framing in legal discourse by judges, lawyers, and legislators brings about real-time implications upon individuals and influences judicial decision-making, argumentation and interpretation of laws. This is crucial in Human Rights infringement cases where language determines severity of punishment, public perception and judicial outcomes.
While automatic metaphor detection in major languages like English, Spanish, Polish, Lithuanian have aided in understanding inherent intentions of metaphorical use of language, there is no such attempt in low-resource languages like Hindi. The dearth of annotated legal corpora in Hindi makes it difficult to develop NLP models and detect metaphors in judicial proceedings. In the Indian context, Convolutional Neural Networks (CNNs) have been used for classification of bail judgements, however there are no existing models designed for metaphor detection.
We present a Hindi Legal Metaphor Corpus (HiLeMe) by isolating judgements from Hindi Legal Data Corpus (HLDC). Legal experts annotated HiLeMe to classify metaphorical constructions using the MIPVU schema. We downstreamed an mBERT on Hindi legal metaphor detection task. We built a transformer-based architecture for metaphor detection that are known to outperform traditional models in legal classification tasks. This model provides insights into the judicial psyche for decoding judicial decisions. Our research contributes to advancing automated models in legal discourse in low-resource languages like Hindi and envisages adoption into 22 Indian schedule languages.

---


### 191. [Geometric Structures on Graphs: a Holonomy-Based Discretization of Curvature](https://arxiv.org/abs/2608.22453)

**<font color=#1a73e8>作者：</font>** Hao Li, Yuhan Peng, Junwen Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a holonomy-based framework for discretizing curvature on graphs equipped with local symmetric positive-definite metrics. Each vertex carries a fibre metric \(g_i\), and each directed edge carries a reversible metric-compatible transport \(F_{ij}\). The ordered product around an oriented triangular loop \(\mathcal C\) gives a holonomy \(H_{\mathcal C}\), whose normalized logarithm \(\Omega_{\mathcal C}=-s_{\mathcal C}^{-1}\operatorname{Log}(H_{\mathcal C})\) is used as a finite-loop curvature observation. Thus the construction discretizes the geometric principle that infinitesimal holonomy is controlled by curvature, rather than treating holonomy as a heuristic feature. Since \(\Omega_{\mathcal C}\) lies in the \(g_i\)-orthogonal Lie algebra, it is not itself a velocity of an SPD metric. We therefore introduce two aggregation mechanisms: a commutator with a symmetric response matrix, producing symmetric Ricci-type metric responses, and an incidence-aware covariant divergence of curvature-induced edge fluxes, reflecting the relation between trace and covariant divergence. The resulting responses are locally orthogonal-gauge equivariant and can drive exponential updates that preserve positive definiteness. We also give a reversible metric-compatible parametrization of edge transports, allowing orthogonal edge factors, loop scales, weights, and response matrices to be learned while respecting the graph geometry. Known-geometry calibrations on the unit sphere test the holonomy--curvature relation, curvature preservation under nontrivial local metric representations, and the empirical recovery of edge transports from local observations.

---


### 192. [KPI-Conditioned Generative Design of Automotive Hood Inner Panels: A Two-Stage Retrieval-Generation Pipeline with Surrogate-Based Performance Estimation](https://arxiv.org/abs/2608.22457)

**<font color=#1a73e8>作者：</font>** Sudeep Chavare  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An inner hood panel must meet a deflection target, stay below a stress limit, and hit a mass target. Machine-learned surrogates have made the forward direction, geometry to performance, fast and routine. The inverse direction, producing geometry from a stated requirement, remains largely unaddressed for industrial parts whose design space is organized into discrete topology families rather than a continuous parameterization. This work presents a two-stage pipeline for that inverse problem. A reachability stage determines which topology families can satisfy a given requirement vector. A conditional variational autoencoder then generates point-cloud geometry within a selected family, and a neural-operator surrogate estimates the performance of each candidate. The pipeline is built entirely from public data and freely available compute, and is deployed as an interactive tool. The pipeline works, with qualifications that are reported as primary findings rather than caveats. The surrogate is accurate in aggregate, but its error is comparable to the performance differences it is asked to discriminate, which bounds what can be claimed for any individual generated design. That ratio of surrogate error to within-class signal is argued to be the quantity that determines whether a pipeline of this kind can work at all.

---


### 193. [MASH-Bench: Diagnosing Cross-Source Failure in Mass-Shooting Risk Classification](https://arxiv.org/abs/2608.22460)

**<font color=#1a73e8>作者：</font>** Neha Sharma, Ritesh Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public mass-shooting databases differ substantially in coverage, feature availability, and reporting practices, creating challenges for machine-learning models that must generalize across data sources. We introduce MASH-Bench, a harmonized benchmark of 6,968 incidents from four U.S. databases: Kaggle, Mother Jones, Stanford MSA, and the Gun Violence Archive (GVA). We evaluate cross-source risk classification using leave-one-dataset-out (LODO) evaluation. Random Forest, XGBoost, and LightGBM achieve VeryHigh-risk recall of 0.68-0.89 on the curated sources but generalize poorly to GVA, where mean recall drops to 0.20 and precision to 0.0004. To investigate the source of this degradation, we conduct a controlled feature-masking ablation that removes the five features unavailable in GVA from the curated sources. The resulting recall collapse to zero provides evidence that feature completeness is a major contributor to the observed cross-source failure. We further evaluate three domain-adaptation approaches: DANN, CORAL, and importance weighting. DANN improves VeryHigh-risk recall on GVA by 0.282 (95% CI [0.11, 0.47], p = 0.003), although precision remains low, whereas CORAL and importance weighting yield zero recall. Oracle prior-shift recalibration likewise fails to recover VeryHigh-risk predictions, indicating that label-side correction alone is insufficient under the observed feature deficiencies. A per-group audit further identifies substantial disparities associated with media-attributed mental-health labels. Overall, these results indicate that, in MASH-Bench, cross-source generalization is constrained more by feature completeness and label prevalence than by classifier choice. The benchmark provides a controlled setting for diagnosing these effects in cross-source risk classification.

---


### 194. [Functional compatibility as a determinant of persistent neural learning](https://arxiv.org/abs/2608.22462)

**<font color=#1a73e8>作者：</font>** Hossein Javidnia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial neural networks can acquire new capabilities but often damage existing ones when they continue to learn. This stability-plasticity problem has motivated replay, regularization and constrained-update methods, yet it remains unclear whether a property of incoming learning itself determines what can be retained without disrupting protected behaviour. Here we show that functional compatibility, the extent to which new learning can coexist with behaviour that must be preserved, is a causal determinant of persistent learning. To our knowledge, this is the first controlled causal demonstration in which compatibility is deliberately changed from matched neural states and persistent learning is measured under a common retention requirement. The effect generalizes across independent learning directions, convolutional and transformer architectures, vision and text, and additional seeds. Learning rules differ in how efficiently they exploit available compatibility, while retention constraints limit how much can be stored. At larger finite updates, nonlinear geometry changes the available learning opportunity and ultimately prevents the matched compatibility continuum from being realized. These results establish functional compatibility as an experimentally controllable principle of persistent neural learning, shifting the problem from preventing forgetting towards identifying which components of new learning can safely become permanent.

---


### 195. [M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465)

**<font color=#1a73e8>作者：</font>** Xinhui Liu, Lei Liu, Zhenghao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity free-viewpoint video (FVV) and interactive rendering increasingly rely on explicit Gaussian representations, yet practical deployment remains constrained by representation size, dynamic updates, and computational cost. Existing multi-view video benchmarks provide valuable real-captured content, but they make it difficult to isolate the effects of controlled camera geometry, representation efficiency, and temporal redundancy. We introduce M$^3$ISR, a controlled synthetic benchmark for 3D and 4D Gaussian Splatting (3DGS/4DGS). The benchmark contains 25 scenes from five indoor and outdoor scene groups, two camera/motion configurations, six synchronized 1080p views, and dense ground-truth annotations including RGB, camera parameters, depth, semantic and instance segmentation, and static--dynamic masks. The shared-center camera design intentionally isolates angular view variation and enables controlled evaluation of novel-view synthesis and representation efficiency. We organize M$^3$ISR into five complementary tracks covering 3DGS synthesis, 4DGS synthesis, 4DGS streaming, 3DGS compression, and 4DGS compression. Representative baseline results show small differences in static reconstruction quality but substantial differences in representation storage, while the evaluated streaming methods exhibit substantially higher reported training or reconstruction cost than the corresponding offline dynamic reconstruction baselines. We further define feedforward compression tasks for 3DGS and 4DGS and provide reference rate--distortion formulations and preliminary baseline evaluations. The benchmark is intended as a controlled and complementary testbed for systematic study of Gaussian-based FVV reconstruction, compression, and streaming.

---


### 196. [Quantum-Inspired Hybrid Neural Networks for Neural Decoding: A Controlled Ablation Study of Learnable Quantum Sidecar Integration](https://arxiv.org/abs/2608.22475)

**<font color=#1a73e8>作者：</font>** Diana Legziel Levy, Menachem Finkelstein, Peter Chin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study parameterized quantum circuits (PQCs) integrated as residual sidecar modules within a ResNet-50 backbone for 31-class neural population decoding---imagined handwriting classification from multi-neuron spike rasters. Under strictly controlled conditions (fixed data splits, seeds, and optimizer), we compare four model variants: baseline, quantum sidecar with frozen input projection, quantum sidecar with backbone-gradient-trained projection, and a measurement-guided variant that aligns angle encodings with circuit measurement outcomes. The backbone-gradient variant improves accuracy in 3/4 seeds (+0.19% mean, 95% CI [-1.10%, +1.48%]) and consistently reduces Linear CKA similarity to baseline features ($\Delta=-0.025$, 4/4 seeds), indicating genuine structural reorganization of representations. A nine-variant ablation identifies simple shallow architectures as the most effective and reproducible configuration. Measurement-guided training consistently improves representation geometry without reducing accuracy. All results use noiseless statevector simulation on 4 qubits, a regime chosen to reflect the practical constraints of current near-term superconducting hardware; no quantum computational advantage over classical methods is claimed.

---


### 197. [Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages](https://arxiv.org/abs/2608.22490)

**<font color=#1a73e8>作者：</font>** Chanwoong Yoon, Jungsoo Park, Alan Ritter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment helps models adhere to human values, but it often reduces response utility. We ask a critical but understudied question: Does safety alignment impose the cost equally across language groups? To answer this, we introduce a rigorous protocol to measure the utility loss imposed solely by safety alignment, which we term Safety Cost. Through direct pairwise comparisons between safety-aligned models and their unaligned counterparts, we find a systematic inequity: non-English users consistently bear a higher Safety Cost than English users. We further identify three underlying patterns. First, multiple languages lie in a double-penalty zone, experiencing both weaker safety protection and larger utility loss. Second, certain languages exhibit apparent utility gains that are in fact a consequence of safety filters failing to engage. Third, even high-resource languages pay a larger Safety Cost than English to reach the same level of safety. We show that these disparities arise from both explicit refusals and implicit qualitative differences across multiple dimensions. By accurately measuring the disparate effects of safety alignment, our findings expose a systematic disparity in current safety alignment practices.

---


### 198. [When Does AI for PDEs Yield Scientific Evidence?](https://arxiv.org/abs/2608.22504)

**<font color=#1a73e8>作者：</font>** Wenshuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing AI-for-PDE benchmarks primarily assess models in terms of predictive or approximation accuracy. In physics research, however, AI outputs often serve as evidence for scientific claims. These two objectives are not equivalent: the former measures an output's agreement with a reference target or satisfaction of governing constraints; the latter asks whether, given a specified object of study, scientific claim, assumptions, and evidence standard, the output provides sufficient evidence for that claim. To bridge this gap, we extend a widely used PDE-simulation benchmark and a comprehensive benchmark for PDE inverse problems to enable, for the first time in AI for PDEs, evaluation of whether and to what extent model outputs support specified scientific claims. Our results show that numerical accuracy and evidential support can rank models differently, explain when and why they do so, and reveal that existing benchmarks can favor methods whose outputs provide weaker support for the scientific claims of interest. Together, we formalize, empirically demonstrate, and explain this evaluation--use mismatch in AI for PDEs.

---


### 199. [ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts](https://arxiv.org/abs/2608.22510)

**<font color=#1a73e8>作者：</font>** YuanHang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks often evaluate only final answers even when agents run on stateful runtimes. We argue this under-specifies what is being evaluated: the proper unit is a declared model-plus-runtime configuration whose failures can occur in evidence acquisition, runtime routing, safety boundaries, or repeated execution. We present ClawProBench, a trace-aware benchmark for runtime-native agent evaluation instantiated on OpenClaw, a live agent runtime with workspace tools and native surfaces for browsing, memory, messaging, scheduling, skills, and subagents. ClawProBench defines two tracks: a 102-scenario full profile with live workspace and native-runtime routing tasks, and a frozen 68-scenario holdout with closed-world JSON output contracts for robust ranking. Trials are scored from execution traces via a safety-gated formula combining correctness, process quality, and efficiency, preserving failure evidence for audit. Our anonymous artifact includes benchmark definitions, scoring code, manifests and sanitized traces. We evaluate 68 configurations on the full profile and 37 on holdout. The top safety-gated average trace score is 0.7671. Native-runtime tasks underperform workspace-live tasks (0.5238 vs. 0.6415). On holdout, pass@k-any outperforms strict three-trial pass (0.6638 vs. 0.2890), while full-profile and holdout rankings show weak alignment (Spearman 0.1300). Rankings based purely on correctness differ substantially from process-aware, safety-gated and strict-pass views. Final-answer leaderboards may hide native-surface weaknesses, one-off successes and trace-local agent failure modes.

---


### 200. [HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems](https://arxiv.org/abs/2608.22512)

**<font color=#1a73e8>作者：</font>** Christos Sardianos, Iliana Pla, Vasilis Efthymiou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, attribution laundering, i.e., spreading an act across redundant agents until none is a but-for cause. Worse, the record is produced by the suspects, which comprises the assumption adopted throughout this work. Agents may therefore anticipate the investigation and the part of logging infrastructure may itself collude. In this paper, HANSARD is proposed, a reference architecture treating accountability as a life-cycle property. First, a readiness profile sealed before operation bounds what later findings may claim. Second, capturing at five choke points beyond the agents' reach makes omissions detectable, not only tampering. Third, a typed PROV-DM-aligned causal graph accrues as the system runs, and three indicators read it live to gate oversight without adjudicating. Fourth, post-incident replay yields contingent effects under the modified Halpern-Pearl definition, together with a compensation-set size. Finally, a synergy residual measures harm due to the combination rather than to individuals, making laundering visible. Cause, responsibility and accountability are then reported separately, each capped by an evidentiary tier, while a future research agenda is also provided.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
