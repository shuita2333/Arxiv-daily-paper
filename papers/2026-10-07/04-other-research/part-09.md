# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 401. [Certification of Real Images through Calibrated Content Authentication](https://arxiv.org/abs/2610.05870)

**<font color=#1a73e8>作者：</font>** Sarim Hashmi, Abdelrahman Elsayed, Mohammed Talha Alam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models can synthesize high-quality inauthentic multimedia content that is already being misused at scale. We evaluate twenty deepfake detectors against ten generators released in the last four years and find accuracy decreasing over time, from near-perfect 99.5% to 76%. Adversarial perturbations further reduce every baseline detector to below 2% accuracy, effectively inverting the detector's assigned label. We argue that this unreliability reflects a fundamental ambiguity: generators can reproduce authentic content exactly (e.g., through memorization), so content alone cannot reveal the true provenance this http URL this reason, content produced by a generator must admit a faithful reconstruction by that same generator, and finding such a reconstruction makes synthetic provenance plausible and authenticity plausibly this http URL therefore propose and evaluate a detection paradigm that outputs a calibrated prediction of whether authenticity is plausibly deniable: a faithful reconstruction by any known generator establishes plausible deniability, while calibration bounds how often content from known generators fails to be reproduced. Our evaluation shows that (i) our detector can be calibrated so that at most 1% of generated content is wrongly certified, an operating point at which most baseline detectors reach near-zero recall, including the strongest with 93% accuracy; (ii) calibrating a stricter security threshold on attacked samples preserves this bound against adaptive adversaries within the evaluated bounded-perturbation attack space, whose perturbations break every baseline, but does not cover arbitrary adversarial transformations; and (iii) post-hoc verifiability is eroding, as 1,116 of 3,000 Reddit images resist reproduction by a 2022 generator, but only 55 to 79 resist reproduction by 2024 generators.

---


### 402. [Off-Policy Merging Beats On-Policy Self-Distillation for Continual Learning](https://arxiv.org/abs/2610.05872)

**<font color=#1a73e8>作者：</font>** Chen Henry Wu, Thomas Zhang, Aditi Raghunathan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A long-standing goal of AI is a model that can continually learn and improve itself. On post-trained models, supervised finetuning (SFT) on new data often causes poor generalization and catastrophic forgetting. As such, the conventional wisdom is that on-policy training is a prerequisite for continual learning. In practice, however, data containing new knowledge or capabilities are often off-policy. While methods such as on-policy self-distillation (OPSD) try to bridge this gap by converting off-policy data into on-policy signal, they have been shown to cause reasoning collapse. In this paper, we show that off-policy merging beats OPSD for continual learning. We first show that SFT learns a useful signal from new data, but naively applying its update interferes with existing capabilities. We reduce this interference with a simple recipe we term grafting, which changes where the update is learned and how it is applied: (1) learning the update on an earlier donor checkpoint, ideally even before the end of pretraining, and applying the weight update to the post-trained model; (2) scaling the weight update, equivalent to a form of model merging; and (3) optionally, masking the most sensitive update directions when the new data distribution is far from the post-trained model. Across continual learning settings including (1) distilling from expert traces, (2) self-improvement with STaR and Pedagogical RL, and (3) injecting knowledge after pretraining cutoff, grafting Pareto-dominates both SFT and OPSD in new-task and old-task performance, while avoiding expensive on-policy sampling. Therefore, our work challenges on-policy training as a necessity for continual learning on RL-trained models.

---


### 403. [fMRI-TAMCL: Text-Anchored Supervised Multimodal Contrastive Learning for fMRI-Based Brain Disorder Classification](https://arxiv.org/abs/2610.05880)

**<font color=#1a73e8>作者：</font>** Juliana Mantebea Danso, Enoch Opanin Gyamfi, Mylene C.Q. Farias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resting-state fMRI is important in the classification of brain disorders, but highly multimodal and exhibits strong multisite heterogeneity. Existing methods fuse images, BOLD-based functional connectivity, and phenotypic data modalities. Unlike other medical imaging datasets, rs-fMRI datasets rarely include a text modality, so they are generated from phenotypic data or BOLD activations. These text generation methods rely on fixed assumptions for subjects, sites, devices, and protocols, leading to poor generalization across datasets. We propose fMRI-TAMCL, a text-anchored multimodal contrastive learning framework that integrates fMRI images, sparse FC, and generated subject-specific text. Its Subject-Adaptive Threshold Derivation module generates BOLD activation text, while Feature-Value Serialization module generates phenotypic text. All three modalities are encoded as clustered graphs, projected onto a shared unit hypersphere space, aligned using pairwise, text-anchored supervised contrastive learning, and fused with attention. fMRI-TAMCL proves its generalization capability across five datasets outperforming 29 baselines with 78.6%-86.4% accuracy in downstream classification.

---


### 404. [Spatial Supervision Without Attribution Optimization: Improving Post-Hoc Class Activation Maps via Box-Guided Evidence Routing](https://arxiv.org/abs/2610.05891)

**<font color=#1a73e8>作者：</font>** Wenhao Liang, Liangwei Nathan Zheng, Lin Yue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc class activation maps (CAMs) are a standard tool for inspecting the evidence behind an image classifier's predictions, yet nothing in ordinary training encourages these maps to be spatially appropriate. We study whether inexpensive spatial supervision can improve a classifier's own predicted-class Grad-CAM without ever optimizing an attribution map. Box-Guided Evidence Routing (BGER) trains a lightweight gate on the final feature map under box or mask supervision and routes classification through the gated features, while Grad-CAM is computed separately at the pre-gate representation, so the evaluated map never enters the training objective. With a BCE routing loss, BGER raises MaxBoxAccV2 from $0.584$ to $0.715$ on CUB-200-2011 and from $0.757$ to $0.832$ on Stanford Dogs at comparable accuracy. Matched controls attribute most of the ResNet-50 gain to the spatial supervision reshaping the backbone rather than to routing itself: when classification bypasses the gate, most of the improvement remains, and detaching gradients through the gate leaves the ResNet-50 result nearly unchanged. The same detachment preserves most of the gain in two DenseNet-121 chest X-ray settings but removes the apparent gain on Swin-T, and directly supervising the CAM reaches stronger localization at a larger accuracy cost. Overall, spatial supervision can improve separately evaluated post-hoc CAMs, but both the mechanism and the size of the benefit depend on the architecture and the evaluation setting.

---


### 405. [TasteRoute: Personalized Routing for Video Generation](https://arxiv.org/abs/2610.05896)

**<font color=#1a73e8>作者：</font>** Zhi Rui Tam, Chao-Chung Wu, Sin-Han Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid progress in video generation has led to a plethora of models that differ substantially in capability and generation cost. This raises a natural question: can each request be efficiently routed to an appropriate model? We find that even when the consensus of the other annotators is used as an oracle, it agrees with each annotator's own favorite only 34-55% of the time. Motivated by this observation, we introduce TasteRoute, a personalized video-generation router that selects a generator jointly based on the input request, user preferences, and available generation budget. Across text-to-video and image-to-video settings, TasteRoute is competitive with strong simple baselines on preference routing while reducing average generation cost. The cost saving increases under higher budget caps. Finally, we release TasteRoute-3k, a human-annotated dataset containing multi-model video comparisons, quality judgments, preference rankings, and user-profile signals to facilitate future research on personalized and cost-aware video routing.

---


### 406. [LoDEOT: Low-Dimensional and Efficient Offset Tokens for Building Footprint Extraction from Off-Nadir Imagery](https://arxiv.org/abs/2610.05899)

**<font color=#1a73e8>作者：</font>** Kai Li, Zigan Zhou, Zhenyang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance-level roof-to-footprint offset (RFO) prediction is central to extracting building footprints from off-nadir imagery. Query-based pipelines commonly use high-dimensional instance tokens to predict signed two-dimensional RFOs. We investigate whether RFO prediction can instead use a compact offset token. Under local pinhole projection and vertical-extrusion assumptions, the idealized RFO map admits a five-parameter sufficient descriptor comprising intrinsic shape, composite amplitude, and relative geometry. This factorization provides a structural prior for a five-dimensional offset token, whose channels learn task-relevant latent representations through end-to-end training. Based on this design, we propose LoDEOT, which retains high-dimensional instance tokens for detection and segmentation but maps instance-token, concentration-gated roof, and box-mask evidence to a five-dimensional offset token followed by an independent two-dimensional readout. Known denoising-query target indices further align each supervised decoder-layer estimate with the same clean instance RFO, organizing successive predictions as target-aligned recovery under perturbed query conditions. Experiments on five real-world building datasets demonstrate the effectiveness of LoDEOT for building footprint extraction. Experiments on real-world building datasets demonstrate that a five-dimensional offset token can support accurate RFO prediction. On BONAI, LoDEOT achieves the best roof-detection bAP and bAP50 and leads all five offset-corrected footprint metrics among the evaluated end-to-end methods, with FAP50 of 54.58 and mEPE of 5.23 pixels. Its FAP50 exceeds those of the evaluated end-to-end baselines by 7.56-16.85 percentage points.

---


### 407. [End-to-End Autonomous Recursive Arborescence Deformable Flow and Non-Linear Hemodynamics for Patient-Specific Coronary Centerline Extraction](https://arxiv.org/abs/2610.05900)

**<font color=#1a73e8>作者：</font>** Zeyu Jia, Xin Ming  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting patient-specific vascular trees from volumetric medical images is fundamental to computational angiography and non-invasive hemodynamic assessment. Conventional voxel segmentation models often sever delicate bifurcations, while heuristic Euclidean Minimum Spanning Trees introduce non-anatomical shortcuts. Moreover, linear Poiseuille flow neglects quadratic kinetic dissipation across arterial narrowings, underestimating ischemia. We formulate an end-to-end framework decoupling continuous geometric arborescence generation from non-linear hemodynamics. First, an autonomous 3D Ostium Landmark Localization Head with dual-sinus query channels and spherical-gated refinement eliminates centerline seeding dependency, achieving cohort mean localization error of 7.63 mm (7.43 mm LCA, 7.83 mm RCA; 71.4% <= 8.0 mm) from raw contrast context. Second, a Spatially-Grounded Deformable Step Flow Architecture queries continuous 3D feature pyramids via trilinear sampling, sequentially generating trajectories with anchor boundary enforcement (X(0) = P_start). Third, a Top-Down Recursive Arborescence State Machine detects bifurcation peaks via Tree-NMS and parameterizes predecessor parent pointers (p_k < k), guaranteeing single connected acyclic tree topology (beta_0 = 1, beta_1 = 0) with differentiable step termination. Fourth, an iterative Picard non-linear Kirchhoff solver with Young-Tsai / Gould quadratic dissipation enforces machine-precision mass conservation (residual 5.82e-11 mL/s). Across 14 development patients under standardized in-silico stenosis stress testing (Q_0 = 4.0 mL/s), linear Poiseuille flow misclassifies 75% diameter lesions as non-ischemic (FFR > 0.80) in 14/14 cases, whereas our non-linear solver captures functional ischemia (FFR = 0.5864, lesion disparity 32.89 mmHg, p = 6.10e-5) with 3.66x collateral shunting. Test set firewall isolation was maintained.

---


### 408. [On Hyperparameter Tuning on the Test Set](https://arxiv.org/abs/2610.05902)

**<font color=#1a73e8>作者：</font>** Matteo Fregonara, Tom Viering, Jan van Gemert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> "Don't tune hyperparameters on the test set" is often stated in machine learning textbooks. Violating it is considered a cardinal sin that produces misleadingly optimistic results, corrupts benchmark integrity, and thus can even be interpreted as scientific fraud. Yet evidence suggests that test set hyperparameter tuning does occur in practice, making it all the more important to understand its actual consequences. So how bad is it, really? In this work we question this dogma and put it to an empirical test. We systematically study the magnitude of the performance inflation caused by tuning the hyperparameters on the test set for MNIST-1D, CIFAR-10, and three tasks from the GLUE benchmark. Our experiments show that while the effect is real and significant, it is frequently small relative to other sources of noise. In many cases, we find that tuning on the test set recovers exactly the same model as when tuning on the validation set. Most importantly, we find that the rankings of models remain essentially preserved after tuning on the test set and therefore that consistent test-set tuning may not invalidate benchmarks or model selection. Our results call for a more nuanced view of tuning hyperparameters on the test set, stimulating researchers to openly report test tuning.

---


### 409. [Safe Image Generation via Reinforcement Learning](https://arxiv.org/abs/2610.05908)

**<font color=#1a73e8>作者：</font>** Eungyeol Han, Jong-Seok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Text-to-Image (T2I) models achieve remarkable visual image generation performance, but they can still generate NSFW (Not-Safe-For-Work) contents, including violent or explicit images. Existing safety checker mechanisms are largely confined to pre-generation filtering (e.g. prompt-level text classifiers) or post-hoc moderation applied after an image is completely synthesized. However, adversarial attack methods operate over a much broader space. This imbalance highlights the need for a safety mechanism that intervenes during the generation process. We propose an in-generation safety framework that monitors the denoising trajectory and detects emerging NSFW signals from intermediate representations. Rather than merely detecting NSFW generations, our method applies reinforcement learning to generate safe images from NSFW prompts. By coupling in-generation detection with controllable steering, our approach mitigates unsafe trajectories even when NSFW signals emerge after generation has already begun. Experiments results show that our method consistently outperforms existing safe image generation methods across both standard and adversarial evaluation sets, while preserving perceptual quality and prompt fidelity. Code will be released upon acceptance.

---


### 410. [Every View Counts: View-Consistent Panoptic Quality for Multi-view Panoptic Segmentation](https://arxiv.org/abs/2610.05911)

**<font color=#1a73e8>作者：</font>** Youngmin Lee, Byungha Ko, Guhnoo Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view panoptic segmentation assigns a semantic class and a scene-level instance ID to every pixel of an unordered set of images, and recent feed-forward 3D models predict these labels for the input views in a single forward pass. Their predictions, however, have been evaluated with the scene-level PQ (PQ^scene) borrowed from per-scene optimization methods, typically on rendered held-out views. PQ^scene tiles all views of a scene into a single image, so that a missed appearance or a change of ID lowers the score of the matched pair only in proportion to its area. We propose View-Consistent Panoptic Quality (VC-PQ), which extends PQ from a single image to a set of input views, counts equally every view in which an instance is visible, and penalizes a prediction that is not visible in the same views as its ground truth. A decomposition of VC-PQ attributes the score a method loses to mask accuracy, view consistency, and the matching threshold. A single additional parameter recovers the area weighting of tiling for comparison. Under a fixed evaluation protocol on ScanNet++ and ScanNetv2, recent feed-forward methods are evaluated with VC-PQ and PQ^scene, and the decomposition shows where each of them loses its score. Controlled perturbations of the ground truth show that VC-PQ responds to the number of views in which an instance is missed or changes ID, whereas PQ^scene responds to their area. The aim of this work is to make view consistency part of the evaluation of multi-view panoptic segmentation, with VC-PQ reported alongside PQ^scene.

---


### 411. [MiniCorp: The Last Mile of the AI Agent Firm](https://arxiv.org/abs/2610.05912)

**<font color=#1a73e8>作者：</font>** Jingying Zeng, Zhenwei Dai, Jinning Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The last mile toward enterprise AGI is a company that runs itself. Training and adapting such agents require longitudinal enterprise data, which remain scarce, costly to acquire, and often restricted by privacy constraints. Historical archives are also frequently incomplete and record only what actually happened. They cannot show the outcomes of alternative decisions. We introduce MiniCorp, an office simulator for studying how agents can collectively run a company while generating enterprise data at scale. Using an e-commerce company as a demonstration, MiniCorp connects two interacting worlds. The external world models customers, dynamic competitors, and market mechanisms. The internal world consists of agents that observe events, discuss their options, and make strategic decisions. These decisions have lasting effects on the market, and the resulting feedback informs the firm's later decisions. As the firm and market interact, MiniCorp continuously records the agents' communications and decisions. These records preserve the information available at the time and the business results that followed. Checkpointing allows the same situation to be replayed under different decisions, providing comparisons unavailable in static archives. We evaluate end-to-end fidelity against patterns reported in empirical studies of real markets. These evaluations provide agents with realistic market feedback and reduce the risk that they learn to exploit flaws in the simulator. Our experiments show agents coordinating across roles and adapting their decisions to market feedback. With explicit long-term strategic guidance, they also sustain advertising exploration despite weak early returns. MiniCorp thus provides an environment for studying AI-run companies and a scalable source of longitudinal and counterfactual enterprise data for agent training and evaluation.

---


### 412. [CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI](https://arxiv.org/abs/2610.05913)

**<font color=#1a73e8>作者：</font>** Boseong Kim, Haejun Chung, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task-fMRI connectomes reveal state-dependent neural reconfigurations, yet conventional methods marginalize these signals by aggregating distinct conditions into static pairwise graphs, thereby obscuring condition-specific multi-ROI organization. We introduce CoHyFuse, a condition-aware ROI-centered hypergraph framework that constructs a task-state-specific incidence matrix from condition-wise functional connectivity (FC)-profile embeddings, allowing the same ROI to form different multi-ROI hyperedges across task phases. Condition-specific neighborhood sizes $K_q$ further adapt the hyperedge scale to each task state, and the resulting condition embeddings are fused with a complementary whole-session FC branch for prediction. In the AABC cohort (N=1,074), CoHyFuse achieved the best mean out-of-fold predictive performance among evaluated baselines on FACENAME Fluid Cognition Composite (FCC) prediction (7.83$\pm$0.10 MAE, 0.439$\pm$0.026 \(R^2\)) and VISMOTOR age prediction (7.52$\pm$0.37 MAE, 0.592$\pm$0.022 \(R^2\)). In an auxiliary CMI-HBN attention-deficit/hyperactivity disorder (ADHD) classification benchmark (N=223), CoHyFuse obtained 72.0$\pm$2.1\% macro-AUC and 74.2$\pm$2.9\% accuracy. Ablation studies support the contributions of condition-wise incidence construction and dual-view fusion, suggesting that state-resolved ROI-set structure provides complementary predictive information beyond whole-session FC alone. Occlusion analysis identifies the Distraction condition as the primary driver of model prediction, pointing toward the Salience/Ventral Attention Network (SAN)--FrontoParietal Network (FPN) and within-SAN hyperedge-defined ROI-set motifs as candidate model-relevant patterns. This framework provides an interpretable, state-resolved view of the connectome for downstream cohort analysis.

---


### 413. [Large Stepsizes Federated Learning on Logistic Regression with Linearly Separable Data: The Case of Heterogeneous Devices](https://arxiv.org/abs/2610.05915)

**<font color=#1a73e8>作者：</font>** Hok Fong Wong, Hoi-To Wai, Chung-Yiu Yau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper revisits the distributed learning problem for training a multinomial logistic regression model with the Federated Averaging ($\texttt{FedAvg}$) algorithm. We concentrate on a scenario with arbitrarily large stepsizes and heterogeneous update rules where the devices may perform a different number of local updates in each round. We show that, with linearly separable data, $\texttt{FedAvg}$ is stable with any stepsizes and the objective values converge to zero at the rate of ${\cal O}(1/R)$, where $R$ is the number of communication rounds. Our result also demonstrates that the effects of device heterogeneity vanish asymptotically. For sufficiently large $R$, the objective values decrease monotonically and is bounded by ${\cal O}( 1 / (R T_{\rm avg}))$, where $T_{\rm avg}$ is the average number of local update steps per communication round across devices. Numerical experiments support our findings.

---


### 414. [Prompt and Refinement: Asymmetric Mutual Learning for Infrared Small Target Detection with Noisy Labels](https://arxiv.org/abs/2610.05918)

**<font color=#1a73e8>作者：</font>** Yimin Fu, Songbo Wang, Lizhuo Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing data-driven infrared small target detection (ISTD) methods typically require large-scale datasets with accurate pixel-level annotations for model training. However, such labor-intensive requirements are difficult to satisfy in real-world applications due to the heavy reliance on expert knowledge and the inherently weak distinctiveness of infrared small targets. Consequently, the presence of noisy labels during model training is inevitable, which can severely mislead the learning of target perception toward spurious patterns. To address this challenge, we propose Prompt and Refinement (PAR), a label-noise-robust asymmetric mutual learning paradigm for ISTD. Specifically, PAR comprises a pretrained Segment Anything Model (SAM) and an ISTD-specific detector trained from scratch, which learn collaboratively through a peer-teaching scheme. Coupled with local contrast regularity, the predictions of the two asymmetric peer models are mutually exploited as rectification cues for the supervisory masks of their counterparts. The interaction between complementary inductive biases effectively prevents the label correction process from degenerating into the self-confirmation loop of a single model, enabling progressive refinement of the annotations toward intrinsic target characteristics. In addition, the detector predictions are utilized as corrective mask prompts to facilitate task-specific adaptation of the vision foundation model. Moreover, an evidential uncertainty estimation strategy is introduced into the optimization process to further alleviate the adverse effects of noisy labels. Extensive experiments under diverse noisy label scenarios on three ISTD datasets demonstrate that PAR consistently achieves state-of-the-art performance.

---


### 415. [Non-invasive Seizure Detection Using Wearable Wrist-worn Accelerometry and Deep Learning](https://arxiv.org/abs/2610.05919)

**<font color=#1a73e8>作者：</font>** Nilushika Udayangani Hewa Dehigahawattage, Kishor Nandakishor, Marimuthu Palaniswami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Seizure monitoring and detection are crucial for reducing the morbidity and mortality associated with seizures. Current epilepsy care, often involving expensive video-electroencephalography (VEEG) monitoring, requires specialized expertise and is limited to in-hospital settings, and intrusive in nature. Seizure diaries, on the other hand, suffer from unreliability due to under-reporting, leading to incorrect therapeutic decisions. Wearable non-invasive seizure detection may offer a more tolerable and feasible solution for long-term ambulatory monitoring. This study explores a wearable remote monitoring system utilizing a single wrist-worn accelerometer device and capable of detecting multiple types of seizures, including shorter duration events. We enrolled 79 patients under video-electroencephalography monitoring to wear accelerometer devices and collect data. Concurrent VEEG recordings were reviewed by board-certified epileptologists to produce annotations, including seizure onset, offset, and seizure type. Using this data, we constructed a deep neural network based on the time-series ResNet architecture, which could discriminate among seizure and non-seizure events. Our proposed approach achieved a seizure detection sensitivity of 95.65% and an overall false alarm rate of 0.15/24 hours during the evaluation, which spanned 5576 hours of total recording. Additionally, it resulted in an area under the receiver operating characteristic curve (AUC-ROC) of 0.98 and an area under the precision-re call curve (AUC-PRC) of 0.67 when averaged over 20 patients who experienced 46 convulsive seizures. These promising results suggest that the proposed seizure detection system can be effectively used for long-term ambulatory seizure monitoring. Future steps include validating our findings in larger datasets and assessing the utility of detection for additional seizure types.

---


### 416. [Beyond Transport Cost: Routing Differences between Flow Matching and Optimal Transport](https://arxiv.org/abs/2610.05921)

**<font color=#1a73e8>作者：</font>** Eungyeol Han, Jong-Seok Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In generative models, Optimal Transport (OT) is used to improve Flow Matching (FM) by reducing noise-data coupling cost. However, different noise-to-output assignments can yield nearly equal costs, raising a key question. Is cost alone sufficient to guide coupling design? We address this question by separating transport cost from routing, i.e., the destination reached by each noise sample. We show numerically how FM and OT can differ in routing while remaining close in cost. We examine its consequences in learned neural FM. Using the exact FM routing as an oracle, we further construct a routing-aware training coupling and find that it yields a directionally consistent improvement in generation over a cost-matched, cost-only counterpart. Our findings highlight what cost minimization can overlook and motivate using both cost and routing to evaluate the design of OT-based FM couplings. Code will be released upon acceptance.

---


### 417. [VERA: Scaling Verifiable Environments for Agentic co-Evolution](https://arxiv.org/abs/2610.05923)

**<font color=#1a73e8>作者：</font>** Junqi Liu, Yongyang Pan, Zhuosong Jiang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Competent agents need precise and verifiable environments, such as sandboxes that are resumable at any stage and evolve from observable evidence. However, most long-horizon work exposes how rare these are: for example, an agent in medical research must ground a finding, classify it, and write a report over dozens of dependent steps, yet recent environments score only the outcome. To address the challenges in stable training, we present VERA, which builds such environments at scale and lets agents evolve on them. VERA builds these environments from initial trajectories: an agent writes rubrics, executable checks, a judge verifies each sandbox, and only those that pass enter the training bank. On these environments, VERA alternates between two updates: train the model with rubric rewards, or edit the harness skills. We also create a verifier which gates model checkpoints and harness edits using explicit development-set acceptance criteria. This attribution distinguishes VERA's co-evolution from single-axis baselines: its updates target not only the cause but the outcome. With an open-source corpus of 9,000+ long-horizon verifiable environments, a 9B model paired with its co-evolved agent beats the strongest baseline by 10.3 and 13.0 points in the two domains. At 27B, it surpasses the baseline on AutoCoWorkBench (71.6) and AutoMedBench (80.7), transfers to unseen workflows, and retains general capabilities.

---


### 418. [UltraDub: Towards Authentic Dubbing by Unifying Visually-Steered Flow Learning and Trajectory Guidance](https://arxiv.org/abs/2610.05932)

**<font color=#1a73e8>作者：</font>** Gaoxiang Cong, Liang Li, Jianwei Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual voice cloning requires intelligible, speaker-consistent speech synchronized with visible articulation. However, sequential multimodal conditioning can disrupt previously established temporal and speaker cues, while imbalanced inference guidance can improve linguistic accuracy at the expense of lip synchronization. In this paper, we propose UltraDub, a Unifying Visually-Steered Flow learning and trajectory Guidance Dubbing framework that leverages vision in two ways: as continuous motion for multimodal context aggregation, and as structural rhythm for trajectory rectification. Specifically, we introduce the Motion-guided Dual-context Retrieving (MDR) module, which continually recalibrates linguistic and speaker-style retrieval through shared lip-motion query residuals, utilizing independent time-conditioned gates to regulate their contributions. Furthermore, we propose Rhythm-anchored Trajectory Guidance (RTG), a training-free mechanism that evaluates hierarchical multimodal corrections at a visual-only predictive midpoint, safely strengthening semantic conditioning while better preserving temporal alignment. Finally, we construct DiverseDub, a multi-scenario benchmark to evaluate video dubbing in the wild. Extensive experiments demonstrate that UltraDub achieves state-of-the-art performance across four datasets.

---


### 419. [Process Constitutions and Process Stewards: Towards the Next Generation of BPM for Agentic Organizations](https://arxiv.org/abs/2610.05942)

**<font color=#1a73e8>作者：</font>** Amin Jalali, Majid Rafiei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Business Process Management (BPM) was built on a foundational assumption that organizations are populated primarily by human actors whose work can be made visible, governable, and improvable through process models. That assumption is depreciating. AI agent ecosystems increasingly execute, coordinate, and adapt organizational work with limited human direction, challenging not only BPM's methods but its core conception of what a process is. We argue that BPM faces a constitutive shift from modeling human work to governing autonomous agents, for which we propose two new concepts: the \emph{Process Constitution}, a machine-interpretable, value-laden framework that defines the space of admissible agent behavior, and the \emph{Process Steward}, a governance agent that interprets and enforces it. The central value proposition of this new generation of BPM is not efficiency but \emph{organizational legibility}: the capacity to keep agentic organizations accountable, contestable, and humanly understandable. We outline what this means and sketch the research agenda it opens.

---


### 420. [OntoInk: Interactive Ontology Visualization, Validation, and Reasoning](https://arxiv.org/abs/2610.05945)

**<font color=#1a73e8>作者：</font>** Ebrahim Norouzi, Jörg Waitelonis, Harald Sack  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology documentation, visualization, and validation are usually carried out with separate tools. This split workflow slows down development and makes knowledge transfer harder. We present OntoInk, an open-source MkDocs plugin that brings these activities together. Within a single documentation-as-code pipeline, OntoInk renders interactive ontology diagrams, validates instance data against SHACL shapes, runs OWL\,DL reasoning, and supports inline Turtle editing. General-purpose diagram plugins for MkDocs cannot parse RDF, dereference IRIs, overlay SHACL constraints, or run OWL reasoning. Compared with standalone ontology visualization tools, OntoInk embeds interactive and editable diagrams directly into documentation pages. A live demo and source code are available at \url{this https URL}.

---


### 421. [Technical Report on the Turba Fertilizer Machine Learning Stack in Morocco](https://arxiv.org/abs/2610.05949)

**<font color=#1a73e8>作者：</font>** Abdelghani Belgaid, Zakaria Mahmoud, Fahd Chibani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Site-specific fertilizer recommendation systems adapt nutrient advice to location, soil properties, crop type, and production targets, but scientific reuse is constrained when recommendation functions remain accessible mainly through interactive interfaces, outputs are not versioned, and trained approximations cannot be independently loaded or benchmarked. This technical report presents the Turba fertilizer machine learning stack, a three-layer open-source implementation for reproducible site-specific fertilizer recommendation in Morocco. \texttt{turba-client} provides programmatic access to publicly accessible site profiles, crop-specific target-yield spaces, and N, P$_2$O$_5$, and K$_2$O recommendation workflows; \texttt{turba-data} distributes analysis-ready snapshots; and \texttt{turba-models} packages crop-specific machine learning surrogates of recommendation outputs. The architecture links upstream retrieval, versioned analytical snapshots, reproducible cross-model benchmarking, and loadable offline surrogates while preserving the distinction between recommendation-system outputs, observed agricultural data, and model-generated predictions. The first dataset was constructed from 44,096 unique ESA WorldCereal locations. Scenario expansion across supported cereal workflows generated 132,017 crop-location recommendation requests under a medium target-yield setting. The resulting 22-variable dataset spans 10 regions, 66 provinces, and 1,149 communes. Nine regression families were evaluated under a fixed deterministic 80/20 protocol, and the current release packages five best-performing crop-specific models. The machine learning task is recommendation-function emulation rather than prediction of observed crop response. The stack provides a reproducible basis for spatial and temporal validation, uncertainty estimation, field-trial comparison, and future integration with additional data.

---


### 422. [Physics-Informed but Not Physics-Consistent: Error Geometry and Subspace Projection for Neural AC Power Flow](https://arxiv.org/abs/2610.05959)

**<font color=#1a73e8>作者：</font>** Changhun Kim, Timon Conrad, Redwanul Karim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent neural power-flow solvers, including emerging foundation models, achieve accurate voltage predictions, yet such accuracy does not necessarily imply physically consistent solutions. Even small complex voltage errors can yield large AC power-balance residuals. We study this accuracy-consistency gap across PIGNN-GC, GridSFM, gridfm-graphkit, and LUMINA on realistic 2224-bus Great Britain network (GBnetwork) scenarios, with cross-grid evaluation of GridSFM over 31 systems. Using a singular value decomposition (SVD) basis fitted to training AC power-flow solutions, we find that neural prediction errors contain substantial components outside the dominant solution subspace. To address this mismatch, calibrated solution-subspace projection (CSP) suppresses off-subspace prediction components after train-only bias calibration, reducing Mean PB by 67.0%, 37.8%, 40.5%, and 68.9% for PIGNN-GC, GridSFM, gridfm-graphkit, and LUMINA, respectively, relative to calibrated predictions, while improving voltage-magnitude accuracy in all four models. These results identify output-error geometry as an important factor in physics-consistent neural AC power flow. Code: this https URL

---


### 423. [Strategic Multi-Agent Learning for Interpretable Action Valuation of All Players in Football](https://arxiv.org/abs/2610.05961)

**<font color=#1a73e8>作者：</font>** Kenjiro Ide, Taiga Someya, Kohei Kawaguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Valuing player actions in football requires accounting for strategic interactions among 22 players, including off-ball movements and defensive positioning. Existing reinforcement-learning-based methods commonly aggregate decisions at the team level or estimate player values independently, leaving strategic interdependence among players insufficiently represented. This study proposes an action valuation framework inspired by Markov perfect equilibrium (MPE) for all players. Each possession is modeled as a finite-horizon dynamic game, with each player represented as an autonomous agent whose policy depends on the current game state. MPE is used as a motivating solution concept rather than an exact equilibrium. To improve interpretability, we use Expandable Decision-Making States (EDMS) and decompose the Q-value into a successor-feature basis and a linear reward-weight vector. The value basis is estimated by linear TD initialization followed by nonlinear refinement. Using tracking and event data from 95 J1 League matches, we compare the proposed formulation with an independent reinforcement learning baseline. Because the two formulations define TD errors in different target spaces, TD MSE is used only for within-formulation consistency. With EDMS fixed, the independent baseline assigns the highest value to forward movement in 99.21% of evaluated off-ball states, whereas the most frequent direction under the proposed formulation accounts for 17.63%. Team-level average Q-values show a negative association with season-level expected goals for the baseline and a weakly positive association for the proposed formulation. Qualitative analyses illustrate context-dependent valuations of off-ball movements and defensive positioning. Overall, the proposed formulation produces more context-sensitive action rankings, although the comparison does not isolate the MPE-inspired component.

---


### 424. [JLD: Perceptual Distance Through A Jacobian Lens](https://arxiv.org/abs/2610.05967)

**<font color=#1a73e8>作者：</font>** Shreshth Saini, Balu Adsumilli, Alan C. Bovik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image compression, restoration, and generation all require a way to measure how different two images look to a person. Pixel error ignores how people see, while the most accurate perceptual distances are typically fitted to human judgments, tying them to a fixed data and resolution. For example, when image resolution is doubled, the correlation of DISTS with human scores on TID2013 drops from 0.815 to 0.717. We introduce the Jacobian Lens Distance (JLD), which derives its perceptual geometry from a frozen vision encoder rather than from human labels. JLD combines the locality of early patch features with the perceptual sensitivity captured by later encoder representations. Specifically, we use the encoder Jacobian to identify directions in the early feature space that most strongly affect the encoder output, producing a fixed metric tensor, $E[J^\top J]$, which we call the Jacobian lens. The lens is fitted only once from 100 unlabeled images, taking about 35 seconds. Locally, this construction defines a pullback metric in pixel space, giving JLD a clear geometric interpretation that can be directly analyzed on real images. Across four standard perceptual databases, JLD achieves state-of-the-art performance and consistently outperforms LPIPS, DISTS, PieAPP, and DreamSim. JLD is also robust to changes in image resolution, on TID2013, its lens-term correlation remains nearly unchanged when the resolution is doubled, decreasing only from 0.850 to 0.845. We further introduce JLD-fast, which is $4\times$ faster than LPIPS-VGG while achieving a mean correlation of 0.911. Finally, JLD naturally extends to video, reaching a correlation of 0.786 on Waterloo IVC 4K compared with 0.611 for VMAF.

---


### 425. [Fast Last-Iterate Convergence in Zero-Sum Markov Games with Bandit Feedback](https://arxiv.org/abs/2610.05968)

**<font color=#1a73e8>作者：</font>** Yuheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study last-iterate convergence in unknown two-player zero-sum discounted Markov games with bandit feedback. The players learn independently along a single trajectory without observing each other's actions. We develop Adaptive Regularized TD Learning (ARTD), which achieves a $\widetilde{\mathcal{O}}(t^{-1/4})$ duality gap bound for the current policies under a uniform hitting time assumption, with high probability simultaneously over all rounds and starting states. This improves the $\widetilde{\mathcal{O}}(t^{-1/(9+\nu)})$ rate of Cai et al. (2023), for any fixed $\nu>0$, under the same feedback model and hitting time assumption. Our algorithm requires no knowledge of the hitting time bound, the time horizon, or the confidence level. To stabilize policy learning as value estimates change, we separate fast temporal difference averaging from bounded value updates. We adapt log-barrier regularization to the progress of value estimation, controlling both policy and value errors throughout learning. Together, these mechanisms enable fast convergence of the policies actually played, even when the players learn independently from bandit feedback.

---


### 426. [Reachability-Aware Diffusion Policy Optimization](https://arxiv.org/abs/2610.05969)

**<font color=#1a73e8>作者：</font>** Hikmet Simsir, Kutay Demiray, Ozgur S. Oguz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion policies provide expressive action distributions for continuous-control reinforcement learning. However, safety-aware online diffusion policy optimization remains underexplored, particularly methods that use predictive reachability information without an explicit dynamics model. We propose Reachability-Aware Diffusion Policy Optimization (RADPO), a model-free method that combines predictive first-hit safety estimation with cumulative-cost budget feedback. RADPO learns a discounted first-hit reachability value that captures the discounted risk of a cost event, assigns larger weight to events that occur sooner, and uses this signal to shape the reward. A separate dual-like multiplier adjusts the shaping strength according to realized episodic costs relative to a prescribed budget. The diffusion actor improves through weighted denoising regression on candidate actions scored by the reward critic. Our approach requires neither a learned dynamics model, action gradients through the critics, nor differentiation through the reverse diffusion sampler. We establish theoretical properties of the reachability value and show that accumulated reachability penalty provides a conservative surrogate for future discounted cumulative cost. Across ten continuous-control safety tasks, RADPO achieves competitive reward-cost trade-offs, with substantial reductions in constraint violations on several tasks relative to the compared baselines. Our theoretical and empirical analysis supports that combining reachability with cumulative budget feedback is a viable approach to safety-aware diffusion policies.

---


### 427. [EpicWorldModel: Exploration-driven Planning with Latent World Models](https://arxiv.org/abs/2610.05996)

**<font color=#1a73e8>作者：</font>** Bowen Feng, Julian Ost, May Mei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models based on Joint-Embedding Predictive Architecture (JEPA) are deterministic by design. While successful in fully observable scenarios, this paradigm breaks down when past observations and actions lead to multiple plausible future possibilities, e.g., due to occlusion. We introduce EpicWorldModel, a framework to train stochastic JEPAs for environments and tasks with inherent uncertainty under partially observability. We jointly train the EpicWorldModel predictor with its latent representation space to directly predict multiple potential future states using a flow-matching objective, when the goal-relevant scene content is absent from the conditioning history. We show that flow predictive variance, motivated by its relation to an upper bound on predictive entropy, serves as a useful exploration guidance for planning. By incorporating this uncertainty signal into Cross-Entropy Method (CEM)-based planning, our approach balances goal-reaching with exploration of uncertain regions where occluded goals are most likely to be located. We demonstrate the effectiveness of EpicWorldModel through a series of latent planning experiments with the best or on-par performance across tasks, showing up to 22% empirical improvement in success rate over LeWorldModel.

---


### 428. [Langevin Flow Maps: Efficient Molecular Dynamics and Transition Path Sampling](https://arxiv.org/abs/2610.05998)

**<font color=#1a73e8>作者：</font>** Sam McCallum, Niklas Rindtorff, Alexander Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular dynamics simulations proceed by integrating the Langevin equations over many small femtosecond timesteps. This poses a challenge for estimating ensemble properties and transition dynamics that occur on much longer timescales. We introduce Langevin Flow Maps, which extend machine-learned force-fields to additionally learn the stochastic Langevin integrator. We show that Langevin Flow Maps enable large-timestep molecular dynamics and recover accurate dynamical properties of the system, while running an order of magnitude faster than current machine-learned force fields. Further, by training on a diverse molecular dataset, we demonstrate a path towards transferable Langevin Flow Maps.

---


### 429. [Learning While Scheduling Jobs under Context-Dependent Service Rates: An Anytime Rate-Optimal Algorithm](https://arxiv.org/abs/2610.06006)

**<font color=#1a73e8>作者：</font>** Seoungbin Bae, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study contextual queueing bandits, where a learner schedules jobs while learning unknown service rates modeled by logistic functions of job-server features. Performance is measured by queue length regret, the expected excess queue length at round $t$ relative to an oracle that knows the service rates. Existing decaying-regret guarantees either have a suboptimal decay rate or require a known fixed horizon. They also assume context-wise slack and a strictly positive minimum eigenvalue of the feature covariance. In this paper, we propose WISE (Widest Interval Selection with Elimination), achieving rate-optimal $\widetilde{\mathcal O}(t^{-1/2})$ queue length regret at every sufficiently large time without knowing the horizon. We assume capacity slack, meaning that expected incoming workload under best-server service is below service capacity, and impose no covariance lower bound. Our analysis uses a workload potential measuring the expected service attempts needed by waiting jobs on their best servers. Its drift on nonempty rounds combines a negative term ensured by capacity slack with errors from suboptimal service choices. Then an elliptical potential count bounds how often WISE selects wide confidence intervals, thereby limiting the number of rounds with large service errors. We also sharpen the arrival-rate dependence of an existing lower bound and make its dependence on feature dimension and server count explicit. We prove another lower bound that quantifies the increase in regret as the normalized capacity slack decreases; to our knowledge, this is the first such lower bound for CQB. Simulations show small regret even when context-wise slack fails.

---


### 430. [Ultrasound Operator Guidance Using World Modeling and Retrieval Based Action Planning](https://arxiv.org/abs/2610.06008)

**<font color=#1a73e8>作者：</font>** Noortje I.P. Schueler, Hans van Gorp, Ruud J.G. van Sloun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ultrasound is widely used, but acquisition quality is heavily dependent on the operator's knowledge and expertise. With demand for examinations outpacing the supply of trained sonographers, operator-guidance systems aim to close this gap by instructing a less trained user how to move the probe toward a target view. In this paper, we propose a retrieval-induced latent transition model for ultrasound acquisition dynamics, formulating ultrasound operator guidance as multi-step planning and retrieval in a world model. Using a V-JEPA 2.1 backbone, observations are first encoded into a latent space where anatomically related views lie close together. We then retrieve similar views from a reference database containing encoded latent states and corresponding probe positions and orientations. Rather than learning a parametric transition function, we directly use physically executed transitions from the database to establish our nonparametric, retrieval-induced transition model that supports receding-horizon planning. At deployment, guidance is generated from the live ultrasound image feed alone, without any probe tracking hardware. Applied to carotid ultrasound, the proposed planner reaches the target view in 86% of retrospective closed-loop episodes, versus 52% and 43% for representative baselines, outperforming both on every target view, including the challenging longitudinal internal and external carotid artery views. A prospective feasibility study on unseen volunteers, run in real time on a CPU using distillation, reaches 83% target-view reachability. Because planning is driven by proximity to any encodable goal latent, the same world model can navigate back to any previously acquired, patient-specific frame, supporting reproducible longitudinal imaging for e.g. perioperative or follow-up monitoring.

---


### 431. [Spectral Geometry of Attention: From Information Routing to Uncertainty](https://arxiv.org/abs/2610.06012)

**<font color=#1a73e8>作者：</font>** Giulio Viganò, Simone Melzi, Maks Ovsjanikov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we study transformer attention through the lens of spectral geometry and operator theory. We view each attention head as a functional map between Hilbert spaces of functions on the token sequence and derive a Token Difference Operator, whose spectral structure controls how token-space information is routed to the output. We show that standard Euclidean spectra are structurally biased by sinks, conflating mass concentration with genuine routing capacity. By recasting token space in the intrinsic probability geometry induced by attention, the token difference spectrum disentangles sink effects from routing capacity and provides a spectral description of the dimensionality of the head output. This yields a unified framework for analyzing attention maps, explaining sinks, routing collapse, and output dimensionality within a single operator-theoretic framework. In practice, by grounding attention heuristics in spectral geometry, we develop a novel attention-based uncertainty estimator that complements probability-based scores, with the largest gains on long-context inputs.

---


### 432. [Investigating Query-Insensitive Behavior in Spatio-Temporal Video Grounding](https://arxiv.org/abs/2610.06018)

**<font color=#1a73e8>作者：</font>** Eryk Kołodziejczyk, Alberto Presta, Karol Szurkowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal video grounding (STVG) aims to localize objects or events described by natural language queries in both space and time. Existing STVG models are typically trained and evaluated under the assumption that each query is relevant to the input video. In this work, we challenge this assumption by studying the behavior of state-of-the-art STVG models under irrelevant queries and missing textual input. Our experiments show that current models can still produce plausible spatio-temporal predictions even when the query is unrelated to the video or removed entirely. We further analyze HCSTVG-v2 and VidSTG to identify dataset regularities that may encourage such query-insensitive behavior. Our study highlights an underexplored limitation of STVG models and motivates negative-aware evaluation protocols and architectures that explicitly assess query relevance.

---


### 433. [Adaptive Expert Guidance for Efficient On-Policy Reinforcement Learning](https://arxiv.org/abs/2610.06019)

**<font color=#1a73e8>作者：</font>** Daniele Affinita, Ming Xu, Rudolf Reiter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With massively parallel simulation, on-policy Reinforcement Learning methods such as PPO have become standard in many domains. However, learning from scratch is sample-inefficient and fails to exploit the potential existence of a suboptimal expert, such as a heuristic, a model-based controller, or a policy trained on a related task. Such an expert is often available and can guide early training, but its sub-optimality limits final performance. The challenge then becomes balancing expert guidance against learning from rewards. Existing methods set the expert's influence through a blending weight, a schedule, or an evaluation-driven curriculum. Alternatively, they adapt it with additional learned components such as critics over expert actions or auxiliary agents. However, none optimizes it using the same on-policy objective as the policy itself. We propose a method in which the learner and the expert alternate control within each training episode, and the expert's share of control is a single learnable parameter optimized jointly with the policy. The learner benefits from the expert early in training, but its share of control declines as the learner becomes more competent, until eventually vanishing completely. This leaves the learner acting alone and better than the suboptimal expert. We evaluate our method on 34 tasks across two benchmarks, spanning discrete and continuous action spaces, using both learned and model-based experts. Our method improves sample efficiency over guided and unguided baselines while requiring minimal hyperparameter variation. The expert's share decays to zero as the learner improves, vanishing when the expert is no longer useful.

---


### 434. [Patch-based Querying Identifies Structures of Interest in Electron Microscopy](https://arxiv.org/abs/2610.06020)

**<font color=#1a73e8>作者：</font>** Niels Vyncke, Nicolas Nadisic, Yvan Saeys 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volume electron microscopy (vEM) has emerged as an essential sensing technique in biomedical research, allowing the three-dimensional imaging of biological cells and tissues at nanometer-scale resolution. The ability to generate extensive datasets has reached the limitations of downstream analysis processes, which depend significantly on the intervention of human experts for preprocessing and annotation. We propose an efficient and reliable patch-based retrieval framework based on self-supervised learning of local image descriptors to locate self-similar structures in vEM datasets. Given a few manual annotations of a given cellular structure, our method can retrieve similar structures across the EM volume. Our framework is interactive, allowing the human expert to refine the search queries and retrieve relevant image patches quickly and using little labeled data. Experiments on real-world vEM images of biological tissues demonstrate that our framework can reliably identify relevant cellular structures, generalize across different organelles and acquisition modalities, and substantially reduce the search space for downstream analysis.

---


### 435. [Scalable Minimal-Change Learning for Controllable Image Editing](https://arxiv.org/abs/2610.06021)

**<font color=#1a73e8>作者：</font>** Shuo Chen, Fengming Huang, Yu Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image editing should change only the attributes specified by an instruction while preserving everything else, yet current methods often make unintended changes. We treat this minimal-change principle as an optimization objective for instruction-based editing. Latent L1 regularization is a poor proxy for output locality in modern nonlinear generators and often requires supervision unavailable at scale. We instead optimize edit outcomes with reinforcement learning. An agentic vision-language reward model audits each source image, instruction, and edited image for two failure types: unimplemented requested changes and unintended changes. A group-level rubric merges and verifies these issues to provide consistent rewards across candidate edits without per-instruction human annotations. On FLUX.1 Kontext-dev, ARRO raises average EditScore from 5.21 to 5.88 across MinEval, MagicBrush, AnyBench, and Emu-Edit. On 600 evaluation examples, it reduces off-target pixel change by 8.4% relative to the base editor. Reward and SFT controls, blinded human evaluations, and transfer to OmniGen2 provide complementary evidence. Code: this https URL

---


### 436. [Joint Precision Neural Networks: Task-Aware Dependency and Predictive Learning](https://arxiv.org/abs/2610.06023)

**<font color=#1a73e8>作者：</font>** Andrea Cavallo, Samuel Rey, Antonio G. Marques 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploiting meaningful latent structures from data to solve downstream tasks is a fundamental challenge in signal processing and machine learning. While Principal Component Analysis (PCA) and coVariance Neural Networks (VNNs) successfully leverage the covariance matrix to process data, they inherently capture both direct and indirect correlations. The precision matrix (inverse covariance) overcomes this by explicitly encoding conditional independencies, making it largely studied in graphical lasso and graph topology identification. However, finite-sample precision estimates are notoriously unstable, and regularized estimators remain task-agnostic. In this work, our principal contribution is tackling the challenging problem of task-aware graph inference. We propose Precision Neural Networks-Joint (PNN-Joint), a framework that jointly estimates a sparse, statistically grounded precision matrix alongside graph neural network weights via an alternating optimization scheme. As a foundational framework to support this, we introduce Precision Neural Networks (PNNs), a broader class of graph convolutional networks operating on precision estimators, and establish their spectral connections to PCA and VNNs alongside their stability to finite-sample errors. Extensive empirical evaluations on synthetic data, as well as real-world neuroimaging and motion sensor datasets, demonstrate that PNN-Joint yields highly interpretable task-aware graphs, exhibits remarkable robustness in low-data regimes, and consistently achieves the best or second-best performance among competitors on real-world tasks.

---


### 437. [Grounded Joint-Attention Other-Play for Zero-Shot Coordination](https://arxiv.org/abs/2610.06025)

**<font color=#1a73e8>作者：</font>** Giulia Benintendi, Constantin Ruhdorfer, Fabian Kögel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Joint attention - the human ability to share a common visual or cognitive focus with others - enables a meeting of minds that lets us coordinate even with unfamiliar partners. In this work we investigate whether equipping AI agents with a similar mechanism can enable such zero-shot coordination. We introduce Mutual Attention for zero-shot TEaming (MATE): a novel multi-agent reinforcement learning method inspired by human joint attention. MATE encourages agents to coordinate their actions by aligning their visual attention on scene-salient objects during the interaction rather than relying on arbitrary partner-dependent conventions established during training. Unlike symmetry-breaking approaches that merely prevent brittle conventions from emerging, MATE actively promotes coordination through an environment-grounded signal that is naturally shared across partners. We evaluate MATE on three benchmarks: our Card Alignment Game, designed to isolate brittle convention formation, and the more challenging Level-Based Foraging and OvercookedV2 benchmarks. Our experiments consistently show that a joint-attention-inspired signal improves coordination with unknown partners, underlining MATE's potential as a general coordination mechanism that complements and surpasses symmetry-breaking approaches.

---


### 438. [Casual Flash Lighting for Gaussian Splat Inverse Rendering](https://arxiv.org/abs/2610.06035)

**<font color=#1a73e8>作者：</font>** Jiamin Xu, Dongheng Wei, Jiarong Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering geometry, materials, and lighting from photographs is highly ambiguous when only static illumination is available. Active-lighting setups reduce the ambiguity but require dark rooms or specialized hardware. Instead, we synergize both static and flash lighting from casual indoor capture, with the flash on or off, each from independent viewpoints. The flash residual constrains albedo and the BRDF, while static lighting captures grazing-angle specular highlights that flash misses. With a 2DGS reconstruction framing, our key contribution is a GS-anchored diffuse field: a hash-encoded MLP is queried at the rasterized 2DGS depth. As it depends only on world position, it is view consistent in 3D and allows the flash residual to drive material decomposition instead of being absorbed by alpha-blending drift across views. At the same time, we render static lighting with deferred shading such that it can also supervise material decomposition. On five synthetic and three real indoor scenes, our method outperforms six recent baselines on diffuse color, albedo and roughness material parameters, and in relighting where PSNR improves by 4.17 dB over the next-best baseline.

---


### 439. [MercerFlow: Flow Matching in a Kernel-Induced Latent Space for Probabilistic Forecasting](https://arxiv.org/abs/2610.06039)

**<font color=#1a73e8>作者：</font>** Ilya Kuleshov, Egor Serov, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that probabilistic flow matching for time series forecasting benefits from a data-matched prior. The resulting prior introduces local correlations, which a sequential architecture usually absorbs: a recurrent neural network (RNN), a structured state-space model (S4), or a Transformer. However, such a backbone costs GPU memory and time per epoch. A cheaper alternative is MLP-based latent-space flow matching: embed the time series via an invertible map to a single latent vector and learn the flow there, so a tabular MLP can treat the series as a set of features. The relationship between the prior and the choice of linear latent map is understudied in conditional flow matching (CFM) forecasting, yet we found it strongly affects performance. Fixed transforms such as Fourier or discrete cosine (DCT) are only well-conditioned for Ornstein--Uhlenbeck priors, while a principal-component (PCA) map fit to the data is a strong but training-set-dependent reference sensitive to train--test shift. Instead, we propose to use the Mercer eigenbasis of the prior kernel: it diagonalises the centred covariance exactly, decouples from training data, and adapts to non-stationary and periodic priors. On five GluonTS benchmarks (ETTh1, ETTh2, Weather, Electricity, Traffic) under a shared protocol with TSFlow, the resulting MLP matches or beats it on CRPS at about $4.7\times$ less training memory and $3.5\times$--$4.4\times$ less time per epoch.

---


### 440. [Representation Disentanglement for Fair Chest X-Ray Diagnosis](https://arxiv.org/abs/2610.06041)

**<font color=#1a73e8>作者：</font>** Yujie Sun, Ruizhe Li, Xiaowu Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has advanced chest X-ray (CXR) diagnosis, yet demographic biases in learned representations may contribute to performance disparities across intersectional groups. We propose a single-encoder framework combining dual-level decorrelation with prototype-guided cross-group contrastive learning to reduce demographic dependence while accounting for within-class variation. We further propose Demographic Representation Alignment Reduction (DRAR), a new metric that quantifies the reduction in demographic structure within disease representations. The framework is evaluated on four classification tasks using 34,809 CheXpert test images across eight intersectional groups, defined by age, sex and ethnicity. Compared with empirical risk minimization (ERM), our method reduces the mean equalized-odds gap from 15.41\% to 10.86\% and the AUC gap from 5.95\% to 5.01\%. Our method achieves a DRAR of 59.04\% relative to ERM, with only a slight decrease in mean AUC. These results demonstrate that representation disentanglement can reduce demographic bias and improve intersectional fairness. Code is available at \url{this https URL}.

---


### 441. [GO-Based Clustering for Learning Cluster-Level Causal Gene Regulatory Networks](https://arxiv.org/abs/2610.06042)

**<font color=#1a73e8>作者：</font>** Azlaan Mustafa Samad, Wei Zhang, Adèle H Ribeiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovery of causal relationships in high-dimensional Gene Regulatory Networks (GRN) is computationally challenging and often difficult to interpret due to dense connections. Therefore, grouping genes together into functional modules can improve tractability and biological interpretability. However, existing cluster level causal discovery methods assume access to a predefined admissible partitions, requiring the graph over clusters to be acyclic. Constructing such partitions is therefore challenging. In this work, we introduce GO-based Clustering for Causal Discovery (GO4CD), an algorithm that uses Gene Ontology (GO) to construct biologically meaningful gene partitions at multiple levels of granularity, while favoring those more likely to be admissible for causal discovery. GO4CD groups together genes participating in a shared biological process, and propagates gene annotations through the ontology hierarchy to achieve different granularity of partitions. Furthermore, we integrate GO4CD with Causal Learning over Clusters (CLOC) algorithm and evaluate recovery of true Markov equivalence class both with an oracle of conditional independencies and on simulated gene expression data using multivariate conditional independence tests. We evaluate GO4CD on multiple this http URL regulatory subnetworks and find that it is inadmissible in 18.1% of the cases, compared with 65.3-82.3% for the semantic-similarity baselines. Our results indicate that GO4CD is substantially better suited to learning causal GRNs defined over biologically meaningful gene clusters.

---


### 442. [Local2Mesh: Spatially Localized Contour-to-Mesh for Left Ventricular Reconstruction from Sparse 2D Cardiac MRI](https://arxiv.org/abs/2610.06052)

**<font color=#1a73e8>作者：</font>** Haoyu Wu, Ling Lin, Pascal Lefèvre 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) left ventricular (LV) reconstruction from sparse cardiac magnetic resonance (CMR) imaging remains challenging due to inter-slice misalignment and insufficient local spatial information between slices. Global aggregation of contour features may obscure local contour-to-surface relationships. We propose Local2Mesh, a spatially localized contour-to-mesh framework that deforms a template mesh to reconstruct 3D LV geometry from sparse 2D contours without 3D mesh annotations. The framework introduces geometry-aware alignment to correct inter-slice misalignment and a plane-aware Local Router that routes contour features to template vertices using vertex-to-plane distances. Local and global contour features then jointly guide graph-based template deformation for 3D LV reconstruction. Experiments on two public datasets, M\&Ms-2 and ACDC, demonstrate superior geometric reconstruction and functional estimation over existing methods. Zero-shot transfer from M\&Ms-2 to ACDC demonstrates strong cross-dataset generalization. Reconstructed meshes also improve disease classification over sparse contours, supporting their utility for downstream cardiac analysis. These results demonstrate that combining geometry-aware alignment with local contour-to-vertex modeling improves LV reconstruction from sparse 2D contours and supports downstream cardiac analysis. The code is available at \url{this https URL}.

---


### 443. [Efficient HQC Implementations on RISC-V: A Cross-Layer Design Space Exploration](https://arxiv.org/abs/2610.06058)

**<font color=#1a73e8>作者：</font>** Maximilian Schöffel, Johannes Feldmann, Elias Biehl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> RISC-V-based hardware/software co-design has become an established methodology for implementing post-quantum cryptography (PQC) on embedded devices. Its software programmability, extensible instruction-set architecture, and optional dedicated accelerators create a broad design space that offers the flexibility required for crypto-agility and post-deployment updates. For HQC, a PQC key-encapsulation mechanism selected for standardization, several RISC-V-based implementations have already been published. However, these works explore only a small subset of this design space.
We present, to the best of our knowledge, the most comprehensive exploration of RISC-V-based HQC. Our exploration is centered around a new, parametrizable architecture framework on which we characterize 29,920 distinct architectural configurations across all three HQC security levels on FPGA. The Pareto-optimal configurations from this framework outperform the state-of-the-art RISC-V-based HQC implementation, ranging from 4.8x lower LUT utilization at 17% lower latency to 69.6x lower latency at 30% lower LUT utilization, while also requiring up to 10.6x fewer block RAMs.

---


### 444. [PRA-TLS: Attestation of a Client Application for TEE](https://arxiv.org/abs/2610.06061)

**<font color=#1a73e8>作者：</font>** Reina Sasaki, Yutaka Ishikawa, Atsuko Takefusa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) are secure foundations for protecting sensitive information and executing computations over confidential data. Processing in an isolated execution environment (enclave) is invoked by an untrusted application in the Rich Execution Environment (REE). Then the enclave returns the execution results to the untrusted application. Even if the enclave has been attested, the boundary between the enclave and the untrusted application poses risks, such as tampering with input arguments or return values and manipulating the order in which the application invokes functions. Therefore, it is necessary to establish the authenticity and integrity of not only the enclave itself but also the application and its execution environment. In this study, we propose an attestation protocol, Portable Remote Attestation TLS (PRA-TLS), for a client application that invokes an enclave. We introduce a daemon that acts as an attester. PRA-TLS uses a trusted Attester Daemon to measure the state of the host environment and application code at runtime, providing these measurements as attestation evidence for verification by a remote Verifier. This mechanism allows the enclave to proceed only when the software environment is in the expected state and the application code is verified as legitimate. We define attack models and security requirements for the proposed protocol and formally evaluate its security using the Tamarin Prover. Furthermore, we implement a prototype of PRA-TLS using Intel SGX and evaluate its performance.

---


### 445. [Pay to Learn, Share to Earn: Incentivized Federated Multi-Player Bandits](https://arxiv.org/abs/2610.06062)

**<font color=#1a73e8>作者：</font>** Pavamana K J, Chandramani Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated multi-player multi-armed bandit problems model collaborative sequential decision-making where multiple players interact with a common bandit environment and share information through a central server to accelerate learning. Existing federated bandit frameworks typically assume that all players willingly share their local observations with the server. However, this assumption is often unrealistic in practical settings where players are self-interested and may not participate in collaboration without explicit incentives. To address this challenge, we propose an incentive-aware federated bandit framework in which players receive rewards for sharing information with the server and incur costs when buying information from the server. We develop a UCB-based algorithm, termed Buying-UCB, that balances individual exploration and collaborative learning by incorporating both sharing incentives and information acquisition costs into the learning process. We theoretically analyze the proposed algorithm and derive upper bounds on the group regret and buying cost. Our analysis further characterizes the trade-off between fully collaborative federated learning and completely independent learning. Extensive numerical experiments validate the theoretical findings and demonstrate the effectiveness of the proposed framework under different collaboration and pricing regimes.

---


### 446. [Vision Transformer Ensembles for Panoramic Street Segmentation](https://arxiv.org/abs/2610.06063)

**<font color=#1a73e8>作者：</font>** Yunus Serhat Bıçakçı  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult. This paper presents the system used for a first place submission to the PalmCity challenge in the leaderboard snapshot dated 5 October 2026. Nine pretrained segmentation systems are compared using approximately equal computation budgets. The candidates include DeepLabV3+, SegFormer, UPerNet, Mask2Former, DINOv3 with a linear decoder, and an Encoder only Mask Transformer using DINOv3. The two leading candidates are trained independently with three random seeds and longer budgets. Equal averaging of class probabilities from the three Encoder only Mask Transformer models, evaluated at three image scales with horizontal reflection, produces 60.95% mean intersection over union and 71.16% mean F1 on the 84 image public validation split. The submitted predictions receive 57.08% mean intersection over union and 67.96% mean F1 on the hidden test leaderboard. Producing all 249 test masks takes 251.49 seconds including model initialization and provenance checks on one NVIDIA RTX 5090. Peak allocated GPU memory is 2.70 GiB. The study reports all eligible models, all inference variants, class level errors, source conditions, and reproducibility checks, providing a documented challenge workflow with existing architectures.

---


### 447. [Boosting Transferable Adversarial Attacks against Deep Reinforcement Learning](https://arxiv.org/abs/2610.06083)

**<font color=#1a73e8>作者：</font>** Zexin Li, Ruili Yao, Yiming Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most adversarial attacks on deep reinforcement learning (DRL) assume white-box access to the victim policy, which rarely holds in practice. This paper studies transfer-based black-box attacks on DRL: the attacker crafts observation perturbations on a white-box surrogate agent and feeds them to an unknown victim. We formulate the attack as return minimization under a per-step perturbation budget. We first show that transplanting transferable image-classification attacks (FGSM, MI-FGSM, and NI-FGSM) with a per-step objective yields perturbations that transfer but are no stronger than random noise of the same budget. We then propose a trajectory-level attack that optimizes a sequence of perturbations over a receding horizon through a differentiable model of the environment and a temperature-smoothed surrogate policy, with the same optimizers. On CartPole-v1 with ten DQN and DDQN agents and 100 surrogate--victim pairs, the trajectory-level attack outperforms per-step attacks and random noise in the white-box, cross-model, and cross-algorithm settings.

---


### 448. [Rethinking Least-Core Computation in Contextual-Distractor Games](https://arxiv.org/abs/2610.06087)

**<font color=#1a73e8>作者：</font>** Hiroshi Kera, Toshinori Yamauchi, Sai Ganesh Nagarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Game-theoretic attribution explains a model by assigning credit to its features or training examples. The least core has attracted interest as an alternative to Shapley-style averaging because it can expose players that cause substantial harm in rare, high-value contexts. However, least-core allocations are generally nonunique, and the choice of allocation can affect the resulting explanation. In this study, we investigate how payoff selection and coalition sampling affect least-core attribution. Our experiments show that selector choice matters for distinguishing useful and harmful contributions, and that sampling can degrade harmful-player identification across the tested selectors even when useful players remain well identified. These observations motivate efficient computation with all coalition constraints and a well-defined selector. We introduce entropic least core (ELC), a smooth approximation whose unique minimizer follows a continuous path along the temperature to the nucleolus, a classical refinement of the least core. Our experiments show that ELC approximates the nucleolus faster than an LP-based nucleolus solver while retaining small payoff errors, with further GPU acceleration at larger problem sizes. In the tested full-coalition contextual-distractor games, ELC matches the minimum-norm selector in identification accuracy and more accurately ranks distractors by harm.

---


### 449. [Anatomy-preserving unpaired cone-beam CT refinement for image-guided radiotherapy using pseudo-label guided diffusion](https://arxiv.org/abs/2610.06094)

**<font color=#1a73e8>作者：</font>** Qi Lai, Yutong He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cone-beam computed tomography (CBCT) is widely used in image-guided radiotherapy, but scatter, beam hardening, noise, truncation, and other artifacts limit image quality and CT number accuracy. Paired CBCT and CT data are difficult to obtain clinically because of motion, anatomical changes, and acquisition mismatch. We present RefineCBCT, an unpaired CBCT refinement framework that uses pseudo-label guidance and short-step diffusion to reduce artifacts while preserving patient-specific anatomy. RefineCBCT was trained and evaluated on unpaired CBCT and planning CT data from public LUNG TCIA and PELVIC TCIA datasets and compared with representative GAN and diffusion based methods. On LUNG TCIA, it achieved the best results across all metrics, with MAE 19.411, RMSE 62.758, PSNR 30.845 dB, and SSIM 0.931. On PELVIC TCIA, it achieved the best MAE, PSNR, and SSIM, with values of 14.905, 36.671 dB, and 0.876. The refined images showed fewer streaking and shading artifacts, clearer anatomical boundaries, and improved soft tissue uniformity, with line profile and ROI analyses showing closer agreement with planning CT. These results suggest that RefineCBCT provides efficient and effective CBCT refinement under clinically realistic unpaired training conditions and may support more reliable CBCT use in image-guided radiotherapy workflows. Code is publicly available on GitHub, and the evaluated datasets are available from The Cancer Imaging Archive.

---


### 450. [Lossy Compression of PDE Training Inputs: Field Reconstruction Error Does Not Order the Cost to a Trained Operator](https://arxiv.org/abs/2610.06095)

**<font color=#1a73e8>作者：</font>** Huy Hoang Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator-learning benchmarks are stored at full precision and have grown to terabyte scale. Rate-distortion theory says how many bits the stored field needs, while a practitioner needs to know how accurate an operator trained on the compressed data will be. We show that the first does not determine the second, and measure why, compressing the input fields while targets and test inputs stay at full precision. A solution operator attenuates a perturbation of its input. Pushing a compressed field through a surrogate already trained at full precision measures how much of the perturbation that surrogate transmits. The fraction is consistent with the smoothing behaviour of the underlying equation, and it spans more than two orders of magnitude across PDE families. Field reconstruction error is computed before the attenuation and cannot see it. For operators trained with mean squared error it inverts 36 of 104 cost comparisons across datasets, where a probe built from the same forward passes inverts 12. Two families that PDEBench stores with identical initial conditions differ threefold downstream at identical field error. Under the relative-L2 objective of the reference recipe the separation narrows, while the ordering of the family-level median transmission factors is unchanged. After one full-precision training run, the probe evaluates an entire rate curve by forward passes alone. It ranks datasets and rates consistently across the codecs and architectures we test, while its magnitude does not transfer between them.

---


> [!TIP]
> 当前位于：**401-450**（第 9/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
