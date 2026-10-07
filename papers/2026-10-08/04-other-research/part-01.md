# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

---

### 1. [TEMPEST: Temporal Embeddings for Scalable Driver Identification via Angular Margin Learning](https://arxiv.org/abs/2610.06855)

**<font color=#1a73e8>作者：</font>** Kyle Musgrove, Dylan B. Lewis, Sarah Powers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalable driver identification requires embedding models that maintain discriminative performance as fleet size grows, yet existing triplet-loss formulations degrade rapidly with driver pool size and overfit to session-specific patterns under rigorous temporal evaluation. We introduce TEMPEST, a Temporal Convolutional Network embedding model trained with an additive angular margin (ArcFace) loss that enforces global class-level separation in a normalized angular space. TEMPEST maps 60-second multimodal driving windows to compact 96-dimensional embeddings, supporting truly dynamic enrollment without any retraining or classifier refitting. Under rigorous temporal evaluation on a 45-driver dataset, TEMPEST achieves 91.71% Rank-1 accuracy, outperforming the best classical model by 17.9 pp and the strongest triplet-loss baseline by 58.4 pp. TEMPEST degrades by only 4.3 pp when growing the subject pool from 10 to 45 drivers, compared to 22 pp and 32.5 pp for supervised and unsupervised triplet-loss baselines, and its cross-session advantage is corroborated on the public KIA Soul dataset, where it outperforms the best classical model by 7.3 pp within-session and 14.3 pp cross-session. With 720K parameters, a 2.80 MB footprint, and 50-epoch convergence, TEMPEST establishes a rigorous, reproducible baseline for scalable behavioral driver biometric identification.

---


### 2. [Neutrosophic Ensemble Classification for Uncertainty-Aware Bearing Fault Detection: Evidence from Laboratory and Variable-Speed Industrial Benchmarks](https://arxiv.org/abs/2610.06880)

**<font color=#1a73e8>作者：</font>** Maikel Leyva-Vazquez, Dayron Rumbaut Rangel, Lorenzo Cevallos-Torres 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning classifiers for bearing fault detection produce scalar confidence scores that conflate confident errors with genuinely ambiguous predictions, and the conventional truth/falsity pair (F = 1 - T) is algebraically redundant by construction. We operationalize a refined neutrosophic decomposition of a Random Forest + XGBoost + Logistic Regression ensemble into four indicators -- T-hat (top-class evidence), F-hat (best-competitor evidence), predictive entropy I1-hat, and decision disagreement I2-hat -- evaluated on two bearing benchmarks (CWRU and JNU, 600-1000 rpm) under a leave-one-condition-out protocol. On CWRU, after correcting a file-to-class mapping error, the ensemble reaches 100.00 percent accuracy on three of four held-out loads (92.27 percent on the fourth), leaving too few errors for uncertainty analysis. On JNU, holding out 1000 rpm, accuracy collapses to 40.64 percent, below a majority-class baseline; Logistic Regression (57.91 percent) generalizes far better than the tree ensembles. I1-hat shows a robust association with error beyond T-hat/F-hat, while I2-hat contributes little; standalone Logistic Regression confidence outperforms the full decomposition, a boundary condition we report honestly. Two further results extend this: fusing a time-domain and a frequency-domain model of the same signal and scoring their Jensen-Shannon divergence beats that model own entropy (AURC 0.29 vs. 0.36 on the standard split; 0.54 vs. 0.73 under a harder single-condition reproduction), the only indicator moving correctly under a CWRU-versus-JNU distributional-shift contrast; and, on CWRU alone, literature-verified bearing fault frequencies, correctly demodulated via the envelope spectrum, separate most fault classes almost perfectly (99.57 percent) using three interpretable features. Code, logs, and figures are released for independent verification.

---


### 3. [Comparative review of hybrid forecasting models for short-term prediction of building thermal load](https://arxiv.org/abs/2610.06881)

**<font color=#1a73e8>作者：</font>** Nikolaos A. Efkarpidis, Despoina Kothona, Georgios C. Christoforidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, a comparative review of different hybrid models for short-term forecasting of building thermal demand is carried out. Particularly, the assessment tackles the comparison of data-driven models enhanced with other state-of-the-art techniques. At the first step, the existing techniques reported in the literature are analysed. It is concluded that Metaheuristics or a data-driven model are used to identify the parameters of the basic model. The qualitative evaluation includes for each method the input and output features, main advantages and drawbacks. At the second step, an existing dataset of historical thermal demand from Scottish households, as well as historical weather forecasts are utilized to assess additionally the performance of existing hybrid methods. From the assessment of 13 hybrid methods, the Empirical Modal Decomposition - long short-term memory - Markov (EMD-LSTM-Markov) model can predict with the highest accuracy the day-ahead power pattern of heating and domestic hot water (DHW) demands. Though local power peaks are also accurately predicted, high power swells and spikes are underestimated. Other methods, such as Support Vector Machine - Simulated Annealing (SVM-SA) and Random Forest - Improved Sparrow Search Algorithm - LSTM (RF-ISSA-LSTM) predict a smooth pattern of heating and DHW demand profiles with rapid changes underestimating most power peaks.

---


### 4. [Learning When to Refine: Long-Horizon Reinforcement Learning for Budgeted Neural-Operator PDE Solvers](https://arxiv.org/abs/2610.06883)

**<font color=#1a73e8>作者：</font>** Ange Tong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide fast surrogates for time-dependent PDEs, but autoregressive deployment creates a refinement-allocation problem: prediction errors vary over space and time, while only a finite number of local corrections can be committed along a trajectory. We formulate this as budgeted adaptive neural-operator solving. A global Fourier neural operator advances the full field, a local operator proposes patch-wise residual corrections, and a set-aware selector chooses where to refine. A macro policy decides when and how much of the remaining refinement budget to spend. We introduce rollout-verified policy improvement (RV-PI), which evaluates feasible refinement counts through actual continuation rollouts of the learned PDE solver, converts long-horizon advantages into conservative policy targets, and accepts an update only when held-out trajectory error improves. On the shallow-water benchmark with a 32-intervention budget, RV-PI achieves a three-seed mean trajectory relative L2 error of 0.6910, improving over immediate-only policy improvement by 5.37% and RandomMacro by 2.41%. On the forcing-driven Brusselator benchmark with a 76-intervention budget, RV-PI attains 0.09954, improving over immediate-only policy improvement by 2.31% and RandomMacro by 5.32%. These results show that, under a fixed refinement budget, the value of a local correction depends on its downstream effect on the autoregressive trajectory, not only on its immediate error reduction.

---


### 5. [Event-Driven ML Pipeline Orchestration for Manufacturing: An AWS Industry Experience](https://arxiv.org/abs/2610.06890)

**<font color=#1a73e8>作者：</font>** Zhengyang, Thomas Cook, Fredaljohn Rohrbaugh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an industry experience report on three years of operating an event-driven cloud infrastructure for continuous machine learning training in automotive manufacturing. Our system orchestrates GPU-accelerated training of product-specialized model pairs, a physics prediction model and a reinforcement-learning control policy, across multiple plants, coordinating long-running GPU workloads triggered by manufacturing events. The architecture combines Amazon ECS with EC2 GPU capacity providers, SQS-based messaging with dead-letter queues, and an admission-controlled Lambda dispatcher that enforces cluster concurrency limits. A Conductor orchestrator on ECS Fargate initiates dependency-aware retraining chains on a weekly schedule. The entire infrastructure is codified in modular Terraform with multi-account separation. From 40000+ production training jobs we report a 72-78% cost reduction versus always-on GPU infrastructure. A discrete-event simulation confirms that admission control is necessary (naive dispatch loses 65% of jobs) and that queue-draining matches AWS Step Functions latency while eliminating per-job startup overhead. We provide lessons learned and release the simulator and Terraform module skeletons as open-source artifacts.

---


### 6. [DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections](https://arxiv.org/abs/2610.06898)

**<font color=#1a73e8>作者：</font>** Li Hu, Kanghua Mo, Yingbin Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As GUI-based mobile agents rapidly progress, rigorous safety evaluation of their autonomous decision-making in realistic app interfaces becomes increasingly critical. Existing benchmarks mainly focus on execution-level anomalies using task success or hijack rates, but fail to capture the in-task goal deviation risk in multi-candidate selection tasks, where the decision may be steered toward an attacker-specified target, even in violation of instruction-implied constraints (e.g., cheapest/highest-rated), without any overt execution anomalies. We present DIBench, a decision integrity benchmark for measuring this risk in mobile agents. DIBench covers 7 commercial and 3 simulated apps with 5 task types. Under a threat model restricted to non-privileged UI content, we construct 8 deceptive injection probe instantiations that can steer critical selections without overt anomalies. The benchmark includes 1,000 clean and 36,672 injected instances, with a unified protocol and integrity metrics for comparison. Experiments spanning 4 agent frameworks and 7 base models show that completion-based evaluation can overestimate agent trustworthiness and miss decision-integrity risks: deceptive injections steer selections and shift early action policies, inflating completion rates and creating a misleading illusion of safety. Common defenses, including detection, image preprocessing, and prompt reminders, yield inconsistent integrity gains. Overall, DIBench provides a unified, reproducible benchmark to quantify the risk of in-task goal deviation in mobile agents and enable comparable evaluations of safety defenses.

---


### 7. [Text2Dashboard: A Governed Agent Architecture for Natural-Language Dashboard Generation over Enterprise DataBrain](https://arxiv.org/abs/2610.06914)

**<font color=#1a73e8>作者：</font>** Yiou Wu, Zezhi Tang, Ningwei Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text2Dashboard is a DataBrain-specific prototype that turns natural-language analytic requests into inspectable dashboards. An installable Codex plugin and standalone Agent Runtime combine schema-constrained model decisions with typed tools, persistent state, and deterministic Hooks for approval, audit, checkpointing, recovery, and failure handling. The pipeline resolves entities, discovers metadata, enforces read-only SQL, composes dashboards, and applies static checks, dynamic preflight, and browser inspection. The model proposes actions while deterministic software controls execution and records state transitions.
We evaluate the workflow on frozen real-DataBrain tasks and controlled Hook faults. Strict success was 6/8 on metadata and SQL tasks: metadata selection passed 4/4, all four SQL tasks met semantic criteria, and 2/4 met the exact output-column contract. The final release passed 4/4 single-panel dashboard tasks, one two-panel task, and one existing-dashboard refinement; a parameterised task exceeded its step limit. All ten fault scenarios met their specified outcomes without unapproved external side effects. Model inference accounted for over 97\% of observed runtime in every reported group. These small, DataBrain-specific results do not establish production readiness, general text-to-SQL accuracy, or an efficiency advantage over manual dashboard construction.

---


### 8. [Learning from Unreliable Trajectories: Adversarially-Robust Federated Q-Learning](https://arxiv.org/abs/2610.06918)

**<font color=#1a73e8>作者：</font>** Sreejeet Maity, Aritra Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study federated reinforcement learning in which multiple agents interact with a common Markov decision process and communicate through a central server to collaboratively learn the optimal state-action value function. Our goal is to understand whether the sample-efficiency benefits of collaboration can be retained when a fraction of the agents behave adversarially and transmit arbitrarily corrupted information. To address this problem, we introduce Robust Async-Fed-Q, an epoch-based federated learning algorithm that combines variance-reduced estimation of the Bellman optimality operator at the agents with robust aggregation at the server. We establish high-probability finite-time guarantees showing that the proposed method preserves the statistical gains of collaboration among the honest agents while tolerating adversarial corruption. In particular, the effect of the adversarial agents decreases as the amount of data collected by each honest agent grows and eventually vanishes in the infinite-sample limit. We complement these guarantees with information-theoretic lower bounds that characterize the unavoidable statistical cost of adversarial corruption, leading to the first nearly matching upper and lower bounds for adversarially robust federated reinforcement learning. We further extend our framework to accommodate single-trajectory Markovian sampling and heterogeneous partial coverage, where different agents may explore different regions of the state-action space and learning relies on their collective coverage. Finally, our epoch-based design substantially improves the best known communication complexity for federated Q-learning under asynchronous sampling.

---


### 9. [Anchor Divergence for Semantic Geometry in Contrastive Learning](https://arxiv.org/abs/2610.06919)

**<font color=#1a73e8>作者：</font>** Akash Kannan, Kiho Park, Victor Veitch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper concerns how semantic context determines geometry in learned vector representations. Similarity is typically measured using cosine similarity, which provides a single fixed geometry. Semantic similarity, however, is inherently context dependent: two images may be similar because they depict the same object, share a visual style, or are relevant to the same clinical finding. We show that contrastive representations naturally encompass a family of geometries that can be specialized to particular semantic structure. The key idea is to use an interplay between contrastive learning, exponential families, and information geometry to establish a correspondence between probability distributions over "anchors" and Bregman geometries on the representation space. We use this correspondence to define "Anchor Divergences", a method for specifying context-specific semantic geometries on fixed representations. Under this correspondence, modeling the anchor distribution models the geometry itself. Experiments on retrieval show that anchor divergences provide an effective and efficient way to specify context-specific semantic similarity.

---


### 10. [Metonymic Circuits for Abstract Concept Grounding in Vision Transformers](https://arxiv.org/abs/2610.06928)

**<font color=#1a73e8>作者：</font>** Jing Ding, Ziqiao Ma, Jiayuan Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how Vision Transformers ground abstract concepts (e.g., angry) when training data provide limited direct referential evidence. We hypothesize a metonymic grounding mechanism in which abstract predictions are driven by concrete, interpretable anchor concepts (e.g., fire) that bridge visual signals to abstract semantics. By applying Transcoders on CLIP and DINO vision encoders, we recover intermediate features that can be associated with semantic labels for more concrete concepts, and trace their contributions in circuits underlying abstract concept recognition. Experiments on a carefully curated icon dataset reveal structured metonymic circuits, in which perceptual primitives dominate early layers and object-like anchors precede abstract targets. Images containing rendered text instead recruit a distinct perceptual-to-textual route. Causal interventions further validate that metonymic intermediates are functionally involved in grounding abstract concepts.

---


### 11. [Near-Optimal Sample Complexity for Recursive Entropic Risk Reinforcement Learning with a Generative Model](https://arxiv.org/abs/2610.06931)

**<font color=#1a73e8>作者：</font>** Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the sample complexities of value and policy learning in finite discounted Markov decision processes (MDPs) under recursive entropic risk preferences with risk parameter \(\beta\neq 0\), assuming access to a generative model of the MDP. We provide a refined analysis of model-based risk-sensitive Q-value iteration (MB-RS-QVI), a plug-in model-based method introduced in prior work, and derive \((\varepsilon,\delta)\)-PAC guarantees for both learning the optimal \(Q\)-value function and an \(\varepsilon\)-optimal policy. Our bounds improve the exponential dependence on the effective horizon \(1/(1-\gamma)\) compared with the best existing guarantees for this setting. In particular, they match the existing lower bounds in their exponential dependence on \(|\beta|/(1-\gamma)\), as well as in \(S\), \(A\), \(\varepsilon\), and \(|\beta|\), up to logarithmic factors. Consequently, our analysis removes the exponential gap between the previously known upper and lower bounds, leaving only a polynomial gap in the effective horizon.

---


### 12. [UniPro: Unified Multi-Mode Medical Image Segmentation from 2D Images to 3D Volumes via Propagation](https://arxiv.org/abs/2610.06938)

**<font color=#1a73e8>作者：</font>** Bangwei Guo, Yunhe Gao, Meng Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation remains fragmented along two axes: segmentation paradigms and data dimensionality. Existing methods are typically developed separately for semantic, in-context, and interactive segmentation, and are further specialized to either native 2D images or 3D volumetric data. In clinical practice, however, segmentation workflows take many forms: a case may be initialized by semantic prediction, reference-guided segmentation, or user interaction. Regardless of how it begins, fine-grained refinement is naturally performed on 2D views; for volumetric scans, such 2D edits must propagate coherently to the rest of the volume. We present UniPro, a unified model that bridges segmentation paradigms and data dimensionality, using propagation to extend 2D segmentation to 3D volumes. Our key insight is that volumetric propagation and in-context segmentation share the same reference-conditioned prediction mechanism, differing only in whether the reference image-mask pairs come from other cases or from previously segmented neighboring slices. Building on this view, UniPro supports semantic, in-context, interactive, and propagation-based segmentation within a single slice-based framework, using class priors, reference exemplars, user clicks, and neighboring-slice predictions as mode-specific conditioning inputs. To improve propagation reliability, UniPro further incorporates bidirectional and 3D supervision to regularize slice-wise propagation beyond per-slice losses. Extensive experiments across diverse modalities and anatomies show that UniPro achieves strong performance across all segmentation settings, enabling annotation-efficient 3D segmentation from sparse 2D initialization and reducing slice-by-slice correction effort.

---


### 13. [Learning to Remember: Distilling Memory Retention for Compact Recurrent Neural Networks](https://arxiv.org/abs/2610.06942)

**<font color=#1a73e8>作者：</font>** Nilushika Udayangania, Kishor Nandakishora, Marimuthu Palaniswami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models, particularly recurrent neural networks and their variants, such as long short-term memory, have significantly advanced time series analysis. These models capture complex, sequential patterns in time series, enabling real-time assessments. However, their high computational complexity and large model sizes pose challenges for deployment in resource-constrained environments, such as wearable devices and edge computing platforms. Knowledge Distillation (KD) offers a solution by transferring knowledge from a large, complex model (teacher) to a smaller, more efficient model (student), thereby retaining high performance while reducing computational demands. Current KD methods, originally designed for computer vision tasks, neglect the unique temporal dependencies and memory retention characteristics of time series models. To bridge this gap, we propose a novel KD framework termed Memory-Discrepancy Knowledge Distillation (MemKD). MemKD leverages a specialized loss function to capture memory retention discrepancies between the teacher and student models across subsequences within time series data, ensuring that the student model effectively mimics the teacher's behaviour. This approach facilitates the development of compact, high-performing recurrent neural networks suitable for real-time, time series analysis tasks. We provide additional experiments, in-depth theoretical analysis, and insights into the proposed framework across extended time series benchmarks. Our experiments demonstrate that MemKD significantly outperforms state-of-the-art KD methods. Additionally, we demonstrate that it can match the teacher model's performance across a wide range of compression levels, achieving notable reductions in parameter count and memory usage without a significant loss in accuracy.

---


### 14. [Beyond the Linear Representation Hypothesis: Non-Linear Activation Steering in Text-to-Image Models](https://arxiv.org/abs/2610.06945)

**<font color=#1a73e8>作者：</font>** Muhammad Atif Butt, Paweł Skierś, Joost Van De Weijer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability often relies on the Linear Representation Hypothesis (LRH), which assumes that high-level concepts are encoded as linear directions in activation space. Yet a natural visual concept does not necessarily require a linear visual transition: between sunny and stormy lies an intermediate weather state such as a sky with a few white clouds, not simply a weaker storm; between a caterpillar and a butterfly, the progression is not a caterpillar with continuously growing wings. This raises the question of whether such true intermediate states are also represented nonlinearly by the model. Indeed, when we prompt text-to-image models directly for intermediate attributes, their activations rarely fall along the straight direction connecting the endpoints. Therefore, we propose KANSteer, which models concept traversal as a curve passing through its intermediate states. Seeking a representation that is both simple and interpretable, we propose to use Kolmogorov-Arnold Networks (KANs), which provide a one-dimensional coordinate whose learned functions define the trajectory. This allows the steering direction to vary along the concept while preserving an interpretable representation. Across several concepts and text-to-image diffusion transformers, we find that their activation trajectories substantially deviate from straight lines, and that KANSteer provide a closer fit and smoother traversal of intermediate attributes than linear steering.

---


### 15. [Do Neural PDE Solvers Learn the Right Dynamics?](https://arxiv.org/abs/2610.06952)

**<font color=#1a73e8>作者：</font>** Haonan Li, Yue Song, Bin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE solvers can achieve low prediction errors, but do they reproduce the dynamics of the systems they model? Prediction scores alone offer an incomplete answer: they measure agreement with reference solutions but provide limited insight into how errors accumulate, nearby states diverge, or extreme events arise. We propose an evaluation framework that directly examines these behaviors in deterministic and stochastic neural solvers. By evolving ensembles of nearby initial states and comparing them with direct numerical simulation, we assess three complementary aspects of learned dynamics: error formation, ensemble geometry, and extreme events. Experiments on two-dimensional Kolmogorov flow reveal limitations that conventional scores can obscure. Smaller trajectory errors can reflect weaker error amplification despite less accurate local updates. Models can match an ensemble's overall spread and effective dimension while failing to capture the spatial directions where nearby states diverge. Similarly, matching overall event frequencies can conceal failures to predict persistent extreme events. These findings show that improved prediction accuracy does not necessarily imply greater dynamical fidelity. Our framework makes this distinction measurable, providing concrete criteria for evaluating whether advances in neural PDE solvers better capture the underlying dynamics.

---


### 16. [DistScene: Object-to-Scene Distillation for 3D Scene Generation](https://arxiv.org/abs/2610.06960)

**<font color=#1a73e8>作者：</font>** Kunming Luo, Hongyu Yan, Ken Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DistScene, a framework for single-image compositional 3D scene generation by jointly modeling the environment and individual objects. Unlike existing methods that represent scenes primarily as collections of objects, we model the environment as an explicit scene component to provide geometric context for object placement. Specifically, we introduce Scene-Frame Generation, which jointly generates separate environment and object components in a shared coordinate frame, allowing their geometry and relative placement to be learned together. Then we introduce Object-Centric Refinement to refine each object in a local frame with scene context. Finally, we develop Object-to-Scene Distillation to transfer pretrained object-generation priors to scene generation through automatically composed and rendered synthetic scenes. Evaluations on indoor and outdoor benchmarks demonstrate improved scene-level spatial coherence over the evaluated baselines. Project page: this https URL

---


### 17. [EVFormer: An Egocentric Vision-EMG Bidirectional Attention Model for Bimanual Hand Pose Estimation](https://arxiv.org/abs/2610.06970)

**<font color=#1a73e8>作者：</font>** JiaCheng Ge, SiYu Zhang, ShengJie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Egocentric bimanual hand pose estimation is important for virtual interaction, wearable control, and rehabilitation, but visual observations are often degraded by self-occlusion, hand-hand contact, and object manipulation. We propose EVFormer, a multimodal framework that combines the current RGB frame with the preceding 200 ms of bilateral wrist surface electromyography (sEMG) to estimate 44 finger and wrist joint angles. EVFormer separately encodes visual spatial features and sEMG temporal features, enables cross-modal information exchange through sequential bidirectional cross-attention, and integrates the two modalities using feature-wise gated fusion. We evaluate EVFormer in a single-participant feasibility study using one synchronized public EgoEMG recording with chronologically separated training, validation, and test splits. On 296 test samples, EVFormer achieves a mean absolute error of 11.482 degrees, compared with 13.228-13.610 degrees for vision-only, sEMG-only, late-fusion, and training-mean baselines. This corresponds to relative error reductions of 13.20% compared with the vision-only model and 14.23% compared with late fusion. EVFormer also achieves the lowest error in four of the five evaluated gesture classes. These results provide preliminary evidence that feature-level interaction between egocentric vision and sEMG can improve bimanual hand pose estimation. Further evaluation across participants, recording sessions, sensor placements, and real-world interaction conditions is required to establish the generalizability of the approach.

---


### 18. [Event Cameras for Melt-Pool Monitoring in Additive Manufacturing: A Benchmark and a Cross-Machine Transfer Analysis](https://arxiv.org/abs/2610.06973)

**<font color=#1a73e8>作者：</font>** Mohamad Yazan Sadoun, Sarah Sharif, Yingtao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Melt-pool monitoring is central to qualifying metal additive manufacturing (AM), yet no public event-camera benchmark exists for this domain. Event cameras report per-pixel brightness changes with microsecond timing instead of reading full frames, giving the temporal resolution AM transients demand at a fraction of the data rate. We present SynAM-E (Synthetic AM Events), the first public multi-source simulated event-camera benchmark for metal-AM melt-pool monitoring: 85 physics-calibrated event shards from 15 sources across 8 institutions, with public baselines and fixed cross-machine evaluation splits. On a single-machine case study, event-spatial monitoring matches dense-frame accuracy (0.874 versus 0.863 macro-F1), and the absolute intensity that events discard adds only +0.006 under fusion. On the NIST Additive Manufacturing Metrology Testbed (AMMT) build, a near-sensor event-rate counter recovers a raw-frame-confirmed 528.7 Hz intensity oscillation at ~380 times less sensor readout than the frame stream requires. A compact 93 k-parameter spiking model runs at 15 times lower modeled inference energy for a 0.073 macro-F1 cost. Every cross-source task includes a built-in trust test against camera identity shortcuts: process-type classification passes while material classification remains confounded by camera band, a corpus-structural limitation the release documents and the trust test exposes.

---


### 19. [Uncertainty in Representation Learning on Knowledge Graphs](https://arxiv.org/abs/2610.06974)

**<font color=#1a73e8>作者：</font>** Yuqicheng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph embedding (KGE) methods represent entities and predicates in continuous vector spaces to infer missing knowledge. Despite strong benchmark performance, their predictions often lack principled reliability guarantees, limiting their use in high-stakes applications. Moreover, uncertainty arises throughout the KGE pipeline, from incomplete or probabilistic input knowledge to stochastic training and prediction. This thesis systematically investigates three sources of uncertainty in KGE: knowledge uncertainty, arising from incomplete, noisy, or probabilistic input knowledge; algorithmic uncertainty, induced by randomness in model training; and predictive uncertainty, concerning the reliability of model outputs. To address algorithmic uncertainty, the thesis demonstrates that models trained under identical settings can produce substantially different predictions and introduces a voting-based aggregation framework to mitigate this instability. To quantify predictive uncertainty, it adapts conformal prediction to KGE, constructing answer sets with distribution-free coverage guarantees and extending them to provide predicate-conditional reliability guarantees. To support reasoning under knowledge uncertainty, it develops statistically valid prediction intervals for confidence-scored triples and an embedding-based approach to approximate probabilistic reasoning over statistical ontologies with formal soundness guarantees. Together, these complementary, model-agnostic methods provide a practical and theoretically grounded approach to uncertainty in KGE, advancing beyond predictive accuracy toward reliable and uncertainty-aware knowledge graph reasoning.

---


### 20. [Hierarchy-GBP: Accelerating Factor Graph Inference via Abstraction and Recovery](https://arxiv.org/abs/2610.06978)

**<font color=#1a73e8>作者：</font>** Yuzhou Cheng, Tom Yates, Ignacio Alzugaray 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Belief Propagation (GBP) is a distributed inference algorithm that passes messages in graphical models, making it attractive for scalable spatial intelligence. However, we find GBP most effective locally: it rapidly smooths message errors that vary sharply between neighbor variables, but corrects global errors across distant graph regions incrementally through long-range message propagations. We propose Hierarchy-GBP (H-GBP), an iterative, two-stage framework that accelerates GBP by first solving these global errors with a coarse graph approximation (abstraction) and projecting the results back to the original graph (recovery), then refining the remaining local errors with GBP. We prove H-GBP convergence to the optimum by deriving the combined matrix operator of our abstraction and recovery steps and analyzing its spectral radius. Experiments on linear sparse graphs show that H-GBP converges fundamentally faster than standard GBP. Moreover, we validate H-GBP on two important spatial problems: Pose Graph Optimization (PGO) and Bundle Adjustment (BA). H-GBP markedly accelerates large-scale PGO and achieves state-of-the-art runtime across all tested BA scales.

---


### 21. [EPOCH: Reliable Discovery through Evidence-Governed Search](https://arxiv.org/abs/2610.06986)

**<font color=#1a73e8>作者：</font>** Binjie Guo, Aisheng Mo, Ruitong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI research agents are increasingly used to search over programs, mathematical constructions, and proofs. However, existing systems typically optimize evaluator feedback without adequately governing how that feedback is interpreted, challenged, and reused. As a result, promising but fragile candidates can be promoted as discoveries, while benchmark improvements, finite certificates, and theorem-level claims are too easily conflated. We introduce EPOCH, an evidence-governed architecture designed to close this gap. EPOCH implements an evidence-governed discovery loop by combining explicit task contracts, typed memory, active falsification, admission checks, and independent replay, so that each candidate is evaluated against the strength and scope of the claim it supports. EPOCH achieves state-of-the-art aggregate performance on AlgoTune, substantially exceeding the strongest baseline in mean normalized score (0.65 vs. 0.53), and attains the highest mean score on the internal Math14 suite (0.57). It further shows favorable held-out behavior under official-test replay and leads the descriptive aggregate on AgentHPO. Across ten discovery problems, EPOCH delivers substantial task-specific advances, including improved executable constructions, optimized algorithms, counterexamples, and proof-supported results. These advances demonstrate its ability to convert search into concrete progress across mathematical and computational domains. Together, the results suggest that evidence governance is a necessary step toward AI research agents that produce not only stronger solutions, but also more trustworthy scientific discoveries.

---


### 22. [An Information-Theoretic Evaluation Framework for Benchmark and Model Diagnosis in Knowledge Tracing](https://arxiv.org/abs/2610.06988)

**<font color=#1a73e8>作者：</font>** Houru Jiang, Zixi Wang, Tengteng Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) models are predominantly evaluated using aggregate metrics such as area under the curve (AUC) and accuracy. However, these global scores obscure where the remaining errors originate and fail to indicate whether a benchmark is approaching saturation. While estimating a global theoretical performance limit is challenging in realistic KT settings, it is possible to quantify local predictability. To address this, we propose an information-theoretic evaluation framework for KT benchmark diagnosis. We use Context Tree Weighting (CTW) on item-response histories and current-item queries as an operational causal uncertainty coordinate, while distinguishing it from the unobserved Local Irreducible Uncertainty (LIU) under the full KT information set. By projecting predictions onto this shared uncertainty coordinate, we evaluate model performance gains across distinct entropy bands rather than only at the global level. Comprehensive evaluations on NIPS Task 3/4 and Algebra 2005 reveal that model improvements are highly non-uniform. Modern KT models show substantial gains in high-entropy regions, and additional item-aware references, log-loss, and equal-frequency analyses support this localization. The framework also flags regions where apparent gains require checks for noise-sensitive behavior. By surfacing these local modeling failures alongside genuine gains, this approach provides a diagnostic tool for studying both residual predictive structure and the limitations of current KT benchmarks and models.

---


### 23. [Repair Lot Skyline: A Weighted Constraint Satisfaction Approach to Pavement Repair Optimization from Geospatial Hazard Density](https://arxiv.org/abs/2610.06989)

**<font color=#1a73e8>作者：</font>** Takato Yasuno, Keita Kobayashi, Ryuta Sakaguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pavement agencies must translate a spatially distributed distress inventory into a bounded, actionable repair-lot plan: accident-critical defects (potholes) must always be addressed, lower-risk defects (cracks) should be included only when their benefit justifies the repair cost, and historical patch locations signal re-degradation risk without themselves triggering repair. We formalize this as a Repair Lot Skyline problem: a Weighted Constraint Satisfaction Problem (WCSP) defined over chainage (distance along the road) rather than over time, so that it requires only a single-epoch distress survey and makes no claim about future deterioration. The WCSP identifies 143 candidate hazard clusters (61 hard, 82 soft), of which 106 are merged into a final repair plan totaling 1,997.4 m---83.7% of the 2,385.9 m that would be required if every soft candidate were included regardless of cost. This plan covers 100% of observed potholes (138/138) and 91.6% of observed cracks (404/441), capturing 93.6% (542/579) of the total hazard benefit available in the full candidate set. The skyline frontier shows pronounced diminishing returns beyond this point: the remaining 37 excluded soft candidates would add only 6.8% additional benefit for a 19.4% increase in repair length. We further formalize the minimum-lot-length $L_{\min}$ and historical-context radius $\kappa$ as a joint, four-objective hyperparameter search over this WCSP; on the same case study, the recommended configuration ($L_{\min} = 14.7$ m, $\kappa = 10$ m) reduces repair-crew mobilizations by 7.1% relative to an untuned default, at the cost of a 12.9% larger budget and a 1.1-percentage-point lower crack coverage.

---


### 24. [State-Aware Interaction MIL for Rare Joint Molecular Phenotype Prediction in Colorectal Cancer and Lung Adenocarcinoma](https://arxiv.org/abs/2610.06991)

**<font color=#1a73e8>作者：</font>** Dasari Naga Raju, Tripti Bameta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint molecular phenotype prediction is complicated by small joint-positive populations and overlapping histological features across alternative molecular states. Existing computational pathology approaches typically predict biomarkers independently or formulate the joint-positive phenotype as a binary endpoint. Independent prediction does not model interactions between biomarker-specific histological representations, whereas binary joint prediction collapses the double-negative and two single-positive configurations into a single negative class. We propose State-Aware Interaction MIL, a weakly supervised method that preserves biomarker-specific histological representations, models their interaction, and supervises the complete four-state molecular configuration. We evaluate the proposed approach for joint BRAF+/MSI+ prediction in colorectal cancer and EGFR+/TP53+ prediction in lung adenocarcinoma using frozen UNI2-h and CONCH pathology foundation-model representations. With UNI2-h, State-Aware Interaction MIL achieved an average precision of 0.5566 in colorectal cancer (joint-positive prevalence 6.8%) compared with 0.5161 for NaiveMTL, and 0.2784 in lung adenocarcinoma (joint-positive prevalence 8.6%) compared with 0.2525 for IndependentPair. With CONCH, State-Aware achieved an average precision of 0.4410 compared with 0.3932 for DirectJoint in colorectal cancer and 0.1659 compared with 0.1226 for DirectJoint in lung adenocarcinoma. These results indicate that pathology foundation-model representations contain predictive information for rare joint molecular phenotypes and that preserving biomarker-specific representations within a structured molecular-state formulation can improve prediction of these phenotypes from histopathology.

---


### 25. [When better traffic forecasts fail to improve signal control: a layered diagnostic study of forecast-to-decision value](https://arxiv.org/abs/2610.06992)

**<font color=#1a73e8>作者：</font>** Jianing Long, Xiaobin Li, Wuming Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improved traffic forecasts do not necessarily yield better signal-control decisions. We investigate this gap through a layered diagnostic study using 29 days of reconstructed demand from Xuancheng, China, with seven dates reserved for testing. The framework evaluates point forecasts, conformal intervals, dependence-aware scenarios, and matched closed-loop controllers. Entry-level and movement-level forecasts reduce mean absolute error by 4.03% and 3.92%, respectively, relative to historical means. A nominal 90% conformal interval achieves 90.72% marginal coverage but only 75.66% on an ex-post high-demand subset. Interface audits identify decision-time leakage and reveal that only two of nine controlled intersections offer multiple effective actions. We correct the temporal interface and compare causal forecasts with a five-second event oracle using exhaustive joint-action search. A synthetic positive control demonstrates that future information can reduce the internal rollout cost by 61.5%. On the frozen test dates, however, causal forecasts and the event oracle increase queue vehicle?seconds by 6.09% and 3.39% relative to the matched no-future rollout, while the oracle reduces spillback exposure by 3.78%; paired-day bootstrap intervals cross zero. These findings indicate that forecast value depends on temporal observability, action identifiability, dynamics consistency, and objective alignment. The proposed protocol provides a practical way to diagnose where predictive improvements fail to translate into operational benefits.

---


### 26. [TARE: Weigh a Never-Poisoned Twin Before Reading Backdoor-Defense Costs](https://arxiv.org/abs/2610.06994)

**<font color=#1a73e8>作者：</font>** Ruizhi Xu, Wei Xu, Sibo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor-defense leaderboards print a clean-accuracy drop and read it as removal cost. Measured on the poisoned victim alone, the drop cannot separate removal from what the defense does to any model, and inherits the victim's start, which for three of BackdoorBench's sixteen attacks is a configuration file: WaNet, BPP and Input-Aware ship a MultiStepLR that never fires, so their victims never anneal and are the least accurate in 30/31 public CIFAR cells at $\leq$5%. On PreAct-ResNet18, fine-tuning-family defenses return a low start to their own level, so there the published cost is negative, the benchmark's rating clips the "gain" to zero, and 2 of 48 citing defense papers we read rest a no-cost claim on those cells; TSBD and CGD, re-run with their code, "gain" on a never-poisoned model too. A $2\times2$ editing only that scheduler line isolates the cause, its swapped arms self-registered before they ran: the sign of the fine-tuning family's clean-model cost reverses both ways while its published gain on the annealed victim only shrinks toward zero, 44/44 seeds following the schedule, replicated on BPP, FT-SAM, CIFAR-100 and VGG19-BN and induced in a second toolkit. TARE runs the same defense on a never-poisoned twin of the same recipe, schedule and seed (on BackdoorBench, $\leq$10 poisoned images, admitted only below 5% attack success); what the twin loses is the tare. On the BadNets grid seven of eight defenses charge the twin (Neural Cleanse only where its detector fires), +0.13 (fine-tuning) to +5.70 points (I-BAU); the eighth, ABL, destroys it. Within an attack the start cancels from rankings, so the tare re-orders nothing there; what poisoning adds beyond it is printed under two estimators and not corrected, its removal share unidentified. We ship the three-key patch, a signed tare column (7 attacks $\times$ 8 defenses) and TARE-Z, a twin-free estimator for seed-stable defenses.

---


### 27. [Joint upper-bound coverage and route-choice utility: an empirical evaluation on two urban proxy tasks](https://arxiv.org/abs/2610.06995)

**<font color=#1a73e8>作者：</font>** Jianing Long, Xiaobin Li, Wuming Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether more accurate traffic forecasts or higher uncertainty coverage improve route decisions is unclear. We evaluate this question with a frozen protocol that separates speed error, joint candidate path upper bound coverage, route selection, and realized loss. Using processed road speed data from Beijing and Chengdu, we construct offline proxy tasks with 150 origin destination pairs, three candidate paths, and 14 test days per city. We compare raw 90th percentile path time bounds with jointly calibrated upper bounds under minimum bound route choice. Joint coverage rises from 83.19% to 92.26% in Beijing M1, from 75.14% to 88.33% in Chengdu M1, and from 74.01% to 90.64% in Chengdu M2. Yet C2 increases lateness by 0.1633, 0.7848, and 0.9200 percentage points, respectively, and mean travel time by 0.588, 3.082, and 4.418 seconds. In a separate Chengdu predictor comparison, a 14.91% reduction in speed mean absolute error accompanies a 1.4571 percentage point reduction in lateness under C0. Joint coverage is therefore not a surrogate for downstream route utility in these frozen tasks the offline results do not establish online or causal benefits.

---


### 28. [Should We Skip Diffusion?](https://arxiv.org/abs/2610.07002)

**<font color=#1a73e8>作者：</font>** Yiping Ji, James Martens, Simon Lucey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models learn semantic representations while generating images. In the Decoupled Diffusion Transformer (DDT), a condition encoder provides features that guide a velocity decoder in denoising. To enable effective denoising at all noise levels, these features must capture both high-level abstract structures and low-level details. However, skip/residual connections in the encoder allow shallow features to bypass successive transformations, which may limit progressive abstraction, or at least make it difficult to disentangle different levels of abstraction. We propose DDT-RFE, which removes the residual connections around the Self-Attention and MLP operations in each encoder block while maintaining stable training. To retain the information that abstraction discards but that the decoder still needs, we fuse the input patch embedding with intermediate and final encoder features to form the encoder output. The decoder thus has access to information from multiple encoder depths, while each encoder block is able to learn more abstract representations. DDT-RFE achieves overall improvements over DDT across visual understanding tasks, including image classification, semantic segmentation, object discovery, and semantic correspondence, while using fewer encoder blocks. It also achieves a lower FID for image generation on ImageNet.

---


### 29. [STOCK-JEPA: Prior-Anchored Latent Revision Representation Learning in Equity Markets](https://arxiv.org/abs/2610.07006)

**<font color=#1a73e8>作者：</font>** Yizhi Luo, Jiahe Yi, Jianhui Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning effective representations helps characterize the structure and dynamics of equity markets from financial data with a low signal-to-noise ratio. Black-box deep models can capture complex patterns but may overfit sample noise and lack explicit economic structure. Meanwhile, classic linear financial models provide interpretable references, but their oversimplified assumptions leave non-linear signals uncaptured. To combine the strengths of these two directions, we propose Stock-JEPA, a joint-embedding predictive framework that learns predictable incremental revisions relative to a point-in-time financial prior. First, we leverage a low-complexity financial model to produce fixed statistics summarizing multi-horizon return and risk. A prior projector then maps these statistics into the target encoder's latent space as an anchor. Second, we design a context-conditioned revision predictor to estimate the future representation's predictable displacement from the anchor. Separate losses update the two branches: the anchor learns from prior statistics, while the revision captures additional predictable information from historical context. Third, we freeze all representation modules and train a downstream readout, evaluating its forecasts through cross-sectional ranking and portfolio performance. Theoretically, we prove that optimal revision reduces the prior anchor's expected squared error for the same future representation by exactly $\mathbb{E}[\|\boldsymbol{\Delta}\|_2^2]$. This non-negative gain is the expected squared magnitude of the additional signal predictable from historical context. Experimentally, Stock-JEPA outperforms 13 strong baselines across large-scale China and U.S. equity universes on 5 key evaluation metrics. Ablation studies and representation analysis further demonstrate the value of the learned revisions for representation learning in equity markets.

---


### 30. [Learning to Curate What You Generate for Generalizable Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2610.07008)

**<font color=#1a73e8>作者：</font>** Junhui Yin, Yuchen Yang, Yilin Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot class-incremental learning (FSCIL) aims to learn novel classes from limited annotations while preserving prior knowledge. Existing methods typically assume a sufficiently large base session, but this assumption fails when both base and incremental data are scarce, leading to weak initial representations, semantic drift, and unstable boundaries. We study this underexplored yet realistic setting, termed Generalizable FSCIL (G-FSCIL), where the base session itself contains only a few classes. Although synthetic data can alleviate supervision scarcity, naively mixing generated samples often introduces semantic noise and exacerbates old-new boundary conflicts. To address this, we propose a framework that curates trustworthy synthetic knowledge for stable G-FSCIL. Specifically, we first construct class-specific synthetic candidate pools using a frozen latent diffusion model, where class inversion is performed at the first observation and the resulting condition embeddings are reused for on-demand generation. Building on these candidates, we learn a knowledge curation strategy that selects samples with both semantic consistency and visual diversity, and distill this process into a transferable selection policy during the base session, which is then reused without further optimization. Leveraging the curated synthetic data, we further design a boundary-stable incremental adaptation scheme, including synthetic-informed prototype initialization and bidirectional boundary calibration to mitigate old-new conflicts. Extensive experiments demonstrate that our method consistently outperforms existing FSCIL baselines, with reduced forgetting and improved balance between old and new classes. Code is available at this https URL.

---


### 31. [DTFormer: Text-Guided Semantic Alignment for RGB-D Segmentation](https://arxiv.org/abs/2610.07014)

**<font color=#1a73e8>作者：</font>** Ziang Wei, Yinlong Liu, Yan Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-D semantic segmentation has made notable progress by fusing RGB and Depth, yet mainstream models still learn features almost exclusively from pixel-level supervision, lacking direct high-level semantic constraints. This raises a central question-can external knowledge such as language priors inject stronger semantic discriminability into mainstream RGB-D segmentation models. We present DTFormer, a novel tri-modal (RGB-D-Text) semantic segmentation framework. At its core is Text-guided Semantic Alignment Module (TSAM) that first encodes textual cues into a set of semantic prototypes and then explicitly aligns multi-modal RGB-D features with these prototypes at multiple encoder and decoder layers. This design imposes strong semantic regularization on representation learning, guiding the network toward more discriminative features. Extensive experiments on multiple benchmarks show that DTFormer delivers consistent gains while remaining simple and efficient. Our results demonstrate that explicit semantic alignment offers an effective and practical route to improving RGB-D semantic segmentation. The code will be released upon acceptance.

---


### 32. [Anchor and Adapt: Asymmetric Prompt Adaptation for Few-Shot Industrial Anomaly Detection](https://arxiv.org/abs/2610.07016)

**<font color=#1a73e8>作者：</font>** Mengyang Zhao, Teng Fu, Haiyang Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In few-shot industrial anomaly detection, the few normal target images provide no direct defect supervision, making anomaly prompts difficult to learn from these samples alone. Some vision-language methods therefore use manually specified descriptions to supply explicit anomaly semantics. However, constructing these descriptions requires product-specific effort, and their effectiveness depends on prompt selection. We propose Anchor and Adapt, a two-stage prompt learning framework that separates the acquisition of anomaly semantics from adaptation to target normal appearance. Stage I learns transferable normal and abnormal anchors from annotated auxiliary data. Stage II keeps these anchors fixed and adapts an additional normal branch using the few target normal samples. The inherited and adapted normal branches jointly characterize target normality, with text-anchor regularization encouraging consistency with the generic normal prior and separation from the abnormal anchors. This design retains learned anomaly knowledge while reducing dependence on category-specific anomaly templates, without requiring synthetic anomaly generation. Cross-dataset experiments between MVTec-AD and VisA under 1-, 2-, and 4-shot settings demonstrate competitive detection and localization performance. Controlled ablations assess the roles of transferred anchors, asymmetric adaptation, dual-normal representations, and anchor regularization.

---


### 33. [WiSPER: Pose-Supervised Predictive and Residual Flow Refinement For Multi-Person 3D Pose Estimation With WiFi CSI](https://arxiv.org/abs/2610.07025)

**<font color=#1a73e8>作者：</font>** Gabriel Lee Jun Rong, Shanhong Liu, Pai Chet Ng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-person 3D pose estimation with WiFi channel state information (CSI) is challenging because reflections from different people overlap without directly identifying individual joints. Existing masked embedding objectives capture wireless relationships without explicit pose supervision, while structured decoders can retain coordinate errors. We propose WiSPER, a two-stage framework combining pose-aware predictive pretraining with conditional residual flow refinement. Pose-Aware Masked Embedding Learning (PAMEL) couples masked latent prediction with auxiliary pose-set supervision on the same CSI context, guiding the encoder toward joint localization from partial observations. Residual Flow refinement with Transformer (ReFT) generates a set of pose candidates to accommodate a variable number of people and refines each candidate through a conditional flow guided by its coarse coordinates and per-joint decoder features. Both stages use paired CSI and pose annotations during training, while inference requires only CSI. Experiments on the PiW3D dataset show that WiSPER achieves an overall mean per-joint position error of 63.72 mm, a 40.0% reduction relative to WiFi-JEPA. For experiments with two and three people, WiSPER reduces MPJPE by 42.1% and 38.1%, respectively. Pose-supervised pretraining configurations obtain lower errors than CSI-only JEPA, and enabling the trained residual refiner reduces overall MPJPE by 13.8-15.6% across the evaluated configurations.

---


### 34. [Identifiable World Models from Pretrained Diffusion Representations](https://arxiv.org/abs/2610.07028)

**<font color=#1a73e8>作者：</font>** Ruchi Sandilya, Conor Liston, Logan Grosenick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based world models can generate and predict trajectories in high-dimensional dynamical systems, but predictive accuracy does not imply that their latent coordinates recover the underlying state variables or causal interactions. We ask whether a frozen pretrained diffusion model can be equipped with identifiable coordinates without retraining its generative backbone. We show that auxiliary-variable nonlinear ICA guarantees can be transferred to Contrastive Diffusion Alignment (ConDA), which learns only a lightweight alignment map on top of frozen diffusion latents. Under standard TCL/GCL assumptions, the aligned representation identifies latent dynamical states up to permutation and componentwise invertible transformations, preserves the latent dynamic structural causal model, and reduces lagged graph recovery to transition-Jacobian sparsity. We evaluate TCL-, GCL-, and CEBRA-based ConDA against TDRL, CaRiNG, IDOL, temporal SuaVE, and iVAE across physical and robotic video systems. TCL and GCL achieve near-perfect blockwise state recovery and competitive lagged graph recovery, including exact recovery in a simulated falling-body system. In a simulated bipedal robot, learned dynamics recover the sign and temporal structure of responses to held-out control perturbations. These results show that a frozen generative diffusion model can be equipped with coordinates that are identifiable, structurally interpretable, and useful for analyzing intervention-relevant dynamics.

---


### 35. [Artemis: Geometry-Grounded Multi-Agent Driving World Models with Shared 3D State and Progressive Memory Update](https://arxiv.org/abs/2610.07031)

**<font color=#1a73e8>作者：</font>** Sitian Shen, Jiuming Liu, Mengmeng Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video world models have witnessed the paradigm shift from single-agent to multi-agent involvements, which can reveal more complicated dynamics and cross-agent interaction in the real world. However, existing approaches commonly adopt implicit inter-agent communications via cross attention, which lack explicit geometry constraints and unified 3D state, thereby leading to poor multi-view consistency and struggling with recovering out-of-sight agents. In addition, most of them assume a static background, failing to represent uncontrolled background dynamics. To address these problems, we propose Artemis: a geometry-grounded multi-agent world model with explicit memory sharing. An explicit 3D world map is reconstructed from multi-agent observations to enforce a unified 3D state across agents, offering high cross-view consistency. Specifically, an action-guided geometric injection module is developed to simultaneously render decomposed foreground-background control maps, which are then injected into a diffusion transformer through a designed GeoAdapter block. Compared to previous methods assuming static-only background, our GeoAdapter can also distinguish uncontrolled non-agent dynamics, which are conditioned on their own multi-frame history positions to provide consistent motion cues. Keyframes selected from progressive video rollouts are used to progressively update the reconstructed 3D world maps. To effectively capture complex dynamic patterns, we curate a novel dataset sampled from the CARLA simulator called MA-CARLA. Extensive experiments demonstrate the superiority of our proposed method in terms of visual fidelity and cross-view consistency in the generated videos. In addition, our Artemis can support simultaneous multi-modal rollouts with both 2D video and 3D point map maintenance, scale to scenarios beyond two agents and multi-camera setting.

---


### 36. [Investigating Model Compression for Neural Machine Translation in the Biomedical Domain](https://arxiv.org/abs/2610.07032)

**<font color=#1a73e8>作者：</font>** Maria Zafar, Souhail Bakkali, Rejwanul Haque  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained transformer models have achieved state-of-the-art performance across diverse machine translation tasks, including multilingual settings. Knowledge distillation has emerged as a sustainable approach for model compression, transferring knowledge from large teacher models to smaller, more efficient student models. Similarly, quantization, which reduces the numerical precision of model weights and activations (e.g., from 32-bit to 8-bit representations) is widely used to accelerate inference, enabling models to run several times faster during deployment. However, both techniques face limitations when applied to specialized domain data, particularly under low-resource conditions. In knowledge distillation, the effectiveness of transfer is often constrained by the scarcity of domain-specific parallel data, while quantization can lead to performance degradation as bit precision decreases. In this work, we investigate the combined application of knowledge distillation and quantization for French-to-English biomedical translation, a domain characterized by specialized terminology and limited parallel resources. We develop and compare multiple fine-tuning strategies to adapt compressed student models to this challenging setting. Our experiments demonstrate that a collaboratively distilled and quantized student model achieves a 69% reduction in size, a 98.21% increase in inference speed, and a 98.46% reduction in CO2 emissions compared to the original baseline all without sacrificing translation quality. These results indicate that jointly optimized compression techniques can yield efficient, high-performance models suitable for translation service providers operating under resource constraints.

---


### 37. [Shaping the Wind: Nested Potentials for Kinematically Admissible Urban Wind Prediction](https://arxiv.org/abs/2610.07033)

**<font color=#1a73e8>作者：</font>** Yidi Wang, Yunhe Zhang, Jiawei Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting transient urban winds is fundamental to understanding urban microclimates and designing climate-resilient cities. Building-resolving large-eddy simulation produces detailed incompressible urban wind fields at substantial computational cost for each layout. Neural surrogates offer a faster alternative by learning to predict the evolution of velocity fields. However, minimizing velocity prediction error does not guarantee local mass conservation and wall impermeability, which together define kinematic admissibility. This limitation stems from an unconstrained output representation: geometry conditioning guides predictions but does not restrict them to admissible velocity fields. Correcting boundary violations in these outputs changes the flux balance in adjacent fluid cells and may consequently compromise local mass conservation. To address the challenge, we propose Sculpt, a nested potential framework that builds the coupled, geometry-dependent constraints directly into its parameterization. This nested parameterization generates divergence-free velocity updates through the discrete curl of a volume vector potential on the native three-dimensional staggered grid. A shared scalar potential constrains the vector potential's boundary values so that the same operator also enforces impermeability, without a per-step pressure projection. Because backpropagation through this curl attenuates large-scale gradient signals, we parameterize the volume potential at multiple resolutions to better capture large-scale flow structures. We introduce UrbanWindFlow, an LES dataset spanning urban morphologies and inflow conditions, to evaluate accuracy and kinematic admissibility together.

---


### 38. [Inference-Time Projection for Physically Valid Biomolecular Diffusion Models](https://arxiv.org/abs/2610.07037)

**<font color=#1a73e8>作者：</font>** Qurat-ul-ain, Yee Whye Teh, Charlotte M. Deane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AlphaFold 3-style cofolding models predict biomolecular complexes with high structural accuracy, yet a large fraction of their outputs are physically invalid: chains overlap at interfaces, ligand bond lengths and angles are distorted, rings are non-planar, and stereocentres are inverted. Current approaches either steer the sampler with physics-informed potentials, which multiplies sampling cost and memory overhead making inference impossible on large complexes, or finetune the model, costing time and tying the fix to one architecture. We observe that, unlike structural accuracy, physical validity is fully verifiable at inference time from quantities the sampler already holds. We therefore treat physical validity as a constrained inference problem and introduce two closed-form projection operators applied to the diffusion model's denoised clean-coordinate estimate, $\hat{x}_0$: an inter-chain van der Waals projection that pushes apart the most severely clashing atom pairs, and a ligand distance-geometry projection that restores bond lengths, angles, internal contacts, planarity and chirality. Both operators are local, sparse and displacement-capped, require no network evaluations, gradients or importance sampling, and leave the denoiser and its weights untouched, so they can be dropped into any AF3-style sampler without retraining. Applied to two independently developed models, Boltz-2 and OpenFold-3, across five benchmarks (CASP15, CASP16, the PoseBusters monomer and complex sets, and the Boltz physical-validity test set), our method recovers perfect physical validity while preserving structural-accuracy and ligand-placement metrics. These gains are achieved with negligible runtime and memory overhead, providing a practical, model-agnostic route to physically valid all-atom structure prediction.

---


### 39. [The Premise Is the Problem: Exchangeability Failure in Self-Monitored Test-Time Adaptation](https://arxiv.org/abs/2610.07038)

**<font color=#1a73e8>作者：</font>** Weijia Han, Lisha Qu, Zhenda Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern forecasting models are often updated after deployment so they can respond to changing data. These updates can also make predictions worse, so practical systems need a reliable monitor that can detect harmful changes and trigger protection. A natural design is to monitor the same prediction errors that guide the updates. This paper asks whether the statistical guarantee behind such a monitor remains valid when monitoring and adaptation use the same feedback. We study this question in multi-step time-series forecasting. We show that overlapping targets and dependence in forecast errors can break a key assumption required by the guarantee. The monitor may then raise alarms even when no harmful change has occurred, and its response can further damage prediction quality. We also find that adaptation can hide sustained changes from its own monitor, while the original frozen model retains a clearer signal. These results expose a basic failure mode in self-monitored adaptation. They show why reliable deployment requires checking the monitor's assumptions, comparing adaptation with the frozen model under realistic feedback, and limiting the effect of every protective response.

---


### 40. [Tellimation: Making Narrative Gaps Visible in Children's Storytelling with Just-in-Time Animation](https://arxiv.org/abs/2610.07039)

**<font color=#1a73e8>作者：</font>** Vincent Cavez, Marielle Zheng, Momin Siddiqui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Illustrated scenes are used to prompt children's stories, yet children with language difficulties often omit the details, actions, and relationships that make a story coherent. We introduce Tellimation, which animates scene elements a child has omitted or misdescribed, drawing attention to a narrative gap without saying what to tell. Its design space covers eight kinds of gaps (who is in the scene, how many, what they are like, what they are doing, where, when, how they relate, and what lies beyond the picture, such as speech and thoughts), instantiated through 20 parameterized animations grounded in classical animation principles. A real-time pipeline detects discrepancies between utterance and scene, then selects and parameterizes an animation from the scene's narrative potential and the child's history. Adults interpreted most animations without instruction (N=120); children (N=12) resolved 46% of the gaps the system identified with animations, against 13% without.

---


### 41. [Crop Yield Prediction for Punjab, Pakistan: A Tree-Ensemble and Leaf-Health Prototype, and What Random Validation Hides](https://arxiv.org/abs/2610.07059)

**<font color=#1a73e8>作者：</font>** Amina Asif, Qurat ul ain Asif, Noor Bakhat Asif  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Yield forecasts help planners and farmers decide on inputs, storage and imports, but small agricultural tables can make reported accuracy fail on a new season. We built a crop-yield prototype for Punjab, Pakistan that combines Random Forest, XGBoost, support vector regression and a Ridge-stacked ensemble with a MobileNetV2 leaf-health classifier, and deployed it as a web application with SHAP explanations. A random 80/20 split of a merged Kaggle-derived table (414 rows) gives the ensemble an R2 of 0.991. An audit showed that the table contains only 46 independent observations: a join with nine temperature records per year copied every crop-year nine times. Holding out whole years takes XGBoost on the same rows from R2 = 0.994 to -0.20. On deduplicated data, and on a longer FAOSTAT table (1990-2024, 70 observations), a per-crop linear trend (leave-one-year-out RMSE 0.29 Ton/Ha) beats every model not given the year (0.84-1.06). Neither pesticide use nor national temperature change explains the trend residuals. An apparent pesticide gain in the Kaggle table disappears on FAOSTAT, where the pesticide series is mostly imputed and the two releases disagree. An independent district-level wheat panel (36 districts, 13 seasons) shows that most variation in Punjab is spatial and that a district mean with a common trend matches the learned models. The leaf classifier reaches 99.87% accuracy on held-out PlantVillage images and recalls 96.4% of 336 unseen diseased leaves after near-duplicates were removed. However, no leaf image is paired with a yield record, so the health score used in the yield models had to be constructed and adds nothing. We report these negative findings together with the prototype.

---


### 42. [Skillful Data-Driven Subseasonal Soil Moisture Forecasting: Prospects and Limits for Flash Drought Prediction](https://arxiv.org/abs/2610.07060)

**<font color=#1a73e8>作者：</font>** Noelia Otero, Atahan Özer, Miguel-Ángel Fernández-Torres 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite substantial progress in short-to-medium-range weather forecasting, predicting high-impact events such as flash droughts remains a key challenge for both early warning operations and physically-based subseasonal-to-seasonal (S2S) prediction systems. Here we demonstrate that, for S2S soil-moisture forecasting over Europe, forecast skill depends as much on how the prediction problem is formulated as on the forecasting model itself. Using a Vision Transformer-based architecture with dual-pathway temporal and spatial attention, we show that residual learning is essential to outperform persistence. This advantage is realized only when forecasting root-zone soil moisture in physical units rather than standardized anomalies, revealing that the target representation itself constrains predictability. A probabilistic extension via quantile-head fine-tuning further provides well-calibrated predictive distributions. Benchmarked against deep-learning and operational ECMWF S2S baselines over 2021-2022, our model achieves the highest deterministic and probabilistic skill at all lead times and reliably detects anomalously dry root-zone states (below the 20th percentile). Yet flash drought onset, defined by multi-pentad intensification criteria, remains a fundamental challenge shared across all current S2S systems. These findings advance data-driven S2S soil-moisture forecasting while highlighting the remaining challenge of predicting rapid drought development.

---


### 43. [Decomposition-Guided Curvelet Thresholding for Sharp-to-Soft CT Kernel Conversion](https://arxiv.org/abs/2610.07067)

**<font color=#1a73e8>作者：</font>** Mahmoud Nasr, Jan K. Argasinski, Krzysztof Brzostowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image denoising is a crucial task in image processing, focused on improving image quality by minimizing noise while maintaining essential structural elements. This study presents a hybrid denoising framework that combines several decomposition techniques, including empirical mode decomposition (EMD), variational mode decomposition (VMD), multichannel EMD (MEMD), and bidimensional EMD (BEMD), with curvelet transform thresholding. Each decomposition mode undergoes processing through both soft and hard thresholding, and the denoised modes are combined to rebuild the final image. Comprehensive evaluations of standard CT image datasets reconstructed with various kernels (B50, B46, B41, B36) reveal substantial enhancements in denoising efficacy. VMD consistently achieves the highest peak signal-to-noise ratio (PSNR) and structural similarity index (SSIM), signifying exceptional noise reduction and feature preservation. The study analyses the trade-offs between soft and hard thresholding: soft thresholding maintains intricate visual details, whilst harsh thresholding provides enhanced noise reduction. The suggested method surpasses traditional techniques in both reference and non-reference quality criteria, indicating its potential for broader application in medical imaging and future incorporation with adaptive thresholding algorithms.

---


### 44. [A BEMD-Based Quaternion Filtering Approach Sharp-to-Soft Kernel CT Image Conversion](https://arxiv.org/abs/2610.07071)

**<font color=#1a73e8>作者：</font>** Mahmoud Nasr, Jan K. Argasinski, Krzysztof Brzostowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quality of computed tomography (CT) images is significantly affected by the selection of reconstruction kernels: sharp kernels improve spatial resolution but increase noise, whereas soft kernels diminish noise at the expense of edge clarity. This study presents an innovative enhancement framework utilising Bidimensional Empirical Mode Decomposition in conjunction with Quaternion Bilateral Filtering (BEMD--QBF) to convert sharp-kernel CT images into representations resembling soft-kernels, while maintaining critical anatomical structures. The technique disaggregates each image into intrinsic mode functions via BEMD and analyzes them inside a cohesive quaternion framework to attain efficient noise reduction and structural integrity. The proposed methodology is evaluated using several reconstruction kernels (B50, B46, B41, B36, B35, B31) and compared with recognised filtering strategies, including Non-Local Means, Anisotropic Diffusion, Bilateral Filtering, and Quaternion Bilateral Filtering. Quantitative evaluations of the Structural Similarity Index (SSIM) and Peak Signal-to-Noise Ratio (PSNR) indicate that BEMD-QBF consistently attains superior structural fidelity and competitive noise reduction across all evaluated kernels. The results underscore the efficacy of the proposed strategy as a viable approach to enhancing post-reconstruction CT images, yielding superior image quality without requiring access to raw projection data.

---


### 45. [On Color Alignment in VAE Latent Spaces and Its Applications](https://arxiv.org/abs/2610.07072)

**<font color=#1a73e8>作者：</font>** Julian D. Santamaria, Kai Wang, Jesús Malo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variational autoencoders (VAEs) are a key part of modern text-to-image models, which generate images within their latent space. VAEs are known to disentangle the main factors of variation in the data, and color is known to be one of the most structured of these in natural images: decorrelating it yields one luminance axis and two opponent-color axes. Color should therefore be expected to emerge as a distinct factor in the VAE latent space. Yet how these latent spaces represent color remains largely unexplored. In this work, we show that the VAEs of text-to-image models share a color subspace aligned with brightness and opponent-colors. Through a linear approximation of the encoder and targeted latent steering, we find this subspace consistently across a broad range of VAEs, from SD1.5 to FLUX.2 and Z-Image. Building on this characterization, we propose three applications: ColorTuning, which achieves state-of-the-art in precise numerical color generation on the fine-grained CSS3/X11 system of GenColorBench, saturation control, to adjust the global chromatic intensity, and color transfer, to change the palette to match a reference. The code and models are publicly available at this https URL

---


### 46. [CuratorMAS: Automating Dataset Curation via Multi-Agent Orchestration](https://arxiv.org/abs/2610.07075)

**<font color=#1a73e8>作者：</font>** Yixin Zhang, Wenjie Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-quality datasets are essential for reliable machine learning, but dataset curation remains costly and hard to generalize across domains. Existing methods typically rely on manually designed heuristics or model-dependent signals, limiting their applicability across tasks and user queries. To address these limitations and automate data curation, we propose \textbf{CuratorMAS}, a multi-agent collaboration framework that orchestrates agents to evaluate and curate high-quality datasets. To achieve the goal of flexible curation, CuratorMAS decomposes the complex curation process into five programmable execution stages and forms a parallelizable workflow. Specifically, CuratorMAS first performs dataset exploration to collect contextual information such as file structures and constraint cues, thereby developing a comprehensive understanding of the given task. In order to acquire up-to-date information, CuratorMAS retrieves domain knowledge from online sources to augment the evaluation process. Next, CuratorMAS derives the necessary evaluation criteria and computes the corresponding metrics. Based on these results, CuratorMAS executes filtering accordingly. Finally, an evolution module summarizes the evaluation outcomes and updates the relevant skills. Extensive and comprehensive experiments demonstrate that CuratorMAS significantly reduces the noise rate by up to 36.03 percentage points (pp) while also improving the F1 score of downstream models by up to 8.88 pp.

---


### 47. [What Must Replay Preserve? Separating Correctable Bias from Class Correspondence](https://arxiv.org/abs/2610.07077)

**<font color=#1a73e8>作者：</font>** BoRen Deng, Xiangyue Ma, Chenglong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-incremental learning must recognize all classes seen so far without task labels. Logit replay methods such as DER and DER++ mitigate forgetting by matching the model's past predictions on stored examples. Deleting this matching reveals its benefit, but the resulting accuracy cost cannot show whether the stored scores themselves are needed, or whether the cost survives correction of the classifier's bias toward recent classes. We propose a diagnostic framework that treats a cached prediction as temporally heterogeneous supervision: it separates classes known when an example was stored from classes learned afterward, edits each group, and evaluates every model before and after a task-level offset that leaves within-task predictions unchanged. On CIFAR-100 with DER++, suitable fixed constants replace the unrefreshed stored scores of later-learned classes within an equivalence margin of 1 percentage point, and the offset reduces the cost of deleting their matching from 14.9 to 1.8 points. Reassigning the non-gold scores of classes known at storage, which preserves their values and each task's target probability, costs 4.3 points before and 4.0 after the offset, and a parallel cost persists in image distillation. In the tested fixed-head setting, the large cost of deleting later-class matching is thus mostly correctable by this offset, whereas the smaller cost of disrupting class correspondence persists. Code and data are available at this http URL.

---


### 48. [Few-Shot Bioactivity Prediction with Meta-Learning under Assay Heterogeneity](https://arxiv.org/abs/2610.07079)

**<font color=#1a73e8>作者：</font>** Michal Kmicikiewicz, Tommy Rochussen, Vincent Fortuin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate bioactivity prediction is a central challenge in early-stage drug discovery, as individual assays often contain too few measurements to train reliable models independently. Meta-learning offers a principled approach to this few-shot setting, but assay heterogeneity may limit its effectiveness. Here, we test this hypothesis and show that meta-learning performance degrades as meta-training tasks become more heterogeneous. To address this, we introduce MetaHeta, a meta-learning framework that accounts for assay heterogeneity by conditioning predictions on auxiliary data from related assays, with relatedness defined flexibly from available assay information. The architecture of MetaHeta combines linear attention over large auxiliary datasets with exact attention over scarce task-specific context, enabling efficient scaling to the former without compromising exact attention over the latter. We demonstrate the benefits of our approach on assays from ChEMBL and BindingDB, improving few-shot bioactivity prediction and downstream compound prioritization in retrospective Bayesian optimization.

---


### 49. [When Attention Does Not Explain the Peak: Temporal Reference vs. Forecast Output in Attention-Based Time-Series Forecasting](https://arxiv.org/abs/2610.07080)

**<font color=#1a73e8>作者：</font>** Yuji Akamatsu, Takao Yamanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention maps are often interpreted as evidence of what a forecasting model uses when making predictions. In our load-forecasting model, a CLS representation of historical demand queries 24 future exogenous horizon tokens through cross-attention, inviting a temporal interpretation in which highly attended horizons may appear to explain forecast peak timing. We test this interpretation using a horizon-level attention descriptor, $\Psi_{\mathrm{out}}$. Across 31 day-aligned windows of the Panama load dataset, the forecast achieves a median peak-time error of 0 h and a 51.6% exact-match rate, whereas the argmax of $\Psi_{\mathrm{out}}$ has a median error of 5 h and 0% exact match. The forecast peak is closer to the observed peak in 27 of 31 windows. This dissociation is not merely an argmax artifact: within $\pm1$ h, attention reaches only $1.16\times$, $1.11\times$, and $1.14\times$ the uniform baseline around observed, predicted, and weekly-naive peaks, respectively, indicating weak and non-selective concentration. Yet the attention profile is structured, with cross-window consistency of 0.83. Replacing 12 future weather features with their training-set means makes the profile nearly uniform, showing sensitivity to future weather variation rather than fixed horizon position alone. The dissociation is also reproduced across three random-seed runs. These results show that structured, input-sensitive, and reproducible horizon-level cross-attention need not provide a valid peak-selective explanation of forecast behavior. The observed behavior is instead consistent with an internal horizon-reference role for integrating future exogenous information, although this functional role is not causally established.

---


### 50. [Graph-Based Recognition of Simulated Train-Driver States From Facial and Upper-Body Keypoints](https://arxiv.org/abs/2610.07083)

**<font color=#1a73e8>作者：</font>** Olivia Nocentini, Marta Lagomarsino, Gokhan Solak 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver fatigue poses a significant challenge to railway safety, with traditional systems like the dead-man switch offering limited and basic alertness checks. This study presents a vision-based monitoring system that relies solely on a single front-facing RGB camera and a graph neural network to classify simulated train-driver states into alert, not-alert, and an emergency class comprising acted emergency-like behaviours. To optimize input representations for the model, an ablation study was performed, comparing three feature configurations: skeletal-only, facial-only, and a combination of both. Experimental results show that combining facial and skeletal features yields the highest accuracy (81%) for the three-class model under the light condition, outperforming models that use only facial or skeletal features. Furthermore, the combination of facial and skeletal features achieves 99% accuracy in the alert/not alert classification in light condition. Additionally, we introduced a controlled RGB video dataset containing alert, not alert, and acted emergency-like behaviours recorded under three illumination conditions. These contributions represent a step toward passive and non-contact train-driver state recognition based on facial and upper-body dynamics.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
