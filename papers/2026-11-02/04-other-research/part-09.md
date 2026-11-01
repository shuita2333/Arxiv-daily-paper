# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-432**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-432**

---

### 401. [A Unified Benchmark for Aerial-Enhanced Autonomous Driving: The KITScenes Aerial Dataset](https://arxiv.org/abs/2610.40455)

**<font color=#1a73e8>作者：</font>** Daniel Lengerer, Richard Schwarzkopf, Jonas Merkert 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial imagery provides complementary spatial context for autonomous driving by exposing road structure beyond the immediate perception range of onboard sensors. Yet map construction from aerial imagery, aerial-assisted online HD mapping, and cross-view localization are typically studied on separate data and benchmarks. We introduce KITScenes Aerial, an extension of the KITScenes Multimodal dataset that augments synchronized onboard sensor data, vehicle poses, and rich Lanelet2 map annotations with spatially associated aerial imagery and higher-resolution neural representations, providing a common basis for a variety of research tasks. Our mapping evaluation focuses on all 53 KITScenes map classes across different model designs, spatial ranges, and aerial resolutions, while retaining compatibility with the widely used three-class setting. Representative baselines show that aerial context is particularly beneficial for fine-grained and extended-range mapping, more than doubling 53-class mAP at the larger mapping extent. Higher-resolution aerial imagery yields a further 4.3 mAP (+24 %) improvement, with gains extending to challenging map elements such as traffic lights. We additionally evaluate cross-view localization under geographically disjoint conditions, where an adapted fine-grained feature-matching baseline achieves a mean translation error of 5.13 m. KITScenes Aerial thus enables unified study of aerial and ground-level information across complementary mapping and localization tasks. Project page: this https URL

---


### 402. [InfantNet: A Large Scale Dataset for Infant Body Pose and Shape Estimation](https://arxiv.org/abs/2610.40467)

**<font color=#1a73e8>作者：</font>** Zhipeng Hui, Jiahao Wang, Xun Dong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infant pose and shape estimation is essential for applications in childcare, developmental monitoring, and medical diagnosis. However, existing methods and datasets are largely designed for adults, and direct transfer to infants fails due to substantial differences in body proportions, articulation limits, and frequent self-occlusion. To address this gap, we introduce InfantNet, the largest real-image infant dataset to date, comprising 108,902 RGB images of infants aged 6-18 months. Each image is annotated with 2D keypoints, and a curated subset of 11,642 images additionally includes 3D pose and shape annotations with full SMIL parameters, verified through multi-view rendering and reprojection-error filtering. We use an iterative annotation pipeline to ensure high fidelity across both 2D and 3D labels. InfantNet establishes a large-scale, comprehensive benchmark for infant 2D keypoint detection and 3D pose-and-shape recovery. Baseline experiments demonstrate that state-of-the-art adult pose estimators do not generalize well to infants, whereas fine-tuning on InfantNet yields a consistent improvement. The gains are even more pronounced for 3D pose and shape estimation, where SMIL-based estimation demonstrates robust performance with accuracy comparable to results reported for SMPL-based models. By releasing the InfantNet dataset and benchmark, we provide a vital resource for advancing infant pose analysis and related healthcare applications.

---


### 403. [Rural Readiness: Domain Generalization with Adversarially Chosen Domains](https://arxiv.org/abs/2610.40468)

**<font color=#1a73e8>作者：</font>** Cynthia Dwork, Andisheh Ghasemi, Lunjia Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models trained at well-resourced data-rich institutions often fail when deployed in new populations. Motivated by the goal of building clinical diagnosis and decision-making algorithms for data-scarce rural populations using the general knowledge learned from data-rich hospitals, we formulate the fundamental question of \emph{domain generalization with adversarially chosen domains}, which asks a learner to perform on any unseen target domain nearly as well as the worst hypothesis consistent with the evidence from the observed source domains.
Assuming only that the hypothesis class contains a "universal" predictor with small error on all $k$ source domains, we characterize the sample complexity of this objective up to logarithmic factors. Letting $d$ denote the VC dimension of the hypothesis class, we find, somewhat surprisingly, that the sample complexity reduces significantly from $\Omega(dk)$ to $O(d)$ under a small relaxation of the learning goal in which, roughly speaking, we allow the learned model to compete with hypotheses that perform well on 99% instead of 100% of the source domains. By applying this insight to the meta-distributional setting, in which source domains are selected according to a distribution on distributions, we obtain a corresponding improvement over known sample complexity upper bounds. We also study the effect of data access to the target domain and show that a small labeled sample from the target domain does not improve the worst-case sample complexity on the source domains.

---


### 404. [Nonlinear Dynamical Systems as Scalable and Efficient Physical Neural Networks](https://arxiv.org/abs/2610.40471)

**<font color=#1a73e8>作者：</font>** Tyler King, Magnus Saebo, Jeremie Laydevant 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth in the size of state-of-the-art machine-learning (ML) models has led to increasing compute demands, spurring the development of energy-efficient hardware accelerators. Physical systems trained to perform ML inference, known as physical neural networks, have been proposed as accelerators in part because of their potential to be highly energy efficient. However, the ML inference accuracies reported in most investigations of physical neural networks have been substantially below the state of the art for conventional digital neural networks. In this work, we show in simulation studies that by applying modern ML training practices, including model compression, various candidate physical neural networks based on nonlinear dynamical systems can achieve accuracies as high as 99.2% on MNIST handwritten-digit recognition. We also show for one dynamical system that using it as the core building block of a parameter-efficient ML architecture inspired by MLP-Mixers enables accuracies of up to 86.4% on CIFAR-10 image classification (92.2% with pretraining and knowledge distillation), compared with 64% for the same system without the mixer architecture. The mixer approach achieved its accuracy while using $>5\times$ fewer trainable parameters than the baseline. Finally, we present back-of-the-envelope estimates for inference energy efficiency and speed when using an example physical dynamical system, suggesting that orders of magnitude improvements may be possible over digital-electronic neural networks.

---


### 405. [Accurate MRI-free PET Quantification and Reliability Assessment via CT-to-MRI Synthesis and Conformal Prediction](https://arxiv.org/abs/2610.40478)

**<font color=#1a73e8>作者：</font>** Jungwoo Seo, Seung Yun Choi, Kun Ho Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standardized uptake value ratio (SUVR) quantification of amyloid PET commonly relies on a subject-specific T1-weighted MRI, yet a usable MRI is not always available. We therefore combined CT-to-MRI synthesis with conformal prediction for MRI-free PET quantification with reliability assessment. A slice-consistent Brownian Bridge Diffusion Model was strengthened with multi-dataset training and data-source conditioning to enrich the anatomical prior learned from MRI, and with expanded multi-slice CT context to exploit the through-plane continuity of subject-specific anatomy in CT. Synthetic MRI was used for FreeSurfer-based anatomical parcellation and PET quantification, while deep-ensemble uncertainty was calibrated with conformal prediction to estimate a plausible range for the corresponding real MRI-based SUVR. On $^{11}$C-PiB PET from OASIS-3, the proposed method achieved the highest synthesis and parcellation fidelity among the compared methods. Mean cortical SUVR from the proposed synthetic MRI agreed closely with the real MRI-based reference (MAE $0.016 \pm 0.015$, Pearson $r = 0.9987$) and yielded the same amyloid-positivity classification as the real MRI in all 87 test subjects at the prespecified cut-off. Conformal prediction achieved empirical coverage close to the prespecified levels, and at 90% target coverage, 85 of 87 subjects had prediction intervals that supported an unambiguous amyloid-positivity decision. Zero-shot evaluation on an independent external cohort showed that the proposed CT-to-MRI model could support PET quantification without retraining, although conformal calibration required target-cohort recalibration to recover the intended coverage. These findings support CT-to-MRI-based MRI-free PET quantification as a promising approach for providing accurate SUVR measurements and an explicit assessment of their reliability.

---


### 406. [AVPS-360: A Spatial Audio-Visual Benchmark for Instance Segmentation and Tracking of Sound-Producing Persons](https://arxiv.org/abs/2610.40480)

**<font color=#1a73e8>作者：</font>** Yifu Sun, Parthasaarathy Sudarsanam, Tuomas Virtanen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual instance segmentation (AVIS) segments and tracks individual sound-producing objects in videos. Existing benchmarks predominantly use monaural audio, which lacks inter-channel cues for spatially distinguishing concurrent sound sources. We introduce AVPS-360 (Audio-Visual Person Segmentation 360), a spatial audio-visual benchmark bridging AVIS and sound event localisation and detection (SELD). Built upon STARSS23, it pairs first-order Ambisonics audio with synchronised 360° video across 230 recordings totalling 10.5 hours. Recordings average 164.0 seconds. The dataset captures intermittent sound production in real-world interactions dominated by speech, alongside laughter, clapping, and footsteps. It provides 31,678 manually reviewed instance masks linked to source identities and sound-event labels. We also present a baseline that integrates spatial audio with visual features for frame-level segmentation and identity association across frames. Experiments on AVPS-360 show that existing AVIS methods struggle with detection and identity association in long recordings with intermittent sound production, while our baseline substantially improves performance in both aspects.

---


### 407. [FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor Knowledge](https://arxiv.org/abs/2610.40482)

**<font color=#1a73e8>作者：</font>** Yunbai Zhang, Yunyi Gao, Han-Tai Shiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial AI workflows that reuse investor knowledge need persistent memory that integrates observations across sources and periods without losing identity or provenance. In a knowledge graph, recurring observations may use different surface forms, fragmenting relationship histories and preventing evidence from accumulating. We introduce Fusion and Identity Registry for Memory Evolution (FIRME), a registry-anchored memory graph that reconciles incoming observations to persistent canonical relationships and retains their source, time, and context. Within periods, rule-based fusion links investor-call discussions to portfolio cash-flow signals, directly or through a fixed product-topic ontology. Across periods, canonical identities and persistent aliases direct recurring observations to the same relationship history; deterministic updates summarize reinforcement, inactivity, and reactivation. We evaluate FIRME on proprietary investor-call and cash-flow records and on S&P 500 earnings-call transcripts. Compared with a historical registry that retains canonical identities and semantic fallback but omits alias memory, FIRME increases final-period Correct Match Rate by 7.8-12.1 percentage points across four dataset-backend settings under a fixed-judge and fallback-review protocol. A blinded human audit of 200 incoming observations per setting finds Correct Match Rate gains of 9.0-16.5 points and reattachment-recall gains of 22.5-29.0 points, with higher observed merge precision in all four samples. A separate audit finds valid evidence paths for 293 of 300 outputs from full within-period fusion in the investor-call setting. Extraction-faithfulness and round-trip diagnostics assess source grounding and preservation of extractor-derived graph content.

---


### 408. [The Precision Wall: An Optimizer-Dependent Boundary for Optimization under Power-Law Measurement Spectra](https://arxiv.org/abs/2610.40485)

**<font color=#1a73e8>作者：</font>** Lngel Kyo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In low-rank matrix sensing of a rank-$D$ factor $U^\ast \in \mathbb{R}^{V \times D}$, replacing isotropic Gaussian designs with power-law measurement covariance $\Sigma = \mathrm{diag}(j^{-s})_{j=1}^V$ leaves the Burer--Monteiro landscape free of spurious local minima, yet division-normalised first-order optimizers stall above a critical exponent $s^\ast$. We trace this failure to a numerical precision wall. At the ground truth, the smallest non-gauge expected Hessian eigenvalue scales at leading order as $V^{-(s+1)}D^{-s}$. When this curvature drops below the effective denominator floor $\epsilon_O$ of optimizer $O$, normalisation noise overwhelms rare-direction gradients, yielding the leading-order boundary $s^\ast_O(V, D) = [\log(1/\epsilon_O) - \log V]/\log(VD) + \delta_O$, where $\delta_O$ is a metric-dependent detection lag. With $\delta_{\mathrm{Adam}}$ calibrated on four configurations and frozen, this formula predicts Adam's onset within $0.45$ across all 16 cells of a held-out grid ($V \in \{64,128,256,512\} \times D \in \{4,8,16,32\}$), separates fixed-$VD$ pairs, and distinguishes denominator-precision walls from conditioning and sign-quantisation walls. The approximation fails at $D = 2$, reflects a finite-$D$ spectral crossover, and saturates below $\varepsilon_0 = 10^{-8}$ at a dynamical floor.

---


### 409. [MetaRefine: Score Refinement with Multi-Level Features for Image Assessment](https://arxiv.org/abs/2610.40487)

**<font color=#1a73e8>作者：</font>** Chuanzhi Xu, Chengkun Yue, Haolan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image's original dimensions, aspect ratio, and composition provide important cues that can affect its technical and aesthetic quality. Image assessment methods use resizing, cropping, padding, or patch sampling to accommodate different input sizes. However, these operations can alter or obscure original geometric and compositional cues. Existing assessment models also encode rich multi-level visual evidence that can be further extracted and exploited to improve existing models. This motivates us to combine visual evidence with original-image geometry for score refinement without changing the original scoring pipelines. In this paper, we introduce MetaRefine, a metadata-aware score refinement architecture whose lightweight residual heads predict score corrections from geometry, multi-level visual features, and the frozen model's original score. Across 100 configurations on 21 datasets, MetaRefine improves PLCC in 88 configurations and SRCC in 85, with average relative gains of 7.55% and 7.10%, respectively. It reduces MAE in 90 configurations and RMSE in 89, with average relative reductions of 23.27% and 21.93%, respectively. The median parameter overhead is only 1.11%. MetaRefine can further improve state-of-the-art (SOTA) assessment models on multiple benchmarks.

---


### 410. [rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment](https://arxiv.org/abs/2610.40488)

**<font color=#1a73e8>作者：</font>** Art Kanke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a research agent alone or as a team, proposes minimum viable experiments (MVEs), forecasts whether each will pass a threshold it sets and ranks them. A separate executor then attempts every MVE, including those ranked last, and three model auditors judge the results. Of 415 MVEs, 194 are judged sound, valuable and new, but fewer than half of these (73) are also judged beyond the seed paper and non obvious. The agents' first choices match the auditors' most valued experiment more often than a random pick, but are not shown to improve on choosing the experiment written first. Their forecasts beat a base rate but are not measurably more accurate than those of a fresh instance of the same model given only the paper and registrations. Teams cost more without a clear overall improvement in proposal quality. The agents produce many worthwhile experiments, but the evidence that their rankings improve the choice of which to run remains limited. The evaluation harness and a dataset of all 415 MVEs, with their forecasts and audited outcomes, are available at this https URL.

---


### 411. [LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495)

**<font color=#1a73e8>作者：</font>** Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LucidLyra, a framework that makes generatively reconstructed 3D scenes directly queryable for semantics and instances in a feed-forward manner from video latents. While generative 3D reconstruction can synthesize virtual environments from a single image, downstream applications in robotics and physical AI require not only visual realism but also access to scene semantics and object identities. Existing 3D understanding approaches, however, require captured multi-view scenes, have limited generalization capabilities, or rely on expensive per-scene processing and optimization. To bridge this gap, our method distills complementary knowledge from a camera-controlled video diffusion model and frozen 2D vision foundation models into a unified model to jointly infer 3D Gaussians encoding geometry, appearance, open-vocabulary semantics, and class-agnostic instance cues. The resulting scenes support novel-view rendering, open-vocabulary segmentation, and object grouping without per-scene optimization, while training requires neither manual 3D annotations nor captured multi-view data. Our method outperforms baselines combining state-of-the-art 3DGS segmentation approaches with generative 3D scene reconstruction on curated synthetic and real-image-conditioned benchmarks, while preserving reconstruction quality. Furthermore, our latent formulation naturally extends to monocular video, reconstructing structured dynamic 3D scenes across time. By turning renderable but unstructured outputs into queryable 3D worlds, LucidLyra enables downstream applications including 3D scene editing, 3D asset mining, and robotic simulation.

---


### 412. [Numerical Integration on Bounded Domains via Learned Reflected Diffusions](https://arxiv.org/abs/2610.40499)

**<font color=#1a73e8>作者：</font>** Kirill Korolev, Artur Goldman, Timofei Gritsaev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study high-dimensional integration on bounded convex domains. Given a non-negative integrand $r$, the goal is to estimate $Z=\int_{D}r(x)\,\mathrm dx$ on $D\subset\mathbb R^d$. Standard Quasi-Monte Carlo does not adapt its evaluation points to the integrand, while effective importance sampling requires a proposal that captures its concentration. Learned diffusion samplers can supply such a proposal, but existing methods are formulated on $\mathbb R^d$ and do not respect the domain constraint $x\in D$. We instead build the proposal from reflected dynamics that stay in $D$ by construction. A reflected diffusion progressively transforms the target distribution toward the uniform distribution on $D$, and a neural score model is trained to reverse this process. A change-of-measure formula for reflected diffusions yields a training objective without additional boundary terms and an unbiased importance-sampling estimator of $Z$. For non-smooth integrands, where reparameterization gradients may be undefined or uninformative, we derive a REINFORCE estimator of the training gradient using Gaussian proposal densities before reflection, without evaluating reflected transition densities or differentiating $r$. We evaluate on numerous synthetic targets and real-world problems, demonstrating strong performance of the proposed method, as well as favorable scaling with the dimension of the problem and the number of points used for the Monte Carlo estimate.

---


### 413. [RecHash: Segmented Hash-Entangled Chains for Stateful Sequential Authentication](https://arxiv.org/abs/2610.40507)

**<font color=#1a73e8>作者：</font>** Luis Adrián Lizama-Pérez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> RecHash is a stateful sequential authentication construction based on paired hash-chain openings and an authenticated record history. It develops the decreasing position relation of the 2019 hash-entangled construction, whose exact integer normalization yields a two-coordinate constant-sum antichain. Direct proportional reuse is constrained by integer capacity and multiplicative contraction. The main construction instead assigns each record to a predetermined chain segment, with complementary positions encoding each digest block. All digests fit every scheduled slot, independently of preceding messages. For an $\ell$-bit digest distributed over $k$ equal-length chain pairs, balanced allocation gives $\lfloor L/(2^{\lceil\ell/k\rceil}+1)\rfloor$ slots. A 256-bit digest, 32 pairs, and length 65535 provide 254 application records followed by a renewal certificate, with 2048 bytes of openings per record for 256-bit chain outputs. We give a complete segmented state transition, a worked trace, exact allocation and resource results, and a renewal-free security-composition theorem conditional on authenticated history and an adaptive one-step guarantee. The analysis relates the construction to constant-sum encodings and standardized hash-based signatures; a concrete post-quantum reduction and security across renewal remain open.

---


### 414. [CrossWeave: Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment](https://arxiv.org/abs/2610.40525)

**<font color=#1a73e8>作者：</font>** Aadith Warrier, Gnana Prakash Punnavajhala, Siddharth Tourani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal scene and instance retrieval aims to retrieve a corresponding 3D environment or object given query 2D images, serving as a foundational mechanism for spatial reasoning in robotics and AR/VR. Existing methods achieve this by learning alignment only at the level of whole scenes or objects, which provides no supervision for the fine-grained local structure within them. In this work, we show that supervision on a set of sparse 2D-3D correspondences, without scene- or instance-level contrastive objectives, is sufficient to train a single model for both scene- and instance-level retrieval. Specifically, we propose $\textbf{CrossWeave}$, a novel framework for cross-modal retrieval that learns sparse patch-point alignment, which alone outperforms existing methods. An optimal transport-based aggregator over the aligned features gives further gains by clustering structurally redundant regions, freeing descriptor capacity for semantically distinct local features. CrossWeave achieves state-of-the-art performance on both scene- and instance-level retrieval on ScanNet and 3RScan with a $\textit{single model}$, whereas existing methods require separate models for each task. Our results suggest that whole-scene encoding is unnecessary for cross-modal retrieval and that sparse local correspondence supervision is a more effective and flexible alternative.

---


### 415. [Efficient Scalable Oversight via Rewinding](https://arxiv.org/abs/2610.40535)

**<font color=#1a73e8>作者：</font>** Ziyi Guan, Yael Tauman Kalai, Ron Rothblum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scalable oversight asks how a weak verifier can check the outputs of computations performed by more powerful AI systems. One proposed approach uses relativizing interactive proofs, in which a weak verifier checks the output of a complex oracle-aided computation by interacting with one or more powerful provers. A prominent example is debate, which is highly efficient but assumes that one of two powerful AI models, or provers, is truthful. For certain classes of oracle-aided computations, this assumption can be removed, but at substantially greater computational cost.
In this work, we introduce \emph{rewindable interactive proofs} (RIPs), a new model of relativizing interactive proofs for scalable oversight. In an RIP, the verifier may rewind the prover to an earlier state of the interaction and continue from there. This is possible when the prover is an AI model, since the verifier can save a snapshot of the model's state and later restore it. We construct a relativizing RIP for computations whose outputs are robust to changing a small fraction of oracle answers. Our construction is more efficient than prior relativizing proofs that do not assume a truthful prover, and it uses no cryptography.
In our construction the honest prover runs in time linear in that of the original computation, and the verifier, after a one-time preprocessing step, runs in time nearly linear in the input length (which can be much smaller than the computation itself). We implement our protocol, report a preliminary MNIST experiment, and show that an RIP can be faster than a state-of-the-art deployed proof system.
RIPs may be of independent interest. Rewinding is possible whenever the verifier controls the prover's machine, for example when the prover runs on trusted hardware or in a virtual machine whose state can be checkpointed.

---


### 416. [Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers](https://arxiv.org/abs/2610.40544)

**<font color=#1a73e8>作者：</font>** Ibrahim Salifu, Muhaisin Tiyumba Nantogmah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service (SMS) and Unstructured Supplementary Service Data (USSD), where fraudsters impersonate network operators, agents, relatives, or regulators to obtain personal identification numbers (PINs), identity data, or funds. We present a supervised machine-learning pipeline for classifying scam and legitimate Ghanaian MoMo SMS messages using a labelled corpus of 220 messages across 18 scam and legitimate subcategories. Domain-specific normalisation of currency amounts, phone numbers, and USSD codes preceded TF-IDF vectorisation of unigrams and bigrams. Using stratified five-fold cross-validation and a 20% held-out test set, we trained and evaluated Multinomial Naive Bayes, linear support vector machine (SVM), and Random Forest classifiers using accuracy, precision, recall, F1-score, Matthews correlation coefficient (MCC), and area under the receiver operating characteristic curve (AUC-ROC). Held-out accuracy, F1, and AUC were 1.00 for Naive Bayes and linear SVM; cross-validated accuracy averaged 96.6% (+/-3.3), 94.9% (+/-4.6), and 92.0% (+/-4.2). Discriminative n-grams reflected imperative urgency ("send," "claim," "please send") and PIN solicitation ("PIN," "pincode"); legitimate messages featured confirmatory and cautionary language ("balance," "successful," "do not share"). Findings are contextualised in Sub-Saharan African SMS fraud detection, small template-based corpus ceiling effects, and a pathway toward larger naturalistic multilingual corpora. Interpretable classical classifiers achieve high accuracy on structured MoMo scam text and suit carrier- or handset-level filtering in low-resource, on-device settings.

---


### 417. [Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents](https://arxiv.org/abs/2610.40545)

**<font color=#1a73e8>作者：</font>** Daniel Strauß, Zhenshan Bing, Alois Knoll  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context models repeatedly solve closely related retrieval problems. Attention or global retrieval can retain large stores, but each forward pass again searches for what matters. Recurrent compression avoids this search only by deciding earlier what information to preserve. Neither mechanism directly exploits that useful memories at neighbouring retrieval steps may substantially overlap. We propose an alternative in which retrieval is a persistent local traversal through an address space. We separate a memory's content from its address. Utility is defined by the information revealed by retrieving the content, while geometry determines only how cheaply that information can be reached. This leads to a cost-regularised indexing objective that preserves information value inside local neighbourhoods while charging for every memory made locally accessible. Its marginal-value form gives both attractive and exclusion pressures. Thus, complementary memories should be co-retrievable when the additional value exceeds retrieval cost, whereas redundant memories should not occupy the same retrieval set solely because they are individually useful. As a proof of principle, we test only the simplest fixed-geometry instance on MiniGrid Memory. A persistent local traversal head reaches $0.95$ mean return after $0.59$M training steps with a five-token context, compared with $0.94$M for Gaussian absolute addressing and more than $2$M for categorical absolute addressing. The experiment does not test learned geometry or repeated retrieval. Instead, it motivates the hypothesis that stateful retrieval may be easier to learn than stateless. To test the full proposed method further experimentation is necessary.

---


### 418. [Power Adjusting Games Under Block-Dependent Pool Payout Schemes](https://arxiv.org/abs/2610.40558)

**<font color=#1a73e8>作者：</font>** Mustafa Doger, Sennur Ulukus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced power adjusting block withholding attacks such as PAW and T-PAW have been analyzed so far under a global-reset version of the proportional scheme (GRP), which is rarely used in practice. In this paper, we analyze T-PAW, which contains FAW and PAW as special cases, under the block-dependent payout schemes deployed in practice: Pay-Per-Last-N-Shares (PPLNS), round-based Proportional (PROP) and exponential-decay (EXP). We derive the revenue ratios analytically, by renewal arguments for PPLNS and through the stationary carry process of an open round for PROP and EXP. We further introduce Power Adjusting Hopping (PAH), where an adversary of any size adjusts its power allocation towards the pool according to the blockwork age of the round without withholding any block, and derive its revenue ratios under PROP and EXP. We show that GRP misestimates the T-PAW gain in a scheme-dependent direction: it overstates the gain under PROP up to an order of magnitude and understates it under EXP for the original slush decay rate. PROP is highly vulnerable to PAH, while EXP faces a trade-off: a slow decay invites PAH and a fast decay invites T-PAW. PPLNS is the least vulnerable scheme: it is immune to PAH and it mitigates, but does not eliminate, T-PAW. All analytical results are verified by Monte Carlo simulations.

---


### 419. [FARMS: A Verifiable Foundation for Automated Computational Science](https://arxiv.org/abs/2610.40560)

**<font color=#1a73e8>作者：</font>** Di Wu, Ling Liang, Haizhao Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated computational science could accelerate discovery by selecting, adapting and developing numerical methods. This prospect requires mathematical knowledge that AI systems can interpret and reuse with explicit guarantees. Here we present FARMS, a faithful and efficient foundation that transforms computational mathematics into AI-ready computing knowledge. FARMS connects formal statements to source context, algorithmic meaning and quantitative guarantees through source preparation, reusable representations and semantic review. Across 171 targets in randomized numerical linear algebra and numerical partial differential equations, 157 were accepted by the pipeline, with mean estimated costs of US \$0.85-2.29 per target across sources. Lean-checked implications from explicit source premises connect selected statements to computational skills, illustrated by a heat-flow solve and wave-response compression. FARMS therefore supports an affordable, reusable knowledge foundation for trustworthy automated computational science.

---


### 420. [PIVOT: Progressive Intervention via Online Teacher Correction](https://arxiv.org/abs/2610.40576)

**<font color=#1a73e8>作者：</font>** Zhihao Yang, Boyuan Zheng, Puhui Tan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) is limited by sparse outcome-level feedback on hard reasoning tasks: when all rollouts in a group fail, rewards provide no learning signal. Stronger teachers can provide additional guidance, but this raises a central question: how can such signals be incorporated into RLVR to support successful rollouts while remaining learnable for the student? We distinguish two complementary mechanisms: trajectory-level intervention, which improves access to reward-bearing trajectories, and token-level supervision, which provides dense targets to guide student learning. Our controlled experiments show that either mechanism alone can remain insufficient, motivating their combination. We therefore introduce PIVOT, which inserts teacher-generated corrections into student rollouts and applies token-level KL supervision to these segments alongside the RLVR objective. Beyond their combination, we systematically analyze where to intervene and how to supervise, yielding a recipe for effective guidance. Across hard logic games and mathematical reasoning benchmarks, PIVOT consistently outperforms existing methods, nearly doubling mean avg@8 on logic games from 19.5% for the best-performing baseline to 35.6%.

---


### 421. [Beyond Ground Truth: A Heuristic Unsupervised Quality Assurance Engine for Diagnosing Calibrational Blindness in Dental Segmentation](https://arxiv.org/abs/2610.40587)

**<font color=#1a73e8>作者：</font>** Fatematuj Johura Mim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world clinical settings, dental X-ray segmentation using deep learning methods suffers from reliability issues. Even when the segmentation quality is bad, deep learning models show high confidence in their predictions (calibrational blindness). Moreover, in real use, doctors do not have ground-truth masks to check their accuracy. To address this problem, we introduce a simple quality-checking engine called HUS-QA with three stages. We train it on the PRAD (Periapical Dental X-ray) dataset to build our SimCLR self-supervised ResNet-18 U-Net model, which generates the segmentation mask and then evaluates its quality. Our HUS-QA checks the segmentation mask quality without a ground-truth mask. Prediction confidence, edge sharpness, shape connectivity, and area-size penalty are the simple indicators considered in this research. Results show that standard confidence methods fail (r = -0.1394, p = 1.7864e-3, ROC AUC = 0.4275). By contrast, our HUS-QA shows a positive correlation with actual Dice scores (r = 0.4647, p = 3.7510e-28) and achieves a strong ROC-AUC of 0.8405. Therefore, HUS-QA serves as a practical tool for clinical quality control.

---


### 422. [HairDeck: Animation-Ready Stylized Hair Cards from a Single Image](https://arxiv.org/abs/2610.40599)

**<font color=#1a73e8>作者：</font>** Yuze He, Yixiang Wei, Wang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The hair of stylized characters in games and avatars is built from hair cards: artist-placed ribbons whose geometry is the visible hair, animated by spring bones. Existing image-based methods produce realistic hair or a single fused mesh, while CHARM, the only generator of stylized hair cards, decodes a hairstyle autoregressively as a long sequence of control points. Observing that a card hairstyle is an unordered set of artist-defined primitives, we propose HairDeck, which generates it as one: each card is a single token, and a set diffusion transformer denoises all cards together. From a single image, HairDeck generates the cards and the spring-bone chains that drive them, yielding an animatable asset that exports to ready-to-use downstream formats. On CHARM's own test set, it lowers Chamfer distance by 44% and card-orientation error by more than half while running 33 times faster, and from single images it outperforms CHARM, image-to-3D pipelines and strand-based methods. Project page: this https URL

---


### 423. [Fight World Model: Customizable Combat through Visual Interaction Proxies](https://arxiv.org/abs/2610.40607)

**<font color=#1a73e8>作者：</font>** Jiahua Li, Zixu John, Tom Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A playable, programmable game world must maintain persistent state, enforce executable rules, and support extensible gameplay mechanics. Existing video world models can generate plausible combat, yet struggle to keep hit reactions and health updates consistent with game rules. We introduce Fight World Model (FWM), which separates rule-governed combat execution from video rendering. An executable engine maintains state and resolves interactions. A deterministic compiler encodes these outcomes and attempted actions in a spatially and temporally aligned interaction proxy. The proxy aligns action and skill windows, brief hit reactions, and persistent health by fighter identity and timing. These cues can be controlled separately to render interactions under modified rules. Identity-bound references preserve character appearance across side switches. We train FWM on FightWorld Corpus, spanning 52 skill effects, 187 character-appearance variants, and 15 arenas. Without retraining the renderer, FWM supports damage scaling, limited-hit immunity, lifesteal, and multi-stage skill mechanisms beyond the native game. It also allows character and arena customization. Experiments demonstrate the effectiveness of FWM, which outperforms existing game world models in action fidelity, hit reactions, health-state consistency, and character appearance preservation. Our project is available at this https URL.

---


### 424. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614)

**<font color=#1a73e8>作者：</font>** Jinhyeok Choi, JoungBin Lee, Jongmin Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches rely on either temporal context or explicit 3D memory, both of which scale poorly because memory grows with the length of the generated stream. Moreover, explicit 3D memories condition latent video generators by re-encoding RGB renderings, which precludes real-time generation. In this paper, we introduce a Latent 3D Gaussian Memory (L3G) that combines the efficiency of feed-forward reconstruction with a compact, rapidly renderable scene representation. Building on this memory, we propose L3G-World, in which a memory updater and a video diffusion transformer (DiT) alternate autoregressively to generate spatially consistent worlds. The memory updater spawns Gaussians in newly observed regions and refines existing ones, so that the memory grows with scene extent rather than stream length. Each Gaussian further stores a VAE latent feature, allowing the memory to be rendered directly into the DiT's latent space without VAE re-encoding. Experiments show that L3G-World achieves state-of-the-art generation quality and long-horizon spatial consistency, with up to $38.6\times$ fewer 3D primitives, $3.2\times$ faster memory updates, and $359\times$ faster memory rendering relative to the most efficient prior 3D-memory baseline for each metric, enabling real-time world generation at 9 FPS.

---


### 425. [Difficulty Calibration Across Time for Membership Inference in Diffusion Models](https://arxiv.org/abs/2610.40616)

**<font color=#1a73e8>作者：</font>** Michael Joseph, Yedid Hoshen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern diffusion models are trained on massive datasets that often include copyrighted or private images. Membership inference attacks (MIAs) address this by testing whether a given image was in a model's training set. The standard approach scores an image by its reconstruction loss and flags low-loss images as members. This often fails because some images are simply easier to reconstruct than others, so a simple unseen image can score a lower loss than a complex training image. Difficulty calibration separates memorization from how difficult an image is to begin with. We show how to calibrate along two axes of time: training time and diffusion time. First, across training time, we introduce Reference-Model Calibration (RMC), which compares a fine-tuned model's loss against an earlier checkpoint. This cleanly isolates newly memorized data and gives near-perfect auditing, even without text captions. Since earlier checkpoints are not always available, we next present Temporal Self-Calibration (TSC), which calibrates across diffusion time using only a single model. Our key observation is that an image's difficulty persists across noise levels, whereas memorization is localized in time. By comparing the loss at a target timestep against neighboring timesteps from the same model, TSC attenuates image difficulty using the model's own trajectory. Empirically, our methods beat the state of the art by a wide margin, and unlike most existing attacks, generalize across different model parameterizations such as $x$-, $v$-, and $\epsilon$-prediction models. Code is available at this https URL.

---


### 426. [An ODE-based Sampler for Discrete Diffusion Models](https://arxiv.org/abs/2610.40618)

**<font color=#1a73e8>作者：</font>** Samson Gourevitch, Yazid Janati, Eric Moulines 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The marginals of a continuous diffusion model can be reproduced by a deterministic ordinary differential equation (ODE), known as the probability flow ODE, which provides a foundation for accelerated sampling and consistency distillation. In this paper we address the question whether an analogous formulation exists for discrete diffusion models and answer it affirmatively by introducing exponential residual flows (ERFs). Our framework augments the discrete state with a continuous residual variable for each token and position. These residuals evolve deterministically according to piecewise-defined ODEs whose vector fields depend on the current discrete state and the forward and backward rate matrices of the prescribed diffusion model. The discrete state changes whenever a residual reaches zero. We prove that this construction preserves the marginals of the original diffusion. We derive a practical discretization of our sampler and specialize it to masked and uniform diffusion. The deterministic trajectories of ERFs support consistency distillation and yield empirical improvements over previous approaches across a variety of benchmarks including code and text generation tasks.

---


### 427. [world2vec: Mechanistic world models through latent dynamics learning](https://arxiv.org/abs/2610.40637)

**<font color=#1a73e8>作者：</font>** Tobias Schmidt, Rodrigo Gonzalez Laiz, Krisztián Szuppinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. Here, we introduce world2vec to learn mechanistic world models without reward information directly from observations and actions. World2vec learns latent dynamics that faithfully reproduce the true system over long prediction horizons, with at least one order of magnitude fewer parameters than DreamerV3, TD-MPC2 and LeWM. This enables state of the art performance in controlling continuous environments from pixels and accurate system identification across a benchmark of 71 attractors, demonstrating how world models are amenable to scientific discovery.

---


### 428. [SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization](https://arxiv.org/abs/2610.40640)

**<font color=#1a73e8>作者：</font>** Derong Jin, Xiyi Chen, Ming C. Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce Video-to-4DAVScene, a new task that turns a video into an explorable, time-varying 4D audio-visual scene, and present the SonoWorld4D framework for this task. Given a monocular video, our method generates a 360 static background, reconstructs explicit motion trajectories of dynamic, sound-emitting foreground objects, and synthesizes a physically-grounded sound field consistent across multiple sources through dual-space audio diffusion synchronization. The resulting 4D scene supports real-time novel-view visual and spatial audio rendering. Evaluation on real-world dynamic scenes and a user study demonstrates SonoWorld4D generates 4D audio-visual scenes with perceptually realistic, physically grounded spatial audio consistent with scene geometry and visual content.

---


### 429. [Luggage re-identification: A study of strategies towards a real-world application](https://arxiv.org/abs/2610.40643)

**<font color=#1a73e8>作者：</font>** Quentin Dhôte, Romaric Audigier  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (lost luggage recovery). It enables the association of observations of the same luggage across disjoint camera views in complex environments such as airports, train stations and border crossing. While existing approaches primarily focus on appearance-based cropped image matching under relatively clean conditions, real-world scenarios are characterized by frequent occlusions, cluttered background and crowded scenes which significantly degrade performance. Yet, strategies leveraging the complementarity of multiple shots and views from different video streams is overlooked. In this paper, we study strategies for an end-to-end pipeline that operates from multiple video streams to detect and re-identify luggage. We evaluate different variants on a benchmark dataset acquired in real-world environments to address the questions of selecting and merging different views and shots of the same luggage as well as training on different environment datasets for an overall ReID performance improvement in practical applications.

---


### 430. [Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers](https://arxiv.org/abs/2610.40647)

**<font color=#1a73e8>作者：</font>** Jiongfan Yang, Weichen Fan, Haiwen Diao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a pixel-space rectified-flow Transformer that decouples output detail from the length of the global attention sequence. SpecSlot expands each spatial anchor into multiple slots, each assigned a disjoint band of DCT coefficients; this separates anchor density from spectral subdivision. Only the lowest-frequency slot from each anchor participates in global attention, while all slots interact locally. This allows the model to increase spectral detail without enlarging the global sequence. A spatial head further adds a local correction to the spectral prediction, while the generative state, target, and loss remain in pixel space. On ImageNet-256, SpecSlot achieves a comparable final FID to a FLOPs-matched JiT control while converging faster. On ImageNet-512, it improves FID by 2.84 over the control with 3.9% fewer FLOPs, and comes within only 0.69 FID of JiT-B/16 at 38.2% lower cost. On text-to-image generation, SpecSlot surpasses JiT-B/8 on DPG-Bench by 1.06 at 40.6% lower forward cost.

---


### 431. [Micro-Edits: Computational Support for Fine-Scale Edits in Film](https://arxiv.org/abs/2610.40653)

**<font color=#1a73e8>作者：</font>** Nhan Tran, Hijung Valentina Shin, Abe Davis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In film editing, every frame matters. While macro, content-level edits shape the high-level narrative of a film, small local edits often control timing and direct visual attention. For example, editors can adjust the precise timing of clips to control the length of a meaningful silence, or cut to shots that highlight a specific character's reactions to important moments. These small, detailed edits are slow and tedious to make in standard editing tools because users have to map high-level narrative goals to low-level frame-by-frame adjustments. At the same time, these fine-scale adjustments, which we call micro-edits, can be nuanced and expressive, with different choices serving different creative goals. In this work, we start by conducting a formative study with professional editors to understand the structure of micro-edits and how they are used. We then derive a mathematical formalization for this structure to develop tools that leverage AI and optimization to make exploring micro-edits simpler and more efficient for users. Finally, we validate our tools in multiple user studies and a wide range of video examples.

---


### 432. [Propose-Filter-Release: Scaling Noise to Typical Sensitivity via Private Filtering](https://arxiv.org/abs/2610.40654)

**<font color=#1a73e8>作者：</font>** Moshe Shenfeld, Eliad Tsfadia, Katrina Ligett  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An estimator can be accurate and stable on typical data, yet sensitive to a few possible records. Differentially private mechanisms commonly scale their noise to the worst-case influence of a single record, which lets these records dictate the noise even when the remaining data would allow far less. Removing them first would restore the smaller scale, but the removal must itself be private.
We introduce \emph{propose-filter-release} (PFR), which, by privately filtering its input, turns a mechanism that protects the addition or removal of a typical record, one that fits the remaining data, into one that is differentially private in the standard sense, on every input. Using our novel filtering step, PFR requires only a concave friendliness score, which measures how well a record fits a dataset, and a release mechanism that is friendly-DP, that is, private when the changed record fits the remaining data. For every such score and release mechanism, it guarantees differential privacy under public conditions on the number of records, so it is a general privacy primitive, comparable to propose-test-release, and FriendlyCore can be viewed as one of its implementations.
We illustrate the generality of PFR by instantiating it for scalar statistics, principal subspace estimation, the KL divergence of user histograms, the effective resistances of a graph, and treatment-rule selection.

---


> [!TIP]
> 当前位于：**401-432**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-432**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
