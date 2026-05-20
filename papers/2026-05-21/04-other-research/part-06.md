# 📦 其他研究 | 2026年05月21日

> 本类共 **338** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-338](./part-07.md)

---

### 251. [Depth2Pose: A Pose-Based Benchmark for Monocular Depth Estimation without Ground-Truth Depth](https://arxiv.org/abs/2605.19797)

**<font color=#1a73e8>作者：</font>** Viktor Kocur, Sithu Aung, Gabrielle Flood 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation has improved significantly in recent years, driven by increasingly powerful models and large-scale training data. Predicted depth is increasingly used as an input signal for downstream tasks such as Structure-from-Motion (SfM), visual localization, and SLAM. However, monocular depth estimators (MDEs) are still primarily evaluated in terms of depth accuracy. Standard metrics aggregate errors globally and may not reflect the usefulness of depth for downstream geometric tasks. We therefore propose Depth2Pose, a framework for evaluating MDEs in the context of downstream tasks. By combining depth predictions with feature correspondences in depth-aware geometric solvers, we use relative camera pose estimation accuracy as a task-driven proxy for depth quality. Traditional benchmarks require dense ground truth in the form of per-pixel depth, which is expensive to obtain. In contrast, our formulation requires only camera poses, which can be estimated efficiently, e.g., using Structure-from-Motion pipelines. As a result, our framework can be applied to scenes where ground-truth depth is difficult to obtain, for example due to large scene scale or heavy occlusions (e.g., vegetated environments). Leveraging this, we introduce the D2P dataset, which contains challenging scenes outside the distribution of commonly used training data. We show that methods performing well under standard depth error metrics on existing benchmarks also perform well under our pose-based metric when evaluated on the same datasets, but do not necessarily generalize to our more challenging dataset. Finally, we provide a simple and extensible evaluation framework. The dataset and code are available at this http URL.

---


### 252. [Latent Laplace Diffusion for Irregular Multivariate Time Series](https://arxiv.org/abs/2605.19805)

**<font color=#1a73e8>作者：</font>** Zinuo You, Jin Zheng, John Cartlidge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular multivariate time series impose a trade-off for long-horizon forecasting: discrete methods can distort temporal structure via re-gridding, while continuous-time models often require sequential solvers prone to drift. To bridge this gap, we present Latent Laplace Diffusion (LLapDiff), a generative framework that models the target as a low-dimensional latent trajectory, enabling horizon-wide generation without step-by-step integration over physical time. We guide the reverse process utilizing a stable modal parameterization motivated by stochastic port-Hamiltonian dynamics, and parameterize its mean evolution in the Laplace domain via learnable complex-conjugate poles, enabling direct evaluation over irregular timestamps. We also link continuous dynamics to irregular observations through renewal-averaging analysis, which maps sampling gaps to effective event-domain poles and motivates a gap-aware history summarizer. Extensive experiments show that LLapDiff improves over baselines in long-horizon forecasting, and its continuous-time generative nature supports missing-value imputation by querying the same model at historical timestamps. Code is available at this https URL.

---


### 253. [Chunking German Legal Code](https://arxiv.org/abs/2605.19806)

**<font color=#1a73e8>作者：</font>** Max Prior, Natalia Milanova, Andreas Schultz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates chunking strategies for retrieval-augmented generation on German statutory law, using the German Civil Code as a structured benchmark corpus. We implement and compare a range of segmentation approaches, including structural units (sections, subsections, sentences, propositions), fixed-size windows, contextual chunking, semantic clustering, Lumber-style chunking, and RAPTOR-based hierarchical retrieval. All methods are evaluated on a legal question-answering dataset with section-level gold labels, measuring recall, query latency, index build time, and storage requirements. Results show that chunking strategies aligned with the inherent legal structure - particularly section and subsection - based retrieval-achieve the highest recall, while more complex approaches that override this structure perform worse. These simpler methods also offer favorable computational efficiency compared to LLM-intensive techniques such as contextual chunking, RAPTOR, and Lumber. The findings highlight a key trade-off between semantic enrichment and operational cost, and demonstrate that preserving domain-specific structure is critical for effective legal information retrieval.

---


### 254. [LionMuon: Alternating Spectral and Sign Descent for Efficient Training](https://arxiv.org/abs/2605.19811)

**<font color=#1a73e8>作者：</font>** Arman Bolatov, Artem Riabinin, Nikita Kornilov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large-scale optimization, the cheapness and effectiveness of update steps are the most crucial factors for a successful optimizer. Sign-based optimizers like Lion or Signum produce cheap per-step updates, whereas Muon's spectral matrix-sign update gives a much stronger direction at a substantially higher per-step cost. In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods. It alternates between Lion's and Muon's updates on a fixed period P, sharing a single dual-EMA momentum buffer between them. The optimizer state memory therefore matches Lion and is exactly half of AdamW's. A simpler single-EMA variant, SignMuon, by itself already outperforms pure Muon. At P = 2, LionMuon Pareto-dominates Muon, Lion, Signum, and AdamW on every dataset and architecture we tested at 124M model size, reaching lower validation loss at lower compute, and the same advantage persists at 355M and 720M scale. On the theory side, we prove sharp complexity bounds under heavy-tailed noise which are governed by period-averaged smoothness and noise that interpolate between Muon's and Lion's constants. These bounds predict the compute-optimal period and the conditions under which LionMuon outruns Muon and Lion. Code: this https URL

---


### 255. [FLUXtrapolation: A benchmark on extrapolating ecosystem fluxes](https://arxiv.org/abs/2605.19812)

**<font color=#1a73e8>作者：</font>** Anya Fries, Jacob A Nelson, Martin Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce FLUXtrapolation, a benchmark for extrapolating ecosystem fluxes under progressively harder distribution shifts. Ecosystem fluxes are central to understanding the carbon, water, and energy cycles, yet they can only be measured directly at sparsely located measurement towers. Producing global flux estimates therefore requires training models on observed sites using globally available covariates and predicting in unobserved regions, that is, upscaling. Flux upscaling is a challenging domain generalization problem that is affected by a shift in covariate distribution across climates, ecosystem types, and environmental conditions, as well as by conditional shift: important drivers remain unobserved at global scale. We provide a quantitative analysis of both these shifts in $P_X$ and $P_{Y\mid X}$. FLUXtrapolation is designed based on domain expertise on flux upscaling: it defines temporal, spatial, and temperature-based extrapolation scenarios and evaluates performance across held-out domains, temporal aggregations, and tail errors. In a pilot study, we find that baselines perform similarly under median hourly RMSE, but separate under the proposed tail-focused and multi-scale evaluation. FLUXtrapolation therefore poses a realistic and thus relevant challenge for machine learning methods under distribution shift; at the same time, progress on this benchmark would directly support the scientific goal of improving flux upscaling.

---


### 256. [General Lower Bounds for Differentially Private Federated Learning with Arbitrary Public-Transcript Interactions](https://arxiv.org/abs/2605.19813)

**<font color=#1a73e8>作者：</font>** Yicheng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove a general lower bound for differentially private federated learning protocols with arbitrary public-transcript interactions. The protocol may use any number of adaptive rounds, and each client's local samples may be reused across rounds. For parameter estimation under squared \(\ell_2\) loss, we establish a federated van Trees lower bound for every estimator satisfying a total clientwise sample-level zero-concentrated differential privacy (zCDP) constraint. The main technical ingredient is a privacy-information contraction inequality for complete public transcripts. We illustrate the bound through applications to mean estimation, linear regression, and nonparametric regression.

---


### 257. [LP-Eval: Rubric and Dataset for Measuring the Quality of Legal Proposition Generation](https://arxiv.org/abs/2605.19815)

**<font color=#1a73e8>作者：</font>** Shanshan Xu, Johan Lindholm, Amogh Raina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal proposition generation is central to legal reasoning and doctrinal scholarship, yet remain under-examined in Legal NLP. This paper investigates the automatic generation and evaluation of legal propositions from decisions of the Court of Justice of the European Union using large language models (LLMs). We introduce LP-Eval, a three-step evaluation rubric co-designed with legal experts that decomposes legal proposition quality into formal validity and substantive dimensions. Using this rubric, we release a dataset of two experts' annotations for 100 LLM-generated legal propositions. Our results show that LLMs can generate predominantly well-formed and high-quality propositions, while expert evaluations reveal higher quality for propositions derived from well established cases than from recent ones. We further examine LLMs as evaluators and find that rubric-guided LLM judgments align more closely with expert assessments than direct overall scoring, but remain insensitive to finer-grained distinctions captured by human experts.

---


### 258. [LaCoVL-FER: Landmark-Guided Contrastive Learning Network with Vision-Language Enhancement for Facial Expression Recognition](https://arxiv.org/abs/2605.19821)

**<font color=#1a73e8>作者：</font>** Jiaxin Wang, Muwei Jian, Hui Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Expression Recognition (FER) in the wild is still challenging due to uncontrolled variations in pose, occlusion, and illumination. Most existing attention-based methods primarily rely on visual appearance cues, suffering from attention redundancy and instability, which limits their performance in complex scenarios. To address these issues, we propose a novel landmark-guided contrastive learning network with vision-language enhancement for FER (LaCoVL-FER), which integrates geometric priors from facial landmarks and semantic priors from a vision-language model. Specifically, a Landmark-Guided Adaptive Encoder (LGAE) is designed to introduce geometric priors through a Bi-branch Gated Cross Attention (BGCA) mechanism, which achieves adaptive fusion of landmark-based geometric and visual appearance features to produce expression-relevant features, thereby focusing on key facial regions and suppressing noise interference. In parallel, a Vision-Language Enhancement Strategy (VLES) is presented to leverage the expression-relevant features to refine the generalizable visual features extracted by the frozen pretrained CLIP image encoder, yielding expression-specific visual representations. Based on these representations, an Expression-Conditioned Prompting (ECP) mechanism is utilized to further adapt the textual features of fixed class-level prompts from the frozen pretrained CLIP text encoder, generating more instance-aware textual representations. These visual-textual representations are aligned as semantic priors to enhance the robustness and generalization of FER. Quantitative and qualitative experiments demonstrate that our LaCoVL-FER outperforms state-of-the-art methods on three representative real-world FER datasets, including RAF-DB, FERPlus, and AffectNet. The code is available at this https URL.

---


### 259. [ST-TGExplainer: Disentangling Stability and Transition Patterns for Temporal GNN Interpretability](https://arxiv.org/abs/2605.19822)

**<font color=#1a73e8>作者：</font>** Hongjiang Chen, Xin Zheng, Pengfei Jiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph neural networks (TGNNs) have gained significant traction for solving real-world temporal graph tasks. However, their interpretability remains limited, as most TGNNs fail to identify which historical interactions most influence a given prediction. Despite promising progress on interpretable TGNNs, existing methods predominantly focus on previously seen historical interactions, which we term stability patterns, while overlooking newly emerging first-time interactions, which we term transition patterns. Both types of patterns are essential for faithful temporal explanations. To address this limitation, we propose ST-TGExplainer, a self-explainable TGNN that disentangles Stability and Transition patterns in temporal graphs for a more faithful Temporal GNN Explainer. Guided by a disentangled information bottleneck objective, ST-TGExplainer learns a compact explanatory subgraph that remains predictive of the event label while explicitly suppressing label-conditioned redundancy between stability and transition patterns. Extensive experiments demonstrate that ST-TGExplainer achieves strong predictive performance and yields more faithful explanations. Code is available at this https URL.

---


### 260. [Smooth Piecewise Cutting for Neural Operator to Handle Discontinuities and Sharp Transitions](https://arxiv.org/abs/2605.19823)

**<font color=#1a73e8>作者：</font>** Ha Dang, Sebastian Schmidt, Juergen Hesser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have achieved strong performance in learning solution operators of partial differential equations (PDEs), but their inherently continuous representations struggle to capture discontinuities and sharp transitions. Existing approaches typically approximate such features within continuous function spaces, often requiring increased model capacity and high-resolution data. In this work, we propose Cut-DeepONet, a two-stage training framework that explicitly models discontinuities while reducing learning complexity. Our approach reformulates the problem via a lifting strategy, partitioning the domain into smooth subregions while representing discontinuities as boundaries in a higher-dimensional space. This separation aligns the operator learning task with the inductive bias of neural networks and avoids directly approximating discontinuities. An additional network predicts input-dependent discontinuity locations for unseen inputs, which are then used to guide the neural operator in generating smooth components within each region. Experiments on benchmark PDEs show that Cut-DeepONet outperforms state-of-the-art methods, even when trained on low-resolution datasets. The method excels on problems with discontinuities and sharp transitions, while using fewer trainable parameters. Our results highlight the benefits of changing the representation of operator learning rather than increasing model complexity.

---


### 261. [Explainable Wastewater Digital Twins: Adaptive Context-Conditioned Structured Simulators with Self-Falsifying Decision Support](https://arxiv.org/abs/2605.19826)

**<font color=#1a73e8>作者：</font>** Gary Simethy, Daniel Ortiz Arroyo, Petar Durdevic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operators of safety-critical industrial processes increasingly rely on digital twins to screen control interventions, but such simulators rarely carry certified safety guarantees. Wastewater treatment plants exemplify the gap: operators face a daily safety-efficiency trade-off where aerating too little risks effluent violations and nitrous-oxide (N2O) spikes, and aerating too much wastes energy. We develop an explainable digital twin for aeration and dosing setpoints. CCSS-IX, the simulator, is a bank of interpretable locally linear state-space "experts" adaptively mixed by a context-aware gating network, building on a continuous-time regime-switching scaffold. A runtime decision layer applies conformal risk control to abstain, reopen, or return a falsifying temporal witness for any operator-proposed action that cannot be statistically certified. The artificial-intelligence contribution is twofold: an identifiable, context-conditioned structured surrogate that retains operator-readable dynamics, and a self-falsifying decision rule with finite-sample coverage guarantees. The engineering contribution is a validated, end-to-end decision-support pipeline, tested on a 1000-step slice of the Avedøre full-scale plant (42.6% sensor missingness, 2-minute sampling), the Agtrup/BlueKolding full-scale plant in Denmark, and the Benchmark Simulation Model No. 2 (BSM2) international benchmark, under a matched ten-seed protocol. The static structured ensemble lies within 0.78% root-mean-square error of an unconstrained black-box reference, and the adaptive variant within 1.08%. The calibrated reopen rule cuts aggregate two-plant regret by 43.6% at an unsafe-action cost weight of 4 and eliminates unsafe chosen actions on the BSM2 main slice. Event-aligned temporal witnesses prevent 93 of 187 false-safe N2O approvals, about 4.65x the dyadic baseline (paired McNemar p < 1e-21).

---


### 262. [Set-Valued Policy Learning](https://arxiv.org/abs/2605.19830)

**<font color=#1a73e8>作者：</font>** Laura Fuentes-Vicente, Mathieu Even, Gaëlle Dormion 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional treatment policies map patient covariates to a single recommended intervention in order to maximize expected clinical outcomes. Although a rich body of causal inference methods has been developed to estimate such policies, point-valued recommendations can be highly sensitive to estimation uncertainty, model specification, and finite-sample variability, while typically providing little guidance about how confident one should be in the recommended action. In this work, we propose a set-valued policy learning paradigm for the multiple-treatment setting, in which policies output a set of plausible treatments rather than a single recommendation. This formulation enables intrinsic uncertainty quantification, with the size of the predicted set reflecting the degree of decision ambiguity. We extend the learning-to-defer framework to multiple treatments via a novel \textit{greatest Lower Bound} method, and introduce \textit{conformal policy learning}, which bridges the gap between unobserved ground-truth optimal treatments and estimated optimal treatment rules. Drawing on insights from the noisy-label literature, we develop a randomness-injection approach that guarantees marginal coverage without requiring assumptions on underlying black-box optimal treatment rules. Through experiments on synthetic data and a real-world application to In-Vitro Fertilization (IVF), we demonstrate that our methods produce robust and actionable policies that naturally incorporate clinical considerations while effectively balancing performance and reliability.

---


### 263. [Material for Thought: Generative AI as an Active Creative Medium](https://arxiv.org/abs/2605.19832)

**<font color=#1a73e8>作者：</font>** Hugo Andersson, Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI collaboration research has largely positioned the human as a judge of AI output, centering effort on evaluating whether rec- ommendations are reliable enough to accept. This decision-support framing leaves little room for the human as creator. We argue that for creative work, this framing misdirects human effort toward eval- uating correctness rather than exploring and shaping the creative space. Drawing on Schön's theory of reflective practice, we propose an alternative: treating generative AI as an active creative medium. As a potter works with clay, humans Shape, Observe, Stir, and Se- lect (SOSS) their medium through ongoing conversation. Where generative AI actively tends toward convergence and resolution, the human role of disruption and curation becomes essential for sustaining creative quality. We present a creative writing probe, Loom, in which users orchestrate simulated narrative agents. We also introduce the SOSS framework for this mode of engagement, and discuss design implications.

---


### 264. [A Closed-loop, State-centric, Multi-agent Framework for Passenger Load Estimation from Heterogeneous Data Streams](https://arxiv.org/abs/2605.19834)

**<font color=#1a73e8>作者：</font>** Yiyao Xu, Hao Zhou, Yuhang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To support operations and passenger-facing services, transit agencies need reliable passenger load trajectories. Currently, load estimates are typically inferred from imperfect sensing systems rather than fully observed, and the accuracy of modern automatic passenger counting (APC) systems still varies with station layout, flow intensity, and operating conditions. To address the challenges of robust passenger load estimation from heterogeneous data streams, including incremental count errors, evidence conflicts, and context-dependent sensor reliability, we propose a closed-loop, state-centric, multi-agent framework. This method enforces physical feasibility at every step, allocates trust dynamically among evidence sources, and feeds physics-derived violation residuals back into training for robustness improvement. The architecture consists of a unified stop-event backbone, a coupled Perception--Physical--Fusion loop for stop-by-stop inference, and optional trip-level macro-correction and closed-loop calibration modules.

---


### 265. [CADENet: Condition-Adaptive Asynchronous Dual-Stream Enhancement Network for Adverse Weather Perception in Autonomous Driving](https://arxiv.org/abs/2605.19837)

**<font color=#1a73e8>作者：</font>** Sherif Khairy, Catherine M. Elias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather (rain, fog, sand, and snow) degrades camera-based object detection in autonomous vehicles. Existing enhancement-then-detect approaches stall the safety-critical perception loop, violating hard real-time requirements. Progress on this problem is also constrained by an under-recognized evaluation ceiling: ground truth annotated on degraded images cannot credit a detector that recovers objects the annotators themselves could not see, so a genuinely useful enhancement can register as a near-flat F1 gain. This paper presents CADENet (Condition-Adaptive Asynchronous Dual-stream Enhancement Network), a training-free three-thread system: Thread S (YOLOv11n) delivers detections at full frame rate with zero added latency; Thread Q applies condition-adaptive enhancement (CAPE) and fuses results via entropy-guided NMS (EG-NMS) without blocking Thread S; Thread E provides CLIP zero-shot weather classification, so new weather categories require only a new text prompt, with no labeled data and no retraining. Evaluated on 1327 DAWN images (YOLOv11m, IoU = 0.5, confidence = 0.25), CADENet achieves Recall = 0.0103 (micro), F1 = 0.0230 on snow, and F1 = 0.0038 on rain. We formalize the annotation completeness bias on DAWN-class data, so the reported F1 values are lower bounds on the true gain; recall is the annotation-gap-immune headline metric. Thread S sustains approximately 44 FPS regardless of enhancement load. No model retraining or additional sensor hardware is required.

---


### 266. [From Role to Person: Trust Calibration Challenges in Twin Agents](https://arxiv.org/abs/2605.19838)

**<font color=#1a73e8>作者：</font>** Hugo Andersson, Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic AI has taken on the role of assistant, collaborator, and decision-support tool. We argue the next role on that list is more personal: you. These are digital twins of each individual -- twin agents -- representing their knowledge, perspective, and communicative style to colleagues when they are unavailable. Drawing on early design work in an ongoing project in which agents represent knowledge workers in a professional setting, we identify a trust calibration problem specific to this approach. When a human colleague doubts a twin agent's output, they face three failure modes (a schema gap, an epistemic gap, and a model artifact) with no reliable attribution path between them. Cognitive forcing functions and related frameworks address overreliance effectively in contexts where there is a clear boundary between the AI and the human decision-maker. However, twin agents dissolve that boundary, raising a class of trust calibration challenge these frameworks were not designed to handle. We introduce the concept, distinguish it from digital twins, and outline the research questions this new class of agent demands.

---


### 267. [When Preference Labels Fall Short: Aligning Diffusion Models from Real Data](https://arxiv.org/abs/2605.19839)

**<font color=#1a73e8>作者：</font>** Weiyan Chen, Weijian Deng, Yao Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preference alignment aims to guide generative models by learning from comparisons between preferred and non-preferred samples. In practice, most existing approaches rely on preference pairs constructed from model-generated images. Such supervision is inherently relative and can be ambiguous when both samples exhibit artifacts or limited visual quality, making it difficult to infer what constitutes a truly desirable output. In this work, we investigate whether real data can serve as an alternative source of supervision for preference alignment. We adopt a data-centric perspective and study a curation strategy that treats real images as reference points and constructs preference signals by contrasting them with generated or perturbed samples, without requiring manually annotated preference pairs. Through empirical analysis, we show that real-data-based supervision provides effective guidance for aligning diffusion models and achieves performance comparable to existing preference-based methods. Our results suggest that real data offers a practical and complementary source of supervision for preference alignment and highlight directions of label-efficient alignment strategies. Code and models are available at this https URL.

---


### 268. [Fast Tensorization of Neural Networks via Slice-wise Feature Distillation](https://arxiv.org/abs/2605.19842)

**<font color=#1a73e8>作者：</font>** Safa Hamreras, Sukhbinder Singh, Román Orús  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a scalable tensorization framework for neural network compression based on slice-wise feature distillation. Unlike conventional tensor decomposition methods that rely on costly global finetuning, our approach decomposes the network into slices consisting of either individual layers or blocks (e.g., convolutional layers or MLPs), or small groups of consecutive layers, and tensorizes each slice independently to reproduce the intermediate representations of the original pretrained model. This modular strategy improves accuracy recovery, reduces data requirements, and enables efficient parallel optimization. Experiments on ResNet-34 show significant gains over conventional global tensorization, achieving near-lossless compression at moderate compression rates with faster optimization. Results on GPT-2 XL further demonstrate the scalability of the method and its applicability to large-scale models, particularly in distributed settings.

---


### 269. [CLIF: Concept-Level Influence Functions for Transparent Bottleneck Models](https://arxiv.org/abs/2605.19848)

**<font color=#1a73e8>作者：</font>** Yike Sun, Mingkun Xu, Mu You 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, the black-box nature of deep learning models has limited their application in high-stakes domains such as medical diagnosis and finance, where interpretability is essential. To address this, we propose a novel approach using influence functions to enhance interpretability in NLP models at both the sample and concept levels. Experiments on CEBaB and Yelp datasets show that influence functions effectively identify the most impactful training samples, both helpful and harmful, on model predictions. By adjusting the labels and weights of these samples, we demonstrate that model performance can be restored to baseline levels without retraining, confirming the value of influence functions for efficient data debugging. Furthermore, our concept-level analysis identifies key concepts within Concept Bottleneck Models (CBM) that significantly affect predictions. Modifying these concepts alters model behavior observably, providing clear insights into the decision process.

---


### 270. [A Framework for Evaluating Zero-Shot Image Generation in Concept-based Explainability](https://arxiv.org/abs/2605.19855)

**<font color=#1a73e8>作者：</font>** Giacomo Astolfi, Matteo Bianchi, Riccardo Campi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept-based Explainable Artificial Intelligence (XAI) interprets deep learning models using human-understandable visual features (e.g., textures or object parts) by linking internal representations to class predictions, thereby bridging the gap between low-level image data and high-level semantics. A major challenge, however, is the reliance on large sets of labeled images to represent each concept, which limits scalability. In this work, we investigate the use of zero-shot Text-to-Image (T2I) generative models as a source of synthetic concept datasets for concept-based XAI methods. Specifically, we generate concepts using predefined prompts and evaluate their faithfulness to real ones through four complementary analyses: (1) comparing synthetic vs. real concept images via concept representation similarity; (2) evaluating their intra-similarity by comparing pairs of subsets of the same concept with progressively increasing size; (3) evaluating their performance for downstream explanation tasks using relevant class images; (4) evaluating how removing a concept from tested class images affects explanations of generated concepts. While current T2I generative models promise a shortcut to concept-based XAI, our study highlights challenges and raises open questions about the use of synthetic data generated by zero-shot pipelines in model analyses. The resulting dataset is available at this https URL.

---


### 271. [StableGrad: Backward Scale Control without Batch Normalization](https://arxiv.org/abs/2605.19856)

**<font color=#1a73e8>作者：</font>** Jose I. Mestre, Alberto Fernández-Hernández, Cristian Pérez-Corral 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training very deep neural networks requires controlling the propagation of magnitudes across depth. Without such control, activations and gradients may vanish, explode, or enter unstable regimes that make optimization fail. Modern architectures often mitigate this problem through Batch Normalization, residual connections, or other normalization layers, which repeatedly re-scale or bypass intermediate representations. However, these mechanisms are not always appropriate. In Physics-Informed Neural Networks (PINNs), the network represents a continuous physical field and its input derivatives define the training objective, making batch-dependent normalization problematic because it can introduce non-local dependencies into the predicted field and its derivatives. We propose StableGrad, an optimizer-level scale-control mechanism that corrects layer-wise weight-gradient imbalances without modifying the forward model. Because the normalization is applied only after backpropagation and before the optimizer update, the network output, its derivatives, and the physical residual remain unchanged. We analyze the effective training dynamics induced by this rescaling and evaluate StableGrad on deep PINNs as the target application, with BatchNorm-free convolutional networks serving as a diagnostic stress test. On PINN benchmarks, StableGrad improves matched-depth solution accuracy and makes deeper models more reliable under standard optimization. On ResNet and EfficientNet architectures, where removing Batch Normalization normally leads to training collapse, StableGrad stabilizes optimization without introducing any other architectural change. These results show that optimizer-level control of weight-gradient scale can provide a practical alternative when forward normalization is unavailable or undesirable.

---


### 272. [Landscape-Awareness for Geometric View Diffusion Model](https://arxiv.org/abs/2605.19865)

**<font color=#1a73e8>作者：</font>** Yan-Ting Chen, Hao-Wei Chen, Tsu-Ching Hsiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate camera viewpoint estimation under sparse-view conditions remains challenging, particularly in two-view scenarios. Recent approaches leverage diffusion models such as Zero123 to synthesize novel views conditioned on relative viewpoint, showing promising results when repurposed for viewpoint estimation via optimization with MSE loss. However, existing methods often suffer from nonconvex loss landscape with numerous local minima, making them sensitive to initialization and reliant on naive multistart strategies. We analyze these optimization challenges and visualize failure cases, showing that geometric ambiguities, such as symmetry and self-similarity, can mislead gradient-based updates toward incorrect viewpoints. To address these limitations, we propose a score-based method that reshapes the optimization landscape to guide updates toward the ground-truth viewpoint, followed by a refinement stage using a viewpoint-conditioned diffusion model. Experiments show that our method improves convergence, reduces reliance on brute-force sampling, and achieves competitive accuracy with higher sample-efficiency.

---


### 273. [Structured Layout Priors for Robust Out-of-Distribution Visual Document Understanding](https://arxiv.org/abs/2605.19866)

**<font color=#1a73e8>作者：</font>** Peter El Hachem, Ahmed Nassar, A. Said Gurbuz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) parse documents end-to-end but frequently break down on layouts unlike those seen in training. We attribute this to a two-hop bottleneck: before the decoder can extract content (Hop 2), it must first classify and localize the enclosing layout entity (Hop 1), and when the first hop fails the second collapses into omissions, malformed structure, or autoregressive repetition. We pre-resolve Hop 1 outside the decoder by running a lightweight RT-DETR detector, serializing its outputs in the parser's native DocTags vocabulary, and injecting them into the prompt alongside the full page image. Unlike analyze-then-parse approaches that crop the page, or prior prompt-level priors written in plain text, our prior shares the decoder's generation space and leaves the global image in view as a fallback when detections are noisy. On a 10k-page structural out-of-distribution benchmark, markdown F1 rises from $0.37$ to $0.92$; on the Chinese subset of OmniDocBench, table TEDS rises from $0.01$ to $0.36$; and on the 26k-page ViDoRe V3 benchmark, infinite-loop decoding failures drop across every industrial domain tested. These gains cost $15\%$ wall-clock latency and a median of $74$ prompt tokens, with no architectural change to the base VLM. An attention-level analysis further reveals a bimodal phase shift in which the decoder attends to injected layout tokens when emitting structure and to image patches when emitting content, consistent with the two-hop bottleneck being alleviated. Model weights will be released to support reproducibility.

---


### 274. [WoundFormer: Multi-Scale Spatial Feature Fusion for Multi-Class Wound Tissue Segmentation](https://arxiv.org/abs/2605.19868)

**<font color=#1a73e8>作者：</font>** Muhammad Ashad Kabir, Rabin Dulal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chronic wounds such as diabetic foot ulcers and pressure injuries require accurate tissue-level assessment to guide treatment planning and monitor healing progression. While deep learning methods have advanced automated wound analysis, most existing approaches focus on binary segmentation and inadequately model heterogeneous tissue composition due to high intra-class variability and limited annotated data. Multi-class wound tissue segmentation, therefore, remains a challenging and clinically relevant problem. We propose WoundFormer, a transformer-based framework that enhances hierarchical spatial feature fusion for multi-class wound tissue segmentation. Specifically, we replace the standard SegFormer decoder with a spatially-preserving multi-scale aggregation head that maintains feature topology during cross-scale integration and strengthens contextual interactions through convolutional fusion. This design improves boundary localization and discrimination between visually similar tissue categories while preserving transformer efficiency. We evaluate WoundFormer on the WoundTissueSeg dataset (147 images, six tissue classes) and a second benchmark (DFUTissue dataset). The proposed method achieves an overall Dice score of 81.9%, outperforming strong CNN- and transformer-based baselines by up to 4.3 Dice points on the WoundTissueSeg benchmark, with consistent improvements across minority tissue classes. These results indicate that explicit modeling of hierarchical spatial interactions enhances transformer representations for heterogeneous wound tissue segmentation and supports more reliable quantitative wound assessment.

---


### 275. [Passive Construction Site Safety Monitoring via Persona-Scaffolded Adversarial Chain-of-Thought VLM Verification](https://arxiv.org/abs/2605.19869)

**<font color=#1a73e8>作者：</font>** Ananth Sriram, Neel Mokaria, Rajveer Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Construction remains the deadliest industry sector in the United States, with 1,055 fatal worker injuries recorded in 2023, and the majority preventable. Existing monitoring approaches are expensive, require real-time human operators, or address only a narrow subset of violations. This paper presents a passive, end-of-shift construction safety monitoring pipeline processing video from POV body-worn and fixed wall-mounted cameras through a three-stage architecture: (1) fine-tuned YOLO11 for primary PPE and hazard detection, (2) SAM 3 for segmentation refinement and worker deduplication, and (3) Qwen3-VL-8B-Instruct with a method-prompted, persona-scaffolded three-pass adversarial chain-of-thought protocol for compliance verification and hallucination control. The principal contribution is the Stage 3 prompt design: professional persona backstories following the method-actor framing drive an observed 12% precision improvement over single-pass prompting in an informal three-author review of the 12-video Ironsite development corpus, with the largest gains on hallucination-prone violation categories. Structural message isolation enforces observational independence between a generator, discriminator, and reconciliation pass governed by asymmetric rules encoding priors about human observation versus automated detection reliability. The system maps violations to OSHA standards, performs REBA-inspired ergonomic risk scoring from pose keypoints, and produces per-worker safety reports with timestamped evidence. An evaluation harness is released for future reproduction.

---


### 276. [Structural Energy Guidance for View-Consistent Text-to-3D Generation](https://arxiv.org/abs/2605.19876)

**<font color=#1a73e8>作者：</font>** Qing Zhang, Jinguang Tong, Jing Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-3D generation based on diffusion models often suffers from the Janus problem, leading to inconsistent geometry across viewpoints. This work identifies viewpoint bias in 2D diffusion priors as the main cause and proposes Structural Energy-Guided Sampling (SEGS), a training-free and plug-and-play framework to improve multi-view consistency. SEGS constructs a structural energy in the PCA subspace of U-Net features and injects its gradient into the denoising process. It can be easily integrated into SDS/VSD pipelines without retraining. Experiments show that SEGS reduces the Janus Rate by about 10% on average and improves View-CS scores across multiple baselines, including DreamFusion, Magic3D, and LucidDreamer. This method effectively alleviates viewpoint artifacts while preserving appearance fidelity, providing a flexible solution for high-quality text-to-3D content generation.

---


### 277. [GoTTA be Diverse: Rethinking Memory Policies for Test-Time Adaptation](https://arxiv.org/abs/2605.19890)

**<font color=#1a73e8>作者：</font>** Shyma Alhuwaider, Yasmeen Alsaedy, Merey Ramazanova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) enables a pre-trained model to adapt online to an unlabeled test stream under distribution shift. While most TTA research focuses on the adaptation objective, practical streams also depend critically on the memory used to select which test samples drive adaptation. Existing memory mechanisms are usually evaluated as components of specific TTA algorithms, making it difficult to isolate which memory design choices matter and when they matter. In this work, we provide a systematic benchmark that decouples memory from the adaptation algorithm and evaluates memory policies under unified conditions across i.i.d., non-i.i.d., continual, and practical test streams. Our study shows that effective memory management requires more than retaining recent or class-balanced samples. In particular, intra-class diversity is a key factor for avoiding redundant buffers and maintaining representative adaptation signals under temporally correlated and label-skewed streams. Motivated by this finding, we introduce Guided Observational Test-Time Adaptation (GOTTA), a family of diversity-aware memory policies that combine class-balanced allocation with feature-space diversity. GOTTA memories act as drop-in replacements for existing buffers and can be paired with different TTA objectives. Across corruption benchmarks and video-stream settings, diversity-aware memory improves adaptation most clearly under constrained memory budgets and challenging non-i.i.d. streams, while remaining competitive as memory capacity increases. These results highlight memory management as a first-class component of robust test-time adaptation and identify diversity as a central principle for practical TTA.

---


### 278. [Streamlined Constraint Reasoning via CNN Pattern Recognition on Enumerated Solutions](https://arxiv.org/abs/2605.19895)

**<font color=#1a73e8>作者：</font>** Patrick Spracklen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint programming practitioners accelerate hard problems through a layered set of techniques applied in order of risk. Standard hardening (symmetry-breaking and implied constraints) is applied first and preserves satisfiability. Streamliner constraints, which restrict search to a structural sub-family of solutions, do not preserve satisfiability and are reserved as a final lever. Existing automated streamliner-synthesis approaches either search a constraint grammar or prompt a Large Language Model directly on the problem model. We propose a different approach: enumerate feasible solutions, train a Convolutional Neural Network contrastively against perturbed non-solutions to detect structural patterns, and translate the CNN's discriminative signal into candidate MiniZinc streamliners through LLM-driven synthesis. The CNN grounds the LLM's constraint generation in observed solution structure rather than model text alone. We evaluate on hardened benchmark models where streamliner discovery is the residual performance lever. Our pipeline achieves 98.8% portfolio time reduction on hardened Vessel Loading, 98.6% on hardened Social Golfers, and 89.4% on Black Hole, with best-single streamliners reaching geometric-mean speedups of 932x, 356x, and 1103x respectively. Discovered streamliners include class-based packing constraints on Vessel Loading, beyond-hardening canonicalisations on Social Golfers, and layout-coordinate bounds on Black Hole.

---


### 279. [reconCTI: A Proactive Approach to Cyber-Threat Intelligence](https://arxiv.org/abs/2605.19899)

**<font color=#1a73e8>作者：</font>** Mohammed Mahir Rahman, Shahzad Memon, Tauseef Ahmed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of information technology has introduced a noticeable shift from traditional offline practices to more efficient and interconnected online environments. This transition, while offering convenience, has also increased exposure to various cyber threats such as identity theft, impersonation, and phishing scams. Reconnaissance, or briefly known as information gathering, is a key stage for threat actors, often relying on open-source intelligence (OSINT) to collect sensitive and extensive data on targets. In response to this challenge, this study introduces reconCTI, a command-line tool built using Python for Linux systems. The tool is designed to search for sensitive data leaks across both surface web and dark web platforms. It allows users to input specific keywords, scan multiple sites at once, and then assess the findings by referencing the MITRE ATT&CK framework. The results are compiled into a threat report that also includes possible mitigation strategies. reconCTI is intended to support both cybersecurity professionals and individuals in identifying risks early and taking appropriate action.

---


### 280. [Hierarchical Contrastive Learning for Multi-Domain Protein-Ligand Binding](https://arxiv.org/abs/2605.19902)

**<font color=#1a73e8>作者：</font>** Shuo Zhang, Rongqi Hong, Huifeng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting protein-ligand binding affinity remains intractable for multi-domain proteins, where inter-domain dynamics govern molecular recognition. Existing geometric deep learning methods typically treat proteins as monolithic static graphs, suffering from rigid-body assumptions and aleatoric noise in flexible regions. To address this, we introduced HCLBind, a self-supervised framework that decouples geometric representation learning from affinity regression. HCLBind leverages a general-to-specific pre-training paradigm on the Q-BioLiP database to learn a robust physical grammar of binding. We propose a novel hierarchical decoy strategy: the model learns local physicochemical constraints through protein coordinate perturbation in single-domain proteins and global conformational geometry through inter-domain rotation in multi-domain complexes. Our hybrid architecture integrates a domain-gated graph attention network and cross-modal attention to explicitly prioritize domain interfaces. Furthermore, we employ LoRA on protein and ligand foundation models, ensuring efficient optimization while preserving evolutionary knowledge. Experiments on PDBBind demonstrate that HCLBind effectively learns discriminative interface features and provides robust uncertainty estimation, overcoming the limitations of standard supervised learning. The code is available at this https URL.

---


### 281. [Fast and Featureless Node Representation Learning with Partial Pairwise Supervision](https://arxiv.org/abs/2605.19916)

**<font color=#1a73e8>作者：</font>** Sujan Chakraborty, Saptarshi Bej  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Contrastive FUSE, a fast and unified framework for scalable node representation learning in graphs with partially available pairwise node labels and no available node features. Unlike existing methods, we directly optimize a spectral contrastive objective that integrates community-aware structural signals with signed pairwise constraints. To support large-scale training, we replace the expensive modularity gradient with a lightweight approximation, which preserves the structure-seeking behavior of modularity while reducing the computational cost significantly. This yields an efficient optimization scheme with a natural gradient decomposition and adaptive learning-rate scaling, enabling fast iterative updates even on million-edge graphs. Extensive experiments on benchmark citation networks, large co-purchase graphs, and OGB datasets show that Contrastive FUSE achieves competitive or superior contrastive classification performance without relying on node features, while offering substantial runtime gains over existing baselines. These results highlight the effectiveness of coupling modularity-inspired structural learning with contrastive supervision for efficient and scalable contrastive node representation learning.

---


### 282. [JAXenstein: Accelerated Benchmarking for First-Person Environments](https://arxiv.org/abs/2605.19926)

**<font color=#1a73e8>作者：</font>** Ruo Yu Tao, George Konidaris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The progression of reinforcement learning algorithms have been driven by challenging benchmarks. The rate in which a researcher can iterate on a problem setting directly impacts the speed of algorithm development. Modern machine learning has produced tools that allow for fast and scalable algorithm development like the JAX library. With the availability of these tools, a serious bottleneck in algorithm development is the availability of large and complex domains for experimentation. Most notably, the JAX reinforcement learning ecosystem does not have any benchmarks that test visual first-person tasks; these domains are crucial for testing both exploration and an agent's ability to overcome partial observability. We introduce JAXenstein: an open-source JAX-based benchmark that implements the Wolfenstein 3D rendering engine for fast and scalable experimentation in visual first-person tasks. JAXenstein is several times faster than comparable vision-based benchmarks, and is easily extensible to more complex first-person domains.

---


### 283. [StruMPL: Multi-task Dense Regression under Disjoint Partial Supervision and MNAR Labels](https://arxiv.org/abs/2605.19931)

**<font color=#1a73e8>作者：</font>** Reza M. Asiyabi, Juan Alberto Molina-Valero, SEOSAW Partnership 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating forest aboveground biomass (AGB) from Earth observation combines two structurally incompatible label sources: spaceborne lidar provides canopy structure at millions of locations but no biomass estimate, and ground-based plots provide biomass at thousands of biased locations but no metrics of structure. No single training sample carries labels for all target variables, plot labels are missing not at random (MNAR), and biomass is linked to the structural variables by known but biome-specific allometric laws. We formalise this as multi-task dense regression under heterogeneous disjoint partial supervision with MNAR labels and inter-task physical constraints, and propose StruMPL to address it jointly. A shared encoder feeds per-variable regression, imputation, and propensity heads for spatial MNAR correction, and a learnable physics module that evaluates the inter-task constraint on the model's own predictions at every pixel. The supervised loss uses an Augmented IPW (AIPW) pseudo-outcome with stop-gradients on the propensity and on the imputation baseline; we show analytically and empirically that both are necessary for joint optimisation to recover IPW-weighted stationary points while keeping the loss bounded. On two ecologically distinct biomes, StruMPL outperforms ablation variants and the closest published method on AGB RMSE and bias, with a stratified analysis showing AIPW reduces high-AGB bias by ~54%.

---


### 284. [Probabilistic Tiny Recursive Model](https://arxiv.org/abs/2605.19943)

**<font color=#1a73e8>作者：</font>** Amin Sghaier, Ali Parviz, Alexia Jolicoeur-Martineau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tiny Recursive Models (TRM) solve complex reasoning tasks with a fraction of the parameters of modern large language models (LLMs) by iteratively refining a latent state and final answer. While powerful, their deterministic recursion can lead to convergence at suboptimal solutions, without escape mechanism. A common workaround relies on task-specific input perturbations at test time combined with answer aggregation via voting. We introduce Probabilistic TRM (PTRM), a task-agnostic framework for test-time compute scaling that addresses this limitation through stochastic exploration. PTRM injects Gaussian noise at each deep recursion step, enabling parallel trajectories to explore diverse solution basins, and selects among them using the model's existing Q head (used for early stopping in the original TRM). Without requiring retraining or task-specific augmentations, PTRM enables substantial accuracy gains across benchmarks, including Sudoku-Extreme (87.4% to 98.75%) and on various puzzles from Pencil Puzzle Bench (62.6% to 91.2%). On the latter, PTRM achieves nearly double the accuracy of frontier LLMs (91.2% vs. 55.1%) at less than 0.0001x the cost, using only 7M parameters.

---


### 285. [A Measure-Theoretic Analysis of Reasoning: Structural Generalization and Approximation Limits](https://arxiv.org/abs/2605.19944)

**<font color=#1a73e8>作者：</font>** Yuyang Zhang, Yifu Zhang, Xuehai Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While empirical scaling laws for LLM reasoning are well-documented, the theoretical mechanisms governing out-of-distribution (OOD) generalization remain elusive. We formalize reasoning via optimal transport, projecting discrete trajectories into a continuous metric space to quantify domain shifts using the Wasserstein-1 distance. Invoking Kantorovich duality, we bound OOD generalization via architectural Lipschitz continuity and functional approximation limits. This exposes two primary constraints. First, position-dependent attention (e.g., Absolute Positional Encoding) fails to preserve shift invariance, yielding an $\Omega(1)$ Lipschitz constant and expected risk, whereas shift-invariant mechanisms (e.g., Rotary Embeddings) preserve equivariance and bound the error. Second, by mapping sequential backtracking to a Dyck-$k$ language, we establish a strict circuit depth lower bound for $\text{TC}^0$ Transformers. Scaling physical layer depth is necessary to avert representation collapse -- a constraint that scaling representation width cannot bypass due to irreducible approximation bounds in Barron spaces. Evaluations across 54 Transformer configurations on combinatorial search corroborate these bounds, demonstrating that generalization risk degrades monotonically with the Wasserstein domain shift.

---


### 286. [Exploiting Non-Negativity in DAG Structure Learning](https://arxiv.org/abs/2605.19947)

**<font color=#1a73e8>作者：</font>** Samuel Rey, Madeline navarro, Gonzalo Mateos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work addresses the problem of learning directed acyclic graphs (DAGs) from nodal observations generated by a linear structural equation model. DAG learning is a central task in signal processing, machine learning, and causal inference, but it remains challenging because acyclicity is a global combinatorial property. Continuous acyclicity constraints have led to important algorithmic advances by replacing the discrete DAG constraint with smooth equality constraints. However, existing formulations still involve difficult non-convex optimization landscapes and may suffer from degenerate first-order optimality conditions. Here, we restrict attention to DAGs with non-negative edge weights and exploit this additional structure to obtain a simpler characterization of acyclicity. Building on this characterization, we formulate a regularized non-negative DAG learning problem and develop an algorithm based on the method of multipliers. We further analyze the benign optimization landscape induced by non-negativity. In the population regime, we show that the true DAG is the unique global minimizer of the proposed augmented-Lagrangian formulation; moreover, the landscape contains no spurious interior stationary points, and the true DAG is the only acyclic KKT point. Numerical experiments on synthetic and real-world data show that the proposed method improves over state-of-the-art continuous DAG-learning alternatives.

---


### 287. [Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949)

**<font color=#1a73e8>作者：</font>** Dongli Wu, Zhuoxiao Li, Tongyan Hua 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing large-scale urban scenes from sparse aerial views is a crucial yet challenging task. Due to biased top-down and shallow-oblique camera poses, sparse aerial captures exhibit strong evidence imbalance: roofs and open regions are repeatedly observed, while facades, distant buildings, and occluded structures receive little multi-view support. Existing feed-forward 3D Gaussian Splatting methods directly regress a deterministic representation from sparse inputs, but this often leads to ghosting, melted facades, and stretched textures. Recent pseudo-view and video-based generative reconstruction methods use additional supervision or generative priors. However, they often lack a clear separation between observed geometry and prior-driven content, which can lead to plausible but inconsistent structures. We propose AnyCity, an observation-grounded generative reconstruction framework for sparse aerial urban scenes. AnyCity first predicts an observation-supported geometry latent to anchor reliable structures, and then uses scaffold-conditioned aerial completion tokens to predict a gated residual update for weakly constrained content before Gaussian decoding. During training, dense-to-sparse distillation transfers structural cues from dense-view reconstruction, while an aerial-adapted video diffusion prior provides fine-grained urban appearance cues through gated token conditioning. Observation-preserving objectives keep the refined representation consistent with input-supported geometry. At inference time, AnyCity reconstructs the final 3D Gaussian scene from sparse aerial views in a single feed-forward pass, achieving coherent urban novel-view synthesis with second-level inference. Experiments on synthetic, aerial-domain, UAV-textured, and real-world scenes show consistent improvements over feed-forward baselines.

---


### 288. [DASM: Domain-Aware Sharpness Minimization for Multi-Domain Voice Stream Steganalysis](https://arxiv.org/abs/2605.19955)

**<font color=#1a73e8>作者：</font>** Pengcheng Zhou, Pianran Guo, Shuhua Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing use of information hiding in network streaming media for covert communication poses a significant security threat, necessitating the development of robust detection technologies. However, existing steganalysis methods for network voice streams mostly rely on data distributions in specific scenarios, making it difficult to adapt to the practical detection needs of non-homologous data distributions. Through Hessian analysis, we find that the loss landscapes of mainstream models are dominated by numerous saddle points and sharp local minima, rendering them highly sensitive to data distribution shifts and fundamentally limiting generalization. Therefore, we propose a new optimizer, Domain-Aware Sharpness Minimization (DASM). The core mechanisms of DASM consist of two aspects: first, it integrates domain-supervised contrastive learning with sharpness-aware optimization, explicitly preserving inter-domain feature separation while seeking flat minima; second, we design an adaptive domain gap modulation strategy that dynamically calibrates the optimization loss weights by sensing the real-time feature separability of different domains. Extensive experimental results demonstrate that our method outperforms the state-of-the-art methods by a large margin and achieves excellent generalization and robustness.

---


### 289. [World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks](https://arxiv.org/abs/2605.19957)

**<font color=#1a73e8>作者：</font>** Zuyao Lin, Jianhui Zhang, Peidong Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models are widely explored in embodied intelligence, yet they typically predict distinct evolutions of the world and the ego within a single stream, where the world captures persistent instruction-agnostic scene regularities and the ego captures robot-centric instruction-conditioned dynamics. This world-ego entanglement leads to a degradation in long-horizon embodied scenarios, particularly in hybrid tasks with interleaved navigation and manipulation behaviors. In this paper, we introduce \emph{World-Ego Modeling}, a new conceptual paradigm that decomposes future evolution into world and ego components. We define the world-ego boundary from three perspectives, i.e., motion-, semantic-, and intention-based views, and analyze three disentanglement strategies with post-, pre-, and full disentanglement. Further, we instantiate this paradigm as the World-Ego Model (WEM), a unified embodied world model that couples an implicit separate world-ego planner with a cascade-parallel mixture-of-experts (CP-MoE) diffusion generator. To enable rigorous evaluation, we further construct HTEWorld, the first benchmark for long-horizon world modeling with hybrid navigation-manipulation tasks, providing 125K video clips (over 4.5M frames) with fine-grained action annotations and 300 multi-turn evaluation trajectories (over 2K instructions). Extensive experiments show that WEM achieves state-of-the-art performance on HTEWorld while remaining competitive on existing manipulation-only benchmarks.

---


### 290. [Learning Orthonormal Bases for Function Spaces](https://arxiv.org/abs/2605.19959)

**<font color=#1a73e8>作者：</font>** Hamidreza Kamkari, Mohammad Sina Nabizadeh, Justin Solomon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Infinite-dimensional orthonormal basis expansions play a central role in representing and computing with function spaces due to their favorable linear algebraic properties. However, common bases such as Fourier or wavelets are fixed and do not adapt to the structure of a given problem or dataset. In this paper, we aim to represent these bases with neural networks and optimize them. Our key idea is that any target infinite-dimensional orthonormal basis can be viewed either as a point on the Lie manifold of the orthogonal group, or equivalently, as the endpoint of a continuous path on that manifold that connects a reference basis, e.g. Fourier, to that target. Paths on the Lie manifold satisfy ordinary differential equations (ODEs) governed by skew-adjoint integral operators. Using neural networks to define finite-rank generators of such ODEs allows us to parameterize and optimize orthonormal bases in function space. While relying on finite-rank generators to model infinite operators might seem restrictive, we prove a universality result: even with a rank-2 generator, the integrated solutions of the ODE are dense in the orthogonal group under the appropriate operator topology. In other words, for any target orthonormal basis, there exists a path originating from a reference basis and driven by finite-rank generators that gets arbitrarily close to that target basis. We demonstrate the flexibility of our framework by transforming the Fourier basis into the principal components of a functional dataset, eigenfunctions of linear operators, or dynamic modes of energy-preserving physical simulations.

---


### 291. [Normative Networks for Source Separation via Local Plasticity and Dendritic Computation](https://arxiv.org/abs/2605.19965)

**<font color=#1a73e8>作者：</font>** Bariscan Bozkurt, Efe Ali Gorguner, Francesco Innocenti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Blind source separation (BSS) is a natural framework for studying how latent causes may be recovered from sensory mixtures, but deriving online and biologically plausible algorithms for structured (i.e., constrained to known domains) and potentially correlated sources remains challenging. Recent work has derived neural networks for BSS from maximization of an entropy measure, yet its online implementations involve complex and nonlocal recurrent dynamics. Motivated by this perspective, we propose Predictive Entropy Maximization, which achieves competitive performance in BSS, using only local weight updates. The method employs a close approximation of an entropy measure, yielding an objective function with easily interpretable components. Minimizing this objective leads to a predictive neural architecture in which feedforward synapses follow an error-driven rule (that can be realized through dendritic mechanisms), lateral inhibitory connections are learned with local Hebbian plasticity, and source-domain constraints are enforced through simple output nonlinearities. We derive explicit spectral bounds on the surrogate error, characterizing when the approximation is accurate. Empirically, Predictive Entropy Maximization remains robust under increasing source correlation and observation noise, outperforms biologically plausible algorithms that rely on stronger independence or decorrelation assumptions, and remains competitive with exact determinant- and correlative-information-based baselines. These results show how local plasticity and adaptive lateral inhibition can emerge from maximizing a regularized second-order entropy over structured source domains. Our implementation code is available at this https URL.

---


### 292. [Block-Sphere Vector Quantization](https://arxiv.org/abs/2605.19972)

**<font color=#1a73e8>作者：</font>** Heesang Ann, Joongkyu Lee, Min-hwan Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vector quantization is a fundamental primitive for scalable machine learning systems, enabling memory-efficient storage, fast retrieval, and compressed inference. Recent rotation-based quantizers such as EDEN, RabitQ, and TurboQuant have introduced strong guarantees and empirical performance, but the surrounding comparisons have been difficult to interpret because they rely on different distortion criteria, probability regimes, and implementation assumptions. As our first contribution, we provide a unified theoretical comparison of these methods and show that their relative advantages are criterion-dependent rather than absolute: EDEN and TurboQuant are favorable for MSE distortion, EDEN is also effective for expected inner-product distortion, and RabitQ provides strong high-probability control. This comparison further clarifies that EDEN provides particularly strong guarantees for expected distortion measures. As our second contribution, we introduce Block-Sphere Quantization (BlockQuant), a new rotation-based block quantization algorithm designed around the spherical geometry of randomly rotated vectors. Unlike coordinate-wise quantizers, BlockQuant quantizes blocks on the sphere, preserving the geometry of rotated embeddings more faithfully. We prove that this block-spherical design theoretically improves over the baselines considered in this paper for both reconstruction MSE and expected inner-product distortion. Our experiments on real embedding datasets and long-context LLM inference tasks show practical gains that are consistent with our theoretical improvements.

---


### 293. [SphericalDreamer: Generating Navigable Immersive 3D Worlds with Panorama Fusion](https://arxiv.org/abs/2605.19974)

**<font color=#1a73e8>作者：</font>** Antoine Schnepf, Karim Kassab, Flavian Vasile 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The generation of immersive and navigable 3D environments is increasingly prevalent with the growing adoption of virtual reality and 3D content. However, recent methods face a fundamental limitation: they cannot produce 3D worlds that simultaneously (i) are navigable over long-range spatial extents and (ii) cover the complete omnidirectional field of view ($360^\circ$ horizontally and $180^\circ$ vertically). To address this challenge, we introduce SphericalDreamer, a method for generating fully immersive and long-range 3D outdoor environments from textual prompts. Our approach is built on the generation of multiple panoramic images, which are subsequently lifted into 3D and fused together while maintaining visual and geometric consistency. SphericalDreamer produces highly detailed, fully immersive 3D environments, while substantially improving scale and navigability compared to prior approaches.

---


### 294. [Learning with Foresight: Enhancing Neural Routing Policy via Multi-Node Lookahead Prediction](https://arxiv.org/abs/2605.19975)

**<font color=#1a73e8>作者：</font>** Xia Jiang, Yaoxin Wu, Yew-Soon Ong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural policies have shown promise in solving vehicle routing problems due to their reduced reliance on handcrafted heuristics. However, current training paradigms suffer from a fundamental limitation: they primarily focus on next-node prediction for solution construction, resulting in myopic decision-making that undermines long-horizon planning capacity. To this end, we introduce Multi-node Lookahead Prediction (MnLP), a novel training strategy that extends the supervised learning paradigm to predict multiple future nodes simultaneously. We incorporate causal and discardable MnLP modules that operate exclusively during training, facilitating models to anticipate multi-step decisions while preserving inference-time efficiency. By incorporating multi-depth auxiliary supervision into the loss function, MnLP equips neural policies with the ability of long-range contextual understanding. Experimentally, MnLP outperforms existing training methods, improving the generalization capability of neural policies across various problem sizes, distributions, and real-world benchmarks. Moreover, MnLP can be seamlessly integrated into diverse neural architectures without introducing additional inference overhead.

---


### 295. [CogOmniControl: Reasoning-Driven Controllable Video Generation via Creative Intent Cognition](https://arxiv.org/abs/2605.19995)

**<font color=#1a73e8>作者：</font>** Hongji Yang, Songlian Li, Yucheng Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion models achieve strong photorealism and fluency in video generation, yet remain fragile under abstract, sparse or complex conditions, leading to poor performance in professional production workflows such as storyboard sketches and clay render conditions. Existing video generation models, either inject conditions through adapters or couple a generic vision-language model (VLM) within a diffusion backbone, leaving a capability gap and failing to produce the videos that align with the user's creative intent. We present CogOmniControl, a reasoning-driven framework that factorizes controllable video generation into creative intent cognition and generation. Specifically, we train a specialized CogVLM using authentic anime production data. Compared to generic VLMs, it generates more professional and clear outputs, accurately cognizing user creative intent from sparse and abstract conditions and tuning these cues into dense reasoning output. Besides, CogOmniDiT unifies the controls from various conditions through in-context generation and is aligned to the CogVLM reasoning outputs via reinforcement learning. Furthermore, leveraging CogVLM's robust capability in guiding video generation, we release its potential in planning specific evaluators and enable a Best-of-N selection for the generated videos. This integration transforms the entire framework into a closed-loop "harness-like" architecture. We further introduce CogReasonBench and CogControlBench, built from professional workflows data that carry genuine creative intent rather than simulated ones. Experiments on two benchmarks show that CogOmniControl surpassed the existing open-source models. The project website: this https URL

---


### 296. [GeoX: Mastering Geospatial Reasoning Through Self-Play and Verifiable Rewards](https://arxiv.org/abs/2605.20006)

**<font color=#1a73e8>作者：</font>** Kyeongjin Ahn, Seungeon Lee, Krishna P. Gummadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geospatial reasoning requires solving image-grounded problems over the complex spatial structure of a scene. However, developing this capability is hindered by the cost of annotating a vast and combinatorial question space. We propose GeoX, a self-play framework that acquires spatial logic through executable programs that yield verifiable rewards, without relying on large-scale human-curated data Given a satellite or aerial image, our framework employs a single multimodal policy that proposes spatial problems as executable programs and solves them under three reasoning modes-abduction, deduction, and induction-over spatial primitives and an image understanding tool. A verifier executes each program to covert a reward signal that jointly optimizes the two roles via reinforcement learning. GeoX consistently improves its base VLMs by up to 5.5 points on average, matching or exceeding conventional baselines trained on millions of curated data. Along-side the proposed method, we release a benchmark for geospatial understanding accumulated through self-play.

---


### 297. [Training Neural Networks with Optimal Double-Bayesian Learning](https://arxiv.org/abs/2605.20009)

**<font color=#1a73e8>作者：</font>** Vy Bui, Hang Yu, Karthik Kantipudi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation with gradient descent is a common optimization strategy employed by most neural network architectures in machine learning. However, finding optimal hyperparameters to guide training has proven challenging. While it is widely acknowledged that selecting appropriate parameters is crucial for avoiding overfitting and achieving unbiased outcomes, this choice remains largely based on empirical experiments and experience. This paper presents a new probabilistic framework for the learning rate, a key parameter in stochastic gradient descent. The framework develops classic Bayesian statistics into a double-Bayesian decision mechanism involving two antagonistic Bayesian processes. A theoretically optimal learning rate can be derived from these two processes and used for stochastic gradient descent. Experiments across various classification, segmentation, and detection tasks corroborate the practical significance of the theoretically derived learning rate. The paper also discusses the ramifications of the proposed double-Bayesian framework for network training and model performance.

---


### 298. [FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration](https://arxiv.org/abs/2605.20022)

**<font color=#1a73e8>作者：</font>** Yaojie Zhang, Jianuo Huang, Junlong Ke 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel. However, conventional sequential speculative decoding suffers from mutual waiting between drafting and verification, and repeated exchange of intermediate states further increases memory access overhead. Parallel speculative decoding addresses this limitation by performing drafting and verification within a single target forward pass, allowing future drafts to be prepared while current candidates are being verified. Although effective at small batch sizes, existing parallel speculative decoding methods either require costly continual pretraining with quality degradation or suffer from low acceptance rates. More importantly, this paradigm inherently suffers from uncertainty in both the bonus token and the accepted length, leading to draft verification mismatch and causing throughput gains to collapse at large batch sizes. To address these limitations, we introduce FlexDraft, a lossless speculative decoding framework that flexibly adapts to varying batch sizes through three key designs. (1) Attention Tuning enables block diffusion drafting by tuning only the attention projectors of the final few layers on mask tokens, while keeping the autoregressive path frozen to preserve the target distribution and produce high quality drafts with minimal trainable parameters. (2) Bonus-guided Calibration uses a lightweight MLP conditioned on the resolved bonus token to calibrate draft logits, mitigating draft verification mismatch caused by bonus token uncertainty. (3) Flex Decoding dynamically switches between parallel draft and verify at small batch sizes and sequential draft then verify at large batch sizes, and adjusts verification length based on draft confidence to eliminate redundant computation.

---


### 299. [When Skills Don't Help: A Negative Result on Procedural Knowledge for Tool-Grounded Agents in Offensive Cybersecurity](https://arxiv.org/abs/2605.20023)

**<font color=#1a73e8>作者：</font>** Samuel Jacob Chacko, James Hugglestone, Chashi Mahiul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills, structured packages of procedural knowledge loaded into an LLM agent at inference time, are widely reported to improve task pass rates by an average of 16.2~percentage points across diverse domains. Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced. The community has not yet articulated a clean mechanism for \emph{when} Skills help and when they are merely redundant overhead. We re-analyze a recently published 180-run controlled study of an MCP-grounded autonomous Capture-the-Flag (CTF) agent under four documentation conditions of increasing richness (55, 1{,}478, 1{,}976, and 4{,}147 lines), and show that these conditions correspond almost exactly to a No-Skills, Experiential-Skills, Curated-Skills, and Comprehensive-Skills ablation. In offensive cybersecurity, a domain not deeply covered by existing Skills benchmarks, the marginal benefit of Skills collapses. The spread between the no-Skills and full-Skills conditions is only 8.9~pp ($p = 0.71$, $\chi^2$; $p = 0.25$, Cochran--Armitage trend test; five of six pairwise Cohen's $h$ values fall below the $0.2$ small-effect threshold). We argue that the missing variable is \emph{environment-feedback bandwidth}. When an agent's tool layer returns strict, schema-validated, low-latency observations, the environment itself supplies the procedural correction signal that Skills are normally needed to provide. As a result, the marginal benefit of curated Skills diminishes substantially, and, in some cases (e.g., our timing side-channel setting), actively degrades performance. We articulate a falsifiable hypothesis, sketch its design implications for compound AI systems, and will release the reanalysis pipeline to support replication.

---


### 300. [Journeys of Parents with LGBTQ+ Children: How Trauma and Healing Reshape Identity and (Mis)Informating Practices](https://arxiv.org/abs/2605.20024)

**<font color=#1a73e8>作者：</font>** Soonho Kwon, Dong Whi Yoo, Koustuv Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines how parents of LGBTQ+ individuals in South Korea navigate the emotional rupture fueled by fear, isolation, and disorientation after learning their children's queer identity, encounter queer-related (mis)information as a way of coping with this emotional toll, and come to listen to queer realities relationally. Through this process, we highlight how parents reconstruct their identities as supportive parents, which reshapes their informating practices, making them more critical in assessing queer-related (mis)information, developing strategies to protect themselves from harmful narratives, and actively challenging misinformation to support others navigating similar experiences.
This work contributes to CSCW by (1) foregrounding parents of LGBTQ+ individuals, an underrepresented yet critical stakeholder group in Queer HCI; (2) demonstrating how identity reconfiguration following a trauma-healing process could transform information practices; and (3) arguing that addressing misinformation requires attention beyond individual fact-based discerning to account for its relational, cultural, and emotional dimensions. Further, we invite CSCW scholars to reconsider the balance between abstracting and humanizing information, explore future design possibilities for parents of LGBTQ+ children, and reflect on the role of researchers as participants in collective research communities fueled by care.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-338](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
