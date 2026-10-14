# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**601-650**（第 13/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 601. [A Time-Synchronous Prequential Evaluation Framework for Next-Week Student Disengagement Prediction from Moodle LMS Logs](https://arxiv.org/abs/2610.17490)

**<font color=#1a73e8>作者：</font>** David Otoo-Arthur, Terence L. van Zyl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrospective evaluation of early-warning models may not reflect information available when predictions are issued and outcomes become observable. We developed a time-synchronous prequential framework for online prediction of next-week student disengagement, operationalised as inactivity onset, from Moodle logs. Ordered by calendar time, models were updated only with available outcomes and remained unchanged for all predictions at each prediction cutoff; development, calibration and evaluation were chronologically separate. We compared stochastic gradient descent logistic regression (SGD-LR), online sequential extreme learning machine (OSELM) and echo state network (ESN) across predictive performance, fixed, frozen and rolling threshold policies, calendar-time variation and four behavioural feature sets. Held-out evaluation comprised 49,329 predictions with 37.68% inactivity-onset prevalence. Discrimination was similar (average precision 0.665-0.679; ROC-AUC 0.755-0.774). OSELM had the highest recall, SGD-LR the highest precision and specificity, and ESN the highest Matthews correlation coefficient and balanced accuracy. Lower thresholds increased recall and alert volume, whereas rolling adaptation did not improve MCC over frozen thresholds. Weekly performance and calibrated-probability distributions varied without sustained deterioration. During model selection, cumulative-and-temporal features achieved the highest individual-set AP, with modest gains from combining all feature groups. These findings indicate that streaming early-warning evaluation should consider calibration, threshold-dependent performance, alert burden and calendar-time variation alongside aggregate discrimination.

---


### 602. [Longitudinal Learner Participation Profiling in Online Learning: Heterogeneous Consensus Clustering under Unequal Observation Windows](https://arxiv.org/abs/2610.17494)

**<font color=#1a73e8>作者：</font>** David Otoo-Arthur, Terence L. van Zyl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning management system traces are clustered to identify participation profiles, but unequal observation windows may cause profiles to reflect duration rather than participation alone. Using 16,448 complete learner--course sequences from 4,599 learners across 152 courses at a South African public university, we evaluated eight participation measures. All remained related to observation-window length even when expressed as rates or shares. Course-grouped adjustment reduced these relationships. Five retained measures were evaluated using K-means, Gaussian mixtures, Ward agglomerative clustering and K-medoids, with standardised measures and principal-component summaries. Evidence supported a broad two-profile grouping and a more detailed adjusted four-profile consensus: Gradually declining, Early-concentrated, Cyclical variable and Sustained active. Profile membership accounted for 2.87% of the variation in duration in the primary consensus, versus 38.18% using original measures. Mean assignment support was 0.739; 8.35% of assignments fell below 0.50, with greatest uncertainty in Sustained active. Two week-by-week sequence analyses agreed strongly with each other but only modestly with the four-profile consensus, indicating that the profiles combined multiple aspects of participation rather than distinct sequence patterns. Profiling should therefore assess duration effects, compare clustering methods and participation summaries, and report assignment consistency.

---


### 603. [Merit: Making every modality earn its contribution in multimodal attention decoding](https://arxiv.org/abs/2610.17507)

**<font color=#1a73e8>作者：</font>** Ali Alavi, Donald S. Williamson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> More than 1.5 billion people have hearing loss. When several people talk at once, hearing aids amplify every voice alike. Auditory attention decoding (AAD) aims to solve this by reading a listener's brain signals to find the attended talker, letting the device amplify only them. A real device will not see the brain alone; smart glasses and earbuds also track eyes, head, and scene. These behavioral signals help, as people often look at who they listen to. However, they show where a listener looks, not whom they hear. A decoder relying heavily on them fails when a listener cannot move their head or listens without looking - exactly when a brain-based device is needed. A multimodal decoder must use these signals without letting them replace the electroencephalogram (EEG). Accuracy alone cannot show whether it does. We present MERIT, a decoder and evaluation method asking: how much accuracy does each input earn? MERIT shuffles each input stream across test examples, measures the accuracy drop, and splits the result across streams using Shapley values. It also blocks two shortcuts: candidate audio is checked before training so it cannot reveal the answer, and the scoring function cannot beat chance if it ignores the brain. On a public dataset with EEG, eye tracking, head motion, and scene video, MERIT improves on the published benchmark, reaching 0.82 four-way accuracy within listeners and 0.74 on unseen listeners (chance is 0.25). The measurement reveals what accuracy hides: adding behavioral streams raises overall accuracy but almost halves the brain's share of it. On two other datasets, the same tests find a label imbalance in a widely used benchmark and flag results that accuracy alone would report as brain decoding.

---


### 604. [CÆNL: Collapse-Based Active Neural Learning with Objective-Aligned Representation Control](https://arxiv.org/abs/2610.17509)

**<font color=#1a73e8>作者：</font>** Saad Alqithami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning changes the representations used to acquire subsequent labels. We study this interaction through Collapse-Based Active Neural Learning (CÆNL), which separates acquisition, Dynamic Collapse Regularization (DCR), and its coefficient policy. DCR penalizes a normalized within-class to between-class scatter residual above a frozen reference, with a separate class-separation safeguard. Fixed, scheduled, deterministic-feedback, and learned-feedback policies apply this objective. The analysis establishes scatter invariances, conditional local descent, and coefficient bounds, and shows why clean geometry alone cannot guarantee input robustness. Six-seed classification comparisons are complemented by a 104-run study with separate control selection and ten-seed evaluations on each of two backbones. At 60% annotations on ImageNet-100, entropy acquisition with DCR and MACC-Lite reaches 73.420 +/- 0.512% accuracy on ResNet-50 and 73.086 +/- 0.397% on ResNet-18 (mean +/- seed SD), exceeding entropy alone by 1.742 and 1.834 percentage points. Both gains survive Holm correction under paired-t and exact sign-flip tests, with unchanged feedback settings across backbones. Independently tuned constants attain slightly higher mean accuracy; the paired comparisons establish neither adaptive superiority nor equivalence. Separate six-seed spectral studies yield a small fixed-regularization C4 loss reduction, worse CIFAR-10 diffusion FID, and inconclusive AudioCaps captioning effects. Earlier classification studies find near-zero AutoAttack accuracy at L-infinity radius 8/255 and no added benefit from learned control. The results support the evaluated combined classification treatment and identify the task dependence of geometry-informed regularization.

---


### 605. [Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513)

**<font color=#1a73e8>作者：</font>** Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) allows for high-quality real-time novel-view synthesis. Since its inception in 2023, its explicit and highly configurable scene representation has been extended toward sparse-view generation, dynamic reconstruction, efficiency and compression, streaming, and simultaneous localization and mapping (SLAM). Although Gaussian Splatting can provide real-time rendering, rendering an existing representation is distinct from constructing, updating, or maintaining the scene itself. In this survey, we synthesize current literature, categorize them and provide a connection of current approaches and tools towards an end-to-end pipeline. Explicitly, we categorize GS scene reconstruction into five overlapping families: single-shot generation, dynamic representations, efficiency and compression, streaming and immersive systems, and Gaussian Splatting SLAM. We distinguish render-only throughput from task-specific scene generation, update, tracking, mapping, and optimization costs, and combine controlled sparse-view benchmarking with native evaluations to identify cross-family quality, latency, memory, and update-cost trade-offs.

---


### 606. [Enhanced Detective: A Dual-Stage Proactive Defense Against Internal Poisoning Attacks in Financial Fraud Detection Using Federated Learning](https://arxiv.org/abs/2610.17523)

**<font color=#1a73e8>作者：</font>** Maria-Ioana-Andrea Ivan, Orhan Ermis, Ruxandra F. Olimid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With recent developments in Artificial Intelligence (AI), the adoption of distributed learning paradigms such as Federated Learning (FL) has emerged. In simple terms, FL enables multiple entities to collaboratively train AI models without sharing local data. The FL paradigm is particularly valuable in privacy-sensitive settings, such as financial services, because it enables institutions to collaboratively improve fraud-detection models while keeping sensitive transaction data local. However, FL schemes are prone to security vulnerabilities, where malicious clients can poison local data or model updates and degrade the global model, and hence the performance of the resulting model might be affected. Therefore, in this work, we propose Enhanced Detective, a dual-stage robust aggregation strategy that combines Median Absolute Deviation (MAD), distance-based update filtering, and FedMedian aggregation. Experiments on an imbalanced credit card dataset evaluate targeted label-flipping and weight-scaling attacks over 50 communication rounds. With 40% malicious clients, Enhanced Detective achieves an AUPRC of 0.796 and a Recall of 0.847.

---


### 607. [CrossPortrait: Cross-Species Portrait Animation via Adversarial Motion Alignment](https://arxiv.org/abs/2610.17532)

**<font color=#1a73e8>作者：</font>** Gezhong Pan, Zhe Li, Yunfan Tao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-species portrait animation, which aims to animate a source portrait of species A using a driving video of species B, is particularly challenging due to substantial anatomical differences in facial structures across species. Previous works typically fine-tune human portrait animation models on animal video datasets but often suffer from driving-species leakage. To address this, we propose CrossPortrait, a novel framework for expressive cross-species portrait animation, supporting diverse scenarios including human-to-animal, animal-to-human and cross-species animal-to-animal (e.g. cat-to-dog) animation. Specifically, we decompose the portrait motion into rigid head poses and expression keypoints. To accommodate species-specific facial structures while facilitating cross-species expression alignment, we introduce a species-routed expression encoder that incorporates species-specific LoRAs into a unified expression encoder. Furthermore, we introduce expression-level adversarial domain adaptation (Ex-ADA) to suppress driving-species-specific information in the expression latents, thereby mitigating species leakage and promoting a shared expression space across species. Extensive experiments show that our method enables expressive and identity-preserving portrait animation across diverse species and outperforms other state-of-the-art approaches.

---


### 608. [Discovery or Memorization? A Faithful Benchmark for Real-World Business-Logic Vulnerability Discovery](https://arxiv.org/abs/2610.17542)

**<font color=#1a73e8>作者：</font>** Rui Yang, Yichao Xu, Zhuohao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of cybersecurity agents in vulnerability discovery has increased the need for benchmarks that evaluate their capabilities accurately. However, synthetic benchmarks lack realism, real-life benchmarks are prone to contamination, and many existing benchmarks have already been saturated by current models. We therefore set out to develop a benchmark that is realistic, reproducible, resistant to contamination, and challenging. Our key insight is that real-life business-logic vulnerabilities are subtle and exercise complex application interactions, making them naturally demanding. The difficulty lies in specifying evaluation criteria precise enough to faithfully measure model capabilities while keeping the tasks free of data-leakage. We introduce AnonVul, a cross-language benchmark of 132 application-level business-logic vulnerabilities, built by a semi-automated pipeline that anonymizes each task, injects oracles from expert-written specifications, and differentially verifies proof-of-concept exploits. The benchmark spans nine languages, with two evaluation tracks on black-box and grey-box settings, where each task runs in a sandbox with specialized oracles embedded in key exploitation steps. We evaluate six state-of-the-art vulnerability-discovery agents on the AnonVul benchmark, measuring discovery success, cost-effectiveness, anonymization sensitivity, oracle validity, and failure modes. Our results show that AnonVul remains challenging, with the best agent succeeding in only 23.11% of attempts. On a matched cohort of 20 vulnerabilities, restoring software identity increases discovery from 21.25% to 40.83%, highlighting the importance of controlling recognizable software knowledge when evaluating vulnerability discovery.

---


### 609. [Reference Wording Shapes Retrieval of Robot Task Instructions](https://arxiv.org/abs/2610.17549)

**<font color=#1a73e8>作者：</font>** Jahnavi Yelamanchi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying a robot task from a short instruction is sensitive to which descriptions are available for retrieval. We investigate this effect in the natural-language instructions included with the RLBench manipulation benchmark. We extract 296 fixed descriptions from 62 publicly available task files and compare five training-free lexical rankers over 80 random choices of one indexed description per task. Exact strings assigned to conflicting task labels are excluded from the primary score. Character n-gram TF-IDF achieves 61.3% mean top-1 accuracy on the resulting held-out instructions, compared with 55.6% for BM25 and 54.9% for word TF-IDF. Across gallery choices, character TF-IDF ranges from 55.2% to 66.8%; its 5th-95th percentile range is 56.9%-64.8%. Adding a second indexed description improves character TF-IDF by 7.0 percentage points on matched queries. These results quantify the influence of reference wording and representation choice on instruction-to-task retrieval under a consistent evaluation protocol.

---


### 610. [FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching](https://arxiv.org/abs/2610.17552)

**<font color=#1a73e8>作者：</font>** Ruchang Yao, Shi Guo, Junhao Zhuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video super-resolution (VSR) models achieve efficient one-step generation through diffusion distillation. However, high-resolution inference remains costly, and distilled models are difficult to align with human preferences. These challenges call for improvements in both model architecture and training strategy. We present \textbf{FlashVSR+} to address both limitations. On the architecture side, we introduce hybrid attention based on the strong locality observed in pretrained VSR models, while retaining sparse global interaction for long-range consistency. It achieves up to $2\times$ DiT speedup and 45\% lower peak memory, enabling spatially untiled 4K VSR on a single 24GB RTX 4090. On the training side, we propose Reward-Yield Distribution Matching Distillation (Ry-DMD) for preference-aligned one-step generation. Ry-DMD uses reward-weighted teacher rollouts to incorporate black-box rewards into distribution matching, without backpropagating through the reward model. We further show that Ry-DMD generalizes beyond VSR to T2I generation. Together, FlashVSR+ delivers stronger restoration quality and substantially improves high-resolution efficiency, with consistent gains in user preference. We release our code, models, and training data at \href{this https URL}{\textcolor{FlashBlue}{\textbf{this http URL}}}.

---


### 611. [Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification](https://arxiv.org/abs/2610.17582)

**<font color=#1a73e8>作者：</font>** Junghoon Kim, Seungyoon Choi, Hyunsung Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entities in real-world systems often evolve over time: users shift between information consumption patterns, researchers migrate between fields, and firms transition between financial risk states. When such systems are modeled as dynamic graphs, these transitions correspond to nodes whose class labels change between consecutive snapshots, which we call shifters. Correctly classifying shifters is often more consequential than classifying stable nodes with persistent labels, as detecting such transitions enables timely intervention in high-stakes settings. Yet, we identify a systematic failure mode across all major dynamic graph neural network architectures: shifter performance consistently lags behind stable nodes, with errors concentrated on the old label. Our structural analysis traces this failure to embedding inertia: neighborhood aggregation keeps shifter representations anchored to the old-class centroid, and this effect is strongest precisely where it is hardest to correct, namely for shifters whose neighborhoods remain aligned with the old class. Guided by this finding, we propose CHASE, a model-agnostic CHange-Aware framework for Shifting nodEs that wraps any dynamic GNN with targeted components for detecting label shifts and overriding stale neighborhood signals. CHASE consistently improves shifter performance across all tested models and datasets (up to 114.9% and 202.5% improvement on accuracy and F1 score, respectively) while preserving stable-node performance. We additionally contribute three dynamic graph benchmarks with naturally shifting labels, filling a gap in existing resources. The source code is available at this https URL

---


### 612. [Taming Softmax at the Limits of Muon: A Unified Approach through Hilbert Geometry](https://arxiv.org/abs/2610.17588)

**<font color=#1a73e8>作者：</font>** Aditya Somasundaram, Charles Guille-Escuret, Alexander Moreno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon controls weight updates through the RMS movement of a linear layer's output. This implicitly treats the linear output as a proxy for the full module, including the nonlinearity that follows. This proxy can be misleading for softmax, where the RMS shift in activations does not faithfully measure the change in the output distribution. We propose Hilbert distance as a natural metric for bounding changes in these output distributions. Hilbert distance bounds changes in cross-entropy loss and limits probability redistribution. For softmax, it takes the form of the variation seminorm of the preactivation perturbation, allowing probability constraints to be expressed as parameter constraints. Formulating the steepest descent problem with a Hilbert distance constraint brings two recently proposed methods under a unified mathematical framework. For the LM head, solving a row-wise approximation to the resulting diameter-constrained problem leads us to RowNorm \citep{pethick2025trainingdeeplearningmodels}. For scaled dot-product attention, the same principle yields the first-order query--key steepest descent problem underlying Compositional Muon \citep{keigwin2026compositional}. These connections motivate using Hilbert distance as a guiding principle for optimizer design in softmax modules.

---


### 613. [Physical-Field-Bridged Material Parameter Inference from Multi-View Deformation Videos](https://arxiv.org/abs/2610.17591)

**<font color=#1a73e8>作者：</font>** Linrui Shou, Jie Li, Yu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating simulation-ready material parameters from visual observations is crucial for deformable-object manipulation but challenging because material properties are only indirectly revealed through physical responses. We introduce physical-field-bridged material inference, a single-pass framework that uses dense physical responses to connect multi-view RGB deformation videos with constitutive-type classification and continuous parameter regression. Unlike inverse-physics methods requiring per-scene reconstruction, online tuning, or simulation-in-the-loop optimization, our model predicts force/contact masks, projected motion-flow fields, and projected stress-response maps, then conditions material inference on these fields to reduce reliance on appearance or category shortcuts. We construct DeformFieldBench, a 3DGS MPM learning environment comprising 5,000 simulations across 100 object shapes and five mechanically informative loading modes, with dense pixel-aligned physical supervision. Our method achieves the best median errors on all four continuous parameters, improves stress-hotspot recall from 0.0762 to 0.5121, and attains 0.8676 SSIM/36.82 dB PSNR in same-simulator replay on unseen objects. Under a protocol-matched GSO evaluation, inference and future-state prediction take approximately 30 seconds, compared with 15-120 minutes for per-scene optimization. The method also yields measurable replay agreement on five real-world sequences. These results support dense physical fields as an effective bridge for fast material inference, while cross-simulator and real-world tests reveal remaining domain and identifiability gaps.

---


### 614. [Morphology-aware deep learning predicts colorectal cancer survival from whole-slide images](https://arxiv.org/abs/2610.17603)

**<font color=#1a73e8>作者：</font>** Hikmat Khan, Metin N. Gurcan, Anil Parwani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Five-year survival prediction from hematoxylin-and-eosin whole-slide images could support risk stratification, but the task is weakly supervised, and the tissue morphologies carrying prognostic information remain incompletely characterized.
Methods: We conducted a retrospective secondary analysis using TCGA-COAD/READ (n=562) for morphology-specific analysis, Alliance/ CALGB 89803 (n=424) for model development, and SurGen (n=218) for external evaluation. We propose MorphContrast, a morphology-aware contrastive multiple-instance learning framework that uses tissue labels as structural supervision for five-year survival prediction. MorphContrast combines gated-attention pooling with three auxiliary objectives: patch-level morphology labels define within-patient contrasts, outcome concordance or discordance defines cross-patient contrasts within matched morphologies, and diversity regularization discourages representational collapse. Morphology-matched patches from patients with discordant outcomes serve as hard negatives, encouraging prognostic discrimination within comparable histologic contexts.
Results: Morphology-specific models show weak but distributed prognostic discrimination: adipose tissue achieves an area under the receiver operating characteristic curve (AUC) of 0.622, stroma achieves 0.604, and both perform comparably to tumor epithelium (0.601-0.605). On Alliance/CALGB 89803, the single model achieves an AUC of 0.642, while the post hoc ensemble reaches a pooled out-of-fold AUC of 0.70 and a risk-group hazard ratio of 3.79 (95% confidence interval: 2.55-5.63). On the external SurGen colon cancer cohort (n=218), the single model and ensemble achieve AUCs of 0.669 and 0.678, respectively.
Conclusions: These findings support tissue morphology as structural supervision for outcome-aware representation learning in colorectal cancer prognosis.

---


### 615. [PLEDGE: Progressive Lossy Error-Bounded Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2610.17605)

**<font color=#1a73e8>作者：</font>** Mingze Xia, Yuxiao Li, Baixi Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D Gaussian Splatting (3DGS) codecs report reconstruction quality after compression, and give users little control over the distortion of individual primitives. We present PLEDGE, a training-free, progressive, error-bounded codec that translates four user-declared tolerances into per-primitive quantization bounds: screen-space position, footprint deformation due to rotation and scale, view-dependent color, and opacity. The bounds apply throughout a declared camera domain, including previously unseen viewpoints. Position and opacity are bounded directly; footprint deformation is bounded under the rasterizer's affine projection model, and color is bounded over all viewing directions. PLEDGE organizes quantized residuals into a progressive bitstream with explicit error bounds for every valid prefix. Experiments across thirteen scenes verify all declared per-mechanism bounds and demonstrate competitive rate-distortion performance. The four tolerances incur substantially different rate costs, so users can spend rate where their application needs it.

---


### 616. [OpenDepth: Repurposing Image Editing Priors for Robust Open-World Monocular Depth Estimation](https://arxiv.org/abs/2610.17610)

**<font color=#1a73e8>作者：</font>** Mengke Zhang, Tianyi Yang, Xinzhuo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, the integration of generative priors has revolutionized Monocular Depth Estimation (MDE), achieving state-of-the-art (SOTA) performance with remarkably high data efficiency. However, although methods based on Text-to-Image (T2I) models excel in general scenes, their efficacy degrades sharply when confronted with open-world environmental perturbations, such as illumination variations and adverse weather. Since T2I priors are optimized for semantic synthesis rather than preserving pixel-level structure, they struggle to decouple geometry from appearance under severe visual shifts, easily triggering structural hallucinations. Therefore, our core insight is to model open-world depth estimation as consistent geometric inference across multi-style images, fully leveraging the powerful structure-preserving editing priors of Image-to-Image (I2I) models. Based on this, we propose OpenDepth, a robust open-world MDE framework that introduces "Intra-Domain Awareness" -- the capability to map diverse stylistic inputs sharing identical geometry into a unified latent space. To achieve this, we first align shallow features within the Diffusion Transformer (DiT) to anchor degraded observations to unified geometric representations. Additionally, we introduce a joint RGB latent reconstruction task, requiring the model to recover clean RGB information from degraded inputs. This multi-stage strategy effectively decouples environmental style interference, compelling the model to focus strictly on underlying geometric recovery. Extensive evaluations show that OpenDepth sets new SOTA records for robust zero-shot depth estimation across standard and extreme weather benchmarks, demonstrating exceptional structural integrity and adaptability.

---


### 617. [Extending Layered Attestation into ARM Application Run-Times](https://arxiv.org/abs/2610.17614)

**<font color=#1a73e8>作者：</font>** Antonio Joia Neto, Bilel Sefsaf, Norrathep Rattanavipanon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern mobile and edge platforms provide hardware-backed attestation of application and platform integrity at load-time. However, they offer little support once application execution begins. We present ARA, an Application-Runtime Anchor for ARM that extends this load-time chain of trust into execution. ARA bootstraps from the underlying ARM platform Root of Trust (RoT) through a measured loading chain and establishes an attested protected run-time within the application address space using recently introduced ARM Permission Overlay Extensions (POE). The resulting run-time domain can host programmable RoTs for Measurement and Storage (RTM/RTS), enabling application run-time integrity verification, attestation evidence generation, and protected use of secrets while retaining efficient access to application run-time state. As exemplary uses, we instantiate ARA for protected media decryption and application control flow measurement. Our prototype and evaluation show that ARA supports frequent run-time RoT-backed operations at near in-process cost, with roughly 10x and 50x lower overhead than out-of-process equivalents. This offers a practical bridge from layered attestation to application run-time trusted computing on ARM.

---


### 618. [When Does an ASR Error Matter? Task-Role Diagnostics for Tool-Using Voice Agents](https://arxiv.org/abs/2610.17619)

**<font color=#1a73e8>作者：</font>** Xiaolong Wang, Shijie Su, Naqi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In cascaded voice agents, ASR errors can have markedly different downstream consequences: a small transcription error may leave a tool call unchanged or alter its intent or arguments. Conventional word error rate (WER), however, does not capture these differences. We introduce SpeechEvalX, a paired diagnostic protocol that evaluates how task roles affected by ASR errors influence structured tool calls. Controlled edits are matched by source utterance, edit count, and operation, while task-role labels are compared with lexical severity, BERT cosine distance, Semantic-WER, and binary criticality. Across 594 source utterances, joint call accuracy falls from 82.3% with reference transcripts to 71.9-74.9% across three ASR front ends. Number and negation edits cause 21.9-25.7 percentage-point losses, versus 1.4-2.9 points for control edits. Detailed task-role labels improve source-grouped ROC-AUC from 0.73 to 0.78 over binary criticality, showing that downstream impact depends strongly on the task role affected.

---


### 619. [Smartphone-Based, Field-Deployed AI Inspection System for Power Distribution Infrastructure](https://arxiv.org/abs/2610.17620)

**<font color=#1a73e8>作者：</font>** Sampath Balaji Masabathula, Srija Vanapalli, Gangadhar Kanchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Routine inspection of power distribution infrastructure remains challenging for utilities operating geographically dispersed networks, where conventional manual inspection can be difficult to perform consistently and at scale. This work presents a smartphone-based AI inspection system for assessing targeted distribution-infrastructure conditions from images captured by field personnel. The proposed workflow integrates image-quality and viewing-perspective validation with AI-assisted assessment of pole lean, crossarm and top-cleat tilt, voltage level, vegetation-clearance risk, and distribution-transformer (DTR)-ground clearance. The system integrates deep-learning models with monocular depth estimation, geometric analysis, and rule-based processing within a common multi-stage inspection workflow designed for practical field operation. The system was pilot deployed across five selected distribution feeders within the Eastern Power Distribution Company of Andhra Pradesh Ltd. (APEPDCL), where 1,222 defect instances were identified across the assessed categories and subsequently tracked through a rectification and verification workflow, with 84 defect instances recorded as rectified during the study period. Feeder-level interruption records were also examined over the study period; however, the available observations do not provide sufficient evidence to establish a reliability improvement attributable to the proposed system. A curated multi-module field-captured dataset, PD-Defect, is also publicly released to support reproducible research in distribution-infrastructure inspection. The field deployment demonstrates the practical integration of smartphone-based AI-assisted inspection into field inspection and maintenance activities, providing a mechanism for systematic identification, documentation, rectification tracking, and verification of targeted distribution-infrastructure defects.

---


### 620. [FedLoRD: Personalized Federated Learning based on Low-Rank Structures of Model Parameter Differences](https://arxiv.org/abs/2610.17621)

**<font color=#1a73e8>作者：</font>** Tsutahiro Fukuhara, Junya Hara, Hiroshi Higashi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose FedLoRD, a personalized federated learning (PFL) method based on the low-rank structure of the differences between the global and personalized model parameters. PFL is a branch of federated learning that aims to learn models tailored to the local data of each client under biased local data distributions. In its local training, each client learns a personalized model by regularizing the difference between its model parameters and the global ones sent from the server. The regularization function needs to be designed with priors on the model parameter difference; however, the existing PFL methods rely on empirical choices (e.g., $\ell_1$- and $\ell_2$-norms), which do not take into account the actual characteristics of the difference. The resulting mismatch of priors can lead to suboptimal personalized models. To address this issue, we propose a PFL method whose regularizer is built on an observed characteristic of the model parameter differences: they are approximately low-rank at every layer. In our method, we first formulate a local training problem with nuclear norm regularization on the layer-wise differences. We further rewrite this problem via the factorized representation of the nuclear norm so that it can be efficiently solved by a plain stochastic gradient descent method. Image classification experiments on three benchmark datasets demonstrate that FedLoRD outperforms several existing PFL methods.

---


### 621. [4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling](https://arxiv.org/abs/2610.17625)

**<font color=#1a73e8>作者：</font>** Jianhui Zhang, Zuyao Lin, Pengxin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For video generation in dynamic world modeling, observed static and dynamic content should be efficiently reused to provide conditions for repeated generation at different times and viewpoints. We introduce 4LC, a 4D latent cache with composite visual representations and a flexible spatiotemporal access interface. As a latent cache, 4LC directly reuses visual representations of static and dynamic content to provide generation conditions, avoiding per-request RGB rendering and re-encoding. As a composite cache, 4LC binds visual representations from multiple visual encoders (e.g., VAE, DINO, V-JEPA, VGGT) to shared geometry and motion, allowing the composite representations to describe the dynamic world with rich information. Besides, we design a flexible spatiotemporal interface, which directly reads the cache at independently specified times and viewpoints and combines readouts across observations, providing a common conditioning format for diverse downstream tasks. Building on 4LC, we develop 4LC-Video to address multiple video generation tasks through different configurations of source observations, spatiotemporal requests, and historical reuse, including camera control, temporal control, novel-view synthesis, scene revisits, and long-term generation. Our experiments show more efficient condition acquisition, effective spatiotemporal controllability, and scene consistency across tasks using a single 4LC-Video model without task-specific fine-tuning.

---


### 622. [Calibrated Disambiguation for Partial Multi-label Learning](https://arxiv.org/abs/2610.17635)

**<font color=#1a73e8>作者：</font>** Zhuoming Li, Yuheng Jia, Mi Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial multi-label learning (PML) aims to train a classifier on datasets whose instances are over-annotated with not only relevant labels but also irrelevant labels, which is common when datasets are collected from crowd-sourcing platform. Existing works primarily approach it from a curriculum learning perspective, leveraging the memorization effect to disambiguate noisy labels and produce robust predictions. However, these methods are based on non-adaptive weighting functions and lack theoretical guidance for optimal weighting. To overcome these issues, a calibrated disambiguation model named PML-CD is proposed. We first formulate the optimal weighting function for curriculum-based disambiguation, which is equivalent to the calibration of the model's predicted confidences, thus providing guidance for curriculum designing. To obtain the optimal weighting function from PML dataset during the training, a transferable calibrator is designed, which takes the histogram of positive samples' confidences as input, and outputs the optimal curriculum weighting for training. Prototype alignment regularization is also proposed to promote the model's performance. Experiments conducted on Pascal VOC, MS-COCO, NUS-WIDE and CUB have verified that our method outperforms existing state-of-the-art PML methods.

---


### 623. [When Should Enterprise Policy Decisions Be Learned, and When Should They Be Reasoned?](https://arxiv.org/abs/2610.17643)

**<font color=#1a73e8>作者：</font>** Hyojung Han, Ryangkyung Kang, Youngeun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An enterprise agent that answers under a written policy must choose an action before it says anything: answer, ask for a missing fact, ask for confirmation, call one or several tools, escalate, or refuse. Holding one 27B Korean enterprise model fixed, we vary whether the decision is a generated JSON object or a single constrained token, and whether the model may reason first.
On 2800 in-distribution items we did not detect an accuracy difference between the two deployed paths (93.46% vs 94.14%), while they differ about tenfold in restart stability (3.00% of actions flip vs 0.29%); they also differ in reasoning, so this is an operational comparison.
On a sealed benchmark of 300 items whose labels come from a hidden executable policy, reasoning is worth +17.3 points [+12.3, +23.0] on exact action. With reasoning off, the format difference was 0.0 points [-4.3, +4.0], a failure to detect an advantage for either interface, not equivalence; with reasoning on it is unresolved. Against a token-matched random control, boundary-targeted supervision moves the two covered boundaries by +17.5 and +20.0 points and leaves a held-out boundary unchanged. In a 3-seed training x reasoning factorial, the sealed-rendering interaction is -4.9 [-8.1, -1.7], consistent with partial substitution.
All supervision was Korean. On independently rendered English versions, the model is 0.82 points lower [-2.68, +0.93] with reasoning on, the same order as re-rendering in Korean; the reasoning-off gain from targeted supervision is not stable in either language, so we do not claim transfer.
The original text stays private as the confirmatory set. An open-model re-rendering made after these results reproduced the reasoning effect and the English verdict; the interaction kept its sign but did not replicate under item-clustered intervals. We release the model and that re-rendering with gold labels.

---


### 624. [InSight: A Mobile Assistant Helping Visually Impaired People Navigate Unfamiliar Environment](https://arxiv.org/abs/2610.17660)

**<font color=#1a73e8>作者：</font>** Junwei Zheng, Jiale Wei, Di Wen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Navigating unfamiliar outdoor environments is one of the most demanding everyday tasks for people with visual impairments (PVI). However, existing navigation systems cannot simultaneously satisfy the needs of informative perception and precise localization during navigation. This paper explores the core navigation demands of PVI through a preliminary study. Based on the results of the pre-study, we present the design of InSight, a mobile assistant that combines scene descriptions with precise localization to support PVI navigating unfamiliar outdoor environments. The offline mode of InSight runs entirely on device for real-time navigation, while the online mode streams camera frames to a self-hosted server for arbitrary object detection and accurate localization. Finally, a user study with 21 visually impaired participants validates that InSight could assist users in navigating unfamiliar outdoor environments with increased success rate and confidence compared to mainstream navigation applications like Apple Maps.

---


### 625. [ScenePercept: Scenario-Conditioned Perceptual Assessment of Real-World User-Generated Content Images](https://arxiv.org/abs/2610.17661)

**<font color=#1a73e8>作者：</font>** Shuhan Xia, Yu Chen, Xiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of mobile imaging and social platforms has led to explosive growth in user-generated content images, making their systematic and comprehensive perceptual assessment increasingly important. Existing image perception benchmarks are typically task-oriented, curating specific scenarios for quality or aesthetic assessment and applying a uniform perceptual criterion across diverse scenarios. This limits their ability to capture the scene diversity and perceptual complexity of real-world UGC images. To address these limitations, we introduce ScenePercept-Bench, a benchmark designed to reflect the distribution of real-world UGC images, comprising 23,100 images across 21 categories and 105 fine-grained scenes. To account for the influence of scene context on human perception, we design a hierarchical, scene-aware annotation protocol, covering visual quality, aesthetic perception, and scene semantics, with 15 attributes in total. Each image is annotated with an overall score, 15 attribute-level scores, and structured explanatory reasoning. Building on this benchmark, we further introduce Scenario-Conditioned Perceptual Alignment, a training framework that tackles the heterogeneity of perceptual criteria across scenarios. SCPA jointly optimizes absolute score prediction, preference ranking, and cross-scenario calibration, preserving the model general perceptual assessment ability while encouraging it to explore and adapt perceptual criteria across different scenarios. Extensive experiments demonstrate that SCPA achieves state-of-the-art performance in UGC image perception and generalizes effectively to established IQA and IAA benchmarks.

---


### 626. [Hierarchical Curriculum Learning for Surgical Video Generation: Focusing on Bilateral Axillo-Breast Approach Robotic Thyroidectomy Datasets](https://arxiv.org/abs/2610.17684)

**<font color=#1a73e8>作者：</font>** Youngbin Kong, Seungho Lee, Jae Kyung Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity surgical video generation is increasingly important for surgical education, simulation, and downstream AI training, as conventional simulation pipelines are limited by cost, realism, and scenario diversity. Adapting generic text-to-video diffusion models to surgical procedures remains difficult, however, due to complex anatomical structures, intricate tool-tissue interactions, the inherently hierarchical nature of surgical workflows, and the scarcity of curated training data outside a few well-studied procedures. We propose a surgical video generation framework that combines hierarchical procedural annotation with curriculum transfer learning. Surgical procedures are decomposed into three levels (phase, task, and action) and a pretrained text-to-video diffusion model is progressively adapted from coarse to fine-grained surgical context, supported by a dynamic sampling strategy that handles variable-resolution and variable-length surgical clips. We instantiate the framework on Bilateral Axillo-Breast Approach robotic thyroidectomy, a procedure for which no curated benchmark currently exists. Relative to the preceding task-level model, the final action-level model reduces FVD by 20.1% and FID by 15.7%, and a matched-budget ablation indicates that these gains arise from the curriculum design rather than from additional training. A user study with six clinicians rates visual realism highly while highlighting remaining gaps in anatomical accuracy and clinical reliability. The proposed framework offers a step toward AI-driven surgical simulation in procedures where curated data are scarce.

---


### 627. [LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents](https://arxiv.org/abs/2610.17685)

**<font color=#1a73e8>作者：</font>** Jingyue Cong, Estrid He, Zhuang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise agents face safety risks that cannot be determined from individual actions alone. Existing safety benchmarks largely evaluate action-local risks, overlooking failures whose safety depends on workflow state. In such state-dependent risks, the same action may be safe in one context but violate policy in another. Hence, we introduce LatentRiskBench for evaluating such state-dependent risks in enterprise settings. It pairs risky trajectories with benign counterparts that share the same terminal action but differ in latent policy-relevant states, requiring models to reconstruct workflow context rather than rely on action-level cues. We also introduce new metrics for state-dependent risk evaluation, including a suite of residual risk (RR) measures. Experiments on the benchmark show that action-level evaluation detects only 0.09 of state-dependent violations, whereas state-level evaluation reaches 0.96. Existing guardrail methods largely overlook such risks unless they are explicitly applied to workflow states. Case studies on a commercial deployed scenario further show that the safety metrics embedded in the benchmark provide a more realistic measure of safety for enterprise agents. Our dataset and code are available at this https URL.

---


### 628. [SWORD: Scene-Grounded Wasserstein Object-Relation Distance for 3D Scene Graph Prediction](https://arxiv.org/abs/2610.17692)

**<font color=#1a73e8>作者：</font>** U-Chae Jun, Jaeeun Ko, Yoonhyuk Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graph prediction is commonly optimized with object-node and relation-edge classification losses. These objectives encourage exact object and relation label recovery, but they do not directly optimize semantic proximity to the ground-truth scene graph: two wrong graphs can receive comparable penalties even when one is much closer in object roles and relation contexts. A direct graph-distance loss is difficult in general, since graph matching and graph edit distance require correspondence search and edit-cost design. Our key observation is that prior supervised 3D scene graph prediction protocols are conducted on fixed object-node indices and supervised edge slots. This can turn a scene graph comparison into a well-defined aligned graph-distance problem. To this end, we propose SWORD, a Scene-Grounded Wasserstein Object-Relation Distance that builds block-normalized object and relation ground distance metrics from training scene graph annotations through a deterministic base-to-context order, without external semantic priors. SWORD lifts these metrics to Wasserstein distances over aligned node and null-augmented edge marginals, providing semantic graph-distance supervision beyond exact-label penalties while preserving the ground-truth graph as the unique zero-distance solution in aligned marginal probability space. We prove that SWORD is a strict metric on aligned marginal probabilistic scene graphs, preserves scene-graph-grounded substitution ordering, controls additive graph-grounded semantic observables, and yields a surrogate upper-bounding decoded semantic error.

---


### 629. [zPocket: Better Pocket Finding with Frozen Co-Folding Features](https://arxiv.org/abs/2610.17696)

**<font color=#1a73e8>作者：</font>** Tally Portnoi, Allison M Keys, Benjamin R DiFrancesco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying protein-ligand binding sites (pockets) is important for understanding protein function and developing drugs. However, no public method has leveraged co-folding models for novel pocket prediction; furthermore, this task lacks a suitable benchmark as existing benchmarks are within the training distribution of co-folding models. We therefore developed PocketWatch,a curated dataset of biologically relevant ligand pockets. The PocketWatch test set consists of unseen pockets stratified by sequence similarity, structural similarity, and crypticity to enable evaluation of generalization to novel and challenging pockets. Using this dataset, we develop zPocket, a method that trains pocket-prediction heads on top of frozen features from co-folding models. We show that zPocket heads outperform baseline methods across all stratifications. Our best zPocket model achieves overall per-target AUPRC of 0.745 compared to 0.598 and 0.595 for the strongest baselines, VN-EGNN and UniSite-1D retrained on the PocketWatch split (0.559 and 0.531 when using the published weights); the widely used P2Rank reaches 0.477. We further show that zPocket can be used to outperform baseline methods on top-N+2 recall of predicted pocket centroids through clustering per-residue predictions or using zPocket to rescore centroids proposed by other models. Finally, we explore two applications of zPocket: crystallographic fragment screens and a proteome-scale scan for uncharacterized pockets on human proteins. Together these results suggest that zPocket heads built on co-folding trunk features can greatly advance ligand binding site prediction.

---


### 630. [Understanding Gene Expression-to-Image Learning: Spatial Structure and Information Fidelity](https://arxiv.org/abs/2610.17699)

**<font color=#1a73e8>作者：</font>** Xiaoqing Lian, Pei Liu, Jiahui Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-cell RNA sequencing (scRNA-seq) enables cell-level analysis of biological heterogeneity, but learning effective representations from high-dimensional, unordered gene expression profiles remains challenging. Gene Expression-to-Image (GE2I) offers an effective learning strategy by arranging gene values on pixel grids for convolutional neural networks, but its underlying mechanisms remain unclear. We study GE2I on full-transcriptome data while keeping the network and training procedure fixed. Our results reveal a trade-off between spatial smoothness and gene-level fidelity. Structured mappings produce smooth, low-frequency patterns that support faster early optimization, whereas assigning multiple genes to the same pixel obscures expression differences and can reduce predictive performance. This trade-off explains why random mappings can compete with structured layouts when many genes are represented. One-to-one gene-to-pixel assignment improves prediction across the tested visual backbones even when image smoothness decreases. We further find that the benefits of pretraining and augmentation depend on the backbone and mapping. These findings provide practical guidance for pixel allocation and the transfer of vision priors to gene expression data.

---


### 631. [A Node Embedding Framework for Model-Centric Conformance Checking in Process Mining](https://arxiv.org/abs/2610.17702)

**<font color=#1a73e8>作者：</font>** Mostafa Abbasi, Homayoun Najjaran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the quality of process models discovered from event logs is a fundamental challenge in process mining. Traditional evaluation relies on conformance metrics such as fitness and precision, which are highly sensitive to noise and deviations in event logs and therefore often fail to give a consistent assessment of discovery algorithms. We introduce a model-centric evaluation framework that combines node embeddings with Procrustes alignment to enable cross-graph comparability, since embeddings derived from different graphs reside in distinct vector spaces. The proposed PetriNetGraph method transforms Petri net process models into graph representations compatible with embedding algorithms. Comparing the node embeddings of ground-truth and discovered models through a parameterized cosine distance yields a unified and bounded metric for evaluating process discovery across datasets and methods. We evaluate the framework under static and context-aware scenarios to examine how prior knowledge of activity existence influences the assessment of structural similarity. The framework also integrates a compliance checking mechanism that localizes deviations at the activity level and an entropy-regularized node distance aggregation function that quantifies global deviations across the model. Experiments on nine publicly available event logs show that the approach provides a reliable embedding-based conformance indicator that reflects the behavior of fitness and precision. Experiments on synthetic logs with controlled noise levels confirm that it is substantially more robust to log deviations than traditional conformance metrics, PetriNet2Vec, and its dynamic-window and Procrustes-aligned variants, while remaining sensitive to process model degradation. All implementation details and datasets are publicly available.

---


### 632. [A Differentiable 3D Scene Graph Metric via Contextual Hellinger Triplet Geometry](https://arxiv.org/abs/2610.17705)

**<font color=#1a73e8>作者：</font>** U-Chae Jun, Yoonhyuk Choi, Jiwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graph prediction is commonly supervised with local object and predicate classification losses. Although effective for slot-wise label prediction, this formulation does not provide a graph-level semantic distance between a predicted scene graph and its ground truth: semantically mild label errors and structurally disruptive relational errors can be treated similarly, and subject-predicate-object facts are not compared as scene-level units. We propose Contextual Hellinger Triplet Geometry, a graph-level supervision objective that measures the semantic and structural discrepancy between 3D scene graphs. Our key idea is to reinterpret the conventional classifier outputs of a 3D scene graph predictor as an aligned probabilistic scene graph field, where object and predicate predictions jointly define contextual subject-predicate-object facts. This formulation yields a differentiable metric-based training objective with an efficient factorized implementation and can be applied to existing 3D scene graph prediction architectures without modifying their network design. Experiments on 3DSSG demonstrate that our supervision improves downstream graph-conditioned 3D scene generation, while ablation studies confirm the complementary roles of the proposed graph-level terms and user studies show better graph descriptiveness, relation plausibility, and structural preservation.

---


### 633. [Focus on What You Need: Global-to-Local Dynamic Attention for Multimodal Sarcasm Detection](https://arxiv.org/abs/2610.17707)

**<font color=#1a73e8>作者：</font>** Dehao Wu, Xingjie Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm detection has attracted increasing attention due to the widespread use of images and text on social media platforms. Existing studies generally treat the semantic or emotional inconsistency between images and text as a key cue for identifying sarcastic expressions. However, images in real-world scenarios often contain multiple visual objects, many of which are irrelevant to sarcasm-related semantics. Such redundant visual information may introduce noise during cross-modal interaction, distracting models from focusing on critical sarcasm cues and potentially leading to inaccurate predictions. To address this issue, we propose GLDA (Global-to-Local Dynamic Attention), a multimodal sarcasm detection framework that models cross-modal interactions from a global-to-local perspective. Specifically, GLDA first employs a global multimodal fusion module to capture high-level semantic interactions between visual and textual modalities, enabling the model to identify coarse-grained cross-modal inconsistencies. To further reduce the influence of irrelevant objects, GLDA introduces a local gated cross-modal attention mechanism that dynamically filters redundant visual and textual features and refines multimodal representations at a finer granularity. In addition, a multi-branch learning objective is designed to jointly optimize unimodal and multimodal representations. Experimental results demonstrate that GLDA effectively improves sarcasm detection performance and achieves competitive results compared with existing approaches. The code will be available at this https URL.

---


### 634. [Where Small Mistakes Matter: Quantifying State Criticality for Imitation Learning](https://arxiv.org/abs/2610.17709)

**<font color=#1a73e8>作者：</font>** Yusuf Umut Ciftci, Joonwon Kang, Ajay Suresha Sathya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation learning typically treats every demonstration state as equally important, optimizing a behavior-cloning objective uniformly across the dataset. Yet not all states are created equal: in a small number of critical states, even a slight deviation from the expert action can lead to a failure, while in many other states such errors are recoverable and inconsequential. We formalize state criticality in imitation learning as the worst-case degradation in downstream value induced by a bounded perturbation of the expert action at a given state. We then propose SCRIM, a practical State CRIticality Measure that estimates this quantity by training an adversarial disturbance policy and a value critic around a fixed imitation policy. SCRIM assigns each demonstration state a score reflecting how vulnerable the task outcome is to small, policy-relevant action errors. We show that these scores can be used to reweight behavior-cloning losses, improving imitation at consequential states and increasing overall task performance. We further show that SCRIM enables data curation by selecting compact, high-value subsets of demonstrations that preserve performance while substantially reducing the amount of training data. We evaluate SCRIM across various simulated and real-world robotic manipulation tasks, and demonstrate that SCRIM improves policy training, enables efficient data selection, and provides interpretable insights into which moments in a demonstration are most critical for task success. Project website: this https URL

---


### 635. [Local Leakage Resilience of Shamir Secret Sharing: Below Half Threshold Rate](https://arxiv.org/abs/2610.17711)

**<font color=#1a73e8>作者：</font>** Hai H. Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the local leakage resilience of Shamir secret sharing, where an adversary leaks a bounded number of bits from every share. For $n$ parties and reconstruction threshold $k$ over a prime field $\mathbb{F}_p$ with $p>n$, we prove the following.
(1) There is an absolute constant $c_{\mathrm{bh}}<1/2$ such that, for $k\ge c_{\mathrm{bh}}n$, Shamir sharing is resilient to arbitrary one-bit leakage from every share. The best previous threshold was $0.668n$.
(2) For every fixed $0<\delta<1/2$ and $k\ge(1/2+\delta)n$, Shamir sharing is resilient to $\left\lfloor\frac{\delta}{24}\log_2 n\right\rfloor$ bits of arbitrary local leakage per share. By a recent attack, this number of bits is optimal up to a constant factor depending on $\delta$.
(3) For every fixed threshold rate $c>0$ and $k\ge cn$, Shamir sharing is resilient to quadratic-residue leakage and to almost all local leakage functions of up to $\eta_c\log_2 p$ bits, for a constant $\eta_c>0$.
All three results follow from one analytic framework, which we develop for generalized Reed--Solomon codes: local leakage from a uniform codeword is statistically close to the same leakage from independent uniform field elements. The framework expresses the leakage distance as the norm of a function on the leakage outputs. The Efron--Stein decomposition splits this function into orthogonal components indexed by supports of dual codewords. Two tools bound the components: list recovery of the dual code, which is ordinary list decoding for one-bit leakage, and a generalized von Neumann inequality for MDS systems of linear forms that retains linearly many Gowers norms. The first tool gives the result above half, the second gives the constant-rate result, and applying both to different ranges of supports in the same decomposition gives the result below half.

---


### 636. [MissPath-FM: Flow Matching with Structured Priors for Partially Observed Time Series](https://arxiv.org/abs/2610.17715)

**<font color=#1a73e8>作者：</font>** Genpei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has emerged as a powerful alternative to diffusion models for generative modeling, but standard conditional flow matching is fundamentally misaligned with partially observed time series: starting from an uninformed Gaussian source forces the model to transport even already-observed entries from noise to the target, wasting capacity on trivially known regions. We propose MissPath-FM, a partial-observation-aware flow matching framework that redesigns the source prior and probability path for incomplete time series. MissPath-FM employs structured source priors (interpolation priors and Gaussian process posterior priors) to initialize the flow close to the observed signal, paired with a missingness-aware smooth path that allocates transport asymmetrically between observed and missing regions. We evaluate systematically across four datasets, four missingness mechanisms (MCAR, block, MNAR, irregular), two missing ratios, and three sequence lengths (T in {24, 48, 96}), totaling 48 settings against eight baselines. MissPath-FM wins 29 of 32 settings at T=48 and 45 of 48 overall (93.8%). Our ablations reveal a regime-dependent design hierarchy in which no single component suffices: under random missingness the source prior yields a large initial gain, but under structured block missingness it can fail entirely and the learned flow becomes indispensable; the missingness-aware path contributes a further 12%-26% across all regimes. Mechanistically, structured priors shorten observed-region transport by up to 15x, concentrating the velocity field on genuinely uncertain entries. Project page: this https URL

---


### 637. [Keep Your Receipts: Trustworthy Cleanup of Agent-Built Knowledge Graphs](https://arxiv.org/abs/2610.17719)

**<font color=#1a73e8>作者：</font>** Vishisht Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents build knowledge graphs as memory, and building them has become easy. Maintaining them has not. When a source is retracted, overruled, or erased, everything built on top of it (entity merges, entailed edges, community summaries) must be re-examined, and the maintainer must choose between deleting too much and too little. Deployed pipelines delete only the directly extracted facts: on our corpus that reduces contaminated queries from 32.2% to 28.0% under a real retraction and changes nothing under predicate revocation. Rebuilding is no repair for a constructor that samples: two builds of the same 300-document corpus differ in 29,475 artifacts, five times the 6,248 that removing the 61 retracted documents changes. PolyGraph instead asks the constructor for receipts: for every artifact, alternative bundles of source evidence, each claimed sufficient on its own, emitted in the call that creates it. Cleanup is then set arithmetic over the receipts, with no model calls. Because receipts are the model's own self-report, a re-derivation audit checks them by deleting the cited evidence and testing whether the constructor still produces the artifact. The audit finds that a receipt is trustworthy when it is shaped like the claim it backs. Merge receipts, each backing one narrow claim, agree with re-derivation 68% and 85% of the time. Summary receipts, elicited per sentence but stored as one flat list for the whole text, are wrong about two thirds of the time, almost always by keeping dead content. One receipt per sentence instead is 100% and 88% faithful and lets cleanup keep 33 of 35 touched summaries. The result holds under a second oracle model, a claim-blind prompt, ten further deletions, a second domain and a second constructor. Distrusting the summary layer cuts contaminated queries to 0.4% and 0.8% at 99.8 to 100% of the recall a perfect maintainer would return.

---


### 638. [Beyond Model Scaling: Rethinking Sequence Construction for Transformer-based Network Intrusion Detection](https://arxiv.org/abs/2610.17725)

**<font color=#1a73e8>作者：</font>** Zeeshan Zulkifl Shah, Muhammad Ikram, Dali Kaafar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Transformer-based network intrusion detection systems (NIDS) have shown strong potential for detecting multi-stage cyberattacks, yet most methods construct input sequences using fixed temporalization schemes rather than treating sequence construction as a systems design decision. In flow-based intrusion detection, timestamp-based windowing often fragments related attack activities while merging unrelated communications, reducing the behavioral context available to transformers. We present a unified pipeline abstraction that decomposes transformer-based NIDS into four design dimensions (traffic representation, temporalization, transformer backbone, and prediction aggregation) and propose session-coherent temporalization, which constructs sequences from communication sessions instead of fixed time windows. Experiments on three complementary intrusion detection datasets show that temporalization is the dominant factor governing transformer performance: session-coherent temporalization more than doubles Macro-F1 over timestamp-based windowing, enabling lightweight transformers to achieve up to 0.95 Macro-F1 at substantially higher inference throughput than pretrained models. We further vary the transformer size from 0.65M to 3.38M parameters and find that larger transformer models provide no measurable accuracy improvement despite substantially higher computational cost, while zero-shot cross-dataset evaluation shows only modest gains under domain shift. These results indicate that preserving communication-session semantics, rather than scaling transformer capacity, is the key to accurate and efficient transformer-based intrusion detection.

---


### 639. [DT-LoRA: Reaching Beyond the Tangent Space of Low-Rank Adaptation](https://arxiv.org/abs/2610.17730)

**<font color=#1a73e8>作者：</font>** Yangming Zhang, Ling Yi, Datong Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) often underperforms full fine-tuning. We investigate this performance gap through a tangent-space lens: factorized updates are confined to the tangent space of the current low-rank factors, leaving gradient components outside this space unexploited. An analysis of ten representative LoRA variants reveals that these residual components account for most of the gradient energy and exhibit strong spectral concentration. Motivated by this finding, we propose Dynamic Tangent LoRA (DT-LoRA), which partitions a fixed rank budget into a stable branch and a dynamic branch to capture the principal residual gradient directions. We show that these directions define the optimal update of a local quadratic model under orthogonal-complement and rank constraints. Matrix-free randomized SVD recovers them without materializing the residual gradient, while controlled write-back preserves accumulated updates and stabilizes training within the allocated rank. DT-LoRA adds no trainable parameters or inference cost over LoRA. Experiments across computer vision and natural language processing tasks demonstrate consistent improvements over LoRA and its variants. Moreover, despite being a general-purpose adaptation method, DT-LoRA outperforms task-specific approaches to open-vocabulary domain generalization for semantic segmentation, achieving state-of-the-art results. Code is available at this https URL.

---


### 640. [Train for Many, Update with One: Improving Multi-Sample Reasoning via Fenchel-Bregman Posterior Learning](https://arxiv.org/abs/2610.17735)

**<font color=#1a73e8>作者：</font>** Sungjun Lim, Adrian Robert Minut, Nico Carlsen Daheim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-sample reasoning measures candidate coverage, the probability that at least one of $K$ candidates is correct. However, minimizing the average loss of individual attempts does not directly optimize candidate coverage. We therefore formulate finite-$K$ posterior learning, which trains a distribution over solver parameters to reduce the probability that all $K$ independently generated candidates fail. To optimize this objective efficiently, we propose a Fenchel-Bregman (FB) approach that requires only one posterior draw per update, rather than the $K$ used by direct Monte Carlo optimization. FB first uses an exact Fenchel reformulation to separate problem-specific weights from the posterior update, enabling one-draw posterior updates. It then applies a closed-form Bregman update to track these weights through an exponential running average of observed failures, reusing the same draw. We instantiate FB with IVON, a variational optimizer for Gaussian posteriors over solver parameters, yielding Fenchel-Bregman IVON (FBI). Across diverse recursive and autoregressive reasoning tasks, FBI improves candidate coverage. In a matched comparison, it achieves comparable Pass@10 using 12.3% of the direct Monte Carlo baseline's measured training time per update.

---


### 641. [HiSTOR: Structured Treatment-outcome Representation Learning for High-Dimensional Longitudinal Data](https://arxiv.org/abs/2610.17739)

**<font color=#1a73e8>作者：</font>** Chuanqi Lao, Junzhou Huang, Qiao Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating potential outcomes under alternative treatment sequences is essential for personalized decision-making, but remains challenging with high-dimensional covariates and time-varying confounding. In this study, we propose HiSTOR (High-dimensional Structured Treatment-Outcome Representation), an end-to-end framework that integrates nonlinear dimension reduction with longitudinal counterfactual prediction. The central idea is to learn structured low-dimensional representations of both current patient states and evolving histories, according to their shared and distinct relationships with treatment assignment and outcomes. This extends latent-space covariate adjustment to longitudinal settings, jointly addressing covariate dimensionality and historical complexity. The resulting framework supports one-step and multi-step outcome prediction under specified treatment sequences. Experiments on CVSim and CancerSim demonstrate the superiority of HiSTOR across varying covariate dimensions, confounding strengths, and prediction horizons compared to state-of-the-art methods. To sum up, HiSTOR offers a unified approach to connecting high-dimensional covariate adjustment with longitudinal potential-outcome prediction.

---


### 642. [Geometric Structure Predicts Per-Example Neighborhood Loss Under PCA Truncation](https://arxiv.org/abs/2610.17742)

**<font color=#1a73e8>作者：</font>** Sriram Loganathan, Gokul Anand, Ragavan Arivazhagan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction can preserve the average performance of text embeddings even when a substantial fraction of their dimensions is removed. Aggregate metrics, however, do not reveal whether degradation is distributed uniformly across examples. We study per-example neighborhood stability under PCA truncation across static word embeddings and modern sentence encoders. Per-item neighbor retention varies widely and is predictable from geometric properties of the representation and its alignment with the retained PCA subspace. The fraction of centered-vector energy retained by the truncated subspace is strongest for CBOW and RI, with neighborhood contrast leading on SkipGram and the modern/Matryoshka settings (GTE approximately tied), while local density is associated with retention in marginal analysis but adds little unique information once energy and contrast are controlled (R-squared increments 0.001 to 0.010). Local intrinsic dimensionality accounts for more variation than density on modern sentence encoders in pairwise comparison. On SciFact, query density predicts retrieval degradation under aggressive compression; on NFCorpus the primary 32d association does not replicate, and a direct variance-restriction test leaves that null unresolved. Average compression performance conceals systematic per-example variation that geometry makes visible.

---


### 643. [AttenIR: Aligning Dense Visual Attention with Mesh Warping for Unsupervised Image Retargeting](https://arxiv.org/abs/2610.17743)

**<font color=#1a73e8>作者：</font>** Yun Zhang, Zhiruo Zhang, Lifei Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image retargeting aims to resize images while preserving salient content free from distortion and stretching. Recent learning-based solutions reduce reliance on traditional hand-crafted features and optimization procedures, leading to more efficient and generalizable performance. Nevertheless, existing approaches still struggle to preserve global structure and content fidelity. To address these limitations, we propose AttenIR, an unsupervised image retargeting framework requiring no manual labels, based on content-aware mesh warping, which ef- fectively couples dense visual attention with sparse mesh constraints. We for- mulate the mesh deformation as a vertex displacement regression task. Guided by saliency priors, our method jointly optimizes scale, structure, and geometry preservation losses. By combining dense visual attention with semantic features, it achieves robust, unsupervised retargeting without manual annotations. Our primary contributions include (1) a lightweight unsupervised method for image retargeting that ensures content fidelity and preserves global structure, and (2) a coarse-to-fine projection strategy to align dense visual attention priors with sparse mesh constraints, enabling content-aware deformation at the pixel level. Experiments demonstrate that our method achieves competitive and superior performance compared with both traditional and state-of-the-art learning-based methods.

---


### 644. [Gaussian Process Bandits for AI System Optimization with Selectively Verified Feedback](https://arxiv.org/abs/2610.17760)

**<font color=#1a73e8>作者：</font>** Shuang Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process bandits exploit similarities among configurations to optimize prompts, retrieval systems, and agent workflows. In these applications, however, inexpensive model-based evaluations can disagree with trusted task outcomes. We study selective verification when an action is chosen before a diagnostic is observed and trusted feedback is informative on an unknown set of diagnostic states. A finite reliability class and a finite RKHS signal dictionary describe these two sources of uncertainty. We construct a fixed audit design that combines reliability coverage with reward separation and establish a finite-time regret bound that accounts for a hard audit budget and the rounds needed to obtain informative observations. A safe adaptive extension mixes this robust design with predictable Chernoff allocations while preserving a uniform identification floor and exact expected acquisition-cost accounting. For signed-coordinate kernels, structured and diffuse reliability classes require different audit scales despite sharing the same reward geometry. Synthetic experiments distinguish these certified designs from an adaptive posterior heuristic and GP controls. Safe adaptive allocation reduces aggregate regret relative to the fixed design under the exact dictionary, but its finite-budget error certificate is numerically loose. Conditional-feedback errors can remove the heuristic's advantage and target perturbations can reverse it. Separate AI-task replays assess feedback correction and fitted-dictionary policies without establishing end-to-end validation of a learned selective-verification method.

---


### 645. [Connecting the Dots: Enduring Performance Gaps in ASR Systems Between Standard and Minority English Varieties](https://arxiv.org/abs/2610.17761)

**<font color=#1a73e8>作者：</font>** Alexander Metzger, Aruna Srivastava, Ruslan Mukhamedvaleev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) system evaluations have consistently revealed performance disparities along lines of race, gender, socioeconomic status, and language variety. While these disparities are well-documented, they are often (implicitly or explicitly) treated as issues that subsequent, larger, and more universal models will correct. We challenge this assumption of steady progress in reducing accent-related performance disparities, conducting a longitudinal evaluation of 16 prominent systems released between 2021-2025 across 8 datasets representing diverse English accent varieties. We find that the performance disparity between Mainstream US English (MUSE) and minority accents is stubborn, not reliably declining as a function of time. Specifically, while systems are reliably performant on MUSE, minority accents are subject to risks of large performance degradations between generations of systems, sometimes worsening by 65% absolute Word Error Rate. We argue that standard ASR benchmarks enact an implicit language policy privileging Mainstream US English varieties. As such, these performance disparities reflect systemic failures of language technology development infrastructure that disproportionately affect underrepresented speaker populations.

---


### 646. [Autonomous 3D Visual-Thermal Inspection for Utility-Scale Solar Farms](https://arxiv.org/abs/2610.17762)

**<font color=#1a73e8>作者：</font>** Lachlan Tychsen-Smith, Mark Cox, Brett Wood 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Utility-scale photovoltaic (PV) inspection is dominated by aerial surveys, which are effective for identifying module-level hot cells but provide limited visibility of critical components located under the array, including connectors, cabling, fasteners and structural elements. These assets are difficult to inspect consistently at scale, and their defects are often spatially small, partially occluded and difficult to localise from isolated images. We present an automated 3D visual-thermal inspection system (Tricorder) for under-panel PV asset inspection. The approach combines LiDAR-inertial Simultaneous Localization and Mapping (SLAM) with geometrically calibrated RGB and thermal imagery and machine-learning-based object detection and segmentation. Detected assets are associated with the reconstructed 3D environment, allowing visual and thermal observations from multiple viewpoints to be spatially fused and localised. We demonstrate the approach on utility-scale PV data for MC4 connector detection and connection-state recognition, thermal anomaly identification, and detection of structural components including bolts, nuts and torque tubes. The results demonstrate a pathway from image-based inspection toward spatially grounded autonomous inspection, where defects are detected and linked to specific assets and their 3D locations within the solar farm.

---


### 647. [Hybrid Parallel Bessel KAN Model: a Kolmogorov Arnold Network: integrated framework for developing a novel architecture to reconstruct the fused-basis approach via a parameter free quadratic interaction](https://arxiv.org/abs/2610.17779)

**<font color=#1a73e8>作者：</font>** Mintu Pathak, Meshv Patel, Mohendra Roy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Kolmogorov-Arnold Network (KAN) challenges traditional MLPs by placing learnable activation functions on network edges. However, scaling KANs to spatial data exposes limitations in default B-Splines. While hybrid architectures mix multiple basis families on a single edge to resolve this, monolithic superposition causes geometric overlap, parameter explosion, and severe numerical ill-conditioning ($\kappa(G) \approx 10^{16}$).To overcome this, we propose Parallel BesselKAN, which isolates B-Spline and low-order Bessel branches into parallel processing pipelines integrated via a parameter-free quadratic interaction. This decoupled architecture acts as an efficient internal ensemble, bypassing monolithic stability bottlenecks. It compresses the parameter footprint by $35\%$ while achieving $97.99\%$ accuracy on MNIST. Although standard MLPs retain a hardware speed advantage for pure vision tasks, Parallel BesselKAN provides a robust, parameter-efficient framework stabilizing mixed-basis networks and paving the way for scalable spatial adaptations like Convolutional KANs.

---


### 648. [Where Words Begin and End](https://arxiv.org/abs/2610.17782)

**<font color=#1a73e8>作者：</font>** Husein Zolkepli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forced aligners locate each word of a known transcript in the audio, and many speech pipelines depend on them. In our own data, a widely used CTC aligner inserts a pause at nearly every word boundary, and we found almost no aligner evaluated on telephone audio. We compare nine aligner configurations against human word boundaries on read, conversational and telephone English. The Montreal Forced Aligner (MFA) is the most precise, while CTC aligners consistently start words late, because most frames inside a word go to the blank token. We then fine-tune Whisper with LoRA to predict each word's start and end as timestamp tokens, training only on boundaries placed by people: 47 hours in 87 languages. The resulting aligner is more precise than MFA on every English test condition, and than MFA's own Korean and Dutch models. With FA-Bench's protocol and code on TIMIT, its word-boundary error is 11.6 ms, against 18.2 ms for the best published system. Two choices matter most on telephone conversations: placing the timestamp slots after the word they time, and training on noisy transcripts, which also makes the aligner nearly insensitive to errors in the transcript. The released model reaches 16.0 ms on real landline calls, against 36.5 ms for MFA. The models are available at this https URL

---


### 649. [Posterior-Averaged Bellman Flow Matching for Distributional Critics](https://arxiv.org/abs/2610.17788)

**<font color=#1a73e8>作者：</font>** Zeqiao Li, Yijing Wang, Haoyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributional critics model the full return distribution, providing richer signals for exploration and risk-sensitive control. Recent work has shown that flow-based critics can model these distributions flexibly and provide effective supervision across flow time for temporal-difference learning. However, unlike standard flow matching with fixed data endpoints, a flow critic is trained on Bellman targets recursively generated by a learned target critic under the current policy. Existing objectives therefore either use noisy single-endpoint supervision or rely on the learned flow itself for additional guidance. Our key observation is that an intermediate bridge state may be compatible with several Bellman endpoints, so its velocity should average their directions under the corresponding posterior. We propose Posterior-Averaged Bellman Flow Matching (PA-BFM), which samples an endpoint pool, infers the closed-form posterior over the latent anchor, and regresses to the posterior-mean velocity. Uniform anchor selection makes this target an exact finite-pool Rao--Blackwellization of the single-endpoint target: for every \(K\), it preserves the population target, cannot increase conditional variance, and its conditional variance scales as \(O(K^{-1})\). The endpoint pool supports conservative updates, while the twin return flows provide critic-disagreement and unsupported-mass diagnostics. Controlled studies show that PA-BFM reduces fixed-query target mean-squared error by \(79.7\%\) and target-induced gradient variance by up to \(98.0\%\), while improving return-distribution fidelity. Across 50 OGBench tasks and four offline-to-online scenarios, PA-BFM achieves higher aggregate performance than Value Flows.

---


### 650. [Multimodal Fusion of RGB and Complementary Modalities for Semantic Segmentation](https://arxiv.org/abs/2610.17800)

**<font color=#1a73e8>作者：</font>** Hu Cao, Yifeng Cheng, Mu He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal semantic segmentation adds an auxiliary sensing stream to RGB images (RGB-X), such as thermal, LiDAR, depth, event, polarization, or light field. This can improve robustness in poor lighting and under motion blur. But different sensors often produce features that do not match well, and fusion can become unstable. To alleviate these issues, we propose a bidirectional polarity-aware cross-modality fusion (BPCF) module that effectively captures complementary cues while enhancing feature alignment. We evaluate the framework on six modality pairings: RGB-Thermal, RGB-LiDAR, RGB-Depth, RGB-Event, RGB-Polarization, and RGB-Light Field. Our model achieve state-of-the-art (SOTA) results on eight public datasets, including MFNet, KITTI-360, DELIVER, DDD17, DSEC, MCubeS, ZJU, and UrbanLF. The codes and trained models will be released upon acceptance.

---


> [!TIP]
> 当前位于：**601-650**（第 13/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
