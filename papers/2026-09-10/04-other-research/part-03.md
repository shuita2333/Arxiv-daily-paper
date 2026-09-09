# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 101. [Compressed Recurrent Feedback in Tsetlin Machines: A Reproducible Boolean-FSM Study](https://arxiv.org/abs/2609.06133)

**<font color=#1a73e8>作者：</font>** Ankit Kumar, Utkarsh Raj, Rishad Shafik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential inference on small devices requires a model to retain useful history without repeatedly processing a long input record. A Recurrent Tsetlin Machine (RTM) provides this memory by returning Boolean clause outputs from one time step as inputs to the next. Direct feedback, however, grows with the clause bank and can make the recurrent input unnecessarily wide. This paper investigates a fixed-width alternative. We combine clause activations by exclusive-OR (XOR) folding, retain the folded bits at two time scales, and threshold them back to a binary state. The resulting design reduces 480 clause activations to 96 recurrent bits. We evaluate the method on a reproducible Boolean finite-state-machine benchmark with explicit transition rules, data splits, and random seeds. Across 144 runs, the compressed model obtains $61.47 \pm 6.74\%$ and $62.94 \pm 9.92\%$ accuracy on the two task families. Raw clause feedback changes these means by less than one percentage point, while increasing the recurrent width tenfold and measured host execution time by $4.38\times$ and $3.71\times$. Gated neural models remain more accurate, and a no-feedback control retaining only short input history achieves comparable or slightly higher accuracy. On this benchmark, folding matches raw feedback within small empirical margins at a much narrower interface; these findings also underscore the critical necessity of no-feedback recurrence controls when benchmarking sequence models.

---


### 102. [Counter-Swarm Doctrine: Containing Coordinated Agent Intrusions](https://arxiv.org/abs/2609.06140)

**<font color=#1a73e8>作者：</font>** Gregory N Frank  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents can turn shared infrastructure into a channel for coordinated intrusion. The Hugging Face incident and a separate public-wiki investigation show why a security assessment may need evidence from several executions and the artifacts they leave behind. We argue that the operational unit of defence should be a revisable coordination episode linking observed transfers, task authority, and response history. The central research problem is prospective episode discovery: finding which actions belong together before an evaluator supplies their membership. We define unsanctioned coordination relative to collaboration and delegated-authority policy, connect storage-mediated coordination to stigmergy, and specify the evidence needed to distinguish influence from common causes. First-contact signals are one possible input to discovery; the design also follows inherited state and later use. A proposed evaluation compares isolated actions, rolling windows, known groups, and prospectively discovered episodes at matched review cost and false-alert workload. It measures harmful outcomes across all assigned population runs and tests recurrence after channel closure and state quarantine. A checksum-verified reconstruction of the public wiki export separates the decline in retained writes from later administrative cleanup. The contribution is an incident-grounded position, descriptive analysis, and evaluation design. It makes the recommendation to monitor across executions testable without claiming a new detector or a measured containment benefit.

---


### 103. [TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144)

**<font color=#1a73e8>作者：</font>** Bihan Li, Xinyang Li, Zeran Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual dubbing must synchronize mouth motion with replacement speech while preserving identity, appearance, and temporal consistency. Although X-Dub provides a strong mask-free video-editing baseline, its application to livestream and generated-video content reveals limitations in production-domain robustness, temporal and motion stability, identity and oral-detail preservation, and inference efficiency. We present \textbf{TBDub}, a production-oriented extension of X-Dub that combines task-adaptive post-training with task-aware few-step distillation. Post-training adapts the video DiT using production-domain data, production-specific conditioning and filtering, and enhanced audio features to obtain a 30-step Teacher. Distillation adapts DMD/DMD2 to conditional video editing and compresses the Teacher into a two-step Student. On 38 TalkVid clips, the Teacher improves all eight reported reconstruction, perceptual, identity, and synchronization metrics over X-Dub. In the MOS evaluation, it improves lip-sync consistency, identity consistency, and visual quality over X-Dub by 0.14, 0.95, and 0.90 points, while the Student achieves the highest lip-sync and visual-quality scores and remains close to the Teacher in identity consistency. In paired end-to-end generation timing from the first VAE encode through the final VAE decode on a single NVIDIA H20 GPU at $512\times512$, the Student reaches 7.13 effective FPS and reduces total latency by $13.93\times$; the DiT stage alone is accelerated by $42.49\times$. The Student largely retains the Teacher's generation quality and audiovisual synchronization. The code is available on GitHub at \this https URL, and the 30-step Teacher and two-step Student weights are available on Hugging Face at this https URL.

---


### 104. [Rethinking One-Shot Federated Graph Learning: Training-Free Statistical Estimation](https://arxiv.org/abs/2609.06154)

**<font color=#1a73e8>作者：</font>** Shutong Zheng, Sijia Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-shot federated graph learning generally aims to train Graph Neural Networks (GNNs) across clients with disconnected subgraphs in a single communication round. Existing methods predominantly design advanced optimization strategies under the premise that local GNN training is indispensable. However, empirical observations reveal that under extreme non-IID conditions, local GNN training suffers from severe cross-client representation misalignment, becoming a major source of error rather than a remedy. Motivated by this, we reformulate one-shot FGL as a statistical estimation problem. We propose SPEAR (Statistical Prototype Estimation with Adaptive Reliability), a completely training-free framework that directly computes topology-smoothed class prototypes from local graphs in the original feature space. The server then aggregates these prototypes using a sample-size-adaptive shrinkage estimator that down-weights unreliable local estimates, producing robust global class prototypes. Extensive experiments across seven benchmarks demonstrate that SPEAR consistently achieves state-of-the-art accuracy under extreme heterogeneity. Moreover, SPEAR delivers at least an order-of-magnitude speedup over all baselines, reaching several orders of magnitude against generative and distillation-based methods. Our findings suggest that training-free statistical estimation, rather than local GNN optimization, provides the key to robust and efficient one-shot federated graph learning. The code is available at this https URL .

---


### 105. [Multiple Myeloma Lesion Segmentation on Whole-Body Diffusion-Weighted Imaging via Efficient Anatomical Anticipation and Multimodal Confirmation](https://arxiv.org/abs/2609.06165)

**<font color=#1a73e8>作者：</font>** Mengmeng Zhang, Shengqian Huang, Junde Zhou 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-body diffusion-weighted imaging (WB-DWI) is widely used for multiple myeloma (MM) assessment, yet automated lesion segmentation remains challenging due to limited anatomical delineation and the low specificity of marrow hyperintensity. Existing studies have introduced bone region-of-interest (ROI) information and apparent diffusion coefficient (ADC) maps to mitigate these ambiguities, but practical limitations remain. Bone ROI construction often relies on costly manual annotation, image registration, or dedicated bone models, while ADC is usually incorporated only through simple channel fusion, limiting its ability to provide complementary structural and lesion-discriminative cues. To address these limitations, we propose a two-stage framework for MM lesion segmentation on WB-DWI. In the first stage, we train a bone ROI generation model from ADC images without dedicated bone labels, providing an efficient and practical anatomical prior for lesion analysis. In the second stage, we propose Anatomy-guided Multimodal U-Net (AMU-Net), which leverages ADC in a manner consistent with clinical lesion assessment rather than treating it as a generic auxiliary modality. Extensive experiments demonstrate the effectiveness and practicality of the proposed method. It achieves the best overall performance among the evaluated methods, with a mean Dice score of 76.2%.

---


### 106. [Decision-Aware Suffix Prediction and Reasoning of Business Processes](https://arxiv.org/abs/2609.06169)

**<font color=#1a73e8>作者：</font>** Henryk Mustroph, Stefanie Rinderle-Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Suffix prediction forecasts the remaining sequence of events of a running case until completion. Most approaches rely on neural networks trained on event logs, which, on average, perform well but struggle with short prefixes or targets belonging to a rare process variant. In such scenarios, the correct path may cross multiple branching decisions, determined primarily by case- and event-level attributes, a signal that NN-based suffix prediction models tend to underweight because they may heavily weight (dense) event labels. Decision mining extracts rules for such decisions from the event log, but has so far been applied only to post-hoc and what-if analysis, not suffix prediction. We therefore extend suffix prediction with decision mining, introducing a decision-aware suffix prediction framework, a neuro-symbolic approach that enables reasoning about predicted events via mined decision rules. Experiments on three of four event logs and three suffix predictors show that the framework can improve suffix prediction, especially for short prefixes but also for rare process variants, and adds intrinsic interpretability.

---


### 107. [FMMO: Detecting the Divergence Between Local Attribution and Global Drift](https://arxiv.org/abs/2609.06173)

**<font color=#1a73e8>作者：</font>** Muhammad Rehman Zafar, Ali El-Sharif, Naimul Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-deployment drift poses a critical risk to algorithmic accountability, particularly when ground truth labels are delayed and performance degradation becomes a "silent failure". While Explainable AI (XAI) is often relied upon to audit these shifts, we demonstrate that popular local attribution methods (e.g., TreeSHAP) can exhibit misleading stability even as model reliability collapses. In this paper, we propose a Framework for Model Monitoring and Observability (FMMO) designed to expose the divergence between local explanation stability and global distribution shifts. Using benchmark, synthetic, and real-world datasets, we show that local XAI methods fail to flag drift-induced disparate impact, specifically where False Positive Rates spike for protected groups while feature attributions remain unchanged. By integrating global surrogate models with model utilization measurements, FMMO mitigates this fairness blind spot, ensuring that stakeholders can detect discriminatory deterioration that standard local XAI tools overlook.

---


### 108. [Spectral Prioritized Sweeping in Nonstationary Reinforcement Learning](https://arxiv.org/abs/2609.06186)

**<font color=#1a73e8>作者：</font>** Hung Pham, Tuan Dam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prioritized Sweeping (PS) accelerates model-based reinforcement learning by selecting backups according to Bellman residual magnitude. In nonstationary reward settings, however, the canonical priority score is shortsighted: after a localized reward shift, residuals propagate only through realized backups, so bottlenecked or topologically distant state estimates may remain static under a limited replanning budget. We introduce the Graph Topology Augmentation framework, which employ the graph's resolvent and its diffusion semantic, to augment the inquired signal. Our application, Graph Topology Augmentation for Prioritized Sweeping (GTA-PS), or which the alias Spectral Prioritized Sweeping (SPS) might be more universal, provides a drop-in ordering score for the setting of fixed dynamics and changing state rewards. GTA-PS uses a smootherized policy, inducing a transition chain, with its in- and out-Laplacian. The standard priority key is augmented with a mixing of regularized Laplacian inverses diffusing the residual magnitude. Furthermore, the topology contribution is annealed by a scheduler based on the Second Largest Eigenvalue Modulus (SLEM), allowing its scale to adapt to the chain's mixing regime. We prove that the forward potential coincides with geometric discounted residual propagation and show that GTA-PS gives active priority instantly to all states. Tabular experiments on FourRooms and GARNET domains demonstrate improved replanning efficiency over standard PS under both exact DP and Dyna-style host planners.

---


### 109. [SolarBench: A global solar energy nowcasting benchmark](https://arxiv.org/abs/2609.06187)

**<font color=#1a73e8>作者：</font>** Yuhao Nie, Stephen Campbell, Quentin Paletta 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As the share of solar power grows, nowcasting weather-driven solar variability becomes critical for reliable energy system operation. State-of-the-art approaches increasingly apply deep learning to sky camera and geostationary satellite observations, but fragmented datasets and inconsistent evaluation make it difficult to determine whether reported improvements generalize across climates, cloud regimes, and photovoltaic (PV) systems. Here we introduce SolarBench, an open global benchmark for image-based solar nowcasting. SolarBench harmonizes more than six million sky and satellite images from 11 diverse sites spanning a decade, together with irradiance or PV output and auxiliary atmospheric data. An accompanying toolbox supports reproducible data access, processing, model development, and evaluation. Using SolarBench, we benchmark representative models and reveal a gap between average forecasting accuracy and the ability to capture rapid solar fluctuations. We further quantify predictability across cloud regimes and demonstrate data-efficient adaptation to new PV systems. SolarBench provides an extensible foundation for fair comparison and methodological innovation in solar nowcasting.

---


### 110. [Customer Relationship Intelligence: Integrating CRM and MDM for Enhanced Customer Engagement](https://arxiv.org/abs/2609.06189)

**<font color=#1a73e8>作者：</font>** Tejasvi c. Addagada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study examines how Customer Relationship Management (CRM), Master Data Management (MDM), and Customer Knowledge Management (CKM) jointly constitute a Customer Relationship Intelligence (CRI) framework for enhanced Customer Engagement (CE). A cross-sectional survey of 100 participants across retail, healthcare, IT, and telecommunications sectors was analysed using Spearman rho correlation and ordinal logistic regression (IBM SPSS). Bivariate correlations were weak and non-significant (r<0.19, p>0.06). Regression identified CRM (beta=0.717, p=0.002) and CKM (beta=0.581, p=0.009) as significant positive predictors of CE; MDM showed a positive but non-significant direct effect (beta=0.346, p=0.071). The model explained 20.5% of CE variance (Nagelkerke R^2=0.205). Parallel mediation analysis (Hayes PROCESS Model 4, 5,000 bootstrap samples) found no significant indirect effects of MDM on CE via CRM (IE=0.021, 95% BC CI [-0.072, 0.121]) or CKM (IE=0.032, 95% BC CI [-0.061, 0.126]); Hypothesis H4 was not supported. CRM and CKM emerge as the principal drivers of CE within the CRI framework, while MDM functions as a foundational data quality enabler whose strategic value is realised through its enabling effect on CRM execution and knowledge management. Findings should be treated as exploratory given the sample size and cross-sectional design. Future research should replicate with larger sector-specific samples and longitudinal designs, particularly in regulated BFSI contexts where MDM architecture is shaped by data governance mandates.

---


### 111. [Predicting Wind Turbine Power Using Machine Learning and Weather Forecasts](https://arxiv.org/abs/2609.06194)

**<font color=#1a73e8>作者：</font>** Khivishta Boodhoo, Isaac Triguero, Josh Plumbly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offshore wind turbines are widely used to generate renewable energy, but their maintenance can result in decreased efficiency due to forced shutdowns. Accurate wind turbine power predictions can identify periods of low power that would be ideal for scheduling maintenance. However, the effects of data volume, feature selection, and data preprocessing on the performance of such power prediction models have not been thoroughly studied. Besides, current models have limited transferability between different wind turbines. Therefore, this study developed a baseline Linear Regression for performance comparison with a more complex Artificial Neural Network model to predict the power output of a wind turbine, using weather conditions only to enhance applicability. A range of data preprocessing techniques were studied, and models were trained on one month and one year of data to determine the effects of data preprocessing and volume on model performance. Feature selection was explored using a Random Forest Regressor. The best results from the different models showed that the Artificial Neural Network models provided the highest accuracy, with an R2 score of 0.98 and a low Mean Absolute Error of 194, when compared with the baseline model (R2 score of 0.94 and Mean Absolute Error of 441). The model performance is comparable to the range of results in past studies, with the advantage that the proposed method leverages a separate weather dataset from a nearby weather station, enabling future applications for similar wind turbines in different locations. The Artificial Neural Network model was then used to identify 4-h periods of low power predictions over 2 months (simulating application for future periods), providing power output savings of approximately 2000 kW for each maintenance event.

---


### 112. [EgoNeMo: Transferable Map of Pedestrian Dynamics via Egocentric LiDAR Scan](https://arxiv.org/abs/2609.06195)

**<font color=#1a73e8>作者：</font>** Azusa Sawada, Allan Wang, Hideo Saito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a transferable Map of Dynamics (MoD) framework that generalizes to unknown environments using only egocentric 3D LiDAR point clouds to overcome the long-standing limitation of traditional MoD methods. While MoDs are essential for encoding human motion characteristics to enable accurate pedestrian trajectory prediction or safe robot navigation, traditional approaches suffer from site-specificity, requiring exhaustive trajectory accumulation at every new location. Extending recent advances in neural implicit modeling, our framework trains a continuous, LiDAR-based MoD estimator across diverse environments. To mitigate the inherent sparsity and temporal bias of real-world trajectory data, we introduce a position-balanced sampling strategy and a multi-task learning architecture that jointly predicts motion distributions and a spatial frequency score map. The latter is further augmented by visibility-aware losses to compensate for incomplete observation data. Comprehensive experiments demonstrate that our method effectively reconstructs underlying motion maps even in unknown locations from a single instantaneous LiDAR scan, despite highly sparse training data. Finally, we show that our improvements enhance the reliability of downstream trajectory prediction.

---


### 113. [PhysWeep: Does a Video Generator Realize the Physics You Ask For?](https://arxiv.org/abs/2609.06207)

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-video generators are often credited with absorbing physical dynamics as implicit world models, a claim the community currently checks with plausibility scores that ask whether a clip looks consistent with real-world motion. Plausibility is the wrong test on its own, because a clip can look natural while encoding the wrong value of the governing physical parameter, and no existing benchmark measures this gap directly. PhysWeep closes it with a fixed, label-free audit, treating a frozen generator as a black box, recovering the realized parameter from generated pixels, and reporting how often generation is trackable at all, how far the realized value sits from the requested one, and which, if either, of the literature's two proposed failure mechanisms the data support. A deterministic-simulator positive control confirms every score is exactly checkable. Applied to three open generators across six sweep axes, PhysWeep finds a specific, reproducible, previously undocumented failure. Conditional on producing trackable motion, two of the three generate confident, well-fit dynamics that converge to one of a small number of fixed, wrong values selected by the sampling seed rather than by the request, reproducing across two independent model families, two physical systems, and an independent tracker. It matches neither the prior reversion nor the case-based clamping the literature anticipates, because the reversion target is seed-conditional rather than a single global default, and a leave-one-out selection rule rejects both; the in-range faithfulness slope is statistically indistinguishable from zero wherever a response is estimable at all. A benchmark averaging over seeds would never see this: each sample is confidently locked to a wrong constant, exactly the failure a plausibility score is structurally blind to. We release the protocol, suite, and analysis code.

---


### 114. [Branch-Centric Tokenization and Test-Time Augmentation for Skeleton Generation](https://arxiv.org/abs/2609.06218)

**<font color=#1a73e8>作者：</font>** Zhengyuan Li, Chuanyu Pan, Yuanming Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic skeleton generation involves predicting both joint positions and skeletal connectivity. However, existing approaches struggle to encode branch structures into token sequences and do not use test-time computation effectively. We study these choices within a unified autoregressive framework. First, we introduce branch-centric tokenization, a branch-aware representation that places structurally related elements next to each other and encodes connectivity directly in the sequence. Compared with standard BFS-style serialization, this representation yields more compact sequences. Second, we introduce view-augmented generation, a test-time augmentation procedure that applies axis-aligned rotations to the input mesh, maps all predictions back to a common frame, and selects the final skeleton based on mesh coverage and consistency among predictions from different views. Experiments show that our method achieves better skeleton prediction accuracy than state-of-the-art methods. In particular, our method reduces the CD-J2B error by 16.9% on the Articulation-XL2.0 dataset compared to the strongest directly comparable baseline, Auto-Connect. Qualitative results on in-the-wild meshes further demonstrate generalization across diverse inputs.

---


### 115. [Spatial Attention Supervision for Defect Localization: Exploiting Ground-Truth Masks as Training Signal in Diffusion-Augmented Defect Detection](https://arxiv.org/abs/2609.06232)

**<font color=#1a73e8>作者：</font>** Sajjad Rezvani Boroujeni, Muskan Saraf, Gnana Tulasi Makineni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground-truth defect masks in industrial inspection datasets are typically reserved for evaluation. This paper repurposes them as spatial supervision signals during training of classification networks, teaching a model not just what to predict but where to look. The method adds an activation-based attention alignment loss that steers convolutional feature maps toward defect regions, in a mixed-supervision formulation that also accommodates samples without masks, such as diffusion-generated images. Combined with DDPM augmentation, synthetic images contribute quantity while masks contribute spatial precision. We evaluate 85 models (four CNN backbones under a 2x2 data/training factorial over five seeds, plus a Swin-V2-T transformer baseline) on the MVTec-AD bottle benchmark, with localization measured on held-out defect images excluded from classifier gradient updates. Main findings: (1) attention-guided training improves activation-based localization (Pixel-AUROC) by +18.0% for EfficientNetB0 with augmentation (p=0.005, Cohen's d=2.6) and +18.7% for ResNet50 (p=0.008), significant in four of eight CNN settings (uncorrected for multiple comparisons) with no significant change in classification; (2) for EfficientNetB0 a data x training-mode interaction is significant (p=0.002), consistent with a super-additive effect (+13.6% combined vs +1.6% summed individual effects); (3) architectures with weaker spatial representations benefit most, whereas ConvNeXt-T shows no effect, apparently because its depthwise-convolution activations yield spatially uninformative channel-mean maps; (4) unsupervised PatchCore remains the strongest localizer (Pixel-AUROC=0.983), contextualizing the supervised gains. These results show that existing evaluation masks can act as practical training signals that measurably and reproducibly improve where defect classifiers attend.

---


### 116. [One Model, Two Worlds: Bidirectional Sonar-Optical Translation](https://arxiv.org/abs/2609.06253)

**<font color=#1a73e8>作者：</font>** Shengji Jin, Trung Tien Dong, Ahmed Lamidi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Translating between imaging sonar and optical cameras is valuable for underwater perception, but supporting both directions with separate models duplicates storage and computation. A unified bidirectional model is therefore attractive, yet existing approaches largely treat the two directions symmetrically despite their fundamentally different image-formation physics. We argue that sharing a generative model does not require sharing the physics. We introduce the Direction-Asymmetric Realism Bridge (DARB), which retains a shared diffusion-bridge trunk while routing direction-specific physical priors through asymmetric pathways: range-aware modulation for sonar-to-optical translation and polar ray-dependent processing for optical-to-sonar translation. We further show that symmetry in training is also costly: applying a common realism schedule reduces sonar-to-optical PSNR by 2.60 dB. Our Adaptive Realism Supervision (ARS) instead determines when, where, and how strongly perceptual supervision is applied from reconstruction quality and gradient balance. Together, DARB and ARS enable one bidirectional model to match the sonar-to-optical specialist within 0.11 dB PSNR, outperform the optical-to-sonar specialist by 0.70 FID, and surpass two independently trained BBDMs on seven of eight metrics.

---


### 117. [SeaCausal-FL: Federated Fuzzy Causal Learning for Maritime IoT Fault Diagnosis and Counterfactual Reasoning](https://arxiv.org/abs/2609.06257)

**<font color=#1a73e8>作者：</font>** Yuhang Qiu, Haihan Zhu, Koteeswaran Seerangan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable marine-engine fault diagnosis in maritime IoT is challenged by distributed data ownership, heterogeneous fault distributions, and continuously changing operating conditions. This paper proposes SeaCausal-FL, a federated fuzzy causal learning framework that combines a shared temporal diagnostic path with mechanism-conditioned causal reasoning. An interval type-2 fuzzy layer represents uncertain and overlapping operating mechanisms, while each mechanism is associated with a physics-constrained structural causal model. Before aggregation, locally learned mechanisms are aligned using operating context, causal structure, and conditional intervention-response signatures. Model parameters are then aggregated according to sample, class, mechanism, and mechanism-class evidence instead of client sample size alone. The learned structural equations further support interval counterfactual reasoning through abduction, action, and prediction. Experiments on a marine-engine fault dataset and a real-data-calibrated semi-synthetic causal benchmark show that SeaCausal-FL achieves an average F1 score of 87.07% across four client partitions, with AUROC and AUPRC of 98.98% and 94.81%, respectively. It also maintains strong performance under unseen loads and fault-type omission during training. On the causal benchmark, SeaCausal-FL reaches an Edge-F1 of approximately 0.58 and an Edge-AUPRC of 0.68, reduces coefficient RMSE to about 0.14, and provides favorable counterfactual estimation and intervention decisions.

---


### 118. [Correction as Annotation: Bootstrapping a Dependency Parser for Documentary Medieval Latin](https://arxiv.org/abs/2609.06266)

**<font color=#1a73e8>作者：</font>** Gabriel H. Pizzorno  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medieval documentary sources remain inadequately served by existing natural language processing tools. None of the five readily available Latin treebank models attains usable performance on a collection of 160 inventories compiled in Marseille between 1258 and 1446. The best labelled attachment score is 0.62 and the best morphology-aware score is 0.24. Performance does not correlate with either genre or period proximity. To address this shortfall, in-domain training data was generated as a by-product of using these inadequate models. In each of nine iterations, a model pre-annotated 200 sentences; an expert corrected the annotations; and the corrected sentences were used to train the subsequent model, with batches sampled independently of model state, without active-learning selection. Thirty-three hours of annotation effort over 1,804 sentences increased universal part-of-speech accuracy from 0.80 to 0.98 and labelled attachment from 0.48 to 0.92, outperforming all baselines on the reported metrics while using 97% less training data than the largest one of them. Annotator effort declined from 54% of tokens to a plateau of 14-18%, an operational progress metric that requires no separate gold standard and can serve as a stopping criterion.

---


### 119. [SIDE: Sensor Impersonation Detection at the Edge via Sequence Prediction](https://arxiv.org/abs/2609.06271)

**<font color=#1a73e8>作者：</font>** Nahom Birhan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Some low-cost Internet of Things (IoT) sensor deployments lack device-level source authentication, leaving them vulnerable to impersonation or injected sensor readings. We present a lightweight approach to sensor impersonation detection in a small proof-of-concept study. We formulate detection as a sequence-prediction problem. A model with three LSTM layers and two fully connected layers is trained only on univariate temperature readings from a genuine sensor, and a window of readings is flagged when its mean absolute prediction error exceeds the mean genuine error by more than six standard deviations. The model is converted to TensorFlow Lite and deployed on an Arduino Nano 33 BLE in three variants, non-quantized (554 KB), 16-bit weight quantized (298.5 KB), and 8-bit weight quantized (185 KB). On a controlled testbed with the impostor sensor placed in a hotter outdoor location, the three variants reached detection accuracies of 99.980%, 99.972%, and 98.206%, and each flagged the change point when a test sequence switched from genuine to impostor data. Quantization made the model smaller but slower in our measurements. The genuine and impostor distributions were well separated, so these results show detection of a controlled distribution shift and should not be read as evidence of general device authentication.

---


### 120. [A Comparative Study of GAN-Based Deep Learning Models for Pneumonia Detection in Chest X-Rays](https://arxiv.org/abs/2609.06276)

**<font color=#1a73e8>作者：</font>** Roshan Paudel, Aashish Ghimire, Pramod Acharya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study evaluates pneumonia classification in chest X-rays using VGG19, MobileNetV2, ResNet50, and a custom CNN, and explores Generative Adversarial Network (GAN)-based synthetic data augmentation. MobileNetV2 achieved the highest reported accuracy of 88% with balanced class-wise performance. The custom CNN achieved pneumonia recall of 92.67% and precision of 79.43%, highlighting a precision-recall trade-off. Accuracy, F1-score, precision, recall, confusion matrices, and training curves were used to assess performance.
Synthetic pneumonia images were combined with real images to investigate whether augmentation could improve classification performance. In the reported VGG19 comparison, augmented-data training accuracy reached approximately 100%, while validation accuracy remained near 50%, below the real-data validation accuracy. This experiment therefore did not demonstrate a validation-performance benefit from GAN augmentation. The classifier comparison highlights differences in accuracy and pneumonia recall, while the augmentation experiment indicates the need for further evaluation of synthetic-image quality and training settings.

---


### 121. [Object-Aware Background-Controlled Editing via Weighted Velocity Guidance](https://arxiv.org/abs/2609.06288)

**<font color=#1a73e8>作者：</font>** Wuji Wang, Yue Wu, Chenhao Yi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free image editing steers diffusion or flow-matching generative models at inference time by modifying prompt-conditioned denoising velocities. Existing velocity-based editors often apply prompt-induced residuals globally over the latent space and rely on the model to localize semantic changes implicitly. For object-centric edits, these residuals are rarely zero outside the target object, so small non-target components can accumulate during multi-step integration, causing background drift and unstable object boundaries. We propose Object-Aware Velocity Control (OAVC), a training-free framework that introduces object-level control into the velocity-integration process. OAVC decouples where semantic residuals are allowed to act from how they are injected into the dynamics. It constructs a background-anchored reference interface under the source prompt and then performs object-localized safe semantic injection under the target prompt. A constrained injection operator suppresses drift-inducing velocity components, while time-adaptive spatial weighting stabilizes the transition near object boundaries. OAVC requires no training or modification of pretrained model parameters. Experiments on object-centric image and video benchmarks with image and video rectified-flow backbones show improved background preservation, structural fidelity, boundary stability, and temporal consistency while retaining effective localized editability.

---


### 122. [Representation Learning for Sample-Efficient CATE Estimation by Leveraging Multiple Outcomes](https://arxiv.org/abs/2609.06294)

**<font color=#1a73e8>作者：</font>** Maitreyi Swaroop, Shikha Bhat, Samantha Rodriguez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating conditional average treatment effects (CATE) enables efficient targeting of interventions, but many applications have limited experimental samples, making it difficult to estimate heterogeneous effects from high-dimensional covariates. In such settings, policymakers and medical practitioners often succumb to the curse of dimensionality or apply off-the-shelf dimension reduction methods that may not preserve treatment heterogeneity. Yet these domains often come with large historical datasets measuring a wide range of outcomes -- a source of supervision that is rarely exploited in practice. Following causal representation learning, we hypothesize that such domains with high-dimensional covariates have lower-dimensional underlying dynamics. We can thus leverage the diverse outcomes measured in historical data to learn a lower-dimensional representation of the covariates. Theoretically, we prove that when the auxiliary outcomes satisfy a set of surrogacy conditions and the representation retains relevant covariate information, the original CATE is identified when the high-dimensional covariates are replaced by the learned representation. Combined with existing dimension-dependent rates for CATE estimation, the result implies greater sample-efficiency on the same experimental sample. Additionally, we characterize the bias-variance tradeoff when the assumptions do not hold perfectly, and show that the representation-based estimator can still achieve lower error when the reduction in estimator variance outweighs the bias due to compression. Empirically, we evaluate the method on synthetic data and semi-synthetic medical data.

---


### 123. [SignDino: Self-Supervised Sign Language Representation Learning via Temporal-Axis Self-Distillation](https://arxiv.org/abs/2609.06296)

**<font color=#1a73e8>作者：</font>** Junyi Hu, Zhewen He, Haomian Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised sign language representation learning must model two properties not central to natural-image SSL: signs are produced by a small set of anatomically distinct articulators, and their meaning depends on the temporal organisation of those articulators. We introduce SignDino, a self-supervised sign-video encoder that moves the DINOv3 student--teacher recipe from the spatial domain of image crops to the temporal domain of tracked sign streams. Each video is decomposed into left-hand, right-hand, and face streams by a detector-first YOLOv8n+ByteTrack pipeline. A frozen DINOv3 ViT-B/16 embeds each per-frame anatomical crop, while lightweight temporal Transformers, not the image backbone, form the student and EMA teacher. They are trained by temporal DINO self-distillation, frame-level masked-token prediction in the style of iBOT, KoLeo feature spreading, and Gram anchoring of the frame-to-frame similarity structure. This design keeps strong image-level visual primitives fixed and learns only how articulator states evolve across time. We evaluate on sign-to-English translation, isolated sign recognition, and fingerspelling detection benchmarks. Across these tasks, SignDino provides a strong public self-supervised representation and shows competitive or state-of-the-art performance under matched downstream evaluation.

---


### 124. [CST-WM: A Causally Structured World Model for Embodied Visual Tracking](https://arxiv.org/abs/2609.06302)

**<font color=#1a73e8>作者：</font>** Junyi Hu, Shuaihang Yuan, Yi Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied visual tracking requires a robot not only to react to the current view, but to choose actions that preserve or recover future evidence of a moving target under ego-motion, occlusion, and distractors. It is therefore a predictive decision problem over future target observability and apparent scale. A central difficulty is a task-specific form of causal hallucination: in action-conditioned prediction, a model can exploit the strong correlation between robot control and target-related observations by hallucinating a direct causal effect from the current action to target evidence, rather than letting action influence that evidence only through robot motion and the resulting observation change. The shortcut yields plausible futures with the wrong semantics for tracking-oriented planning and re-acquisition. We propose CST-WM, a causally structured world model that decomposes the latent state into target-evidence, robot, and observation branches and factorizes the transition so that direct action injection into the target-evidence branch is blocked, while action remains available to robot motion and observation updates. Combined with rollout-based model-predictive control, CST-WM supports both stable following and temporary target re-acquisition in one planning framework. On EVT-Bench and Habitat 3.0, covering standard tracking, target-loss recovery, and cross-dataset transfer, it improves following quality, distance-range control, safety, and re-acquisition over reactive and world-model baselines; offline diagnostics show better multi-step rollout fidelity, stronger planning-value consistency, and substantially reduced direct action leakage. For embodied visual tracking, future prediction alone is not enough: the predictive structure itself must align with how target evidence enters planning.

---


### 125. [MARS: Detecting Unauthorized Variable Manipulations in Multi-Application PLC Runtimes](https://arxiv.org/abs/2609.06306)

**<font color=#1a73e8>作者：</font>** Syed Ghazanfar Abbas, Dongyan Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Programmable Logic Controllers (PLCs) increasingly run multiple applications alongside the main control program, with shared access to PLC variables. Yet, Industrial Control System (ICS) defenses primarily detect malicious updates by checking whether variable values violate expected bounds, without considering which application performed the update. A malicious application can exploit this gap by modifying variables within normal bounds while still driving the physical process toward an unsafe state. Even when such manipulation is detected, operators cannot identify the responsible application because PLCs do not associate variable updates with application identity.
We present MARS, an automated framework for application-level authorization and attribution of PLC variable manipulations. MARS profiles applications on an isolated virtual PLC (vPLC) to derive application-specific variable-access policies and uses a shadow vPLC during operation to attribute production-PLC updates to individual applications without instrumenting the production controller. MARS also detects manipulations that occur only on the production PLC and therefore have no corresponding update on the shadow vPLC. We evaluate MARS on manufacturing, chemical, and water-treatment systems against attacks in which unauthorized applications manipulate PLC variables while remaining within normal bounds. Our results show that MARS detects these manipulations and identifies the responsible application.

---


### 126. [FrankenReport: Early Exiting in Long-Form Generation Using Expected Value of Computation](https://arxiv.org/abs/2609.06320)

**<font color=#1a73e8>作者：</font>** Zhengping Jiang, Gonzalo Ramos, Jina Suh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While deep research systems address interactive information-seeking needs impressively, their real-world deployments face latency and resource-consumption challenges. We present FrankenReport, an interface for long-form knowledge-seeking report generation that supports adaptive early exiting per section: it evaluates intermediate outputs during generation and predicts whether further targeted computation will yield significant quality gains. In a simulation study, FrankenReport outperforms random allocation baselines by a large margin (up to 4x) under low budgets and smoothly recovers full-pipeline quality as the budget grows, showing that future quality gains are predictable from intermediate drafts. Through experiments and user studies, we further show that despite varying preferences across users and topics, FrankenReport adapts to simple, natural user feedback as efficiently as methods requiring much costlier supervision such as generated drafts and explicit rationales.

---


### 127. [Inevitability of Encrypted Traffic Side-Channel Leakage in the Multi-Class Setting](https://arxiv.org/abs/2609.06322)

**<font color=#1a73e8>作者：</font>** Guangjie Liu, Guang Cheng, Weiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Side-Channel Existence Theorem proves $I(X;Y)>0$ in the binary, undefended setting, but is confined to pairwise arguments and ignores active defenses. We extend it to $k$ classes via the per-class decomposition $I(X;Y)=\sum_i\pi_i D_{\mathrm{KL}}(P_{Y|i}\|P_Y)$, with defense cost modelled by per-class Wasserstein-1 constraints $\sup_x W_1(Q_x^D,P_x)\le B$. Three results follow: (1) a summation-form MI lower bound over all active classes; (2) a cascade critical cost theorem and a per-class budget corollary, nonzero where the uniform-budget bound vanishes; (3) an accuracy corollary $\mathrm{Acc}^*\ge 2^{I_0}/k>1/k$. On a 95-class website fingerprinting dataset the measured MI has a strictly positive $95\%$ confidence lower bound under every defense tested. Against the strongest pairwise baseline---a convex program over all $\binom{k}{2}$ triangle constraints, also $\Theta(1)$ in $k$ under the same non-vanishing-gap conditions---the summation form is only $1.45\times$ stronger, so the case for the per-class decomposition is structural: only it gives each class a critical cost and a cascade. FRONT's apparent $122\times$ gap is inflated mainly by threshold exclusion rather than the inequality chain: on the active classes it is $21\times$, within $1.4\times$ of the $15\times$ measured undefended. Measuring the chain's two steps separately bounds the collapse onto one Lipschitz statistic below by $28\times$, against a divergence step measured at $1.5\times$. Undefended OVR distinguishability predicts post-defense per-class leakage at Spearman $\rho=0.62$--$0.77$, the transfer the certification procedure relies on. The framework carries over unchanged to a 100-class QUIC/TCP pair.

---


### 128. [One Shared LoRA Weight for MRI Reconstruction across Acceleration Factors](https://arxiv.org/abs/2609.06338)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhao, Weikang Gong, Zhongnian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accelerated MRI reconstruction recovers images from undersampled k-space. However, different acceleration factors produce distinct artifact patterns. Existing methods often train separate models for each factor, leading to poor cross-factor generalization and high training and storage costs. We propose Shared LoRA, a parameter-efficient framework that freezes the pretrained SHFormer backbone and trains a single shared set of LoRA adapters together with a lightweight gating network. During training, undersampled inputs are generated by randomly sampling acceleration factors and their corresponding sampling masks, enabling the shared adapters to learn reconstruction knowledge across factors. Given the acceleration factor, GateNet generates layer-wise coefficients to dynamically modulate the residual strength of each adapter. Experiments show that Shared LoRA achieves the best or competitive PSNR and SSIM across acceleration factors, while its trainable parameters account for only about 5.3% of the total model parameters. Its performance at lower acceleration factors remains largely unaffected as the jointly trained factor set expands, and it generalizes stably to unseen neighboring factors.

---


### 129. [Radiation, Rotation and Scale Invariant Feature Descriptor for Multimodal Image Matching](https://arxiv.org/abs/2609.06343)

**<font color=#1a73e8>作者：</font>** Yuanxin Ye, Tengfeng Tang, Tao Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal image matching is a fundamental task for multi-source information fusion. However, geometric distortions and nonlinear radiometric differences (NRD) severely limit performance, especially under radiometric, rotation, and scale variations. To address this issue, we propose a radiation, rotation, and scale invariant (RRSI) feature descriptor. First, a dual-head regional sampling (DHRS) module simultaneously performs Cartesian and Log-Polar sampling on keypoint neighborhoods, retaining spatial structural properties while enhancing robustness to rotation and scale variations. We then jointly encode geometric and radiometric relations between multimodal images in a unified deep feature space, enabling feature encoding, interaction, and fusion across intra-modal, dual-head sampled, and inter-modal regions. Furthermore, we introduce a bidirectional cross-modal generative reconstruction constraint during training. By decoding implicit features into structural patches of the counterpart modality, this mechanism anchors modality-invariant geometric topologies without additional inference overhead. Experiments on optical-infrared and optical-SAR datasets demonstrate highly competitive matching performance and strong robustness to rotation and scale variations. RRSI supports the full rotation range from 0 to 360 degrees and scale factors up to four. Its generalization ability is further validated on multimodal images from computer vision, remote sensing, and medical imaging. The implementation will be made publicly available at this https URL .

---


### 130. [Robust Dynamic Expansion for Continual Learning under Backdoor Attacks via Purification and Selective Recovery](https://arxiv.org/abs/2609.06346)

**<font color=#1a73e8>作者：</font>** Keyu Lin, Fei Ye, Qihe Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) enables models to acquire new knowledge from sequentially arriving tasks while retaining previously learned knowledge. However, in practical scenarios, task streams collected from untrusted sources may contain backdoor-poisoned samples, posing a critical challenge to the stability, plasticity, and security of continual learners. In this work, we investigate a challenging setting termed Continual Learning Under Backdoor Attack (CLUBA), where each incremental task may involve a small proportion of maliciously manipulated training samples. Unlike conventional continual learning or backdoor defense scenarios, CLUBA requires models to simultaneously mitigate catastrophic forgetting, preserve adaptation capability, and prevent the absorption of malicious supervision during sequential updates. To address this challenge, we propose a robust dynamic-expansion framework that integrates sample purification, selective recovery, and robust expert routing into a unified continual learning paradigm. Specifically, we introduce Bi-Prototype Purification (BPP) to identify suspicious samples by exploiting semantic discrepancies in feature space. Based on purified data, Gradient Discrepancy-based Robustness Optimization (GDBRO) selectively recovers informative poisoned samples through pseudo-label correction and gradient consistency evaluation, improving robustness while maintaining model plasticity. Furthermore, Robust Feature Consistency-based Expert Selection (RFCBES) constructs perturbation-aware class prototypes to enable reliable expert routing under corrupted or shifted inputs.

---


### 131. [ChildGaze: A Benchmark Dataset for Collaborative Behavior Understanding in Children](https://arxiv.org/abs/2609.06353)

**<font color=#1a73e8>作者：</font>** Sindhuja Penchala, Saketh Reddy Kontham, Prachi Bhattacharjee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding collaborative behavior in children is important for analyzing social participation, peer interaction, shared attention, and engagement during play and learning activities. Reliable recognition of these cues can support research in child development, educational analysis, and human-centered computer vision. However, estimating where a child is looking does not necessarily reveal whether the child is actively participating in a shared activity. To support this higher-level analysis, we introduce ChildGaze, a child-centered behavioral annotation dataset built on the ChildPlay video collection [1]. ChildGaze introduces two behavioral labels, collaborative and non-collaborative, assigned independently to each child within a frame. The dataset provides face, left-hand, and right-hand bounding boxes for children and adults and organizes the annotations at the row, person, and frame levels. The current release contains 27 annotated video files, 10,641 frames, and 73,268 body-part annotation rows. Annotation reliability was evaluated on 1,187 frames using independent annotations from two annotators. The collaboration labels achieved 93.16% raw agreement and a Cohen's kappa of 0.8631, while bounding-box annotations achieved an overall mean IoU of 0.808. Baseline experiments with pretrained ViT and Swin Transformer models achieved up to 97.44% child-person-level accuracy and 96.80% frame-level accuracy, respectively. These results show that ChildGaze provides a reliable benchmark for studying collaborative behavior in naturalistic child-adult and peer interactions.

---


### 132. [Adaptive stabilization of a leaderless bearing-constrained formation with disturbances](https://arxiv.org/abs/2609.06355)

**<font color=#1a73e8>作者：</font>** Minh Hoang Trinh, Chuong Van Nguyen, Quoc Van Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we consider the problem of regulating and maintaining a target formation characterized by a set of bidirectional bearing constraints under disturbances. The agents in the formation are modeled by single integrators with bounded continuous disturbances of which the upper bound is unavailable for the control design. Due to the time-varying disturbances, the target formation is time-varying. We propose adaptive sliding mode control laws to uniformly globally asymptotically stabilizes the moving target formation and reject the matched disturbances. In addition, to alleviate chattering phenomena from sliding mode control, smooth adaptive control laws are then designed to guarantee uniform global boundedness of the desired formation. Finally, simulation results are given to support the analysis.

---


### 133. [MSCA-UNet: Multi-Scale Context and Attention U-Net for Image Segmentation](https://arxiv.org/abs/2609.06356)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> U-Net remains a practical baseline for image segmentation because of its simple encoder-decoder structure and skip connections. However, the bottleneck representation is still dominated by a limited set of receptive fields, while decoder features are propagated without explicitly emphasizing the most informative channels and spatial locations. This paper presents MSCA-UNet, a U-Net-based segmentation architecture that combines multi-scale contextual aggregation at the bottleneck with channel-spatial attention refinement in the decoder. The multi-scale module uses parallel atrous convolutions to capture contextual features at different receptive fields, while Convolutional Block Attention Modules (CBAMs) progressively recalibrate decoder features. Under identical experimental settings, the baseline U-Net achieves 96.9% mIoU on a held-out test set. Adding multi-scale context improves mIoU to 97.5%, while attention alone reaches 98.4%. Combining both mechanisms yields 99.1% mIoU, a 2.2 percentage-point improvement over the baseline. Parameter analysis further shows that the attention-only variant adds approximately 0.044M parameters, whereas the multi-scale module contributes most of the additional model capacity. The results support the view that multi-scale context enrichment and attention-based feature refinement provide complementary benefits within a U-Net framework.

---


### 134. [AGSA-Net: Abundance-Guided Self-Attention Network for Spectral Unmixing-Aware Hyperspectral Remote Sensing Image Classification](https://arxiv.org/abs/2609.06359)

**<font color=#1a73e8>作者：</font>** Nafisa Anjum, Satavisa Dey Borno, Ananna Saha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) classification plays a vital role in remote sensing applications, including agriculture, environmental monitoring, and urban analysis. However, its performance remains challenged by high spectral redundancy, noise sensitivity, and the difficulty of jointly modeling local material composition and long-range spectral dependencies. To address this, we propose AGSA-Net, an abundance-guided self-attention network that explicitly integrates spectral unmixing priors into the classification process. AGSA Net first estimates physically meaningful subpixel abundance maps subject to non-negativity and sum-to-one constraints, regularized by hybrid linear-nonlinear reconstruction decoder. The learned abundances are then used to construct an abundance affinity prior that guides a spectral transformer to emphasize class-discriminative interactions, and the resulting transformer features are fused with compact abundance descriptors for final prediction; in contrast to existing approaches that use abundance as auxiliary or concatenated features. Experiments on Indian Pines, Augsburg, and Berlin demonstrate the benefit of incorporating abundance- guided contextual modeling, particularly in heterogeneous urban scenes. The source code and trained models are available at: this https URL

---


### 135. [DualPathOcc: Dual-Resolution BEV Encoder for 3D Occupancy Prediction](https://arxiv.org/abs/2609.06370)

**<font color=#1a73e8>作者：</font>** Lihao Qiu, Jian Chen, Ruihao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting 3D occupancy from multi-view images requires preserving geometric detail during 2D-to-3D lifting while reasoning over sparse, volumetric scene representations. We present DualPathOcc, a camera-based framework that combines a Spatial Enhancer for high-resolution feature aggregation before BEV compression, a SENet-augmented dual-path BEV encoder for local-global context modeling, and height-aware weighted cross-entropy for near-ground occupancy. The final model is optimized with occupancy supervision and no explicit depth loss. On single-frame Occ3D-nuScenes, DualPathOcc achieves 37.37 mIoU. We further analyze how surface-centered depth targets interact with volumetric occupancy learning.

---


### 136. [Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation](https://arxiv.org/abs/2609.06373)

**<font color=#1a73e8>作者：</font>** Jiawei Mao, Haoqin Tu, Hardy Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating long-form multi-shot videos requires coherent within-shot motion and visually consistent narratives across shots. Existing video generators favor continuous motion and struggle to present complete shot sets when an entire narrative is packed along one temporal axis. We propose MovieGrid, a Multi-Grid Post-Training paradigm that decomposes a long video into shorter, temporally ordered chunks and arranges them on a spatial grid for joint modeling. This design reduces the number of shots handled by each temporal axis while enabling global information exchange across chunks. We construct the Multi-Grid Long Video (MGLV) dataset from 1,000 long-form videos using source video collection, hierarchical segmentation, grid video construction, and character-aware story annotation, producing 54K grid videos paired with story prompts. Our Noise-Free Random-Grid Training retains a random subset of chunks as clean visual context for denoising the remaining chunks. Grid Embedding encodes grid structure, character-aware Story Prompts link recurring entities, and Grid Boundary Loss stabilizes layouts. Under the same token budget, MovieGrid generates 6.05 times more shots than Temporal Packing in a 1,616-frame video. On a benchmark spanning five real-world categories, it achieves state-of-the-art intra-shot consistency (0.9131 versus 0.8086 for HoloCine) and inter-shot consistency (0.5914 versus 0.5384 for StoryMem). MovieGrid can further scale video length with minimal compromise through single or multiple generations.

---


### 137. [Parameterized and Streaming Algorithms for Euclidean Fair $k$-Center Clustering](https://arxiv.org/abs/2609.06384)

**<font color=#1a73e8>作者：</font>** Zeyu Lin, Chaoqi Jia, Longkun Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by the growing importance of fairness in machine learning, fair $k$-center clustering has attracted considerable research attention as a fundamental problem. In this problem, a dataset is partitioned into $m$ disjoint groups, and the objective is to select $k$ data points as centers, subject to upper bounds on the number of centers chosen from each group, aiming to minimize the maximum distance between any data point and its assigned center. Focusing on Euclidean spaces, which are ubiquitous in machine learning applications, we first develop a parameterized approximation algorithm for Euclidean fair $k$-center with an approximation ratio of $2.732$. By incorporating this algorithm as a post-processing stage into a one-pass streaming framework for large-scale data, we obtain an approximation ratio of $4.464$. These ratios can be further respectively improved to $2.414$ and $3.828$ with a runtime exponential on $k$. To ensure polynomial-time complexity, we further design a one-pass streaming algorithm with an approximation ratio of $4.732$, which can be further improved to $4.42$, outperforming the state-of-the-art ratio. Finally, extensive experiments show that our methods significantly outperform state-of-the-art approaches in terms of clustering accuracy.

---


### 138. [Scaling 3D Generative Priors to Large-Scale Scene Meshes from Multi-View Images](https://arxiv.org/abs/2609.06385)

**<font color=#1a73e8>作者：</font>** SangEun Lee, Wonseok Chae, Hoyoung Yoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained 3D generative models produce detailed geometry and appearance but are primarily designed for object-centric generation within a limited spatial extent. Recent approaches address this limitation by partitioning large scenes into smaller spatial regions and applying pretrained 3D generative priors to each region. However, scaling tiled generation to large multi-view scenes makes it challenging to maintain local geometric continuity and global appearance consistency.
We present a training-free framework for large-scale textured mesh generation from multi-view images. Our key idea is to scale tiled generation to large scenes with increased spatial detail while coordinating generation both locally and globally. We introduce local context tiled generation to improve geometric continuity between neighboring regions and global appearance alignment to reduce appearance discrepancies across distant regions. An adaptive scene decomposition further determines the number of tiles according to the input scene geometry. Experiments demonstrate improved geometric and appearance fidelity over existing approaches while enabling fine-grained generation of large-scale scenes.

---


### 139. [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396)

**<font color=#1a73e8>作者：</font>** Zihan Tan, Leixin Sun, Zitong Shi 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) lets a system improve the model-building machinery from its own failures, so every later model inherits the gain. Yet RSI has been validated almost exclusively on coding and formal benchmarks such as science QA and mathematics. This format bound limits RSI to improvement within a machine-checkable slice, not general capability where questions are open and correctness is settled by argument, replication, or measurement. We argue RSI must next operate across real, diverse scientific, engineering, and meta-scientific domains, not where formal evaluation is merely tractable. To that end we present MetaRSI-v1, where improvement is the scheduled composition of three typed operators over one unified paradigm. Data-RSI amplifies existing competence and marks its boundary; Harness-RSI edits a five-slot scaffold without touching weights; Model-RSI internalizes capability into parameters through bounded training. Sharing one loop kernel and artifact vocabulary, they make data, scaffold, and model changes composable rather than exclusive. A two-axis optimizer jointly decides operator order and each operator's proposal policy, while a meta-level policy revises the schedule across terms. We validate MetaRSI-v1 under the field's standard evaluations, on code and closed-form science, with no external teacher: the target model plays every role in its own loop. MetaRSI-v1 reframes self-improvement from a single-surface edit to a composition across the full model-production pipeline, opening two paths: a model route internalizing capability through training, and a harness route leaving weights untouched and thus extending self-improvement to any model reachable through an interface, with Data-RSI redefined as the shared substrate feeding both. The framework further yields refutable laws on where loops exist, how operators compose, and what supervision buys.

---


### 140. [Hierarchical Wasserstein Merging for Multi-Domain Multi-Task Learning: From Specialists to a Generalist](https://arxiv.org/abs/2609.06406)

**<font color=#1a73e8>作者：</font>** Ming Cheng, Jiaying Gong, Hoda Eldardiry  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-domain multi-task learning (MD-MTL) aims to build a single generalist model that performs well across heterogeneous domains and tasks. However, joint training often suffers from interference under distribution shifts. Existing model merging methods mostly operate on model parameters while overlooking the geometric structure of latent representation distributions across domains and tasks. To address these limitations, we propose Hierarchical Wasserstein Merging (HWM), a representation-level framework that models each domain-task specialist as a distribution of hidden representations on a shared support. HWM constructs task-level and global Wasserstein barycenters to capture within-task domain variation and cross-task structure, enabling either training-free specialist aggregation by Wasserstein-derived weights or training-based generalist learning through a hybrid Wasserstein alignment loss. Experiments on four NLP tasks across four domains per task show that HWM achieves superior effectiveness and generalization capability in MD-MTL settings.

---


### 141. [FoldNTT: A Multiplier- and Twiddle-Lean NTT Core with Formally Verified Arithmetic for Proth Primes](https://arxiv.org/abs/2609.06412)

**<font color=#1a73e8>作者：</font>** Masato Kamba  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware for lattice-based post-quantum cryptography spends a large share of its area on the number-theoretic transform (NTT), dominated by modular multipliers and twiddle storage. FoldNTT is a redesign of the released radix-2 CFNTT accelerator (TCHES 2022) for the Falcon / FN-DSA prime q = 12289 with one hardware multiplier per butterfly instead of three and about half the stored twiddle constants. The Proth shape q = 3*2^12 + 1 turns modular reduction into shift-and-add K-RED folds, and the bit-reversed twiddle table obeys w[N/2+j] = psi*w[j], so half the table is derived without a multiplier. Checking the released RTL against the mathematics also exposed a bug: its inverse transform omits a per-stage halving and returns 2^10*x, which the retrofit corrects. Every arithmetic block is proven by exact-width SMT and compositional SymbiYosys proofs, control-safety invariants by k-induction; the proofs are mutation-tested and the composed transform is validated by simulation, all rerun by CI. On Artix-7 in a fully open flow, the retrofit costs 3->1 DSP48 per butterfly and -50% stored twiddle bits at a whole-core Fmax cost of about 4% (best of three seeds; within the seed-to-seed spread), measured on the released datapath driven by a controller we reconstructed (the reference FSM was never released) and validated by full-core simulation; a sequential core with our own controller builds to a timing-gated Basys-3 bitstream.

---


### 142. [On BatchNorm Forward Modes in Value-Based Reinforcement Learning](https://arxiv.org/abs/2609.06421)

**<font color=#1a73e8>作者：</font>** Daniel Palenicek, Mikael Henaff, Scott Fujimoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Batch normalization (BN) substantially improves sample efficiency in continuous-control actor-critic methods such as CrossQ, yet recent studies report performance degradation in discrete-action value learning on Atari. These failures are surprising because discrete Q-networks lack the action-input distribution mismatch identified by CrossQ. We show for target-based C51 and target-free PQN that the simple choice between running and batch statistics at specific forward passes can reverse this degradation. In C51, switching the BN bootstrap forward to batch-statistic mode significantly improves performance over unnormalized and LayerNorm baselines and scales stably with update-to-data ratios up to 12. In PQN, using batch-statistics for both action selection and bootstrapping recovers performance from the failing running-statistic configuration. Across 26 Atari games at 400M frames, this configuration achieves a higher final aggregate score than PQN with LayerNorm. Our results show that carefully configured BN can substantially improve discrete-action value learning, and that its forward protocols are an essential part of the algorithm specification.

---


### 143. [Sparse Oblique Rule Boosting for Simpler Additive Rule Ensembles](https://arxiv.org/abs/2609.06426)

**<font color=#1a73e8>作者：</font>** Shahrzad Behzadimanesh, Pierre Le Bodic, Geoffrey I. Webb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small additive ensembles of symbolic rules offer interpretable prediction models. Traditionally, these ensembles use rule conditions based on conjunctions of simple threshold propositions $x \geq t$ on a single input variable $x$ and threshold $t$, resulting geometrically in axis-parallel polytopes as decision regions. While this form ensures a high degree of interpretability for individual rules and can be learned efficiently using the gradient boosting approach, it relies on having access to a curated set of expressive input features so that a small ensemble of axis-parallel regions can describe the target variable well. Absent such features, reaching sufficient accuracy requires increasing the number and complexity of individual rules, which diminishes the interpretability of the model. Here, we extend classical rule ensembles by introducing logical propositions with learnable sparse linear transformations of input variables, i.e., propositions of the form $\mathbf{x}^T\mathbf{w} \geq t$, where $\mathbf{w}$ is a learnable sparse weight vector, enabling decision regions as general polyhedrons with oblique faces. We propose a learning method using gradient boosting based on a weighted logistic regression. Empirical results across 14 regression and classification tasks demonstrate that the proposed method achieves lower model complexity than competitive baselines while maintaining similar or better predictive accuracy. Hence, the approach provides a favorable trade-off between interpretability and accuracy and reduces the reliance on manual feature engineering.

---


### 144. [Stability and Generalization of Straight-Through Estimators for Training Two-Layer Quantized Neural Networks](https://arxiv.org/abs/2609.06430)

**<font color=#1a73e8>作者：</font>** Yiming Ying  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the identity straight-through estimator (STE) for training a two-layer binary-activation network with hinge loss from the perspective of Statistical Learning Theory (SLT). Our central question is whether algorithmic stability can explain the statistical generalization of the estimator produced by the discontinuous STE training rule. In the saturated-output regime, the zero-initialized samplewise STE recursion is exactly the stochastic subgradient descent on the convex latent loss $(-yu^\top x)_+$. This representation makes a stability analysis possible. We derive an exact distance identity for two coupled updates and prove approximate non-expansiveness of the common-example map, with a quadratic defect only when the two latent margins straddle zero. We then obtain explicit $\ell_2$ on-average model-stability and generalization bounds, transferring stability isometrically from the latent vector to the full first-layer matrix. Combining stability with a standard optimization bound yields an explicit excess induced-risk guarantee and the rate $O(n^{-1/2})$ when $T=n^2$. Under margin separability, a complementary argument gives the optimal-order $O(R^2/(\gamma^2n))$ expected excess misclassification error for a randomized one-pass STE iterate and a corresponding majority-vote bound.

---


### 145. [Can People Distinguish Human and AI Agency in Humanoid Teleoperation? A Preliminary Study of Agency Perception](https://arxiv.org/abs/2609.06434)

**<font color=#1a73e8>作者：</font>** Xiang Li, Koya Dendo, Keigo Minamida 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Can people distinguish between human and AI agency in humanoid teleoperation? To explore this question, we developed \textit{Ghost-in-the-Loop}, a teleoperation framework that supports both human-operated and AI-generated control of a robot's voice, facial expressions, and gestures while maintaining a consistent embodiment. We conducted a preliminary online study ($N=50$) in which participants viewed short interaction clips generated by either a Human Operator or an AI Control and judged the perceived source of control. Results suggest that participants often struggled to distinguish between the two conditions in brief interactions. Qualitative responses indicate that judgments were primarily influenced by perceived naturalness, temporal coordination, and consistency across speech, facial expression, and gesture. These findings provide initial insights into agency perception in embodied human--AI communication and motivate future investigations of blended human--AI telepresence systems.

---


### 146. [PLSR: Progressive and Localized Super-Resolution of 3D Objects via Localized Latent Voxel Diffusion](https://arxiv.org/abs/2609.06436)

**<font color=#1a73e8>作者：</font>** Yuxin Liu, Minshan Xie, Jiawen Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution 3D asset generation is vital in various 3D applications. Existing state-of-the-art diffusion-based models remain constrained by fixed resolutions, limiting their ability to produce details. In this paper, we tackle the challenge of generating more detailed, higher-resolution 3D objects by introducing a 3D super-resolution (SR) framework built on existing 3D generative foundation models. To this end, we design PLSR, a progressive and localized super-resolution solution to achieve this goal effectively and memory efficiently. Technically, given a coarse geometry from a pretrained 3D generator, we decompose the global SR task into localized sub-tasks via an associative input decomposition scheme, adapt a flow-based 3D generator into a localized super-resolution model through low-cost finetuning, and unify them in an iterative patch-wise denoising pipeline for seamless high-resolution output. Experiments on challenging objects show that our approach is able to generate 3D details with new strong fine-detail fidelity while significantly reducing the computational cost, offering a new and practical solution for high-resolution 3D asset generation.

---


### 147. [Large-Scale Pretraining for Improving Deep Learning-Based Geometric Distortion Correction of Diffusion-Weighted Imaging](https://arxiv.org/abs/2609.06437)

**<font color=#1a73e8>作者：</font>** Saroj Khanal, Yashawant Kumar Yadav, Kritam Bhattarai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-weighted imaging (DWI) is widely used in clinical settings but remains vulnerable to geometric distortion. Conventional correction methods often require additional acquisitions or vendor-specific solutions, limiting their feasibility in high-throughput, resource-constrained settings. This study investigates whether large-scale pretraining strategies can improve deep learning-based distortion correction for single-phase-encoding DWI. We formulate the task as image reconstruction, and compare a non-pretrained baseline against a self-supervised and a generative pretrained model, evaluated using both quantitative image-similarity metrics and qualitative expert assessment. The best-performing model was further tested for transferability on data collected in an LMIC setting with acquisition shift. Pretrained models outperformed the non-pretrained baseline, with cWDM achieving the strongest results across both quantitative and qualitative evaluation. However, application to LMIC data revealed transferability challenges, including contrast alteration and over-reliance on T1-weighted anatomical structure. Registering images to a common standard space improved predictions, suggesting that harmonized preprocessing may enhance cross-domain deployment.

---


### 148. [Causal Attribution for Agentic Decisions: Estimators, Coupling, and a Traceability Specification](https://arxiv.org/abs/2609.06445)

**<font color=#1a73e8>作者：</font>** Ajay Pravin Mahale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A provider of a high-risk AI system must keep records that make a decision traceable, and for agentic systems it has not been established what those records must contain for post-hoc causal attribution to be possible. We give the estimator framework and then the conditions under which it fails. We separate the marginal total effect that prior work measures from a common-random-numbers total effect that isolates a step's own contribution, add the natural direct effect under a pinned downstream, and check the estimators against hand derivations. Both estimands then fail, in the same direction. Under the marginal estimand a causally inert step has the identical total effect to the decisive one on every run of our planted chain, an algebraic identity and not a coincidence at one draw. Under common random numbers the decisive step returns exactly zero on the runs where the executing step flips, about one in ten, while its direct effect there is 0.25 and it demonstrably acts; an exact zero does not certify that a step did nothing, and we put that here rather than in the limitations. We derive the coupling that keeps the direct effect estimable once contexts diverge, with a closed form for its degradation, and show that the mediated share on which a natural ranking is built is not a share under suppression: where the direct and mediated paths oppose, it exceeds one and ranks a suppressed component above a pure mediator. We publish the discrepancy experiment's pre-registration rather than a result, because the live pipeline it requires was not available in the study window. We contribute the traceability specification such a filing would need, against a gap the Act's calendar opens: Article 86's right to an explanation has applied since 2 August 2026, while the Article 12 logging and Annex IV documentation that could evidence one were deferred to 2 December 2027 by Regulation (EU) 2026/1744.

---


### 149. [A Theoretical Framework for Masked Pretraining (MPT)](https://arxiv.org/abs/2609.06460)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Runyu Zhou, Yifei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, Masked Pretraining (MPT) based on reconstruction pretraining tasks has risen to a promising self-supervised learning paradigm across various domains and achieves remarkable performance in multiple downstream tasks. However, the theoretical understanding of the working mechanism behind MPT is still limited. In this paper, we introduce a new theoretical framework to analyze MPT and understand the crucial role of masking in extracting meaningful representations. We establish theoretical connections between MPT and another popular self-supervised paradigm: contrastive learning. We prove that the masking technique implicitly creates positive pairs that are semantically similar and the reconstruction loss pulls them together in the feature space. Besides, as a result of the implicit alignment, we point out the dimensional collapse issue of MPT and propose a Uniformity-enhanced MPT (U-MPT) loss that can effectively address this issue and bring significant improvements in downstream tasks including linear evaluation, cross-dataset fine-tuning and out-of-distribution generalization on real-world data sets. Furthermore, we establish downstream guarantees of U-MPT and theoretically analyze the influence of masking strategies. Based on the theoretical analysis, we propose a new masking strategy which enhances the downstream performance of MPT and explains current improvements of masking strategies with our theoretical perspective.

---


### 150. [Local and Global Stability in Performative Reinforcement Learning](https://arxiv.org/abs/2609.06467)

**<font color=#1a73e8>作者：</font>** Debmalya Mandal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In performative reinforcement learning the deployed policy shapes the environment that generates the learner's future data, and the natural solution concept is a performatively stable policy that is optimal in the environment it induces. Existing convergence guarantees rely on Lipschitz sensitivity assumptions on the environment map $\pi \mapsto (P_\pi, r_\pi)$, which are hard to verify and fail in settings such as multi-agent best-response dynamics. We instead study stability for mixtures of policies, and show that the resulting picture is fundamentally different from performative prediction, where randomization removes the need for any sensitivity assumption. We distinguish local mixed stability, an occupancy-weighted first-order relaxation that we show is equivalent to stationarity, from global mixed stability, which certifies against arbitrary deviating policies. Our first result is that a weighted per-state Hedge dynamic drives the local stability gap to zero at an $O(1/\sqrt{T})$ rate for an arbitrary, possibly discontinuous, environment map, both with exact and with trajectory feedback. The two notions genuinely differ: we exhibit an instance where local stability is achieved exactly but every mixture has global stability gap bounded away from zero. For global stability we introduce a bounded transition range assumption, strictly weaker than Lipschitz sensitivity, under which unweighted per-state Hedge converges up to a floor of $O(\gamma\epsilon_P/(1-\gamma)^3)$, and we prove a matching-in-$\epsilon_P$ lower bound of $\Omega(\gamma\epsilon_P/(1-\gamma))$ under trajectory feedback, so this floor is unavoidable. Finally, we extend both notions to $n$-player performative Markov games, obtaining local stability with no assumption on the joint environment map or game structure, and global stability for performative Markov potential games.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
