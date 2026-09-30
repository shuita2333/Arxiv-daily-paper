# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 101. [Reducing the Adaptation Gap Through Reachable Fisher Geometry](https://arxiv.org/abs/2609.36329)

**<font color=#1a73e8>作者：</font>** Wasif Jalal, Sachin Deb, Asif Salekin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) determines not only how many parameters are trained, but also which local directions a model can move in, so similar adapters can affect subgroup losses differently. Since curvature matrices are infeasible to form at adapter scale, scalar summaries such as the Fisher trace are often used instead. We study what the trace reveals and what it loses through the reachable Fisher: each subgroup's full-model Fisher pulled back through the adapter Jacobian. Under likelihood losses, it represents the Gauss-Newton curvature accessible to the adapter, and its trace can be computed from score-gradient norms without forming the full matrix. Under matched subgroup gradients, a positive-definite reachable-Fisher difference, with a margin exceeding the Hessian-Fisher defect, implies that every sufficiently small nonzero model-changing update increases the signed gap. In contrast, the restricted operator norm determines worst-case quadratic change, while a matrix-free Frobenius discrepancy bounds its reachable-Fisher component. Trace alone cannot certify definiteness or control matrix mismatch. Equal traces rule out a positive-definite difference but can still hide large operator discrepancies. Across 306 single-seed models, higher trace accompanies greater subgroup difficulty in 75.7 percent of 1,218 eligible evaluations, while trace matching reduces the best-worst subgroup gap in all 30 dataset-encoder-adapter combinations. However, held-out audits show that operator discrepancy decreases in 23 of 30 combinations, while the unbiased squared-Frobenius statistic decreases in only 16 of 30. Fisher trace is therefore a scalable diagnostic and training heuristic, but not a certificate of local gap behavior or matrix alignment.

---


### 102. [DecoyTrace: Toxic Decoys for Active Defense in Decentralized Federated Learning](https://arxiv.org/abs/2609.36330)

**<font color=#1a73e8>作者：</font>** Pedro Beltrán-López, Enrique Tomás Martínez Beltrán, Pantaleone Nespoli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized Federated Learning (DFL) eliminates the central aggregation server, reducing the single point of observation that traditional defenses against attacks rely on. As a result, peer-to-peer networks become exposed to malicious updates containing backdoors or semantic poisoning, since such updates can remain close to benign ones in the parameter space while behaving very differently. This may evade defenses based on passive parameter inspection. However, existing deception-based defenses have mainly been designed for centralized FL and do not jointly address local observation, poisoning propagation, source attribution, and containment in strictly serverless DFL. To address these limitations, this paper presents DecoyTrace, a proactive cyber deception-based defense for strictly serverless DFL environments. DecoyTrace deploys a mobile DecoyNode that generates decoy challenges using chaotic maps, disseminates a dual model (clean vs. decoy) based on neighbor trust, and evaluates them using three-state semantic metrics. Upon confirmation, a distributed protocol isolates the source and performs a model reset or recovery to preserve training progress. Evaluated across sixty configurations on the NEBULA platform (five datasets, three topologies, and four attack/defense scenarios), DecoyTrace systematically restores lost utility. The F1-score remains within 0.03 of the baseline on MNIST/FashionMNIST (mitigating drops of up to 0.37), matches or exceeds the baseline on EMNIST and CIFAR-100, and remains between 0.05 and 0.10 below the baseline on CIFAR-10, the most visually complex convolutional scenario evaluated. Furthermore, containment reduces CPU and network usage by up to two-thirds. These results demonstrate the feasibility of unifying deception, identification, and containment in DFL, while also identifying its limitations in complex tasks and multi-attractor threat models.

---


### 103. [Calibrating One-Round Membership Inference with Neighbors](https://arxiv.org/abs/2609.36331)

**<font color=#1a73e8>作者：</font>** Francesco Rita, Jie Zhang, Florian Tramèr  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The state-of-the-art Membership Inference (MI) methods calibrate their signal separately for each example using reference models, auxiliary models trained to exclude the target. This paradigm scales poorly to modern large models, however, whose training is too expensive to replicate. This has motivated one-round settings, where only a single trained model is available; but without reference models the per-example calibration that drives the strongest attacks can no longer be estimated, leaving the membership signal weak. We ask whether neighbors of the target point can recover this calibration without training any additional model. Our key observation is that reference models serve only to reveal how an example behaves under models not trained on it, and that querying the target model on nearby samples yields the same information. We propose two complementary ways to obtain such neighbors, and show that querying them against an early training checkpoint further sharpens the signal. We evaluate across three image classification datasets and three training setups, showing that neighbors yield strong membership signals and competitive attack performance at no additional training cost.

---


### 104. [DeepRewind: Predicting and Repairing Premature Commitments in Deep Research Agents](https://arxiv.org/abs/2609.36344)

**<font color=#1a73e8>作者：</font>** Amirhossein Abaskohi, Amirhossein Dabiriaghdam, Lele Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep-research agents conduct long-horizon investigations through iterative search, evidence evaluation, belief revision, and synthesis. However, they may commit to claims before sufficient evidence is available, causing later reasoning to reinforce an incorrect interpretation. We introduce DeepRewind, an additive control layer for reversible deep research that represents the agent's evolving epistemic state as a typed graph of sources, evidence, claims, hypotheses, assumptions, commitments, plans, and drafts. Before accepting an intermediate conclusion, a prompt-based world model predicts its impact and estimates reversibility based on hypothesis narrowing, information loss, recovery cost, and contradiction-trigger coverage. A binary controller blocks risky commitments, while a consistency monitor performs dependency-aware rollback when later evidence invalidates them. Across DRBench and LiveDRBench, DeepRewind improves insight recall by 3.6 percentage points and reduces premature commitments by 59.1% relative to Open Deep Research.

---


### 105. [Representation by Design in Generation: Cross-View Class-Token Alignment in Diffusion Transformers](https://arxiv.org/abs/2609.36348)

**<font color=#1a73e8>作者：</font>** Xiaoyu Wu, Yifei Wang, Chen Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative and representation learning remain asymmetrically connected: semantic representations are used to improve diffusion generation, whereas the models' own representations are often treated as a by-product of synthesis. We ask whether diffusion models can instead be trained to learn substantially stronger semantic representations without sacrificing generation quality. SelfFlow takes a step in this direction by introducing self-supervised patch alignment into flow matching, but its main gains remain in faster convergence and improved generation. Inspired by DINO and iBOT, we extend this framework with cross-view class-token alignment to further strengthen semantic representations. Specifically, we form two independently noised, dual-timestep observations of each image and align each student class-token representation with the stop-gradient EMA-teacher target from the other observation. This objective is optimized jointly with the inherited flow-matching and local patch objectives. Notably, although the additional objective acts only on the class token, it strengthens both class-token and patch representations. Compared with a matched two-view baseline, ImageNet linear-probing accuracy improves by 9.4\% using the class token and 10.1\% using mean-pooled patch tokens, while frozen-backbone VOC2012 segmentation improves by 3.6 mIoU. These representation gains are achieved while maintaining comparable ImageNet generation FID. In text-to-image training, the same objective also improves generation FID, reducing it from 2.52 to 2.37 at matched checkpoints. Our results show that representation need not remain a by-product of generation or merely a tool for improving it: it can be directly optimized as a first-class capability of diffusion pretraining alongside generation.

---


### 106. [Explainability from Training with Applications to TCR-Epitope Prediction](https://arxiv.org/abs/2609.36354)

**<font color=#1a73e8>作者：</font>** Jiarui Li, Zixiang Yin, Samuel Landry 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models have achieved strong performance in artificial intelligence for science, yet their black-box nature limits our understanding of how they learn scientific tasks. Existing methods for interpretability provide limited insight into how models organize evidence and evolve during learning. We introduce explainability from training (EFT), a model-agnostic paradigm that traces model interpretation during training to explain why models rely on specific features and how they organize these features as predictive evidence. We apply EFT to four state-of-the-art T cell receptor (TCR)-epitope prediction models, TCR-SRIM, TULIP, MixTCRpred, and NetTCR-2.2, spanning post-hoc and interpret-by-design approaches as well as transformers and CNNs. To investigate how structural information affects model explanations, we introduce a benchmark, TCR-XAI2, containing 388 unique experimentally resolved TCR-epitope structures, complemented by structures predicted using AlphaFold3, Boltz-2, TCRModel2, tFold-TCR, and OpenFold3. Using EFT with TCR-XAI2, we demonstrate that (1) CNN and transformer models exhibit distinct learning trajectories; (2) TCR $\alpha$ and $\beta$ evidence can conflict during learning, limiting the benefits of jointly modeling both chains, while MHC information mitigates this; and (3) real versus predicted structural data for TCR-epitope prediction exhibits distinct TCR and peptide feature preferences as well as differing trajectories of model certainty.

---


### 107. [OTT3R: Multi-View 3D Reconstruction and Fast Dataset Generation at 1% Compute](https://arxiv.org/abs/2609.36374)

**<font color=#1a73e8>作者：</font>** Brandon Leblanc, Charalambos Poullis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models have achieved impressive performance by scaling model and dataset size, but their cost excludes most research groups and precludes edge deployment. Additionally, generating 3D supervision without sensors still relies on slow, unreliable Structure-from-Motion, as the community lacks a COLMAP-like system for neural 3D pseudo-label generation. We present OTT3R (RGB-Only Tiny Transformer for 3D Reconstruction), a knowledge distillation framework that addresses both problems on a single workstation equipped with 2 GPUs. Distilling $\pi^3$ (959M parameters) into a 102M-parameter student yields 9.4$\times$ compression and up to 7$\times$ faster inference, trained at 1.6% of VGGT's training compute. An integrated pseudo-label pipeline offers a reliable, high-throughput alternative to COLMAP, generating dense per-pixel point maps and SE(3) camera poses for a 667K-image corpus in 3.5 hours on two commodity GPUs and succeeding on every sequence we tested, including those where COLMAP fails. The general student tracks the teacher on in-distribution monocular depth and, zero-shot, outperforms COLMAP on 7-Scenes and on DTU completion, but it does not replace the teacher on out-of-distribution multi-view geometry. The deployable artifact is the domain-specialized student: after specialization at 0.2% compute, it is 4$\times$ more accurate than COLMAP on 7-Scenes at 980$\times$ throughput, with near-teacher completion. Code is available at this https URL

---


### 108. [Neural Succession: A Mesoscopic Theory of Invasion, Coexistence, and Stabilization in Continual Learning](https://arxiv.org/abs/2609.36375)

**<font color=#1a73e8>作者：</font>** Shoaib Ahmed Dipu, Md Salman Shamil, Sayeed Shafayet Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning is usually studied through mechanisms that preserve old knowledge. We develop Successional Learning Theory (SLT), a mesoscopic account in which the current representation is a resident community, the incoming task is an invader, forgetting is resident displacement, joint retention is coexistence, replay is resident reinforcement, and training moves from establishment toward stabilization. Its empirical coordinate is directional pre-invasion compatibility, measured on the resident model before the incoming task is learned. Across eight experiments, compatibility orders later forgetting on the 20 directed Split-CIFAR-10 transitions (three-repeat r=-0.789, incoming-task cluster 95% CI [-0.90,-0.72], every repeat alone r<=-0.67), forecasts held-out forgetting with 24% lower error than a no-information baseline, and reproduces under controlled MNIST permutations and CIFAR-10 rotations (r=-0.804, -0.718). On an 84-transition suite, compatibility separates coexistence from exclusion at every retention threshold (AUC 0.93-0.97). Replay repairs every transition with at most 325 stored examples and is most efficient where displacement is largest. Compatibility reaches |r|=0.720, while activation, representation, Jacobian, and fixed-coefficient Lotka-Volterra specializations do not. Plasticity and feature turnover fall reliably from early to late training (15/15 and 14/15 runs). We formalize a minimum habitat-modification bound, a displacement floor, a sufficient coexistence condition, an identifiability law with a range-restriction corollary, successional stabilization, and local reinforcement. The identifiability law also predicts where the coordinate loses leverage, and the prediction matches three CIFAR-100 partitions and five optimizer regimes. SLT is a pre-adaptation diagnostic that complements replay, regularization, and projection methods.

---


### 109. [Stealth Is a Relation, Not a Property: How Event Representations Create Blind Spots for Timing Attacks in Event-Based Perception](https://arxiv.org/abs/2609.36386)

**<font color=#1a73e8>作者：</font>** Shoaib Ahmed Dipu, Md. Shaown Miah, Kamrul Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An event camera produces an asynchronous stream, but what is visible in that stream depends on how a downstream consumer, such as a model or detector, processes time. The same timestamp change may leave a coarse temporal representation unchanged while changing the response of a model that preserves finer timing. We characterize this dependence as observer-relative stealth. For recorded event streams, retiming an event within its protected accumulation window leaves the accumulated integer tensor exactly unchanged. We use this exact blind space to construct Null, a gradient-guided timestamp-retiming attack, and define SC-ASR_A(tau) to measure attack success while bounding the change visible to observer A. On DVS Gesture at a 10% event budget, Null reaches 81.56 +/- 5.81% ASR on ConvSNN and 98.67 +/- 0.45% on a GRU while preserving the protected tensor exactly. On DailyDVS-200, a protocol-scale Multi-View Fusion Network variant reaches 99.28 +/- 0.11% exact-null ASR, compared with 9.70 +/- 1.06% for its matched control. In a five-attack comparison, Null is the only method with nonzero attack success at exact observer equality, reaching 81.4% on DVS Gesture and 87.35% on DailyDVS-200. We also search the same exact blind space with an independently implemented constrained projected-gradient optimizer, C-PGD. At matched victim-gradient evaluations, C-PGD reaches 84.50 +/- 2.89% ASR on DVS Gesture and 89.55 +/- 4.39% on DailyDVS-200, again with exact protected equality. Perturbations that are exactly hidden from the protected observer become visible under shifted, finer, overlapping, and randomized temporal views. Adding observer constraints reduces the real-valued blind-space fraction from 87.5% to 75.0% to 62.5%, while DVS ConvSNN ASR falls from 74.9% to 61.9% to 37.2%. These results show that stealth is not a property of the perturbation alone.

---


### 110. ["I didn't know how to read a map, but now I can": TouchingSpace, an Audio-Haptic Map for Blind and Low-Vision Readers](https://arxiv.org/abs/2609.36404)

**<font color=#1a73e8>作者：</font>** Li Liu, Yihe Wang, Jiaming Qu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accessible map systems either make a layout explorable by hand or convey information through speech; few combine both to support pre-travel spatial understanding for blind and low-vision (BLV) people. We present TouchingSpace: a system that retrieves map data for an outdoor place and renders its surroundings as bounded regions at fixed trackpad positions. During exploration, users receive audio and haptic feedback and can ask a conversational agent open-ended questions. We conducted a user study with fourteen BLV participants who explored a place using TouchingSpace and reflected on the experience. We found participants used sound and vibration to locate places and speech to identify and describe them; the bounded surface supported discovery, revision, and spatial checks by hand; they expected this awareness to support future travel. TouchingSpace demonstrates how a laptop trackpad can support self-directed spatial exploration. These findings suggest accessible AI maps should ground conversation on bounded, user-controlled spatial surfaces.

---


### 111. [What Makes High-Magnification Knowledge Transferable? A Study of Cross-Resolution Distillation in Whole-Slide Imaging](https://arxiv.org/abs/2609.36407)

**<font color=#1a73e8>作者：</font>** Zhiyuan Yang, Jiahao Cheng, Mahdi S. Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-resolution knowledge distillation aims to improve low-magnification whole- slide analysis by transferring high-magnification representations, yet the conditions for useful transfer remain unclear. We develop a decomposition-based analysis of teacher access, representation loss, and model excess, motivating three questions: whether (a) teacher targets help the task, (b) low-magnification students can predict them, and (c) slide models benefit from those predictions. We investigate them through controlled experiments across ten pathology cohorts spanning classifi- cation, grading, and survival prediction. In the main comparison, providing teacher regional means alongside native low-magnification features improves downstream performance in all ten cohorts. Direct prediction achieves lower reconstruction error than residual prediction, yet the predicted features underrepresent variation in the teacher targets. Moreover, better reconstruction does not consistently improve downstream scores, and retaining native features changes performance even when the predicted teacher features are held fixed. Together, these findings expose a gap between reconstructing teacher representations and realizing their downstream value. They challenge the sufficiency of reconstruction error as a measure of cross-resolution transfer and provide a diagnostic framework for examining where that transfer breaks down. Future distillation designs must account for both what students can predict and how slide models use those predictions.

---


### 112. [Longer Records, Broader Invariance: The Hidden Scaling Problem in Longitudinal Contrastive Learning](https://arxiv.org/abs/2609.36409)

**<font color=#1a73e8>作者：</font>** Rameen Mahmood, Xuhai "Orson" Xu, Zachary Beattie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal data are valuable because people change. Yet the objectives used to learn from these data can inadvertently erase that change. In person-level contrastive learning, observations from the same person are treated as positives; as records grow, those positives can span increasingly distant---and increasingly different---behavioral states. More history can therefore produce not only more data, but broader invariance. We show that this distinction is fundamental. We separate \emph{record span}, how much history the learner sees, from \emph{supervision span}, how far across that history positive-pair supervision reaches. Across in-home sensing records spanning up to 2.7 years, broader supervision systematically suppresses recoverable changing-state information, even when the available history is held fixed. At the broadest span, less than 10\% of the information recoverable from an untrained encoder remains. Yet keeping positives local is not sufficient: as records grow, even distant states that are never paired become increasingly similar. Explicitly contrasting other observations from the same person reverses this loss without shortening the record, revealing a second route by which longitudinal scale can broaden invariance. Finally, we prospectively reproduce the supervision-span effect in 199 GLOBEM participants. Longitudinal scale therefore presents a choice: more history need not mean more invariance. By controlling what is held invariant as records grow, we can preserve the change that made the longitudinal data valuable in the first place.

---


### 113. [Agent-Based Evolutionary Dynamics for Mixed Autonomy Weaving Ramps](https://arxiv.org/abs/2609.36424)

**<font color=#1a73e8>作者：</font>** Sheryl Paul, Kexin Wang, Ruolin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Existing models of mixed-autonomy weaving ramps characterize how altruistic connected and automated vehicles (CAVs) can improve traffic efficiency at the population level, but provide limited insight into how such behavior emerges from decentralized vehicle interactions or how it is affected by finite populations, heterogeneous preferences, and imperfect information. We develop an agent-based model of a macroscopic weaving-ramp framework in which individual vehicles adapt their lane choices using an evolutionary game-theoretic update rule and altruism-based objectives providing a microscopic interpretation of the original Wardrop model. We prove convergence of the decentralized dynamics to the unique equilibrium predicted by the macroscopic theory. Beyond reproducing aggregate equilibrium behavior, the framework enables the study of deployment-level questions that cannot be addressed by static analysis. Simulation results demonstrate close agreement with the macroscopic predictions while revealing how convergence rates, adaptation to changing traffic conditions, heterogeneous altruism levels among CAVs, and imperfect state information influence system performance and the distribution of altruistic burden across vehicles. These results provide a bridge between equilibrium traffic theory and decentralized mixed-autonomy deployment.

---


### 114. [Towards Scalable Context-Aware Single-Cell Spatial Transcriptomics Prediction from Histology Images](https://arxiv.org/abs/2609.36429)

**<font color=#1a73e8>作者：</font>** Zijun Gao, Chunbin Gu, Jinxi Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting gene expression from H&E-stained histology images offers a scalable alternative to costly spatial transcriptomics, yet most existing methods operate at the spot level, where signals from multiple cells are aggregated and critical cellular heterogeneity is obscured. Extending this paradigm to single-cell resolution is non-trivial. Naively applying pathology foundation models faces a scale mismatch: their patch-level representations mix multiple cells, whereas per-cell cropping or resizing distorts morphology and removes local context. Conversely, segmentation-based models without strong pretrained visual encoders often lack the morphological representation capacity needed for accurate molecular prediction and inherit errors from imperfect cell boundary masks. Here, we present CELLO, an efficient end-to-end framework that performs a single pathology foundation model forward pass per image and uses grid sampling to extract location-specific features for all cells simultaneously. We further introduce a distance-decay cross-attention module that refines each cell representation using spatially biased local morphological context. Using 52 public Xenium-H&E pairs from HEST-1k that span 12 organs and approximately 10 million cells, CELLO improves the average predictive accuracy over the evaluated baselines while reducing the mean whole-slide inference time compared to DeepSpot2Cell, a 14.0x speed-up on average that excludes upstream cell segmentation. Our work establishes a scalable foundation for single-cell gene expression prediction from H&E images.

---


### 115. [Temporal-Aware Fusion for Robust Outdoor LiDAR Localization](https://arxiv.org/abs/2609.36432)

**<font color=#1a73e8>作者：</font>** Minghang Zhu, Zhijing Wang, Yuxin Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR relocalization aims to estimate the global 6-DoF pose of a sensor in the environment. However, existing regression-based approaches often encounter limitations in dynamic or ambiguous scenarios, as they typically prioritize single-frame inference, leaving the potential of spatio-temporal consistency across scans not fully explored. In this paper, we propose a Temporal-aware Localization framework (TempLoc) designed to enhance the robustness of outdoor localization by effectively modeling sequential consistency. Specifically, a Global Coordinate Estimation module is first introduced to predict point-wise global coordinates and associated uncertainties for each LiDAR scan. A Prior Coordinate Generation module is then presented to estimate inter-frame point correspondences by the attention mechanism. Lastly, an Uncertainty-Guided Coordinate Fusion module is deployed to integrate both predictions of point correspondence in an end-to-end fashion, yielding a more temporally consistent and accurate global 6-DoF pose. Experimental results on the NCLT and Oxford RobotCar benchmarks show that our TempLoc outperforms state-of-the-art methods by a large margin, demonstrating the effectiveness of temporal-aware correspondence modeling in LiDAR relocalization.

---


### 116. [RA-CFGCache: From Branch-Level Criteria to Guided-Risk Control under Classifier-Free Guidance](https://arxiv.org/abs/2609.36433)

**<font color=#1a73e8>作者：</font>** Yiming Liu, Ben Wan, Tongxuan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models enable high-quality visual generation, but iterative denoising remains computationally expensive, especially under classifier-free guidance (CFG), which requires both conditional and unconditional evaluations. Training-free caching reduces this cost by reuse of previously computed features or predictions. However, existing branch-local reuse criteria do not explicitly account for how cache errors combine under CFG or how local perturbations affect the final output. We identify two misalignments in cache control: a branch-guided mismatch, where guided error depends on both the magnitudes and alignment of branch errors, and a local-final mismatch, where the downstream impact of a local error varies across timesteps. We propose RA-CFGCache, a Risk-Aligned Caching framework under CFG that incorporates both factors while keeping the sampling schedule and guidance rule fixed. CFG-aware Guided-Risk Composition combines existing branch-wise proxies using CFG coefficients and offline-calibrated cross-branch alignment. Propagation-Aware Rescaling further weights the resulting guided-risk estimate with a timestep-dependent propagation prior calibrated from isolated reuse perturbations. An online threshold controller then determines when to jointly refresh or reuse both branches. Experiments on FLUX.1-dev, Wan2.1-T2V-1.3B, and CogVideoX-2B demonstrate improved efficiency--fidelity trade-offs over evaluated training-free caching baselines. Moreover, RA-CFGCache is compatible with diverse base proxy families, including TeaCache-, DiCache-, and MagCache-style estimators, and consistently improves fidelity at nearly unchanged latency. Code is available at this https URL.

---


### 117. [Merlin Plus: A Large-Scale, Multi-Cancer, Image-Mask-Report Dataset](https://arxiv.org/abs/2609.36436)

**<font color=#1a73e8>作者：</font>** Pedro R. A. S. Bassi, Wenxuan Li, Szymon Plotka 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-cancer segmentation in computed tomography (CT) is fundamentally limited by the scarcity of tumor masks across different organs. We present Merlin Plus, the first large-scale CT dataset with radiologist-created tumor masks across 9 organs. Merlin Plus extends the Merlin dataset by adding 1,153 per-voxel tumor masks and longitudinal metadata. To create these tumor masks, we developed a report-based active-learning framework in which radiology reports identify tumor cases for annotation and support training of a tumor segmentation model. The model generates initial masks, which radiologists review and correct to produce the final masks, reducing annotation burden while maintaining high-quality annotations. Besides tumor masks, the longitudinal metadata in Merlin Plus enables temporal modeling of cancer progression. By directly addressing the major bottleneck of limited multi-cancer segmentation masks, Merlin Plus supports scalable multi-organ cancer detection, segmentation, and longitudinal analysis in CT. Dataset is available at: this https URL

---


### 118. [Online Versatile Incremental Learning: Towards Class and Domain-Agnostic Adaptation at Any Time](https://arxiv.org/abs/2609.36442)

**<font color=#1a73e8>作者：</font>** Jae-Ho Lee, Min-Yeong Park, Jun-Yeong Moon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual learning enables vision systems to adapt to ever-changing data distributions. Despite significant advances, existing approaches fail to capture continuous and concurrent shifts in classes and domains, a critical capability for real-world deployment. This work introduces Online VIL (Online Versatile Incremental Learning), a novel scenario where class concepts and visual domains evolve simultaneously online without explicit boundaries. To better adapt to the challenges of such dynamic environments that more closely resemble real-world conditions, we propose a novel framework TopFlow, Topology preservation with Flow matching representation that contains two complementary mechanisms: Domain-agnostic Flow Matching (DFM) and Global Topology Preservation (GTP). DFM guides the model to have domain-agnostic representations by integrating the geodesic flow kernel into contrastive learning. In contrast, GTP maintains the global structure of the feature space without explicitly storing past examples. Our extensive experiments demonstrate that TopFlow effectively addresses the limitations of existing methods within the Online VIL scenario, achieving state-of-the-art performance in challenging Online VIL. The proposed methods suggest potential directions for building continual learning systems in realistic dynamic environments. Our implementation code is available at this https URL.

---


### 119. [Channel-Dependent State Space Model for Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.36453)

**<font color=#1a73e8>作者：</font>** Yu-Cheng Wu, Fan-Keng Sun, Li-Chun Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting (MTSF) is critical across many real-world domains. Existing deep learning approaches fall into two paradigms with distinct limitations: channel-independent (CI) methods unconditionally ignore cross-variable dependencies and model only temporal dynamics, while channel-dependent (CD) methods consider both but typically rely on architectural compromises to mitigate overfitting and computational overhead. We therefore propose Chameleon, a specialized CD state space model (SSM) that enables data-dependent, fine-grained interactions across variables while scaling linearly with their number. By connecting selective SSMs with the Kalman filter, we leverage the missing measurement update in the former for cross-variable modeling while preserving the SSM backbone for robust temporal modeling. We further identify favorable inductive biases of GatedDeltaNet for time series, adapt it as our backbone, and improve generalization through additional techniques, including a previously unexplored stochastic perturbation of reversible instance normalization. On strongly dependent ODE and PEMS datasets, Chameleon achieves the best MSE and MAE across all settings, while its CI ablation and prior CD methods incur 61-178% higher MSE on average. Across 28 standard benchmark settings, Chameleon also achieves better MSE and MAE than each baseline in at least 27 and 22 cases, respectively. Training-time and peak-memory analyses on Traffic and ETT further demonstrate competitive efficiency and favorable memory scalability across different variable counts.

---


### 120. [DynamicHOI: Coupled Dynamics for Physics-aware HOI Reconstruction](https://arxiv.org/abs/2609.36454)

**<font color=#1a73e8>作者：</font>** Wenliang Guo, Zhanbo Huang, Yu Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study hand-object interaction (HOI) reconstruction from monocular RGB videos, where partial observations can produce visually plausible yet mechanically inconsistent trajectories. Existing methods mainly enforce visual and geometric agreement, leaving the underlying interaction dynamics insufficiently constrained. We propose DynamicHOI, a physics-aware HOI reconstruction framework combining geometry-grounded diffusion refinement with coupled hand-object dynamics. Geometry spatially grounds visual evidence for trajectory refinement, while articulated inverse dynamics and Newton-Euler dynamics derive hand generalized forces and object wrenches for dynamics-level supervision. We further couple hand and object dynamics through contact-force transfer and recover active hand actuation as an interaction-level physical quantity. We formulate its empirical magnitude distribution into a probabilistic prior that penalizes unlikely actuation and suppresses mechanically implausible reconstructed motion. Experiments on three HOI datasets show consistent improvements in both hand and object reconstruction. The reconstructed trajectories further benefit downstream applications including hand world-model generation and robotic manipulation learning, demonstrating the value of physics-aware HOI modeling beyond reconstruction.

---


### 121. [Memory Consolidation Flattens the Temporal Shape of User Facts](https://arxiv.org/abs/2609.36457)

**<font color=#1a73e8>作者：</font>** Sugam Panthi, Muhaiminul Yeamin, Siyan Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory systems turn conversations into short stored notes. A note can keep a user fact while losing evidence about whether the fact still holds. For example, "I am driving a Peugeot" can become "The user drives a Peugeot," which drops the cue that the activity is ongoing. We call this aspectual flattening and measure it with LAPSE, a benchmark of matched user statements that differ only in temporal form. We find that memory writers flatten aspect selectively. Three writer models flattened the progressive statement but kept its simple-present match in 244 of 381 pairs, never the reverse. The asymmetry holds in all 11 model configurations tested and in the installed pipelines mem0, Graphiti, and Letta. The lost cue matters to later readers. In exploratory tests, changing only the stored verb shifted all three readers' estimates that a fact still holds. When readers could ask the user before acting, two of three acted without asking more often on flattened notes. Our planned memory-use task could not detect this, because readers there acted on almost every stored fact, even expired ones. Memory writing can thus remove evidence that later models use to decide whether to act.

---


### 122. [Fisher-IRG: Fisher-Induced Local Invariant Representation Geometry across Language and Vision Models](https://arxiv.org/abs/2609.36458)

**<font color=#1a73e8>作者：</font>** Abdullah All Tanvir, Xin Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic-preserving transformations can induce substantial motion in learned representations, while small changes may strongly affect model predictions, raising a basic question: what local metric best captures semantically consequential variation? We propose Fisher-induced invariant representation geometry (Fisher-IRG), which measures local representation directions through their predictive sensitivity. Around each representation, we construct semantic-preserving and semantic-changing neighborhoods, aggregate their local Fisher information, and recover invariant directions through a contrastive generalized eigenvalue problem. Controlled displacement analyses first show that comparable Euclidean motion can have substantially different predictive consequences, supporting the need for a predictive geometry. Across language and vision models, Fisher-IRG yields stronger semantic-versus-nuisance predictive selectivity and generally more reproducible subspaces than covariance-based geometry, while recovering systematically distinct local directions. Representation interventions further localize semantic effects to the Fisher-derived subspace, and held-out separation and retrieval show that the recovered geometry generalizes beyond the discovery neighborhoods. These results support Fisher-IRG as a principled framework for characterizing local invariant representation geometry.

---


### 123. [DisCoMBO: Steering Expert-in-the-Loop Black Box Optimization via Distributional Conformance](https://arxiv.org/abs/2609.36472)

**<font color=#1a73e8>作者：</font>** Jonas Seng, Bennet Wittelsbach, Kristian Kersting  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential Model-Based Optimization (SMBO) traditionally relies on Bayesian or ensembling surrogates for uncertainty quantification. While historically treated as fully data-driven, SMBO increasingly integrates external domain expertise to accelerate discovery. To overcome the opaque guidance and diminished integration fidelity of standard acquisition re-weighting, Probabilistic Circuits (PCs) have emerged as a generative surrogate alternative, enabling direct knowledge injection via conditional sampling. However, these generative routines lack the formal exploration-exploitation semantics required for rigorous optimization. We introduce the Distributional Conformance Score (DisCo), a novel metric that unifies the flexibility and efficiency of PCs with a formal uncertainty framework. DisCo provides a bounded, $[0, 1]$-normalized measure of model "surprise" that (1) recovers properties comparable to kernel-based uncertainty known from, e.g., Gaussian Processes, while maintaining linear-time inference, and (2) enables accurate assessment of conformance of external knowledge w.r.t. model evidence. We then present DisCoMBO, a framework leveraging these properties for robust, knowledge-aware optimization. We prove that DisCoMBO is a zero-regret algorithm and demonstrate its effectiveness across diverse benchmarks from AutoML, material optimization, and wind park optimization.

---


### 124. [Going Beyond State-Reaching: Learning Abstractions for Intrinsically Motivated Option Discovery](https://arxiv.org/abs/2609.36473)

**<font color=#1a73e8>作者：</font>** Akhil Bagaria, Anita De Mello Koch, George Konidaris  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal abstraction via options can improve exploration in large environments. However, existing option discovery algorithms find subgoals that target all aspects of the state simultaneously. This state-reaching approach produces options that only apply in narrow regions of the state-space, eventually causing an explosion in the number of options that overwhelms the agent, and impedes progress on its primary task of reward maximization. We introduce an algorithm that instead identifies a small, relevant subset of features for each subgoal, yielding options that generalize broadly and accelerate exploration. Our approach learns abstract, transferrable options and achieves rapid exploration in three sparse-reward, image-based domains, including the Atari game MontezumasRevenge.

---


### 125. [Guard Models Are Overconfident Where Base Models Are Uncertain](https://arxiv.org/abs/2609.36477)

**<font color=#1a73e8>作者：</font>** Jonghyun Hong, MinJae Jung, Minwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guard models are used as safety classifiers, with confidence scores driving downstream moderation decisions. We evaluate five guard models for prompt classification and find that although several are nearly calibrated on clean inputs, adversarial attacks degrade their calibration by an order of magnitude, turning false negatives into high-confidence errors indistinguishable from correct detections. Comparing each guard with its corresponding base LM, we find that uncertainty signals often remain available, with the base model typically expressing uncertainty on the same inputs where the guard fails. Layer-wise analyses localize this guard-base divergence to later layers, where guard models exhibit sharper safe/unsafe separation and lower-rank representations, while adversarial harmful inputs lie closer to the clean-safe region. These findings highlight a mismatch between guard confidence and base model uncertainty under attack.

---


### 126. [Learning to Harvest Without Collapse in a Regenerative Commons: A Lagrangian Framework](https://arxiv.org/abs/2609.36478)

**<font color=#1a73e8>作者：</font>** Jose Tupayachi, Xueping Li, Soham Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The tragedy of the commons poses a multi-agent safety problem: reward-seeking agents can deplete a shared resource, and cooperation among its users does not itself specify how much must be preserved. We make preservation an explicit requirement by formulating a regenerative commons as a constrained Markov game or a constrained multi-agent MDP with a designer-specified depletion budget. We develop a nonstationary Lagrangian framework that constructs a policy sequence from solutions of unconstrained games or cooperative control problems. Extending earlier time-average constructions, we introduce average-epoch solution concepts for reset episodes with discounted rewards and terminal costs. We prove a reward-independent feasibility certificate, cooperative feasibility and approximate optimality against feasible policy mixtures, and an extension to unbiased sampled costs. For self-interested agents, a constrained Nash certificate quantifies the price-dispersion term introduced by deviations that redistribute budget across epochs. Under the stated assumptions on solver accuracy and multiplier updates, these results give constrained policy-sequence guarantees using solutions of unconstrained problems. Experiments with constrained IPPO and MAPPO in a Gordon-Schaefer fishery examine how depletion budgets shape stock retention, harvest rewards, and price adaptation.

---


### 127. [Human-AI Collaboration: From Paradoxes to Patterns](https://arxiv.org/abs/2609.36481)

**<font color=#1a73e8>作者：</font>** Michael Weiss  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence shows that humans and AI systems perform better together, by collaborating, than alone. This paper examines two key design dimensions of human-AI collaboration (autonomy and initiative) and explores the collaboration patterns that they generate. Documenting these patterns starts with identifying the underlying problems and solutions, followed by examining the internal tensions within the problems. The paper uses a paradox perspective to analyze those tensions. It describes a process for surfacing the tensions and mapping the underlying paradoxes. It also illustrates how the pattern descriptions can be derived from mapping these paradoxes. Finally, the paper documents four human-AI collaboration patterns: Instruction, Delegation, Assistance, and Co-creation.

---


### 128. [Optimal Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2609.36486)

**<font color=#1a73e8>作者：</font>** Zijun Chen, Zihan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study an unknown-transition finite-horizon Markov decision process (MDP) with a finite collection of known reward functions $\{r^1, r^2, \ldots, r^M\}$. The goal is to output an $\epsilon$-optimal policy for every reward using online episodic interaction only. Performance is measured by the policy error $V_{0}^{*, m} - V_{0}^{\widehat\pi^{m}, m}$ where $m\in [M]$ represents the reward function and $V_{0}^{*, m}=\mathbb{E}_{s_1\sim \mu}[V_{1}^{*, m}(s_1)]$. Under this setting, we design a provably efficient algorithm to establish a minimax sample complexity bound of $$ O\left(\frac{SAH^3}{\epsilon^2}\log M \mathrm{polylog}\left(\frac{SAH\log M}{\min\left\{\epsilon, 1\right\}\delta}\right)\right)$$ episodes, with no additional burn-in cost. This matches the information-theoretic lower bound up to a factor of $ \mathrm{polylog}(SAH\log M/(\min\left\{\epsilon, 1\right\}\delta))$. Our method combines three technical ingredients. First, we adapt MVP to reward-switching learning to construct optimistic value estimates. Second, we use fresh replay samples to conservatively evaluate the candidate policies. Third, gap-based multiplicative weights updates adjust the reward-sampling distribution using the differences between these estimates, converting weighted learning progress into simultaneous guarantees for all rewards.

---


### 129. [Reimagine Video Dynamics](https://arxiv.org/abs/2609.36496)

**<font color=#1a73e8>作者：</font>** Yu Yuan, Yawen Lu, Guoxian Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most video editing methods focus on changing the appearance of the source video, while offering limited control over its dynamics. We introduce Reimagine Video Dynamics (RVD), a framework that disentangles a compact, editable dynamics token from visual context. We learn this token through self-supervised reconstruction: given the first frame as visual context, a renderer must recover the original video from the dynamics token, encouraging it to capture how the scene evolves rather than how it looks. This disentanglement allows video dynamics to be edited directly while preserving visual context. We develop a language-guided dynamics-token editor that transforms source dynamics into target dynamics, and train it with a scalable counterfactual video-pair pipeline and a two-stage training strategy. Extensive experiments show that RVD enables effective video dynamics editing, training-free retiming, and appearance-controlled re-rendering.

---


### 130. [Towards Breaking the Learning System Wall Using Multimodal Tutoring Transcriptions](https://arxiv.org/abs/2609.36502)

**<font color=#1a73e8>作者：</font>** Danielle R. Thomas, Marie Cynthia Abijuru Kamikazi, Ashish Gurung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Past research using log data has faced the "learning system wall," whereby few methods exist for generalizing models of student learning across platforms. Increasingly, online learning is captured by richer forms of data, including dialog and video, with new affordances. An example of this is remote tutoring programs, where human tutors support students who use learning systems while video conferencing. Toward better platform-general modeling of learning, we introduce an AI-driven multimodal transcription system that processes screen-recording videos into unified screenplay-style transcripts containing audio dialogue and annotated learning log actions. We describe a planned method for temporally aligning AI-generated multimodal transcripts with MATHia learning logs and for identifying and classifying student learning processes to align with MATHia logs. Lastly, we highlight challenges and potential solutions in capturing learning processes in one system, offering initial steps towards generalizing log data across diverse systems.

---


### 131. [AVIO: Learning to Add and Remove Sounding Objects in Audiovisual Scenes](https://arxiv.org/abs/2609.36503)

**<font color=#1a73e8>作者：</font>** Weihan Xu, Kan Jen Cheng, Koichi Saito 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adding or removing a sounding object requires coordinated changes to visual content and sound while preserving the surrounding scene. Yet paired supervision for localized non-speech audiovisual editing remains limited, as visual and acoustic edits must target the same object and isolate its sound from overlapping sources. To address this gap, we introduce \textit{AVIOBench}, a dataset comprising 37.9 hours of paired audiovisual examples spanning 1{,}878 target-object names. AVIOBench links the visual presence and acoustic contribution of each target object through a shared identity and visual mask. Our automated pipeline uses visual grounding and cross-modal consistency to select target-sound removal candidates, then jointly refines the audiovisual pairs to improve perceptual quality and cross-modal consistency. Building on this dataset, we propose \textit{AVIO}, which adapts a pretrained text-to audiovisual generation model through source-conditioned feature modulation to jointly learn object addition and removal. A reference-frame curriculum gradually reduces reference conditioning during training, enabling one model to perform instruction-only editing with optional visual guidance. Quantitative and qualitative evaluations demonstrate effective audiovisual object removal and addition, with optional reference guidance providing appearance and placement control for addition.

---


### 132. [Efficient and Scalable Physics-Guided Fully Convolutional Spatiotemporal Learning for 3D Microstructure Evolution Prediction](https://arxiv.org/abs/2609.36504)

**<font color=#1a73e8>作者：</font>** Michael Trimboli, Wenxi Liu, Xianqi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of three-dimensional (3D) microstructure evolution remains computationally demanding because high-fidelity phase-field simulations require repeated numerical integration over large volumetric domains and long temporal horizons. This study develops an efficient and scalable physics-guided fully convolutional spatiotemporal framework for direct multi-frame prediction of complete 3D microstructure sequences. The model combines shared 3D spatial encoding and decoding with a factorized latent translator that integrates temporal, local 3D spatial, and channel interactions. A discrete Cahn--Hilliard (CH) residual is incorporated during training to regularize the learned evolution toward the governing dynamics without altering the inference pathway. The framework is evaluated on high-resolution 3D spinodal-decomposition trajectories under nominal, long-horizon, and reduced-temporal-context forecasting. Under full temporal context, the model accurately reproduces volumetric evolution, with average 3D structural similarity remaining above 0.97 over the nominal prediction horizon. Physics guidance becomes increasingly beneficial as temporal information is reduced, improving predictive robustness and preservation of interface-level morphology. The framework also achieves more than a 30-fold wall-clock speedup relative to the reference spectral phase-field solver, while physics guidance introduces no additional inference cost. These results establish direct multi-frame, physics-guided fully convolutional learning as a high-throughput surrogate strategy for dense 3D phase-field dynamics and repeated microstructure forecasting.

---


### 133. [PDE-OBS: Controlled Evaluation Across Observation Patterns](https://arxiv.org/abs/2609.36521)

**<font color=#1a73e8>作者：</font>** Ruichen Xu, Siyao Wang, Fang Wan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical-field reconstruction and forecasting depend on both measurement density and spatial layout, yet evaluation under a single observation pattern does not characterize performance when that pattern changes. We introduce PDE-OBS, an integrated benchmarking platform spanning numerical data generation, model training, and inference and evaluation under varying observation conditions. It combines 560,000 fields and trajectories from seven partial differential equation families with configurable observation operators and seven adapted baseline methods for stationary reconstruction and short-horizon forecasting. Separating observation construction from physical records allows users to specify parameterized patterns and deterministic mixtures for training and testing while preserving prediction targets and data splits. The evaluation protocol uses references trained for each test pattern to compare models on identical test observations and targets, alongside equal-count groups for spatial-layout comparisons. On a 14,000-record subset, we evaluate 441 trained models under nine test patterns, yielding 3,969 evaluations. Mean cross-pattern error exceeds mean matched-pattern error in all 49 PDE-method pairs, and this finding persists in a configuration-matched subset of 117 models. Denser test observations do not consistently reduce error for a fixed model. Mixed-pattern training on five completed pairs reduces large single-pattern transfer errors, although destination-trained references usually remain more accurate. Together, the benchmark and findings support systematic evaluation of observation-pattern sensitivity and provide a reusable workflow for developing methods under changing measurement conditions. Code: this https URL.

---


### 134. [SCOPE: Observation-Conditioned Full-Target Prediction for Sparse PDE Inference](https://arxiv.org/abs/2609.36527)

**<font color=#1a73e8>作者：</font>** Ruichen Xu, Siyao Wang, Fang Wan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering complete physical fields from sparse observations is challenging because the measurements may not uniquely determine the underlying state. Diffusion-based PDE solvers address this problem through iterative sampling whereas neural operators provide deterministic one-pass predictions. We propose SCOPE (Sparse-Context Observability-aware Predictive Embeddings) to recover complete PDE fields from sparse observations by coupling full-field latent prediction with physical reconstruction. A shared decoder reconstructs fields from both predicted and complete-view representations so that representation learning is guided by both physical recovery and latent matching. We derive a quadratic risk decomposition at fixed teacher-decoder pairs showing why optimal latent prediction need not yield optimal field reconstruction. We also establish sufficient conditions for decoder improvements on complete inputs to transfer to recovery from partial observations. Experiments across five PDE settings show that SCOPE outperforms mask-aware neural operators on all ten forward and inverse tasks and achieves lower errors than those reported for diffusion-based solvers including DiffusionPDE and FunDPS. Decoder-only adaptation further improves recovery without retraining the backbone while retaining deterministic single-pass inference.

---


### 135. [Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models](https://arxiv.org/abs/2609.36531)

**<font color=#1a73e8>作者：</font>** Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ehécatl Sacamch'en Núñez Rico 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are largely regarded as predictive models of the physical world and are therefore expected to anticipate the consequences of observed events. However, evaluation has mainly focused on reference similarity, physical-law consistency, or judgment plausibility, estimating anticipation only indirectly. We address this directly: when a release or impact has just occurred but its consequence is withheld, can a world model anticipate what should happen next? We introduce an event-anchored evaluation based on 62 controlled real-world free-fall recordings and 124 clips spanning three object types, with fine-grained release and impact annotations and ground-truth trajectories. The protocol separates consequence production, temporal placement, and physical realization. Across six contemporary video generation and world models, Runway and Veo produce release and subsequent impact events at rates above 93% but often initiate them substantially late, whereas Cosmos-Predict-2.5 and MAGI-1 frequently preserve the pre-event state and produce little or no measurable consequence. Among measurable falls, plausible timing does not necessarily imply physically consistent motion. We further conduct a 15-participant, 20-condition human study in which participants describe the expected consequence from a single event-anchored frame and draw its trajectory. Human predictions favor the recorded future in aggregate while revealing genuine ambiguity among plausible continuations. Overall, physical foresight emerges as a sequence of distinct challenges: initiating a consequence, anchoring it in time, and realizing its motion.

---


### 136. [SCCM: Spherically Consistent Coarse Matching for ERP Dense Feature Correspondence](https://arxiv.org/abs/2609.36545)

**<font color=#1a73e8>作者：</font>** Gyeonggwan Lee, Eunsoo Im, Seunghwan Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Equirectangular projection (ERP) is the standard representation for 360$^\circ$ imagery, and robust dense feature matching on ERP underpins panoramic stereo, view synthesis, and omnidirectional SLAM. Dense matchers trained on flat images degrade systematically on ERP because the chart introduces three coupled distortions -- topological, metric, and area -- that standard coarse matching and visibility estimation do not explicitly model. We show that correcting the three distortions at the coarse-stage interfaces where they arise -- pairwise distortions in attention, per-pixel distortion in covisibility gating -- improves PCK@$1^\circ$ from 0.229 to 0.275 on Matterport3D under a fixed coarse scaffold, with the refiner architecture unchanged -- our central result. Concretely, SCCM (Spherically Consistent Coarse Matching) augments a chart-naive cross-attention/dual-softmax coarse matcher with two sphere-derived priors: Spherical Positional Attention (SPA) pairs a yaw-periodic RoPE (topology) with a tangent-plane bias (metric), and Area-Aware Covisibility (AAC) applies a pre-sigmoid log-area correction (area). The chart-naive scaffold serves as a controlled reference, separating the scaffold-replacement effect from the spherical-prior effect. Instantiated in the RoMa V1 framework with the same frozen encoder, refiner architecture, and loss, SCCM also outperforms the ERP-native EDM (0.163) and an ERP-retrained RoMa V1 (0.198) under a unified ERP dense matching protocol, while perspective-trained matchers largely fail on ERP. It further transfers zero-shot to Stanford2D3D and, when trained on outdoor Holo360D, leads there as well.

---


### 137. [SERA: Scale-Equalized Rollout Allocation for Maximum Likelihood Reinforcement Learning](https://arxiv.org/abs/2609.36552)

**<font color=#1a73e8>作者：</font>** Zihao Chen, Fanxiang Xiong, Hongran Ren 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maximum Likelihood Reinforcement Learning (MaxRL) targets prompt-wise log-success and has shown strong performance on reasoning tasks. Under finite rollout budgets, however, the estimator used by MaxRL attenuates each prompt's likelihood gradient by a factor that depends on its success probability and rollout count. Under uniform rollout allocation, the common rollout count fails to compensate for success-dependent attenuation, leaving low-success prompts more strongly attenuated and distorting their relative contributions to the expected aggregate gradient. We introduce SERA (Scale-Equalized Rollout Allocation), which redistributes a fixed rollout budget to approximately equalize these finite-rollout scaling factors. Building on our theoretical analysis of how finite rollouts distort prompt-wise likelihood gradients, we formulate the allocation as a fixed-budget max--min problem, derive a waterline solution to its continuous relaxation, and introduce a multiplicity correction to remove the additional prompt weighting induced by heterogeneous rollout counts. Experiments show stronger alignment with exact likelihood gradients in a controlled ImageNet setting and improved multi-sample solution coverage over MaxRL on maze navigation and mathematical reasoning under matched training rollout budgets.

---


### 138. [HiTS-CL: A Continual Learning Framework for Long-Horizon Temporal Knowledge Graph Extrapolation](https://arxiv.org/abs/2609.36559)

**<font color=#1a73e8>作者：</font>** Yansong Liu, Rui Liu, Yuan Zuo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extrapolative temporal knowledge graph reasoning (TKGR) predicts future facts from historical snapshots. Most existing methods train once on an early prefix of the timeline and then use a frozen model for all future timestamps. We argue that this fixed-prefix protocol is misaligned with extrapolation. It learns from a static prefix, whereas the target stream is non-stationary: new entities and facts emerge, temporal dependencies shift across regimes, and recurring historical signals must be refreshed online. As a result, models trained only on early snapshots become outdated and degrade over long horizons. We address this mismatch by formulating extrapolative TKGR as continual learning over streaming snapshots. Under this view, effective extrapolation must jointly handle current dynamics, stable knowledge, and recurring historical evidence. Based on these requirements, we propose History-enhanced Two-Step Continual Learning (HiTS-CL), a backbone-agnostic continual learning framework for extrapolative TKGR.  HiTS-CL tracks current dynamics via continual fine-tuning, preserves stable knowledge via multi-teacher adaptive distillation, and retains recurring historical evidence via a selective memory of recent and frequent facts. We integrate HiTS-CL into five representative TKGR backbones and evaluate it on four benchmark datasets. HiTS-CL consistently improves extrapolation accuracy, reduces long-horizon degradation, and outperforms strong continual-learning baselines, including a recent method for temporal knowledge graphs. Source code and data are available at this https URL.

---


### 139. [FM-ReID: Selective Competitive Token Routing for Object Re-Identification](https://arxiv.org/abs/2609.36560)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Xiaowei Zhou, Zeyuan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object re-identification (ReID) faces a recurring challenge: different identities can share highly similar global appearances, while the cues that distinguish them are localized, heterogeneous, and visible only under particular viewpoints. This challenge arises in animal ReID through markings, contours, and scars, in person ReID through subtle clothing and accessory cues, and in vehicle ReID through localized appearance details. Although visual foundation models encode such information in dense tokens, a single holistic descriptor can obscure discriminative local signals. We propose FM-ReID, an end-to-end framework that formulates local representation learning as selective competitive token routing. Its Competitive Fine-grained Mining module uses multiple mining queries and a residual query to compete for dense DINOv3 tokens. Above-prior selection retains tokens preferentially allocated to each mining query, while the residual slot receives tokens excluded from the retrieval descriptors. The resulting multi-query descriptors are jointly trained with a holistic representation for retrieval, without fixed spatial partitions or equal-area constraints. FM-ReID achieves strong results on animal, person, and vehicle ReID benchmarks, supporting competitive token routing as an effective way to augment holistic foundation-model representations.

---


### 140. [AffectReveal: Event-Grounded Emotion Recognition Beyond Visual Appearances](https://arxiv.org/abs/2609.36563)

**<font color=#1a73e8>作者：</font>** Yihao Qian, Runhao Zeng, Sicheng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual emotion recognition commonly assumes that all evidence required for prediction is contained in the observed image or video. Yet the same visible reaction can convey different emotions depending on events beyond the input: tears, for example, may indicate grief or joy. We formulate Event-Grounded Emotion Recognition (EGER), where emotion recognition requires recovering the affect-determining event. We construct EGER-Bench, comprising 10,052 videos and 10,734 images across 11 emotions, two source domains, and four visual settings. A study with six annotators shows that event context raises human recognition accuracy from 33.96% to 72.08%, confirming that visual evidence alone is often insufficient. Semantic relevance alone does not solve EGER: a plausible event may imply the wrong emotion if its identity, focal-person role, relationship, or outcome is misinterpreted. We therefore propose AffectReveal, a tuning-free framework that first constructs and independently verifies evidence-grounded alternatives over these affect-critical factors. It then cross-checks the recovered event against face-masked in-media facts through bidirectional atomic evidence support, while retaining the original unmasked input for final prediction. Across three downstream models and four input settings, AffectReveal yields average UAR gains of 5.26--10.53 points. For three fine-tunable models, it also enables untuned models to outperform their fine-tuned visual-only counterparts in all 12 accuracy comparisons, without updating downstream parameters.

---


### 141. [Sharp Convergence and Sampling Trade-offs for Riemannian Diffusion under Nonnegative Ricci Curvature](https://arxiv.org/abs/2609.36568)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Longbo Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as state-of-the-art generative models, with recent extensions from Euclidean spaces to Riemannian manifolds. However, existing convergence guarantees for Riemannian diffusion models typically require $\tilde{O}(\mathrm{poly}(d,T)/\epsilon^2)$ score evaluations, with potentially unfavorable dependence on the dimension. In this work, we develop a general framework that separates score discretization from Brownian-motion simulation and allows multiple geodesic random-walk steps per score evaluation. Under nonnegative Ricci curvature assumption and an exact Brownian-motion simulation oracle, we show that $\tilde{O}(d/\epsilon^2)$ score evaluations suffice to achieve an $\epsilon^2$ KL divergence from the target distribution, matching the existing convergence rate of Euclidean diffusion models. We further show that $\tilde{O}(d^4T/\epsilon^2)$ geodesic random-walk steps suffice to approximate the required drifted Brownian motion to $\epsilon$ total variation error. Combining these results yields a sampling scheme with $\tilde{O}(d/\epsilon^2)$ score evaluations and $\tilde{O}(d^4T/\epsilon^2)$ geodesic random-walk steps, motivating multiple random-walk steps between consecutive score evaluations. Our results provide a sharper characterization of the convergence and sampling complexity of Riemannian diffusion models.

---


### 142. [From Checkpoint Variation to Selection Gains in Supervised Fine-Tuning](https://arxiv.org/abs/2609.36569)

**<font color=#1a73e8>作者：</font>** Yupeng Chang, Wenxuan Zhang, Yuan Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Checkpoint selection is a routine decision in supervised fine-tuning (SFT): training produces multiple checkpoints, but only one is retained. Yet fixed-budget comparisons do not by themselves distinguish three empirical claims: whether more validation data improve checkpoint selection, whether a selection rule outperforms validation-loss selection, and whether it improves over simply retaining the final checkpoint. We therefore treat checkpoint selection as a finite-information decision problem. Holding completed training trajectories, candidate checkpoints, and independent test items fixed, we vary the validation budget and separately measure improvement from additional validation data, gain over negative log-likelihood (NLL) selection, and gain over the final checkpoint. Across 60 mathematical SFT trajectories and 19 configurations, increasing the validation budget from 32 to 305-313 examples raises independent-test accuracy by 0.32 percentage points (pp) for generated-accuracy selection and 0.29 pp for checkpoint agreement, with 95% configuration-bootstrap CIs of [0.10, 0.56] and [0.11, 0.50], respectively. At the full validation budget, the two generation-based rules outperform matched NLL selection by 0.71 and 0.85 pp, respectively, while their gains over the final checkpoint remain unresolved. A cross-domain replication on 12 newly trained Commonsense trajectories shows the same qualitative separation: increasing the validation budget from 32 to 1,024 questions improves generated-accuracy and checkpoint-agreement selection by 0.87 and 0.27 pp, while gains over the final checkpoint again remain unresolved. Together, these results show that benefiting from more validation data, outperforming NLL selection, and outperforming the final checkpoint are distinct empirical claims that require separate evidence.

---


### 143. [Factorized Scheduling Principle: Learning Interpretable and Transferable Policies via Structured Additive Functions](https://arxiv.org/abs/2609.36578)

**<font color=#1a73e8>作者：</font>** Hong Je-Gal, Hyun-Suk Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scheduling problems arise from repeatedly selecting one item from a set of candidates based on their states. These problems often reduce to assigning priority scores and choosing the highest-ranked item. In this work, we propose a factorized scheduling principle (FSP) framework to learn interpretable and transferable scheduling rules. The FSP framework represents system states as condition distributions and decomposes a global scheduling principle into additive univariate and pairwise components with identifiability constraints. The scheduling principle enables the framework to maintain a simple priority-based structure during deployment. This principle is learned by using a policy-based objective combined with a temporal-difference signal defined on the condition distribution. Experiments on synthetic and realistic scheduling tasks demonstrate the FSP framework's strong performance, interpretability, and zero-shot generalization across different system scales.

---


### 144. [Making Analog Training Scale: Co-Designing Mapping, Optimizer, and Converters](https://arxiv.org/abs/2609.36584)

**<font color=#1a73e8>作者：</font>** Zhaoxian Wu, Tayfun Gokmen, Omobayode Fagbohungbe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analog in-memory computing (AIMC) offers an alternative for model training by executing matrix operations directly where weights are stored. However, scaling AIMC to train modern deep models remains an open challenge due to severe hardware non-idealities, including physical weights with finite dynamic range and write granularity, analog-digital converters with finite resolution, and noisy and asymmetric updates. Guided by the insight that gradient accumulation is sensitive to precision and rounding errors, we adopt a mixed-precision training paradigm: executing forward and backward matrix multiplications in the analog domain while computing weight gradients in the digital domain. To enable scalable training, we present a holistic system-algorithm co-design that co-optimizes weight mapping to ensure well-conditioned physical and logical weight profiles, couples a preconditioned optimizer with threshold-triggered open-loop pulsing to stabilize training trajectories, and aligns converter dynamic ranges to suppress quantization errors. Evaluated via hardware-calibrated architectural simulations calibrated with electrochemical RAM measurements, our framework scales Transformer training up to $123\text{M}$ parameters with validation loss scaling as $L\propto N^{-0.231}$, where $N$ is the parameter count, comparable to $L\propto N^{-0.238}$ for digital training.

---


### 145. [Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598)

**<font color=#1a73e8>作者：</font>** Ziying Zhang, Litao Li, Junchao Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A video can exhibit convincing motion and photorealism yet fail immediately when visual text collapses. Unlike generic scene content, visual text is unforgiving in video generation: minor stroke corruption, temporal instability, or editing errors instantly break legibility and realism. Existing benchmarks overlook this challenge by treating text as incidental or using static OCR metrics that ignore temporal dynamics. We introduce VidScribe, a unified diagnostic benchmark spanning four generation regimes: writing from language (T2V), transferring text identity from a reference (R2V), sustaining text under dynamics (I2V), and localized text editing (V2V). VidScribe contains 803 human-verified samples across a 12-axis conditionally orthogonal factor space covering Intrinsic Text Properties, Physical Imaging Conditions, and Temporal Behavior. For reliable evaluation, we build a track-grounded, gated suite with 11 shared metrics and 2 task-specific probes under strict measurability conditions. Benchmarking 11 commercial and open-source systems shows that video text capability is non-monolithic, with content recognition decoupled from stroke-level glyph correctness. Performance is highly task-asymmetric: I2V sustains text most reliably, whereas V2V editing is the primary bottleneck. Counter-intuitively, degradation concentrates on a small subset of text-centric structural and temporal factors rather than adverse imaging conditions. Further probes show that visual references improve glyph and typographic fidelity rather than content accuracy, while localized editing fails to isolate target text without corrupting undeclared source text. Beyond evaluation, VidScribe also provides an actionable training signal, where benchmark-aligned preference optimization measurably improves visual text generation. this https URL.

---


### 146. [Scaling Video Generation for Reasoning: At What Cost?](https://arxiv.org/abs/2609.36599)

**<font color=#1a73e8>作者：</font>** Weihang Guo, Xiaoyu Wu, Yifei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study whether scaling video generation enables models to reason about hidden information from the past frames, and at what computational cost. Our controlled benchmark requires predicting nine prescribed moves of an initially solved 2x2x2 Rubik's Cube from a fixed view of three faces. Correct predictions require inferring how actions change hidden states, and the simulator provides exact ground truth for evaluation. Models learn plausible cube geometry early, while correct sticker configurations require substantially more training. Although validation MSE follows approximate power-law scaling, lower MSE loss does not reliably indicate downstream reasoning capabilities. Smaller autoregressive models achieve higher state accuracy with limited compute, while larger models reach higher accuracy after more training. At roughly 0.1 PF-days, the 70M-parameter model correctly predicts the visible sticker configuration in 44.6% of post-action frames, compared with 0.3% for the 1B model, which reaches 83.7% at 3.14 PF-days. Symbolic state supervision raises the 20M model's frame accuracy from 31.1% to 67.3% at the same training-data budget, suggesting that learning representations of state changes can complement scaling.

---


### 147. [Pixel-wise Exposure for Highly Robust In-Vehicle Remote-PPG](https://arxiv.org/abs/2609.36607)

**<font color=#1a73e8>作者：</font>** Jieying Wang, Xinqi Cai, Caifeng Shan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) offers a promising non-contact solution for heart rate monitoring, yet its real-world robustness is fundamentally limited by an inherent hardware limitation: existing camera exposure control paradigms, whether fixed or auto-exposure, impose a uniform exposure time across all pixels within a frame. In high-dynamic-range scenes such as automotive cabins with strong directional sunlight, this spatially invariant exposure constraint inevitably leads to localized facial overexposure or underexposure, irreversibly corrupting the subtle pulsatile signals essential for rPPG at the point of capture, a physical degradation that no downstream algorithm can recover. To overcome this bottleneck, we propose PixExpo (Pixel-wise Exposure), a "temporal-for-spatial" framework that sequentially captures frames under a predefined cyclic exposure schedule and performs non-iterative pixel-wise fusion. At each pixel location, PixExpo selects the observation closest to an rPPG-motivated target intensity. This criterion seeks to reduce local saturation and severe underexposure rather than optimize perceptual appearance. PixExpo requires no sensor modification but assumes programmable frame-level exposure control. We validate the proposed PixExpo framework using our newly introduced MEX-Drive dataset, comprising 48 participants under real-world driving conditions. Experimental results demonstrate that PixExpo outperforms manufacture-default auto-exposure methods, reducing the mean absolute error (MAE) by 7.21 bpm (from 13.94 to 6.73 bpm) and increasing the success rate by 37.29 percentage points (from 25.95% to 63.24%) across challenging driving scenarios.

---


### 148. [Communication-Efficient Agnostic Federated Learning via Faster Convergence and Compression](https://arxiv.org/abs/2609.36610)

**<font color=#1a73e8>作者：</font>** Haomin Bai, Junyan Sun, Sifan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agnostic federated learning (AFL) seeks a model that performs reliably across $m$ heterogeneous workers, but communication remains a bottleneck. We improve communication efficiency by reducing the number of synchronization rounds via faster convergence and the communication cost per round via compression. We first propose AFL-BR, which updates the dual weights over workers using online mirror ascent with KL divergence and blockwise restarts. It achieves an $O((\log m)^{1/4}T^{-1/8})$ stationarity rate after $T$ update rounds, reducing the $m$-dependence of the synchronization rounds required for convergence from polynomial to logarithmic order. Building on AFL-BR, we develop AFL-Com by applying bidirectional compression with error feedback (EF). Instead of compressing local gradients, workers apply EF to their dual-weighted gradients, enabling direct control of the aggregated compression error under time-varying weights. We then establish an $O((\delta^{-1}+(\log m)^{1/4})T^{-1/8})$ stationarity rate for AFL-Com under general $\delta$-approximate compressors and improve the $\delta$-dependence from $\delta^{-1}$ to $\delta^{-1/2}$ for additive-and-idempotent compressors with shared randomness (SR). With suitable compression levels, AFL-Com retains the same convergence rate as AFL-BR at a lower per-round communication cost, yielding reductions in total communication complexity by factors of $(\log m)^{1/4}$ with Top-$k$ and $(\log m)^{1/2}$ with Rand-$k$ and SR. Experiments validate the improved synchronization and communication efficiency of our methods.

---


### 149. [RobotEQ 3.0: Towards Personalized Social Proactive Intelligence in Embodied Agents](https://arxiv.org/abs/2609.36618)

**<font color=#1a73e8>作者：</font>** Shufan Zhang, Xinyi Che, Kuofei Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social Proactive Intelligence (SPI) is an emerging research area, aiming to shift embodied agents from reactive assistance toward proactively understanding human needs and executing socially desirable actions. Prior work has largely centered on the average user. However, human expectations are inherently diverse, and prior work overlooks individual nuances. To bridge this gap, we introduce RobotEQ 3.0, a benchmark for Personalized SPI. (Dataset) We first profile participants via a structured questionnaire covering factors that are correlated with human expectations of embodied agents, such as basic demographics and personality traits. Participants then select their preferred actions from a set of candidates. Unlike prior SPI benchmarks that focus on assessing behavioral appropriateness, our task centers on predicting the actions preferred by a specific user, thereby capturing human subjectivity. The resulting dataset establishes explicit links between individual traits and behavioral preferences. (Solution) We observe substantial inter-annotator variance, confirming that user preferences over actions are highly individualized. This motivates our exploration of Personalized SPI, in which user traits serve as additional inputs to predict individual preferences. Experimental results show that incorporating user traits can aid personalized prediction. This work aims to shift the research paradigm from developing agents suited for the average user to designing systems tailored to specific individuals.

---


### 150. [Neural Structural Reasoner: A Brain-inspired Architecture for Reasoning over Structured Knowledge](https://arxiv.org/abs/2609.36620)

**<font color=#1a73e8>作者：</font>** Zixing Jia, Yuhang Pan, Ni Ji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structural reasoning, the ability to recognize and make inferences over the relational structure between objects and concepts, is a hallmark of human cognition, yet prevailing methods often collapse relational topology into flat embeddings, cannot discover hidden structure and lack interpretability. We introduce Neural Structural Reasoner (NSR), a brain-inspired network that preserves relational structure directly in the connectivity and dynamics of coupled neuronal populations. NSR draws inspiration from three biological mechanisms: multi-layered architecture for encoding hierarchical knowledge, stable representations of entity and concepts, and path integration for input-driven state inference. At query time, NSR parallelizes computation over candidate relational structures and leverages confidence-weighted scores to perform link prediction. Across standard knowledge-graph benchmarks, NSR achieves competitive accuracy without leading on every dataset, and has lower reported training times than several neural baselines. Because reasoning is implemented through sequences of human-readable neuron activations, NSR affords native interpretability by tracking intermediate inference steps. The model further extracts latent relational hierarchies and compositional rules, demonstrating the brain-inspired architecture as an effective, efficient, and highly interpretable substrate for structural reasoning.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
