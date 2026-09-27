# 📦 其他研究 | 2026年09月28日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 151. [CoSWA-YOLOv12: Scale-Invariant Tiny Object Detection and Segmentation of Malaria Parasites](https://arxiv.org/abs/2609.29527)

**<font color=#1a73e8>作者：</font>** Ahmed Tahiru Issah, Carine Mukamakuza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated microscopy could widen access to malaria diagnosis in low-resource settings, but the deadliest species, P. falciparum, presents in its early ring stage as an object only a few tens of pixels wide. Such tiny targets are systematically under-detected: overlap-based label assignment starves them of positive samples, and overlap-based box regression gives weak gradients at their scale. The Normalized Gaussian Wasserstein Distance (NWD) repairs both effects, but applied uniformly across a slide that also holds objects three to four times larger it loosens their supervision and erodes their localisation, so overall accuracy can fall even as the tiny class improves. We present CoSWA-YOLOv12, a compact YOLOv12 instance-segmentation detector whose core Cooperative Scale-adaptive Wasserstein Assignment routes the Wasserstein treatment to an object in inverse proportion to its size, tapering back to standard assignment for larger species. Two further components support it: a wavelet detail residual, and a min-max Gaussian regression loss (M2-NWD). All three additions are transfer-safe: each reproduces the standard pretrained model exactly at initialisation, so public pretrained weights load without any loss of accuracy. On a five-class Rwandan thick-smear dataset, CoSWA-YOLOv12 raises P. falciparum recall from 0.63 to 0.74 and mAP@50 from 0.73 to 0.81 (mask), cuts missed P. falciparum from 38% to 15%, and improves strict-localisation mAP@50-95 on all five classes for both detection and segmentation, while a 2x2 ablation shows the scale gate and the regression loss are synergistic.

---


### 152. [A Corpus of Real Scam- and Spam-Call Conversations from an Active Voice-Agent Honeypot](https://arxiv.org/abs/2609.29528)

**<font color=#1a73e8>作者：</font>** Ethan Traister, Dennis Tsang Ng, Siyu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Real conversations between fraudsters and their targets are among the most informative artifacts for studying telephone scams, yet also the scarcest: passive honeypots overwhelmingly capture automated messages and hang-ups, large-scale studies characterize call metadata rather than dialogue, and manual scam-baiting does not scale. We present a dataset of real scam-call conversations collected by an active voice-agent honeypot. Dedicated numbers are seeded into the lead-generation channels fraud operations harvest; inbound callers are answered by a low-latency conversational agent that adopts a plausible target persona and sustains the interaction while every call is recorded, transcribed, and automatically labeled. Over an initial 53-day window we captured 10,015 inbound scam and spam calls (6,601 with two or more turns): roughly 895 hours of audio and 328,869 transcribed turns from 5,665 distinct originating numbers. Under a holistic classifier the substantive calls are predominantly predatory-but-legal lead generation ("spam", about three in five), while about one in seven is an outright "scam" (949 in this snapshot). Each call carries a turn-level transcript, three-channel audio, per-turn latency telemetry, and layers of automatic labels, including a holistic scam/spam/legitimate judgment corroborated by independent human review (75% agreement on the binary decision). We describe the collection system, the record structure, and technical validation of the corpus's realism and label quality, including that the agent is recognized as non-human in only about 5% of engaged calls. We also benchmark established scam-detection methods, where detectors trained on published synthetic dialogue collapse in precision on real traffic.

---


### 153. [The Impossible Trinity of Time-Series Validation: A Conservation Law among Training Sufficiency, Test Coverage, and Temporal Causality](https://arxiv.org/abs/2609.29530)

**<font color=#1a73e8>作者：</font>** Jiayu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Validating a model on a time series asks for three things at once: each training run should use most of the sample (sufficiency), the test sets should together cover most of the sample (coverage), and training data should come before test data (causality). We prove that the three cannot be had together and price each one. Let $\alpha$ be the smallest training fraction over folds, $\beta$ the fraction of the sample covered by tests, $\Lambda$ the fraction of the sample used as training data from the future of a test point, and $\delta$ the distance from a test point to the nearest training point in its future. Every scheme on a sample of length $T$ satisfies $\alpha+\beta \le 1+\Lambda$ and $\alpha+\min\{\beta,\delta/T\} \le 1$, and under $\beta$-mixing the leakage bias at a test point is at most $2M\beta_{\mathrm{mix}}(\delta)$. In words: going beyond the causal frontier $\alpha+\beta=1$ requires training on the future; that future data must sit within $(1-\alpha)T$ of a test point; and its harm depends on its distance, not its amount. Hence expanding walk-forward is exactly the Pareto frontier of causal validation, $k$-fold cross-validation buys the most future data, and purged $k$-fold with an embargo pays in distance instead, which is cheap when the process forgets quickly but cannot repair the part of causality demanded by non-stationarity. On pure noise, shuffled 5-fold reports an information coefficient of $+0.32$, while contiguous 5-fold, using the same amount of future data, reports $+0.004$.

---


### 154. [Clinical Knowledge Graphs for Chest X-Ray Device Reasoning](https://arxiv.org/abs/2609.29536)

**<font color=#1a73e8>作者：</font>** Harshil Lodhiya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chest radiographs are routinely used to verify the position of catheters, tubes, and other support devices. Existing image models often return labels or segmentations, while report-processing systems structure text without access to image geometry. We present an uncertainty-aware clinical knowledge graph that represents device instances, tip estimates, placement assessments, provenance, report events, and temporal links as separate but connected evidence.
We evaluate the implemented visual graph layer using saved predictions from the complete RANZCR CLiP test archive, comprising 30,083 studies from 3,255 patients across five non-overlapping outer folds. The graph builder materializes 914,632 B7 evidence nodes and 884,549 typed relationships. All 118,647 B7 predicted-device nodes retain tip covariance, placement probabilities, fragment provenance, and fragment counts, whereas the direct B2 baseline retains none of these fields. We further define typed data contracts, uncertainty representations, abstention rules, report-image grounding, and longitudinal query mechanisms for extending the graph to report-bearing cohorts.
The reported graph-materialization analysis is post-hoc descriptive and does not establish report grounding, longitudinal performance, or clinical utility. It demonstrates a reproducible foundation for evidence-preserving AI reasoning over chest X-ray device assessments.

---


### 155. [GeoRefer-Bench: A Benchmark from Referring Pixels to Verifiable Geospatial Reasoning](https://arxiv.org/abs/2609.29541)

**<font color=#1a73e8>作者：</font>** Shuaishuai Cao, Min Huang, Meng Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring segmentation in overhead imagery is inherently relational: a query may ask for the buildings north of the road or the pond closest to a residential area, so the correct referent can contain one object, several objects, or none. Existing benchmarks mainly score mask overlap, which cannot verify whether a model actually resolved the stated spatial relation. We introduce GeoRefer-Bench, a benchmark for verifiable geospatial referring segmentation. Each query is represented by an executable logical form over a metric scene graph, and predictions are evaluated with Exact Query Success (EQS), which is satisfied only when the returned instance set exactly matches the set denoted by the query. GeoRefer-Bench contains 700 whole 2048x2048 UAV scenes (2.94 Gpx) at 12.5 and 25 cm ground sampling distance, 26,217 instances, 142,796 spatial relations, and 20,916 executable queries spanning five reasoning levels. It further includes three paraphrases per query, 24.0% unanswerable queries, 2,477 counterfactual pairs, and five leakage-controlled evaluation splits. An independent audit re-derives object geometry, mask ownership, relation values, query execution, and split provenance, finding zero issues across all 700 scenes. Relation-blind strategies can retain non-trivial mIoU while achieving at most 22.7 EQS overall, showing that overlap alone does not certify relational grounding. Across fifteen current models, the strongest reaches 74.1 EQS but drops from 98.9 at level 1 to 60.5 at level 5, while ten models score below 5 EQS on two-hop queries. GeoRefer-Bench turns geospatial referring segmentation from mask matching into verifiable reference resolution.

---


### 156. [Generalized Graph Variational Autoencoders: Bounded Divergences Control Posterior Collapse](https://arxiv.org/abs/2609.29546)

**<font color=#1a73e8>作者：</font>** Kleyton da Costa, Bernardo Modenesi, Ivan F.M. Menezes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The variational graph autoencoder (VGAE) regularizes its posterior toward the prior with the Kullback-Leibler divergence, a choice inherited from the variational autoencoder rather than argued for. We introduce the generalized graph variational autoencoder (GGVA), which replaces that term with any member of the Rényi-Tsallis family of order $q$ while leaving every other part of the model untouched. Both members admit closed forms for diagonal Gaussians and both recover the KL exactly as $q \to 1$, so the VGAE is the $q=1$ arm of our own model rather than a separate baseline, and any measured difference is attributable to a single scalar. Our analysis identifies boundedness, not the order, as the operative property: for $q<1$ the Tsallis divergence is bounded above by $1/(1-q)$, independently of the latent width, whereas the KL and the Rényi divergence of the same order are unbounded. On ten graphs spanning three synthetic families, a social network, three citation networks, a connectome, a power grid and a road network, $q$ moves the retained posterior information by up to $49\times$ relative to the VGAE, while the Rényi arm at the same order stays within $1.02$-$1.30\times$ of it on all six larger real graphs (isolating the bound as the cause). The retained information is usable: probing the frozen embedding for node class, a label absent from the objective, gives GGVA up to $+0.14$ macro-F1 over the VGAE on CiteSeer, with the Rényi control again tracking the VGAE. We also report what the design was built to expose: none of this reaches held-out link-prediction accuracy on any of the six larger real graphs, and boundedness delays posterior collapse rather than preventing it.

---


### 157. [Spaceborne differential photogrammetry for control-free measurement of large-gradient deformation with structural immunity and a predictable accuracy envelope](https://arxiv.org/abs/2609.29550)

**<font color=#1a73e8>作者：</font>** Yueqiang Zhang, Chang Ma, Shuixin Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical satellite image correlation measures wide-area deformation in regimes where coherent interferometric synthetic aperture radar fails because displacement gradients are too large. However, standard pairwise workflows lack a pre-acquisition error budget and rely on extensive stable terrain. We formulate repeat-pass optical correlation as a differential estimation problem without surveyed ground control. Nominal georeferencing defines the coordinate frame, stable-area constraints and displacement priors resolve the datum, and surface displacement is estimated jointly with inter-epoch revisit-bias coefficients. The model yields a predictive accuracy envelope and calibrated per-point posterior uncertainty, bounds along-track uncertainty through a displacement prior, and represents pushbroom jitter using per-line revisit offsets. Simulations and Sentinel-2 and WorldView-2 experiments on the 2019 Ridgecrest earthquake, the 2023 Kahramanmaraş earthquake, and the Baltoro glacier validate the predicted noise floor, control-free accuracy margin, and leakage caused by view-angle and digital elevation model errors. The measured noise floor reaches approximately $0.05$ pixel at $10$,m ground sampling distance. With only five stable tiles, conventional destriping changes the estimated Baltoro trunk velocity from $106$ to $1251$myr$^{-1}$, whereas the prior-constrained estimate remains $87$myr$^{-1}$. Closure analysis attributes approximately $88\%$ of pair-error variance to individual scenes, consistent with $25{,}354$ ITS_LIVE glacier-velocity triplets. Three matching methods lead to the same conclusions. The framework therefore turns pairwise correlation into a robust measurement with a predictive error budget, reduced dependence on stable terrain, and conclusions independent of the matching method.

---


### 158. [UNWIND: Any-Length Facial Video for Stress Detection without Temporal Windowing](https://arxiv.org/abs/2609.29553)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Christian Arzate Cruz, Eric Nichols 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic stress recognition from facial video provides a non-contact approach for affective monitoring. However, most existing video-based methods divide complete recordings into shorter temporal segments before performing classification. Such segmentation requires additional decisions concerning segment duration, overlap, and prediction aggregation, and may restrict the model from exploiting information distributed across the entire recording. We introduce UNWIND, a facial-video framework for stress detection that analyzes a complete recording as a single model input, eliminating the need for temporal windowing or external segmentation. UNWIND reorganizes the video by folding its temporal dimension into the channel dimension of a two-dimensional spatial representation, which is subsequently processed through a unified asymmetric-attention architecture. With a temporal stride of $\tau=1$, the framework processes the entire $120$-second sequence, corresponding to $3{,}600$ frames sampled at $30$~fps, in a single input. We evaluate seven temporal-stride settings on a stress dataset comprising $58$ subjects, using a stratified subject-level protocol that covers configurations from dense frame retention to sparse temporal sampling. The highest test accuracy, $70.02\%$, is obtained at $\tau=15$, while processing all frames at $\tau=1$ achieves a comparable accuracy of $69.73\%$. Computational requirements range from $12.48$ to $348.78$ GFLOPs across the evaluated stride settings, illustrating the balance between temporal sampling density and computational efficiency. The findings show that effective facial-video stress recognition can be achieved without dividing recordings into temporal windows and that complete-recording inference can be performed within a single unified model.

---


### 159. [Visual Representation and History Modeling for Navigation World Models](https://arxiv.org/abs/2609.29555)

**<font color=#1a73e8>作者：</font>** Guangfu Guo, Xiaoqian Lu, Rui Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Navigation World Models (NWMs) predict action-conditioned visual futures for planning. Two practical challenges are central to their design: selecting a suitable visual representation and efficiently modeling observation history for repeated candidate queries. Standard Global-Softmax attention provides flexible interactions but repeatedly processes the same history, leading to increasing computation and memory costs for long contexts and multi-query planning. We study both problems within a unified conditional flow-transformer framework. We first compare five frozen visual representations under the same dynamics model and evaluation. To reduce redundant history computation, we design Cached-Linear, a hybrid architecture that combines local and shifted-window attention for target mixing with linear attention for reusable history access. We further develop Balanced Gated Delta Network (GDN), which augments this design with frame-wise recurrent memory for temporal history modeling. Experiments on RECON, SACSoN, and SCAND show that representation choice depends on the prediction objective: PAE-L performs best for reconstruction, RAE-B for direct prediction, and V-JEPA for long-horizon rollout. Under shared-history workloads, Cached-Linear substantially reduces computation and memory compared with Global-Softmax, while Balanced GDN improves selected direct-prediction endpoints with efficient context reuse. Overall, we systematically study visual representation and history modeling for NWMs and develop hybrid reusable-history architectures for efficient long-context and multi-query prediction.

---


### 160. [Cross-Modal Emotion Understanding: A Transformer-GAT Approach for Dialogue Emotion Recognition](https://arxiv.org/abs/2609.29556)

**<font color=#1a73e8>作者：</font>** Jiaqi Qiao, Yifan Lyu, Xiujuan Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition is a key research area in affective computing, with applications in sentiment analysis, intelligent customer service, and human-computer interaction. However, existing methods often rely on single-modal features or simple multimodal fusion, failing to capture the synergy between global and local contexts, which limits model performance and emotion understanding. To address this challenge, we propose Transformer-GAT, a hybrid framework that combines Transformer and the Graph Attention Network to enable cross-modal emotion understanding. The Transformer is used to capture global semantic information, while the Graph Attention Network is employed to model fine-grained relationships between modalities, thereby enhancing the representation of emotional features. Experiments on the IEMOCAP and MELD datasets show that our model achieves weighted F1 scores of 72.45% and 77.37%, outperforming state-of-the-art methods. These results demonstrate that Transformer-GAT effectively integrates multimodal features, balances global and local contexts, and provides deeper emotional insights, offering new directions for multimodal emotion computing.

---


### 161. [Classifier-Dependent Benefits of Pseudo-Labeling for Semi-Supervised Android Malware Attribution](https://arxiv.org/abs/2609.29564)

**<font color=#1a73e8>作者：</font>** Md Rafid Islam, Zahid Hasan, Hafiz Abdur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting and classifying Android malware families remains challenging due to high feature dimensionality, class imbalance, and the high cost of expert-labeled data. Semi-supervised learning (SSL) offers a way to leverage unlabeled samples, but prior works rarely test whether SSL benefits generalize across classifier types or report statistical significance. We present a systematic evaluation of pseudo-labeling across six classifiers (LightGBM, XGBoost, Random Forest, Logistic Regression, MLP, and SVM) on the CICMalDroid 2020 dataset, using five-fold stratified cross-validation and paired t-tests across five labeled ratios (1-20%). We find that SSL benefit is strongly classifier-dependent: SVM shows the largest significant gain (+4.4% accuracy at 5% labels, p = 0.0028), LightGBM improves modestly (+0.8 to +1.3% at 2-5% labels), while Random Forest is significantly harmed at low label ratios (-3.1% at 1% labels). Per-class analysis reveals SSL disproportionately benefits the hardest-to-classify families, with Adware F1 improving by +13.8 percentage points versus only +0.8 for the already well-classified Benign class. We further show that approximately 800 labeled samples (10% of the dataset) yield near-optimal performance across all classifiers. These findings offer practical guidance on when and with which classifier pseudo-labeling is worthwhile for Android malware classification.

---


### 162. [From Spectrum Regulation to Computational Enforcement: An Auditable Governance Architecture for Adaptive Spectrum Sharing](https://arxiv.org/abs/2609.29571)

**<font color=#1a73e8>作者：</font>** Navaneetha Krishnan Kamalakannan, Harinisri Velmurugan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Spectrum governance requires rules to be translated into machine-executable decisions while preserving incumbent protection, regulatory authority, and an auditable record of why a decision was made. We present SPECTRA-GOV, a Tri-Layer Adaptive Governance Architecture (TLAGA) connecting international treaty coordination, national adaptive licensing, and real-time enforcement. The work builds on the original reference implementation preserved at v0.1.0-paper and adds a post-audit evaluation layer rather than replacing it. V2 introduces controlled spectral-contention scenarios, corrected geodesic-distance calculation, per-operator selective authorization, paired baseline counterfactuals, policy perturbation, regulatory-change analysis, and causal provenance. Across 10,000 scenarios in each of seven contention classes, incumbent protection was 100.00% in the no-contention control, 99.92-99.87% in weak-to-dynamic classes, 99.47% under strong overlap, and 90.00% in the adversarial close-proximity class. In a paired S3 baseline experiment, selective authorization achieved 100% incumbent protection and 89.43% access opportunity, while the population-wide dynamic baseline achieved 99.91% protection and 99.53% access. Identical results for the dynamic-SAS and SPECTRA-GOV selective variants mean selective admission alone is not claimed as an exclusive algorithmic novelty. The contribution is the integration of policy representation, computational enforcement, auditability, provenance. Enforcement timing was measured in-process, with mean latency increasing from 0.028 ms for one operator to 1.682 ms for 500 operators; these are software benchmarks, not field measurements. The results establish a reproducible computational governance prototype and identify remaining questions before operational or regulatory claims can be made.

---


### 163. [When Identical Rows Disagree: From Benchmark Identifiability to Replication-Robust Anomaly Detection](https://arxiv.org/abs/2609.29580)

**<font color=#1a73e8>作者：</font>** Jie Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A released table is often treated as an i.i.d. sample, although its repeated rows may encode business frequency, repeated entities, joins, resampling, or extraction errors. We show that this ambiguity creates a hidden measurement layer with three consequences: feature-identical rows impose an attained evaluation ceiling, row-weighted AUROC is sensitive to replication, and row-trained detectors learn a multiplicity-size-biased law. An exact-row audit of all 690 OddBench datasets finds train-test overlap in 355, feature-identical label conflict in 147, and a test anomaly identical to a training normal in 137. Switching from row to support weighting changes AUROC by at least 0.05 on 50-61 datasets across four classical detector geometries. We introduce SCOUT (Support-Count Orthogonalized Unsupervised Testing), a factorized anomaly detector that separates replication-invariant support evidence from exposure-aware count evidence. Factorwise split-conformal calibration yields marginal false-positive-rate control, while the support channel is exactly invariant to arbitrary positive row replication. On 686 OddBench datasets and five seeds, support-only SCOUT is non-inferior to row-wise Isolation Forest in raw AUROC and improves replication-invariant AUROC. External normal-support evaluations track nominal false-positive levels, and four backbones remain exactly unchanged under controlled replication. Semi-synthetic interventions show that conditional count modeling helps materially only under strong rate heterogeneity. These results specify when multiplicity should be treated as signal, nuisance, or uninterpretable without additional information.

---


### 164. [Long-Tail Adaptive Flow Matching with Explicit Conditional Consistency Guidance for Precise Multimodal Face Synthesis](https://arxiv.org/abs/2609.29581)

**<font color=#1a73e8>作者：</font>** Yushe Cao, Xuechao Zou, Xing Xi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although diffusion-based methods have substantially improved the controllability of multimodal face synthesis, their semantic alignment remains suboptimal because most existing approaches rely on implicit latent-space objectives to model the relationship between denoising variables and multimodal conditions. Such implicit modeling is often insufficient to enforce precise correspondence between synthesized faces and conditional inputs, especially under long-tailed semantic mask distributions where rare attributes receive weak optimization signals. To address these limitations, we propose EC\textsuperscript{2}Face, a multimodal face synthesis framework that improves semantic alignment through explicit semantic supervision and distribution-aware optimization. First, we introduce Explicit Conditional Consistency Guidance (ECCG), which imposes direct consistency supervision in pixel space by decoding an approximate reverse estimate of the clean latent and explicitly aligning the synthesized image with textual descriptions and semantic masks. A temporal dynamic modulation function is further designed to adapt the supervision strength according to the timestep-dependent reliability of reverse estimation. Second, we propose Long-Tail Adaptive Flow Matching (LAFM), which reweights spatial optimization signals based on semantic attribute frequency, with normalized weights to maintain numerical stability during training. Importantly, all additional modules are used only during training and introduce no extra inference overhead. Extensive experiments show that EC\textsuperscript{2}Face consistently outperforms competitive baselines in both generation quality and semantic alignment, achieving a 29.38\% improvement in mask accuracy on rare attributes.

---


### 165. [A Computational Framework for Modelling Organisation-Level Semantic Identity from Longitudinal Textual Data](https://arxiv.org/abs/2609.29584)

**<font color=#1a73e8>作者：</font>** Brinda Murali Krishna, Oktay Karakuş, Can Eyupoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Organisations continuously generate large volumes of textual data that capture how they communicate, evolve and differentiate themselves over time. Although recent advances in natural language processing have substantially improved organisation-level text analytics, existing approaches primarily represent organisations as latent embeddings or predictive feature vectors for similarity estimation, classification or retrieval. Consequently, there is currently no general computational framework for modelling organisation-level semantic identity as an interpretable and evolving semantic construct derived from longitudinal textual evidence. This paper introduces a computational framework that integrates semantic representation learning, graph-based semantic modelling, organisation-level semantic fingerprints, temporal semantic evolution and evidence-driven validation within a unified analytical methodology. Organisations are characterised through complementary semantic dimensions describing diversity, concentration, connectivity, novelty and semantic community composition, which are analysed longitudinally to infer evidence-supported semantic identities. The framework is demonstrated using a longitudinal corpus of K-pop lyrics from artists affiliated with the four major South Korean entertainment companies. The empirical analyses reveal distinguishable multidimensional semantic identities, diverse temporal evolutionary trajectories and coherent integrated identity profiles. Comprehensive validation demonstrates that the inferred identities are statistically supported, robust under alternative analytical assumptions, reproducible and operationally informative. Beyond the case study, the proposed framework establishes organisation-level semantic identity and provides a transferable methodology for modelling organisational behaviour from longitudinal textual data.

---


### 166. [CATCH: Counterfactual Anatomical Tissue Inpainting with Conditional Haar Diffusion](https://arxiv.org/abs/2609.29591)

**<font color=#1a73e8>作者：</font>** Simon Winther Albertsen, Hjalte Bjoernstrup, Said Djafar Said 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> BraTS local synthesis replaces masked regions in T1-weighted brain MRI with plausible tumor-free tissue while preserving observed anatomy. We present CATCH, conditional 3D diffusion in an invertible Haar-wavelet domain. Its denoiser receives noisy target coefficients, voided-image coefficients, and a signed mask; tumor-excluded wavelet reconstruction and a hole-focused loss guide training, and hard compositing preserves observed voxels. We compare fixed masks, tumor-component augmentation, and a weighted mixture of tumor-derived, irregular-blob, and ellipsoidal masks. Of 25 development cases, five prespecified cases select each arm's checkpoint and all 25 of their trajectory aggregations; a separate 75-case internal set compares the frozen pipelines and selects a weighted mixture for organizer evaluation. Five-trajectory averaging yielded internal SSIM/PSNR/MSE (mean$\pm$SD) of $0.80\pm0.13$, $19.18\pm1.80$dB, and $0.010\pm0.005$. As the sole officially evaluated pipeline, weighted mixture yielded $0.772\pm0.119$, $20.89\pm3.27$dB, and $0.0098\pm0.0054$ on the 219-case BraTS 2026 validation set. Against compute-matched random augmentation internally, it improved SSIM by 0.019 (95% bootstrap CI: 0.013-0.025), PSNR by 0.95dB, and MSE by 0.003; all three paired comparisons remained significant after Holm correction. Results favor the complete weighted-mixture policy within CATCH; absent official fixed- and random-pipeline scores and a directly comparable external baseline limit broader conclusions.

---


### 167. [QINA: Quantum-Inspired Nonlinear Adapters for Pretrained Vision Models](https://arxiv.org/abs/2609.29592)

**<font color=#1a73e8>作者：</font>** Mostafa Mehdipour Ghazi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting large pretrained vision models under limited data and frozen-backbone constraints remains a central challenge in transfer learning. While lightweight adapters and parameter-efficient fine-tuning methods are widely adopted, most rely on generic multilayer perceptrons or low-rank linear updates, offering limited control over the spectral and geometric structure of feature transformations. We investigate whether structured nonlinear feature lifting can improve representational alignment in frozen regimes. We introduce Quantum-Inspired Nonlinear Adapters (QINA), compact modules that perform learnable trigonometric feature lifting followed by bounded nonlinear aggregation. The design induces structured oscillatory basis functions with an explicit norm-dependent Lipschitz bound, enabling spectral reshaping of pretrained representations without increasing the receptive field or significantly expanding parameter count. Importantly, the method operates entirely within standard deep learning frameworks and does not require quantum hardware. Through systematic experiments across natural and medical imaging datasets, classification and segmentation tasks, multiple adapters and placements, and varying training budgets, we show that performance in frozen regimes is primarily representation-limited. Nonlinear lifting improves adaptation, and the proposed structured trigonometric formulation consistently outperforms identity baselines, fixed Fourier feature mappings, and parameter-matched baseline adapters. Within the evaluated frozen-backbone settings, structured spectral parameterization provides a more effective inductive bias than generic nonlinear adapters. This work highlights the importance of geometry- and spectrum-aware adaptation mechanisms for large pretrained vision models.

---


### 168. [PEEL: Physics-Enabled Evidential Learning for Identifiable Uncertainty in CT Imaging](https://arxiv.org/abs/2609.29599)

**<font color=#1a73e8>作者：</font>** Ge Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Normal-inverse-gamma (NIG) regression is not uniquely identifiable from its marginal Student-t likelihood: the likelihood determines three combinations of four NIG parameters and is constant along a one-dimensional fiber. We identify that fiber using independent physical measurement. As an initial embodiment, a reconstruction network receives one noisy filtered-backprojection (FBP) image and is first trained only by Student-t negative log-likelihood to estimate the three identifiable coordinates (gamma, alpha, c). The network is then frozen; repeated physical-noise realizations propagated through its reconstruction output form a Monte Carlo (MC) teacher label for output-domain aleatoric variance. An aleatoric head attached to frozen features learns this label, after which (beta, nu) are recovered algebraically. On 30 held-out simulated objects at five photon levels, one-image predictions achieved pooled Spearman correlations of 0.832-0.951 against independent 400-repeat references, median within-image correlations were 0.834-0.947, and 98.81-99.55% of evaluated pixels satisfied the algebraic admissibility condition. The method needs no KL term, reference prior, evidence regularizer, or cross-loss weight.

---


### 169. [Active Client Selection in Federated Trajectory Prediction with Uncertainty-Awareness and Heterogeneous Complexity](https://arxiv.org/abs/2609.29600)

**<font color=#1a73e8>作者：</font>** Yiming Xie, Muzi Peng, Fei Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training sequence models such as transformers is now standard for autonomous vehicle trajectory prediction, yet assembling high-quality centralized datasets remains challenging because real-world trajectories are fragmented across regions and vehicles. Federated Learning (FL) offers a natural alternative, but faces two distinctive challenges: high scene uncertainty arising from trajectory or map ambiguity, and cross-scene complexity heterogeneity caused by diverse map topology, traffic density, agent composition, and driving behaviors.
We propose a family of active client selection methods that progressively incorporate awareness of scene uncertainty and complexity to prioritize informative clients. Our uncertainty-aware selectors use per-client negative log-likelihood under an uncertainty-aware global objective and estimated aleatoric uncertainty. We further develop a selector that jointly considers scene complexity and uncertainty, motivated by the intuition that knowledge from complex scenes can transfer to easier ones.
Experiments on Argoverse show that federated trajectory prediction outperforms locally trained models. Uncertainty-aware selection accelerates convergence and improves minADE, minFDE, and MR. Under strong scene-complexity heterogeneity, our joint complexity- and uncertainty-aware selector achieves the best generalization and further accelerates convergence, demonstrating the benefit of prioritizing complex and informative scenes.

---


### 170. [MoSign: Challenge-Response Motion-Watermark Authentication for Anonymous Virtual-Reality Users](https://arxiv.org/abs/2609.29603)

**<font color=#1a73e8>作者：</font>** Xujun Che, Thomas Carr, Depeng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Social virtual reality (VR) creates a paradox. A user's body motion is a high-entropy biometric: head and hand trajectories alone re-identify users among tens of thousands with over $94\%$ accuracy, so anonymizing the rendered avatar is a practical necessity. Yet a user often still wants to prove their identity to a chosen party from inside that anonymity. We present MoSign, which recasts digital watermarking as a challenge-response authentication protocol on the motion channel. MoSign embeds a time-varying keyed message into the style latent of a motion variational autoencoder via keystream-whitened Gaussian-Shading: watermarked motion is provably indistinguishable from watermark-free motion, since any detector's advantage reduces to breaking a pseudorandom function, so the mark composes with anonymization. The message is a keyed MAC over an epoch counter, a session nonce, and a deployment context, making MoSign replay-resistant and bounding forgery by the verifier's measured false-accept rate times the adversary's online query budget. A key-holding verifier decides with a sequential test. We identify render$\rightarrow$record$\rightarrow$re-estimate ("recapture") as the realistic VR attack surface: a generic pose estimator strips the necessarily subtle watermark, but a recapture-robust keyed reader recovers it (up to $0.96$ codeword accuracy on a projected-2D channel, $0.81$ through a full render-to-video loop), while without the key recovery stays at chance. On HumanML3D, MoSign authenticates every legitimate user at a false-accept rate of $10^{-4}$ on clean and most channels and stays undetectable (detection AUC $0.51$, chance $0.5$); on the BOXRR-23 VR dataset it carries the mark through a real anonymizer at $0.99$ codeword accuracy and adds no de-anonymization side channel.

---


### 171. [From Maturity Models to Ground Truth: Reconciling Cybersecurity Capacity Frameworks with Household-Level Governance Realities in the Global South](https://arxiv.org/abs/2609.29611)

**<font color=#1a73e8>作者：</font>** Wael Albayaydh, Ivan Flechais  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> National cybersecurity and digital-governance capacity frameworks, most prominently the Cybersecurity Capacity Maturity Model for Nations (CMM), shape hundreds of millions of dollars in donor-funded governance investments across the Global South. Yet a persistent, under-theorised gap remains between state-level institutional maturity and the governance actually experienced by end-users. We term this the last-mile governance gap: the structural space between what a maturity assessment can see - laws, agencies, standards, awareness campaigns - and what a household living under that formal architecture can access, understand, or enforce. Drawing on a dual vantage point combining CMM assessment experience with peer-reviewed empirical fieldwork on smart-home privacy governance in Jordan, corroborated against studies from Kenya and China, we identify four mechanisms by which national capacity fails to reach the household: legibility, intra-household power distribution, accessibility of redress, and infrastructure-affordability constraints. We map these mechanisms explicitly onto the CMM's five dimensions, propose four concrete, low-cost last-mile indicators pilotable within existing CMM deployments, and outline a staged adoption roadmap with responses to anticipated objections. With AI-enabled devices entering homes across the Global South faster than institutional capacity can adapt, the stakes are rising: this dynamic risks converting a measurable maturity gap into an invisible one. We conclude with actionable implications for the GCSCC, the ITU, the World Bank, and other institutions relying on maturity scores to prioritize investment.

---


### 172. [Limited Structural Reliability in Public Educational Prediction Benchmarks: A Four-Dimension Audit of Seven Datasets](https://arxiv.org/abs/2609.29625)

**<font color=#1a73e8>作者：</font>** Yan Ma, Lizhuo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across seven public educational prediction datasets, three passed all four pre-modeling reliability checks; the remaining four either failed group-aware generalization tests or lacked the provenance metadata needed to run them. One dataset was initially classified as failing but corrected after excluding group-identifier features from the holdout matrix, demonstrating that the audit can distinguish genuine cross-group confounding from feature-encoding artifacts. Each dataset was audited before model optimization using four checks: baseline gap, split instability, null separation, and metadata adequacy under group-aware holdout. The dominant failure mode was not weak iid performance alone but cross-group fragility: in the clearest case, UCI Student declined from iid R-squared 0.242 to group-holdout R-squared -0.097, while Higher Ed collapsed from 0.041 to -8.79. Increasing model complexity did not remove this pattern: ensemble models improved structurally sound datasets but amplified instability or failed under group holdout on fragile ones. An exploratory cross-dataset comparison further showed that stronger profiles clustered in larger, richer-grouped, performance-proximal datasets, while random-split performance severely overstated deployable signal in fragile datasets. Classification-metric sensitivity analyses reached the same substantive conclusions. The results show that benchmark reliability in educational AI is constrained less by algorithm choice than by data structure, group heterogeneity, and evaluation design. A reusable pre-modeling audit offers a minimum quality gate before public educational datasets support strong benchmark or deployment claims.

---


### 173. [A Manifold-Aware Topic Modeling Approach via Rank-Based Prototypes](https://arxiv.org/abs/2609.29630)

**<font color=#1a73e8>作者：</font>** Thiago César Castilho Almeida, Daniel Carlos Guimarães Pedronette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent topic models leverage pretrained embeddings, but neural architectures produce latent representations without grounding in specific texts, and clustering-based pipelines assign representative documents only post hoc, relying on absolute distances distorted by hubness and anisotropy in high-dimensional spaces. We introduce MARETopic, a training-free framework that casts topic discovery as rank-based prototype selection. After projecting embeddings onto a low-dimensional manifold, MARETopic builds ranked lists encoding ordinal neighborhood structure. A greedy algorithm selects exactly K exemplar documents, real corpus texts, whose neighborhoods cover the corpus. Two variants share this criterion. MARETopic$_\text{Corr}$ scores candidates with a query performance predictor and a rank correlation measure, leading Purity and NMI on the two benchmarks with the most categories, ahead of both neural and clustering-based topic models. MARETopic$_\text{Diff}$ scores them with a rank-based diffusion matrix, needs neither measure, and runs 1.7 to 1.9 times faster. Without a single gradient update, MARETopic leads topic coherence on two of three datasets. A novel inter-topic Maximal Marginal Relevance step raises vocabulary diversity at little cost in coherence. Our code is available at this https URL.

---


### 174. [TTLab at AlexandriaX-2026: A Fine-Tuned Surface Tagger for Arabic Machine-Translation Error-Span Detection and Classification](https://arxiv.org/abs/2609.29633)

**<font color=#1a73e8>作者：</font>** Ali Abusaleh, Bhuvanesh Verma, Alexander Mehler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present TTLab's submission to the AlexandriaX-2026 Subtask~3 on Arabic MT error span detection and classification. Our system frames the task as token-level classification over surface forms, preserving character offsets to ensure exact alignment with the evaluation metric. To handle severe label imbalance, we employ a focal loss with class weighting and dialect-specific decoding thresholds. Among six Arabic pre-trained encoders, MARBERTv2 achieves the best overall performance of 40.8 and 40.91 on the development and test set, respectively, ranking $\nth{3}$ out of all participating teams. While our system localizes error spans effectively, classification of rare error types remains challenging, highlighting the need for data augmentation for tail categories. The code is available at ${\href{this https URL}{\faGithub~ TTLab at AlexandriaX-2026}$

---


### 175. [SpectralCTGaussians: Projection-Domain Reconstruction and Basis Material Decomposition for Spectral CT using 3D Gaussian Splatting](https://arxiv.org/abs/2609.29638)

**<font color=#1a73e8>作者：</font>** Reinout Vos, Saptarshi Neil Sinha, Michael Weinmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectral computed tomography (CT) extends conventional CT by measuring attenuation across multiple energy channels, allowing improved modeling of physical X-ray interactions and energy-dependent material behavior and leading to richer scene understanding. We present a novel method for spectral CT reconstruction and basis material decomposition using 3D Gaussian Splatting by adding per-Gaussian basis material fractions to the set of learnable parameters, which together with a set of energy-dependent basis functions define the attenuation across the full spectral range. The basis functions represent various physical attenuation models such as photoelectric absorption and Compton scattering, and are jointly optimized across all energy channels through a differentiable polychromatic forward model, with material decomposition performed via mean-shift clustering of the resulting coefficients. We evaluate our method on a baseline real-world dataset as well as a synthetic dataset that we introduce, comparing against traditional reconstruction algorithms and state-of-the-art learning-based CT reconstruction methods. Our approach outperforms all traditional baselines in novel view synthesis and achieves the best PSNR among all compared methods for spectral CT volume reconstruction, while describing all energy channels with a single shared representation that requires a number of Gaussians comparable to single-channel Gaussian splatting-based CT reconstruction approaches. For basis material decomposition, no traditional or learning-based baseline offers one-step decomposition with direct RGB material segmentation, and our method additionally recovers the photoelectric basis with higher PSNR than traditional pipelines.

---


### 176. [Automated Abstraction Refinement for Information Flow Security in Embedded Systems](https://arxiv.org/abs/2609.29645)

**<font color=#1a73e8>作者：</font>** Jonas Becker-Kupczok, Lukas Ernst, Paula Herber  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Information flow analysis (IFA) is a powerful technique for verifying confidentiality and integrity and is therefore highly desirable for security-sensitive embedded systems. However, as these systems are inherently concurrent and time-dependent, existing IFA for embedded systems tend to be either imprecise or expensive. In this paper, we propose an approach to tackle this problem using automatic abstraction refinement. The key idea is to heuristically choose abstraction levels based on information about dependencies between states and detected potential information leakage. Our approach builds on previous work, where we leverage symbolic execution to precisely capture data, control, timing, and event dependencies between processes within an IFA. To capture values symbolically, this analysis uses abstract interpretation. While the existing approach requires manual definition of abstraction levels, our novel contribution in this paper is using carefully designed heuristics to select these levels automatically. The aim is to keep analysis times acceptable while also retaining enough information to decide whether or not illegal information flow is possible. We have implemented our approach for the system design language SystemC and demonstrate its feasibility with experimental results on several shared bus architectures.

---


### 177. [Albireo: Adaptive, Energy-Efficient Inference Framework for Video Object Detection on the Edge](https://arxiv.org/abs/2609.29648)

**<font color=#1a73e8>作者：</font>** Amir Taherin, José Cano, Bin Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object detection on edge devices runs computationally expensive detectors over long frame streams, causing high energy consumption and sustained GPU utilization. Although consecutive frames are highly redundant, naive frame skipping is content-blind: it skips during critical moments such as object entry, occlusion recovery, and abrupt motion, degrading detection quality. We present Albireo, a detector-agnostic, codec-free adaptive inference framework that wraps off-the-shelf detectors and decides when detector invocation can be safely skipped based on scene content and per-object temporal state, requiring no detector modification or retraining. Albireo maintains a 10-dimensional Kalman filter (KF) per active object and invokes the detector only when prediction uncertainty exceeds a threshold; on skipped frames, boxes are predicted from the KF state at near-zero GPU cost. A KF-based rescue mechanism preserves confirmed objects through brief detector misses to prevent output fragmentation, while a lightweight empty-scene screen avoids detector calls on objectless frames. We evaluate Albireo on the BDD100K MOT validation split with three architecturally distinct detectors (YOLO11x, YOLO26x, RF-DETR-Large) on two NVIDIA Jetson platforms (AGX Thor, AGX Orin). Across all configurations, Albireo keeps AP@50 within +/-1.2 pp of per-frame inference while reducing total energy by 12.1-17.6%. On YOLO26x, it improves AP@50 by +0.8 pp while reducing energy by 17.6% (Thor) and 14.4% (Orin) and per-frame energy-delay product by 24.9% and 26.1%, respectively. Thus, the default operating point improves accuracy, energy, and latency together. In contrast, FixedSkip-2, a fixed-interval baseline with a 50% skip rate, loses 8.6 pp AP@50. Source code, evaluation pipeline, and per-clip results are available at this https URL

---


### 178. [VG-TIE: An interpretable tabular-to-image encoding method based on visibility graphs](https://arxiv.org/abs/2609.29650)

**<font color=#1a73e8>作者：</font>** David Chushig-Muzo, Luis M. López-Ramos, Ángeles Rodríguez de Cara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tabular-to-image encoding methods enable the application of models based on both convolutional neural networks and vision transformers to tabular data, transforming feature vectors into images. Existing methods employ linear and nonlinear dimensionality reduction techniques (e.g., Principal Component Analysis (PCA), t-SNE, and UMAP) to determine pixel positions, resulting in images whose spatial layout do not inherently reflect feature relationships. This paper introduces Visibility Graphs for Tabular-to-Image Encoding (VG-TIE), a novel method that encodes the structure of feature values using Natural Visibility Graph (NVG) and Horizontal Visibility Graph (HVG) into a two-dimensional space obtained through PCA. The resulting images are model-agnostic and intrinsically interpretable. Each pixel corresponds to an input feature, its intensity reflects the magnitude and direction of deviation from the population mean, and edges represent formally defined visibility relationships between features. VG-TIE provides two interpretability methods: (i) feature ranking from node degree distributions; and (ii) local and global feature importance from pixel intensity combined with Grad-CAM. Experiments on six public tabular datasets show that VG-TIE is competitive with other tabular-to-image methods while providing interpretability on feature importance and ranking similar to intrinsic interpretable methods. The results highlight the potential of the proposed image-based transformation to provide an effective framework that expands the use of deep learning across tabular data domains.

---


### 179. [Ingest-Time Fact Compilation for Cost-Efficient and Reliable Question Answering over Revised Corpora](https://arxiv.org/abs/2609.29661)

**<font color=#1a73e8>作者：</font>** Kyle Wild, Yusuke Takahashi, Asako Uraki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most agentic question answering (QA) systems do an important part of their semantic work at the worst possible time: every time someone asks a question. When a corpus contains revisions, drafts, revocations, deletions, and sources with different levels of authority, the model must reconstruct the governed current state on every read - then throw that work away and repeat it on the next query. This is a bit like a database that rebuilds a materialized view every time someone reads from it. We present ingest-time fact compilation, an architecture that performs this work when corpus data is ingested or changed. Raw passages are rephrased into self-contained facts; rules governing revisions, deletions, effective dates, and source trust are resolved once; and the resulting state is stored as typed records carrying source and revision provenance. At query time, an inexpensive model reads the compiled record instead of reconstructing it from noisy candidates. In a controlled synthetic experiment across five seeds, the same low-cost model produced the correct value, source, and revision in only one of 30 trials under query-time reconstruction, but in all 30 trials from the compiled substrate, at 12.89 times lower mean read cost per question. On simpler revision questions both architectures were exact, but the compiled path used 21.6 times fewer tokens. A separate test found that fact rephrasing roughly halved verbose Federal Reserve dialogue while preserving high source entailment, but left concise Wikipedia prose essentially unchanged. These results support a narrow but practical claim: resolving a corpus state once can make subsequent QA cheaper and more reliable for inexpensive models. We release the open source, MIT-licensed implementation and experimental artifacts.

---


### 180. [Investigating White Blood Cells as a Source of False-Positive Malaria Parasite Detection in African Blood-Smear Images](https://arxiv.org/abs/2609.29663)

**<font color=#1a73e8>作者：</font>** Samuel A. Adeniji, Goodness C. Obasi, Chris-Victor Ntwali 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> White blood cells (WBCs) present on every Giemsa-stained thick blood smear share visual properties with early-stage Plasmodium falciparum ring-form trophozoites: small size, round morphology, and intense purple staining. They are a plausible but untested source of false positives in parasite-only detectors. We trained two YOLOv12s models on the Lacuna Malaria Detection dataset (8,000 images from Uganda and Ghana): Model A with parasite labels only, and Model B with both parasite and WBC labels. Seven independent spatial and statistical analyses tested whether false positive (FP) predictions cluster near WBC locations. All seven refute the hypothesis. In both models, 95% of FPs are pure background detections (IoU below 0.10 against any ground-truth box); zero are WBC class confusions. Ripley's Cross-K analysis shows spatial repulsion between FP centroids and WBC positions at every radius tested. Model B outperforms Model A overall (mAP50 0.859 vs. 0.755), and the advantage is uniform across all WBC-proximity bands, pointing to multi-task representation learning rather than WBC suppression as the cause. False positives arise from Giemsa stain debris and preparation artifacts. Effective mitigation requires staining artifact augmentation and annotation of unannotated early-stage ring forms rather than WBC labeling alone.

---


### 181. [GBFRVFL: Granular-Ball Computing-Based Fuzzy Random Vector Functional Link Network](https://arxiv.org/abs/2609.29670)

**<font color=#1a73e8>作者：</font>** A. Quadir, A. Rahaman, P. N. Suganthan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In practical machine learning tasks, data are often contaminated with noise, outliers, and class imbalance, which can degrade the performance of conventional models. While random vector functional link (RVFL) networks offer fast training and strong generalization, they do not explicitly handle uncertainty or exploit local data structure. To address these limitations, we propose a fuzzy granular-ball random vector functional link (GBFRVFL) framework that leverages granular-ball computing to abstract raw samples into adaptive granular balls. Within this framework, we introduce two membership assignment schemes: (i) F-GBRVFL, which incorporates fuzzy membership to quantify the reliability of each granular ball, and (ii) SDAP-GBRVFL, which we propose, incorporates a novel statistical density-adaptive pythagorean membership (SDAPM) scheme that dynamically adjusts membership and non-membership values based on class variance, local sparsity, and granular-ball compactness. These schemes enhance robustness to noise, outliers, class imbalance, and uncertainty in granular-ball distributions, while retaining the computational efficiency of RVFL networks. Extensive experiments on 37 benchmark UCI and KEEL datasets under both clean and noisy conditions demonstrate that the proposed models consistently outperform baseline models, achieving superior accuracy and stability. The results validate the effectiveness of integrating granular-ball computing with adaptive membership schemes for reliable, scalable, and noise-tolerant learning.

---


### 182. [LLMersion: A Local-First AI Agent Framework for Low-Cost Home Language Learning toward Educational Equity](https://arxiv.org/abs/2609.29672)

**<font color=#1a73e8>作者：</font>** Qiming Guo, Jinwen Tang, Xingran Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence helps education most where an essential provision has been rationed by cost. For language learners that provision is a teacher's voice, which binds listening, reading, speaking, and writing into one act. Published evidence shows why most learners lack it, from a global shortage of 44 million teachers to heavy household tutoring bills, and why technology has not substituted for it: computer-assisted language learning proved effective but narrow, applications presuppose connectivity 2.6 billion people lack, and One Laptop per Child's randomized evaluation found that hardware without capable software teaches nothing. We distill eight difficulties and four binding constraints, and argue that small open-weight models dissolve the last: a complete four-skill stack now fits a \$200-class laptop and, on community measurements, generates at the pace speech is consumed, for about one US cent of electricity per study hour. We therefore propose LLMersion, a scheme for AI for education that runs entirely at home, over the learner's own documents, with an AI-written, AI-understood, AI-updated codebase anyone can customize; present LLMersion-1, a released open-source prototype (this https URL and outline the vision of a private learning agent.

---


### 183. [The Sequential Price of Continual Learning](https://arxiv.org/abs/2609.29674)

**<font color=#1a73e8>作者：</font>** Zonghuan Xu, Xingjun Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential task updates are fundamental to continual learning, but their recency bias can impose a lasting performance cost. We study this cost in an overparameterized linear-regression model with i.i.d. task sampling. We prove that distribution-level forgetting and population loss converge to the same stationary limit. This common limit separates exactly into the intrinsic loss asymptotically attained by joint training and an additional sequential price, and in more homogeneous task geometries the two terms coincide, making the total loss twice that of joint training. We further analyze fixed-strength elastic weight consolidation (EWC) under general task curvatures and characterize its stationary sequential price at every regularization strength. Under strong regularization, the price decays inversely with EWC strength while convergence to stationarity slows at the same scale. On the Jester joke-rating dataset, the theory exactly quantifies both the sequential price generated by naturally conflicting user preferences and its reduction by EWC.

---


### 184. [ReCalMatch:Reliability-Calibrated Semantic Guidance for Semi-Supervised Fine-Grained Recognition](https://arxiv.org/abs/2609.29678)

**<font color=#1a73e8>作者：</font>** Yundi Hong, Hongyang He, Zheng Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised fine-grained visual recognition is highly vulnerable to overconfident pseudo-label errors: visually similar categories frequently produce high-confidence yet incorrect predictions, and consistency regularization then reinforces these errors throughout training. Existing semi-supervised learning (SSL) methods estimate pseudo-label reliability almost entirely from the visual classifier itself---maximum probability, adaptive thresholds, or entropy---signals that remain blind to whether a predicted class is \emph{semantically} compatible with the visual representation. We propose \textbf{ReCalMatch}, a reliability-calibrated semantic framework for semi-supervised fine-grained recognition. Rather than treating textual semantics as auxiliary supervision, ReCalMatch uses multi-aspect semantic prototypes as \emph{calibration evidence} for pseudo-label learning. We construct class-conditioned semantic prototypes from class names and domain-specific semantic aspects, and measure a \emph{visual--semantic agreement} score between each unlabeled embedding and its pseudo-label prototype. This agreement is combined with prediction confidence and entropy into a single reliability weight that down-weights pseudo-labels that are visually confident but semantically inconsistent. A semantic consistency term and a semantic margin regularizer further sharpen prototype separability under limited labels. Extensive experiments on CUB-200-2011, Stanford Dogs, NABirds, and iNaturalist18 show that ReCalMatch consistently improves strong SSL baselines, with the largest gains in low-label regimes where pseudo-label noise is most severe.

---


### 185. [Confident but Wrong: A Constrained Decoding Diagnostic for Low-Resource Automatic Post-Editing](https://arxiv.org/abs/2609.29680)

**<font color=#1a73e8>作者：</font>** Isuru Wijesiri, Nisansa de Silva, Kavindu Warnakulasuriya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Post-Editing (APE) for low-resource languages (LRLs) often fails to improve Machine Translation (MT), and the score alone cannot say why: whether more training would help, or whether the training data is too inconsistent to learn from. We introduce a black-box, inference-time diagnostic that tells these two cases apart without retraining or annotation. It varies an edit-distance penalty $\lambda$ that drives the model from free editing towards copying the MT, and reads two signals: (1) the shape of the Translation Edit Rate (TER)-vs-$\lambda$ curve, U-shaped if edits from the model reduce error and monotonically decreasing if none does; and (2) the ordering of constraint variants that trust model confidence to increasing degrees, which shows whether confidence tracks edit quality. Across decoder-only and encoder-decoder models on English-Sinhala, the diagnostic exposes two failure modes consistent with a heterogeneous post-edit signal as the underlying cause: Binary Collapse, where the model copies the MT or makes off-target edits, and Confident Miscalibration, where the confidence signals we test do not separate useful edits from unnecessary ones. The pattern holds on English-Marathi and English-Tamil, with the failure modes tracking the post-edit distribution rather than MT quality or language family. Beyond diagnosis, the curve shape prescribes a concrete next step for practitioners; in the favorable case, a static constraint yields a free inference-time accuracy gain. We release the first English-Sinhala (~66k) and a new English-Tamil (~39k) APE datasets with all code.

---


### 186. [Named Entity Recognition using Sliding Window Approach](https://arxiv.org/abs/2609.29682)

**<font color=#1a73e8>作者：</font>** Hariom Ingle, Ronit Ghode, Ishwari Gondkar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition (NER) is a core NLP task, but transformer-based sentence-level models struggle with long documents because of fixed input-length limits: truncation drops content, and non-overlapping chunking fragments entities at segment boundaries. We introduce an inference-only pipeline that extends a frozen NER model, MahaNER-BERT, fine-tuned on the MahaNER corpus, to document-level prediction via overlapping sliding windows that are merged into a single annotation, without any retraining or architectural change.
We evaluate the pipeline on six document-level corpora built from the MahaNER test set using two strategies: Normal Repeat, which duplicates sentence sequences to extend length while preserving contextual continuity, and Random Repeat, which concatenates distinct sequences to produce longer, heterogeneous inputs, each instantiated at three length levels, across several sliding-window configurations. The model retains a macro F1-score of up to 0.8902, with variation staying below one percentage point regardless of document length or construction strategy. Compared with the conventional non-windowed approach, the sliding-window pipeline avoids the boundary-fragmentation errors introduced by non-overlapping segmentation, yielding consistently higher and more stable document-level F1-scores.

---


### 187. [DP-IPI: A Hybrid Differential Privacy Text Rewriting Mechanism for Indirect Personal Identifiers in Clinical Texts](https://arxiv.org/abs/2609.29684)

**<font color=#1a73e8>作者：</font>** Ibrahim Baroud, Stephen Meisenbacher, Sebastian Möller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the strengths of modern anonymization and de-identification techniques, the risk of re-identification remains significant due to the indirect identifiers remaining in texts. To address this problem, recent works have applied text rewriting under Differential Privacy (DP) to prevent data linkage by perturbing texts via noise addition. Such methods privatize all tokens in a text indiscriminately, diminishing text quality and usability in critical domains such as in clinical settings. Focusing on indirect personal identifiers (IPIs), we introduce a utility-preserving DP text rewriting method that only privatizes spans containing IPIs. We show that our method effectively reduces re-identification risks in clinical texts while being producing more coherent and usable output texts, leading to higher privacy-utility trade-offs. In this, we demonstrate the effectiveness of hybrid text privatization, which leverages the promise of DP in an efficient, usable manner.

---


### 188. [TransCAVE-E: A distributed virtual reality testbed for adaptive external human-machine interfaces](https://arxiv.org/abs/2609.29686)

**<font color=#1a73e8>作者：</font>** Yun Ye, Zexuan Li, Haoyang Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> External human-machine interfaces (eHMIs) are evolving from predefined displays toward adaptive communication strategies that respond to changing traffic and road-user states. This transition requires experimental infrastructure that supports human-in-the-loop (HIL) interaction, software-in-the-loop (SIL) algorithm execution, reusable experiment orchestration, and synchronized multimodal human-factors evaluation. This paper presents TransCAVE-E, a distributed virtual-reality testbed for developing and validating adaptive and intelligent eHMIs. The platform integrates three coupled modules: a Scenario Design Center for configurable traffic environments and experimental conditions; an eHMI Algorithm Module for bidirectional real-time coupling between simulation and external algorithms; and a Data Management System that synchronizes trajectories, eye-tracking, physiological, system-log, and subjective data. A distributed multi-agent architecture supports synchronous interaction among pedestrians, human drivers, automated vehicles, and other traffic entities. Two use cases demonstrate the platform. In an AV-pedestrian experiment, an intent-recognition-based eHMI improved decision efficiency by 12.8% and 13.0% in yielding and non-yielding scenarios, reduced gaze distraction by 17.1% in the yielding scenario, and reduced unnecessary prompts by 40% in the non-yielding scenario while maintaining interaction safety. An HV-AV study further demonstrated real-time SIL validation of a game-theoretic information-disclosure strategy under active driver interaction. TransCAVE-E provides an extensible and reproducible infrastructure for closed-loop evaluation and iterative refinement of intelligent human-vehicle communication strategies.

---


### 189. [Not All Synthetic Data Are Equal: Expert-Committee Audit Screening for Imbalanced Crash-Injury-Severity Prediction in Automated Driving Systems](https://arxiv.org/abs/2609.29687)

**<font color=#1a73e8>作者：</font>** Zewei Li, Qiaoqiao Ren, Hang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated driving systems (ADSs) are increasingly operating on public roads, raising safety concerns, yet reliable prediction of crash injury severity remains difficult because crash reports are limited, severe outcomes are rare, and injury classes are highly imbalanced. Existing augmentation methods mainly increase minority-class sample size but rarely assess whether generated samples are credible for safety-critical prediction. This study proposes Expert-Committee Audit Screening (ECAS), a credibility-aware sample acceptance framework for ADS crash injury severity prediction under data imbalance. Using 1,477 incident-level ADS crashes from the National Highway Traffic Safety Administration Standing General Order records, ECAS audits generated minority samples through a real-data-only expert committee based on label support, boundary separation, committee agreement, and local plausibility. Within-class percentile normalization and Pareto non-dominated sorting select accepted samples without manually assigned evidence weights. With a fixed backbone combining normalizing flow augmentation and a Tabular Prior-data Fitted Network (TabPFN) classifier, the best ECAS configuration achieved the highest balanced accuracy, macro-F1, and minor-injury recall among all evidence configurations. Local neighborhood analysis showed that ECAS-accepted samples were better supported by nearby real minority crashes than unscreened retained samples. Shapley additive explanations and partial dependence plots further indicated that lower injury severity classes were mainly associated with crash counterpart and pre-crash movement, whereas moderate-plus injuries were more sensitive to posted speed limit and operating context. These findings support a shift from quantity-oriented augmentation to credibility-aware sample acceptance for ADS safety prediction and risk governance.

---


### 190. [Predicting Symptoms of Amotivation and Anhedonia among University Students with a Novel Oversampling Method](https://arxiv.org/abs/2609.29690)

**<font color=#1a73e8>作者：</font>** Dang Nguyen, Bao Duong, Arun Kumar 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> University students experience disproportionately high rates of common mental health conditions, such as depression, which can impair learning, social functioning, and overall well-being. Within this context, symptoms of amotivation (i.e. loss of motivational drive) and anhedonia (i.e. diminished interest or pleasure) are particularly debilitating, yet they frequently go undetected. Developing new approaches to identify students with prominent amotivation and anhedonia could enable earlier and more targeted intervention. Machine learning (ML) methods have increasingly been used to classify individuals according to symptom severity. However, these ML models often suffer from class imbalance, where the majority of cases fall in the low-symptom group and relatively few in the high-symptom group. This imbalance can reduce model accuracy and bias predictions. To address this, studies commonly employ the popular oversampling strategy SMOTE. However, SMOTE has a notable limitation: it may generate invalid values for nominal variables. In this paper, we introduce a novel and effective oversampling method that addresses this shortcoming. Our approach leverages a predictive model to generate nominal variables, rather than interpolating them. We validate our method on a large-scale GPS location dataset collected from university students and demonstrate that it is significantly better than existing oversampling approaches in predicting elevated symptoms of amotivation and anhedonia.

---


### 191. [Bandit Multiclass PAC Learning: Corrected Lower Bounds, Exact Families, and a Confidence Direct-Sum Phenomenon](https://arxiv.org/abs/2609.29694)

**<font color=#1a73e8>作者：</font>** Guangjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study realizable multiclass PAC learning with bandit feedback: the learner observes an i.i.d. instance, predicts one of $K$ labels, and learns only whether the prediction was correct. Hanneke, Meng, Moran, and Shaeiri (arXiv:2605.25678) characterized the optimal sample complexity via the bandit DS dimension $\mathrm{BDS}$ up to logarithmic factors, and asked whether every class admits sample complexity $O((\mathrm{BDS}+\log(1/\delta))/\epsilon)$.
First, we show that the published lower bound $\Omega((\mathrm{BDS}+\log(1/\delta))/\epsilon)$ is incorrect as stated: we exhibit explicit classes with $\mathrm{BDS}=K-1$ whose sample complexity is exponentially smaller, and locate two independent gaps in its proof. We repair the lower-bound theory around a new anchored dimension $\mathrm{aBDS}\le\mathrm{BDS}$, proving a constant-free three-part lower bound. On the upper-bound side we remove the ambient label count $K$ entirely, proving $O((B\log^3 B+B\log(1/\delta))/\epsilon)$ for $B=\mathrm{BDS}$, plus a constant-confidence bound via a new fiberization lemma; for two natural families we determine the sample complexity up to constant factors.
Finally, we answer the open question in the negative under its uniform-constant reading, and show the failure is intrinsic: for an explicit affine multiplexer class we establish the full confidence profile $\Theta((n\min{n,\log(1/\delta)}+\log(1/\delta))/\epsilon)$, a confidence direct-sum regime where a multiplicative $\log(1/\delta)$ cost is information-theoretically necessary, followed by a rank-saturation phase transition. Two classes with identical dimension profiles can have polynomially different sample complexities, so no characterization by these dimensions alone is accurate to polylogarithmic factors. We also show these results are consistent with additive-confidence list-PAC guarantees via the ListCascade bridge.

---


### 192. [An Agnostic Sample Compression Scheme for Squared Loss of Near-Linear Size in the Fat-Shattering Dimension](https://arxiv.org/abs/2609.29696)

**<font color=#1a73e8>作者：</font>** Guangjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We construct, for every function class $\mathcal{F}\subseteq[0,1]^{\mathcal{X}}$ and every accuracy $0<\alpha\le 1$, an agnostic sample compression scheme for the empirical squared loss: for every finite sample $S\in(\mathcal{X}\times[0,1])^m$ with arbitrary (noisy) labels, the scheme stores at most $O(\mathrm{fat}(\mathcal{F},c'\alpha)\cdot\log^3(2/\alpha))$ original labeled examples and auxiliary bits, independent of the sample size $m$, and reconstructs a function $\hat f$ with $L_2(\hat f,S)\le\inf_{f\in\mathcal{F}}L_2(f,S)+\alpha$. This resolves, in the positive, the open problem of Attias, Hanneke, Kontorovich, and Sadigurschi (ICML 2024, Section 5), which asks for an agnostic $\ell_2$ compression scheme of size $\mathrm{fat}(\mathcal{F},c\alpha)\cdot\mathrm{polylog}(c/\alpha)$. All previously known bounded-size constructions, agnostic and even realizable, incur a multiplicative dual fat-shattering factor, which can be exponentially larger than the primal dimension; our scheme removes the dual factor entirely, including in the realizable case. The dual factor in prior work enters solely through a sparsification step that forces uniform approximation on the sample. By targeting only a $(1-\epsilon)$-fraction of sample points, which suffices for an average-loss guarantee over a bounded range, K'egl's boosting margin bound yields $O(\log(1/\epsilon))$ rounds independent of $m$, and sparsification is never needed. The booster's synthetic target labels (values of a near-optimal $f^*\in\mathcal{F}$) are transmitted through quantized side-information bits attached to stored original examples, and the cross term of the squared loss forces the weak-learning scale $\Theta(\alpha)$, matching the same-scale form of the open problem.

---


### 193. [Safety-oriented pedestrian trajectory prediction at urban intersections using time-to-collision and crossing-zone context](https://arxiv.org/abs/2609.29706)

**<font color=#1a73e8>作者：</font>** Erel Avineri, Yftach Gil, Yehudit Aperstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate pedestrian trajectory prediction is important for proactive road-safety applications, particularly at urban intersections where pedestrian motion is shaped by both vehicle interactions and crossing context. This study presents a safety-oriented trajectory-prediction framework that combines pedestrian motion history with Time-to-Collision (TTC) information and crossing-zone indicators. Using naturalistic trajectories from one urban intersection in the inD (Intersection Drone) dataset, several neural architectures were evaluated with 1.6 s observation and 2.4 s prediction horizons. A pooled Long Short-Term Memory (LSTM) separately encodes TTC histories and crossing-zone context before integrating them with pedestrian positions. In addition to conventional Average Displacement Error (ADE) and Final Displacement Error (FDE), prediction performance was assessed using the frequency and magnitude of errors exceeding a study-defined 1 m tolerance. A weighted loss was also introduced to place greater training emphasis on large coordinate-wise errors. Applying this loss to the position-only LSTM reduced ADE from 0.210 to 0.190 m and FDE from 0.550 to 0.503 m, while reducing ADE and FDE exceedance counts by 34.8% and 19.8%, respectively. The final pooled configuration incorporating TTC and crossing-zone information achieved an ADE of 0.184 m and FDE of 0.491 m, with further reductions of 33.5% and 6.3% in ADE and FDE exceedance counts relative to the safety-oriented position-only LSTM. The results indicate that safety-oriented training and structured integration of interaction and contextual information can reduce large trajectory-prediction errors, although broader validation across pedestrians, sites, and datasets is required.

---


### 194. [Revalidation Beats Stateful Routing for Scientific Surrogates Under Distribution Shift](https://arxiv.org/abs/2609.29715)

**<font color=#1a73e8>作者：</font>** Harshil Lodhiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate models are often chosen during development and then left in place as new measurements arrive. That practice becomes risky when noise, input support, or physical parameters change. We asked whether such changes call for a stateful adaptive controller, or whether it is enough to validate the candidate models again on each new batch. To study this question, we built RegimeShift-Surrogates, a reproducible streaming benchmark spanning eight analytic and dynamical tasks, four stationary or shifting regimes, ten held-out seeds, and eight classical, multilayer-perceptron, and Kolmogorov-Arnold network surrogates. The confirmatory run contains 30,720 model fits and 3,200 scored deployment windows. Choosing the model with the lowest validation loss in the current window yields mean log regret 0.091 against a per-window oracle; the best fixed model chosen in hindsight yields 0.192. The paired difference is -0.101 (hierarchical bootstrap 95% CI [-0.165, -0.040]; Holm-adjusted p = 0.0469), with revalidation ahead in 26 of 32 task-scenario combinations. None of the stateful alternatives, including exponential smoothing, dual-timescale adaptation, Page-Hinkley resets, or margin gating, improves the pooled result, and delayed bias correction makes it worse. Oracle choices also differ substantially by task: k-nearest neighbors dominate the damped oscillator, vanilla KAN is often selected for two-dimensional surfaces, and MLPs lead on the Runge and Van der Pol tasks. In this benchmark, fresh validation evidence is useful; carrying old evidence forward is often not.

---


### 195. [TopoFuse: Topology-Aware Tri-Planar Fusion for 3D Cryo-Electron Tomography Segmentation](https://arxiv.org/abs/2609.29717)

**<font color=#1a73e8>作者：</font>** Rohit Kumar Salla, Neelesh Gupta, Xingjian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated segmentation of cryo-electron tomograms routinely produces masks that are voxel-accurate but topologically broken: membranes fragment, organelles merge into one another, and enclosed cavities collapse. Existing topology-aware losses reduce these violations but cannot eliminate them, because topology is encouraged through gradient pressure rather than structurally enforced. We introduce TopoFuse, which reframes topology as a differentiable projection operator rather than a loss penalty. At each forward pass, the projection operator $\mathrm{Proj}_T$ (a PH-guided sparse edit) identifies the critical voxels responsible for topological violations via bottleneck matching and applies sparse edits to satisfy a specified topology target (diagram feature counts and lifetime budgets) for dimensions $d \in \{0,2\}$. If the projection converges, the output satisfies those constraints on the downsampled grid ($s=2$); when it does not, a repair certificate exposes this explicitly, enabling downstream filtering. A topology prior head predicts the correction target directly from input features, removing any dependence on ground-truth topology at inference. Across three cryo-ET benchmarks, TopoFuse reduces Betti number error by 54% over the strongest soft-loss baseline ($p < 0.001$), improves Dice by 4.6 points, and edits only 3.1% of voxels to achieve this.

---


### 196. [SALI: Shot-Aware Late Interaction for Cross-Shot Relation Matching in Text-to-Video Retrieval using Film-Grammar Knowledge](https://arxiv.org/abs/2609.29721)

**<font color=#1a73e8>作者：</font>** Toya Oyama, Rainer Lienhart, Shin'ichi Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video retrieval usually represents a video clip by a single embedding. This embedding often loses important relations between people. E.g., an interaction "Anna confronts Mark" is regularly filmed as alternating shot and reverse shot of both (Fig. 1a). No single shot or averaged embedding over clip shots captures this relation. Thus, we propose SALI (Shot-Aware Late Interaction). It extracts the subject and object from a single-sentence query, and matches the query, its subject and object text embeddings against each visual shot embedding of a video clip. The matching operator is greedy max or optimal transport. A film-grammar penalty in fine-tuning adds a small, consistent shift. Built on CLIP4Clip-meanP, SALI keeps overall recall on par on Condensed Movies and ActivityNet while raising R@1 on multi-shot relation queries by 3 and 12 points, the most among all compared methods, and improves such queries on MSR-VTT at a cost of 1.4 R@1 overall.

---


### 197. [A General Framework for Budgeted Threshold Incentives on Request](https://arxiv.org/abs/2609.29724)

**<font color=#1a73e8>作者：</font>** Zhuolin Wu, Chengrui Zhu, Wenhua Nie 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-demand delivery platforms pay riders through incentive activities whose tiers are set from recent completions of riders with a similar history. Operators request such plans for changing periods, rider populations, payment rules and budgets, often for holidays or bad weather, where randomized trials are scarce and take months to collect. We present a request-driven framework that composes four stages (conditional prediction, population reduction, trajectory integration and budget allocation) through seven replaceable modules that exchange conditional trajectory laws, whose award probabilities and award-marked moments give payment and uplift for any activity rule. A response-correction step reweights trajectories from abundant no-offer history to match the moments of a short pilot. We prove that, on a fixed plan menu and given the stage errors, the end-to-end value loss is bounded by the sum of four stage terms, and that for every stage there are instances on which omitting it leaves an error floor the others cannot remove. On 3,000 riders over 45 weekly origins, all 127 windows of a week are answered 11.04x faster with identical scenarios and at most 0.92% value lost by the allocation. On 24 new controlled response laws, the response correction with a one-week pilot lowers regret by 51.2% relative to a trial with the same nominal randomized rider-weeks, and a four-week pilot with exact summation comes within +0.007 of an 18-week trial. In registered studies where windows, populations, rules and binding budgets change from request to request, the framework's regret is below that of a trial with the same nominal rider-weeks and below dose interpolation of the same pilot data, and reusing its one-off preparation answers 60 requests 14.1x and 2.70x faster with identical answers. Against a nine-offer trial fitted with the framework's own dose curve, one-week regret is 0.055 lower.

---


### 198. [A Multimodal Dataset for Survival Prediction in Resected Pancreatic Ductal Adenocarcinoma](https://arxiv.org/abs/2609.29726)

**<font color=#1a73e8>作者：</font>** Anh-Tien Nguyen, Mawuko Tettey, Jacqueline Michelle Metsch 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Survival research in pancreatic ductal adenocarcinoma (PDAC) is limited by the scarcity of datasets linking whole-slide histology with clinical, molecular, and long-term outcome data. We present a retrospective single-centre cohort of 302 patients who underwent PDAC resection at University Medical Center Gottingen. The dataset comprises 446 H&E whole-slide images, clinicopathological variables, targeted sequencing data for 154 patients, and overall-survival outcomes. During follow-up, 253 patients died, and the median follow-up was 76 months.
To establish initial reference values, we evaluated fourteen survival-prediction configurations using identical five-repetition Monte Carlo cross-validation partitions. Ridge Cox regression using numeric clinicopathological variables achieved a mean concordance of $0.649 \pm 0.042$ and $0.652 \pm 0.046$ after adding KRAS and TP53 mutation status. The image-only attention model achieved $0.603 \pm 0.030$, while multimodal fusion achieved $0.619 \pm 0.025$, the highest concordance among the neural models. These results establish promising initial benchmarks for future research using this pancreas-specific multimodal dataset, paving the way for external validation.

---


### 199. [C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks](https://arxiv.org/abs/2609.29735)

**<font color=#1a73e8>作者：</font>** Xueshu Chen, Yan Wang, Zihao Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks require preserving and later recovering cross-session evidence under a bounded, query-blind memory budget. Existing compression can discard fine-grained visual cues or conflate semantically similar but incompatible observations. We present C3M, a cross-session multimodal memory organization that maintains a bounded active index over persistent source text-image evidence. Relation-aware updates consolidate safe redundancy while preserving complementary and incompatible records. At query time, budgeted routing selects useful index pages and expands their associated source evidence under a fixed reader budget. Together, these mechanisms establish a compact, provenance-preserving multimodal memory organization for cross-session long-horizon tasks, retaining temporal distinctions and source links required for reliable downstream reasoning. Code is available at this https URL.

---


### 200. [TopU-LBVS: A Realistic Multi Target Benchmark for Ligand Based Virtual Screening](https://arxiv.org/abs/2609.29740)

**<font color=#1a73e8>作者：</font>** Surbhi Kumar, Yuhe Zhou, Varun Shiralkar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ligand-based virtual screening (LBVS) is a practical first-pass tool in early-stage drug discovery, but existing benchmarks can overestimate performance through random negatives, easy decoys, limited target coverage, and non-standardized evaluation protocols. We introduce TopU-LBVS, a multi-target benchmark for LBVS under hard-negative screening conditions. Starting from curated ChEMBL~35 bioactivity data, TopU-LBVS covers 93 protein targets across 7 protein classes and constructs target-specific screening libraries with property-matched, structurally similar decoys at a fixed 1:40 active-to-decoy ratio. Libraries contain roughly 400 to 10,000 compounds and are designed to reduce simple physicochemical and nearest-neighbor fingerprint shortcuts.
TopU-LBVS provides three fixed protocols. TopU-LBVS-full evaluates ChEMBL$^\ast \rightarrow$ TopU generalization across all 93 targets. TopU-LBVS-low evaluates low-data TopU $\rightarrow$ TopU learning within the hard-negative distribution. TopU-LBVS-mini provides a compact seven-target protocol with a paired random-decoy control that changes only the test decoys, enabling low-cost development and direct measurement of the gap between random ChEMBL$^\ast$ and TopU decoys. Across ten reference baselines spanning fingerprint methods, molecular GNNs, fingerprint hybrids, and modern molecular models, performance under random-decoy evaluation degrades sharply under hard-negative screening. We release data, fixed splits, evaluation code, and baseline implementations for reproducible comparison of future LBVS and molecular representation learning methods.
Code and data are available at this https URL and this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
