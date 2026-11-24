# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 51. [FastD4RT: Training-Free Acceleration of Dynamic 4D Reconstruction and Tracking](https://arxiv.org/abs/2611.28193)

**<font color=#1a73e8>作者：</font>** Meng Bi, Yili Jin, Kaiyuan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Query-based 4D reconstruction models such as D4RT encode a video once into a global scene representation and obtain outputs by decoding independent point queries. However, inference is often influenced by dense outputs and long videos. Although D4RT separates encoding from decoding, a dense output still requires one decoder query for every pixel of every frame, and a long video is still encoded as many overlapping segments. In this work, we analyze the inference cost of D4RT and show that a large part of it is redundant. In particular, we find that the later decoder blocks attend to a small set of tokens shared by all queries. Based on these findings, we propose FastD4RT, a training-free framework that accelerates D4RT. By exploiting the smoothness of the outputs over time and across pixels, FastD4RT encodes and decodes only at sparse anchors and recovers the remaining outputs via interpolation. It decodes the remaining queries against a shared token set selected once per segment. We further characterize the errors introduced by both components. Experimental results show that FastD4RT accelerates D4RT by about 5 times on average across all its tasks with competitive accuracy, and further improves accuracy on long videos. Our code is available at this https URL.

---


### 52. [torchtsetlin: Fast, Interpretable Tsetlin Machines for PyTorch](https://arxiv.org/abs/2611.28195)

**<font color=#1a73e8>作者：</font>** Vajira Thambawita, Pål Halvorsen, Ole-Christoffer Granmo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Tsetlin machine learns propositional rules with teams of Tsetlin automata that are driven by reward and penalty rather than gradients, so its models are interpretable by construction and cheap to evaluate. Its software, however, consists of C and CUDA kernels behind scikit-learn-style wrappers that sit outside the deep learning ecosystem. torchtsetlin implements the Tsetlin machine family as ordinary PyTorch modules: vanilla and weighted, coalesced, regression, convolutional over sequences, images and volumes, and dense per-pixel segmentation. The automata are a tensor buffer, so a model moves with .to(device), is saved with state_dict() and learns from a mini-batch with one update(x,y) call. Its core technique is a batched formulation of Type I and Type II feedback, in which automaton transitions become event counts realised as binomial draws, with one commit per mini-batch. On ten benchmarks taken from the existing libraries, it matches their accuracy, and on all but the two smallest it trains 2.4-10.9X faster than PyTsetlinMachineCUDA and 10.3-81.2X faster than tmu on the same GPU. The package is pure Python, MIT-licensed and on PyPI; every number in this paper is reproduced by one script. Code: this https URL package: this https URL.

---


### 53. [AutoPILOT: A Visual Agent Harness for Real-Time Gameplay](https://arxiv.org/abs/2611.28202)

**<font color=#1a73e8>作者：</font>** Mark Zhao, Pengcheng Wang, Rui Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal foundation models can play video games well when the game waits for them, but often fail when it keeps running. We find that much of this gap lies in the harness, which decides what the model sees, what it remembers, and how its outputs become actions over time. Existing harnesses such as VISTA improve the first two, yet turn each model call into at most one action, so the agent acts only as often as its model thinks. We introduce AutoPILOT, which changes the third: in each model call, the model can send a primitive action, start an open-loop macro, or write a closed-loop controller that keeps playing from the screen without further model calls until it hands control back. To evaluate agents in real-time games, we build AFK-Bench, 120 diverse browser games grouped by how they respond to inaction and playable in real time or with the clock paused. With GPT-6.1 Sol under the same budgets, AutoPILOT reaches 68.6% real-time success against 38.3% for VISTA, and on GameWorld it keeps 80.0% in real time while VISTA drops from 84.1% to 42.9%. Its gains hold across models, and it reaches VISTA's final success rate at a fifth of its API cost. Our results suggest that how a harness turns model outputs into actions over time is a central yet underexplored part of agent design, and we hope AutoPILOT and AFK-Bench will serve as a foundation for agents in a world that does not wait.

---


### 54. [Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers](https://arxiv.org/abs/2611.28227)

**<font color=#1a73e8>作者：</font>** Benhao Huang, Xuezhe Ma, Hector Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance. However, this feedback breaks speculative decoding, since verifying a drafted token requires the top-layer state from its preceding position, which forces the draft to rely on an approximate stand-in. Training the model to adapt to this stand-in can lower the exact-decoding performance ceiling, while using it at inference time further introduces approximation error. We propose Feedback Shortcut to address both bottlenecks. First, state alignment trains a lightweight projection from multi-token prediction head states to stand-ins, leaving base model training untouched. Second, pipelined correction re-evaluates each draft using its predecessor's newly computed state, a much closer proxy to true feedback. Running this correction inside the verification pass of subsequent drafts improves accuracy with zero extra calls. Across 135M and 780M scales, Feedback Shortcut stays within $10^{-4}$ bits per byte of the exact-decoding ceiling on Paloma and accelerates decoding by 2.4-2.8x with about 2% more training compute than the latent feedback Transformer. At large batch sizes, skipping correction still preserves Transformer speed and over 80% of latent feedback's gains.

---


### 55. [Co-Defining Transparency for Clinical AI: A Replicable Participatory Methodology](https://arxiv.org/abs/2611.28232)

**<font color=#1a73e8>作者：</font>** Mina Bjelogrlic, Inês Espinhal Amaro, Hugues Turbé 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Transparency is the most invoked safeguard for clinical AI, yet frameworks (e.g. the EU AI Act, FUTURE-AI) are specified top-down by regulators and technical experts, not bottom-up by the frontline users whose trust and adoption they should calibrate. This disconnect exacerbates the central deployment failure of clinical AI, miscalibrated reliance and adoption (such as automation bias, deskilling, or disuse), which technical explanation alone does not resolve. We argue that "how much transparency, of what kind, and for whom" is an empirical, context-dependent question, and present a replicable participatory methodology to answer it, instantiated at a large European university hospital. A cumulative chain of six workshops engages an inter-professional panel (clinicians, patient and caregiver partners, students) in agnostic, open-ended elicitation: 274 stakeholder verbatims and external benchmarks (eCH-0272, EU AI Act, Stanford FMTI) yield 20 indicators (18 prioritised and 2 recovered at a later stage), rated across five clinical scenarios of graduated intervention before and after technical briefings, discussed with legal experts, and translated into concrete implementation features. As an existence proof, the use case yields decision-useful signals: human review of automated decisions is the single most critical transparency indicator (84% of participants), and required transparency for adoption rises monotonically with the perceived risk of intervention, corroborating WHO risk-proportionality. A short explainability briefing did not substantially shift participants' transparency requirements. Of 151 evaluated AI transparency solutions, 79 were accepted as-is, covering (at least partially) 17 out of the 20 selected indicators. We position the six-workshop protocol (not its single-site outcomes) as the transferable artefact and release all instruments to support replication.

---


### 56. [Learning the Projection onto the Data Support: Distribution Learning that Avoids Memorization](https://arxiv.org/abs/2611.28234)

**<font color=#1a73e8>作者：</font>** Lin Chen, Dejan Slepčev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a framework for learning distributions supported on manifolds based on estimating the nearest-point projection onto the data support. Specifically, we define an objective functional over a class of functions whose minimizer recovers this projection. The proposed framework automatically adapts to the intrinsic dimension and allows for data supported on unions of manifolds with varying dimensions. The resulting objective can be optimized using standard neural network architectures. We present population-level results establishing recovery of the manifold projection and prove finite-sample Wasserstein generalization bounds. Furthermore, we validate the approach empirically across a range of settings. In contrast to widely used generative models such as diffusion models, whose objectives can be minimized by memorizing training samples, our formulation excludes such behavior. We also introduce a direct memorization metric to verify that the learned projection generates new samples rather than reproducing the training set.

---


### 57. [A Closed-Form Temporal Readout for Surgical Triplet Recognition](https://arxiv.org/abs/2611.28240)

**<font color=#1a73e8>作者：</font>** Lemar Abdi, Amaan Valiuddin, Fida Mohammad Thoker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical triplet recognition requires identifying which instrument performs which action on which anatomical target, and following these interactions as they unfold over time. The task is challenging because several triplets can occur at once, their components span very different durations, and the evidence for an interaction is rarely complete in a single frame. We introduce STRIDE, a post-hoc temporal readout that adds temporal context to any trained recogniser. It averages the recogniser's features and logits over a few fixed temporal windows and combines them with the current frame through ridge regression, solved in closed form on a CPU. Applied as a plug-and-play readout to nine existing methods, STRIDE improves $AP_{IVT}$ in 24 of 27 method-dataset pairs, by up to 7.4 points. Moreover, we propose a simple pipeline consisting of an adapted foundation vision encoder with a linear classifier and STRIDE. Across thirteen encoders, STRIDE improves 37 of 39 encoder-dataset pairs by up to 7.2 points. STRIDE reduces false alarms by 41%, at the cost of a slower response at interaction boundaries. Code will be made publicly available upon acceptance.

---


### 58. [Development of an Effective Federated Learning-Based Defense System Against Phishing Attacks on Mobile Platforms](https://arxiv.org/abs/2611.28245)

**<font color=#1a73e8>作者：</font>** Eren Dogan, Busra Buyuktanir, Gozde Karatas Baydogmus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing remains one of the most pervasive and damaging cyber threats, exploiting both technical flaws and human behavior to compromise sensitive data. We present a privacy-preserving, real-time defense that analyzes full webpage source code on mobile platforms. Our system combines a lightweight Convolutional Neural Network (CNN) for end-to-end feature extraction with a Federated Learning (FL) framework that updates models collaboratively on user devices without transferring raw data-supporting regulatory compliance and personalization. Evaluated on a large and diverse dataset, the model attains 86.02\% accuracy, 90.35\% precision, 80.64\% recall, and 92.78\% ROC-AUC. While some centralized, classical approaches may report higher accuracy, our design emphasizes a practical balance among accuracy, user privacy, and real-time performance on resource-constrained devices. We further demonstrate an end-to-end integration within the open-source Lightning Android browser, achieving real-time detection with low computational overhead. This work shows that privacy-first, AI-driven phishing detection is both feasible and scalable across mobile and IoT settings, delivering robust protection while keeping user data on-device.

---


### 59. [The Cross-Context Threshold Test: Detecting Discrimination Under Environmental Shifts](https://arxiv.org/abs/2611.28259)

**<font color=#1a73e8>作者：</font>** Jun Yuan, Xinyue Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how threshold tests for detecting discrimination under environmental shifts, focusing on the Veil-of-Darkness (VoD) setting where visibility changes between daylight and darkness. We show that standard threshold tests, when applied separately to daylight and darkness data, violate key assumptions: risk distributions drift across contexts and thresholds fluctuate arbitrarily. We propose a cross-context threshold test that enforces distributional invariance and monotonic threshold decay. Using New York City stop-and-frisk data and synthetic experiments, we demonstrate that this model yields more reliable thresholds, improves bias detection, and aligns with the counterfactual logic of the VoD test. Our framework generalizes to fairness auditing whenever environmental context influences decisions.

---


### 60. [FoGConcept: Identifying Interpretable Movement Concepts for Freezing-of-Gait Detection from Multi-Scale IMU Signals](https://arxiv.org/abs/2611.28262)

**<font color=#1a73e8>作者：</font>** Chuntian Chi, John Clapham, GinaMari Blackwell 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Freezing of gait (FoG) is a disabling motor symptom of Parkinson's disease, characterized by an episodic inability to initiate or sustain effective stepping. Current inertial measurement unit (IMU)-based models can detect FoG accurately, but they fail to explain their predictions in terms of human-understandable movement concepts. A major contribution of this work is to identify nine human-understandable movement concepts encoded by a multi-scale FoG model, including gait initiation, rhythmic bilateral gait, trembling in place, shuffling steps, and pivot turns. These concepts recur across subjects, are functionally linked to the model's FoG decisions, and exhibit emergent specialization across short and long temporal contexts. Repeating the concept-discovery procedure on a new FoG dataset, wider temporal contexts, and a deeper backbone recovers the same comparatively stable set of movement concepts. Accordingly, we propose FoGConcept, a mechanism-based interpretability framework for learning movement concepts from multi-scale IMU signals. Domain experts independently recognize 88.9% of the identified concepts, while the proposed model achieves an F1 score of 94.2% for FoG detection. Our findings show that accurate FoG detection can be understood through human-recognizable movement patterns, providing new insight into what a detection model learns to distinguish FoG from non-FoG movement.

---


### 61. [A Nepali-Accented English Evaluation Dataset for Automatic Speech Recognition](https://arxiv.org/abs/2611.28263)

**<font color=#1a73e8>作者：</font>** Santosh Dahal, Kiran Chandra Dahal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems perform strongly on native-English benchmarks, yet their accuracy degrades sharply when the input speech comes from under represented non-native accents. Nepali-accented English is particularly under-served: existing resources either focus on native Nepali speech, cover broader multi-accent settings without dedicated Nepali evaluation, or provide only limited Nepali-accent coverage. This paper presents a Nepali-accented English evaluation dataset designed to support robust ASR benchmarking under accent mismatch. The corpus was collected through a web-based platform that did not collect directly identifying metadata and contains recordings from 57 speakers. Each session follows a fixed 22-prompt protocol consisting of 11 phonetic prompts, 10 domain prompts, and 1 spontaneous prompt, providing complementary coverage of pronunciation, topical vocabulary, and natural speaking style. In addition to transcribed speech, the dataset includes participant metadata for coarse exploratory subgroup analysis and speaker-level manual recording-quality labels. Manual quality assessment shows that 50.9% of sessions are clean and 42.1% contain only mild noise. As a descriptive reference, open-source ASR baselines are substantially worse on this corpus than the corresponding LibriSpeech test-clean values reported in official model cards, reaching 38.15-55.00% WER on the collected set versus reported 2-4% WER on LibriSpeech test-clean. These baseline results position the corpus as a practical held-out resource for evaluating accent robustness and out-of-distribution generalization on Nepali-accented English.

---


### 62. [DeFlowCritic: Dense Latent Reward Alignment for Text-to-Image Flow Matching Models](https://arxiv.org/abs/2611.28265)

**<font color=#1a73e8>作者：</font>** Zeeshan Khan, Xin Yu, Shizhe Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) has emerged as a powerful paradigm for aligning text-to-image flow matching models with complex user intent. However, existing methods typically rely on sparse rewards computed only from final decoded images. This delays credit assignment across the denoising trajectory and makes training computationally expensive. Moreover, simply combining multiple rewards does not reliably produce a Pareto trade-off, where gains in compositional accuracy often degrade aesthetic quality. In this work, we propose DeFlowCritic, an efficient online RL framework based on Dense Latent Reward Alignment. Unlike prior work, our method provides dense supervision on intermediate latents, enabling early-stage guidance for the denoising trajectory. To achieve this, we introduce an internal critic that evaluates noisy latents using features extracted directly from the diffusion model, a representation inherently better suited for latent-space reward estimation than standard image encoders. We construct a high-quality reward-modeling dataset with continuous scores for critic training, capturing compositional correctness on high-quality reference images. The resulting dense reward enables efficient online RL training and inference-time scaling. Experiments show that our method achieves a superior balance between prompt faithfulness and visual quality on GenEval2 and T2I-CompBench++ benchmarks. The approach also generalizes across text-to-image flow matching models, including SD3.5-Medium, SD3.5-Large, and FLUX.1-dev.

---


### 63. [Failure Modes and Data-Efficient Remedies for Transformer-Based Prediction of Viscoplastic Flows](https://arxiv.org/abs/2611.28267)

**<font color=#1a73e8>作者：</font>** Maedeh Saberi, Hugo Franca, Maziyar Jalaal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast and accurate prediction of viscoplastic flows remains a challenge in computational rheology due to yield surfaces, discontinuous gradients, and strongly nonlinear transitions between yielded and unyielded regions. Transformer-based neural operators such as RheOFormer have recently shown strong potential for surrogate modeling of non-Newtonian flows. However, their applicability to viscoplastic systems and their efficacy in recovering realistic flows remain poorly understood. In this work, we present the first systematic investigation of RheOFormer applied to steady Bingham channel flow. By isolating the problem to a simple geometry and constitutive model, we examine how dataset structure, numerical value range, and input representation govern the model's ability to interpolate and extrapolate within the parameter space. The data regimes in which RheOFormer remains accurate and those in which errors emerge are identified, particularly for plug-dominated flows and for conditions outside the velocity scales or flow structures represented during training. Upon identifying these failure modes, targeted enhancements to the input representation and loss formulation are introduced to better predict low-gradient plug regions. Logarithmic velocity representations and gradient-aware loss formulations substantially improve accuracy in challenging regimes where the baseline formulation fails. In addition, extrapolation errors are reduced by augmenting the training set with only a few strategically selected cases spanning the missing physical regimes. Finally, a single partially developed snapshot suffices for an accurate steady-state prediction, and the model outperforms simply copying its input throughout flow development. These results highlight the importance of appropriate field representation and parameter-space coverage for data-efficient neural-operator prediction of viscoplastic flows.

---


### 64. [SONATI: Spatio-temporal ocean neighbourhood asymmetric transformer for imputation of sparse, tabular data with uncertainty](https://arxiv.org/abs/2611.28270)

**<font color=#1a73e8>作者：</font>** Yvonne Jenniges, Boris Peter Koch, Maike Sonnewald 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing value imputation is often a prerequisite for downstream analyses. In oceanography, observational data are frequently structured in a tabular manner, highly sparse and exhibit spatio-temporal structures that classical imputers such as k-nearest neighbours or MissForest are not suited to exploit. We present the Spatio-temporal Ocean Neighbourhood Asymmetric Transformer for Imputation (SONATI), a masked, factorised time-space transformer operating on pre-computed, local time and space neighbourhoods, which reduces computational complexity compared to global attention. SONATI is designed to work with tabular data and is thus in principle able to work on both gridded and unstructured data, though evaluation here was performed on gridded North Atlantic data only. It provides aleatoric and epistemic uncertainties through a negative log-likelihood loss and multiple forward passes with Monte Carlo dropout. Systematic ablations on attention type and masking strategies guided the final architecture design. The results showed that SONATI outperformed classical and transformer-based methods by at least 12.5% in terms of root mean squared error (RMSE) on a large observational oceanographic dataset with key biogeochemical and physical parameters in the North Atlantic (potential temperature, salinity, oxygen, nitrate, silicate and phosphate). Attention type and masking strategy strongly affected imputation accuracy and smoothness of the produced oceanographic fields. Best results were achieved by factorised time-space attention and combined geographic and per-sample masking. The combined masking strategy reduced the imputation error by 14.3% compared to per-sample masking only. Uncertainties were moderately well calibrated (miscalibration area at observed locations $0.074\pm0.012$) and moderately correlated with the imputation error.

---


### 65. [What Do Differentiable Rule Learners Need? FLARE: Fuzzy Rules with Additive Evidence](https://arxiv.org/abs/2611.28272)

**<font color=#1a73e8>作者：</font>** Javier Fumanal-Idocin, Javier Andreu-Perez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rule learners are used where transparency and accountability are required, because they give practitioners patterns they can read. Learning rules is a discrete problem, so neurosymbolic pipelines that use rules as explanations rely on relaxations such as the straight-through estimator. However, these differentiable rule learners often lag behind both classical rule learners and black-box classifiers in terms of performance. We study which parts of a rule-based classifier affect performance, and how well gradient-based training learns each of them. We found that most of the performance comes from how the rules are weighted: random rules with learned weights are already more accurate than every published differentiable rule learner we tested. Based on our results, we propose FLARE (Fuzzy Learned-Antecedent Rule Evidence), a differentiable rule learner that learns simple rules that combine to make the final decision. We also propose a learned encoding for variables with thousands of categories. We test FLARE on tabular data, using 42 datasets of OpenML-CC18 and the 38 classification tasks of TabArena. On CC18, FLARE exceeds the compared rule learners by 7.69 to 12.38 macro-F1 points and performs comparably to random forests, while remaining 1.00 to 1.11 points below tuned gradient-boosted trees. On TabArena it ranks at the same level as random forests and ahead of the other rule learners. As the concept-to-label head of a concept bottleneck model, FLARE is the best rule-based head in five of six settings. On graphs, it is competitive on PubMed and EMOGI but falls behind graph neural networks on Cora and Citeseer. Our code is available at this https URL

---


### 66. [eSPG: The Unreasonable Effectiveness of Event Speckle Plethysmography](https://arxiv.org/abs/2611.28275)

**<font color=#1a73e8>作者：</font>** Aniket Dashpute, Anirudh Bindiganavale Harish, Bhargav Ghanekar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-contact measurement of vital signs such as heart rate (HR) is valuable for patient monitoring and rescue operations. However, existing methods struggle with ambient illumination and motion, and have been demonstrated only at distances of tens of meters. Here we introduce event speckle plethysmography (eSPG), which illuminates a body part with a low-power (0.5-5 mW) laser and captures the resulting dynamic speckle pattern using an event camera. Event cameras, with their high dynamic range, temporal resolution, and sensitivity to intensity changes, are well-suited to capturing rapid speckle fluctuations that encode the physiological signal, even under challenging illumination and imaging conditions. We demonstrate HR estimation at 1 km with a mean absolute error of 5 beats per minute, and 90% of estimates satisfy an AAMI-defined HR estimation criterion. This distance exceeds previous remote plethysmography demonstrations by an order of magnitude and previous speckle plethysmography demonstrations by over three orders of magnitude. We also study and characterize robustness to motion and ambient illumination. Our theoretical analysis and experimental results demonstrate that resolving dynamic speckle fluctuations enables accurate heart rate estimation even at kilometer-scale distances, establishing a new direction toward robust, non-contact physiological monitoring.

---


### 67. [Temporal Logic Tensor Networks: Foundations of Temporal Reasoning in Neural Networks](https://arxiv.org/abs/2611.28277)

**<font color=#1a73e8>作者：</font>** Edjard Mota, Artur d'Avila Garcez, Maria Azevedo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In dynamic scenes---football matches, traffic streams, surgery, or assembly---actions unfold at fundamentally different time scales: in football, a kick happens in milliseconds, a possession lasts seconds, and complex events such as a successful pass followed by a goal combine multiple atomic actions over extended durations. Models trained solely on visual data struggle to learn effectively across different time scales, lacking a principled way of reasoning across fine-grained instants and broader intervals. Neither point-wise nor purely interval semantics suffices: the former fragments events into frame-level snapshots lacking overall event identification; the latter treats intervals as atomic truth-values, ignoring state trajectories. We introduce Temporal Logic Tensor Networks (tLTN), a differentiable neuro-symbolic framework addressing this duality via a formal, multi-sorted logic where events and states are structurally interdependent. Extending Interval Logic Tensor Networks (ILTN), tLTN grounds state predicates as fuzzy truth-value paths over time points, while events are first-class entities with learnable trapezoidal fuzzy durations and differentiable Allen-style relations. A compositional semantics fuses static, event-structural, and state-dynamic satisfaction into a single differentiable LTN grounding. Crucially, the modalities constrain each other bidirectionally: the interval layer dictates where point-wise constraints (e.g., Until, Since) are evaluated, restricting them to event-defined spans; conversely, the point-wise layer validates interval relations, rejecting them if underlying state dynamics contradict the relation. Through controlled synthetic examples, we show when single-modality learning fails and how this localization reduces frame-level computational cost on long traces.

---


### 68. [Scalable Beckmann Maps Improve One-step Generation](https://arxiv.org/abs/2611.28286)

**<font color=#1a73e8>作者：</font>** Ulrik Unneberg, Shiyi Wang, Lee Cheuk-Kit 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Beckmann Transport Models (BTM) learn one-step generative maps end-to-end from data, without a teacher, a distillation stage, or pretrained features. We introduce Scalable Beckmann Maps (SBM), which bring to BTM the two ingredients behind the quality of modern multistep generators: classifier-free guidance (CFG) and a training recipe that scales, while keeping sampling at a single network evaluation. CFG combines conditional and unconditional velocity or score predictions, which a Beckmann map does not have. Our guidance rests on one observation: the BTM current is a positive multiple of an autonomous denoising field, to which CFG applies as it does to a velocity. With exact denoisers this gives guided BTM. In practice we substitute the map's own conditional and null predictions for the denoisers, which requires no additional network and introduces a bias that we characterize. We show that the guided update is consistent with a guided conservation equation, and that guidance can move the boundaries between basins, sending more noise to the modes a condition favors. Trained from scratch in the latent of a representation autoencoder, SBM reaches a one-step FID of 1.6 on ImageNet 256x256 without a teacher or a feature loss, outperforming the Improved-MeanFlow baseline with 3.2x fewer FLOPs. In text-to-image generation it reaches a GenEval score of 0.86 with one network evaluation. As a world model, where we train without guidance, the recipe alone outperforms DriftWorld on all five metrics of two robot-manipulation benchmarks, with 1.9-2.8x less training compute and no pretrained auxiliary feature encoder.

---


### 69. [When Video Verifier Scores Mislead: Capability Assessment and Verifier Selection](https://arxiv.org/abs/2611.28287)

**<font color=#1a73e8>作者：</font>** Charles Weng, Zixi Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video verifiers judge whether a candidate answer or trajectory agrees with a video, and are themselves chosen by a score. We show that this score depends on two choices in the test, the type of negative and the judgment interface, strongly enough to reverse conclusions about what a model can do and which verifier to deploy. We separate the two with controlled constructions that have exact truth conditions: endpoint-matched negatives, wrong only in their internal states, and a truth-switch test, in which the same two candidates swap correctness between two videos. Under direct judgment, where the verdict is read from answer scores, models that reject a visibly wrong start fall to near chance against endpoint-matched negatives. When the frames disclose each event, writing out reasoning before the answer lifts three of four models from under 10% to 70-100% on the truth-switch test, and staged inputs trace the direct failure to one step, composing events into states. But when the event must first be found, on human-validated natural video, the same change brings no significant gain under a protocol common to all models and can lower accuracy if one candidate denies that the event occurs. The negative type also changes which verifier is selected: one chosen on event-denial negatives is 8.9 points less accurate against negatives that keep the event and change a detail, the errors a generator mostly makes, and recovers about half as much accuracy when it reranks that generator's answers. A verifier should be evaluated on the errors it will face, and neither a low direct score nor a gain from reasoning should be read as a property of the model alone.

---


### 70. [Task-Agnostic Incremental Vision-Language Object Detection via Prompt Augmentation and Distribution-Aware Fusion](https://arxiv.org/abs/2611.28291)

**<font color=#1a73e8>作者：</font>** Yonghan Jiang, Zhengyuan Xie, Wenchu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental Vision-Language Object Detection (IVLOD) empowers pre-trained open-vocabulary detectors to continuously learn new visual concepts from sequential tasks without forgetting foundational knowledge. However, existing methods predominantly rely on oracle task identities during inference, severely limiting their open-world practicality. In this paper, we formalize Task-Agnostic IVLOD (TA-IVLOD), a more realistic setting where such priors are unavailable, requiring the model to simultaneously recognize classes from all learned tasks. This unconstrained setting exposes severe performance degradation due to cross-task semantic interference and parameter conflicts. To tackle these challenges, we propose TADA, a novel modular framework. Specifically, TADA introduces Stochastic Prompt Augmentation to mitigate semantic interference via training-time noise injection, and Test-Time Distribution-Aware Fusion to dynamically weight class-specific LoRA experts, effectively resolving parameter conflicts. Extensive evaluations demonstrate that our method significantly outperforms baselines in standard IVLOD and yields substantial improvements in the rigorous TA-IVLOD setting on the ODinW-13 benchmark, while effectively preserving zero-shot generalization on the MS COCO dataset. The code is available at this https URL.

---


### 71. [Benchmarking EEG feature families for ADHD research in children and adolescents: performance and explainability across attention tasks](https://arxiv.org/abs/2611.28299)

**<font color=#1a73e8>作者：</font>** Javier Sanchis, Jorge García-Carrasco, Álvaro Navarro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention Deficit Hyperactivity Disorder varies in presentation. Diagnosis requires clinical and developmental assessment. Reproducible electroencephalography measures may complement clinical and behavioural characterisation, but differing feature definitions and evaluation methods hinder comparison. We compared seven feature families and four combinations across attention tasks and assessed the stability of held-out explanations. Two serious games yielded four overlapping attention-task cohorts of 123-140 participants each. Repeated nested participant-held-out evaluation assessed recruitment-group discrimination. Exploratory paired participant-cluster bootstrap tests corrected for multiplicity in two separate families: 72 individual-task contrasts and 18 fusion contrasts. For eight configurations selected after inspecting predictive results, we explained held-out native probabilities before calibration. In the strongest task context, the highest configuration mean AUROC over three repetitions was 0.773, with a fixed-prediction 95% interval of 0.692-0.854 unadjusted for selecting the maximum. Precision, sensitivity and specificity were 0.740, 0.556 and 0.861. In that task, the paired AUROC difference for connectivity minus spectral features averaged +0.2083 across six classifiers and the common 8 s and 16 s durations, with pointwise 95% CI 0.1076-0.3072 and adjusted p = 0.0036. F4-AF4 beta-band coherence led repetition-level attribution summaries in five selected procedures and was selected in every fit. Other contexts showed weaker discrimination and less consistent retention of leading scientific inputs. No general classifier winner emerged. Connectivity and its recurring coherence input warrant independent replication, but do not justify a universal feature recommendation. These exploratory findings do not establish causal task effects, disease mechanisms or diagnostic validity.

---


### 72. [Cross-Boundary Vulnerability Management for SDVs: A Traceability Architecture at the ISO/SAE 21434 and EU Cyber Resilience Act Interface](https://arxiv.org/abs/2611.28303)

**<font color=#1a73e8>作者：</font>** Krishna Teja Medam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A software-defined vehicle depends on products that sit under different EU regimes. The type-approved vehicle and the systems, components and separate technical units made for it fall under Regulation (EU) 2019/2144, which makes UN R155 mandatory; Regulation (EU) 2018/858 does so for R156; and ISO/SAE 21434 supports the management system R155 requires. Chargers, companion apps, aftermarket devices and many backends may fall under the Cyber Resilience Act (CRA) instead, whose reporting duty in Article 14 has applied since 11 September 2026. Neither side defines how a vulnerability found on one reaches the other's risk process. We contribute a four-question classification procedure, a five-regime traceability matrix, a reference architecture with four handoff paths and three boundary findings. On 75 classified products from a frozen public-source corpus, the procedure yields 47 Periphery, 11 Core, 1 Other and 16 Boundary products, three of them outside both the CRA and compulsory R155. Because UN R10 lets an electronic sub-assembly be approved as a component, the texts leave a second reading open, and we report both counts. Under it, 22 aftermarket devices become components, Periphery falls to 25 and 25 products sit outside both regimes. Seven retrospective walkthroughs suggest that, for third-party products, vulnerability information stops in the vehicle manufacturer's own inventory, triggers or exploitation assessment, and that no provision obliges a product maker to tell a vehicle manufacturer: the only defined two-way route is a contract. No reviewed source establishes a case that reached an Article 14 clock.

---


### 73. [Quantity-Level FDIA in SDR-Based P2P Energy Trading: Cyber-Economic Impact and Pre-Clearing Detection](https://arxiv.org/abs/2611.28317)

**<font color=#1a73e8>作者：</font>** Wassim Sarrieddine, Razane Tajeddine  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper investigates the cyber-economic impact and pre-clearing detectability of false data injection attacks (FDIAs) in peer-to-peer (P2P) energy trading among interconnected microgrids. In the proposed cyber-economic framework, load and photovoltaic profiles drive a sequential 15-minute market with deterministic double-sided proportional (pro-rata) allocation and supply-to-demand-ratio (SDR) pricing, while true physical injections are separated from communicated market quantities. The framework is evaluated through a multi-microgrid case study over 69,904 market-aligned states, for which all AC power-flow solutions converged and voltages remained within 0.98999-1.04369 per unit. Healthy local exchange reached 1,159.66 MWh and generated USD 92,772.62 of community benefit. Bias, scaling, and ramp attacks modify only one microgrid's communicated quantity, altering the settlement price, P2P allocation, scheduled residual-grid exchange, participant financial outcomes, and benefit fairness, while true feeder injections remain unchanged. Role-specific random forest, statistical threshold, and score-fusion detectors are compared using only information available before clearing. Pooled sample-level detection rates range from 7.82% to 12.14%, with false-alarm rates from 4.69% to 7.70% and role dependence. In the investigated case study, measurable downstream economic distortion and low pre-clearing detectability coexist under bounded quantity manipulation.

---


### 74. [Click and Count: Multimodal Prototype Adaptation for Class-Agnostic Object Counting](https://arxiv.org/abs/2611.28321)

**<font color=#1a73e8>作者：</font>** Amani Aifi, Wassim Bouachir, Ahmed Zgaren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a multimodal, class-agnostic, density-based object counting framework that specifies the object of interest through visual exemplars, a text description, or both, within a single iterative refinement pipeline. Existing counters typically fall into two groups: methods that fuse two modalities, a hand-drawn bounding box and a text description, to specify the target object, and single-modality methods that rely on either a box exemplar or text alone. A few recent methods replace the box with a point or click. We expand a single click into a precise object mask via a frozen visual-prompt segmentation model, feeding an iterative prototype-refinement process that also fuses a text description at every refinement step. We make two contributions: first, a click-derived exemplar extraction module that removes the bounding-box requirement of prior exemplar-based counters; second, a per-step text-fusion mechanism that combines visual and textual prompts throughout refinement. Combined with text guidance, our model achieves state-of-the-art counting accuracy, outperforming prior click-based counting methods across all metrics and surpassing the box-exemplar base architecture in mean absolute error. The code is available at this http URL.

---


### 75. [AV-FLARE: Feature-Level Reliability Estimation for Multimodal Emotion Recognition](https://arxiv.org/abs/2611.28327)

**<font color=#1a73e8>作者：</font>** Ines Jemmali, Alaa Nfissi, Wassim Bouachir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition (MMER) systems typically rely on learned feature representations and attention mechanisms that implicitly weight information across time and modalities. However, these mechanisms do not explicitly incorporate input reliability, despite the presence of noise in audio, occlusions in visual data, and the sparse and event-driven nature of affective cues. We propose AV-FLARE, a framework that explicitly estimates fine-grained reliability scores across both temporal and feature dimensions prior to temporal modeling and uses them to modulate feature representations. Reliability is computed using two complementary components: (i) a supervised network trained jointly with the classification objective, and (ii) an unsupervised Gaussian Mixture Model that models global feature distributions. These signals are combined to provide both task-driven and distribution-aware reliability estimates. To integrate modalities, we introduce a hierarchical cross-modal attention mechanism in which textual features are used to guide audio-visual fusion as a semantic reference modality. Experiments on the IEMOCAP dataset show that AV-FLARE improves over a no-reliability baseline, achieving 90.81\% accuracy and 81.69\% F1-score, corresponding to gains of +4.41% and +8.56%, respectively. These results suggest that incorporating explicit input reliability estimation may improve robustness in multimodal emotion recognition under the evaluated setting.

---


### 76. [TabK: Amortized Bayesian Estimation of the Number of Clusters in Tabular Data](https://arxiv.org/abs/2611.28335)

**<font color=#1a73e8>作者：</font>** Mohammadreza Bakhtyari, Bogdan Mazoure, Renato Cordeiro de Amorim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the number of clusters, $k$, is a fundamental prerequisite for most clustering algorithms. Traditionally, this estimation has relied on computationally expensive grid searches over internal cluster validity indices (CVIs) or adaptive clustering algorithms, both constrained by specific statistical assumptions. We introduce TabK, a zero-shot, permutation-invariant transformer architecture that frames the estimation of $k$ as an amortized Bayesian inference problem for tabular data. TabK leverages a novel Quantile Feature Encoder (QFE) to extract position-free, content-derived representations from empirical marginal distributions. By learning a generalized structural bias over a diverse synthetic prior, TabK estimates the number of clusters in a single forward pass per ensemble member. Evaluated across 50 diverse real-world benchmarks, TabK outperforms all competing methods, achieving a mean absolute error (MAE) value of 1.04 compared to 2.14 for the closest competitor. TabK also achieves the lowest average inference time, producing estimates in less than one second on average and running $2\times$ faster than TabClustPFN and $30\times$ faster than traditional CVIs such as Silhouette and Calinski-Harabasz. Code is available at this https URL.

---


### 77. [Which Loans, Not How Many: Exactly Level-Invariant, Anytime-Valid Monitoring of Deployed Risk Models](https://arxiv.org/abs/2611.28342)

**<font color=#1a73e8>作者：</font>** Xin Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A refinancing wave can change the number of mortgage prepayments without changing the relationship between scores and prepayment. In a logistic model, conditioning on the monthly count removes the intercept from the likelihood of which loans prepay. Our fixed-start slope product tests a lower bound on the calibration slope. At threshold 20 its probability of ever crossing under the null is at most 5%. The restarted level sum tracks departures from intercept tolerance. A confidence sequence estimates a constant slope, and the restart-intersection rule detects changes in that slope. A continuous mixture avoids the off-grid width floor of a discrete prior. On Freddie Mac loans, fixed-slope resampling reproduces 78% of maintained-model monthly AUC variance in development and 70% in the holdout (95% intervals 57-100% and 48-100%). From fresh holdout starts, the restarted level sum crosses on both paths, and the fixed-start slope product stays below threshold on both. The restart-intersection rule signals a downward change for the frozen model in April 2018 and an upward change for the maintained model in a supplementary run in August 2019.

---


### 78. [Enabling Verifiable Output Lineage for Virtualized ML Workload Execution](https://arxiv.org/abs/2611.28344)

**<font color=#1a73e8>作者：</font>** Prach Chantasantitam, Adam Caulfield, Sujaya Maiyya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) property attestation lets a model provider demonstrate properties of their models and datasets to verifiers, and trusted execution environments (TEEs) have emerged as its most practical mechanism. However, existing TEE-based systems attest only a static snapshot of the TEE's initial configuration, leaving run-time behavior unauditable. Proof of execution (PoX) architectures close this gap by requiring the prover's root of trust to also demonstrate that (1) the attested operation actually executed and (2) the claimed outputs were affected only by that operation. Existing PoX designs, though, target microcontrollers and rely on hardware features unavailable in server-grade TEEs, so they cannot be applied directly to ML workloads.
We present EVOLVE, a software-based PoX framework for server-grade TEEs. EVOLVE mediates an operation's writes and control flow to track whether a requested ML operation executes without violation. It binds the execution status to measurements of the operation's inputs and outputs, enabling verifiers to assess run-time behavior through ML property attestation. We implement EVOLVE on Intel TDX as a Rust module within its virtual firmware, with policy checks built on primitives formally verified in F*. Our evaluation shows that EVOLVE is versatile across diverse ML applications on unmodified hardware, provides formal guarantees for its policy checks. EVOLVE incurs per-request run-time overhead on average ranging from 1.07$\times$ (for decision trees) to 2.13$\times$ (for multi-layer perceptrons).

---


### 79. [Toward Adversarially Robust World Models](https://arxiv.org/abs/2611.28345)

**<font color=#1a73e8>作者：</font>** Ethan Rathbun, Jonathan Nöther, Christopher Amato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent dynamic world models have proven to be highly versatile tools for embodied artificial intelligence systems, enabling online action planning, safe policy evaluation, and scalable policy learning. However, this versatility makes world models a vulnerable and centralized point of failure as a compromised model can impact planning, evaluation, and training at once. Therefore it is critical that the security and robustness properties of world models are properly understood before they are universally deployed in embodied AI systems. In this work we take a unifying approach towards this understanding, developing two novel attacks against world models, named state hallucination and dynamic shift attacks, aimed directly at impacting downstream systems, and proposing a new theoretical lens through which to study the robustness of latent dynamic world models. Through our analysis we identify robust latent space encoders as the key component of robust world models. We empirically validate this finding on four separate latent dynamic world model families, studying Dino World Model, Le World Model, r2Dreamer, and Cosmos 3, demonstrating significant improvements in robustness through adversarial encoder model training.

---


### 80. [Two Actions from One State: Fork Futures Teach JEPA World Models to Compare](https://arxiv.org/abs/2611.28350)

**<font color=#1a73e8>作者：</font>** Yihao Wu, Runjia Zeng, Tongyan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> JEPA world models are trained to predict logged transitions but used to compare counterfactual actions from one state. The logged behavior data show one action per state, and under a local linear approximation we prove the action response is unidentified along any direction the policy never varies within a state. We therefore supplement behavior data with measured outcomes of alternative actions from the same state. Our fork futures execute two actions from one restored state, and their outcome difference cancels the state term, identifying the action response on the sampled span. The resulting model, Fork-JEPA, matches predicted to measured differences, anchors the logged successor with behavior prediction, and adds a lookback head that keeps the predecessor recoverable, all at training time, leaving planning unchanged. On three visual control tasks, behavior-only training leaves the predicted action effect no better than a constant guess. Fork-JEPA makes it readable and raises planning success by up to 14\% over LeWM, its base model. Where the action response changes across hidden zones, it nearly doubles cross-zone success, and 1,024 fork pairs beat 1.2M extra behavior steps. Our project is available at this https URL.

---


### 81. [Coupling-Aware Reinforcement Learning for Co-Evolving Graph Games](https://arxiv.org/abs/2611.28351)

**<font color=#1a73e8>作者：</font>** Mina Kim, Guanghui Lan, Benoit Montreuil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building hydrogen station networks, electric vehicle charging grids, or vaccine distribution systems requires coordinating two separately operated graphs, demand-side facilities and the supply-side networks they depend on, where each operator's payoff depends on the other's choices. We formalize this as the Co-Evolving Graph Game (CEGG), a setting that sits between facility location, interdependent-network analysis, and graph-based multi-agent reinforcement learning (MARL) but is not jointly addressed by any of them. We propose Cross-Graph Attention with Policy Mirror Descent (CGA-PMD), pairing cross-graph attention, which lets each agent read only the partner-graph nodes structurally coupled to its own, with a policy mirror descent update for stable training. Across three reward domains and a range of practical network scales, we find that the structure of the coupling selects which method wins: at small scale most methods are competitive, but as scale grows or coupling becomes irregular, CGA-PMD is the one method that stays reliable: it attains the highest success count on each of five real city networks, while own-only, unmasked-attention, and Proximal Policy Optimization (PPO)-based variants degrade in distinct ways. Our theoretical analysis addresses the optimizer side: the Kullback-Leibler (KL)-regularized update admits an iteration-uniform cumulative drift bound, whereas the clip update admits no such bound on the iterations where the clip does not bind. The implementation is available at this https URL.

---


### 82. [Understanding Membership Inference Attacks on EEG Models](https://arxiv.org/abs/2611.28354)

**<font color=#1a73e8>作者：</font>** Mehrdad Khodapanahandeh, Selin Unal, Berkay Kemal Balioglu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) signals contain sensitive, subject-specific information, making models trained on them potential targets for membership inference attacks (MIAs). Although MIAs have been studied extensively in other domains, their applications to EEG models are relatively scarce, and the factors driving the vulnerability of EEG models to MIAs are not adequately understood. In this paper, we present a systematic empirical analysis of MIAs on EEG models using three datasets, seven model architectures, four attack methods, and two metrics. Results show that poor model generalization (large train-test loss and accuracy gap) is the strongest indicator of MIA vulnerability. Longer training and larger models also increase vulnerability. Moreover, no particular scalp region, frequency band, inter-channel correlation pattern, or temporal versus spectral representation of EEG data consistently explains MIA vulnerability across datasets. Finally, subject identification and leave-one-subject-out experiments indicate that models relying more heavily on subject-specific representations are more vulnerable to MIAs. Overall, our findings identify the key drivers of membership leakage in EEG models and can provide guidance for developing MIA-resilient EEG systems.

---


### 83. [Cross-Site Transformers Are Robust Heart Rate Estimators](https://arxiv.org/abs/2611.28366)

**<font color=#1a73e8>作者：</font>** Mason Kadem, Rong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-site heart-rate estimation from photoplethysmography (PPG) degrades sharply under real-world motion. Multi-site PPG provides a natural solution, but existing models fuse sites as generic sensor channels rather than exploiting their hemodynamic structure: each heartbeat propagates along the arterial tree, appearing across body sites as delayed and transformed copies of the same cardiac event. We propose the Cross-Site Transformer, which introduces a hemodynamically informed inductive bias by restricting multi-sensor fusion to cross-attention between PPG sites. On WildPPG, the largest in-the-wild benchmark available, our model establishes a new single-model state of the art, reducing error by 21% over the previous best and 35% over the best prior transformer. The same cross-site restriction makes the trained network directly auditable. Because each cross-attention head lies on one directed pathway between sites, causal resample ablation can isolate and test each direction of information flow. Ablating the chest-to-wrist pathway doubles error, whereas the reverse costs far less. Encoding hemodynamic structure into attention routing thus improves real-world sensing robustness and enables rigorous auditing of multi-sensor fusion.

---


### 84. [Taking the PULSE of Enterprise Workflows: Evaluating Persistent Project-State Understanding](https://arxiv.org/abs/2611.28374)

**<font color=#1a73e8>作者：</font>** Jiexin Ding, Lin Ai, Adam Davies 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise agents must maintain an up-to-date understanding of work distributed across heterogeneous artifacts, evolving over time, and unevenly visible to different collaborators. We formulate this challenge as persistent project-state understanding (PPSU) and introduce PULSE, a benchmark of 1,573 questions over 30 enterprise project histories. PULSE constructs deterministic, time-indexed project state and documented collaborator views from source-linked records, and evaluates three families of questions: open loops, project evolution, and view gaps. Across retrieval agents, graph- and memory-augmented retrieval, long-context, and oracle conditions, we find substantial headroom for current systems. Retrieval and extraction account for the largest share of the gap, but providing explicit project state on top of gold evidence yields further substantial gains, showing that PPSU cannot be reduced to retrieval alone. Further analysis shows that questions requiring information to be reconciled across multiple parts of the project history remain difficult even when the relevant evidence is provided, while project-state synthesis and perspective conditioning remain persistent challenges. These results motivate enterprise agents that explicitly maintain and reconcile temporally grounded state across sources, actors, and time.

---


### 85. [Data-Dependent Probability Estimation via Sample Amplification](https://arxiv.org/abs/2611.28399)

**<font color=#1a73e8>作者：</font>** Vitaly Feldman, Satyen Kale, Mahbod Majid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can we estimate the probability of an event chosen after seeing the data, without using any fresh samples? Its empirical probability can be arbitrarily misleading, while learning the entire distribution to constant accuracy requires $\Theta(d)$ samples on a domain of size $d$. We show that $\widetilde{O}(\sqrt{d})$ samples suffice for constant mean squared error, provided the rule choosing the event is known. More generally, our estimator handles arbitrary $[0,1]$-valued queries and runs in polynomial time given evaluation access to the rule. This sample complexity matches the known lower bound up to logarithmic factors and resolves the open question posed by Feldman, Kale, Raman, Talwar, and Tewari (arXiv:2610.41244).
Our estimation framework relies on a new combination of sample amplification (arXiv:1904.12053 and arXiv:2201.04315) with distribution learning via online optimization. Our estimator achieves mean squared error $O(d^{3/4}/n)$ when $d\leq n$ and $\widetilde{O}(d^{1/4}/\sqrt{n})$ when $d>n$. We complement this with a lower bound of $\Omega(\min\{1,\sqrt{d}/n\})$ on the mean squared error. Using our framework, we also design an efficient estimator for data-dependent queries on Gaussian distributions with unknown mean and identity covariance. Finally, we show that a smoothed variant of the problem is much (exponentially) easier. For discrete distributions, if the sample size is chosen uniformly from $\{n,\ldots,2n-1\}$, then $n=O(\log d)$ suffices for constant mean squared error.

---


### 86. [WingBench: Benchmarking How AI Agents Search for Better Designs](https://arxiv.org/abs/2611.28418)

**<font color=#1a73e8>作者：</font>** Yiming Yang, David Xia, Jisen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Design search often uses cheap learned predictions to choose which candidates deserve expensive tests, but these tests can fail, especially on the unusual designs that optimization favors. We introduce WingBench, a multifidelity benchmark in which optimizers and AI agents design transonic wings with computational fluid dynamics (CFD) inside the search. They can query a learned aerodynamic surrogate and spend a fixed budget of sequential CFD evaluations, each returning a score or a failure type. WingBench grades the design each method recommends, reporting separately whether it receives a valid score and how good that score is. Using WingBench, we contribute a study of five baseline optimizers and a comparison of three AI agent methods, which produced 6,629 CFD evaluation records. Feedback helps baseline optimizers deliver valid designs when it changes their later proposals, but the differential-evolution variant does so with lower aerodynamic quality. An open-ended research agent finds designs of similar quality to the strongest baselines over 32 CFD queries, with different prior information and unmatched total computation. In early search, our reflection and planning implementations do not consistently improve on it. We release the data, code, agent prompts, and analysis scripts for reproducibility.

---


### 87. [Center-Aware Ordinal Learning for Prostate Cancer Grading from Histopathology Images](https://arxiv.org/abs/2611.28419)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Abootorabi, Parvin Mousavi, Purang Abolmaesumi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prostate cancer grading from histopathology whole-slide images (WSIs) is complicated by the ordered nature of ISUP grades, class imbalance, and center-dependent variations in staining, tissue preparation, and scanning. Most weakly supervised methods treat grade groups as independent categories and may therefore learn representations that do not transfer reliably across institutions. We propose a center-aware ordinal learning framework that combines a pretrained pathology encoder with attention-based multiple instance learning. The framework uses an Earth Mover's Distance loss to account for ordinal errors, an ordinal supervised contrastive objective to align same-grade slides across centers while separating grades according to disease severity, and curriculum learning to reduce the dominance of benign cases. We evaluate the framework on approximately 9,100 biopsy WSIs from the two-center PANDA dataset. The proposed framework achieves an accuracy of 0.842 and a quadratic weighted kappa of 0.958 on the held-out test set. Its main benefit is observed in cross-center transfer: when a linear probe is trained on Karolinska representations and evaluated on Radboud, accuracy increases from 0.643 to 0.823 and quadratic weighted kappa from 0.899 to 0.930. Performance remains stable in the reverse direction. UMAP projections further show improved mixing between centers while preserving an ordinal grade trajectory. These results suggest that combining ordinal and center-aware objectives produces more transferable slide representations for multi-center prostate cancer grading.

---


### 88. [Lean Census: A Distributional Analysis of AI-Generated Lean Code](https://arxiv.org/abs/2611.28430)

**<font color=#1a73e8>作者：</font>** Justin Asher, Pietro Pellegrino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We compare two human-written and four AI-generated Lean libraries with Mathlib through the distributions of simple statistics of their code. For each library we measure inline claims in proofs, proof length, how often each declaration is used, and design choices such as instances and private declarations, and we read each against the variation among Mathlib's own areas. The AI-generated libraries have more inline claims per theorem, longer proofs, fewer instances, and more private declarations than the human-written ones. We release the code for the analysis as a package, lean-census, at this https URL.

---


### 89. [PFN-Syn: Generating Synthetic Tabular Data with Prior-Data Fitted Networks](https://arxiv.org/abs/2611.28440)

**<font color=#1a73e8>作者：</font>** Michael Zuo, Inwon Kang, Oshani Seneviratne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic tabular data can help enable data sharing and model development in privacy-sensitive domains, but existing generators often require dataset-specific training and substantial computation. We introduce PFN-Syn, a training-free framework for synthetic tabular data generation based on prior-data fitted networks. We evaluate PFN-Syn against training-based generators on eight binary classification datasets. PFN-Syn achieves the highest average downstream utility among evaluated synthetic generators, with higher generation throughput than training-based baselines, while maintaining competitive distributional similarity and distance-to-closest-record privacy behavior. Our results suggest that tabular foundation models can serve as useful building blocks for practical synthetic tabular data generation.

---


### 90. [Decoding Frozen Vision Representations for Training-Free Few-Shot Pineapple Detection](https://arxiv.org/abs/2611.28442)

**<font color=#1a73e8>作者：</font>** Manfred Gonzalez-Hernandez, Danny Xie-Li, Fabian Fallas-Moya 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot object detection in agricultural imagery is hampered by dense vegetation, repeated patterns, and scarce annotations. We present a training-free detector that turns dense features from frozen visual foundation models directly into detections, without fine-tuning, a learned head, or external proposals: a whitened foreground-background direction estimated from annotated support images scores every query patch, and the score field is decoded with an adaptive threshold and support-derived geometry. We also test whether predicted relative depth can be fed directly to RGB-pretrained frozen encoders. On aerial pineapple imagery, the detector outperforms PET-DINO and GeCo2 at every evaluated support size; at K=40, predicted depth alone reaches 92% of the RGB performance with DINOv2, and RGB-depth fusion lowers counting error for both encoders. We release the Pineapple Plantation dataset (4,908 aerial frames, 1,995 annotated with 17,609 boxes, predicted depth, leakage-aware splits) and analyse transfer to two further agricultural datasets.

---


### 91. [Optimal User-Level Private Stochastic Convex Optimization and Mean Estimation with Heavy Tails](https://arxiv.org/abs/2611.28460)

**<font color=#1a73e8>作者：</font>** Andrew Lowy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic convex optimization with heavy-tailed stochastic gradients under $(\varepsilon, \delta)$-user-level differential privacy, which protects each user's entire collection of samples. Instead of assuming a uniformly bounded Lipschitz constant, we only assume bounds on the second- and $k$-th moments of the random sample Lipschitz parameters. This allows for unbounded, heavy-tailed stochastic gradient distributions and can lead to sharper excess risk bounds. We characterize the minimax optimal excess population risk up to logarithmic factors. Our algorithm achieves the optimal rate with only $\widetilde{O}(1/\varepsilon)$ users. As a byproduct of our algorithmic developments, we obtain tight bounds for user-level private mean estimation under norm-moment assumptions, improving over the guarantees of Esfandiari et al. (2022) and Zhao et al. (2024). Finally, for mean estimation under the directional-moment assumption of Agarwal et al. (2025), we close their remaining approximate-DP gap by removing the additional $d/\varepsilon$ user requirement and attaining the optimal sample complexity up to logarithmic factors.

---


### 92. [HiPPO Functional Memory: Coordinate-Queryable Attention for Irregular Time Series](https://arxiv.org/abs/2611.28465)

**<font color=#1a73e8>作者：</font>** Zhaodong Guo, Haoyun Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular time series are recorded at nonuniform times and are often queried at other times: between observations, after the last one, or on a regular grid. Continuous-time models answer such queries by integrating latent dynamics, and time-aware attention models answer them by revisiting the observation tokens. We introduce HiPPO Functional Memory (HiPPO-FM), an attention operator that writes an irregular history into a rank-M function space with explicit time coordinates. Masked self-attention first exchanges content among the observations; the updated values are then contracted against kernel-smoothed HiPPO-Legendre features and solved through a regularized Gram matrix, so the retained coefficients define a function that is read at any time through the same features. The write and read have the form of an interdomain sparse Gaussian-process mean: every readout lies in an M-dimensional reproducing-kernel subspace, and a pointwise bound separates the approximation error of this subspace from the error of the learned memory. Removing the functional memory from the encoder raises Spiral reconstruction RMSE 18-fold. The full model has the lowest error in 11 of 12 Spiral settings, the highest overall accuracy and best average rank on 20 irregular UEA datasets, the highest event-type accuracy on all five multi-type event benchmarks, and a 21% lower extrapolation MSE than CRU on PhysioNet. Because the memory has fixed rank, the state retained after encoding keeps a fixed size as the history grows and is 102 times smaller than a token cache at 1,024 observations.

---


### 93. [VICA: Video Contextual Agreement for AIGC Video Detection and Localization](https://arxiv.org/abs/2611.28485)

**<font color=#1a73e8>作者：</font>** Runheng Lin, Jialiang Shen, Jiyang Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of AI-generated content (AIGC) video generation and editing technologies has raised growing societal concerns about the authenticity and reliability of digital videos. Existing video detection methods primarily exploit temporal inconsistencies through holistic frame-level representations, whereas manipulation localization methods focus on artifacts within individual spatial regions. However, holistic representations may obscure localized artifacts through global feature aggregation, while region-centric approaches may overlook disagreements between individual regions and their surrounding spatiotemporal context. To address these limitations, we propose VIdeo Contextual Agreement (VICA), a unified framework that masks individual video regions and leverages a frozen V-JEPA model to predict their representations from the surrounding spatiotemporal context. Complementary masking ensures complete regional coverage, while context-conditioned predictions establish references for assessing regional agreement with the broader video context. By comparing predicted and observed representations, VICA derives spatial residuals that characterize intra-frame discrepancies and bidirectional temporal residuals that capture inconsistencies across preceding and subsequent frames. These residuals characterize contextual disagreements, providing a shared forensic representation for both tasks and shifting the focus from identifying isolated manipulation artifacts to assessing regional agreement with expectations inferred from the broader video context. Extensive experiments demonstrate that VICA achieves state-of-the-art performance on both tasks across multiple benchmarks, with strong generalization to unseen video generators and editing methods.

---


### 94. [AMP-OD: Active Model Probing for Unsupervised Outlier Model Selection--Extended Version](https://arxiv.org/abs/2611.28488)

**<font color=#1a73e8>作者：</font>** Hong-Phuc Phan, Tuan-Anh Vu, Tung Kieu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outlier detection is often deployed in fully unsupervised settings, where labels are unavailable and practitioners must choose a detector without direct performance feedback. Existing unsupervised outlier model selection methods predict detector quality from static meta-features and historical performance on meta-datasets, but they commit before observing how any detector behaves on the target dataset. We propose AMP-OD, an execution-conditioned probe-then-commit framework. AMP-OD runs a small number of inexpensive probe detectors, uses their score patterns as target-dataset evidence, and then selects a final detector from a larger candidate pool. To interpret unlabeled probe responses, we introduce a Leave-One-Out Family Probe Posterior (LOO-FPP), which converts probe score patterns into gated detector-family evidence while reducing self-validation in pseudo-label construction. AMP-OD further combines this evidence with historical reliability through a warm-start prior, a sequential probe/stop policy, and lower-confidence-bound arbitration. Extensive experiments and ablation studies show that detector responses provide useful evidence beyond static meta-features, with the LOO-FPP and conservative arbitration as key contributors.

---


### 95. [SoK: Splitting the Trigger or Adding Attackers? Disentangling Distributed Backdoor Attacks in Federated Learning](https://arxiv.org/abs/2611.28491)

**<font color=#1a73e8>作者：</font>** Zhuotao Lian, Qingkui Zeng, Weiyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed backdoor attacks split a trigger among several federated learning clients, so that the backdoor appears only in the aggregated model. Since DBA, a line of work has reported that such attacks are stronger, more persistent, and stealthier than a single attacker with the full trigger. We systematize this literature and test this belief. We code nineteen primary studies and fifteen papers that evaluate against DBA. The reported advantage is rarely measured against a complete trigger delivered by the same attackers, and none of the fifteen evaluations tests whether individual pieces remain effective. We then run 875 paired federated runs that separate adding attackers from splitting the trigger. In our image experiments, adding attackers raised attack success in every seed of all 30 cells where we measured it, by 7.5 to 83.4 percentage points on average. Splitting the trigger among the same attackers had a smaller effect, and its sign depended on the piece layout, the allocation, and the attackers' local training. With DBA's compact layout, splitting lowered attack success on CIFAR-10. A larger penalty on small CNNs vanished once the attackers trained longer, and an FCBA-style allocation gained a few points. Widely separated pieces helped on CIFAR-10, its grayscale version, and GTSRB. No model required all pieces. Neural Cleanse suppressed single pieces together with the full trigger, but split backdoors with separated pieces survived it better than complete ones. We derive reporting requirements for attack and defense evaluations.

---


### 96. [Simple Baselines for Fetal Brain Unsupervised Anomaly Detection](https://arxiv.org/abs/2611.28505)

**<font color=#1a73e8>作者：</font>** Hongjia Yang, Mingxuan Liu, Yingqi Hao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised anomaly detection (UAD) offers a promising approach to fetal brain magnetic resonance imaging (MRI) analysis, where pathological data are scarce. Existing methods rely mainly on brain age prediction or image reconstruction, but are limited by noisy gestational age (GA) labels, lack of lesion localization, or poor cross-domain generalization. We propose FetalBUAD, a UAD framework based on voxel-level brain age estimation. A joint multi-task network predicts global brain age, voxel-level brain age maps, and brain segmentation to establish an internal biological brain age reference, reducing reliance on clinically recorded GA. Uncertainty-aware voxel-level brain age gap maps are then used for anomaly localization. Experiments on 1,317 internal fetal brain MRI volumes and an external benchmark demonstrate state-of-the-art anomaly detection performance and improved cross-domain generalization. FetalBUAD also generates anatomically interpretable maps that localize diverse fetal brain abnormalities. Our code is publicly available at: this https URL.

---


### 97. [State of Mind: Learning and Evaluating World Models of Naturalistic Brain Dynamics](https://arxiv.org/abs/2611.28508)

**<font color=#1a73e8>作者：</font>** Yuxiang Wei, Zundong Wu, Weiyu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding naturalistic brain activity requires going beyond the stimulus alone, as external inputs continuously interact with an individual's evolving brain state. A world model captures such dynamics in a latent state by inferring it from neural observations, predicting stimulus-driven evolution, and updating with new observations. However, existing brain world models fail to maintain a persistent latent state over time, and standard metrics of neural prediction accuracy cannot tell whether a model tracks an individual's brain state or relies solely on the stimulus. To directly test state inference, prediction, and updating, we introduce BrainStateBench, which evaluates a model's latent state through a frozen linear probe on whole-cortex, movie-driven fMRI. Its State task tests whether a model captures trial-to-trial variability in an individual's responses to repeated stimuli, while Forecast and Updating evaluate future activity predictions without and with new observations, respectively. To track individual brain state across time, we propose Spectator, a linear latent world model trained with a joint-embedding predictive objective. Spectator encodes short- and long-horizon observation histories into a two-timescale latent state and predicts state transitions linearly from the current state and stimulus. Stimulus-only encoders reach 0.320 in fMRI prediction correlation without observing the brain (0% on State), while prior deep brain world models reach 0.239 yet score at most 0.4% on State. In contrast, Spectator achieves 0.349 correlation alongside 5.5% on State, 16.0% on Forecast, and 20.3% on Updating, outperforming all baselines while forecasting over 20x faster than deep forecasting models.

---


### 98. [Digital Twins for Multi-Agent Systems: When to Trust, What to Change](https://arxiv.org/abs/2611.28517)

**<font color=#1a73e8>作者：</font>** Truc Nguyen Thi Le, Phuoc Nguyen T. H  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Digital twins of agent networks need to flag unreliable forecasts and help users choose interventions. Both decisions depend on what happens over several steps: an error can spread through the network, and an edit whose trajectory is easy to predict may still yield a poor collective outcome. We ask when information about error propagation improves failure detection and whether a learned twin can select effective network edits despite imperfect forecasts. We propose Propagation-Aware Validation for Networked Digital Twins (PAV-Twin). Its monitor combines Jacobian-based propagation features with recent errors and ensemble disagreement to estimate the risk that a forecast exceeds an error threshold. Its planner simulates each candidate edit and ranks the edits by their predicted collective outcomes. In simulations, the monitor gained 0.13 in area under the precision-recall curve on larger oscillator networks with familiar topologies and 0.09 on larger networks with held-out topologies, relative to a graph baseline without propagation features. Gains were small in contractive consensus. Giving the graph baseline the same features narrowed the gap. In a separate planning study, ensemble simulation recovered about 99% of the possible improvement over random intervention selection in oscillators and nearly all of it in consensus. With a simplified oscillator twin, selecting by predicted outcome also gave lower regret than selecting by trajectory fidelity. These results show when propagation features help flag unreliable forecasts and why the quality of intervention choices should be measured directly.

---


### 99. [VG3R: Video Generation Model for Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2611.28520)

**<font color=#1a73e8>作者：</font>** Jingong Chen, Qingwen Zhang, Lin Lian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are widely used as 3D priors for novel view synthesis and 3D scene generation. Fine-tuned for perception, generation models also excel at dense prediction such as depth estimation. However, methods that apply video generation models to 3D reconstruction either predict depth without cameras or generate geometry and estimate cameras through many iterative denoising steps, which makes them slower. In this paper, we present $\textbf{VG3R}$, which turns a pretrained video generation model into a feed-forward 3D reconstruction model. Our key observation is that such a model already captures the depth and camera motion of a video, but not in the form required for reconstruction. We introduce two components: $\textit{clip-level shift prediction}$, which corrects depth distortion caused by the unknown shift in decoded inverse depth, and a $\textit{multi-layer camera head}$, which predicts per-frame cameras parameters by combining features across transformer blocks. Using Wan2.1 as its video backbone, VG3R reconstructs a scene and estimate the camera of every frame without iterative denoising. It achieves the lowest ATE and reconstruction errors among methods built on video generation models, runs about 4 and 14 times faster than Aether and Geo4D. VG3R also demonstrates competitive depth estimation and 3D reconstruction performance compared with geometry foundation models. Project page: this https URL

---


### 100. [Walks2Maps: Learning Indoor Geometry from Crowdsourced Wi-Fi RTT and Motion Trajectories](https://arxiv.org/abs/2611.28532)

**<font color=#1a73e8>作者：</font>** Enguang Fan, Binh Minh Tran, Fulin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Everyday smartphone walks offer a scalable source of indoor geometry, but their motion traces drift and their radio measurements are distorted by multipath. We present Walks2Maps, a physics-guided framework that reconstructs a shared metric map from Wi-Fi round-trip-time (RTT) and motion observations, without a floor plan, surveyed access-point (AP) coordinates, or position labels. Walks2Maps jointly estimates pedestrian trajectories, AP locations, and per-trajectory stride scales, then recovers the pathway layout from the reconstructed paths. Shared AP observations connect walks recorded in different local frames, while metric ranges constrain their relative geometry and scale. An asymmetric range loss accommodates multipath-induced excess delay. On 22 phone trajectories collected along 11 routes on an office floor with 30 APs, Walks2Maps achieves median AP and trajectory errors of 0.87 m and 0.89 m, respectively, and a walked-area F1 score of 0.985. Ablations show that radio similarity can recognize places while still producing a distorted map; retaining the metric information in RTT resolves this ambiguity. Asymmetric modeling further reduces AP error by 54% relative to a symmetric loss. These results demonstrate how radio and motion measurements can jointly reveal indoor geometry without a dedicated mapping survey. We will release the dataset and toolkit.

---


> [!TIP]
> 当前位于：**51-100**（第 2/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
