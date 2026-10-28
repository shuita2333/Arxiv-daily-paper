# 📦 其他研究 | 2026年10月29日

> 本类共 **257** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-257](./part-06.md)

---

### 151. [RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878)

**<font color=#1a73e8>作者：</font>** Delin Wang, Sinuo Wang, Rui Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirements explicit, but task-level checklists may leave the overall analytical structure underexamined. We introduce RubricAtlas, which derives type-level analytical requirements from expert reports on different objects within the same research type and organises detailed checks around recurring analytical questions. The requirements give related tasks a shared standard for what to analyse, without prescribing their answers. Our framework links binary checkpoints to report passages and evaluates completeness separately from argument validity. Built from 3,079 Chinese financial research reports, RubricAtlas covers 99 research types. Reference-report selection experiments show that individual reports cover only about half of their type's analytical questions, and that selecting requirements from different reports changes evaluation scores and agent rankings. Across ten agents, two judge pipelines achieve checkpoint agreement of $\kappa$ = 0.71 and agent-ranking agreement of Kendall $\tau$ = 0.87. Controlled deletions reduce scores on the affected analyses, while padding produces no detectable increase. These findings support type-level rubrics for comparing the analytical completeness of Web deep research outputs, with individual decisions traceable to report evidence.

---


### 152. [Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL](https://arxiv.org/abs/2610.36882)

**<font color=#1a73e8>作者：</font>** Nihal Acharya Adde, Hanno Gottschalk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study, we propose a dual-branch evolutionary framework that simultaneously performs Neural Architecture Search (NAS) and Hyperparameter Optimization (HPO) for Reinforcement Learning (RL) in Autonomous Driving (AD) tasks. While NAS has shown strong potential in automating architecture design for Convolutional Neural Networks (CNNs), its application to RL remains limited, especially in scenarios that require joint optimization of architectural and training dynamics. Building on our prior work on Evolutionary Multi-Objective NAS (EMNAS), the proposed framework evolves discrete network architectures and continuous hyperparameters in parallel under a unified multi-objective search strategy. In this setup, NAS targets the convolutional layers of the RL policy network - responsible for visual feature extraction, while HPO focuses on optimizing critical RL hyperparameters. To accelerate convergence and improve generalization, we incorporate parallel evaluation and a teacher-student policy transfer mechanism. Experiments in a high-fidelity driving simulator show that the joint NAS-HPO framework consistently outperforms standalone NAS, yielding policies with higher rewards, fewer parameters, and improved stability. These results highlight the benefits of jointly optimizing model structure and training dynamics for scalable and effective RL agent design.

---


### 153. [Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning](https://arxiv.org/abs/2610.36888)

**<font color=#1a73e8>作者：</font>** Martín de Frutos, Baptiste Corban, Claire Bizon Monroc 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing noise mitigation strategies for wind farms usually consist in reducing turbines power output, without accounting for the wake interactions between them and the noise emission directivity. This leads to over-conservative policies and unexploited wind power. Yet, turbine yaw can simultaneously affect wake interactions and the direction of noise emission, offering an additional degree of freedom for farm-level noise control. We therefore propose Noise Steering, a model-free reinforcement learning (RL) strategy that jointly controls turbine yaw angles and power setpoints to maximise farm power while satisfying a local noise constraint in a defined region. To enable training at a reduced computational cost, a low-fidelity acoustic model is coupled with the steady-state FLORIS simulator. The RL agent effectively learns how to redirect wakes and noise directivity away from the protected region while redistributing power across the farm. On a six-turbine test farm, the policy satisfies the 40 dB noise constraint throughout the full range of turbulent winds, with an average power deficit of only 2% relative to greedy unimpeded control, and up to 7.7% at high wind speeds. In comparison, the industry-standard noise-reduced operation (NRO) baseline here generates an average power loss of 17%. When deployed in the higher-fidelity this http URL simulator, the policy largely retains its performance under steady and turbulent inflow, despite differences in simulation fidelity. These results demonstrate the potential of combining yaw control and power derating through RL to improve the power-noise trade-off in wind farm operation.

---


### 154. [PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets](https://arxiv.org/abs/2610.36896)

**<font color=#1a73e8>作者：</font>** Beomjin Ahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PREEN (Preset Regression via an Exemplar-based Editor Network), which casts color style transfer as regression onto the 29 parameters of a deterministic image editor. Given a content image and a style reference, PREEN predicts a preset, a vector of editor slider values that is interpretable and editor-consumable, not a raster image. The key obstacle is supervision, since an arbitrary real reference lacks a preset ground truth. We therefore supervise with a style-transfer teacher, whose target looks we invert into the editor's parameter space as pseudo-presets, then pretrain a CLIP-conditioned regressor and refine it with LoRA under an image-level CIELAB loss. On the human-curated PST50 benchmark, PREEN applies the reference's color while preserving structural fidelity, leading the baselines on pixel- and perceptual-fidelity metrics. The preset is compact and predicted at sub-second on-device latency. The low-dimensional subspace also exposes a single inference-time strength knob that traces a continuous default-to-vivid trajectory in one forward pass, with every intermediate state a valid editor preset. A two-axis human study shows that raters prefer the vivid end for matching the reference but the default as a standalone photo, a trade-off the knob spans without retraining.

---


### 155. [Natural Hard-Negative Mining from Positives for Instruction-Following Retrieval](https://arxiv.org/abs/2610.36900)

**<font color=#1a73e8>作者：</font>** Chaolang Li, Jingyu Li, Zhaocheng Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction-following information retrieval (IFIR) requires retrievers to rank documents by both a query and its instance-specific instructions, yet instruction-conditioned contrastive supervision remains scarce. Existing synthetic methods typically fix a positive passage and generate additional negatives, overlooking the hard-negative potential of the original positive. We propose Natural Hard-Negative Mining (NHNM), which promotes convertible negatives under query-compatible instructions and repurposes original positives as natural instruction hard negatives. Its automated Candidate Cleaning, Reversal Construction, and Geometry Filtering pipeline produces compact, high-contrast supervision aligned with the pretrained retrieval space. Applied to MSMARCO, NHNM yields NHNM-MARCO, an IFIR training set of nearly 7K instances. On InstructIR and FollowIR, models with 568M to 4B parameters fine-tuned on NHNM-MARCO achieve strong instruction-following performance and match or surpass substantially larger retrievers in several settings. Controlled analyses and ablations attribute these gains to natural hard-negative supervision rather than model scale or training-data volume.

---


### 156. [Developing a Dynamic Multi-factor Authentication System for Securing Smart Organizations](https://arxiv.org/abs/2610.36926)

**<font color=#1a73e8>作者：</font>** Mohsen Saffar, Hamid Reza Naji  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As smart organizations increasingly rely on technologies like AI, big data, and IoT, securing these systems is crucial. This research introduces a dynamic multi-factor authentication (MFA) system within the Zero Trust Architecture (ZTA) framework, which enforces continuous verification. The system randomly selects biometric authentication factors, such as fingerprint, iris, and face recognition using a Markov chain model to ensure adaptability and reduce predictability in security measures. Using CASIA biometric datasets and AES-128 encryption, the system securely manages user data and authentication. Performance analysis shows that the dynamic selection process balances security and efficiency, making it suitable for smart organizations, particularly in e-government contexts. This MFA system strengthens cybersecurity by providing a flexible, real-time defense against evolving threats.

---


### 157. [DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding](https://arxiv.org/abs/2610.36929)

**<font color=#1a73e8>作者：</font>** Saifullah Saifullah, David Dembinsky, Stefan Agne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal transformer models have driven unprecedented performance breakthroughs in modern document understanding. However, the inherent black-box nature of these models remains a major obstacle to their safe deployment in high-stakes sectors. Despite significant progress in explainability for vision and language tasks, explainable AI (XAI) research tailored to multimodal document understanding has received little attention. To address this gap, we present \ourframework{}, the first comprehensive explainability framework that adapts existing XAI methods and evaluation metrics to the multimodal (text, layout, and image) document understanding context, while introducing efficient multi-target adaptations of both methods and metrics for domain-specific tasks such as semantic entity recognition. Using \ourframework{}, we systematically evaluate 13 XAI methods across 3 document understanding tasks, 8 datasets, 4 models, and 17 evaluation metrics, and find that only a few methods perform consistently across all evaluation criteria, with Occlusion emerging as the most faithful and interpretable method overall. Through a dedicated meta-evaluation, we observe moderate to strong agreement among several faithfulness and complexity metrics while identifying certain ones that produce unreliable results. Finally, through multiple dataset-wide diagnostic analyses, we uncover key insights into model behavior, including the contribution of individual modalities across tasks and labels, spatial attribution patterns around target entities, and potential dataset biases. Overall, this work serves as both a benchmark and a practical guide for future XAI research in multimodal document understanding. To support reproducibility, we publicly release our code at this https URL.

---


### 158. [Provenance Signatures for Low Rank Adaptations of Image Diffusion Models](https://arxiv.org/abs/2610.36933)

**<font color=#1a73e8>作者：</font>** Tobias Cheung, Mohan Dantam, Marc Juarez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have revolutionized the generation of realistic artificial images. Efficient techniques such as Low Rank Adaptation (LoRA) can modify these models for particular use cases, making them more diverse and widely usable. At the same time, open base models may be adapted to deliver biased, harmful or illegal images in an online service. In this paper, we develop a protocol to detect when a service may be using an adaptation of an otherwise standard model. We describe the precise setup and threat model for this provenance question and define two different problems arising due the presence of multiple model families and multiple adaptations. In contrast to previous works that have considered model identification within lists of known candidate models, we consider the realistic open world scenario where the set of possible adaptations and alternative models are unknown. Using a hypothesis testing approach, our protocols can distinguish between the base model, a LoRA adaptation and other completely different families of models. For this test, we develop a black box signature of the models based only on intrinsic dimension of sets of images generated by the models.

---


### 159. [Gaussian Process Bandits for Constraint Black Box Lever Optimization](https://arxiv.org/abs/2610.36935)

**<font color=#1a73e8>作者：</font>** Bram van den Akker, Hidde Fokkema, Anastasiia Kornilova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing discrete allocation weights across competing segments of a shared budget is a fundamental challenge in resource-constrained, sequential decision-making environments. In practice, this optimization is often hindered by delayed, noisy, and aggregate feedback, alongside strict operational constraints on how frequently weights can be adjusted. Because of the resulting combinatorial action space and extreme data sparsity, classical multi-armed bandit algorithms that evaluate arms independently are rendered highly inefficient. To overcome these limitations, we propose a segmentation-agnostic approach utilizing Gaussian Process Upper Confidence Bound (GP-UCB) algorithms. By placing a Gaussian Process prior on the reward function, our method effectively shares information across neighboring configurations, drastically reducing the necessary exploration horizon. In this paper, we bridge the gap between theoretical bandit research and production-scale deployment. We first introduce a high-fidelity synthetic simulator to evaluate various kernel configurations under stationary, drifting, and reactive environments, identifying a composite Matérn + Linear kernel as the most robust choice for overcoming local noise and global shifts. Finally, we validate our findings through a large-scale Randomized Controlled Trial (RCT) in a live production environment. Our empirical results demonstrate that the GP-UCB approach delivers a statistically significant efficiency lift compared to a standard $\varepsilon$-greedy baseline, offering a highly practical solution for real-world black-box lever optimization.

---


### 160. [Algorithmic Monoculture in Machine Learning-based Site-Specific Fertilizer Recommendation](https://arxiv.org/abs/2610.36941)

**<font color=#1a73e8>作者：</font>** Abdelghani Belgaid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning recommendations are often evaluated one model at a time, despite deployment across interconnected decision makers. For continuous NPK fertilizer prescriptions, correlated errors can aggregate across farms and generate systemic costs. A model of shared and farm-specific recommendation errors links expected social loss to model adoption shares; the Herfindahl-Hirschman Index characterizes concentration effects when common model errors are independent and predictive risks are equal. A covariance-generalized formulation captures the dependence between model families. A two-model threshold characterizes when privately optimal monoculture is socially dominated, and a convex portfolio rule limits average private predictive regret. Nine model families across five Moroccan cereal systems provide a benchmark-based calibration. Under illustrative parameters and a 10% regret cap, accuracy-constrained diversification lowers modeled social loss in all five systems by 10.89-41.53% (mean 19.41%). Uniform allocation reduces modeled loss in this setting, but breaches the regret cap in every crop. Correlation sensitivity shows that highly dependent model errors attenuate the benefits of diversification. These counterfactual outcomes are not estimates of agronomic or monetary welfare; the framework identifies adoption architecture and error dependence as ecosystem-level evaluation variables.

---


### 161. [Too many clients spoil the logs: distributed parsing, aggregation techniques and metrics](https://arxiv.org/abs/2610.36946)

**<font color=#1a73e8>作者：</font>** André García Gómez, Viktor Beck, Max Landauer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Log messages are employed to identify anomalies in IoT systems and have been widely used across many applications. To enable collaboration among infrastructures belonging to different organizations, federated log anomaly detection has been thoroughly investigated for this purpose, often assuming the availability of ground truth log templates. However, this is typically not the case, as it is still necessary to depend on log parsers to extract log templates at inference time, while the design and deployment of such parsers in distributed environments remains largely an open problem. To this end, we report on an empirical investigation of distributed parsing and its key challenges, providing insights and lessons learned towards closing the gap between research and application. To further refine and contextualize the resulting benchmarks, we examine and introduce new metrics that provide a more comprehensive view for evaluating distributed parsers and how they behave in distributed environments. We propose a set of lessons learned and recommendations to support the design, deployment, and evaluation of distributed parsers. In particular, we evaluate the performance of five distinct parsing algorithms in combination with aggregation techniques that allow a unified agreement of event-template mappings across all participating clients, a prerequisite for federated log anomaly detection. In total, 6,720 distinct distributed configurations were tested for this purpose.

---


### 162. [Dense Representation Learning and Differentiable Shape Modeling for Spine Landmark Detection](https://arxiv.org/abs/2610.36951)

**<font color=#1a73e8>作者：</font>** Augustin Daridon, Sofiane Sifaoui, Ayman Assi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spine landmark detection from spinal X-ray is a key step for estimating spine deformation severity, for building biomechanical models, and for pre-operative planning. We reframe anatomical landmark detection as a pixel-level contrastive representation learning problem, matching dense pixel embeddings with landmark prototypes. Surprisingly, even with a generic U-Net backbone, this formulation results in more discriminative heatmaps compared to the traditional heatmap regression paradigm, leading to improved discrimination between vertebral corners on distinct vertebra. Furthermore, we combine the resulting heatmaps with learnable shape priors over the global configuration of spinal landmarks to resolve ambiguities in landmark locations, yielding a simple and practical approach to spinal landmark detection. Our approach is competitive, in terms of landmark accuracy and clinical parameter estimation, with the state-of-the-art on the public AASCE dataset and on two private spinal X-ray datasets. Our code and pre-trained weights are available at this https URL.

---


### 163. [Mining the Nineteenth Century for the Thirteenth: Register-Scale Forced Alignment and HTR Bootstrapping via Legacy Regesta and Antiquarian Editions](https://arxiv.org/abs/2610.36956)

**<font color=#1a73e8>作者：</font>** Tamas Kovacs, Daniel Luger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten text recognition (HTR) for the registers of Pope Honorius III depends on modern expert transcriptions, which exist only for regnal years 1-2 of Reg. Vat. 9. For the remaining registers, nineteenth-century scholarship offers Pressutti's regesta and partial editions. On fol. 1-203, where both layers exist, we measure what this legacy layer can contribute, on transcriptions that we first audit against it, and find a division of labor across three tiers. At the orthographic tier, raw editions are at best neutral for adapting a recognizer to the second regnal year and harmful without replay, whereas projection onto curial spelling with replay of modern source lines turns them into zero-label adaptation targets: pooled over all 134 year-2 sides, the WER falls by 1.50 points (95% CI -1.84 to -1.15), closing 33% of the gap to an oracle; the spelling changes at the year split, through the scribe or the transcriber, whereas the hand changes visibly only at fol. 191r. At the lexical tier, the corpus-wide legacy lexicon contains 82.2% of the out-of-vocabulary words of unedited entries and flags recognition errors with 66.7% precision, and labels from pre-trained medieval NER models, distilled into the recognizer's NER head, reach F1 82.1% on an expert validated benchmark, level with the best tagger applied after recognition. At the topological tier, Pressutti's regests, the closing datum clauses, and the regests' dates converted to the chancery's Roman form find 73.9% of entry starts in the recognized line stream, and edition agreement estimates a CER of 7.80% beyond fol. 203. Antiquarian scholarship thus cannot replace modern transcription, but it can steer, check, and segment HTR across the untranscribed registers.

---


### 164. [On the VC Dimension of Autoregressive Linear Threshold Functions](https://arxiv.org/abs/2610.36970)

**<font color=#1a73e8>作者：</font>** Ilan Doron-Arad, Idan Mehalel, Elchanan Mossel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear threshold functions (LTFs) are a canonical class of Boolean predictors. In the autoregressive setting, the same LTF reads the most recent $d$ bits, generates the next bit, and returns the bit produced after $T$ steps. While the one-step class has VC dimension $d$, for general $T$ the counting upper bound is $O(d^2)$. We prove that the VC dimension is $\Theta(d^2)$ for every $T\ge d^2$, resolving the quadratic gap for deterministic autoregressive LTFs. We then adapt the same technique to show an exponential separation between deterministic and stochastic autoregressive models: replacing the sign of LTFs by logistic sampling can increase the VC dimension of the final majority prediction class from quadratic to exponential in $d$.

---


### 165. [GNN-Guided Network Reduction for Centralized Urban Traffic Routing](https://arxiv.org/abs/2610.36981)

**<font color=#1a73e8>作者：</font>** Nikolai Antonov, Lukáš Chrpa, Andrii Nyporko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the centralized traffic routing (CTR) problem, where a central planner assigns routes to origin-destination (OD) vehicle flows to minimize congestion-dependent segment cost. Prior work formulates CTR efficiently as a mixed-integer linear program (MILP), but scaling this formulation to the full road network is computationally prohibitive within an operational time budget. Bounded Routes and Smart Routes speed up optimization using precomputed reduced networks; however, these methods do not account for vehicle information within each OD flow. Motivated by this gap, we propose a learning-based urban network reduction approach. A dedicated graph neural network (GNN) first scores road segments for each OD flow using the road network and vehicle-flow information. Highly ranked segments are then incorporated into complete OD routes, and the original segment-flow MILP is solved on the resulting reduced road network. The GNN thus guides the reduction of the road network, while the solver enforces feasibility and determines the routing. Experiments on four real urban networks -- Prague-Dejvice, London, New York, and Sydney -- show that the proposed approach achieves the smallest relative objective difference to the $30$-second full-graph reference in every city under both traffic regimes. Averaged across cities, this difference is more than six times lower than that of the best competing method. Moreover, traffic simulation results show that the optimization gains of the proposed method lead to more efficient routing, with the highest aggregate arrival rate and a competitive trip duration per arrival percentage point.

---


### 166. [GPA-VGGT: Geometry-Preserving Acceleration of VGGT](https://arxiv.org/abs/2610.37000)

**<font color=#1a73e8>作者：</font>** Muyeol Sung, Jangwon Kim, Jongwoo Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward geometry models such as VGGT recover camera parameters, depth maps, and point maps from one to hundreds of views in a single forward pass, making them powerful backbones for multi-view 3D perception. However, VGGT's global attention is quadratic in the number of frames and dominates end-to-end runtime on long sequences, which has motivated a range of training-free efficiency methods such as token merging. These methods, however, come with a drop in accuracy that makes them hard to use in place of VGGT. We propose GPA-VGGT, a training-free acceleration method that replaces global attention in early blocks with frame attention augmented by a shared cross-frame K/V set. In the remaining blocks, we merge only keys and values while preserving all queries, restore the attention mass of the tokens each merged key represents, and randomly project the matching metric to 128 dimensions to reduce matching cost. Across diverse multi-view geometry tasks, GPA-VGGT provides training-free acceleration at speedups comparable to prior work while preserving the information required for precise geometric estimation, retaining over 99% of VGGT's pose accuracy under AUC@3.

---


### 167. [Compote: Collapse-Resistant Multiple Hypothesis Learning For Sequential Recommendation](https://arxiv.org/abs/2610.37005)

**<font color=#1a73e8>作者：</font>** Louis Castres Saint Martin, Clement Calauzenes, Alain Rakotomamonjy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-item prediction is inherently ambiguous: a single interaction history often admits multiple plausible continuations across distinct catalogue regions. Standard sequential recommenders compress these alternatives into a single prediction, conflating user intents. We introduce COllapse-resistant Multiple hyPOThesis lEarning (COMPOTE), a multi-hypothesis transformer trained with an annealed objective that transitions from uniform supervision to a winner-takes-all assignment. This mechanism forces hypotheses to specialize into distinct catalogue regions, while inference relies on an efficient, normalizer-free max-similarity rule. Theoretically, we show that in the population case, the optimal solutions partition the conditional next-item distribution according to a max-entropy quantization principle, while pooled scores preserve the Bayes-optimal ranking. We also prove a generalization bound scaling logarithmically with the number of hypotheses. Across three Amazon Reviews 2023 benchmarks, COMPOTE outperforms strong ID-based, generative, and multi-interest baselines using item IDs alone. Matched-capacity ablations confirm that performance gains stem directly from the annealed objective, preventing the head collapse observed in conventional multi-head architectures, rather than added capacity, ensembling, or routing.

---


### 168. [Evaluating Priority Dispatch for Premium Membership in On-demand Taxi-sharing](https://arxiv.org/abs/2610.37011)

**<font color=#1a73e8>作者：</font>** Nozomi Yamamoto, Hiroki Sakaji, Itsuki Noda  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we analyze the dispatch-level feasibility of introducing premium membership into an on-demand taxi-sharing service using a sequential optimal insertion method. We propose two dispatch-level methods: deadline shortening for premium users, and deadline shortening with dedicated premium vehicles. We compare them with a baseline dispatch method through SUMO-based simulations under three demand scenarios: steady uniform demand, time-varying demand with a peak period, and urban-focused demand with concentrated peak traffic. Our results show that the suitable priority mechanism depends on operating conditions and premium ratio, suggesting that condition-dependent method switching may provide premium benefits while keeping non-premium-user burden smaller for overall optimization.

---


### 169. [RePAIR: Inverting Backdoor Attacks in Semantic Segmentation](https://arxiv.org/abs/2610.37015)

**<font color=#1a73e8>作者：</font>** Arnold Brosch, Kira Maag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in computer vision, semantic segmentation models remain vulnerable to backdoor attacks, posing a security risk. These attacks redirect pixels of a chosen victim class to an attacker-specified target class when a trigger is present, while preserving clean predictions. Existing defenses are largely derived from image classification, while dedicated segmentation defenses remain scarce and typically require retraining or model modification. We introduce RePAIR, a post-hoc, label-free, attack-unaware defense based on the observation that backdoor-induced shifts can be stronger in the classifier head than in internal representations, leaving recoverable victim-class semantics. RePAIR infers the victim-target relation from an unlabeled, potentially contaminated image pool, constructs a safety-approved semantic reference, and localizes suspicious pixels by comparing head predictions with internal semantic evidence. It then applies feature-space and output corrections toward the inferred victim semantics, while conservative localization and output constraints limit changes to benign predictions. We model the attack as adversarial probability transport and repair as its approximate reversal, deriving bounds and sufficient conditions for localization, residual attack success, clean-side changes, defense-induced target predictions, and attack-unaware pair identification. Experiments across segmentation architectures and attack settings show that RePAIR substantially reduces attack success while largely preserving clean performance.

---


### 170. [Ground-to-Satellite Knowledge Distillation for Crop Classification under Temporal and Geographic Shift](https://arxiv.org/abs/2610.37021)

**<font color=#1a73e8>作者：</font>** Miro Miranda, Rocco Sedona, Valerio Marsocci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous and up-to-date crop type mapping is essential for agricultural monitoring but is often hampered by limited reference data. The growing availability of ground-level field photographs offers a promising way to address this challenge. When combined with satellite time series, these images provide complementary perspectives on the same parcel, capturing crop characteristics from distinctly different perspectives. However, field photographs are not always available for each satellite pixel at inference time, limiting their potential in scalable crop type mapping. We investigate whether ground photographs can provide privileged supervision for crop classification built on pretrained satellite embeddings. A photo teacher based on frozen CLIP features supervises classifiers trained on AlphaEarth and TESSERA representations; photographs are used only during training. On a paired field photo and satellite imagery dataset with 17 crop classes, knowledge distillation consistently improves over satellite-only classification; for frozen embeddings the margin grows under temporal shift, reaching up to +5.5 macro-F1 points, and widens in geographic holdouts (+3.7 vs +3.0 in-distribution). These results show that ground-view supervision can complement satellite embeddings and improve their robustness without changing inference requirements.

---


### 171. [Crop Yield Prediction Using Regression Models: A Comparative Evaluation of Model Performance](https://arxiv.org/abs/2610.37022)

**<font color=#1a73e8>作者：</font>** Saptak Das, Arijit Sarkar, Soumik Neogi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable crop-yield prediction can support agricultural planning and resource allocation. This study evaluates five regression models for predicting crop yield from environmental, crop-related, and agricultural management variables. The dataset initially contained 1,000,000 observations and ten variables, with 231 observations having negative target values removed during preprocessing. Categorical variables were represented using one-hot encoding, and Boolean variables were converted into binary values. The models considered were multiple linear regression (LR), random-forest regression (RF), decision-tree regression (DT), ridge regression, and lasso regression. Their performance was evaluated using 80:20 and 70:30 training-testing splits based on the coefficient of determination (R-squared), mean squared error (MSE), and root mean squared error (RMSE). Applying an 80:20 split, LR achieved a test R-squared of approximately 0.9130 and a test RMSE of 0.5008. Applying a 70:30 split, lasso regression yielded the highest test R-squared (approximately 0.9131) and the lowest test RMSE (approximately 0.5008), with performance almost identical to LR and ridge regression. DT also showed improved test performance under the 70:30 split, whereas RF exhibited a substantial gap between training and testing performance. These results indicate that the evaluated linear regression model provides competitive baselines for this dataset. Further experimentation, including validation testing, will help determine the models' performance and predictability.

---


### 172. [Interpretable Deep Learning Models for Breast Cancer Diagnosis Using Medical Imaging](https://arxiv.org/abs/2610.37026)

**<font color=#1a73e8>作者：</font>** Sami Alnawali, Muhammad Atif Saeed, Abdul Hadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning shows promise for breast cancer diagnosis, but limited interpretability hinders clinical adoption. We benchmark ten ImageNet-pretrained models (ResNet50, VGG19, InceptionV3, DenseNet121, Xception, MobileNetV2, EfficientNet, ConvNeXt, ViT, and Swin Transformer) for benign-versus-malignant classification on the BreakHis histopathology dataset using a patient-level split, and explain their predictions with Grad-CAM, LIME, Integrated Gradients, and LRP. DenseNet121 performed best, with 99.4% test accuracy and an AUC-ROC of 0.999, and significantly outperformed all other models (p < 0.001). Transformer-based models trailed the CNNs. The explanations consistently highlighted nuclei-rich and glandular regions of diagnostic relevance. Combining transfer learning with explainable AI can thus yield accurate, interpretable tools for breast cancer diagnosis.

---


### 173. [GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036)

**<font color=#1a73e8>作者：</font>** Jinxin Ai, Matthias Niessner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inserting virtual objects into scenes reconstructed via 2D or 3D Gaussian Splatting (2DGS/3DGS) is a key capability for content creation, AR, and synthetic data generation. However, realistic insertion requires the object to be seamlessly lit by the scene and, conversely, to cast physically plausible shadows onto it. Existing approaches either harmonize appearance in image space, sacrificing multi-view consistency, or approximate scene illumination with an environment map at the insertion point, which cannot represent near-field area lights such as windows and lamps that dominate indoor lighting. To address this, we present GraftRay, a unified method for physically consistent insertion of mesh objects into indoor scenes represented by either 2D or 3D Gaussians. We recover scene materials and surface normals with diffusion-based priors, and explicitly model spatially-extended emitters, solving their radiance in closed form. A hybrid renderer then jointly path-traces the scene Gaussians and inserted meshes, producing view-consistent shading, interreflections, and soft shadows. On FIPT, GraftRay sets a new state of the art, outperforming recent baselines such as ComGS and EAG-PT in rendering fidelity and shadow accuracy, while maintaining highly competitive rendering efficiency.

---


### 174. [AI-Assisted Discovery of CNOT Decompositions for Quantum Permutations on Constrained Topologies](https://arxiv.org/abs/2610.37045)

**<font color=#1a73e8>作者：</font>** Daniele Lizzio Bosco, Jacopo Cossio, Simone Faro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient quantum circuit compilation is challenging for quantum computers, where limited qubit connectivity can introduce substantial overhead in the implementation of logical operations. Recent AI-assisted synthesis methods have shown considerable potential for reducing circuit complexity, but their role in uncovering principles that can guide the design of new deterministic compilation algorithms remains largely unexplored. In this work, we investigate this perspective for the synthesis of quantum permutations into CNOT circuits under constrained qubit connectivity. Using AlphaCNOT as an exploratory tool, we identify a recurring decomposition for remote transpositions that improves on the construction based on adjacent SWAP routing. For two qubits at graph distance $d>1$, the discovered pattern yields a topology-legal implementation using at most $6d-4$ CNOT gates, compared to the $6d-3$ gates required by the corresponding SWAP-based construction. We formalize this observation through a constructive proof to define Global Transpositions, a deterministic synthesis method that searches for a minimum-cost decomposition of an entire permutation into topology-aware logical transpositions. The resulting method subsumes optimal SWAP routing within its synthesis model and provides certified upper bounds on the topology-constrained CNOT cost. Our experiments also reveal circuits that cannot be expressed as concatenations of independently synthesized transpositions. Instead, these circuits exploit intermediate linear transformations that temporarily leave the permutation subgroup and combine partial effects of multiple logical operations, a mechanism we call intermediate CNOT fusion. Our results show that AI-assisted synthesis can support not only circuit optimization, but also the discovery of reusable identities, provable constructions, and hidden mechanisms in quantum circuit compilation.

---


### 175. [Janus Vehicles: Entity-Centric Threat Modelling of Protocol-Conformant Vehicles under a Malicious-Manufacturer Assumption](https://arxiv.org/abs/2610.37059)

**<font color=#1a73e8>作者：</font>** Jaeung Franciskus Yoo, Huy Kang Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automotive cybersecurity commonly assumes benign end-product manufacturers and design authorities, focusing on supply-chain threats, external attacks, and compromised network participants observable through misbehaviour. This assumption overlooks malicious-by-design vehicles that remain authentic and protocol-conformant while performing undeclared sensing, communication, or context-triggered actuation. We formulate an Entity-Centric Threat Model spanning three subcomponents. The first, Malign Entity Archetypes, describes four types of malign entity: peer-benign, purpose-malicious vehicles; compromised vehicles; reappropriated genuine components; and imitated vehicles or components. The model exposes two assurance gaps: authenticity does not establish declared-purpose conformance, while malicious functionality can evade detection based on behavioural history or peer-visible evidence. Reappropriated components can remain genuine and retain usable identities or capabilities outside authorised contexts, reducing the effectiveness of signal fingerprinting and certificate-based authentication. To structure this threat space, we introduce a Behaviour-Locus Matrix that maps covert, overt, and concealment actions across hardware, software, and network loci. For peer-benign, purpose-malicious vehicles, we further present a Behavioural Interaction Model that represents how hidden capabilities are contextually activated, realised through actions, manifested within the vehicle and its environment, and potentially observed or concealed.

---


### 176. [GKS Fully Homomorphic Encryption: Security Analysis](https://arxiv.org/abs/2610.37061)

**<font color=#1a73e8>作者：</font>** John Graham, Soundes Marzougui, Miloš Pavlović 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> All traditional encryption schemes share a fundamental operational vulnerability: encrypted data must be decrypted before it can be used. Fully homomorphic encryption eliminates this vulnerability by enabling computation directly on encrypted data, but existing FHE schemes impose substantial practical constraints that limit deployment. This paper presents a formal security analysis of the Gribov-Kahrobaei-Shpilrain (GKS) private-key FHE scheme. GKS requires no bootstrapping or de-linearization, produces bit-exact decryption, supports native encrypted search, and scales to unbounded depth.

---


### 177. [Systematic Morphometric Brain Autoencoding for Representation Learning in Neurodegenerative Diseases](https://arxiv.org/abs/2610.37074)

**<font color=#1a73e8>作者：</font>** Nuria Balbás-Esteban, Albert Belenguer-Llorens, Elaheh Moradi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early identification of neurodegenerative disorders using structural T1-weighted MRI is essential for timely clinical intervention, yet supervised deep learning models often struggle to generalize due to limited annotations and scanner-induced distribution shift. Self-supervised learning offers a promising alternative; however, existing approaches are largely adapted from natural image paradigms, relying on contrastive objectives or generic masked reconstruction with voxel-wise losses, which may not fully capture the distributed morphometric patterns associated with neurodegeneration.
We introduce SYMBA (SYstematic Morphometric Brain Autoencoding), a self-supervised pretraining framework specifically designed for structural brain MRI. SYMBA integrates anatomically constrained masking, a multi-scale structural similarity (MS-SSIM) reconstruction objective, and a progressive curriculum that transitions from local anatomical detail to global brain morphology. These components explicitly incorporate neuroanatomical structure into the self-supervised objective rather than relying on generic image priors.
Pretrained on 6,953 T1-weighted MRI scans from nine heterogeneous cohorts, SYMBA is evaluated using frozen linear probing on two independent unseen datasets, enabling a strict assessment of out-of-distribution generalization. Across multiple clinical tasks, SYMBA consistently outperforms recent neuroimaging foundation models, achieving 0.930 AUROC for Alzheimer's disease classification, 0.772 for mild cognitive impairment conversion prediction, and strong performance in amyloid status prediction. In low-label regimes, SYMBA demonstrates high sample efficiency, reaching approximately 0.90 AUROC for AD/CN classification using only six labeled subjects.

---


### 178. [TriDifNet: A Unified Three-Task Diffusion Network for End-to-End RGB-T Perception](https://arxiv.org/abs/2610.37097)

**<font color=#1a73e8>作者：</font>** Qianchao He, Jing Liu, Yunhao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared--visible (IR--VIS) multi-modal perception supports robust scene understanding under challenging illumination. Infrared and visible images are often misaligned due to platform motion, viewpoint changes, and modality-dependent distortions, causing registration errors to propagate into subsequent fusion and detection stages. We propose TriDifNet, a unified three-task diffusion network for end-to-end RGB-T perception. To the best of our knowledge, TriDifNet is the first diffusion-based network that jointly optimizes registration, fusion, and detection for misaligned RGB-T pedestrian perception. TriDifNet consists of three diffusion-based modules, i.e., the Registration Diffusion Module (RegDM), the Fusion Diffusion Module (FusDM), and the Detection Diffusion Module (DetDM). RegDM aligns the unaligned infrared image to the optical reference by estimating a dense deformation field. FusDM performs residual conditional diffusion to generate a detection-oriented fused representation with optical structural cues and complementary infrared saliency. DetDM formulates pedestrian detection as an iterative denoising process in bounding-box space. To couple the three tasks, TriDifNet introduces a closed-loop optimization mechanism, where detection semantics guide fusion and registration, and the fusion result further regularizes geometric alignment. A stage-wise progressive training strategy and a lightweight Nash multi-task learning (Nash-MTL)-based late-stage refinement are further adopted to balance registration, fusion, and detection optimization. Extensive experiments on the KAIST multispectral pedestrian benchmark show that TriDifNet achieves superior downstream detection performance under misaligned RGB-T settings. Against strong system-level competitors, TriDifNet achieves 65.44\% Recall, 57.55\% mAP$_{50}$, and 26.83\% mAP$_{50:95}$.

---


### 179. [A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation](https://arxiv.org/abs/2610.37110)

**<font color=#1a73e8>作者：</font>** Wenwu Tang, Dong Wang, Yun Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution-matching distillation enables high-quality image generation in only a few denoising steps. However, distilled student models often map different initial noise samples to similar outputs under the same prompt. To locate where diversity is lost, we compare the teacher and student along the sampling trajectory. The largest measured reduction in the response to different initial noises occurs during the first, high-noise step. When we replace the first step with the teacher's corresponding trajectory and leave the final three student steps unchanged, most of the output diversity returns. This suggests that the first step is a key point for restoring diversity. Motivated by this finding, we introduce \emph{ReSeed}, a post-distillation method that adds a seed-response bias adapter only to the first student step and aligns its velocity with the teacher's first-interval secant velocity. All student weights and later denoising steps remain unchanged. We evaluate ReSeed on three text-to-image models (SD3-Medium, SD3.5-Medium, and FLUX.1-dev) and one text-to-video model (Wan2.1-T2V-1.3B). For a distilled 4-step FLUX.1-dev model, \emph{ReSeed} requires only $0.00196\%$ additional trainable parameters relative to the base model and is trained on 8,000 prompt--noise pairs, while keeping the distilled student fully frozen and requiring no target images, perceptual losses, or adversarial losses. It improves DINO diversity by $48.3\%$ while maintaining competitive visual quality. These results show that substantial diversity can be recovered through a lightweight, data-efficient tuning of only the first denoising step, without finetuning the full student model.

---


### 180. [SFE-O: An Ontology for Knowledge-Grounded AI in Supercritical CO$_2$ Biomass Extraction and Fractionation](https://arxiv.org/abs/2610.37123)

**<font color=#1a73e8>作者：</font>** Thomas Pallet, Mario Lezoche, Gianpaolo Leone 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supercritical CO$_2$ extraction (CO$_2$-SFE) offers a sustainable route for recovering high-value compounds from biomass while limiting the use of conventional organic solvents, but its design and interpretation require heterogeneous knowledge spanning biomass properties, operating conditions, mass transfer, and product fractionation, typically fragmented across technical reports, engineering models, external databases, and expert practice. This paper introduces SFE-O, a modular Web Ontology Language (OWL 2) ontology for supercritical CO$_2$ biomass extraction, structured around interconnected Biomass, Process, and Product dimensions and extended with explicit representations of process topology, parameter provenance, external and internal mass-transfer phenomena, and the Constant Extraction Rate (CER) / Falling Extraction Rate (FER) mechanisms. Computational dependencies among process quantities are represented explicitly, without embedding numerical solving in the ontology, so that input, measured, computed, externally retrieved, and fitted parameters remain traceable. SFE-O reuses established semantic resources (ChEBI, QUDT, OWL-Time, PROV-O) and is evaluated through a worked example that instantiates a real pilot-scale extraction batch, a reasoner-based consistency check, and a competency-question SPARQL query. The resulting knowledge model provides a machine-actionable foundation for querying, consistency checking, and mechanistic explanation of SFE processes, and establishes a knowledge layer that could support future ontology-grounded AI reasoning, a direction this paper motivates but does not evaluate.

---


### 181. [MCP-Net: Real-Time Coronary Perception Network and Topological Analysis for Robotic Guidewire Navigation](https://arxiv.org/abs/2610.37127)

**<font color=#1a73e8>作者：</font>** Sahar Nasirihaghighi, Tianyuan Wang, Kenan Niu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coronary guidewire navigation during percutaneous coronary intervention requires continuous interpretation of vessel anatomy, guidewire position, and target stenosis under two-dimensional X-ray fluoroscopy. While existing approaches commonly address vessel segmentation or device localization as separate tasks, a robotic system requires a more structured perception of the coronary scene to support downstream navigation. In this work, we present a simulation-driven framework centered on a Multi-Task Coronary Perception Network (MCP-Net) for robotic guidewire navigation, integrating coronary vessel segmentation, vascular topology extraction, and roadmap generation. Starting from three-dimensional coronary CT angiography, we generate simulated fluoroscopy images containing vascular structures, simulated guidewires, stenotic lesions with varying severity, and diverse vascular geometries, together with simulation-derived ground truth. MCP-Net jointly performs coronary vessel segmentation, guidewire-tip localization, and stenosis localization from a single fluoroscopic frame. These predictions are subsequently converted into a structured vascular graph containing centerlines, bifurcations, endpoints, branch directions, and branch angles. By associating the predicted stenosis with this graph, the framework generates a roadmap from the automatically selected graph root toward the target lesion. The results demonstrate that the proposed framework can jointly recover coronary perception targets and transform them into an interpretable vascular representation suitable for downstream robotic navigation.

---


### 182. [Science-Fiction Transformation as a Design Lens for Visualization Transformation](https://arxiv.org/abs/2610.37131)

**<font color=#1a73e8>作者：</font>** Abdulhaq Adetunji Salako, Christian Tominski  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Science fiction often features characters or objects that undergo radical changes in form while still being recognizable as the same entity. For example, a vehicle might unfold into a robot, or one body might flow or shape-shift into another. We use such transformations as a reflective lens to study similar shape-shifting in visualization, where one visual representation transforms into a completely different one. For example, a node-link diagram might transform into a parallel coordinates plot as a user's task changes from understanding relationships to identifying correlations. Based on four instances of science-fiction transformation, our paper highlights two key questions: First, why is a transformation into a target form needed, or what is the purpose? Second, what remains recognizable across the transformation from source to target, or what is the correspondence? Through four hypothetical transitions between visual representations of a multifaceted dataset, we demonstrate that purpose is also essential to visualization transformations. Furthermore, we show that the question of correspondence results in different levels of complexity in terms of designing and understanding transitions. Depending on whether correspondence is 1:1, 1:N, or N:1, visualization transformations may be direct and easy to understand, or they may require more elaborate transition constructs, implying increased cognitive effort for interpretation. Particularly, cases of 1:N and N:1 correspondence pose challenges for designing visualization transformations.

---


### 183. [MRI-to-CT Translation of Spinal Images via Anatomy-Guided Pseudo-Pairing and Adversarial Diffusion](https://arxiv.org/abs/2610.37134)

**<font color=#1a73e8>作者：</font>** Eduardo Nieto, Ibai Genua, Davide Scorza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) is routinely used to diagnose spinal disorders, but surgical planning often requires Computed Tomography (CT) for better visualization of vertebral bone anatomy. Synthesizing CT from MRI could avoid additional radiation exposure and streamline preoperative assessment.
We propose a three-stage framework for spine MRI-to-CT synthesis. First, an anatomy-guided vertebral matching system identifies similar sagittal MRI and CT slices using spine segmentations and aligns them through rigid registration, creating pseudo-paired data from unpaired scans. Second, these pairs train an adversarial diffusion model for MRI-to-CT translation. Third, synthesized slices are assembled into 3D volumes and refined by a network that improves inter-slice continuity and structural coherence.
The framework was trained on over 10,000 unpaired sagittal MRI and CT slices and evaluated on 1,911 slices from 83 MRI volumes spanning all spinal regions. Assessment combined distribution-based measures with vertebral segmentation metrics. Compared with diffusion alone, the proposed approach increased binary 3D vertebral Dice from 0.666 to 0.739. Volumetric post-processing reduced visible discontinuities between stacked slices and improved vertebral coherence in axial and coronal views.
Combining anatomy-guided pseudo-pairing, adversarial diffusion and 3D refinement improves spine MRI-to-CT synthesis. Vertebral matching primarily enhanced anatomical alignment and fidelity, while volumetric refinement improved 3D consistency. These findings support further development of MRI-derived CT-like visualization for preoperative planning, particularly to preserve fine intensity details while maintaining volumetric coherence.

---


### 184. [Physics Guided Diffusion Model Based Exposure Interpolation for High Dynamic Range Imaging](https://arxiv.org/abs/2610.37135)

**<font color=#1a73e8>作者：</font>** Zhengguo Li, Chaobing Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ghosting artifacts are an open problem for popular multi-shot based high dynamic range (HDR) imaging. An effective solution is to capture two large-exposure-ratio (LER) standard dynamic range (SDR) images simultaneously via a single-shot. Brightness order reversal (BOR) artifacts are generated when the two LER images are directly fused together. It is crucial to interpolate an image with an exposure time in between the exposure times of two LER images. In this paper, a novel physics-guided diffusion model based exposure interpolation algorithm is proposed to address the BOR artifacts. An initial image is interpolated by a physics-driven component, and the residual high-frequency details are generated by a new diffusion model based component. The new diffusion model is based on the correlation analysis of generative models and includes a new predicted target to reduce the variation of the Pearson correlation between the noisy data and the target, as well as the amplification factor of the fitting error. Compared with existing neural augmented exposure interpolation algorithms on top of convolution neural networks, the proposed exposure interpolation algorithm has an inherent advantage to generate more high frequency information. Experiment results validate the proposed exposure interpolation algorithm.

---


### 185. [MixSIS: Mixed-supervised instance segmentation](https://arxiv.org/abs/2610.37138)

**<font color=#1a73e8>作者：</font>** Christian Wilms, Emre Gülsoylu, Sven Schreiber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly-supervised instance segmentation (WSIS) based on either box-, point-, or image-level annotations has been proposed to overcome the labor-intensive annotation process in fully-supervised instance segmentation. Despite decent results, most WSIS methods only focus on a single annotation level, ignoring that some objects are easy to spot from point annotations, while others require box or even mask annotations. Therefore, we propose the Mixed-Supervised Instance Segmentation (MixSIS) task, which allows a flexible mix of annotation levels (image, point, box, and mask) within a dataset. MixSIS has a high practical relevance, as it allows optimizing the annotation process by annotating challenging objects in more detail, while saving time on simpler instances with less detailed annotations. To address MixSIS, we propose AnnotationsMixer (AnnsMixer) as a baseline. AnnsMixer is a truly mixed-supervised instance segmentation system, which generates pseudo mask annotations from all annotation levels, even mixed within a single image. We evaluate AnnsMixer on both WSIS and MixSIS tasks, largely outperforming state-of-the-art methods. In three case studies, we also demonstrate how the unique features of MixSIS and AnnsMixer can substantially reduce the annotation time (-90%) or improve the results (+34%) in instance segmentation with a simple annotation rule or leveraging heterogeneous data. Our code is available at this https URL

---


### 186. [Generative Replay for Equilibrium Propagation: Toward Edge-Friendly Continual Learning in Hopfield Networks](https://arxiv.org/abs/2610.37139)

**<font color=#1a73e8>作者：</font>** Victor Cook, Gilles Sassatelli, Thierry Gil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equilibrium Propagation (EqProp) offers a biologically grounded and hardware-aligned alternative to backpropagation for training Hopfield Networks. However, its behavior in continual learning settings remains largely unexplored. This work confronts catastrophic forgetting in EqProp-trained Hopfield Networks from the inside out, eliminating the need for external data buffers or architectural overhead that standard Experience Replay \textbf{(ER)} and Generative Replay \textbf{(Gen-Replay)} inevitably require. We introduce an Energy-Based Generative Replay strategy \textbf{(EB-Gen)} which exploits the intrinsic generative dynamics of Hopfield Networks, allowing a single model to act as both classifier and replay samples generator. Samples capturing past task knowledge are generated by relaxing a frozen copy of the network, enabling rehearsal solely through internally generated pseudo-data. We evaluate the proposed method in the Class-Incremental setting, using the split versions of the MNIST and CIFAR10 benchmarks and compare it with FineTune, Experience Replay, Generative Replay, Sleep-Like Replay Consolidation (SRC) and Joint training. Our results show that EB-Gen significantly improves stability while preserving plasticity, achieving a 75\% and 64\% average accuracy on Split MNIST and Split CIFAR10 respectively. These findings show that Equilibrium Propagation can be adapted to alleviate catastrophic forgetting without forgoing the traits which made it compelling in the first place.

---


### 187. [Beyond Parameter Protection: Fisher-Shaped EWC for Replay-Free Continual Learning](https://arxiv.org/abs/2610.37145)

**<font color=#1a73e8>作者：</font>** Liying Wang, Simone Magistri, Joost van de Weijer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In replay-free continual learning, Elastic Weight Consolidation (EWC) uses Fisher information matrix (FIM) to protect acquired knowledge by penalizing changes to historically important parameters. However, a local importance estimate at the retained solution does not in general characterize sensitivity after finite parameter displacement. This motivates controlling Fisher sensitivity over a neighborhood of potential future updates. We propose Fisher-Shaped EWC (FS-EWC), which extends the role of FIM from parameter protection to solution formation for future retention. During task learning, FS-EWC minimizes the worst-case empirical FIM trace within a prescribed neighborhood, explicitly favoring solutions that are less sensitive to bounded future displacement. At task completion, trajectory-based model merging constructs the retained solution from multiple optimization states rather than a single terminal iterate, after which FIM is estimated for subsequent consolidation. Experiments across multiple benchmarks show that FS-EWC improves performance over EWC, while controlled studies indicate a more favorable stability--plasticity balance and greater tolerance to parameter drift. These results suggest that effective knowledge retention requires both forming solutions with future retention in mind and protecting acquired knowledge.

---


### 188. [Variational Optimal Control for Diffusion Guidance](https://arxiv.org/abs/2610.37146)

**<font color=#1a73e8>作者：</font>** Ruoyu Wang, Xinyi Ye, Yunshuo Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a variational control framework that connects sampling-time guidance and reward-based model adaptation through a shared Jacobian pullback. Starting from terminal reward maximization with a path-space KL penalty, the Gibbs variational principle and Doob transform yield a correction to the generative dynamics. A local denoising approximation exposes the pullback that transports output preferences to the controlled variable. This construction gives Variational Optimal Guidance (VOG) in state space and extends to Distilled Variational Optimal Control (DVOC) by amortizing locally improved endpoints into model parameters. The resulting controls share a local variational rule: VOG acts through the denoising Jacobian, while DVOC realizes the parameter pullback by endpoint distillation. Under a linear MMSE model, VOG's exact correction lies in the data subspace. On ImageNet, VOG reduces DiT-XL/2 FID from 2.27 to 2.04 at 250 sampling steps and from 7.58 to 4.44 at 25 steps. After 20 updates on Z-Image-Turbo, DVOC improves HPSv3++ and four held-out evaluator scores over the untrained model, with the highest corresponding means among the trained methods compared. These results connect inference-time control and reward adaptation through a common geometric principle.

---


### 189. [GCSR-OCC: Geometry Calibration and Semantic Routing for Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2610.37149)

**<font color=#1a73e8>作者：</font>** Bohua Wang, Congyang Zhao, Tianxiong Lv 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D occupancy prediction represents scene geometry and semantics in a unified voxel grid, enabling recognition beyond predefined categories. One approach reconstructs scenes with 3D Gaussians and converts them into voxel occupancy. However, Gaussian scale inflation and excessive overlap can distort voxel occupancy predictions, while semantic mixing can arise within Gaussians spanning multiple categories and during 3D--2D semantic feature alignment. We propose GCSR-OCC, which combines geometry calibration and multi-mode query-conditioned semantic routing for indoor occupancy prediction from a single RGB image. The Evidence-Conserving Gaussian-to-Occupancy operator (EC-G2O) uses kernel mass normalization, $p$-norm aggregation, and a learnable gain to suppress scale inflation and excessive local evidence accumulation while calibrating occupancy responses. Multi-mode Query-First Gaussian Semantic Routing (MM-QGSR) matches multiple semantic modes per Gaussian to text queries and aggregates query-specific evidence into voxels through a learnable text-conditioned router. Fine-grained subclass queries and smoothed semantic aggregation further refine voxel-level predictions. Without 3D semantic annotations, GCSR-OCC achieves state-of-the-art performance in open-vocabulary occupancy prediction on Occ-ScanNet, with 63.31% geometric IoU and 27.44% semantic mIoU. It also reduces geometric aggregation latency from 19.76 ms to 12.88 ms. Our code will be made publicly available.

---


### 190. [FastBEVFusion: Simple Multi-Modal Fusion for 3D Object Detection at 50 FPS](https://arxiv.org/abs/2610.37153)

**<font color=#1a73e8>作者：</font>** Tom Sanitz, Emre Gülsoylu, Simone Frintrop 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable real-time 3D object detection based on LiDAR and camera data is critical for safety in autonomous driving, where systems must accurately perceive their surroundings with minimal latency. Many state-of-the-art systems achieve high-quality detection results but fail to meet real-time constraints, limiting their practical use. To address this challenge, we propose FastBEVFusion, a simple, fast, and robust fusion system for 3D object detection. Based on modality-specific features, FastBEVFusion projects these features into semi-aligned modality-specific BEV spaces, without relying on a computationally intensive and potentially error-prone depth estimation. Given these BEV spaces, we propose a light-weight, soft, and dynamic fusion module based on cross-attention, which adapts dynamically to the scene context and enables feature fusion across the entire BEV spaces. Experiments on the complex nuScenes dataset show that FastBEVFusion outperforms state-of-the-art real-time systems, and achieves over 50 FPS without deployment libraries. Additionally, our system shows strong robustness to calibration errors, making FastBEVFusion a powerful 3D object detection system for real-world applications.

---


### 191. [Rènyi-Regularized Flow-Based Variational Inference for Bayesian Calibration](https://arxiv.org/abs/2610.37169)

**<font color=#1a73e8>作者：</font>** Exaucè Luweh Adjim Ngarti, Élise Arnaud, Léo Nicoletti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Variational inference with normalizing flows provides a flexible posterior approximation for Bayesian model calibration, but struggles when the posterior has several modes separated by regions of low probability mass. We study this behavior in a two-parameter twin experiment and regularize the variational objective. Under Gaussian observation errors and a Gaussian prior, the corresponding minimization objective is the expected Tikhonov calibration objective minus the differential entropy of the approximating distribution. However, the expected Tikhonov term favors concentration near one of the modes, while entropy maximization does not guarantee multimodality. We introduce a regularization term based on Rényi divergence that encourages the approximate posterior to cover the prior support. In the connected bimodal case, a flow approximation represents both modes; in the case with well-separated modes, the flow and Gaussian mixture frequently miss one mode. The introduced regularization reduces the near-collapse fraction from 50% to 25%. While the regularization improves mode coverage in this experiment, it changes the Bayesian variational objective, introduces a trade-off in approximation accuracy, and does not provide a general solution to mode collapse.

---


### 192. [INTR++: INterpretable TRansformer with better Accuracy, Interpretability, and Adaptability](https://arxiv.org/abs/2610.37178)

**<font color=#1a73e8>作者：</font>** Dipanjyoti Paul, Arpita Chowdhury, Maneet Chatterjee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpretable Transformers often perform well in domain specific settings but lose effectiveness beyond that. Achieving ViT-like broad applicability requires models with consistent performance across domains. Recent works on Interpretable Transformers, INTR and Prompt-CAM, were developed keeping domain adaptability in mind. Prompt-CAM leverages learnable prompts to promote adaptability. However, these prompts are fixed in nature and therefore struggle to adapt to domains with substantial variation in input image characteristics, resulting in reduced interpretability. To address this limitation, we propose INTR++, which extends Prompt-CAM by incorporating a lightweight Prompt Adapter Module (PAM). PAM enables prompts to be adaptive by enriching them with domain-specific knowledge, thereby ensuring consistent interpretability across diverse domains including those with varying image characteristics such as medical imaging, micro-scopic imaging, and remote sensing imagery. INTR++ retains the standard architecture and end-to-end learning of Interpretable Transformer based models, while adding only a small number of additional parameters compared to Prompt-CAM. We demonstrate that INTR++ delivers consistent improvements in all aspects across domains like animals, plants, medical imaging, microscopic imaging, remote sensing imagery and object-centric data.

---


### 193. [Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution](https://arxiv.org/abs/2610.37201)

**<font color=#1a73e8>作者：</font>** Jiawei Zhou, Bo Peng, Yuxuan Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill optimizers adapt an agent to long-horizon tasks, such as repairing a terminal environment, by rewriting its skill, a natural-language procedure in its context, and keeping the edits that raise success on a small dev set. On such tasks success is noisy, so a gain on a small dev set does not show that an edit helps, and a success score does not show what the edit costs. We introduce BiPA, which replays an optimizer's acceptance rule on candidates identical to its seed to measure what selection alone reports, and records each episode as a bipartite graph of turns and the text they read to trace extra input tokens to the behavior behind them. Across three optimizers, three agentic benchmarks and two models, the learned skills succeed about as often as their hand-written seed, 0.1 points higher on average. Their dev gains vanish on test: keeping the best of several candidates on at most 30 tasks reports gains this large even when none changed. They read about 16% more input tokens: the optimizers almost always add rules, half to re-check work and some to act one call at a time, and the agent follows them as extra turns, each re-sending the whole conversation. Four principles follow: accept an edit only if its gain exceeds what selection alone reports; charge it for the turns it adds, not for its length; let the editor delete and merge rules; show it what earlier rules cost. Code is available at this https URL.

---


### 194. [TopoField: Technical Report for ECCV 2026 SceneFun3D Challenge](https://arxiv.org/abs/2610.37218)

**<font color=#1a73e8>作者：</font>** Zhiwei Chen, Zhiheng Fu, Zixu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional segmentation requires locating small interactive parts, such as knobs, buttons, and sockets, in indoor point clouds and returning confidence-ranked instance masks. A point-wise semantic predictor produces a continuous probability field, whereas the benchmark evaluates a discrete set of scored instances. This creates a substantial field-to-instance gap. We present TopoField, a deterministic decoder built on top of VOLT. TopoField first converts 13 test-time forward passes into a semantic consensus field, then decodes instance candidates from the consensus geometry, and finally ranks the candidates in a class-aware manner. The augmentation stage retains the processed-point identity of every fragment prediction, accumulates probabilities in a common point array, normalizes by coverage count, and fuses the resulting caches. The decoding stage separates high-confidence cores from broader support regions, constructs a symmetric radius-pruned point graph, and uses a multi-source graph-geodesic partition to split support regions that contain multiple seeds. On 561 ground-truth instances across 30 validation scenes, an IoU-0.5-valid candidate exists for 67.2% of instances, and top-1 coverage is 20.0%. These complementary measurements motivate joint attention to candidate construction and ranking. TopoField achieves 28.286% AP, 41.383% AP50, and 47.558% AP25. TopoField achieved second place on the ECCV 2026 SceneFun3D Challenge.

---


### 195. [Sharpness-Aware Muon: Matrix-Aware Optimization with Momentum-Guided Perturbations](https://arxiv.org/abs/2610.37225)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhai, Wenjing Yan, Ying-Jun Angela Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is a matrix-aware optimizer that combines momentum with orthogonalization to produce structured update directions with strong empirical behavior. However, it only shapes the geometry of the update itself and does not explicitly control neighborhood worst-case loss or bias training toward flat regions, which are often linked to stronger generalization. To address this limitation, we introduce the sharpness-aware formulation of Muon. We first develop \textsc{MuSAM}, which incorporates Sharpness-Aware Minimization (SAM)-style perturbation into Muon's orthogonalized update and establishes a principled bridge between sharpness-aware training and matrix-aware optimization. We then show that this formulation faces an efficiency--stability tension: constructing the perturbation requires an extra gradient evaluation, while the perturbation itself is generated from a single minibatch gradient and is therefore noisy. To resolve this issue, we propose \textsc{MoMuSAM}, which turns Muon's momentum from an update variable into a sharpness-probing signal. By using normalized momentum as the perturbation direction, \textsc{MoMuSAM} removes the extra clean-gradient computation and replaces the single-batch perturbation proxy with a temporally aggregated one. We prove that both \textsc{MuSAM} and \textsc{MoMuSAM} attain the same asymptotic first-order stationarity order, and further show that \textsc{MoMuSAM} yields a more stable stochastic linearization than \textsc{MuSAM}. Experiments on standard benchmarks demonstrate that sharpness awareness consistently improves Muon.

---


### 196. [Subspace Clifford Networks](https://arxiv.org/abs/2610.37226)

**<font color=#1a73e8>作者：</font>** Zhongping Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose Subspace Clifford Networks, a reformulation that replaces global cyclic rolling with grouped subspace interactions. Instead of sampling sparse cyclic diagonals across the entire $D$-dimensional channel space, we project the features into an aligned space $\R^{\tilde{D}} = \bigoplus_{g=1}^{G} V_g$ partitioned into $G$ low-dimensional groups $V_g \cong \R^k$ with $k \in \{2, 3, 4\}$. Within each $k$-dimensional group, we compute all $\binom{k}{2}$ wedge coordinates and concatenate them with $\operatorname{SiLU}$-activated coordinate-wise products, while sandwiching the grouped interaction between learnable $1\times 1$ linear projections to enable cross-group channel mixing. This design reduces intermediate feature expansion from $2|\mathcal{S}|D$ (typically $10D$ for 5 shifts) down to $1.5\tilde{D}$ ($k=2$), $2.0\tilde{D}$ ($k=3$), or $2.5\tilde{D}$ ($k=4$). Furthermore, exploiting the small, fixed group size $k \in \{2, 3, 4\}$, we implement a fused CUDA kernel that evaluates the forward interaction and a recomputation-based analytical backward pass using thread-local variables without allocating global-memory buffers for elementwise intermediates. Finally, we extend the backbone from an isotropic columnar layout to a multi-resolution Hierarchical Clifford Network with configurable per-stage subspace dimensions. Experiments on CIFAR-100 show that the proposed models substantially reduce parameter count and training time across both regimes, while the hierarchical variants also improve classification accuracy over the evaluated shift-based hierarchical baselines.

---


### 197. [Asynchronous Verifiable and Complete Secret Sharing: From Design Patterns to System-Level Trade-offs](https://arxiv.org/abs/2610.37234)

**<font color=#1a73e8>作者：</font>** Joachim Bruneau-Queyreix, Martin Zivojinovic, Leo Mendiboure 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern secret sharing protocols promise robust secret sharing in fully asynchronous Byzantine systems, but their practical costs remain difficult to compare across papers, assumptions, and workloads. The difficulty is not merely experimental: protocols with similar asymptotic guarantees often place very different work on the critical path through their choices of dissemination, verification, batching, and recovery. This paper turns that fragmented research landscape into a corpus-backed designspace analysis and systems evaluation of asynchronous verifiable and complete secret sharing. We derive a design sieve, select seven representative protocols, and implement them in a common Rust framework. In our experiments on the Grid'5000 platform, we evaluate honest-dealer and faulty-dealer stress executions using latency, throughput, message count, bandwidth, and aggregate CPU-time. The results show that message complexity alone poorly predicts latency, that optimistic paths can be dominated by recovery cost, and that batching or packing helps only when verification stays off the critical path. These findings turn protocol-by-protocol comparisons into design-to-cost guidance for choosing, implementing, and extending asynchronous verifiable and complete sharing protocols.

---


### 198. [HDVS: semi-supervised semantic segmentation via heterogeneous dual-branch voting supervision](https://arxiv.org/abs/2610.37236)

**<font color=#1a73e8>作者：</font>** Yongqi Shan, Yunzhi Zhuge, Huchuan Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised semantic segmentation, which aims to utilize large volumes of unlabeled images to achieve accurate segmentation results with fewer human annotations, has attracted increasing attention. Prior methods were primarily based on the assumption that the pseudo-labels generated by each branch were sufficiently reliable to supervise the remaining branches. However, there is a concern that the errors in pseudo-labels could accumulate during co-training, potentially resulting in suboptimal performance. To this end, we present a novel framework called heterogeneous dual-branch voting supervision (HDVS), which is designed to enhance the reliability of pseudo-labels and mitigate the issues arising from pseudo-labeling. Specifically, based on the cross-supervision framework, we introduce a voting mechanism that correlates pseudo-labels from heterogeneous branches to produce pseudo-labels with enhanced reliability. Concurrently, we employ a feature communication module to introduce perturbations at the feature level in each branch to maximize prediction diversity across the dual branches while maintaining convergence. Comprehensive evaluations of the proposed HDVS on two benchmark datasets (PASCAL VOC 2012 and Cityscapes) demonstrate its superiority to the state-of-the-art approaches.

---


### 199. [When Is a Relation Worth Trusting? Manipulation Costs, Exposure, and the Trust Trap in Multi-Relational Graph Learning](https://arxiv.org/abs/2610.37239)

**<font color=#1a73e8>作者：</font>** Vincess Dongmo, Astride Melvin Fokam Ninyim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-relational graph detectors learn from clean data how much to trust each relation, but an adversary pays a different price to manipulate each relation and each action; taking such costs as given, we ask when using a relation is worse than ignoring it. Our first main result proves that degree gating strictly beats every selection or reweighting of a relation when part of the population is isolated on it and the attacker cannot afford to open the gate, and that this window is sharp; on real graphs, validated gating gains exactly on the relations that meet these conditions and nowhere else. Our second shows that a per-node exposure bound, which extends to message passing, tells a platform which relation to harden: exposure per unit cost, computed without any attack, picks the relation whose hardening raises the exact trap threshold most in 15 of 16 cases, against at most 7 for informativeness, cheapness, or an analysis with equal edit costs. Supporting tools give exact worst cases for linear relational models, certified brackets for R-GCN and tree ensembles, and a finite-sample guarantee for adversarial validation, under which clean-trained graph detectors fall below their graph-free counterparts in 58 of 90 settings on six graphs. A selection protocol built on these results is never significantly worse than ignoring the graph; with at most four relations it mostly abstains, as validation alone would, and its cost-aware proposals help when relations are many, so far shown on synthetic graphs. Without cost information, the safe choice is to abstain.

---


### 200. [TCM-DiagCommit: A TCM-SD-Derived Benchmark for Evidence-Conditioned Syndrome Selection and Commitment](https://arxiv.org/abs/2610.37243)

**<font color=#1a73e8>作者：</font>** Erwei Hou, Yue Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional Chinese Medicine (TCM) syndrome differentiation is usually evaluated as static final-label selection over complete clinical records. This setting hides three diagnostic behaviors: whether a model distinguishes semantic-neighbor syndrome labels from easy random distractors, whether it updates predictions as evidence fields are revealed, and whether it should commit under uncertainty. We introduce TCM-DiagCommit, a benchmark derived from the public TCM-SD/ZY-BERT resource while retaining its source syndrome labels; it converts 1,834 source cases into 23,842 task rows over 148 syndrome labels. The benchmark combines random, profile-neighbor, and full-vocabulary candidate ladders with staged t1/t2/t3 evidence. It also includes fixed-label tongue/pulse perturbations and insufficient-evidence variants. A benchmark-defined action contract scores commit, acquire, defer, and abstain. Across five zero-shot DirectLLM calibrations, random10 top-1 accuracy is 63.2% to 66.4%, but hard20 falls to 24.7% to 30.3% and full148 to 14.8% to 22.3%; on hard20, WT(all) wrong-terminal commits remain 62.2% to 74.3%. These results show that final-answer accuracy alone is insufficient for diagnostic benchmark evaluation: answer selection, evidence use, and benchmark commitment scoring should be measured separately.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-257](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
