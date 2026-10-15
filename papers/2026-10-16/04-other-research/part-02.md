# 📦 其他研究 | 2026年10月16日

> 本类共 **264** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-264](./part-06.md)

---

### 51. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](https://arxiv.org/abs/2610.19327)

**<font color=#1a73e8>作者：</font>** Zefan Yang, Zheyuan Zhang, Boris Maihe 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic ultrasound can standardize image acquisition and reduce operator workload and variability, but policy learning remains limited by the lack of realistic, controllable simulation environments. While controllable world models have advanced rapidly in natural-image domains, ultrasound world modeling remains challenging because each frame captures only a cross-section of unobserved 3D anatomy, causing small probe motions to induce large appearance changes. Existing approaches rely on robot-tracked poses and latent-space prediction, but do not directly generate the observations required for interactive control. We propose SonoWorld, a causal ultrasound world model that learns video dynamics from unlabeled clinical videos and grounds them to 6-DoF control using a small set of freehand clinical scans tracked with an EM sensor. SonoWorld is trained in three stages: pretraining a latent-action-conditioned video diffusion model on around 6.9 million unlabeled multi-organ ultrasound frames; grounding the learned video dynamics to metric probe poses with a small EM-tracked thyroid dataset; and applying distribution matching distillation to enable causal, long-horizon autoregressive generation with selectively caching eviction tokens at inference time. We evaluate controllability through pose-following fidelity, round-trip consistency, and axis-specific control under synthetic actions on held-out tracked scans, and further validate it with a user study. In model-based action discrimination, SonoWorld correctly ranks the target-directed probe motion over an equal-magnitude opposite motion in up to 74.8% of trials. To our knowledge, SonoWorld is the first causal, pose-controllable ultrasound world model learned primarily from freehand clinical videos, providing a data-driven interactive environment for robotic ultrasound data acquisition and policy evaluation.

---


### 52. [Counterfactual Gate-Support Decomposition: Separating Selection from Redistribution in Training-Data Filtering](https://arxiv.org/abs/2610.19343)

**<font color=#1a73e8>作者：</font>** Hyojung Han, Jongmin Kim, Seung-Hun Jeon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A training-data quality gate changes both which examples survive within regions of the input space and how training mass is distributed across those regions, so a gate-versus-random comparison does not isolate these mechanisms. We introduce Counterfactual Gate-Support Decomposition (CGSD), a four-arm, budget-matched design that crosses gate eligibility with support distribution and decomposes the observed gate effect into within-support selection, between-support redistribution, and their interaction. The practical constraint is finite-pool realizability: we characterize mass and token-assembly conditions under which the required arms can be constructed, together with a support-extinction case in which the ordinary design is undefined. On Korean-English and Korean-Japanese retrieval, the mean within-support selection component is the only one that exceeds its calibrated null band (+29.7 and +5.6 holdout items; 30/30 positive replicates), decisively in Korean-English and marginally in Korean-Japanese; redistribution and interaction remain unresolved at the available power. The same pattern holds for a second, unrelated gate family -- a model-confidence threshold rather than a deterministic verifier -- judged against its own null (+27.3 items, 9/9 positive), so the result is not a property of one gate's mechanism. On a mathematics gate, zero-eligibility supports leave the ordinary design undefined at every budget, while the extended design is constructible only inside narrow budget bands that an exhaustive scan locates and that the natural operating point misses -- the assembly condition separating a property of the pool from a limitation of the packer. CGSD therefore returns a decomposition, a constructible-but-underpowered design, or an explicit non-constructibility result, and says which; it prevents support redistribution from being silently interpreted as sample-level gate quality.

---


### 53. [Integrated Novelty Detection Systems: From Sensor Networks to Multi-Novelty Computer Vision](https://arxiv.org/abs/2610.19347)

**<font color=#1a73e8>作者：</font>** Irené Tematelewo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Novelty detection is crucial in various technological and scientific domains. Its importance spans from ensuring the reliability of sensor networks to enhancing the adaptability of computer vision systems. As AI systems become increasingly sophisticated and complex, effective anomaly detection is essential for maintaining reliability and accuracy. This work addresses novelty detection in weather sensor networks and computer vision. In weather sensor networks, particularly for monitoring rainfall, detecting blocked rain gauges can significantly impact data reliability, food security, and disaster management. This work evaluates four existing quality control methods for detecting blocked rain gauges and demonstrates their limitations, particularly in detecting clusters of faulty sensors. By comparing methods such as the Conditional Mixture Model (CMM), PSWQ (Fz-filter), Kernel Regression, and Gaussian Method, we identify their shortcomings and propose three novel quality control techniques that integrate probabilistic fault detection and consistency-based diagnosis framework to improve timely detection of blocked sensors, while reducing false alarms.
In the realm of computer vision, current systems often fail to handle multiple types of novelty due to their focus on single-novelty scenarios. We highlight the need for integrated systems capable of handling multiple types of novelty. To support this, we introduce the Novel Snapshot Serengeti (NOVEL-SS) dataset, derived from the Snapshot Serengeti camera trap data, which includes various forms of novelty. We also present the DCA (Detect, Characterize, and Accommodate) baseline system, designed to handle multiple novelty by detecting, characterizing, and accommodating them. This work aims to advance the robustness and adaptability of novelty detection systems across both weather sensor networks and computer vision applications.

---


### 54. [BFHD: Bidirectional Feature Harmonization Decomposition for Heterogeneous Clinical Assessments](https://arxiv.org/abs/2610.19352)

**<font color=#1a73e8>作者：</font>** Yuanhao Zhuo, Zixi Qin, Ling Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical assessments are often collected using heterogeneous assessment systems across centers and time, leading to records that mix different but related sets of measurements. This motivates harmonization beyond total-score linking. We formulate clinical harmonization at the measurement level as a bidirectional recoverability problem: given paired observations from two assessment systems, the goal is to identify which measurements can be reliably translated in both directions within an application-defined tolerance, while separating non-translatable components. We propose Bidirectional Feature Harmonization Decomposition (BFHD), a feasibility-driven framework that enforces bidirectionally coupled translation and uses feature-wise output gating to produce an explicit decomposition in the original measurement space. Experiments on synthetic data and real clinical assessment pairs show that BFHD achieves broader feasible harmonization coverage and improved subset stability compared to baselines.

---


### 55. [Asymptotic Behavior of Transformers](https://arxiv.org/abs/2610.19358)

**<font color=#1a73e8>作者：</font>** Katy Blumer, Da-Cheng Juan, Jon Kleinberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we study the behavior of transformer networks generating text over long periods of time. We show that even a three-token, single-layer attention-only transformer can fail to converge. We then study a rich class of transformers with arbitrary finite depth, layer normalization, MLPs, RoPE encodings, and an arbitrary mix of local and global layers. Every transformer in this class has a softmax temperature threshold above which its empirical cache distribution converges to a unique limit, independent of initial conditions. We show further that, while each transformer has a temperature threshold, the supremum of this set is infinite, so there is no global minimal temperature that forces all transformers to converge.

---


### 56. [Steering Vectors for Competing Ethical Frameworks Are Interchangeable: A Competing-Target Test for Activation Steering](https://arxiv.org/abs/2610.19359)

**<font color=#1a73e8>作者：</font>** Weilun Xu, Zipeng Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering adds a vector to a model's hidden states to control a named behaviour. A gain on that behaviour, however, does not show that the vector controls it directly: it may act through a component shared with neighbouring behaviours, which unsteered and random baselines cannot separate. We introduce the competing-target test: a vector is compared with the vector built the same way for a competing target, and an equivalence test states when their difference is below a useful margin. We apply it in open-weight models to vectors for Kantian deontology, which judges an act by the rule it follows, and act utilitarianism, which judges it by the welfare it produces. On held-out situations, prompting a framework raises its score and lowers the other's, whereas vectors for either framework move both scores alike, and none reaches the margin. The two vectors share most of their direction, a request to apply some framework; the same construction separates an optimistic from a pessimistic tone, whose vectors share much less. What a vector shares with its competitors therefore sets what it controls: steering a perspective can deliver a mixture, and measuring a disposition can measure its neighbours, unless tested against the competing target.

---


### 57. [VLX-Go: Robust Embodied Tracking through Multi-Stage Learning and On-Policy Refinement](https://arxiv.org/abs/2610.19361)

**<font color=#1a73e8>作者：</font>** Kyusong Lee, Heting Ying, Tiancheng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied visual tracking requires a robot to identify a designated target from visual observations and control its own motion to follow that target through an environment. Following an isolated person is a comparatively simple demonstration of embodied visual tracking, but following the intended person among distractors remains challenging. Existing methods exhibit a substantial drop in success from single-target to distractor tracking, motivating a focus on the shared spaces that person-following robots must navigate. We present \method{}, a vision--language waypoint policy built around the hypothesis that visual and language representations should be aligned before tracking-specific motion is learned. The policy combines complementary frozen visual encoders, multiscale temporal context, a transformer backbone, and a lightweight head for robot-centric waypoint prediction. Its training progresses through vision--language alignment, multimodal reasoning mid-training, and tracking specialization on 19,532 oracle episodes. Compared with 41.54\% distractor-tracking success for our earlier OmTrackVLA model, the complete multi-stage recipe achieves 55.80\%. We then explore on-policy refinement using filtered oracle labels for states visited by the policy. This preliminary study adds 2.42 percentage points of distractor-tracking success, reaching 58.22\%, while reducing collision rate by 1.99 pts. The final policy records the highest distractor- and ambiguous-tracking success rates among the compared methods. These results support staged multimodal learning as a promising direction for tracking among distractors and motivate further study of on-policy refinement for person following in shared spaces.

---


### 58. [Dynamic Graph World Modelling: Learning Future Dynamics from Temporal Context](https://arxiv.org/abs/2610.19364)

**<font color=#1a73e8>作者：</font>** Bo Li, Yue Yang, Yujin Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graph learning models how entities and their relations evolve from historical observations to predict future graph states. Existing methods do not fully address dynamic graph world modelling, which requires learning transitions from temporal context to future latent graph states. This is difficult for three reasons: nodes and relations rely on different historical evidence, structural evolution is path-dependent, and future snapshots provide sparse and realization-specific targets. We propose Dynamic Graph World Modelling (DyG-WM), the first framework to jointly predict future node and relation representations from temporal context by answering three questions: what has evolved, how it evolved, and what will evolve next. To capture what has evolved, a historical node-relation context encoder summarizes node-neighborhood trajectories and pair-specific histories. To characterize how it evolved, a node-relation path-signature encoder captures ordered structural changes. To predict what will evolve next, a dual-level joint-embedding objective predicts target-snapshot node and relation representations without reconstructing the raw graph. Experiments on 12 link-prediction and two node-classification datasets demonstrate the effectiveness of DyG-WM across both tasks.

---


### 59. [The Impact of Detector Architecture, Model Scale, and Scene Density on Multi-Pedestrian Tracking](https://arxiv.org/abs/2610.19369)

**<font color=#1a73e8>作者：</font>** Pedro Manoel Herminio Alves, Dalton Cézane Gomes Valadares, Cláudio de Souza Baptista  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian tracking in video is important for applications such as surveillance and scene analysis, but it becomes more challenging in crowded scenarios with frequent occlusions and rapid motion. This paper analyzes how detector architecture, model scale, scene density, and inference regime affect the tracking of multiple pedestrians. We compare the YOLO11, RT-DETR, and YOLO26 detector families with the ByteTrack and BoT-SORT trackers on sequences from the MOT17, MOT20, and SOMPT22 benchmarks. For YOLO26, we also compare traditional overlap filtering via Non-Maximum Suppression (NMS) with end-to-end inference. The RT-DETR family achieved the highest mean scores on the HOTA tracking quality metric across all three benchmarks with both trackers, with a more pronounced advantage on MOT20, albeit at a higher computational cost. On MOT17 and SOMPT22, YOLO26 variants, especially YOLO26-L with NMS, offered favorable combinations of quality and speed compared with RT-DETR. In the YOLO26 inference comparison, the end-to-end mode did not yield consistent tracking gains over the NMS-based regime. Taken together, these results provide a practical guide for selecting detectors and trackers for this task based on application priorities.

---


### 60. [One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models](https://arxiv.org/abs/2610.19375)

**<font color=#1a73e8>作者：</font>** Joshua Cheung, Zhang He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models are routinely selected, checkpointed and ablated on one-step prediction loss, on the assumption that a model which predicts the next latent better is a better model. In model-based RL this assumption is known to be unreliable; we ask whether it also fails for latent world models, where the training target is the model's own embedding and the loss is not expressed in interpretable units. We introduce a frozen-decoder protocol reporting one-step error in physical units, decomposed into the part already present in the encoder's representation and the part the predictor adds. Applying it to a recent end-to-end JEPA world model across three continuous-control environments, we move the metric by fine-tuning and measure goal-conditioned planning on the same checkpoints, with three training seeds and paired planning seeds throughout. Within one environment, a per-epoch ladder shows the relationship saturating after a single epoch: the first epoch improves fidelity by 32% and planning by 4.4 pp, but across the fifteen checkpoints that follow -- a further 15% fidelity improvement, monotone in every training seed -- the correlation between one-step error and planning success is r = -0.010. This is not a task-ceiling artifact: stratifying by a model-independent measure of training-data support, planning in the lowest-support stratum starts at 80%, leaving ample headroom, and is nonetheless flat from epoch 1 onward. Across environments the exchange rate is equally unstable: a 93% fidelity reduction on TwoRoom yields -0.7 pp of planning, while a 40% reduction on PushT yields +4.9 pp [+1.1, +8.9]. All results replicate under a decoder-free measure, latent drift. We also show that a matched continued-training control absorbs the entire fidelity gain we had attributed to an auxiliary objective.

---


### 61. [Robust Explanatory Analysis for Structured Optimization Networks (REASON) in Learning](https://arxiv.org/abs/2610.19378)

**<font color=#1a73e8>作者：</font>** Vahid Jebraeeli, Hamid Krim, Keisuke Fujii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We seek a hierarchical resolution of residual error under a composite learning objective as a principled mechanism for identifying and exploiting additional information, particularly under distribution shift and perturbation. Inspired by the System 1/System 2 paradigm, we formulate this principle as a two-loop mechanism serving a common inference goal. A fast, System 1-like loop resolves the residual addressable by the available evidence; the remaining epistemic residual triggers a medium speed, System 2-like loop that actively acquires additional evidence and measures its informational value through residual reduction. Over nested solution spaces, the medium-loop optimum is provably no worse than the fast-loop optimum. Experiments show that the resulting two-loop model consistently improves upon the fast loop at approximately half the computation of the medium loop, including under unseen corruptions, and, when provided a cleaner observation, outperforms staged classifiers and learning-to-defer methods at equal computational cost.

---


### 62. [MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation](https://arxiv.org/abs/2610.19384)

**<font color=#1a73e8>作者：</font>** Yuke Wang, Benlei Cui, Shen Pang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal agents increasingly rely on visual interfaces to perceive state and select actions, creating an attack surface not captured by text-only safety evaluations. We study Visual Semantic Hijacking, in which deceptive but semantically meaningful interface elements, such as forged system alerts, cause an agent to depart from its authorized task. We propose a trajectory-guided procedure that identifies candidate injection points and inserts reproducible visual payloads into the observation stream. Using this procedure, we construct MMA-SafetyBench, which contains 1,083 adversarial trajectories across web automation, desktop GUI control, mobile navigation, document understanding, and video processing. Across nine evaluated models, Attack Success Rate (ASR) reaches 87.96%, while Semantic Compromise Rate (SCR) reaches 98.09%. A 1--3--5 scoring scheme distinguishes target-matching outputs, semantic disruption without a target match, and successful preservation of the benign task. Controls covering all nine models and five domains show that attacks persist under neutral prompts. A safety-priority prompt lowers ASR without eliminating the failure mode.

---


### 63. [The Sum of All Summaries: PROPALIGN for Graded Proposition Salience Evaluation](https://arxiv.org/abs/2610.19387)

**<font color=#1a73e8>作者：</font>** Lin Ai, Emma Thronson, Katherine Conhaim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identification and ranking of salient propositions in documents is indirectly involved in many AI tasks, but few papers define proposition salience scores clearly, make diverse data available, or evaluate models directly on the task. This paper proposes PROPALIGN, a multiple-summary-based approach for propositional salience score estimation, and releases PROPALIGNBANK, an accompanying dataset for the method with 138K alignments of over 35K propositions. We compare several approaches to salient proposition extraction in English across a broad range of spoken and written genres, and demonstrate that naively asking models for judgments leads to inconsistencies. By contrast, graded, summary-based metrics are more stable. We further observe that while single models perform worse than humans, an ensemble of models incorporating linguistic features approaches manual annotation quality ceilings. In addition, analyses of the model outputs suggest insights into how models can extract salient information with and without the use of summaries.

---


### 64. [ELARSpeech: A 30K-Hour Dataset Across 675 Underrepresented Languages for Long-Tail Multilingual Speech Technologies](https://arxiv.org/abs/2610.19388)

**<font color=#1a73e8>作者：</font>** Sangmin Lee, Yejin Jeon, David Ifeoluwa Adelani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Massively multilingual speech modeling has made remarkable progress in recent years, yet existing training resources and benchmarks still underrepresent much of the linguistic long tail. To address this gap, we introduce ELARSpeech, a large-scale multilingual speech resource comprising 30,202 hours of speech across 675 underrepresented languages, curated from the Endangered Languages Archive. Combining human-annotated and unlabeled recordings, the corpus spans diverse recording conditions, domains, and language families. Beyond corpus construction, our experiments show how ELARSpeech supports extending ASR and TTS capabilities to diverse underrepresented languages, with further benefits from pseudo-labeling unlabeled data. At the same time, our speech representation analysis reveals remaining limitations in transferring existing multilingual models to the linguistic long tail. Together, ELARSpeech provides both a resource and a testbed for extending multilingual speech technology further into the linguistic long tail. We publicly release the dataset, all trained ASR and TTS models, and the complete data construction pipeline to facilitate research on long-tail multilingual speech technologies.

---


### 65. [Fully sequential Gaussian process regression for preference learning](https://arxiv.org/abs/2610.19391)

**<font color=#1a73e8>作者：</font>** Ilya O. Ryzhov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study continuous global optimization problems in which the objective function cannot be directly evaluated; rather, we observe only which of two selected design points appears to perform better, subject to noise. Such comparisons complicate the use of Gaussian process regression because they yield non-Gaussian posteriors. We consider a fully sequential approximation, based on moment-matching, that yields a fast closed-form update of the metamodel's mean and covariance. We then propose DOVE, a fully sequential sampling policy that combines an information gain criterion with randomized sampling designed to control error accumulation. Under fairly standard regularity conditions, we prove convergence rates for both statistical error and expected simple regret that depend on kernel smoothness. To our knowledge, these are the first such rates for fully sequential approximate Bayesian inference in continuous global optimization.

---


### 66. [Selective Next-Location Prediction with MetaModelSelect: A Lightweight Post-Hoc Confidence Metamodel](https://arxiv.org/abs/2610.19394)

**<font color=#1a73e8>作者：</font>** Calvin Jary, Nafiseh Kahani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-location prediction can support proactive mobile-network decisions, but acting on unreliable predictions can waste resources. We apply MetaModelSelect, a lightweight post-hoc confidence metamodel, to selective cellular next-location prediction. The mobility-specific model combines a learned embedding of the predicted location with the four largest softmax probabilities and Softmax Concentration. It learns whether a frozen recurrent neural network's top-1 prediction is correct, using only its outputs and without retraining the backbone. On path-balanced Changchun cellular mobility trajectories, we evaluate backbones trained with cross-entropy (CE) and self-adaptive training plus entropy minimization (SAT+EM), comparing against eight scalar confidence scores, two location-aware lookup methods, and a raw-logit multilayer perceptron. Relative to maximum softmax probability, MetaModelSelect achieves mean per-run reductions in area under the risk--coverage curve (AURC), excess AURC (E-AURC), and area under the generalized risk--coverage curve (AUGRC) of 2.6%, 4.2%, and 3.0% for CE, and 2.0%, 3.3%, and 1.9% for SAT+EM. It also achieves the lowest reported mean risk at every evaluated partial coverage. The results show that MetaModelSelect improves confidence ranking in this mobility setting while leaving the underlying location predictor unchanged.

---


### 67. [EpiGuard: An Autonomous Infectious-Disease Early Warning Agent Platform](https://arxiv.org/abs/2610.19396)

**<font color=#1a73e8>作者：</font>** Tonglong Wei, Zheng Yuan, Lingshuai Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Infectious disease outbreaks often spread rapidly before signs of widespread transmission become apparent, leaving a big challenge for rapid response and effective intervention. However, current infectious-disease early-warning systems face three major challenges: fragmented epidemiological evidence across diverse surveillance sources, highly uneven data availability across diseases and geographic regions, and delayed warning procedure caused by manual data collection, analysis, and reporting. To address these challenges, we present EpiGuard, an autonomous, continually self-improving agentic platform for timely and reliable early warning of more than 50 infectious diseases across different regions. EpiGuard proactively monitors and captures newly released official surveillance records, using the latest available evidence for risk assessments. It dynamically adjusts its analytical strategy across three evidence availability regimes, enabling reliable risk assessment under diverse data conditions, ranging from the absence of historical observations to sparse and abundant evidence. Moreover, EpiGuard learns from the successful execution process by preserving effective data-acquisition and analytical procedures as reusable standard operating procedures, enabling it to progressively generalize to previously unseen diseases and regions. We use officially released infectious-disease surveillance data from the China CDC and the United States CDC to evaluate EpiGuard's effectiveness. Experimental results demonstrate that EpiGuard outperforms state-of-the-art forecasting systems, improving forecasting performance by 9.68% and 14.04% on the China CDC and U.S. CDC datasets, respectively.

---


### 68. [Train to Stitch: Topology-Preserving Regularization for Interoperable Representations](https://arxiv.org/abs/2610.19401)

**<font color=#1a73e8>作者：</font>** Akshay Malhotra, Nicolas Zilberstein, Shahab Hamidi-Rad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large, powerful pre-trained models become more prevalent, there is growing interest in developing methods that allow different neural networks to be seamlessly combined with little or no direct communication between them. Take autoencoder-based data compression as an example: the ability to independently choose architectures and train encoder and decoder models, while still ensuring they work together, could fundamentally transform how such models are built, deployed, and updated. In this work, we introduce a novel approach that leverages topological regularization to align the latent spaces of two independently trained autoencoder models, entirely eliminating the need for coordination during training. We provide a conditional theoretical analysis showing how the structural agreement encouraged by our regularizer can translate into approximate geometric compatibility between independently learned representations. Reconstruction experiments validate this approach empirically, substantially narrowing the interoperability gap across multiple datasets.

---


### 69. [W-JEPA: Wavelet Joint-Embedding Predictive Architecture for Wearable Activity Recognition](https://arxiv.org/abs/2610.19411)

**<font color=#1a73e8>作者：</font>** Yogesh Prabhu, Loki Natarajan, Jingjing Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A major challenge in wearable device activity recognition is the heterogeneity across datasets in sensor placement, channel count, sampling rate and subjects. Moreover, the motion patterns that distinguish activities often appear as subtle, scale-specific variations within otherwise similar waveforms. As a result, raw signals are often ambiguous, and models trained on them tend to rely on cues specific to a particular sensor setup or participant, which limits both cross-dataset transfer and generalization to unseen participants. Addressing this requires representations that preserve such activity-relevant, scale-specific variation. We introduce W-JEPA, a self-supervised framework that exploits the multiscale structure of inertial motion and leverages a joint-embedding predictive architecture, by organizing windows into a fixed grid of wavelet tokens indexed by scale, sensor axis, and time. These wavelet tokens help expose activity-specific detail within broadly similar raw signals, and serve as the units of masked latent prediction. W-JEPA predicts masked token representations supplied by an exponential-moving-average (EMA) target encoder. Because recovering a masked token requires relating motion at one scale and axis to motion at other scales and axes, the model learns the cross-scale, cross-axis structure of human movement. Across six wearable activity benchmarks, W-JEPA outperforms state-of-the-art methods under random-window splits and remains the strongest when subjects are held out, improving average macro-F1 by 8.7 percentage points over the strongest published baseline. These results indicate that physically grounded multiscale tokenization, combined together with latent predictive learning, provides a promising foundation for transferable representations of heterogeneous wearable inertial data.

---


### 70. [Comprehensive Comparisons of Reinforcement Learning Algorithms in Autonomous Driving](https://arxiv.org/abs/2610.19429)

**<font color=#1a73e8>作者：</font>** Dechen Xie, Mushuang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive comparison of four representative reinforcement learning (RL) methods in autonomous vehicle (AV) decision-making, including: Fitted Value Iteration (FVI), Rollout Classification Policy Iteration (RCPI), Deep Q-Network (DQN), and a discrete-action adaptation of Deep Deterministic Policy Gradient (D-DDPG). The four methods are applied to the same AV decision-making problem at an unsignalized intersection and are compared in terms of optimality and safety, training stability, and training and decision cost. RCPI is the closest to a reference solution and has the most stable training process. However, it is the least data-efficient. D-DDPG reaches the second-smallest gap to a reference solution with the highest data efficiency, but has the least training stability. DQN is the most stable model-free method but has the highest collision rate. FVI achieves a lower collision rate than DQN, but is less data-efficient and less stable. Based on these results, we provide suggestions for selecting a method according to whether a model is available, the budget for training, and whether stable training is required.

---


### 71. [Learning to Select Features with Manifold Deep Unfolding PCA](https://arxiv.org/abs/2610.19436)

**<font color=#1a73e8>作者：</font>** Jingjing Liu, Pei Tai, Xianchao Xiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised feature selection (UFS) is of great significance in image processing and pattern recognition. Nevertheless, existing model-based methods often rely on manually tuned hyperparameters, while deep learning-based methods generally require massive training data. To address these issues, this paper proposes an efficient manifold deep unfolding feature selection network (MDUFS-Net). Technically, we first incorporate the $\ell_{2,0}$-norm into the classic principal component analysis (PCA) framework, then unfold the alternating direction method of multipliers (ADMM)-based iterative algorithm into an end-to-end trainable network, thereby enabling automatic parameter learning. Moreover, a manifold optimization strategy is developed to improve the numerical robustness. On this basis, we further extend MDUFS-Net into an enhanced variant called MDUFS-Net+ by introducing the $\ell_{0}$-norm for more discriminative feature representations. Extensive experiments validate that our proposed MDUFS-Net and MDUFS-Net+ outperform state-of-the-art methods in the UFS task, with promising performance in clustering. Our code is available at this https URL.

---


### 72. [More Than Seeing: Vision as Scalable Anchors in Native Multimodal Pre-Training](https://arxiv.org/abs/2610.19443)

**<font color=#1a73e8>作者：</font>** Haoyuan Wu, Aoqi Wu, Jiani Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Native multimodal pre-training trains a single model from scratch on text and multimodal data, enabling it to understand both language and visual inputs. However, how visual signals shape scaling behavior and support capabilities beyond visual understanding remains unclear. We investigate this question through controlled visual-content ablations across model sizes and training budgets. Specifically, we replace image embeddings with content-free padding token embeddings. Retaining visual content improves text prediction on image-text examples without materially changing the lowest text-only loss at a given compute budget, the optimal balance of model size and training data, or aggregate language scores. The relative multimodal loss benefit grows approximately as a power law of compute. To test benefits beyond understanding images, we evaluate spatial reasoning from text descriptions alone. Both conditions improve with model and data scaling. During training of the largest model, visual gains are most sustained in localization, navigation, and symbolic planning, which involve maintaining object configurations or composing spatial updates; gains in spatial relations, geometry, and physical commonsense are less consistent. These findings identify visual content as a scalable anchor for multimodal learning, with benefits that extend beyond visual inputs while preserving aggregate language performance.

---


### 73. [xLightGCN: Explainable Graph Neural Network Based Recommendation Systems with Most Influential Peers](https://arxiv.org/abs/2610.19446)

**<font color=#1a73e8>作者：</font>** Calder Johnson, Robin Cohen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommendation systems, systems that predict a user's preference for items in order to curate that user's feed, are a ubiquitous and central feature in online social networks. While they are a central piece of our modern digital infrastructure, many modern approaches are opaque black boxes, making them difficult to audit, understand, and assess the trustworthiness of. In this paper we present an exact, graph-based approach for generating explanations for decisions made by recommendation systems. We argue that in the risk-sensitive sociotechnical context of user-facing AI such as recommendation systems, explainability is a key pillar for establishing the trustworthiness of models and validating their effectiveness. We propose a technique built on LightGCN like architectures, an influential and popular class of recommendation models. We describe our approach and argue that it provides an appropriate assurance mechanism for these AI systems leading to specific advantages, including interpretable explanations and a theoretically guaranteed measure of explanation fidelity. We conclude by discussing limitations and directions for future research.

---


### 74. [AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System](https://arxiv.org/abs/2610.19454)

**<font color=#1a73e8>作者：</font>** Tianzhu Hu, Hang Yu, Zeyuan Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital advertising is an important means for platforms to reach potential users and drive business growth. Advertising delivery is the core link between marketing objectives and actual returns. Existing methods have achieved partial automation in individual tasks such as bidding and budget allocation, but they still rely on human operators for overall coordination, making it difficult to support large-scale operations. They also often fail to achieve optimal performance, and individual experience remains difficult to turn into reusable operational capabilities. In addition, as advertising markets change, advertising delivery systems need timely strategy updates to remain effective in dynamic markets. To automate the entire advertising operations process and improve adaptability to market changes, we propose AdCoEvo, a co-evolving multi-agent advertising delivery system. Specifically, the system connects delivery decisions across different timescales and operational granularities through role specialization. Diagnostic results guide account planning and strategy adjustment in the next period. The multi-agent system updates its model parameters based on actual delivery outcomes and continually improves delivery strategies through mutual feedback among planning, adjustment, and diagnosis, thereby achieving co-evolution. Experiments show that, relative to the rule-based operational baseline (Rule), AdCoEvo increases advertiser value by 14.02% while reducing cost per acquisition by 7.07%. Compared with a multi-agent system with fixed parameters, AdCoEvo increases advertiser value by 3.96% and reduces cost per acquisition by 1.24%, indicating that co-evolution can yield greater delivery returns.

---


### 75. [DeBoneDiT: Depth-Driven Conditional Bridge Diffusion Transformers for Bone Suppression in Chest X-Ray Images](https://arxiv.org/abs/2610.19466)

**<font color=#1a73e8>作者：</font>** Yifei Sun, Fenglei Fan, Junhao Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-Ray (CXR) is a primary modality for diagnosing pulmonary diseases, yet the overlap of bony structures often obscures critical radiographic findings, increasing the risk of diagnostic uncertainty. While Dual-Energy Subtraction (DES) is the clinical benchmark for bone suppression, its widespread adoption is primarily hindered by specialized hardware requirements and increased radiation exposure. Recently, diffusion-based generative models have shown promise for this task, yet they are still constrained by reconstruction-biased latent compression, prior-induced domain gap, and a scarcity of high-quality paired datasets. To address these challenges, we propose DeBoneDiT, a depth-driven conditional bridge diffusion Transformer architecture for efficient high-resolution bone suppression. We first introduce Depth Auto-Encoder (DAE), a structure-aware vision tokenizer for latent compression. By incorporating a multi-level depth feature loss derived from the pretrained Depth Anything V2 encoder, DAE preserves both visual fidelity and structural consistency. Second, we formulate bone suppression as a source-conditioned Brownian bridge diffusion process, leveraging CXRs as both the diffusion prior and structural guidance to narrow the source-to-target domain gap and maintain anatomical plausibility. Furthermore, we have constructed and released SZCH-X-Rays, the largest publicly available high-quality paired dataset for bone suppression to date, comprising 741 pairs of CXR and DES soft tissue images. Extensive experiments and downstream evaluation demonstrate that DeBoneDiT achieves superior bone suppression performance with reduced computational overhead.

---


### 76. [Quantum-Resilient Secure Protocol for Decentralized Edge-IoT Peer-to-Peer Energy Trading Systems](https://arxiv.org/abs/2610.19491)

**<font color=#1a73e8>作者：</font>** Ali Shahidinejad, Jamshid Aghaei, Mahdi Jalili  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of quantum computing presents substantial challenges to the security of Peer-to-Peer (P2P) energy trading systems. This paper introduces an innovative mutual authenticated session key agreement protocol aimed at protecting edge-IoT P2P energy trading communications in the quantum era. Each peer is an IoT-enabled smart metering device that is registered by an edge registration authority and acts as both producer and consumer. The proposed protocol incorporates CRYSTALS-Kyber's quantum-resistant cryptographic suite to guarantee the authenticity and confidentiality of negotiated session keys in the presence of quantum threats. Furthermore, it leverages the Hedera Hashgraph public blockchain, which is recognized for its quantum-resilient design, to ensure transparency and support efficient revocation mechanisms. Extensive comparative analyses have been conducted to demonstrate the protocol's superiority over existing alternatives, including both traditional schemes based on classical cryptography and emerging early-stage post-quantum approaches, in terms of performance and security features. By combining robust security and high efficiency, the proposed protocol fosters the development of resilient decentralized energy markets, paving the way for secure and sustainable energy distribution in the future.

---


### 77. [Robust Real-Time Monocular Human Pose Estimation with Insole-Based Sensor Fusion](https://arxiv.org/abs/2610.19494)

**<font color=#1a73e8>作者：</font>** Liang Yu, Tao Zhu, Xiangqing Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time monocular human pose estimation is an important sensing component for human-centered intelligent systems. While recent camera-based methods have achieved impressive accuracy, fundamental challenges persist, particularly when visual observations are incomplete, such as during lower-body occlusion or short out-of-frame intervals. In these challenging but common scenarios, vision-only systems often struggle to reconstruct physically plausible lower-limb motion and reliable foot-ground contact. Due to the highly unobtrusive and wearable nature of smart insoles, this paper investigates whether simple plantar pressure and acceleration sensors can effectively resolve these visually induced limitations. To systematically investigate this, we first collect a synchronized multimodal dataset and then propose a part-decoupled temporal fusion framework. The proposed model fuses foot-sensing features into the lower-body branch to compensate for incomplete visual evidence, while a lightweight coordinator exchanges information between the upper- and lower-body temporal representations to maintain whole-body consistency. The framework is evaluated with three representative real-time visual backbones based on 2D keypoints, 3D landmarks, and SMPL-based human mesh recovery. We evaluate our framework on three representative real-time visual backbones. Quantitative experiments demonstrate that incorporating simple foot sensors consistently improves pose accuracy, motion smoothness, and gait-related measurements over vision-only baselines, with the most significant gains observed under occlusion and short visual-dropout conditions. Ultimately, our results demonstrate that unobtrusive foot sensing provides vital and complementary physical observability when camera observations are temporarily unavailable.

---


### 78. [SKG: A Law-Induced Engine from Inference to Induction](https://arxiv.org/abs/2610.19505)

**<font color=#1a73e8>作者：</font>** Jian An, Chaoshi Wu, Jinhui Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes the SKG (Symplectic-Kernel Gradient) reasoning engine for law-induced inference and induction. Laws are a priori; data provide instances. Inference is geometric evolution under law constraints. We organize symplectic geometry, GENERIC, kernel methods, RKHS, group-equivariant networks, and constrained mechanics into a unified, analyzable, implementable, verifiable framework. We propose the SKG octuple S = (M, g, omega, H, S, G, Delta, Pi), whose four components correspond to four levels of laws: conservation laws, constitutive relations, symmetry groups, and axiom systems.
Main results: (1) Invariants enter metric construction via the Jacobian: g = J^T Sigma^-1 J + epsilon_G I. For constant cases, we establish inverse reconstruction theory: solvability rank condition (Thm 3.9), consistency criterion (Thm 3.11), and uniqueness theorem (Thm 3.14). (2) The kernel bandwidth matrix is uniquely determined by Fisher information and satisfies task-independence (Thm 3.19). (3) The metric reconstruction error decomposes into four terms (Thm 3.21), with squared condition number kappa(Sigma^*)^2 as the dominant amplification factor (Thm 3.22). (4) For state-dependent cases, we establish function-space reconstruction theory on matrix-valued RKHS (Thms 4.8, 4.9). (5) Three-layer projections handle axiom, symplectic-step, and conservation constraints. (6) The residual equation yields the observable formula, four-dimensional rank condition, and noise propagation, while g_qq is structurally unidentifiable. (7) Kernel parameterization yields the RKHS extrapolation bound (Thm 4.15) and strict OOD gain theorem in group directions (Thm 8.15). (8) The learning-decoupling theorem (Thm 9.1) proves the sole object of induction is the parameters of the task energy.
Validation: 1D damped oscillator and 2D rotation-invariant system; 6 unit tests, 10 experiments (paired t-test, p < 0.01).

---


### 79. [CktHGVAE: A Symmetric Design/State Heterogeneous Graph Variational Autoencoder for Transistor-level Analog/Mixed-signal Circuit Design and Analysis](https://arxiv.org/abs/2610.19508)

**<font color=#1a73e8>作者：</font>** Shigeyasu Uno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose CktHGVAE, a heterogeneous graph variational autoencoder for transistor-level analog/mixedsignal CMOS circuits that takes not only design variables but also state variables as its inputs and outputs. With a single hyperparameter configuration without topology-specific tuning, comparison between model-generated and SPICE-simulated circuit operational states gives median R2 values above 0.9 for typical single-ended voltage amplifiers and the CMOS inverter, and 0.81-0.96 for differential amplifiers with larger datasets. Latent-space optimization in the PCA-reduced latent space with Bayesian optimization, evolutionary search, random search, and quasi-exhaustive search is demonstrated for a common-source voltage amplifier with NMOS input and resistive load, where the objective function is defined as a penalty for deviation from required circuit specifications. For each search strategy, 93.3 - 100% of all design candidates suggested by the model satisfy the required circuit specifications at the decoder output, and SPICE simulations verify that 90 - 100% of them indeed satisfy the requirements. The model pretrained on a batch of topologies can be transferred to unseen topologies without retraining at all, with zero-shot reconstruction median R2 values of 0.72-0.90 in three of four scenarios, including transfer from single-ended to differential topologies, although the transfer fidelity depends on the choice of pretraining topologies. Our demonstrations suggest that the proposed model can potentially serve as a basis for AMS CMOS circuit design automation.

---


### 80. [Revisiting Triplet Contrastive Learning for 3D Shape Understanding](https://arxiv.org/abs/2610.19519)

**<font color=#1a73e8>作者：</font>** Chaoyang Zhu, Zhe Liao, Jiayi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-modal 3D pre-training, aligning 3D shapes, their 2D image counterparts, and language descriptions has made tremendous progress. However, we find that supervision from rendered images is unreliable, the semantics encoded in synthetic views are distorted due to domain gap, self-occlusion, and rendering artifacts. Instead, we learn transferable 3D representations from language only. We observe that, in real world, 3D shapes are organized in a tree-like structure, ranging from general concepts to fine-grained instances with specific attributes, while language typically denotes generic concepts and subsumes these various 3D instantiations. Hence, we propose to embed 3D representations in hyperbolic space, whose geometry is well-suited for modeling tree-like data without distortion. To capture the asymmetric hierarchy between language and 3D shapes, we further impose a partial-order relation that language entails 3D shapes. Our method, Hyperbolic Contrastive Learning (HyperCL), jointly optimizes a hyperbolic geodesic-based contrastive objective and an entailment loss to learn discriminative cross-modal representations while explicitly preserving this hierarchy. We also introduce a rigorously verified benchmark for comprehensively evaluating cross-modal 3D alignment. Across two widely used benchmarks and ours, we improve the performance up to 4.6% absolute percentage on 3D shape classification and 5.5% on cross-modal text-to-3D retrieval under the same parameter budget. The code and evaluation benchmark will be made publicly available.

---


### 81. [HankelKANet: Lightweight Path Loss Estimation via Physics-Inspired Hankel Convolution](https://arxiv.org/abs/2610.19524)

**<font color=#1a73e8>作者：</font>** Yue Ruan, Xiaoxiao Cheng, Yunan Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate path loss (PL) estimation is essential for wireless network planning and optimization. This paper proposes HankelKANet, a lightweight physics-inspired network for PL estimation that structurally embeds electromagnetic propagation characteristics into the neural architecture. Built on a single residual UNet backbone, the proposed model integrates urban layout features with a convolutional Kolmogorov-Arnold network(KAN). Specifically, the convolutional kernels are parameterized by the radial amplitudes of the zeroth- and first-order Hankel functions. This formulation acts as a physics-inspired nonlinear distance encoding, enabling the network to capture dominant attenuation characteristics directly without requiring additional physics-based loss terms. Experimental results demonstrate that HankelKANet achieves state-of-the-art accuracy and efficiency on both the simulated RadioMapSeer dataset and the real-world Huawei RSRPSet. Compared with the leading baseline, PEFNet, it reduces the parameter count by 78% and lowers the RMSE by 16.96% on the simulated data, while further exhibiting robust cross-dataset transferability and high data efficiency during target-domain adaptation. To interpret these empirical gains, we mathematically establish a parameter-conditional spatial gradient bound. Using discrete Dirichlet energy (DDE) and Jacobian sensitivity heatmaps, we empirically verify that this physical encoding intrinsically constrains the network's spatial derivatives. This structural smoothness effectively eliminates non-physical spatial ripples, preventing overfitting to simulator artifacts and serving as the fundamental driver for robust real world generalization.

---


### 82. [Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following](https://arxiv.org/abs/2610.19525)

**<font color=#1a73e8>作者：</font>** Sangyeon Yoon, Wooseok Seo, Hamish Ivison 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verifiable instruction-following benchmarks emphasize output-constraint satisfaction but can overlook whether responses meaningfully answer the underlying request, creating an evaluation blind spot. We show that frontier models can receive full credit for responses with little substantive answer content. Using the same verifier-based criterion as a training reward can induce reward hacking, as publicly released checkpoints exhibit higher constraint satisfaction but lower response quality after reinforcement learning with verifiable rewards. To address this reward hacking, we introduce CALIF, a lightweight method that augments verifier rewards with a calibrated likelihood-based bonus to preserve response quality. CALIF evaluates response likelihood under the request alone using the existing frozen reference policy, requiring no additional judge or learned reward model. Across models ranging from 1.7B to 8B in reasoning and non-reasoning modes, CALIF improves constraint satisfaction on IFBench while maintaining response quality near or above pre-RL levels. It also outperforms corresponding base policies in 40 of 45 model-metric comparisons across three rubric-based instruction-following benchmarks, demonstrating gains beyond training verifiers.

---


### 83. [Reducing the Gap Between Spatial and Space-Filling Curve Neighbors in 3D Point Cloud Segmentation](https://arxiv.org/abs/2610.19530)

**<font color=#1a73e8>作者：</font>** Konan Sasaki, Junya Komori, Kazuhiro Hotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a lightweight and highly accurate method for nearest-neighbor search in 3D point clouds, approaches based on space-filling curves (SFC) have been proposed. However, due to the inherent properties of SFC, a gap arises between proximity relationships along the SFC and those in the original Euclidean space. In this study, we propose a loss function that reduces the influence of this gap. Specifically, we compute the distances between adjacent points along the SFC and train the model to optimize feature similarity between pairs of points that are distant from each other in the original 3D space. We incorporate the proposed method into a high-performing 3D point cloud segmentation model and evaluate its effectiveness on three datasets. The results demonstrate that the proposed method outperforms conventional methods on both indoor and outdoor point cloud datasets.

---


### 84. [A Unified Response Framework for Questions and Tutoring Dialogues](https://arxiv.org/abs/2610.19532)

**<font color=#1a73e8>作者：</font>** Zhangqi Duan, Simon Woodhead, Maya Miller-Vedam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing student models in educational applications largely focus on student responses to questions. However, as tutoring becomes more accessible at large scale, it is important to analyze dialogues between tutors and students, which may reveal fine-grained evidence on student knowledge. In this work, we propose a unified framework that models both student responses to questions and tutor-posed subtasks during dialogues on a shared item response theory (IRT) scale. We first identify mathematical subtasks in tutoring dialogues, rewrite them into self-contained questions, and identify the correctness of student responses to these subtasks. We then develop an IRT framework that estimates question/subtask difficulty from text, tracks students' evolving abilities across question-answering and dialogue interactions, and a novel method to leverages tutor moves between consecutive subtasks to regularize their difficulty values. We evaluate our framework on two real-world math education datasets containing both human- and AI-tutored dialogues. Results show that our framework outperforms strong baselines on both question difficulty prediction and response correctness prediction.

---


### 85. [RDCompGS: Rate-Distortion Optimization for Compression of 3D Gaussian Splatting with Image Codecs](https://arxiv.org/abs/2610.19538)

**<font color=#1a73e8>作者：</font>** Huiping Ren, Shuai Wan, Luqian Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables high-quality, real-time novel view synthesis but requires significant storage and transmission resources. Mapping Gaussian attributes to 2D representations enables efficient compression using mature image codecs. However, Gaussian representations that achieve comparable rendering quality are generally treated similarly during optimization, despite substantial differences in coding rate, leading to limited rate-distortion (R-D) performance after compression. To address this limitation, we propose RDCompGS, a 3DGS compression method that enables overall R-D optimization of Gaussian representations with respect to subsequent coding. A differentiable estimate of the coding rate is incorporated into the R-D optimization with rendering distortion. The rate constraint adjustment model further regulates the R-D trade-off across different compression conditions. Extensive experiments on three benchmark datasets demonstrate that RDCompGS achieves average Bjøntegaard Delta Rate reductions of 37.84% and 49.31% with H.265/HEVC and JPEG XL, respectively. The estimated rate also shows a strong correlation with the actual bit-rate under different compression conditions.

---


### 86. [Two-stage Residual Learning for Modelling Strength-Informed Optimisation of Thermal Systems](https://arxiv.org/abs/2610.19539)

**<font color=#1a73e8>作者：</font>** Talha Ansar, Waqar Muhammad Ashraf, Abdulelah S. Alshehri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggregate performance metrics do not identify local modelling inaccuracies in machine learning (ML) surrogates used for thermal-system optimisation. This study assesses local modelling strength through validation-based reliability screening and post-optimisation residual assessment. A two-stage residual learning (TSRL) framework, built on artificial neural networks (ANNs), is developed for modelling-strength-informed and domain-constrained optimisation of thermal systems. Within the TSRL framework, a base ANN predicts the process output, and a residual ANN learns the signed residuals left by the base ANN. The TSRL framework is implemented on two case studies of thermal systems, including 817 simulation observations of a crude distillation unit and operating records from a 395 MW industrial gas turbine. The TSRL framework reduces the test root mean square error (RMSE) from 10.3 g/s to 4.7 g/s for Fuel Oil in the refinery dataset and from 151 kJ/kWh to 105 kJ/kWh for turbine heat rate (THR). The base ANNs trained within TSRL are embedded in domain-constrained optimisation problems, and the modelling strength at each computed solution is assessed using the locked residual-score threshold. Each computed solution receives a good modelled region (GMR) or weak modelled region (WMR) label to inform ML model-based decision-making for safety-critical operation of thermal systems.

---


### 87. [Cross-Scenario Industrial Defect Detection via Domain-Robust Training and Metric-Aligned Selection](https://arxiv.org/abs/2610.19540)

**<font color=#1a73e8>作者：</font>** Dikai Li, Weijia Wang, Yuan-Gen Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated defect detection of industrial boards must remain highly reliable under cross-scenario variations in lighting, surface contaminants, and production line conditions. This makes cross-scenario defect detection a domain generalization problem, wherein models are required to detect, localize, and classify defects across unseen scenarios while minimizing false alarms on clean boards. For the IDA 2026 Track 1 challenge, we propose a cross-scenario defect detection method that includes four complementary modules: cross-scenario robust training, small-defect-aware learning, score calibration and inference threshold selection, and metric-aligned checkpoint selection. These four modules respectively introduce cross-scenario robust normalization and DSU-style statistic perturbation with progressive random convolution, NWD and parameter-free spatial attention, the VFL learning objective, and a custom SWAD variant driven by the Track 1-oriented proxy. Experimental results demonstrate that our model achieves a Track 1 score of 0.564 with a screening score of 0.696 on the test dataset on a single RTX 4090 GPU. The code is available at this https URL.

---


### 88. [Test-Time Forecasting: Recurrent Depth Enables In-Context Dynamics Prediction](https://arxiv.org/abs/2610.19552)

**<font color=#1a73e8>作者：</font>** Jeffrey B. Lai, John Quinn, Anthony Bao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for dynamical systems can forecast unseen partial differential equations (PDEs), ordinary differential equations (ODEs), and time series during inference. However, it remains an open question whether these foundation models truly learn generalizable in-context forecasting strategies. We show that looped transformers are capable of emulating propagators for dynamical systems in-context by first establishing a link between linear attention and (extended) dynamic mode decomposition. We then generalize this insight into the $\textit{Test-Time Forecasting}$ (TTF) framework in which a one-step forecaster leverages iterations of gradient descent as recurrent depth. We demonstrate that lightweight TTF models trained on ODEs and PDEs generalize to out-of-distribution system dynamics during autoregressive rollout after being trained for one-step prediction. Our results reinforce TTF as a theoretically motivated framework for designing recurrent depth models capable of forecasting unseen dynamical systems at test-time.

---


### 89. [Evidence-Anchored Overdose Death Prediction from Death Investigation Reports](https://arxiv.org/abs/2610.19556)

**<font color=#1a73e8>作者：</font>** Raavi Gupta, Ziqing Yang, Karli R. Hochstatter 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Confirmation of overdose deaths in the United States is often delayed due to the complexities of certifying drug-involved deaths. Death investigation reports represent a rich but underutilized data source that could be used to predict whether a death is a suspected overdose (i.e., a death preliminarily identified as an overdose prior to the final cause and manner of death determination). We present an automated framework that classifies suspected overdoses from death investigation reports, while producing supporting explanations guided by expert knowledge. Through an expert-guided design process, we investigate 1) what type of explanations are best for model prediction performance, and 2) which architecture is better suited for this task: pipeline models that rationalize first and then predict, or self-rationalizing models that jointly predict and rationalize? Our experiments show that a pipeline model with explanations grounded in the input death investigation reports outperforms the other settings. Our best model also outperforms a rule-based system currently in deployment by 15%, while allowing expert interventions for final decisions.

---


### 90. [TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series](https://arxiv.org/abs/2610.19557)

**<font color=#1a73e8>作者：</font>** Aditya Radhakrishnan, Maxwell A. Xu, Wanting Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive learning for time series depends on deciding which pairs of inputs should be treated as similar and dissimilar. Because few augmentations reliably preserve meaning in time series, prior methods have relied on two disjoint notions of similarity between windows: structural similarity, which relates windows with similar morphology, and temporal similarity, which relates windows that occur close together in time. We introduce TEX-MEX, to our knowledge the first approach to unify the two into a single relationship. Given a random batch of windows drawn across the dataset, TEX-MEX uses the encoder to identify which windows are structurally similar or dissimilar to each other. It then pulls each window toward the temporally shifted versions of similar windows and pushes it away from those of dissimilar ones, learning what typically accompanies similar windows in time. Across PPG, EEG, ECG, accelerometry, and continuous glucose monitoring, TEX-MEX broadly achieves state-of-the-art performance against contrastive, reconstructive, JEPA-based, and modality-specific approaches, establishing it as a strong general SSL objective. We further train a 560K-parameter PPG foundation model that achieves state-of-the-art performance across a broad range of downstream benchmarks while being roughly 50x smaller than the next-best unimodally pretrained PPG foundation model in our evaluation. We will release this foundation model open-source and open-weight to the community to support future work and practical applications.

---


### 91. [SaTPO: Text-to-Image Safety Alignment via Transition Preference Optimization](https://arxiv.org/abs/2610.19563)

**<font color=#1a73e8>作者：</font>** Ziyi Fang, Jingzhi Li, Xiaojun Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safety alignment of text-to-image diffusion models aims to suppress harmful content without compromising useful generation capabilities. However, preferences over completed images compress multidimensional generation factors into a coarse signal, potentially driving changes beyond those required for safety. To address this, we propose Safety Transition Preference Optimization (SaTPO), which enforces step-wise alignment during denoising. SaTPO leverages the insight that an unsafe prompt and its safe rewrite naturally form a tightly coupled preference pair when conditioned on a shared parent state and noise realization. By anchoring optimization on identical parent states, SaTPO eliminates historical trajectory divergence, confining safety adaptation to an incremental alignment while preserving task-relevant semantics. Multi-scale drift constraints and benign replay further limit behavioral deviation and preserve ordinary generation. We additionally construct CoProPV, a refined dataset ensuring visually verified contrasts. Experiments on Stable Diffusion v1.5 and SDXL demonstrate improved safety-quality trade-offs. Compared with AlignGuard, PerspectiveVision unsafe-detection rates on Inappropriate Image Prompts decrease from 12.70% to 6.00% and from 15.04% to 9.30%, respectively, while FID improves from 32.28 to 25.95 and from 36.50 to 27.51. Warning: this paper includes potentially offensive content.

---


### 92. [Learning Across Temporal Graph Representation Silos](https://arxiv.org/abs/2610.19576)

**<font color=#1a73e8>作者：</font>** Minwoo Yu, Young-guk Ha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph data are recorded in different representations, but whether these differences also determine the scope of learned knowledge reuse remains unclear. This study investigates whether predictive structure learned from relational histories can be reused between continuous-time dynamic graphs (CTDGs) and temporal knowledge graphs (TKGs). Bidirectional reuse emerges while retaining distinct input and prediction interfaces and independent vocabularies, and sources with the same representation are not always more useful. Controlled reorganizations of source histories show that the organization contributing to reuse varies across source-target conditions. We show that learned aspects of Relational Dynamics, the predictive structure present in relational histories, can be reused across conventional representation boundaries. Independently pretrained TKG and CTDG learners can also be fused at the score level to improve prediction on a third dataset without entity or relation-semantic alignment. Two proofs of concept in recommendation and security detection illustrate that external temporal sources without direct alignment can also become useful pretraining resources.

---


### 93. [InstructPro2: Natural Language and Biological Grounding Guided De Novo Protein Design](https://arxiv.org/abs/2610.19592)

**<font color=#1a73e8>作者：</font>** Charles Novak, Zhenqiao Song, Chuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to generate proteins with desired functions is a central goal of computational biology. Although natural language can express diverse design objectives, existing protein generation methods often support only narrow tasks or make limited use of biological constraints. We develop InstructPro2 to translate natural-language design objectives into protein sequences while incorporating task-specific biological context. A text encoder captures the design instructions, while dedicated ligand and antigen encoders provide biological context to the sequence-generating decoder. For pretraining, we assemble InstructPro2Bench, comprising 205.7 million <function description, protein> pairs from UniProtKB. We subsequently adapt the model to ligand-binding protein and antibody design. On functional protein generation benchmarks, InstructPro2 outperforms Pinal, the strongest baseline, achieving a functional recovery F1 of 74.8 versus 62.2 and lowering global RMSD from 5.33A to 3.04A. For antibody design, the model obtains a DockQ score of 0.39, while ligand-binding protein design reaches a docking success rate of 72.6%. These findings highlight how integrating language-based instructions with biological conditioning can extend protein generation to distinct design settings.

---


### 94. [Are AI Decision Models Biased? A Case Study of Jev](https://arxiv.org/abs/2610.19619)

**<font color=#1a73e8>作者：</font>** Ilaria Imperatrice, Taisia Kameneva, Adam Eric Greenberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do AI models designed for fast, structured decisions exhibit the cognitive and social biases observed in human judgment? We evaluate Jev, a model described as a System One decision-maker, using 41,500 responses across cognitive reflection tasks, five classical cognitive-bias paradigms, and a pricing experiment testing ethnic and gender bias. At the level of selected answers, the results are largely encouraging. We confirm previous findings that Jev performs extremely well on cognitive reflection problems. We also observe that it generally avoids the characteristic choice patterns associated with several well-documented human biases, and exhibits only small differences among demographic groups in the tested pricing scenario. However, this apparent robustness conceals important vulnerabilities. Its judgments are sensitive to irrelevant numerical information and the ordering of response options. Moreover, several cognitive-bias manipulations substantially affect returned probabilities even when selected answers remain unchanged. Most strikingly, Jev answers a well-known probability problem correctly in every response but violates the same underlying probability rule in every response to an adapted version. We investigate this discrepancy using 15,000 additional responses across 30 conjunction tasks. Jev violates the rule in 54\% of responses, with accuracy varying dramatically across formulations and answer orders. These findings suggest that evaluating decision models solely on familiar benchmarks and selected answers may substantially overstate their reliability in practical applications. They also identify vulnerabilities for developers to address and practical considerations for users integrating such models into automated decision-making systems.

---


### 95. [MagicGarment: Benchmarking Single-Image Standalone 3D Garment Reconstruction](https://arxiv.org/abs/2610.19623)

**<font color=#1a73e8>作者：</font>** Jia Chen, Ruyang Zhao, Jun Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D reconstruction has advanced rapidly, yet standalone garments remain challenging due to thin-shell geometry, open boundaries, and layered structures. Existing datasets and evaluation protocols provide limited support for systematic evaluation in this setting. We introduce MagicGarment, a benchmark for single-image standalone 3D garment reconstruction with 1,518 professionally constructed assets across 17 composite garment types, aligned multimodal annotations, and a unified evaluation protocol. We further establish a garment-aware reference baseline by adapting a pretrained image-to-3D backbone at two levels: Grounded Semantic Refinement (GSR) provides garment-focused visual conditioning, while Flow-Time-Route LoRA (FTR-LoRA) adapts the frozen 3D generative backbone using flow-timestep, token-routing, and expert-load information. Experiments demonstrate MagicGarment's benchmark utility and the effectiveness of garment-aware adaptation. Project page: this https URL.

---


### 96. [Adaptive Observation Control for Active Visual Recognition](https://arxiv.org/abs/2610.19624)

**<font color=#1a73e8>作者：</font>** Dikai Li, Weijia Wang, Yuan-Gen Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual recognition models usually process a fixed view under a fixed computation budget, although images often benefit from different scales and amounts of spatial evidence. Active vision can adapt by observing a coarse scene and then selecting informative fixations, but the public AdaptiveNN-DeiT-S pipeline still fixes both field of view and observation count. We extend this fixed-step recognizer with a controllable observation interface that adapts both the field of view and the number of fixations to the input. Specifically, the model predicts a per-fixation scale that sets its field of view, refines each selected crop with optional scale-gated foveation and a residual high-resolution detail-token branch, and uses label-grounded stop heads for input-dependent early termination. Experiments across fine-grained benchmarks, full ImageNet-1K, and ImageNet-A/R-derived classification splits show that the interface remains competitive with fixed-step references while exposing a controllable observation budget. The same checkpoint enables threshold-controlled accuracy-compute trade-offs without per-threshold retraining. On sequential ImageNet-1K, the learned stop rule outperforms fixed-step truncation of the same checkpoint, sustaining 81.9% top-1 using 2.45 of the four focus steps and exceeding three-step truncation at lower cost. On each benchmark, a variant combining scale control and detail-token fusion achieves the highest accuracy among the tested component-added non-exit variants. Our code is available at this https URL.

---


### 97. [Self-Conditioning Enables Deep Sequential Reasoning in Flow Matching](https://arxiv.org/abs/2610.19628)

**<font color=#1a73e8>作者：</font>** Zeyang Zhang, Linxiang Gao, Meiqi Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work has explored visual reasoning through image generation, where models solve visual-reasoning problems by directly generating solution images. Intuitively, iterative samplers such as flow matching are well suited to this task, since each sampling step may resemble one reasoning step. However, in this work, from a circuit complexity perspective, we show that this intuition is misleading. We prove that as long as the model outputs satisfy certain mild regularity conditions, the trajectory of the vanilla flow-matching sampler can be simulated by a constant number of sequential rounds of parallel model evaluations. Consequently, additional sampling steps cannot increase the expressive power of a constant-depth backbone model under the standard complexity-theoretic model of transformers. We then reveal that self-conditioning, which conditions the model on the previous step's estimate of the final image, plays a previously unrecognized role in removing this bottleneck. Controlled experiments on diverse visual-reasoning tasks show that flow matching with self-conditioning achieves higher accuracy and greater reasoning depth than vanilla flow matching, and its performance improves with more sampling steps. Theoretically, we prove that with self-conditioning, a constant-depth backbone can achieve expressive power equivalent to that of space-bounded Turing machines. Our study suggests a design principle for future visual reasoning research: carry more information between sampling steps, so that additional steps translate into deeper reasoning.

---


### 98. [Synthetic reaction data from transformation rules for graph-to-sequence pretraining in biodegradation pathway prediction](https://arxiv.org/abs/2610.19640)

**<font color=#1a73e8>作者：</font>** Irsyaad Rijwan, Liam Brydon, Aidan Jared 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The scarcity of observed biodegradation reactions constrains the training of product and pathway predictors. We present enviGraph, a framework that generates and curates synthetic reaction data, uses these data to pretrain a graph-to-sequence predictor, and fine-tunes the predictor on observed environmental reactions for product and recursive pathway prediction. Applying inherited environmental transformation rules to structures from PubChem, NORMAN SusDat and EPA DSSTox, followed by curation, produces 776,851 canonical parent-product pairs for pretraining. We compare this dataset with three United States Patent and Trademark Office (USPTO) reaction datasets: USPTO-50K, USPTO-MIT and USPTO-Stereo. We evaluate enviGraph and the sequence-based enviFormer using ten folds split by pathway on the EAWAG Biocatalysis/Biodegradation Database (BBD), regulatory pesticide biodegradation data (Soil) and activated-sludge biodegradation data (Sludge). For both predictors, synthetic pretraining gives the highest BBD mean precision-recall area under the curve (PR-AUC) among the evaluated pretraining datasets for single-generation and multi-generation prediction. enviGraph achieves BBD single-generation PR-AUC of $0.202 \pm 0.050$ with synthetic pretraining, compared with $0.169 \pm 0.065$ for the retrospectively selected strongest USPTO condition, USPTO-Stereo (mean $\pm$ sample standard deviation across folds). Its exact BBD top-1 and top-5 accuracies with synthetic pretraining are 0.355 and 0.594. The strongest USPTO conditions give higher PR-AUC means than synthetic pretraining in most Soil and Sludge comparisons. enviGraph has higher Soil multi-generation PR-AUC means than enviFormer under each of the four main pretraining datasets, and with synthetic pretraining it also leads enviFormer on BBD single-generation PR-AUC and exact top-1 and top-5 accuracy.

---


### 99. ["The Rose Garden Is a Cemetery": Spatial Dissonance and Divergent Public Experiences of an Indigenous Augmented Reality Tour](https://arxiv.org/abs/2610.19641)

**<font color=#1a73e8>作者：</font>** Grace Fujii, Vittorio Murtas, Sarah Sallee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Community-authored augmented reality (AR) can contest dominant heritage narratives by juxtaposing stories with physical surroundings. We examine the Thámien Ohlone AR Tour, developed with members of the Ohlone Native American community at Mission Santa Clara and Santa Clara University. Combining paired pre/post surveys from 57 participants with collaborative thematic analysis, we compare reception among Ohlone community members, university affiliates, and Mission visitors. Spatial dissonance captures felt tensions when AR challenged familiar campus readings or when surroundings conflicted with Ohlone histories the AR affirmed, such as a garden's significance as a burial ground. Cultural frames shaped interpretation; contemporary people and relationships made Ohlone continuance tangible. Participants appreciated the tour and called for permanent physical acknowledgment. We propose staging reflective encounters, clarifying community-authored meanings, and using AR to prototype public acknowledgment and support community-directed advocacy. These findings foreground relationships to land and place, informed by Indigenous scholarship, in designing and evaluating AR.

---


### 100. [Mapping Arctic Polynyas from Sea Ice Concentration Data Using Hierarchical Partitioning and Differentiated Region Growing: Sensitivity to Threshold and Product Choices](https://arxiv.org/abs/2610.19647)

**<font color=#1a73e8>作者：</font>** Tianyu Zhang, Haiyi Ren, Zhilun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately delineating Arctic coastal polynyas from sea ice concentration data remains challenging because of complex coastal geometry and spatially heterogeneous ice conditions. We develop a daily sea ice concentration (SIC) mapping framework based on hierarchical partitioning, connected-component analysis, and differentiated region growing for polynya and open-water regions. Applied to September-May ice seasons from 2002/03 to 2024/25, the framework achieves a mean overall accuracy of 96.74% and a mean kappa coefficient of 0.93 in the 63-scene visual assessment. Sensitivity experiments reveal a consistent pattern: the absolute magnitude of SIC-defined polynya extent is strongly configuration-dependent, whereas major temporal features are comparatively more stable. Relative to a 75% upper SIC threshold, seasonal extent integrals differ by 13.48%, 32.47%, and 65.04% at thresholds of 80%, 85%, and 90%, respectively, while the broad interannual structure remains recognizable. The response is also strongly regional and seasonal, with the largest threshold sensitivity in the Central Arctic Ocean, very weak sensitivity in the Gulf of St. Lawrence, and greater pan-Arctic curve separation from January onward. At an 80% threshold, product-comparison MAPE is 68.19% between the 6.25 and 25 km products and 11.47% between the 12.5 and 25 km products under their respective comparison periods and reference definitions. Regional product disagreement is likewise heterogeneous. Together, these results show that reproducible long-term polynya monitoring requires a fixed and explicitly documented combination of SIC product, threshold, and spatial classification rules, while broad temporal patterns can remain informative even when absolute extent differs substantially.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-264](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
