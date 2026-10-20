# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 251. [Data-driven forecasting of tropical cloud forest phenology: A dynamical systems and machine learning hybrid approach](https://arxiv.org/abs/2610.25283)

**<font color=#1a73e8>作者：</font>** Pedro Garcia, Saul Flores  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting how species and ecosystems respond to climate change is a critical challenge in ecology, particularly in hyper-diverse tropical biomes. While traditional phenological models often rely on preconceived functional forms, this study introduces a data-driven hybrid approach that integrates dynamical systems theory with machine learning to forecast flowering and fruiting cycles.
Using a robust 35-year dataset from a Venezuelan tropical cloud forest, we reconstruct the system's state-space using delay vectors inspired by Takens' theorem, incorporating climate forcing variables such as temperature and precipitation. The model was trained using Gaussian Process Regression, providing both point predictors and explicit uncertainty estimates.
Our results clearly suggest that the synergy between dynamical systems and machine learning effectively captures the non-linear complexities of ecological time series. Specifically, the model achieved higher predictive accuracy for flowering and fruiting. This hybrid framework offers a scalable tool for anticipating phenological mismatches and informing conservation strategies in the face of global environmental change.

---


### 252. [Learning Lane-Structured Conditioning Fields for Online HD Mapping](https://arxiv.org/abs/2610.25284)

**<font color=#1a73e8>作者：</font>** Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-definition maps provide critical structural information for downstream autonomous driving tasks. Recent methods increasingly rely on external priors to improve prediction accuracy and robustness. Yet, existing prior representations expose a trade-off: dense rasters are easy to integrate but ignore certain map geometric properties, while sparse vectors preserve geometric structure but require dedicated encoders and are difficult to plug into existing architectures. Moreover, external priors can be inaccurate, costly to acquire, or difficult to maintain, motivating a structural representation that can provide geometric guidance while remaining learnable and broadly applicable. We address this limitation with the Lane Field, a dense BEV-aligned geometric representation that encodes local lane structure at each spatial location and can be either predicted from onboard observations or constructed from external map priors. Building on this representation, we introduce a plug-and-play framework that enhances online HD mapping through two complementary mechanisms: BEV feature modulation, which injects lane-structured cues into latent BEV features, and deformable attention guidance, which steers query sampling toward the underlying lane geometry. We primarily evaluate our method on OpenLane-V2, showing that conditioning BEV features and guiding deformable attention with local lane geometry enables our framework to consistently improve existing methods and achieve state-of-the-art performance on lane segment perception. Project page: this https URL

---


### 253. [A discrete-continuous-time stochastic framework for attention-deficit/hyperactivity disorder-related symptom modeling and pharmacological intervention via methylphenidate](https://arxiv.org/abs/2610.25285)

**<font color=#1a73e8>作者：</font>** Oana-Maria-Catalina Crisan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents an original mathematical and computational framework for modeling the efficacy of methylphenidate as an optimal control policy acting on the nonlinear dynamics of attention deficit hyperactivity disorder. Neural processes in ADHD are conceptualized as stochastic processes with trajectories that inherently converge towards stable, yet dysfunctional patterns associated with clinical symptoms. The pharmacological intervention is mathematically formalized as an external control signal that reassesses the system's drift and redirects these trajectories towards neurotypical regimes. To bridge these theoretical stochastic models with empirical clinical data, latent representations are inferred using a novel deterministic hybrid deep learning architecture, combining a one-dimensional convolutional neural network and a Vision Transformer, trained on preprocessed functional magnetic resonance imaging data.

---


### 254. [PRICE: Privacy-Preserving Image Classification in Mobile Edge-Cloud Computing with Homomorphic Encryption](https://arxiv.org/abs/2610.25286)

**<font color=#1a73e8>作者：</font>** Duc-Huy Nguyen, Bui Duc Manh, Chi-Hieu Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-assisted image classification enables many mobile AI applications, but transmitting raw images to the cloud raises significant privacy concerns. Homomorphic encryption (HE) allows computation over encrypted data; however, existing end-to-end HE-based inference pipelines incur prohibitive latency and computational overhead, limiting their feasibility for latency-sensitive mobile systems. This paper addresses how to enable efficient encrypted image classification in mobile edge-cloud environments without sacrificing accuracy. We propose PRICE, a three-tier edge-cloud architecture that partitions deep neural network inference between a trusted edge and an untrusted cloud. The edge performs lightweight feature extraction in plaintext, while only compact embeddings are encrypted using the Cheon-Kim-Kim-Song (CKKS) scheme and offloaded to the cloud for encrypted final-layer inference. This design avoids homomorphic evaluation of deep backbone layers, significantly reducing computation depth, ciphertext size, and end-to-end latency. To further improve efficiency, we develop RowHyDiag, a row-packed hybrid diagonal encoding with hoisted-rotation-aware encrypted matrix-vector computation, which minimizes rotation operations and improves slot utilization. Extensive experiments on real devices across five datasets demonstrate that, under the evaluated 128-bit-security configurations, RowHyDiag achieves up to 31.8$\times$ faster cloud inference, 85.3$\times$ fewer rotations, and 83.0$\times$ lower setup payload than the conventional Halevi-Shoup diagonal method. RowHyDiag also outperforms the PEGASUS linear-transformation baseline, providing 1.1-4.5$\times$ faster cloud inference and 1.2-3.4$\times$ lower setup payload. The results show that PRICE enables deployment-ready, low-latency encrypted inference for mobile edge-cloud systems under a trusted-edge threat model.

---


### 255. [The Explainability Illusion: Must ViTs Exhibit Patch-Decoding Interpretability?](https://arxiv.org/abs/2610.25289)

**<font color=#1a73e8>作者：</font>** Ronen Schaffer, Hila Manor, Tomer Michaeli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformers are widely assumed to exhibit token-decoding explainability. In particular, in vision transformer (ViT) classifiers, decoding individual patch tokens has become a common diagnostic tool due to its tendency to yield human-interpretable outputs. In light of the increasing popularity of this approach, an important question is whether token-decoding explainability is an inherent property of transformers that should be expected to hold across architectures, scales, and training objectives, or merely an artifact of some implicit bias. In this paper we systematically study token-decoding explainability across diverse ViT settings, spanning architectures, scales, and training objectives, using both controlled experiments and real-world models. We find that while some models indeed exhibit aligned and interpretable token decodings, others exhibit either inverted explainability maps or a complete lack of correlation with the image semantics. As we show, these tendencies toward different explainability behaviors are not intrinsic to the architecture and can vary arbitrarily with changes in the optimization landscape. We provide theoretical support for these observations by demonstrating a setting where a single fixed toy transformer architecture can provably implement the optimal classification rule in multiple ways, which differ in their patch-decoding explainability patterns. Our results show that token-decoding explainability is not an inherent property of trained transformers, but rather an outcome contingent on the problem setting and thus should not be a-priori assumed to hold. Code can be found in this https URL .

---


### 256. [World Model Interpretability: From Decoding Representations to Understanding Latent Worlds](https://arxiv.org/abs/2610.25296)

**<font color=#1a73e8>作者：</font>** Jize Wang, Yongcheng Jing, Xinyi Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emerging Joint-Embedding Predictive Architectures (JEPAs) are moving beyond representation learning towards latent world models that support prediction, planning, and control. Yet their latent worlds naturally lack a human-interpretable interface. In this Perspective, we argue that as JEPA latents become internal states for prediction and action, interpretability must move beyond what they encode to how latent variables interact, evolve, and causally drive prediction. To this end, we envision a four-stage research agenda, involving Ground, Structure, Verify, and Act, to guide this shift toward actionable latent-world understanding. Within our framework, existing JEPA interpretability efforts provide early evidence for Ground, while systematic analysis of latent structure, causal verification, and intervention remains largely unexplored. Overall, this Perspective aims to call for a broader latent-world interpretability agenda that shifts attention from decoding representations toward understanding, validating, and acting on latent worlds.

---


### 257. [Learning When to Abort in Transformer Planning: A Mechanistic Study](https://arxiv.org/abs/2610.25300)

**<font color=#1a73e8>作者：</font>** Shi Feng, Qimin Zhong, Siwei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning does not by itself imply the ability to recognise errors, but recognising errors can improve planning capacity. In this paper, we study this phenomenon in Transformer planning. To analyze the inner mechanism, we follow the approach of Wang et al. (2024) and abstract planning as path-finding in graphs. In this setting, we train the model to detect the error of invalid transitions, i.e., after the model generates a next node that is not adjacent with the current node, the model should then generate a special abort token x. For expressiveness, we construct a Transformer with feed-forward width $O(|V|)$ for any fixed graph with node set $V$. It can detect all possible invalid transitions, and select a valid next node if the prefix is valid. We then propose a worst-case lower bound on feed-forward width, which makes the detector's linear width near-optimal up to logarithmic factors. In trained models, we demonstrate that invalid-transition detection increases previous-node attention, and most of the valid--invalid separation locates in the feed-forward network's output. This accords with our theoretical insights. Finally, we use this error detection to improve the model's performance: at inference, generating the abort token x will directly cause an external procedure to discard the attempt and restart from the original prompt. Experiments show that error detection combined with retry improves model's planning reliability on graphs, Countdown, and mazes.

---


### 258. [SENRI: Understanding the Space-Event Nexus in Real-Life Videos](https://arxiv.org/abs/2610.25309)

**<font color=#1a73e8>作者：</font>** Kehan Lan, Kaining Ying, Henghui Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human memories are organized in a way that connects events with their corresponding spatial contexts. An AI assistant should also be able to memorize and recall the nexus of events and spaces. Thus we introduce SENRI, a task that studies this space--event connection in long, continuous real-life egocentric video. It contains six task types in two directions: Event$\rightarrow$Space, which recovers spatial knowledge from event cues, and Space$\rightarrow$Event, which retrieves events from regions and trajectories. To evaluate this, we build SENRI-Bench, containing 500 manually annotated multiple-choice questions over 10 uninterrupted self-recorded videos with around 25.3 hours of content. Also, we evaluate three typical long video understanding paradigms: direct perception, evidence seeking, and persistent memory. The task remains challenging across all three paradigms, highlighting substantial room for improvement. Then we show two representative failure modes of existing memory methods and address these evidence gaps with SENRI-Agent, a controller that uses Target-Guided Visual Check (TGVC) to propose local visual check tasks for parallel verifiers and integrate the reports into a working memory to help with reasoning. Built upon existing memory systems, SENRI-Agent improves the performance of existing baselines without modifying their stored memories. We hope SENRI will provide valuable insights into how real-life egocentric understanding should be evaluated, reveal the gaps in existing approaches, and offer a possible direction for improvement.

---


### 259. [AdaFedXplain: Adaptive Federated Learning with Explainable AI for Ransomware Detection](https://arxiv.org/abs/2610.25318)

**<font color=#1a73e8>作者：</font>** Md. Emran Biswas, Md. Delowar Hossain, Mst. Tanbin Yasmin Tanny 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attacks using ransomware have developed into complex multiphase campaigns that target vital infrastructure, resulting in annual damages of billions of dollars. Conventional detection techniques are ineffective against zero-day variations, and privacy issues are raised by centralized machine learning algorithms. Federated learning allows for cooperative model training without data sharing, however current FL approaches suffer from explainability issues, high communication cost, and non-IID data heterogeneity. In this study, we present AdaFedXplain, an explainable AI-based adaptive federated learning system for ransomware detection. Our approach includes progressive XGBoost complexity to avoid overfitting, a decaying learning rate schedule for stable convergence, and dynamic client grading based on ransomware prevalence and data sufficiency. Using 62,485 real-world ransomware samples from four OS-based non-IID clients, we compare AdaFedXplain against FedAvg, FedProx, and SCAFFOLD. According to experimental data, AdaFedXplain outperforms all baselines with 99.59% detection accuracy and 99.64% F1-score while cutting energy usage by 75%, latency by 65%, and communication overhead by 75%. The ablation investigation demonstrates that every element enhances performance. Security analysts can use SHAP explainability to identify important PE header characteristics that influence detection decisions. Our system provides a collaborative ransomware detection solution that is efficient and interpretable, while reducing privacy risks through federated learnings data-local training paradigm.

---


### 260. [MPIG: Multi-angle Polarization Image Generation from a Single Polarization Observation](https://arxiv.org/abs/2610.25326)

**<font color=#1a73e8>作者：</font>** Jue Wang, Ruilin Huang, Liquan Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarization imaging provides informative cues for material analysis, scene understanding, and visual perception. However, acquiring complete polarization observations typically requires specialized hardware and multi-angle measurements, thereby increasing system complexity and limiting practical deployment. In this work, we address the problem of predicting the missing $45^\circ$, $90^\circ$, and $135^\circ$ polarization views from a single $0^\circ$ observation by leveraging a learned scene prior. To this end, we propose MPIG (Multi-angle Polarization Image Generation), a Swin Transformer-based framework that couples cross-angle feature interaction with residual decoding to predict angle-dependent intensity variations while preserving shared scene structure. Specifically, measured Stokes differences and polarization-strength-aware supervision guide the recovery of polarization modulation, orientation, and magnitude, while low-rank factorization further reduces the decoding cost. We also construct HighPol, a large-scale real-world polarization dataset comprising 5,474 groups of high-resolution four-angle polarization images collected from diverse indoor and outdoor scenes. Experimental results demonstrate improved image and polarization accuracy, achieving 29.729 dB PSNR, 0.9505 SSIM, and $21.514^\circ$ AoLP MAngE while requiring 85.86 M parameters and 1.126 T FLOPs. Furthermore, downstream validation on glass and semantic-segmentation tasks suggests that the generated polarization images can preserve task-relevant information, demonstrating the effectiveness of MPIG and the practical utility of predicted polarization observations for downstream vision applications.

---


### 261. [CoRe-WM: Conditioned Response-State World Modeling for Longitudinal Treatment-Response Prediction in Breast DCE-MRI](https://arxiv.org/abs/2610.25333)

**<font color=#1a73e8>作者：</font>** Lin Zhao, Bowen Chen, Qiaohui Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathologic complete response (pCR) after neoadjuvant chemotherapy is a key prognostic indicator in aggressive breast cancer, yet existing prediction approaches either rely on pretreatment imaging alone, missing the patient's evolving response, or optimize multi-visit classifiers under direct outcome supervision, coupling representation learning with the clinical endpoint. We formulate longitudinal pCR prediction as a world-modeling problem and propose Conditioned Response-state World Modeling (CoRe-WM), which learns a latent state-transition model that predicts the next imaging state from the observed sequence. The transition function is conditioned on patient clinical profile and assigned therapy through additive shift and feature-wise modulation, enabling patient- and treatment-specific dynamics. A Factorized Response State pathway further decouples treatment-response dynamics from imaging appearance by encoding the structural prior that response manifests primarily in lesion morphology. After pretraining, all parameters are frozen and a linear readout predicts pCR at each clinical decision point. We evaluate CoRe-WM on I-SPY2 under five-fold cross-validation and assess cross-cohort transfer on I-SPY1. CoRe-WM achieves the highest discrimination among all evaluated methods at every prospective decision point, and demonstrates robust cross-cohort transfer. Ablation studies identify patient-profile conditioning and the factorized response pathway as the principal contributors. These results establish world-model-based representation learning as a promising framework for outcome prediction in oncology and beyond.

---


### 262. [A Distribution-Free Separation Between Learned and Fixed Features](https://arxiv.org/abs/2610.25335)

**<font color=#1a73e8>作者：</font>** Daniel Barzilai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of neural networks is largely attributed to their ability to learn useful representations from training data. However, known results that prove a computational advantage of learned features over fixed ones are restricted to specific input distributions. We settle the COLT open question of Feldman, Kamath, and Srebro (2026) by showing that this advantage can persist in the distribution-free setting.
We construct a family of hypothesis classes that can be efficiently learned by a natural gradient-based algorithm on a two-layer ReLU network, but cannot be represented by linear predictors over any fixed feature map with polynomial dimension (and runtime). Specifically, for any sufficiently small error and any sufficiently large runtime budget R (depending on the error), there exists a hypothesis class that the neural network learns under any input distribution to the desired expected classification error in time at most R, while the dimension complexity (governing the dimension needed by linear predictors) is superpolynomial in R.

---


### 263. [Edge Deployable Lightweight Framework for Real-Time Driver Safety System with Integrated Lane Departure and Traffic Sign Recognition](https://arxiv.org/abs/2610.25340)

**<font color=#1a73e8>作者：</font>** Hassaan Ali Qureshi, Danish Hussain, Ali Hassan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lane departure and traffic-sign negligence are leading contributors to road accidents, particularly in regions with non-standardized signage and limited annotated data. Existing Advanced Driver Assistance Systems (ADAS) solutions are often developed as disjointed submodules, are rarely validated for real-time operation, and struggle to balance accuracy with low-latency inference for embedded deployment. We address these gaps with a unified, edge-deployable ADAS framework that simultaneously performs lane-departure warning (LDW) and traffic-sign detection and recognition (TSD/TSR), and validate the proposed system on automotive-class devices. Our framework combines a lightweight, lane-segmentation-driven LDW, which includes a drivable-area fallback for degraded markings, with a two-stage TSD/TSR pipeline consisting of efficient sign localization followed by fine-grained classification, designed to preserve accuracy at embedded latency. To support region-specific deployment under data scarcity, we curate a 35-class local traffic-sign dataset and introduce a generalized augmentation and balancing profile, expanding the corpus from 359 images to 8,750 samples. On an NVIDIA Jetson Orin Nano, the integrated system sustains 15 FPS end to end (32 FPS for LDW and 18 FPS for TSD/TSR). The TSD/TSR branch achieves 97.4 mAP for detection and 95.6% validation accuracy (93.1% on a local real-world set) while maintaining an approximately 13.9 M parameter footprint. Relative to recent methods that target a single task or report results only on desktop-class GPUs, our approach delivers both LDW and TSD/TSR with real-time performance on edge hardware, providing a practical pathway to low-cost, field-ready ADAS in resource-constrained settings.

---


### 264. [CASE: Complementary Articulation-Aware Speech Encoder to Enhance Speech-Driven 3D Facial Animation](https://arxiv.org/abs/2610.25342)

**<font color=#1a73e8>作者：</font>** Jaehong Myung, Seungho Eum, Taegon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose self-supervised speech encoders provide strong acoustic representations, but their pretraining objectives are not explicitly aligned with the visible articulatory dynamics required by speech-driven 3D facial animation. We propose CASE (Complementary Articulation-aware Speech Encoder), a complementary speech encoder adapted by contrastively aligning short speech clips with continuous 3D lip-mesh VQ-VAE latents. After adaptation, the geometry branch is removed, and the audio-only CASE representation is fused with the baseline SSL speech representation through residual cross-attention, while retaining the motion-decoder architecture and objective. Across four VOCASET baselines, CASE reduces mean lip vertex error by 2.8-6.0%, and mean full-face vertex error decreases in every system. Under the same fusion protocol, CASE yields lower mean LVE than the unadapted AV-SE stream on all four generators, with model-dependent margins. Because adaptation uses Korean speech-geometry pairs and evaluation uses English VOCASET, the result is consistent with cross-language downstream transfer under a shared English-pretrained audio-visual prior.

---


### 265. [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)

**<font color=#1a73e8>作者：</font>** Yifei Wang, Wei Tian, Wenhua Bao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors. First, cross-camera photometric inconsistency, caused by variations in exposure, ISP, and illumination, can be incorrectly absorbed into Gaussian geometry. Second, unreliable local geometric supervision arises from normal-based constraints near depth discontinuities. To address these issues, we present \textbf{MCSplat}, a multi-view consistent feed-forward Gaussian splatting framework for driving scenes. MCSplat constructs a canonical appearance space from depth-guided multi-camera correspondences to decouple geometry learning from camera-specific appearance. A multi-scale Bilateral Grid Transformer restores raw camera appearance from canonical renderings, enabling photometric supervision without contaminating Gaussian geometry. To improve local geometric reliability, we estimate Fisher-information-based uncertainty from photometric sensitivity and use it to adaptively weight surface-oriented self-supervision. Extensive experiments demonstrate improved reconstruction quality and generalization across driving datasets. Geometry-oriented evaluations further reveal enhanced cross-view depth consistency and local surface-normal agreement, while qualitative results show fewer geometric artifacts and more coherent structures across overlapping views.

---


### 266. [Equivalent Non-linear Shift Register Transformations and Espresso](https://arxiv.org/abs/2610.25346)

**<font color=#1a73e8>作者：</font>** Anirban Ghatak, Kaushik Sarkar, Anupam Chattopadhyay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The stream cipher Espresso was designed by E. Dubrova and M. Hell as a hardware-efficient candidate for 5G security. It has two components - a 256-bit binary non-linear feedback shift register (NFSR), with 14 feedback taps, and a 20-variable non-linear output function. However, the security of Espresso with regard to several standard cryptanalytic attacks are estimated using an alternate NFSR, which has only two feedback taps. The above analysis is based on the claim that this alternate NFSR is obtained using a transformation algorithm which preserves the output sequence of the original NFSR. This issue has become all the more significant in the light of recent results on hardware performance evaluations, which assume that the stated equivalence holds.
This article presents the first successful attempt in settling the above question of Espresso NFSR equivalence. We arrive at our main result by a careful analysis of existing transformation methods relevant to the question. In doing so, we first identify and correct a critical flaw in the proof of a foundational result of E. Dubrova. Next, in the context of Espresso equivalence, we analyze and unify the transformation framework of Dubrova and the one proposed by Yao and Parampalli. Based on our analysis, we have succeeded in transforming the LFSR in an Espresso-equivalent design reported by Yao and Parampalli to the Espresso alternate NFSR. Further, we have obtained a corresponding non-linear output function which achieves output-equivalence with the LFSR design, and hence, with Espresso.

---


### 267. [On Pearl Blockchain's Proof of Useful Work: Systematization and Flexibility](https://arxiv.org/abs/2610.25347)

**<font color=#1a73e8>作者：</font>** Youlong Ding  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We revisit the proof-of-useful-work (PoUW) scheme in Pearl blockchain's white paper (Pearl Research Team), giving a systematic sensitivity characterization as an alternative to its Jackpot policy, along with efficient algorithm for verifying the sensitivity condition.
Beyond its independent interest, our characterization yields a more flexible PoUW scheme that eenables miner autonomy: each miner can independently choose its noise magnitude to tailor the trade-off between computational accuracy and mining efficiency to its own needs.

---


### 268. [Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data](https://arxiv.org/abs/2610.25349)

**<font color=#1a73e8>作者：</font>** One Octadion, Novanto Yudistira, Yuta Nakashima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-conditional conformal prediction calibrates a separate score threshold for every class and therefore requires labelled calibration examples of every class. In long-tailed deployments these are exactly what is missing: rare classes are left with few or no held-out examples, and existing methods are either undefined for them or fall back to the shared marginal threshold. We ask whether the per-class correction can instead be predicted from descriptors of the class that require no labels at all. We propose Predicted Class Correction (PCC), which regresses the offset between the per-class and the marginal conformal quantile on geometric descriptors of the classifier head, shrinks the prediction by a scalar selected on the labelled classes, and refits a single marginal offset. The descriptors depend only on the model's weights, so a class with zero calibration examples still receives its own threshold, and since only one scalar is calibrated, split conformal's marginal guarantee is retained. On ImageNet, PCC improves worst-class coverage on such classes by 0.058 [0.006, 0.110] at matched average set size, 42% of an oracle that sees the test labels. Of eight baselines on the same splits, six change the statistic by exactly zero and the best reaches 0.016 with an interval containing zero, so PCC is the only one distinguishable from no improvement; the gain persists with only 100 labelled classes out of 1000. A second finding concerns evaluation: worst-class coverage becomes unmeasurable before it becomes unachievable. Below roughly 35 test examples per class no improvement can be shown even for an oracle, so a null result there reflects the evaluation set, not the method. Restricting evaluation above this depth recovers a significant improvement on Pl@ntNet-300K, where the effect had appeared absent.

---


### 269. [LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization](https://arxiv.org/abs/2610.25358)

**<font color=#1a73e8>作者：</font>** Mohammad Omama, Aeyan Ashraf, Sandeep Chinchali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization is critical for embodied agents, but deploying state-of-the-art deep feature matchers on edge devices is fundamentally limited by their massive computational cost. Standard deep matchers tightly interleave intra-image context building and inter-image matching at every layer, creating a severe interaction bottleneck. Localizing a single query against K database images forces the system to execute the full network K independent times with no capacity for caching. To break this bottleneck, we advocate for a paradigm shift toward cacheable image matching. We realize this paradigm with LateMatch, a versatile approach that restructures existing matchers by deferring inter-image interaction to their final layers. By isolating intra-image processing into offline-cacheable Context Blocks, only a small set of Interaction Blocks must be executed online. To further optimize LateMatch, we introduce E-SToRE (Entropy-guided Spatial Token Reduction and Expansion). E-SToRE leverages the decreasing Shannon entropy of the late Interaction Blocks to dynamically reduce token counts just prior to cross-image interaction. Evaluated across HPatches, ScanNet, MegaDepth, ETH-3D, and Aachen, LateMatch reduces effective computational cost by over 2x compared to standard deep matchers, while E-SToRE yields an additional 10% to 14% savings with negligible degradation in accuracy.

---


### 270. [Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence](https://arxiv.org/abs/2610.25360)

**<font color=#1a73e8>作者：</font>** One Octadion, Firmansyah Sundana, Novanto Yudistira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are increasingly judged by how well they rank plausible futures, yet plausibility alone is the wrong target. The same scene can evolve under many latent rules, and a future that is smooth and physically valid under one rule can be incoherent under the rule actually in force. We formalize the resulting failure, operator-blindness, and show that it is systematically hidden by standard evaluation: a scorer can attain near-perfect generic ranking while separating current-world from other-world futures no better than chance. We introduce Operator-Mismatch Contrastive (OMC) learning, whose semantic hard negatives are valid-but-wrong-operator trajectories, and a matching protocol that measures world-relative coherence directly. On a controlled synthetic benchmark with in- and out-of-distribution operator parameters, across two trajectory-scoring backbones, and on feature-level external validation with CoPhy ballsCF, OMC raises operator-sensitive scoring far above a chance baseline that nonetheless achieves 0.99 generic top-1. We prove that the wrong-operator negative is necessary both for the protocol to detect the failure and for the objective to fix it, and position OMC as an auxiliary coherence signal (a trajectory-coherence scorer, not a generative model, planner, or control agent) that can be attached to existing world-model representations.

---


### 271. [GreenNIDS: A Benchmark Workflow and Analysis Dataset for NetFlow Intrusion Detection Experiments](https://arxiv.org/abs/2610.25366)

**<font color=#1a73e8>作者：</font>** Lilia-Eliana Popescu-Apreutesei, Sabina-Cristiana Necula  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Comparing the predictive performance and computational cost of flow-based intrusion detection experiments requires both quantities to be available for each run. GreenNIDS connects benchmark execution on public NetFlow datasets to a reusable analysis dataset. Model implementations write a common set of outputs, which are ingested into a run-level table with companion tables for model configuration, feature importance, and training history. The run-level table combines predictive metrics with timing, throughput, memory use, and energy estimates based on thermal design power. A CPU-only demonstration comprises 216 runs across four dataset families, three versions, and binary and multiclass tasks. Ingestion produces a 216 x 96 analysis table with no duplicate run identifiers and complete Matthews correlation coefficient (MCC) and F1 coverage. Multiclass ROC-AUC is missing for 36 PyTorch runs, making metric availability an explicit part of subsequent comparisons. The stored records support grouped performance and training-time plots, as well as resource screening after execution. Combining task-specific MCC thresholds with limits on training time, peak RAM, and estimated training energy retains 25.0% of the full run collection. These results establish compatibility within the evaluated collection and support comparisons after execution, subject to the recorded preprocessing, execution profile, and approximate energy accounting.

---


### 272. [Painting Change Map as guidance for generating painting processes](https://arxiv.org/abs/2610.25369)

**<font color=#1a73e8>作者：</font>** Markus Pobitzer, Chang Liu, Niccolò Biondi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital art generation has undergone a massive paradigm shift, moving from static image synthesis to dynamic video generation that can mimic the human painting process. While existing models can synthesize visually stunning time-lapses of paintings being created or "unpainted," they largely treat the creative process as a black box. Current conditioning mechanisms are either too rigid, relying on static geometric cues like Canny edges or depth maps, or too holistic, utilizing simple scalar progress variables that offer no localized control. Consequently, users lack the agency to steer how a painting evolves over time. In this work, we argue that true control over the video generation of artwork requires a joint understanding of two fundamental dimensions: where an artist acts, and when those actions take place. To achieve this, we introduce the Painting Change Map, a novel spatio-temporal control mechanism that explicitly tracks normalized structural changes across a 1,000-timestep continuum, a resolution sufficient to capture fine-grained stroke-level changes while remaining computationally tractable. By mapping localized visual differences into an encoded RGB space, our representation enables fine-grained guidance for both the forward painting and reverse unpainting processes. Extensive benchmarking demonstrates the efficacy of our approach. We outperform existing control baselines and achieve competitive or superior results compared to state-of-the-art painting methods. Furthermore, under oracle conditions, our method surpasses all baselines by a significant margin. Code is available at this https URL.

---


### 273. [Multi-site Learning for Forecasting Day-Ahead Wind-Power Production for Onshore Wind Farms in Great Britain with Deep Neural Networks](https://arxiv.org/abs/2610.25370)

**<font color=#1a73e8>作者：</font>** James Kean, Aidan O'Sullivan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate day-ahead wind-power production forecasting is increasingly important for energy system operations, market activity and balancing Great Britain's grid as wind generation grows. In this study, we train multi-site deep neural networks (DNNs) using pooled historical production and reanalysis weather data from 88 onshore wind Balancing Mechanism Units (BMUs). Forecasts are produced at 09:00 UK time for the following midnight-to-midnight delivery day, matching NESO's operational day-ahead forecasting schedule. We use reanalysis weather as future covariates during training and numerical weather prediction (NWP) forecasts during inference, extending training beyond the available historical NWP archive. Our multi-site recurrent neural network outperforms site-specific RNNs and a multi-site XGBoost model, while processing the full future-weather trajectory for the forecast horizon further improves accuracy relative to hour-aligned approaches. Our best model, an RNN with a bidirectional weather encoder (BiRNN) for NWP trajectory processing, reduces MW mean absolute error and root mean squared error relative to NESO by 17.94% and 12.51%, respectively, across 638,246 matched BMU-hour observations under conditions approximating unconstrained wind farm operations. In 40 leave-one-out trials, the BiRNN achieves lower MAE than NESO at 32 excluded sites, indicating transferable forecasting ability despite reduced accuracy when sites are omitted from training. Our capacity-estimation, data-cleaning and reanalysis-based training approach provides a basis for scaling NWP-aware multi-site forecasting to additional wind farms, longer production histories, and increased forecast accuracy beyond that seen in this study.

---


### 274. [Simulating Infant Senses with Age-Tuned Networks](https://arxiv.org/abs/2610.25377)

**<font color=#1a73e8>作者：</font>** Somesh Mohapatra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What a newborn sees, hears and feels, and how this changes month by month, has been measured sense by sense, with different methods and in different units. We bring these measurements together for the first two years of life and ask whether small neural networks tuned to a given age can turn them into a quick, inspectable simulation of sensory perception. Each sense's immaturity is written as a fixed, age-indexed filter on the input, and a small prediction network learns behind it over the first year. The filters alone reproduce the order in which the senses mature, by construction. The networks add what filters cannot: in vision they extract far less than their input allows at early stages (at the newborn stage a toy's position cannot be read out, $R^2 = 0.00$, against 0.57 for a network trained directly on the same input), and a critical period and perceptual narrowing emerge without being built in; in hearing they track what their input allows. The same filters drive the Baby Senses Lab, a free website that shows a user's own images and sounds as a baby of a chosen age might sense them. It is a research and teaching tool, not a diagnostic test.

---


### 275. [Structured Relevance Determination and Channel Additive Gaussian Processes for Image Data](https://arxiv.org/abs/2610.25385)

**<font color=#1a73e8>作者：</font>** Harald Roßels, Ludovico Scarton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce radial basis function (RBF) kernels for Gaussian processes that use structured hyperparameter sharing for image-valued inputs. For high-dimensional inputs such as images, a fully anisotropic RBF kernel assigns a separate lengthscale to each input dimension, which can introduce many hyperparameters and may lead to overfitting and poorly calibrated predictive uncertainty when data are limited. We propose structured relevance determination by tying lengthscales across groups of adjacent pixels and within each colour channel. This yields patch-wise and channel-wise constrained anisotropic RBF parametrisations that reduce the number of independently learned lengthscales. We further introduce channel-additive Gaussian processes for multi-channel images and combine them with structured relevance determination, resulting in a parameter-efficient decomposition of the latent function into components defined on channel subsets, enabling some non-local generalisation. The proposed kernels are evaluated on MNIST and a compact binary aircraft-detection dataset of low-resolution RGB satellite image chips. We also show how channel-wise structured relevance determination can be incorporated into convolutional Gaussian processes. We observe improved predictive performance compared to isotropic and fully anisotropic RBF baselines.

---


### 276. [Only Means Only: what a harmonization benchmark score averages over](https://arxiv.org/abs/2610.25387)

**<font color=#1a73e8>作者：</font>** Imad Buljić, Delaida Muminović  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image harmonization methods adjust the colour and lighting of an object pasted into a photograph so that it looks native to its new scene, and they are ranked by average error on one benchmark whose test images are real photographs with one object recoloured. One photograph can yield several such test images, and the benchmark promises that no photograph appears in both the training and the test split. We find that 1,399 photographs do, and the composites built on them are a quarter of the test set. Duplicate checks over file names or bytes miss this, because every composite is a different file. On that quarter the three methods we score end to end read two to five times lower error than on the rest, but most of the gap is composition rather than the sharing: the shared composites come almost entirely from one of the benchmark's four source collections, and inside that collection the gap falls to about one and a half times. An official score is therefore an average over two populations, mixed in a proportion the benchmark does not report. We release a test list of 5,581 composites whose construction identities do not appear in training, with four confirmed near-duplicate pairs disclosed rather than removed, adoptable without retraining at the price of one rescore per checkpoint. We leave open whether the sharing itself changes what a model learns.

---


### 277. [The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data](https://arxiv.org/abs/2610.25389)

**<font color=#1a73e8>作者：</font>** Abdelkrim Alfalah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empirical studies of electricity prices routinely state that their models use only information available at the time of the trading decision. For weather-driven forecasts drawn from commercial archives, this condition is harder to meet than it appears, and whether it holds can change over time. We identify three timing pitfalls. A forecast run is labelled by the issue time of its weather model, but becomes available hours later and keeps changing after publication. Auction gates follow local clock time, while archives use UTC. Outturn series are revised after publication without earlier values being kept. Using the timestamps of 128,656 forecast runs from ten weather-model configurations, matched to the day-ahead and first intraday auction gates in Great Britain over 2022-2026, we find that selecting "the latest run issued before the gate" picks a run not yet published at the gate on more than 99% of delivery days for six of the ten configurations at one of the two gates. For GFS at the day-ahead gate, the share is 0.6% in winter and 99.8% in summer. The exposure also shifts as publication delays drift, and an action margin of a few minutes can cost a full six-hour forecast cycle. The wrongly selected inputs differ materially from those available at the gate, but their apparent accuracy gain ranges from -9% to +24% across variables, models, gates and seasons, so its effect cannot be assumed and must be measured. We argue that point-in-time correctness is a dynamic property of the data pipeline, and propose a protocol that audits it from timestamps before any model is fitted.

---


### 278. [ATLAS: Attention-Guided Test-Time Latent Selection for Compositional Visual Autoregressive Generation](https://arxiv.org/abs/2610.25390)

**<font color=#1a73e8>作者：</font>** Hossein Shahabadi, Raya Namazi, Mahdieh Soleymani Baghshah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual autoregressive models produce convincing images but can misassign attributes and spatial relations. Searching multiple generation paths can improve composition, yet completing every candidate is costly. We introduce ATLAS, a training-free framework that uses the frozen generator's internal attention to guide search before final images are available. Within-prompt diagnostics identify attention-derived scores that predict final compositional preferences on Infinity, with category-dependent transfer to Switti. ATLAS uses these on-the-fly signals to progressively concentrate computation on promising trajectories. It maintains multiple coarse alternatives, prunes candidates without decoding at intermediate scales, and reserves image-space evaluation for a final choice among partial trajectories. ATLAS scales effectively on both backbones, achieving higher mean scores on the evaluated T2I-CompBench and GenEval categories as more computation is devoted to search. At the largest tested budget, the targeted T2I-CompBench mean improves by over 10% relative to each backbone. Separate profiles show over 50% less generation time than completing and evaluating all candidates at equal initial counts, alongside lower peak allocated GPU memory. Relative time savings are larger at the higher tested candidate count. Together, these results support scalable compositional search: additional sampling expands exploration, while attention-guided selection limits continuation cost without parameter updates or gradient-based optimization.

---


### 279. [Paloma: Phase-Conditioned Residual Modulation for Time Series Forecasting](https://arxiv.org/abs/2610.25392)

**<font color=#1a73e8>作者：</font>** Jingru Fei, Wei Fan, Kun Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explicitly modeling periodicity has proven to be an efficient approach for time series forecasting, where the residual, obtained after removing the periodic component from the time series, is typically treated as unstructured noise. However, in this work, we show that such residuals still exhibit structured, \textit{phase-dependent} deviations, as supported by both empirical observations and theoretical analysis. This suggests that residuals should not be treated merely as unstructured noise, but instead as \textit{phase-conditioned signals} whose variations arise in both direction and magnitude. Motivated by this perspective and inspired by phase and amplitude modulation in classical signal processing, we propose \textit{Paloma}, a simple yet effective framework for modeling residual deviations. Specifically, Paloma comprises two complementary modules: \textit{a Phase Rotation module}, which performs phase-conditioned rotations to capture directional changes in the feature space, and \textit{an Amplitude Scaling module}, which applies phase-conditioned affine transformations to model magnitude variations. We further abstract the two modules into a general-purpose plugin, termed the \textit{Paloma technique}, which can be readily integrated into existing forecasting architectures to modulate input sequences in a phase-aware manner, enabling backbone models to capture phase-dependent variations in both direction and magnitude. Extensive experiments on twelve datasets demonstrate that Paloma achieves state-of-the-art and robust forecasting performance. Additional results show that the Paloma technique consistently improves a wide range of baseline models, validating its effectiveness as a general-purpose component. Our Code is available at \url{this https URL}.

---


### 280. [A 3D-Driven Framework for Moving-Camera Perspective-to-360° Video Generation](https://arxiv.org/abs/2610.25395)

**<font color=#1a73e8>作者：</font>** Michael Wakeham, Mrinmoy Kumar Das, Wenqi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Turning a moving-camera perspective video into a 360° video requires more than just generating content outside the input frame: observations revealed over time must be preserved, unseen regions completed, and the resulting scene kept consistent as the camera viewpoint changes. Existing methods assign these different requirements to a single conditional video model, requiring them to be jointly learned from panoramic video data. We instead present a modular, 3D-driven framework that distributes these three responsibilities across specialized components, all connected through a shared scene representation. Input observations are reconstructed explicitly in 3D, while a pretrained panoramic image model completes unobserved content from a selected panoramic render. This generated content is lifted into the shared 3D scene, where it remains spatially anchored across camera viewpoints. Without requiring any additional panoramic-video training, our framework achieves state-of-the-art input-view fidelity, perceptual quality, and geometric consistency on a static-scene subset of the Argus evaluation set. These results support our decomposed, 3D-driven formulation as a promising alternative to direct video generation in this setting.

---


### 281. [PolarVis: A Dataset and Diffusion Framework for RGB-to-Polarization Perception in Adverse Driving Scenes](https://arxiv.org/abs/2610.25396)

**<font color=#1a73e8>作者：</font>** Ruilin Huang, Jue Wang, Zhen Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reflections, glare, transparent structures, and material-dependent appearance variations can introduce ambiguity into RGB-based visual perception in vehicle-relevant environments. Polarization provides complementary reflection- and material-sensitive information, but its acquisition requires dedicated sensing hardware. This paper presents RGB-P Wild, a real-world dataset containing 10,000 paired RGB and four-angle linear-polarization image sets, together with PolarVis, a diffusion-based framework for recovering polarization representations from a single RGB image. PolarVis combines hierarchical RGB feature extraction, diffusion-based feature refinement, four angle-specific decoders, and multi-scale attention recalibration to reconstruct polarization intensity images at $0^\circ$, $45^\circ$, $90^\circ$, and $135^\circ$. On RGB-P Wild, PolarVis achieves a normalized-domain MSE of 0.0465, a PSNR of 27.83 dB, and an SSIM of 0.8597. Compared with the released PolarAnything model under the adopted evaluation protocol, PolarVis obtains an AoLP error of $25.66^\circ$ and a DoLP MAE of 0.0404, compared with $46.03^\circ$ and 0.1084, respectively. Cross-dataset evaluation on vehicle-mounted imagery further examines transfer beyond the training domain. In downstream evaluation, a frozen PCDNet achieves AP50/AP50:95 of 86.3%/59.1% on 990 RGBP-Car test images using PolarVis-generated polarization, compared with 87.0%/59.8% using measured polarization. These results indicate that RGB-derived polarization retains useful polarimetric information for the evaluated perception tasks, while remaining distinct from calibrated physical polarization measurements.

---


### 282. [RAHF-Net: Range-Aware Heterogeneous Fusion for LiDAR-Assisted RGB Semantic Segmentation](https://arxiv.org/abs/2610.25400)

**<font color=#1a73e8>作者：</font>** R.D. Lin, Pengcheng Weng, Ge Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies LiDAR-assisted RGB semantic segmentation, where LiDAR point-cloud features improve dense pixel-wise predictions in the RGB image plane rather than 3D point labels or detections. Existing 2D fusion methods often project point clouds into shallow depth/range maps and apply spatially uniform fusion, discarding rich 3D structure and ignoring the range-dependent reliability of outdoor LiDAR. We propose RAHF-Net, a Range-Aware Heterogeneous Fusion Network. Its Cylindrical-to-Perspective (C2P) module projects pretrained cylindrical voxel features into the image plane, preserving structured 3D semantic priors. A Range-Aware Heterogeneous Fusion (RAHF) module then uses a soft depth-derived range mask to perform LiDAR-guided geometric enhancement in reliable near-field regions and visual-context enhancement in sparse far-field regions. On KITTI-360, RAHF-Net achieves 65.76 mIoU, outperforming representative RGB-only and RGB-LiDAR baselines, including CMX by 1.45 points. Experiments on DELIVER further demonstrate improved robustness under adverse weather, illumination degradation, and sensor corruption.

---


### 283. [MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion](https://arxiv.org/abs/2610.25404)

**<font color=#1a73e8>作者：</font>** Houyuan Chen, Fanzhou Wang, Xiangyu Fan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-turn image editing aims to modify an image according to a sequence of instructions, enabling more effective interactive visual content creation for users. However, existing methods often exhibit noticeable drift after only a few editing turns, manifesting in two aspects: 1) unstable visual quality, with accumulating artifacts and degraded details; and 2) inconsistent image content, with unintended changes to preserved regions and prior edits. To address these challenges, we propose MT Forcing, a novel training paradigm for multi-turn image editing with unified multimodal models (UMMs) based on autoregressive diffusion. Specifically, we propose Single-Turn Distribution Matching Distillation (Single-Turn DMD), which supervises student self-rollouts with a teacher that applies cumulative edits to the source image in a single turn, providing visual-quality guidance without recursive error accumulation. Additionally, we introduce Teacher-Forcing Guidance, which supervises history-dependent transitions on reference trajectories during warmup and as a regularizer during distillation, encouraging cross-turn content consistency beyond what per-turn distribution matching alone can ensure. Extensive experiments demonstrate that our approach significantly improves the multi-turn image editing capabilities of UMMs, yielding more stable visual quality and stronger cross-turn consistency.

---


### 284. [Spectrum of Liability: Forensically Sound Acquisition of Wireless Evidence for the Reconstruction of Maritime Cyber-Physical Incidents](https://arxiv.org/abs/2610.25411)

**<font color=#1a73e8>作者：</font>** Giacomo Longo, Alessandro Cantelli-Forti, Alessio Merlo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern maritime navigation depends on mandatory wireless inputs, most notably GNSS and AIS, whose reception can be spoofed or jammed. When groundings or collisions occur, liability and safety investigations often turn on whether RF interference corrupted bridge instruments, yet the artifacts typically available (VDR outputs, IBS logs, screenshots, decoded messages) are downstream, lossy, and easy to contest in adversarial proceedings. We introduce a forensically sound acquisition methodology that preserves upstream wireless evidence together with the minimal contemporaneous context needed to interpret it. Our system records coherent, multichannel IQ across relevant bands while simultaneously collecting time-aligned receiver and instrument-state metadata (e.g., decoded AIS/GNSS outputs and NMEA sentences), enabling later re-decoding and physical-layer reanalysis tied to what the onboard stack indicated at the time. To make the record independently auditable, we package samples and metadata into a single append-only forensic envelope that cryptographically binds per-stream hash chains with trusted-time anchors and periodic checkpoints, allowing third parties to detect tampering (modification, truncation, splicing, cross-case substitution) and to verify the claimed recording window. A prototype implementation shows the approach is practical: integrity mechanisms add negligible storage overhead and modest compute cost at operationally relevant multiband capture rates.

---


### 285. [UniState: Unifying Memory and Intervention for Controllable World Simulation](https://arxiv.org/abs/2610.25414)

**<font color=#1a73e8>作者：</font>** Jaeseok Jeong, Kyungmook Choi, Sohyun Chung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models offer increasingly rich environments for exploration, yet intervening in a world while observing the consequences from freely chosen viewpoints remains challenging. We tackle these challenges by introducing UniState, a framework for controllable world simulation built on a unified world-state representation. This representation unifies spatial memory and user interventions. Users specify object motion directly within spatial memory, while independently choosing the camera trajectory from which the resulting world state is observed. This unification makes the relationship between the scene and the requested changes explicit, removing ambiguity between object motion and viewpoint change from the control specification. Crucially, specifying an intervention does not require prescribing every resulting movement: the video model can synthesize additional motion within controlled objects and plausible interactions with their surroundings. We develop training and sampling strategies that help generated videos follow the specified object motion and camera trajectory while preserving this capacity to generate responses beyond the prescribed transformations. Experiments demonstrate more accurate joint object and camera control than the existing methods, alongside qualitative evidence that intervention-induced scene changes persist across rollouts.

---


### 286. [Adaptive Cyber-Defense for Evolving Attacker Capabilities using Reinforcement Learning and Behavior Trees](https://arxiv.org/abs/2610.25420)

**<font color=#1a73e8>作者：</font>** Nicholas Potteiger, Ankita Samaddar, Xenofon Koutsoukos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous cyber-defense agents trained using reinforcement learning (RL) are increasingly adopted for defending enterprise computer networks. However, existing approaches may become brittle as attacker capabilities evolve and enable new attack strategies. In this work, we study the problem of adapting defender policies learned in CAGE Challenge Scenario 2 (CC2), a benchmark enterprise network defense scenario, to an extended network scenario with new attacker capabilities represented by new attacker actions. Effective attack strategies that leverage new actions are initially unknown, and therefore attacker policies must be learned before defender adaptation can occur. To address this challenge, we develop adversarial RL (ARL) with behavior trees (ARLBT), which uses reward behavior trees (RBTs) to define progression-based reward functions and condition attacker policies on RBT execution. The proposed RBT incorporates the new attacker actions into structured attack strategies while leveraging parallel execution to generate rewards across multiple network nodes simultaneously. We evaluate ARLBT for learning attacker policies against two baseline defender policies across network scenarios with different sets of new attacker actions and compare against multiple attacker baselines. The results demonstrate that ARLBT improves attacker success compared to ARL using the original CC2 reward function and that conditioning policies on RBT execution can improve sample efficiency. We further show that defender policies can be adapted against the learned attackers, improving robustness to attacks that leverage new attacker actions.

---


### 287. [Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding](https://arxiv.org/abs/2610.25429)

**<font color=#1a73e8>作者：</font>** Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal alignment of synthetic aperture radar (SAR) imagery to natural language is constrained by two distinct failures. The first is modality mismatch: text encoders pre-trained on optical imagery, such as CLIP, cannot be efficiently fine-tuned on SAR, because active microwave backscatter is physically incompatible with passive optical reflectance and the available SAR caption datasets are orders of magnitude too small to bridge this gap without substantially degrading the learned semantic manifold. The second is physical forgetting: SAR encoders pre-trained on large-scale self-supervised objectives encode radar physics that are progressively erased when the encoder is fine-tuned for text alignment on limited caption data. A single design principle addresses both failures: keep both encoders frozen and learn only a constrained, structure-preserving bridge. Our Frozen Expert framework aligns a frozen CROMA SAR encoder with a frozen CLIP text encoder via a lightweight constrained residual bridge. We formally define physical forgetting via Procrustes disparity and show our bridge preserves SAR geometry significantly better than fine-tuning (disparity: 0.210 vs. 0.351). We validate generality across multiple SAR backbones and text encoders. On zero-shot SAR scene classification, our approach outperforms fine-tuned baselines using up to 8x less training data: DFC2020 (+10.3% R@1, +15.5% mAP), EuroSAT-SAR (+15.7% R@1, +12.2% mAP), BigEarthNet-MM (+14.7% R@1). These results establish frozen manifold alignment as a principled, data-efficient alternative to fine-tuning in high-disparity cross-modal settings.

---


### 288. [RARE: Reinforcement Learning with Adaptive Rubric Evolution for Open-Ended Generation](https://arxiv.org/abs/2610.25434)

**<font color=#1a73e8>作者：</font>** Xueyun Tian, Bingbing Xu, Chuyue Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifiable rewards have advanced reinforcement learning in mathematics and code. However, many valuable open-ended tasks share three properties: no automatic verifier of overall quality, multiple requirements to satisfy jointly, and multiple valid responses to each query. Training therefore needs feedback on requirement satisfaction across different valid responses. Rubric-based reinforcement learning provides this feedback by aggregating scores from explicit criteria. As learning progresses unevenly, some criteria become fully satisfied and lose discrimination while others remain informative. Dynamic methods revise shared rubrics or select evolving criteria to restore discrimination, but may also change useful criteria. To address this, we propose Reinforcement Learning with Adaptive Rubric Evolution (RARE). The core idea is to use current policy feedback to guide both which criteria change and what their replacements assess. Sample-level updates replace criteria fully satisfied across current outputs with checks of remaining quality differences, retaining all other criteria and scores. Within this rule, we compare rewarding desirable qualities with penalizing observed flaws. Video script generation exemplifies these properties and supports content production. Its demands for coherent, executable narratives under constraints make it a challenging testbed. Targeting flaws performs best across three video types with a mean gain of 3.82 points over matched static rubrics. Model and human preferences support these gains. Improvements also extend to writing and general generation benchmarks.

---


### 289. [DragonMoCap: Monocular Video-based Motion Capture for Diverse Dragon Topologies](https://arxiv.org/abs/2610.25437)

**<font color=#1a73e8>作者：</font>** Zhongfei Qing, Xiaoxiang Zhao, Ling-Hao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work explores monocular motion capture for dragon-type characters, which currently relies on manual keyframing due to the lack of high-quality datasets and parametric models. The primary obstacle lies in the extreme topological diversity across dragon rigs, where varying joint counts and naming conventions render traditional fixed-template regressors inapplicable. To address this, we introduce DragonMoCap, a novel framework that treats the target rig as a dynamic input rather than a fixed prior. By deliberately scoping the framework to the most prevalent production topologies, we ensure high-fidelity results across diverse morphologies. The core of our approach is the design of language-grounded joint query tokens, which establish a dual-property representation: ensuring intra-rig discriminability while maintaining cross-rig similarity. We further propose a non-parametric query-token retrieval mechanism to enable zero-shot adaptation to unseen rigs without retraining. Extensive evaluations demonstrate that DragonMoCap consistently outperforms HMR-style baselines across diverse dragon topologies. The practical utility of our framework is further evidenced by its integration into professional animation workflows, highlighting its potential for real-time industrial applications.

---


### 290. [A New Hope for PRNU on Modern Smartphones? Evidence That Device-Specific Fingerprints Survive Computational Photography](https://arxiv.org/abs/2610.25438)

**<font color=#1a73e8>作者：</font>** Benjamin Loison, Quentin Bammey, Thibaud Ehret 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photo Response Non-Uniformity (PRNU) is widely regarded as the most reliable marker for source camera identification. Recent studies, however, report high correlations between images and fingerprints from different modern smartphones, which calls into question the discriminative power of PRNU on these devices. Using 30 recent smartphones under controlled acquisition conditions (e.g., no digital zoom), we investigate whether the fingerprint itself is at fault or the way it is compared. We find that a component shared by all fingerprints of the same model inflates the standard signed peak-to-correlation energy (sPCE). To counter this, we propose $\Delta$sPCE: the sPCE between a query image and a candidate camera's fingerprint, minus the mean sPCE between that image and the fingerprints of the remaining candidates, in the spirit of T-norm score normalization. $\Delta$sPCE improves attribution accuracy, suggesting that the device-specific PRNU signal is still present. Although the limited dataset size and the dependence of $\Delta$sPCE on the candidate camera set currently restrict operational applicability, these results suggest that PRNU-based attribution of modern smartphones remains feasible when fingerprints are compared appropriately.

---


### 291. [UBD-Bench: Benchmarking and Analyzing Unimodal Branch Degradation in Multimodal Perception for Autonomous Driving](https://arxiv.org/abs/2610.25448)

**<font color=#1a73e8>作者：</font>** Ang Liu, Xiang Gu, Ruikai Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal perception improves autonomous-driving performance by combining complementary sensor information. However, stronger multimodal predictions do not necessarily imply stronger representations in each modality-specific branch. Such branch-level weaknesses can remain hidden in conventional output-level evaluation. We introduce UBD-Bench, a systematic benchmark for studying unimodal branch degradation (UBD) in multimodal perception. UBD-Bench uses a Paired Frozen-Branch Probe to compare the task-relevant representation quality of the same modality after independent unimodal training and multimodal joint training under matched decoding conditions. Across four autonomous-driving perception tasks and 10 models, we find that Camera branches consistently degrade after multimodal joint training, whereas LiDAR branches exhibit weaker and more model-dependent changes, revealing a pronounced modality asymmetry. Hierarchical probing further shows that Camera-branch degradation extends from the visual backbone through the Camera-to-BEV pathway and is most severe at the pre-fusion Camera BEV representation. Guided by this diagnosis, we introduce unimodal-to-multimodal distillation at the degraded representation. This intervention consistently improves both Camera-branch Probe performance and full-model performance across all four tasks. These results show that multimodal gains can coexist with degraded unimodal representations, highlighting branch-level representation quality as an important dimension for evaluating and improving multimodal perception.

---


### 292. [Semi-supervised learning on singular data sets](https://arxiv.org/abs/2610.25450)

**<font color=#1a73e8>作者：</font>** Guillaume Valette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose to model singular data clouds by subanalytic sets, and develop an approach to semi-supervised learning in this setting. It relies on a Morrey-type embedding for Sobolev spaces relative to globally subanalytic measures with possibly singular support. As an illustration, we present a greedy method based on a Monte Carlo approximation of the Sobolev norm of the candidate solutions. We report numerical experiments on point clouds sampled from real algebraic varieties, as well as a test on a classification problem based on MNIST images downsampled into $7\times7$.

---


### 293. [On Reasoning Correctness Directions](https://arxiv.org/abs/2610.25464)

**<font color=#1a73e8>作者：</font>** Munachiso Samuel Nwadike, Zayd M. K. Zuhri, Rifo Genadi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present experimental evidence suggesting that information about whether a model's reasoning is on the right track can be linearly decodable without defining a causally useful direction for steering. To study this, we introduce ChainSearch, a controlled arithmetic reasoning task that extends Countdown with explicit search and backtracking. We train a 3-million-parameter model to solve this task. Its compact size allows us to study internal model correctness directions in detail using linear probes, mean activation differences, and direct optimisation, as part of a rigorous search for internal reasoning-correctness directions. We find that while the model contains statistically significant internal directions of reasoning correctness, none of the resulting directions consistently improves reasoning under causal intervention. This calls into question whether the linear representation hypothesis is sufficient for identifying causally useful directions in the context of reasoning. Our code is made available together with this work.

---


### 294. [Near-Optimal Last-Iterate Convergence of SGD in the Smooth Interpolation Regime](https://arxiv.org/abs/2610.25469)

**<font color=#1a73e8>作者：</font>** Matan Schliserman, Tomer Koren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the last iterate of stochastic gradient descent (SGD) with a constant stepsize on smooth convex objectives in the low-noise and interpolation regimes, where the variance $\sigma_\star^2$ of the stochastic gradients at the optimum is small or zero. We establish that after $T$ steps of SGD on $\beta$-smooth convex losses with any constant stepsize $0<\eta<2/\beta$, the last iterate attains expected excess risk $\widetilde O\bigl(\tfrac{1}{\eta(2-\beta\eta)^3T}+\tfrac{\eta}{(2-\beta\eta)^4}\sigma_\star^2\bigr)$, which gives the rate $\smash{\widetilde O(1/T)}$ for every constant stepsize in the interpolation regime ($\sigma_\star=0$), matching the $\Omega(1/T)$ lower bound up to logarithmic factors and improving upon the $O(1/\sqrt T)$ rate of Attia et al. (2026) for $\eta=1/\beta$. Our analysis is based on a new technique, which compares the second moments of the stochastic gradients along the SGD trajectory across only logarithmically many time scales. For quadratic losses in the interpolation regime, an adaptation of this technique gives an $O(1/T)$ rate for every constant stepsize, extending the recent optimal rate for the randomized Kaczmarz method of Derezinski and Dong (2026) to stepsizes above the greedy stepsize with an arguably simpler proof.

---


### 295. [Multimodal-Conditioned Latent Diffusion Models for Spatiotemporal Brain MRI Forecasting](https://arxiv.org/abs/2610.25481)

**<font color=#1a73e8>作者：</font>** Antonio Scardace, Silvia Ingala, Sebastiano Battiato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal forecasting of 3D anatomical changes is a critical generative vision challenge for modeling Alzheimer's Disease (AD) progression. While brain MRI forecasting from single-modality data has advanced, other key complementary multimodal biomarkers remain underutilized. In this work, we propose the Multimodal-Conditioned Latent Diffusion Model (MC-LDM), a novel framework for patient-specific brain MRI synthesis. MC-LDM leverages multimodal biomarkers---MRI, tau-PET, Clinical Dementia Rating (CDR), and APOE4---during training, but relies only on baseline MRI, APOE4, and patient metadata at inference, reflecting realistic clinical availability. Our contributions are threefold: (1) a Latent Diffusion Model (LDM) fine-tuned via Low-Rank Adaptation (LoRA) for data-efficient learning; (2) a multimodal conditioning that integrates molecular and clinical signals to model heterogeneous disease trajectories; and (3) auxiliary predictors estimating unobserved multimodal biomarkers from MRI features and patient covariates to condition the diffusion model, removing the need for these assessments at inference. Trained on 1,355 visits from 852 subjects in the Alzheimer's Disease Neuroimaging Initiative (ADNI), MC-LDM reduces average regional volumetric MAE by 18% over the second-best baseline on an independent test set of 664 visits. To our knowledge, MC-LDM represents the first diffusion-based framework to leverage multimodal priors for MRI forecasting. This conceptual advancement enables patient-specific trajectory generation that captures aspects of AD heterogeneity not observable from structural anatomy alone, bridging the gap between rich multimodal supervision and the strict constraints of routine clinical deployment. Code is available at: this https URL.

---


### 296. [PCXR-Copilot: Device-aware pediatric chest radiographic analysis with segmentation, suppression, and edema-related cues](https://arxiv.org/abs/2610.25486)

**<font color=#1a73e8>作者：</font>** Xueyang Li, Alec Girten, Peng Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patients admitted to pediatric ICU and cardiac ICU often require intensive perioperative support and frequent chest radiography to monitor support devices, extravascular lung water, and body-wall edema. Radiographic interpretation and analysis is often difficult due to superimposed anatomic and iatrogenic structures that obscure clinically relevant signals. While deep learning can provide decision support, translation to pediatric radiographs is still limited by high device burden and scarcity of pediatric datasets with clinically grounded device annotations. To address this gap, we first introduce PediaDeviceSeg-1K, a curated dataset of 1,000 anterior-posterior radiographs of pediatric CICU patients with clinically grounded, fine-grained annotations of common ICU devices. To our best knowledge, this is the first publicly available pediatric CICU CXR resource with clinically grounded device annotations for device-focused benchmarking. Building on PediaDeviceSeg-1K, we further present PCXR-Copilot, a device-aware pipeline that outputs lung and device masks, optional device-suppressed views, and edema-related visualization maps and scalar indices. The full pipeline has been integrated and runs in real time within the TWIST platform at Boston Children's Hospital, demonstrating feasibility for real-world clinical deployment.

---


### 297. [SlimFormer++: Token Mixing Where It Matters for Efficient 3D Medical Image Segmentation](https://arxiv.org/abs/2610.25488)

**<font color=#1a73e8>作者：</font>** Yang Hong, Lei Zhang, Zhihong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To determine where computation is needed in volumetric segmentation networks, we analyze block-level redundancy and stage-wise token-mixer contribution. Centered Kernel Alignment reveals high input-output representational similarity within blocks of representative convolutional, hybrid, and Transformer-style segmentation networks. Similarity-guided pruning reduces their parameter counts by 39-75% while decreasing mean Dice by less than 0.4 percentage points. To examine token mixers within blocks, we introduce Anatomical Relation Distortion, which quantifies how bypassing a mixer distorts feature relations between labeled anatomical positions. Applied to an unpruned candidate architecture, Centered Kernel Alignment indicates high representational redundancy in intermediate encoder mixers, whereas Anatomical Relation Distortion shows that they contribute little and the bottleneck mixer most. These findings motivate SlimFormer++, which uses Selective Mixing blocks with windowed Mamba mixing in the first encoder stage and only residual channel MLPs in deeper stages. At the bottleneck, Augmented Mixing injects similarity-weighted sparse long-range context into the axial taps of a depthwise convolution at cost linear in voxel count. Evaluated against 12 baselines across eight public CT, MRI, and ultrasound datasets (1,809 cases), SlimFormer++ achieves the highest mean Dice (87.84%) and lowest mean HD95 (6.50 mm) with the fewest parameters (5.98 million). These results support stage-aware token mixing as a design strategy for improving the accuracy-efficiency trade-off in volumetric segmentation. The source code is available at this https URL

---


### 298. [Probabilistic Limit Order Book Forecasting with Conditional Diffusion Models](https://arxiv.org/abs/2610.25495)

**<font color=#1a73e8>作者：</font>** Junyu Chen, Franklin Liu, Moshu Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling limit order book (LOB) dynamics is central to market forecasting and execution-strategy evaluation. While diffusion models achieve strong empirical performance, existing LOB snapshot models typically lack a learned recurrent encoder and formal statistical guarantees. We introduce LOBGrad, a conditional DDPM framework for probabilistic LOB forecasting that combines an autoregressive RNN encoder with a diffusion-based generator. In particular, we establish an excess-risk oracle inequality for the one-step DDPM noise-prediction objective under exponential mixing and regularity assumptions. We further show that, under contractive dynamics, the dependence on the conditioning-window length can be reduced to a dependence on the latent-state dimension. Experiments on BTC/USDT, GOOGL, and META show that LOBGrad improves on its encoder-free diffusion ablation across all reported queue metrics and obtains competitive results against other baselines. It also reproduces the key stylized facts of LOB microstructure, and yields reasonably calibrated queue-based predictive intervals. A stylized downstream task illustrates the potential value of the generated forecasts.

---


### 299. [From Proposal to Execution: Modeling Interaction Semantics in Shared Autonomy](https://arxiv.org/abs/2610.25496)

**<font color=#1a73e8>作者：</font>** Shashank Shekhar, Laurent Jeanpierre, Abdel-Illah Mouaddib  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In many human-AI systems, candidate actions are not executed directly but are first evaluated by another decision-making entity under a potentially different objective or decision model. Standard decision-theoretic frameworks do not require this interaction to be represented explicitly, as they define transition dynamics directly over state-action pairs, allowing evaluation to be absorbed within the transition model. We introduce a semantics-aware decision framework in which a candidate action is proposed, evaluated under an interaction context, and then resolved into an executed outcome. We formalize this through a joint action language and an interpretation function that maps each joint action and context to a semantic outcome. Transition and reward dynamics are induced through these semantic outcomes, thereby introducing an explicit representational layer for \textit{interaction semantics}. Semantic outcomes provide explicit units for organizing interaction principles, which can be instantiated through application-specific evaluation mechanisms and reused across distinct interaction instances. This provides a structured interface for specifying context-dependent evaluation separately from the resulting execution dynamics, without requiring changes to the underlying planning algorithm. We instantiate the framework in shared human-AI autonomy, capturing interaction patterns such as advisory and authorization, and illustrating how interaction context influences decision making. The resulting formulation remains compatible with standard Markov decision process (MDP) planning.

---


### 300. [Assessing the AI Readiness of Construction Datasets: A Multidimensional Operational Framework](https://arxiv.org/abs/2610.25499)

**<font color=#1a73e8>作者：</font>** Xiaoyu Hou, Bo Xiao, Abdolmajid Erfani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of artificial intelligence (AI) applications in construction has increased the demand for datasets suitable for reliable model development, evaluation, and reuse. However, construction datasets vary widely in documentation, quality, governance, and evaluation support, and consistent criteria for assessing AI readiness remain limited. This study develops a Construction Dataset AI Readiness Framework with 30 attributes across four dimensions: Metadata Completeness, Data Quality and Representativeness, Data Governance and Accessibility, and AI Utility. The framework uses attribute-specific scoring, applicability screening, and automated and manual verification. It was evaluated using 21 publicly available datasets across seven data-type groups. Overall readiness scores ranged from 0.720 to 0.964, with a mean of 0.879. Hybrid verification achieved 90.5% agreement between automated suggestions and manually verified scores. The framework supports consistent assessment of heterogeneous construction datasets and identification of readiness gaps.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
