# 📦 其他研究 | 2026年10月22日

> 本类共 **288** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 151. [Privacy Accounting for Empirical Denoisers](https://arxiv.org/abs/2610.27710)

**<font color=#1a73e8>作者：</font>** William Cheng, Mijung Park, Dongjun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as the foundation of modern generative systems, yet their high memorization capacity raises privacy concerns. While differentially private (DP) training provides formal guarantees, it comes at a cost in sample quality. In this work, we study a complementary question: how much privacy loss is incurred during the sampling process itself? Directly analyzing modern neural denoisers is challenging because their sensitivity to a single training example is generally intractable. To overcome this challenge, we construct and analyze a clipped privacy-accountable empirical denoiser, a training-free estimator of the Bayes-optimal denoiser, whose per-step sensitivity can be computed explicitly, allowing each denoising step to be a Gaussian mechanism. This perspective enables privacy accounting under Gaussian DP when each training example contributes to each denoising step, and under $f$-DP trade-off functions when each generated sample uses a single randomly subsampled block of the training data. We report every $(\varepsilon, \delta)$ guarantee as a certified upper bound from a privacy loss distribution accountant, and use a cumulant-based Edgeworth approximation as a fast diagnostic, characterizing where it is reliable and where it becomes anti-conservative. We also analyze the privacy loss along the denoising trajectory and show that it grows steeply near the critical window in which semantic content is formed. This observation motivates hybrid samplers that use the private empirical denoiser through the formative steps where it remains a faithful proxy for the neural denoiser, then switch to a public neural denoiser for the remaining refinement. Our results on CIFAR-10 and CelebA-64 show that the privacy of diffusion models depends not only on the training procedure, but also on sampling-time design choices such as subsampling, stopping time, and hybrid denoising.

---


### 152. [RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.27712)

**<font color=#1a73e8>作者：</font>** Injae Kim, Minseok Joo, Jihwan Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (FF3DGS) reconstructs 3D scenes from images in a single forward pass, making it well-suited to applications that must operate within limited resource budgets. To further improve its practicality, recent budget-controllable FF3DGS methods allow the number of Gaussians to be adjusted at inference, so that the output meets a given storage limit or rendering-latency constraint. However, these methods overlook the cost of inference itself: to produce a representation with the target number of Gaussians, they first predict a dense set of Gaussians and then prune or select from it, requiring nearly constant latency and peak memory regardless of the budget. We therefore propose RLSplat, a resource-linear budget-controllable FF3DGS framework whose representation size, inference latency, and peak memory all decrease linearly as the Gaussian budget is reduced. Instead of pruning or selection, RLSplat learns a Gaussian allocation policy that distributes the budget across local scene regions, so that exactly the requested number of Gaussians is generated. These Gaussians are then refined through resource-linear Gaussian decoding, in which each Gaussian attends only to nearby Gaussians found via an efficient hierarchical neighbor search, so that the decoding cost decreases linearly with fewer Gaussians. In zero-shot evaluation, RLSplat outperforms prior budget-controllable methods at every budget, surpassing the strongest baseline even with 4$\times$ fewer Gaussians, while running up to 4.1$\times$ faster with 9.6$\times$ less peak memory at low budgets.

---


### 153. [Push-Pull Attentional Anchoring for Diffusion Concept Erasure](https://arxiv.org/abs/2610.27719)

**<font color=#1a73e8>作者：</font>** Nattanat Chatthee, Tagon Sompong, Ekapol Chuangsuwanich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advances in diffusion models have raised concerns about privacy, harmful content, and copyright violations. Concept erasure methods aim to address these risks by removing undesirable concepts from pretrained models without full retraining. However, existing approaches often degrade non-target generation quality through heuristic strength scaling (e.g., classifier-free guidance or negative prompt scaling), leading to uncontrolled and excessive semantic drift. To address this, we propose Push-Pull Attentional Anchoring (PPAA), a mechanism in the cross-attention space that displaces target representations while anchoring the scale of erasure via bounded cosine-similarity constraints. By using a relative similarity ratio instead of an absolute difference, our adaptive threshold represents a meaningful percentage of semantic retention, facilitating a single value to be applied uniformly across layers. We conduct extensive experiments across multiple concept categories, including celebrities, artistic styles, nudity, and intellectual property. Our method achieves favorable trade-offs against prior approaches on Stable Diffusion v1.4 and demonstrates its applicability to modern architectures such as FLUX.

---


### 154. [World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation](https://arxiv.org/abs/2610.27725)

**<font color=#1a73e8>作者：</font>** Jiushu Li, Haoran Wang, Yumeng Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon human-object-scene interaction (HOSI) is central to embodied AI, animation, and game development. Existing human-object interaction (HOI) and human-scene interaction (HSI) models excel in their respective domains, but none alone covers tasks requiring multiple interaction skills. Training unified HOSI models is hindered by scarce and costly data. We introduce World2HOSI, a multi-expert orchestration harness that generates continuous HOSI data from 3D Gaussian Splatting (3DGS) scenes and natural language instructions. Our key insight is that long-horizon HOSI hinges not on a stronger single model but on orchestration. Given a shared, structured scene state and an orchestration harness grounded in it, existing experts can jointly accomplish tasks beyond the reach of any of them alone. World2HOSI realizes this insight as a closed loop around a persistent scene state built from decoupled background and object assets. A harness plans action stages over this state, invokes experts via their native conditioning interfaces, and writes each action's effects back, so that every invocation is grounded in the evolving world. To reduce physical artifacts, bounded residual optimization and contact-driven physics simulation further ensure the physical plausibility of human motion and object manipulation, respectively, while preserving interaction intent. Experiments and a perceptual user study show that World2HOSI achieves the best task completion and interaction quality on the evaluated HOSI tasks, while generating more diverse data.

---


### 155. [CILA: Confusion-based Instance-wise Logit Adjustment for Long-Tailed Recognition](https://arxiv.org/abs/2610.27728)

**<font color=#1a73e8>作者：</font>** Jiyoung Lim, Jee-Hyong Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world datasets are inherently class-imbalanced, leading models to favor majority classes and struggle with minority ones. Existing logit adjustment methods address this by modifying logits based on class frequencies, but their class-wise adjustments ignore instance-wise confusion and often suppress informative signals from confusing non-target classes. This results in insufficient learning of such classes, increased prediction uncertainty, and limited generalization.
To address this, we propose two complementary methods. First, \textbf{Confusion-based Instance-wise Logit Adjustment (CILA)} adaptively adjusts logits based on instance-wise confusion between the target and non-target classes, restoring informative gradients that class-wise adjustment suppresses. Second, \textbf{Batch-adaptation Noise-Injection (BNI)} perturbs the target logit during training, extending the confusion-aware update to correctly classified but near-boundary samples that the penalty alone cannot reach. CILA is a loss-agnostic plug-in module that can be seamlessly integrated into existing long-tailed learning methods, and consistently improves performance across multiple benchmarks. Our code will be available at this https URL.

---


### 156. [EEG-Based Classification of Hypnotic Susceptibility Using Two-Dimensional Convolutional Neural Networks](https://arxiv.org/abs/2610.27738)

**<font color=#1a73e8>作者：</font>** Krzysztof Wrobel, Grzegorz M. Wojcik, Filip Postepski 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guided Imagery (GI) is a mind-based relaxation technique widely used in clinical and therapeutic settings. Objectively assessing whether a patient has entered a relaxed state remains a challenge for clinicians. This study investigates electroencephalography (EEG)-based classification of hypnotic susceptibility using two-dimensional Convolutional Neural Networks (2D CNNs) applied to minimally preprocessed signals, without manual feature extraction. Data were collected from 62 male participants (32 Control, 30 Hypno) using a 256-channel dense array amplifier during Guided Imagery or cognitive task conditions. A sliding-window framework evaluated up to 868 independent models across seven anatomically defined brain regions and 124 ten-second time windows. Segment-level random-split screening was followed by Leave-One-Subject-Out (LOSO) cross-validation to obtain subject-independent performance estimates, and an ensemble approach combined predictions across K = 10 windows. The best single-window model achieved accuracy of 0.82 on the random split. Under LOSO, anterior regions generalised better across subjects: the frontal region achieved mean accuracy of 0.646 (AUC: 0.692). An ensemble of K = 10 windows further improved the prefrontal region to mean accuracy of 0.738. The occipital region, dominant in random-split screening, collapsed to near-chance under LOSO, revealing subject-specific EEG fingerprinting rather than genuine group differences. Bandpass filtering and z-score normalisation suffice for competitive EEG classification without manual feature extraction. Anterior cortical regions are identified as the most generalisable neural markers of hypnotic susceptibility.

---


### 157. [S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with 500 Million Household Persona Agents](https://arxiv.org/abs/2610.27746)

**<font color=#1a73e8>作者：</font>** Yang Li, Di Wan, Yike Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Simulating economic responses at society scale requires agents whose decisions reflect household circumstances and the effects of earlier actions. We introduce S$^2$-MAS, a society-scale multi-agent simulation framework built on 500 million synthetic household personas grounded in real-survey data. Its Genese engine separates decisions from state updates, while reusable financial scenarios and application ledgers track consumption, cash, debt and payments. FinL-mlx, a compact decision model trained with SFT + RLCD on 2.93 million examples, achieves 74.55% accuracy and 38.37% question-macro F1 in consumer financial-choice scenarios, outperforming Jev 1.13 and GLM-5.3-Flash on both measures. We evaluate eight financial task families and simulate 12 million distinct household agents in paired purchase-funding conditions. Jointly raising purchase goals and approved credit limits increases consumption, with responses differing across age and income groups. Education, employment and household-size differences persist after age--income standardization and mainly reflect transitions from deferral to purchase. Asset and debt groups differ in cash drawdown, repayment and closing debt. A 24-month panel varies purchase goals under a common credit product, with repayment and arrears updating subsequent offers. S$^2$-MAS links heterogeneous household decisions to evolving consumption, cash and repayment paths, supporting economic experiments across household groups, population scales and time horizons.

---


### 158. [Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics](https://arxiv.org/abs/2610.27747)

**<font color=#1a73e8>作者：</font>** Pratik Jawanpuria, Bhabatosh Garai, Bamdev Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon and related optimizers update a weight matrix with a spectrally transformed gradient. In this work, we study such spectral optimizers with a constant step size on strongly convex matrix quadratics, which isolate the effect of the update from the confounds of nonconvexity, noise, and step size schedules. We analyze an update using two quantities: the gain, which is the factor by which it amplifies the gradient along each singular direction, and the length, which is the norm of the update. These two quantities place the popular spectral updates in three regimes with different behavior: (i) with a bounded gain, the iterates behave like preconditioned gradient descent and converge for step sizes set by the largest curvature; (ii) with an unbounded gain but a vanishing length, they still converge, with the admissible step sizes set by the total curvature instead; and (iii) with a non-vanishing length, they do not converge for almost every initialization. Interestingly, the practical variants of Muon fall in all three regimes, depending only on how the update is normalized and scaled and not on the polynomial that approximates the polar factor. Experiments validate these findings.

---


### 159. [Detection of Memorization in Diffusion Models Through Thermodynamic Singularity](https://arxiv.org/abs/2610.27754)

**<font color=#1a73e8>作者：</font>** Iljung Kim, Kangwoo Park, Yung-Kyun Noh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In diffusion models, proper distributional learning entails reversing a diffusion process over underlying density functions, whereas a key failure is memorization, in which the reverse process instead learns diffusion from individual training samples. We provide an analytical characterization of such memorized reverse processes, along with a criterion that detects the associated thermodynamic singularity. The proposed criterion reliably distinguishes between properly learned and memorizing networks across a range of neural network models designed to promote or mitigate memorization.

---


### 160. [Revealing Inter-Channel Modality Discriminability: Channel Selective Interaction Fusion Network for Optical-SAR Object Detection](https://arxiv.org/abs/2610.27757)

**<font color=#1a73e8>作者：</font>** Haojie Li, Yuanfei Huang, Lingfei Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar (SAR) and optical imagery provide complementary structural and appearance information for remote sensing object detection. However, substantial cross-modal discrepancies and indiscriminate channel interaction inevitably introduce redundant or conflicting features. Since different feature channels encode heterogeneous semantic information and contribute unequally to cross-modal fusion, selectively highlighting task-relevant channels while suppressing redundant ones is essential. To address this issue, we propose the Channel Selective Interaction Fusion Network (CSIF-Net), which performs selective channel-level cross-modal interaction. CSIF-Net first employs a frequency decomposition module to construct frequency-aware SAR inputs, facilitating the separation of structural information from noise-related responses. It then models cross-modal channel relationships through a cross-attention channel selection module and dynamically partitions the features into shared and modality-specific components. Finally, a dual-branch fusion module performs cross-modal interaction and channel realignment for shared features while independently enhancing SAR-specific features, thereby exploiting complementary information and suppressing modality interference. Extensive experiments on the OGSOD 1.0 and M4-SAR datasets demonstrate that CSIF-Net achieves state-of-the-art performance in both horizontal and oriented object detection, surpassing the existing methods by 4.01% and 3.18% gains, respectively.

---


### 161. [PixelSR: Pixel-Space Orthogonal Flow Decoupling for Real-World Image Super-Resolution](https://arxiv.org/abs/2610.27759)

**<font color=#1a73e8>作者：</font>** Xiang Lv, Kai Zhao, Qiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models have recently achieved remarkable progress in Real-world Image Super-Resolution (Real-SR). However, existing methods consistently exhibit a persistent seesaw effect: enhancing perceptual realism compromises structural fidelity. This effect, we argue, is not intrinsic to diffusion models, but largely stems from the architectural constraints of prevailing two-stage frameworks. To address this challenge, we propose PixelSR, a novel single-stage Pixel Diffusion Transformer for Real-SR that operates directly in pixel space. Specifically, PixelSR consists of two core designs: Pixel-space Conditional Diffusion and Orthogonal Flow Decoupling. The former establishes an effective pixel-space restoration framework by integrating spatially aligned LR conditioning, visual semantic guidance, and lightweight texture refinement, thereby bypassing VAE compression and enabling end-to-end optimization directly in RGB space. Complementarily, the latter decomposes the asymmetric flow target into a low-rank semantic component and a noise-free orthogonal texture component. By routing these components to specialized branches, it achieves decoupled optimization with reduced mutual interference. Benefiting from these designs, our PixelSR restores perceptually realistic details while faithfully preserving structural content. Extensive experiments across multiple benchmarks demonstrate that PixelSR not only achieves competitive performance, but also effectively mitigates the fidelity--realism seesaw effect.

---


### 162. [CrystalAR: Autoregressive Modeling for Symmetric Crystal Generation](https://arxiv.org/abs/2610.27762)

**<font color=#1a73e8>作者：</font>** Ziqiao Meng, Rongsheng Chen, Zhi Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep generative modeling has achieved remarkable progress in crystal generation. Given the rich symmetries inherent in crystalline structures, recent work has sought to explicitly incorporate space-group symmetry into generative models, enabling more effective exploration of novel symmetry templates. Yet introducing symmetry templates increases the combinatorial complexity of stoichiometric relationships between atomic species and crystallographic sites, while creating a fundamental tension between flexible exploration of discrete crystallographic templates and faithful realization of these templates as continuous three-dimensional structures. To address these challenges, we propose CrystalAR, a unified autoregressive framework that models Wyckoff symmetry templates and complete crystal structures within a single generative sequence. Specifically, CrystalAR reformulates continuous coordinate generation as a symmetry-conditioned hierarchy of discrete spatial localization decisions, autoregressively refining the positions of all symmetry-inequivalent sites across resolution levels while jointly modeling their spatial configuration within each level. This discrete hierarchical formulation further enables constraint-aware search over both crystallographic templates and geometric realizations. As a result, CrystalAR retains strong symmetry-template generation capability while achieving competitive de novo generation performance and template-free crystal structure prediction (CSP) accuracy. These results suggest that symmetry-template generation can be retained alongside broadly competitive de novo generation performance and competitive CSP without reliance on symmetry templates retrieved from prior data, providing a promising alternative paradigm for symmetry-preserving crystal generation.

---


### 163. [Foundation-Style Pretraining for Scalable and Transferable Distributed PV Forecasting](https://arxiv.org/abs/2610.27763)

**<font color=#1a73e8>作者：</font>** Dayin Chen, Xiaodan Shi, Xin Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth of distributed photovoltaic (PV) generation is increasing the demand for accurate forecasting across large numbers of geographically dispersed stations. Existing approaches are commonly developed for individual sites or specific forecasting horizons, requiring repeated training and maintenance as new stations are integrated and limiting direct reuse at previously unseen sites. To address this scalability gap, this paper presents a domain-specific foundation-style pretraining framework that learns a shared forecasting model from heterogeneous multi-site and multi-horizon PV data. NWP-assisted forecasting is formulated as a sequence-completion problem that unifies historical PV power, meteorological observations, future numerical weather prediction (NWP) forecasts, and time encodings. Three pretraining objectives are designed and systematically evaluated, including forecast-aligned reconstruction, generic reconstruction, and mixed reconstruction. The mixed objective combines the operational structure of PV forecasting with random sequence reconstruction and provides the most balanced performance across forecasting accuracy, degraded NWP conditions, and downstream adaptation. Experiments on 479 distributed PV stations use 340 stations for model development and 139 spatially held-out stations for zero-shot evaluation. Across horizons from 6 hours to 7 days, the multi-site pretrained MR model outperforms representative station-specific and shared baselines, as well as generalist time-series models, including a recent large-scale pretrained foundation model. The pretrained model can also be directly deployed at new PV stations and subsequently adapted to region-specific operational objectives when local data become available, providing a scalable forecasting paradigm for large distributed PV fleets.

---


### 164. [Testing TLS 1.3 PQC on constrained devices and microcontrollers](https://arxiv.org/abs/2610.27766)

**<font color=#1a73e8>作者：</font>** Olivier Gillot, William J. Buchanan, Callum Turino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The UK, EU and US governments have set timelines for post-quantum cryptography migration of critical systems, with deadlines ranging from 2028 to 2035. This paper focuses on IoT-class devices and microcontrollers and the viability of using PQC to connect these devices in secure TLS 1.3 connections. Using wolfSSL, we benchmark a 36-combination TLS 1.3 algorithm matrix, pairing ML-KEM-512/768/1024 and X25519/ECC P-256 key exchange with ML-DSA-44/65/87, Ed25519, ECDSA, and RSA-PSS authentication, across four devices (Raspberry Pi Pico W & Pico 2 W, ESP32, and a Raspberry Pi Zero), measuring both handshake latency and energy consumption. We found that in capable devices, all choices in the TLS matrix gave similar results, but that in IoT-class devices, PQC performance is highly implementation- and architecture-dependent: the common assumption that elliptic-curve key exchange must be cheaper than post-quantum lattice-based key exchange does not hold in this wolfSSL-based implementation, where the best full-PQC combination (ML-KEM-512 + ML-DSA-44) completes TLS handshakes 41% faster than the equivalent classical-modern pairing (X25519 + RSA-PSS) on the Pico W (up to 2.12x as energy-efficient, depending on the paired authentication algorithm), and 8.9x faster on the ESP32. Full-PQC, ML-KEM-512/ML-DSA-44, is not only possible but energy-competitive with or superior to Hybrid or Elliptic Curve alternatives on the most constrained devices, though ML-DSA's variable signing time means applications with strict latency-predictability budgets must accept this variance as the cost of full quantum-safe authentication. We further show that the IETF's draft-specified X25519+ML-KEM-768 hybrid incurs approximately the combined cost of its two components, rather than offering a performance compromise, making pure ML-KEM the more practical choice on hardware lacking Curve25519 assembly support.

---


### 165. [Engram Memory Network: Brain-Inspired Prototype Explanations](https://arxiv.org/abs/2610.27770)

**<font color=#1a73e8>作者：</font>** Hyunjun Kim, Myoung Hoon Ha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems are increasingly deployed in high-stakes decision-making. In response, prototype-based models in explainable AI have attracted growing attention for their ability to retrieve visually similar examples as faithful explanations. Although these models achieve competitive classification accuracy, they often exhibit degraded explanation quality across datasets with varying characteristics, limiting their practical applicability. We draw on insights from cognitive neuroscience, particularly the human memory system, which encodes input-relevant information into representations that support recognition. We propose an Engram Memory Network (EMN), a model that emulates the ventral visual stream and inferior temporal cortex in the human brain. Central to this model is a Hopfield-inspired memory module that iteratively retrieves representative prototypes. These memory-refined latents are used for both reconstruction and classification, encouraging the selected prototypes to capture input-relevant information across diverse datasets. To address the lack of standardized evaluation for prototype explanations, we assess three complementary aspects: perceptual similarity (LPIPS and DISTS) for perceived resemblance, subclass alignment, measuring whether prototypes match the input's fine-grained category beyond supervised labels, and information preservation (NMI), measuring how much input information is captured by selected prototypes. Experiments show that EMN improves visual similarity by 17.06%, subclass alignment by 104.57%, and NMI by 42.42% on average across CIFAR-10/100, MNIST, HAM10000, and CUB-200, while achieving the highest average classification accuracy (87.62%) among all methods. These findings underscore the effectiveness of neuroscience-inspired explanation mechanisms in advancing the interpretability and reliability of prototype-based models.

---


### 166. [How Much Do $\ell_1$ Attacks Need Concentrated Perturbations?](https://arxiv.org/abs/2610.27773)

**<font color=#1a73e8>作者：</font>** Melika Shirian, Kianoosh Vadaei, Arshia Hemmat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A global $\ell_1$ budget limits how much an adversary may change an image, not how that change is distributed. We ask how much of an $\ell_1$ attack's observed success remains when large coordinate changes are restricted. We add a per-coordinate cap to the budget, enforce the joint constraint by exact in-loop projection, and sweep the cap for APGD-$\ell_1$, SLIDE, and FMN-$\ell_1$ without altering their objectives. Across 18 standard-model settings, caps of at most $32/255$ retain a median $97\%$ of attack success relative to each method's native uncapped baseline, while median peak magnitude falls by $80\%$ and median effective support nearly triples. At matched realized $\ell_1$, capped perturbations remain structurally distinct; separate ImageNet comparisons also show lower LPIPS and DISTS at selected caps. Direct in-loop constrained optimization preserves up to $88$ percentage points more attack success than post-hoc clipping, highlighting the importance of constraint enforcement. Suitable caps nevertheless vary across attacks and models, and adversarially trained classifiers exhibit more heterogeneous concentration sensitivity. These results establish perturbation concentration as a complementary, model- and attack-dependent axis of $\ell_1$ attack evaluation.

---


### 167. [Radar-Based 3D Human Pose Estimation via Motion-Aware Pose Initialization and Observation-Guided Refinement](https://arxiv.org/abs/2610.27774)

**<font color=#1a73e8>作者：</font>** Woo-Jin Jung, Chan-Bin Lim, Seung-Hyun Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Human Pose Estimation (3D HPE) is used in indoor environments, such as smart homes, to analyze human movement and monitor human states. Millimeter-wave (mmWave) radar is suitable for this task because it is robust to lighting variations and does not capture images of human appearance. However, radar observations often provide insufficient information about certain body parts or contain overlapping reflections from multiple body parts, limiting accurate 3D joint localization. To address these limitations, we propose the Initialization-to-Refinement Pose Framework (I2R-Pose), comprising two stages: Motion-Aware Pose Initialization and Observation-Guided Refinement. In the first stage, joint-wise features are learned by incorporating temporal relationships across consecutive radar observations and human skeletal structure to compensate for insufficient joint information and estimate an initial 3D pose sequence. In the second stage, separately extracted radar observation features predict joint-wise positional corrections that refine the initial pose and generate the final pose sequence. The framework supports individual and fused inputs of time-Doppler/time-range (TD/TR) maps and radar point clouds (PCs). To evaluate performance across indoor activities, we construct the Radar Motion and Spatial Information for 3D Human Pose Estimation (RaMoS-Pose) dataset, providing synchronized TD/TR maps, radar PCs, and 3D joint ground truth (GT). Evaluations on RaMoS-Pose and the publicly available MVDoppler-Pose dataset show that I2R-Pose reduces mean per-joint position error (MPJPE) by 39.50% on MVDoppler-Pose and by 15.13% on RaMoS-Pose with fused inputs, compared with the best-performing existing methods evaluated on each dataset.

---


### 168. [Geometry Regularization for Vanilla NeRF via Self-Supervised Cross-Ray Consistency](https://arxiv.org/abs/2610.27776)

**<font color=#1a73e8>作者：</font>** Zongji Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural Radiance Fields (NeRF) achieve high-quality novel-view synthesis by representing a scene as a continuous volumetric radiance field. However, the geometry encoded by the density field of vanilla NeRF can be noisy and inaccurate, since different combinations of shape and radiance may explain the same input images. To reduce this ambiguity, we augment vanilla NeRF with a geometry-optimization branch based on self-supervised cross-ray consistency. Specifically, this branch samples candidate surface points from the density field, generates virtual rays that intersect at each point from different directions, and renders their appearance using the NeRF network. Based on the visibility-weighted color consistency across these rays, we constrain the implicit geometry. We further regularize the implicit geometry by penalizing opacity at candidates with inconsistent appearance predictions and encouraging local normal smoothness. These geometric constraints are derived from the NeRF predictions and require no ground-truth depth or surface-normal supervision. Experiments on eight Replica scenes show that the proposed method reduces the mean Chamfer distance by 30.8% compared with vanilla NeRF.

---


### 169. [Decoupled Representation Learning for Face Presentation Attack Detection under Smart Glass Capture](https://arxiv.org/abs/2610.27800)

**<font color=#1a73e8>作者：</font>** Raghavendra Ramachandra, Narayan Vetrekar, Neha Naik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face presentation attack detection is typically studied under fixed camera or handheld acquisition, whereas smart glass capture introduces a more challenging setting with ego motion, changing viewpoint, background clutter, distance variation, and less controlled illumination. To address this challenge, we present \emph{SmaGla-FPAD}, a smart glass based face presentation attack database acquired using Ray-Ban Meta Wayfarer Smart Glasses across indoor, outdoor, and in-car settings. The database contains 297,000 sample images with both bona fide and silicone mask based attacks. We further propose \emph{DeCoupPAD-FAS++}, a decoupled representation learning framework that separates spoof related evidence from nuisance sensitive capture variation through complementary attack and style branches, pseudo-domain supervision, adversarial suppression, and prompt guided semantic alignment. Experiments on SmaGla-FPAD show that the proposed method achieves the best balance between attack rejection and bona fide acceptance in both in domain and cross scenario evaluation. Ablation results further confirm the contribution of disentanglement, pseudo-domain supervision, and prompt based regularisation under smart glass capture.

---


### 170. [Looks Fine to Me: Understanding Oversight in Agentic Interactions](https://arxiv.org/abs/2610.27801)

**<font color=#1a73e8>作者：</font>** Dinithi Dissanayake, Yasith Samaradivakara, Hyung Woon Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are deployed to execute complex tasks across domains such as writing, coding, and data analysis. As execution is offloaded to AI agents, the human role shifts toward oversight. Effective oversight requires recognizing when closer scrutiny is needed, even though flawed outputs may appear convincing. Our formative study (N=12) revealed that users accepted plausible outputs without thorough evaluation, and only recognized these lapses in retrospect. To examine this systematically, we conducted a controlled within-subject study (N=36) in which participants completed programming tasks with an agent that produced correct outputs, silent defects, or visible failures. Combining task outcomes, interaction logs, gaze, physiological signals, and self-reports, we examined perceived, behavioral, and effective oversight. Participants were often highly confident while missing silent defects: they performed generic checks, failed to generate diagnostic evidence, or even misinterpreted defect evidence. We discuss how studying oversight across multiple dimensions can support future work on timely, task-calibrated re-engagement.

---


### 171. [LatBridge: Efficient and Stable Model Replacement in Latent-Communication Multi-Agent Systems](https://arxiv.org/abs/2610.27813)

**<font color=#1a73e8>作者：</font>** Jiajun Zhu, Haobo Li, Zixin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems rely on communication to complete tasks, and latent communication passes continuous representations to reduce text generation and re-encoding. However, multi-agent systems must reconfigure agent models, whereas existing latent-communication methods are built for fixed model combinations, so their interfaces may fail after replacement. Our pilot study confirms this interface failure and identifies the requirement for interface reuse after model replacement. We present LatBridge, which connects agent models through a shared Bridge and separate interfaces under a shared latent-communication protocol. After agent model replacement, LatBridge reuses unchanged interfaces, selects matching low-rank interfaces, and combines them through the Bridge, training only missing ones with all models frozen. The Bridge processes source representations in the basic mode and constructs target input without autoregressive generation in the accelerated mode. Experiments support effective communication after model replacement, with mean basic-mode accuracies of 14.8% on MATH and 27.3% on ALFWorld next-action prediction across eight small-model configurations. Analyses examine the factors supporting task accuracy and communication efficiency.

---


### 172. [From Generic to Dedicated: A Novel Optimizer for Online Continual Learning](https://arxiv.org/abs/2610.27835)

**<font color=#1a73e8>作者：</font>** Yongyi Wu, Zheng Wang, Sen Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online Continual Learning (OCL) requires models to learn from non-stationary data streams under a strict single-pass constraint, making them highly susceptible to catastrophic forgetting. While existing studies have explored various strategies from data, architecture, and optimization perspectives, the optimizer often directly uses generic approaches such as SGD and AdamW. In this work, we reveal a new link between optimization dynamics and OCL needs by recasting Polyak-Ruppert averaging as the engine of "plasticity" and Primal averaging as the anchor of "stability". This inspires our novel optimizer, SPIN (Stability-Plasticity INterpolation), which explicitly decouples plasticity and stability by interpolating between a fast-moving "plasticity" sequence and an adaptive "stability" sequence. We theoretically demonstrate that SPIN implicitly employs an inverse Hessian approximation, providing crucial Tikhonov regularization to damp noisy, single-sample Hessian estimates and mitigate forgetting. More importantly, SPIN can be seamlessly integrated into existing OCL methods by taking resulted gradients as input and replacing standard optimizers. Extensive experiments show that using SPIN instead of standard optimizers yields consistent and significant performance gains across multiple OCL approaches, including the challenging rehearsal-free setting and under strict memory constraints.

---


### 173. [Manifold Prior Guided Deep Unfolding for Hyperspectral Image Reconstruction](https://arxiv.org/abs/2610.27874)

**<font color=#1a73e8>作者：</font>** Shuqi Liu, Yingkai Zhang, Lin Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral Image (HSI) reconstruction has made substantial progress with the deep unfolding framework by decomposing the problem into a projection module and a denoiser module. Nevertheless, existing methods still exhibit limitations of insufficient matching with HSI data. The issues lie in two aspects: 1) the data-consistency projection module applies a fixed gradient descent step while ignoring the spectral content adaptivity of HSI; 2) the denoiser module either suffers from high computational complexity or is limited to the local receptive field, failing to efficiently capture the global spatial-spectral dependencies. In this paper, we propose a deep unfolding framework centered on a two-stage manifold learning strategy to obtain a degradation-free structural prior, which is then strategically injected into both the projection and denoiser modules. In the data-consistency projection, a prior-guided spectral weight mechanism is introduced to adaptively modulate the weight of spectral band. In the denoiser module, a manifold-guided Mamba is proposed to achieve the structure-aware extraction of spatial-spectral features through prior modulation. Quantitative and visual comparisons on synthetic and real-world datasets show that the proposed method significantly outperforms existing state-of-the-art approaches, while maintaining the structural interpretability of the unfolding framework. The code is available at this https URL.

---


### 174. [S$^3$E-Det: A Strict Spatial-Spectral Equivariant Detector for Multispectral Object Detection](https://arxiv.org/abs/2610.27882)

**<font color=#1a73e8>作者：</font>** Peng Zhang, Tingfa Xu, Jinrui Sui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral object detection requires detectors to exploit material-dependent spectral responses while maintaining consistent localization under geometric variations. Existing MOD detectors learn discriminative spectral representations, yet lack a unified mechanism that preserves spectral order, adapts spectral-context fusion across pyramid levels, and regulates geometric responses under rotation. To address these limitations, we propose S$^3$E-Det, a strict spatial-spectral equivariant detector that couples ordered spectral modeling with transformation-consistent prediction. Spectral Order-aware Sampling Calibration (SOSC) imposes local order constraints on input-derived spectral features through first-order variation, while Common-Differential Equivariant Fusion (CDEF) adapts spectral-context aggregation across pyramid levels. A compact Geometric Alignment Head (GAH) reconciles invariant and equivariant output properties within a unified prediction stage. Across MODA, HOD3K, and DroneVehicle, S$^3$E-Det combines high detection accuracy with a compact parameter footprint and reduced rotation-induced variation. Code is available at this https URL.

---


### 175. [SGLDet: Spectral-aware Global-Local Dynamic Modeling for Multispectral Aerial Object Detection](https://arxiv.org/abs/2610.27883)

**<font color=#1a73e8>作者：</font>** Peng Zhang, Shuaihao Han, Tingfa Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral aerial object detection aims to exploit spectral-spatial cues to address object detection challenges in complex aerial scenes. Existing methods mainly focus on spectral-spatial decoupling and object-aware spectral-spatial fusion to improve spectral utilization. However, two critical issues remain underexplored: 1) severe foreground-background imbalance caused by large scene coverage hinders reliable object recognition; 2) aerial objects exhibit substantial local variations in scale, orientation, and structure, which hinder accurate localization. To address these issues, we propose SGLDet, a spectral-aware global-local dynamic modeling framework for multispectral aerial object detection, which is motivated by the observation that object semantics are jointly determined by global spectral consistency and scene context, while precise localization requires dynamic feature modulation conditioned on the input spectral and spatial properties. To realize these properties, SGLDet consists of three coordinated components: a Spectral-driven Global Dynamic Modeling module that aggregates spectrally related features across the scene via similarity-guided sparse matching; a Multi-scale Global Context Integration module that constructs a compact scene memory for scene-guided contextual reasoning; and a Spectral-aware Input-dependent Calibration Aggregation module that performs expert-kernel aggregation with scene-guided spectral-spatial calibration to enable adaptive local feature modulation. Extensive experiments on MODA, HOD3K, and DroneVehicle demonstrate that SGLDet achieves superior performance with competitive computational cost. Code is available at this https URL.

---


### 176. [Automatic Differentiation with Constraints in Forward and Inverse Problems](https://arxiv.org/abs/2610.27888)

**<font color=#1a73e8>作者：</font>** Nikolay Yavich, Alexander Ryabov, Viacheslav Naumov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Approximate solutions of partial differential equations (PDEs) on unstructured grids can be represented on a graph. Numerical optimization involving stiff evolutionary and static PDEs often requires solving a large system of equations, which can be treated as a constraint. In this work, we present a fully differentiable graph-based implicit solver that incorporates this constraint. We evaluate its performance across four key tasks: a) linear and nonlinear forward modeling of evolutionary and static problems, b) solving inverse problems to estimate equation coefficients, c) solving inverse problems to estimate the right-hand side, and d) learnable graph coarsening to accelerate forward modeling. The stability and differentiability of our solver enable significant reductions in the complexity of forward modeling while efficiently addressing related inverse problems. These capabilities make it a powerful tool for different physics and engineering applications, in particular for geophysics, where inverse problems are commonly solved in order to reduce the model uncertainty.

---


### 177. [EndoWorld-JEPA: Motion-Guided Global-Local Latent World Modeling for Endoscopic Video Representation Learning](https://arxiv.org/abs/2610.27890)

**<font color=#1a73e8>作者：</font>** Jie Wang, Shilong Yang, Tao Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Endoscopic video contains state transitions induced by camera displacement, deformable tissue, and instrument interaction, yet existing pre-training methods treat dynamics implicitly. Inspired by action-conditioned joint-embedding predictive world models and by the observation that endoscopic optical flow contains both shared image-plane displacement and localized residual motion, we reformulate passive endoscopic video pre-training as causal motion-guided latent-state prediction. We present EndoWorld-JEPA, to our knowledge the first latent world-model pre-training framework designed for general-purpose endoscopic video representation learning. In place of recorded actions, calibrated poses, or robot kinematics, the model conditions prediction of the next latent state on motion observed up to the current state. Its Optical Motion-guided module separates dominant displacement from residual motion and converts the resulting evidence into an ordered temporal motion condition and spatial local-motion weights. Complementary global and motion-local predictors use these outputs: the temporal condition modulates both latent transitions, whereas the local weights define an auxiliary motion-local state that extends prediction from scene-level evolution to spatially selective dynamics. Patch-wise motion weighting emphasizes localized change while retaining anatomical context, and past-motion-window dropout randomly withholds the complete motion condition to reduce dependence on unreliable motion. This global--local formulation learns predictable visual--motion dynamics in representation space without reconstructing stochastic appearance artifacts. Evaluation shows that a common pre-trained checkpoint achieves strong transfer across four downstream benchmarks, supporting motion-guided global--local latent prediction as an effective pre-training paradigm for endoscopic video.

---


### 178. [Physical-Variable-Informed Deep Learning for Robust Diagnosis in Industrial Fluid Transport Systems](https://arxiv.org/abs/2610.27891)

**<font color=#1a73e8>作者：</font>** Yu Sha, Junqi Tao, Dixin Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial fluid transport systems are monitored through heterogeneous sensing streams, but robust fault diagnosis remains difficult because response signals vary with operating conditions and differ from physical variables in sampling rate, observation duration and data granularity. To address these challenges, we propose a physical-variable-informed deep learning framework (PhyNet) for robust fault diagnosis under real-world sampling heterogeneity. PhyNet treats physical variables as global operating constraints and response signals as local diagnostic evidence. Its physical-to-response cross-attention mechanism connects sequence-level physical-variable tokens with a learnable global response token, enabling interaction without strict temporal alignment. Across four benchmarks, including three real-world cavitation datasets and one public two-phase-flow dataset, PhyNet achieves the best performance across all evaluated metrics. Class-wise analyses, together with attention and masking analyses, show improved discrimination of ambiguous states and indicate that physical variables meaningfully constrain local response interpretation. These findings demonstrate a deployment-oriented approach to robust diagnosis in heterogeneous industrial environments.

---


### 179. [ICIBS: Increasing the Context for Ice Boundary Segmentation](https://arxiv.org/abs/2610.27912)

**<font color=#1a73e8>作者：</font>** Marcel Dreier, Dakota Pyles, Nora Gourmelon 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mountain glaciers and ice sheets are undergoing rapid loss of ice mass. To assess their current volume and ice-thickness distribution, and to accurately forecast their future, ground-penetrating radar systems are employed to measure ice thickness. These instruments produce radio-echo sounding data that reveal the internal structure of the ice and its boundaries at the surface and beneath the ice body. However, delineating these interfaces is time-consuming as the surveyed area can span several hundred kilometers. To accelerate the labelling process, automated methods have emerged, but they often struggle to delineate the ice bottom, particularly in temperate glaciers. The high water content inherent in temperate ice increases both scattering and attenuation of the radar signal, resulting in weak and ambiguous reflections at the ice bottom and generally noisier data. As a result, the visual features corresponding to the ice bottom become ambiguous. To address this issue, we propose several extensions to deep learning models that incorporate additional contextual information into the prediction. Specifically, we integrate modifications that incorporate additional spatial and geo-spatial contextual information into the network. With these enhancements, we achieve a new state-of-the-art performance on the IceAnatomy benchmark dataset, with mean errors of 10.9 m for the FAU subset and 43.4 m for the CReSIS subset in a single combined system. We also demonstrate that our method generalises well to previously unseen data, outperforming the baseline by 49.6 % on new campaign data from Patagonia. The model code and the new dataset are available at this https URL and this https URL.

---


### 180. [World Models with Configurable Perception](https://arxiv.org/abs/2610.27914)

**<font color=#1a73e8>作者：</font>** Yijun Shen, Delong Chen, Xianming Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world observations are noisy and often contain excessive task-irrelevant information. Effective world modeling and planning need to abstract observations into world state representations while filtering out irrelevant information. However, encoders in existing world models are typically non-adaptive, leading to state representations that are easily distracted by task-irrelevant information. As a result, the model may not selectively filter observations to cater to different task demands. To address this problem, we introduce ConfigWM, which realizes configurable perception through task-conditioned state extraction. Given a language description of the task at hand, ConfigWM uses it as a configuration signal to steer how visual embeddings are mapped into a task-specific state space, selectively preserving information relevant to the current task while suppressing task-irrelevant variations. Action-conditioned dynamics are then learned in this task-specific state space for planning. We evaluate ConfigWM in environments with increasing levels of distraction. While existing methods exhibit substantial declines in planning success rate as the environments become increasingly noisy, ConfigWM remains comparatively stable and outperforms the strongest competing method by 22.3% on average across diverse environments. Consistent gains in physical-quantity probing (+0.365 Pearson r) and distracted-to-clean retrieval (+75.5%) further indicate that ConfigWM learns states that preserve task-relevant information while remaining robust to distractors, supporting reliable world modeling and planning in noisy worlds. Project Page: this https URL

---


### 181. [Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models](https://arxiv.org/abs/2610.27921)

**<font color=#1a73e8>作者：</font>** Zhiyuan Liu, Sicheng Liu, Haiyu Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A single observation can admit several plausible futures, making uncertainty an essential part of world modelling. However, quantum generative models remain underexplored for this task. We introduce Quantum-JEPA, a latent-action JEPA framework that learns distributions of future representations using a conditional quantum Born prior. Circuit measurements generate binary latent actions, which a shared predictor maps to alternative future representations. We train the quantum prior through the quality and diversity of these predictions using a sampled energy objective. Our model learns distinct continuations on constructed multimodal tasks and captures latent-action correlations that support coordinated multi-agent futures. On D3IL, a benchmark of diverse human demonstrations, our trained models generate multiple obstacle-crossing routes from a common starting point without observed motion. On the controlled tasks, our classical and quantum prior implementations improve prediction validity and distributional fidelity over the evaluated variational baselines. Our quantum priors combine competitive predictive quality with a parameter-efficient sampling structure: they avoid an exponentially sized categorical output layer while supporting correlated latent actions. We further validate finite-shot parameter-shift training, including training with readout noise. Unlike most prior work, which focuses on simulation, we also verify the feasibility of inference with trained priors on a real QPU. These results establish a trainable quantum component for JEPA future prediction and a basis for exploring quantum-enhanced world models at larger scales.

---


### 182. [From Comparison to Selection: Enhancing Cross-Scale Generalization of Pointer Networks Trained with Reinforcement Learning for Capacitated Drone Delivery Routing](https://arxiv.org/abs/2610.27936)

**<font color=#1a73e8>作者：</font>** Sofiene Lassoued, Devara Tertia, Stefan Lier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) enable fast, flexible last-mile and emergency delivery, but their routing remains challenging as the number of clients varies. Classical approaches based on mixed-integer programming and heuristics can scale poorly or require problem-specific design, motivating learning-based alternatives. Reinforcement learning is particularly promising, provided a single policy can generalize across problem sizes without retraining. Although attention-based Pointer Networks are inherently size-agnostic, their solution quality degrades under both upscaling and downscaling. Using the Capacitated Vehicle Routing Problem (CVRP) as a controlled proxy, with fixed capacity reflecting drone payload constraints, we investigate this degradation and identify three contributing factors: shifts in node density, attention dispersion, and dilution of the mean-pooled graph context. We systematically compare architecture-wide, encoder-side, and decoder-side modifications to address these limitations and propose a learned, permutation-invariant graph-context aggregation mechanism, implemented as a weighted average and as Set2Set. Results reveal distinct requirements for transfer in each direction: entropy-based attention scaling reduces the CVRP20-to-CVRP100 performance gap by 1.41 percentage points, while the proposed aggregation methods achieve the largest improvement on the more challenging CVRP100-to-CVRP20 transfer, approximately 0.9 percentage points. Exploiting this complementarity, we introduce an approach selector that chooses the best model for each training-target size pair. The selector reduces cost relative to the reference model across all nine seen train-test pairs and eight of nine pairs involving unseen sizes (CVRP35, CVRP75, and CVRP200), achieving improvements of up to 3.2 percent.

---


### 183. [HypTI: Hyperbolic Geometry-Aware Multimodal Feature Fusion Framework for Dementia Detection Based on Tabular-Image Data](https://arxiv.org/abs/2610.27941)

**<font color=#1a73e8>作者：</font>** Jianfei Xu, Huizhi Liang, Judith Harrison 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted dementia detection usually requires multimodal fusion of diverse data, such as clinical tabular assessments and neuroimaging data. However, most existing approaches perform feature fusion in Euclidean space. This overlooks the geometric structure of representation, including hierarchical organization in clinical assessments and multi-scale anatomical patterns in neuroimaging data. Recent studies have proved hyperbolic space provides a natural geometry for modelling hierarchical and multi-scale structures due to its exponentially expanding space. Motivated by these, we propose HypTI, a hyperbolic geometry-aware multimodal fusion framework for dementia detection based on clinical tabular assessments and MRI scans. HypTI extends hyperbolic representation learning to an underexplored tabular-MRI setting, jointly modelling clinical tabular, MRI scans, and cross-modal interactions in hyperbolic space. Specifically, clinical tabular variables are represented through learnable Lorentz prototypes to capture hierarchical relationships among assessments, while MRI scans are encoded using ROI-guided multi-scale representation learning to capture anatomical patterns across brain regions and spatial scales in Lorentz space. The multimodal representations are integrated through an adaptive fusion module generates subject-specific scale and shift coefficients to dynamically modulate and integrate the multimodal embeddings, enabling effective patient-level tabular-image representation learning for dementia detection. Experiments on OASIS-3 dataset show that the proposed framework achieves strong performance compared with representative approaches.

---


### 184. [Decoupling Action from Egocentric Observation for World Simulation](https://arxiv.org/abs/2610.27946)

**<font color=#1a73e8>作者：</font>** Yue Ma, Pengjie Song, Xinyu Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric action transfer aims to decouple the semantic action from egocentric observations and reproduce them in new visual contexts, enabling scalable world simulation, embodied policy learning, and robotic data generation. Existing approaches to transferring actions rely on condition-guided video generation, which converts the observation video into explicit geometric controls (e.g., hand poses or meshes) to drive synthesis. However, these methods introduce geometric estimation errors, making it difficult to preserve physically plausible interactions when transferred to new scenes. Alternatively, motion transfer methods directly extract motion patterns from the observation video, yet motion-level features alone cannot encode rich contact dynamics, frequently leading to severe hand structural collapse and implausible contact layout. To address both limitations, we present EgoACT, a test-time framework for egocentric action transfer that operates directly on the denoising process of video diffusion models without requiring additional geometric estimators. EgoACT uses Velocity-guided Structure Anchoring to stabilize reference-consistent hand-object structure in the early denoising stage, and Sparse Correspondence Calibration to refine reliable local correspondences in the mid-to-late denoising stages. Together, these two components preserve transferable action semantics while improving temporal coherence and interaction realism. We further establish EgoActionBench, a benchmark for evaluating action preservation, visual quality, and hand-object plausibility across diverse egocentric manipulation scenarios. Experiments show that EgoACT generates more coherent and physically plausible interaction videos than strong baselines.

---


### 185. [Edit in Sync: Unified End-to-End Audio-Visual Editing for Human-Centric Videos](https://arxiv.org/abs/2610.27947)

**<font color=#1a73e8>作者：</font>** Ziye Yuan, Minghong Cai, Xu He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-centric audio-visual editing requires precise alignment of lip movements, gestures, and expressions with speech. Existing methods process inputs through independent video and audio pipelines, preventing cross-modal interaction between visual editing and audio dubbing. Many of these pipelines further rely on mask-based inpainting. As a result, they suffer from poor lip-audio synchronization, cumulative pipeline errors, and an inherent mask-size dilemma. We present AVE, the first unified end-to-end framework that jointly performs reference-guided person swapping, insertion, and deletion across both audio and video modalities without requiring spatial masks. To overcome data scarcity, we design a synthesis pipeline and introduce AVE-Dataset, the first audio-visual editing dataset to provide 100K pairs with appearance and voice references. By combining Synthetic-to-Real reconstruction with preliminary audio warm-up, our framework transcends synthetic pipeline limits and mitigates audio-video token imbalance. AVE outperforms modality-separate audio-visual editing pipelines in editing realism, temporal consistency, and audio-visual alignment.

---


### 186. [Unsupervised Head Network Personalization for Split Computing via Federated Learning](https://arxiv.org/abs/2610.27952)

**<font color=#1a73e8>作者：</font>** Yutaro Horikawa, Takayuki Nishio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Computing (SC) is a distributed inference method designed for balancing computational load and reducing latency by partitioning a neural network into head and tail networks and deploying them across both a mobile device and a server, respectively. Due to the limited bandwidth and computational power of mobile devices, the head network is often replaced with a neural network that requires lower computational and communication resources. However, it is challenging to prepare a sufficient quantity and quality of labeled data on the mobile device side for training the replacement head network. Furthermore, the data prepared by mobile users often contains sensitive privacy information, making data aggregation difficult. In this paper, we propose a data-efficient head network training method for SC. This method utilizes federated learning and knowledge distillation to train the head network using a small amount of non-IID and unlabeled data from mobile devices, ensuring that the training datasets are not exposed. Moreover, by introducing personalization, we enhance the accuracy to levels comparable to or exceeding those of existing methods. The experimental evaluations demonstrate that, despite data constraints imposed only on our method, it achieves accuracy comparable to the baselines. Furthermore, it significantly reduces the communication requirements by 95% on mobile devices, with only a 3-5 percentage point drop in accuracy from the original model.

---


### 187. [From Proper Scoring Rules and Edge Biases to Mumford-Shah Models: Robust Unsupervised Hyperspectral Image Segmentation](https://arxiv.org/abs/2610.27958)

**<font color=#1a73e8>作者：</font>** Fabian Conrad, Benjamin Berkels  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral images provide a rich representation of the underlying spectrum for each pixel, allowing for a pixel-wise classification/segmentation into different classes. As the availability of labeled hyperspectral images is limited and the acquisition of labeled training data is time-consuming, unsupervised segmentation methods are important in hyperspectral image segmentation. Spectral variability, mixed pixels, noise as well as high correlation between neighboring spectral bands make this task challenging. We present a feature-agnostic, unsupervised hyperspectral segmentation framework based on the piecewise-constant Mumford-Shah functional. Our framework turns a strictly proper scoring rule and a family of parametric probability distributions into an indicator function for the Mumford-Shah functional, and we naturally generalize some previous Mumford-Shah based models for image segmentation this way. Our focus will be on heavy-tailed elliptical distributions, the negative log-likelihood score and the score based on the beta-divergence to deal with the heavy outliers in hyperspectral imaging. Using the interplay between the calculus of variations and statistics, we also propose a robustness step to estimate the statistical parameters of these heavy-tailed elliptical distributions. In addition, an edge bias, which contains prior boundary information, is incorporated into both the data fidelity term and the perimeter term of the Mumford-Shah functional. Numerical experiments show that, to the best of our knowledge, our method achieves the highest overall accuracy among fully unsupervised methods on three of the four standard benchmarks (Indian Pines, Kennedy Space Center, Pavia University and Salinas) evaluated on the full scenes. It also improves upon our previous Mumford-Shah based model.

---


### 188. [Efficient SAM3 Adaptation for Multi-Class Semantic Segmentation via Dense Competitive Representations](https://arxiv.org/abs/2610.27960)

**<font color=#1a73e8>作者：</font>** Wenbin Liao, Hao Zhu, Yike Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model 3 (SAM3) has achieved significant progress in Promptable Concept Segmentation (PCS) by processing short noun phrases to generate segmentation masks with unique instance identifiers. While SAM3 excels at single-concept segmentation, it falls short in complex, real-world environments where multiple concepts must be segmented simultaneously. In particular, SAM3 typically fails to simultaneously process concepts with semantic overlap, leading to semantic misclassifications and redundant mask predictions. Moreover, as the number of concepts increases, the independent inference paradigm introduces prohibitive inference latency. To address these limitations, we propose the Dense Competitive Representations SAM (DCR-SAM) framework. By decoupling cross-modal interactions, the proposed method alleviates the inference latency. To resolve semantic misclassifications, DCR-SAM dynamically aligns textual concepts with visual representations and incorporates a dense competition head to enforce explicit inter-class competition. Furthermore, a learnable background token is applied to absorb non-target objects dynamically. These mechanisms effectively suppress overlapping predictions and generate high-fidelity masks. Extensive experimental evaluations across multiple benchmarks demonstrate that the proposed framework: (1) achieves a 2.3% $\sim$ 10.7% performance improvement over state-of-the-art methods, (2) delivers a 33$\times$ inference speedup compared to the native SAM3, and (3) exhibits strong robustness across diverse scenarios.

---


### 189. [When Do Humans and Machines Truly Complement Each Other? Formal Conditions and Empirical Evidence for Human-AI Synergy](https://arxiv.org/abs/2610.27965)

**<font color=#1a73e8>作者：</font>** Andrea Campagner, Federico Cabitza, Vincenzo Crupi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can humans and artificial intelligence cooperate such that their combination yields greater accuracy than either agent alone? This result, termed \emph{synergy} or \emph{complementarity}, is notoriously difficult to achieve, even when both agents possess significant independent accuracy. In this paper, we present a formal framework to model human-AI interaction through the lens of reliance patterns, which characterize the joint correctness structure of human and algorithmic decisions. We derive mathematically necessary and sufficient conditions for synergy, demonstrating that its emergence depends on the ability of either agent to identify and correct the errors of the other, what we call Human and Algorithmic Correction. Beyond its theoretical contribution, the proposed framework provides a foundation for the design and evaluation of knowledge-based decision support systems, where interaction policies must dynamically integrate heterogeneous sources of expertise. We demonstrate this through the analysis of seven clinical case studies. Our empirical results reveal a ``dominance trap,'' where a strong algorithmic advantage can paradoxically inhibit synergy by eroding human corrective intervention. We also show that synergy can persist even in the presence of cognitive biases, such as automation bias, provided there is functional de-correlation between human and AI errors. These results provide a formal foundation for key concepts in the human-AI systems literature and offer actionable insights for designing interaction-centric AI systems that foster complementarity.

---


### 190. [Media Intelligence Platform: Multimodal Detection of Synthetic and Manipulated Content](https://arxiv.org/abs/2610.27974)

**<font color=#1a73e8>作者：</font>** David Fischinger, Marcel Hasenbalg, Silvia Poletti 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of generative artificial intelligence has led to a significant increase in manipulated multimedia content, including synthetic faces, forged videos, AI-generated images, fake audio, and locally edited images. Existing detection approaches are typically designed for a single manipulation type, limiting their applicability in real-world scenarios involving heterogeneous media sources. In this work, we present the Media Intelligence Platform (MIP), a unified web-based framework for multimodal media forensics integrating specialized modules for fake video detection, face morphing detection, AI-generated image detection, audio deepfake detection, localized image manipulation detection, and text analysis. Its modular architecture enables flexible integration of heterogeneous models and supports future extensions for emerging manipulation techniques. Experimental results on representative benchmark datasets demonstrate reliable detection performance across multiple media modalities while providing a practical and user-friendly interface for forensic investigations. The platform highlights the potential of unified multimodal systems for comprehensive deepfake detection in real-world environments, and is accompanied by a public demonstrator released with this workshop submission to support reproducibility and community evaluation.

---


### 191. [Beyond the Frame: Redundancy, Not Trajectory, Carries the Privacy Leak in Video Unlearning](https://arxiv.org/abs/2610.27982)

**<font color=#1a73e8>作者：</font>** Kavyansh Tyagi, Paolo Russo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class unlearning for video segmentation aims to ensure that a removed category cannot be reconstructed from a deployed model's outputs. Current leakage evaluation algorithms inspect one frame at a time, and we show that this understates leakage by a wide margin: an attacker that averages a model's output field over a two-second clip recovers the forgotten class from every method we evaluate on VSPW and most on Virtual KITTI~2, including models whose per-frame predictions are visually indistinguishable from a retrain oracle (a model trained from scratch without the forgotten class). We attribute the recoverable signal to cross-frame redundancy rather than object trajectory, establish this with a time-shuffled control that leaves leakage intact, and introduce PACE, an unlearning method that suppresses redundancy directly using an exactly permutation-invariant pooled adversarial discriminator and a two-sided temporal consistency objective. Across VSPW and Virtual KITTI~2, PACE lowers pooled attacker AP to $18.79$ (\texttt{person}) and $12.10$ (\texttt{car}) on VSPW and $9.11$ (\texttt{car}) on Virtual KITTI~2, achieving on the latter the strongest suppression among verdict-safe methods retaining usable utility, while retaining $19.8$ mIoU on VSPW \texttt{car} against at most $8.3$ for any baseline achieving comparable erasure.

---


### 192. [Recast the Past: Stable Long Video Generation with Full Context Memory](https://arxiv.org/abs/2610.27986)

**<font color=#1a73e8>作者：</font>** Yukuo Ma, Cong Liu, Junke Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon video generation requires retaining an ever-expanding history, but conditioning on its growing token sequence is costly. Existing methods restrict or compress historical context, potentially losing information needed for future generation. This work proposes ReCam, which groups local spatiotemporal blocks of historical latents into vectors and projects them directly into the high-dimensional hidden space of a Diffusion Transformer. The model learns to use the resulting memory tokens through native self-attention, reducing token count while retaining block-level access to the full history. To mitigate temporal drift during autoregressive rollout, we further introduce dual-pointer denoising with separate noise schedules for recent context and target frames. Among the evaluated methods, ReCam achieves the highest VBench-Long overall score of 80.1 and competitive static-scene revisitation performance on R2M-Bench. It also leads on all four consistency metrics for off-screen subject reappearance, including clothing consistency of 4.09 versus 3.03 for the best baseline.

---


### 193. [On Johnson-Lindenstrauss Transforms for Byzantine-Robust Optimization](https://arxiv.org/abs/2610.27989)

**<font color=#1a73e8>作者：</font>** Aleksandr Shestakov, Vladimir Aletov, Aleksandr Beznosikov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing scale of data and models in machine learning calls for efficient optimization methods. Distributed optimization addresses this challenge, with compression mechanisms helping to reduce communication costs. A classical tool for dimensionality reduction is the Johnson-Lindenstrauss (JL) transform, which is simple to implement and offers strong geometric guarantees. In particular, JL transforms approximately preserve inner products and pairwise distances between vectors with high probability. In this paper, we exploit this property in Byzantine-robust optimization, where worker messages are weighted according to their alignment with a trusted reference gradient. We further support our theoretical findings with experimental results.

---


### 194. [When Momentum Helps Polyak--Ruppert Averaging](https://arxiv.org/abs/2610.27990)

**<font color=#1a73e8>作者：</font>** Alexandra Suvroikova, Darina Dvinskikh, Yuriy Dorn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Polyak--Ruppert averaging gives SGD and momentum methods the same asymptotic covariance. We characterize how fast finite runs reach it and how far they can be parallelized. For strongly convex quadratics with additive noise, we prove an online--offline bridge: the empirical risk minimizer on the samples of a tail average is one Newton step from the tail-averaged query point of any online procedure. For SGD, heavy ball, and Nesterov's method with constant momentum, this step is a boundary term at the two ends of the tail and splits the gap to the offline estimator into center, covariance, and shape errors. Necessary and sufficient conditions show that, on the least curved direction, the center error sets the pace: SGD needs $m\gg\kappa^2$ rounds but momentum only $m\gg\kappa$, where $\kappa$ is the condition number, so at sample size $N$ the critical batch size grows from $\Theta(\sqrt{N}/\kappa)$ to $\Theta(\sqrt{N/\kappa})$. The covariance error separates the momentum methods: heavy ball has relative variance excess $\Theta(\kappa^{3/2}/m)$ along the stiffest direction, whereas Nesterov has relative error $O(\sqrt{\kappa}/m)$ in every direction. The shape error is method-independent by a Berry--Esseen bound uniform in $\kappa$ and batch size, so confidence intervals are valid when the other two errors vanish. We further examine how the conclusions change under heavy-tailed or state-dependent noise and clipping, and establish a first-order comparison with ERM for nonlinear Nesterov averaging under explicit conditions.

---


### 195. [Dancing Diffusion: Learning Continuous Programs for Image Generation and Editing](https://arxiv.org/abs/2610.28003)

**<font color=#1a73e8>作者：</font>** Cui Enhe, Jinyue Yang, Bojian Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate samples through a multi-step denoising trajectory, yet condition every step on the same instruction, so the trajectory cannot be addressed at the level of individual operations. We introduce Dancing Diffusion, which assigns each span of timesteps a dedicated continuous condition block and thereby turns conditioning into a latent program. A compiler maps text features into this program, and a fixed pretrained generator executes its blocks over successive sampling intervals. The trajectory can then dance, keeping its executed history while its continuation is redirected. A shared prefix is executed once and reused, and a later operation is rewritten while content fixed by earlier operations is preserved. The compiler is trained through the images it produces, with visual feedback on both the requested change and the retained content. On SANA, reusing an executed prefix preserves markedly more of the scene than regenerating from noise at a similar strength of edit, learned conditions preserve more background than native prompt switching from the same saved state, and the learned program improves generation quality over native SANA. Later branches weaken the edit, which leaves semantic control over individual operations limited. By converting a single-instruction trajectory into a program of addressable operations, Dancing Diffusion lays a foundation for structured intermediate computation in diffusion models.

---


### 196. [Differentiable Task-Driven Coded Aperture Camera Design with 3D Gaussian Scene Representations](https://arxiv.org/abs/2610.28004)

**<font color=#1a73e8>作者：</font>** Chengyang Yan, Donald G. Dansereau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera design heavily influences perception task performance, yet cameras are typically designed by domain experts through costly experimentation, in isolation from the tasks they serve. Existing joint-design methods either rely on differentiable simulation limited to pre-captured 2D images, restricting them to optics or image-processing pipeline design, or use non-differentiable camera simulators optimised with derivative-free or reinforcement-learning methods that scale poorly with the number of design parameters. We present a differentiable framework for jointly designing complex camera systems and downstream perception tasks. We use it to design two coded-aperture depth-from-defocus cameras, a monocular and a stereo configuration, by jointly optimising the coded aperture mask, camera parameters, and a depth estimation network end-to-end. Our framework represents scenes with 3D Gaussian Splatting reconstructed from real-world captures, providing a differentiable image formation process for gradient-based optimisation over design spaces intractable for prior differentiable approaches. Results demonstrate that our differentiable method improves over existing coded aperture design and non-differentiable camera design baselines, offering a step forward in automated and principled camera design for autonomous systems.

---


### 197. [AdaptMIL: Domain Adaptation for Multiple Instance Learning in Digital Pathology](https://arxiv.org/abs/2610.28007)

**<font color=#1a73e8>作者：</font>** Ben Vardi, Dana Schonberger, Yuval Friedmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) support a wide range of histopathology tasks on whole-slide images through multiple instance learning (MIL). Despite recent progress, these models remain sensitive to cross-hospital distribution shifts: performance often degrades when a task head (e.g., classification) is trained on data from one hospital and then used on data from another hospital. To address this challenge, we propose AdaptMIL, a training strategy for integrating domain adaptation into MIL training. AdaptMIL is motivated by our finding that directly applying domain adaptation objectives during MIL training can interfere with MIL aggregation learning, often resulting in performance degradation over standard training. AdaptMIL resolves this by decoupling representation-level domain alignment learning from MIL aggregation learning through a two-stage training procedure. We show that AdaptMIL improves cross-hospital performance and outperforms alternative adaptation methods across experiments spanning multiple WSI datasets, tasks, PFMs, MIL architectures, and domain adaptation objectives. AdaptMIL's code will be released upon publication.

---


### 198. [Spherical Geometry-Aware Panoptic Scene Graph Generation for Equirectangular Panoramas](https://arxiv.org/abs/2610.28033)

**<font color=#1a73e8>作者：</font>** Zhe Wu, Xiaoyan Fei, Xinyi Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoptic scene graph generation (PSGG) represents scene entities with segmentation masks and directed relations. Equirectangular projection (ERP) panoramas challenge PSGG through distortion, latitude-dependent pixel areas, and an artificial seam. We propose a two-stage spherical geometry-aware framework that fuses overlapping perspective-view predictions using observation reliability, spherical overlap, and angular proximity. Relation reasoning combines spherical-area-aware aggregation, weighted no-relation supervision, and dual-longitude score fusion. We also construct a dataset of 340 high-resolution panoramas with 10,571 nodes and 6,632 directed relations. Against corresponding baselines, spherical fusion improves PQ by 36.03% under matched views, while relation reasoning improves mR@50 by 11.20% under PredCls with ground-truth masks and object labels. The full framework improves mR@50 by 52.99% under SGDet with predicted panoptic segments. These results demonstrate the value of spherical geometry for panoramic PSGG.

---


### 199. [When Does Training on Synthetic Data Provably Work?](https://arxiv.org/abs/2610.28036)

**<font color=#1a73e8>作者：</font>** Leroy Odunlami, Tobias Riedlinger, Hanno Gottschalk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-quality training data are a major bottleneck in machine learning, motivating increasing use of artificially generated data. We study when a binary classifier trained on synthetic data transfers successfully to a real distribution, under a shared conditional label distribution. First, we derive finite-sample excess-error bounds when the real covariate distribution is absolutely continuous with respect to the synthetic distribution under a controlled density ratio. Second, we study the partially and fully singular case, where the real distribution has mass outside the synthetic one. If the hypothesis class is sufficiently expressive, synthetic risk alone cannot uniformly control real-world error: a classifier can be nearly optimal on synthetic data while approaching worst-case error on the uncovered real region, even when the distributions are arbitrarily close in Wasserstein distance. For function classes where hypotheses and the log-odds of the conditional label probability are Lipschitz, we recover a bound in terms of the probability that a real sample lies outside the reach of the synthetic data, restoring a transfer guarantee even in the fully singular case. Experiments confirm this in controlled low-dimensional settings and on 32,200 images generated as counterparts to real ImageNet images by four state-of-the-art generators: an adversarial classifier reaches 0.5% error on the synthetic domain but 99.25% error on the real domain, while ordinarily trained architectures show positively correlated synthetic and real test errors. Synthetic data should be budgeted at high sample counts and models validated on real data.

---


### 200. [Using Letter Positional Probabilities to Assess French Word Complexity](https://arxiv.org/abs/2610.28040)

**<font color=#1a73e8>作者：</font>** Michael Dalvean  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We use Letter Positional Probabilities (LPPs) to examine the orthographic differences between simple and complex French words. We draw from a sample of 38,000 French words scored by reaction time on a lexical decision task. We take the 5000 highest reaction time words and the 5000 lowest as a proxy for high and low word complexity groups respectively. We create 18 variables based on the structure of the words, such as length and number of syllables. We also reduce each word to a string of binary values by one-hot encoding each letter according to the 42 characters of the standard French alphabet up to a length of 25 letters. Thus, each word is represented by 42 x 25 binary characters. We then create LPPs by looking at the average binary scores for simple as opposed to complex words for all letter/positions. We find that there is a high number of LPPs that are associated with word complexity. For example, we find that most accented letters are associated with simpler words. We examine the effects of structural and LPP variables in classifiers and find that word length alone enables a classification accuracy of 77.27%, while adding the binary variables from the first 6 letter positions provided an accuracy of 83.95%. We discuss possible explanations as to how complexity could be encoded in orthography.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
