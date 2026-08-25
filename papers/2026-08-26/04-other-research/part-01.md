# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

---

### 1. [AIREP: A Protocol for Per-Decision Evidence in AI Runtime Governance](https://arxiv.org/abs/2608.21363)

**<font color=#1a73e8>作者：</font>** Ali Toygar Abak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A protocol is presented for recording the governance decisions of automated AI runtimes. When a runtime releases, blocks, defers, redacts, or escalates an individual output, AIREP records that decision as a single signed object that any party can check offline, independent of the runtime that produced it. A record carries the decision as one of a closed set of verbs under a stated policy basis, references its input, output, and evidence by hash rather than by value, and declares both what its evidence covers and what it does not. Records form a SHA-256 hash chain that binds each record to its position, so that tampering and gaps are detectable by recomputation. Vendor-, model-, and domain-specific content is confined to a single optional namespace, and a mechanical neutrality test keeps the shared format free of it. A reference implementation and a two-language conformance kit are described. Some implementation issues are considered, and problems such as alignment of the canonical form across implementations, freshness witnesses, and multi-runtime chains are exposed. The format is offered for adoption by any AI runtime that records governance decisions.

---


### 2. [Distinguishing Revision and Delayed Elaboration in Incremental Narrative Interpretation](https://arxiv.org/abs/2608.21364)

**<font color=#1a73e8>作者：</font>** Yi-Chun Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Both human and AI systems that process narrative or long-form content operate incrementally: input is received over time, and internal representations must be updated accordingly. Incremental interpretation, therefore, depends not only on what is represented but also on how the representational state evolves under new evidence.
We distinguish two structurally different update operators that arise in narrative interpretation: revision-driven update and delayed elaboration. Revision-driven updates retract or replace previously committed structure in response to a contradiction and are therefore non-monotonic. Delayed elaboration, by contrast, refines initially underspecified elements through constraint addition without retracting prior commitments, yielding monotonic extension of the interpretive state. Although both operators may alter how earlier material is understood, they impose fundamentally different structural requirements on state transitions.
Using visual narratives as a diagnostic domain, we demonstrate how a structured narrative representation can explicitly separate committed from underspecified content and support both update operators during incremental construction. Through a worked example, we show how delayed elaboration enables monotonic refinement of interpretive state, while revision requires non-monotonic correction. We discuss the broader relevance of this structural distinction for incremental reasoning and hybrid symbolic-neural systems.

---


### 3. [AI Learning and Conceptual Transfer in the Game of Hidden Rules](https://arxiv.org/abs/2608.21372)

**<font color=#1a73e8>作者：</font>** Christo Mathew, Wentian Wang, Jacob Feldman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This report summarizes the work conducted on the Game of Hidden Rules (GOHR), focusing on reinforcement learning agents trained to infer hidden rules from trial-and-error feedback, representation design, rule difficulty analysis, transfer learning, generalization, and pseudo-bot-assisted human learning analysis. The report focuses on the Transformer-based A2C framework, Feature-Centric and Object-Centric representations, experimental findings, and classification of human learning data.

---


### 4. [A Social Media Analysis of Discourse on the Israel--Palestine Conflict on Telegram](https://arxiv.org/abs/2608.21385)

**<font color=#1a73e8>作者：</font>** Michail Zafeiropoulos, Despoina Antonakaki, Sotiris Ioannidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media has become a central arena in which armed conflicts are contested, yet the pro-Israel and pro-Palestine communities on Telegram, whose broadcast architecture yields an unusually direct record of deliberate political communication, have not been systematically compared at scale. This study presents a multi-method computational analysis of 87,617 messages from sixteen Telegram channels, eight pro-Israel and eight pro-Palestine, spanning May 2021 to June 2026 and covering multiple conflict escalations. It combines sentiment analysis, three stance detection methods drawn from distinct paradigms (keyword matching, zero-shot DeBERTa via natural language inference, and a fine-tuned BERTweet model), and a framing analysis, all evaluated against 736 manually annotated messages. The fine-tuned model performed best (72.1% accuracy, 0.721 macro F1 under 5-fold cross-validation), outperforming both label-free baselines by 8 to 11 points; the baselines stalled in the low-to-mid 60s, indicating a hard ceiling for stance detection not adapted to in-domain language. The central finding emerges only when sentiment, stance, and framing are read together: the two communities deploy the same death- and victim-related vocabulary in opposite emotional registers, pro-Israel channels predominantly neutral and report-style, pro-Palestine channels markedly more negative, consistent with writing from the distinct discourse positions of acting party and affected party.

---


### 5. [Model of Models: When Does Emitting a Specialist Beat Attending, Adapting, or Tuning?](https://arxiv.org/abs/2608.21386)

**<font color=#1a73e8>作者：</font>** John C. Howell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a task described by a few examples, how should a model be specialized to it? Four mechanisms are available -- zero-shot, in-context attention, test-time gradient adaptation, and emitting specialist weights from a hypernetwork -- yet the operating regime of the last is rarely mapped. We run the identical four-way comparison across six tasks spanning regression, generation, language modeling, reinforcement learning, and clinical and genomic classification, holding the specialist, the context, and (where we can) the training budget fixed. The clearest wins for emission are about cost at matched quality: it ties the state-of-the-art amortized tabular model (TabPFN) on clinical few-shot classification while emitting a reusable specialist instead of re-attending the support set per query, and reaches noise-floor shape generation with a $132$-float per-instance program. On few-shot sinusoid regression it is $2$--$3$ orders of magnitude below MAML at zero test-time gradient steps -- a margin that narrows to $\sim$$30\times$ but persists once training budgets are equalized. Emission cannot match in-context attention on high-dimensional sequence modeling: under matched-budget pre-training a one-pass adapter recovers only a minority of the in-context gain ($14.0\pm0.9\%$ at $5$M, $11.2\pm0.5\%$ at $15$M), and a LoRA-rank sweep shows this shortfall is a partial capacity limit -- capture climbs from $5\%$ to $21\%$ as rank grows but plateaus far below full recovery. Mechanism ablations confirm the emitted specialist is genuinely task-conditioned, not a memorized prior; and, more speculatively, emitted specialists compose in weight space -- interpolating two of them tracks the corresponding blend of their functions. We close with a falsifiable thesis, operationalized through a per-task resolution measure, bounding when each conditioning mechanism should be preferred.

---


### 6. [Runtime Action Interference for AI Control of AlphaStar in StarCraft II](https://arxiv.org/abs/2608.21398)

**<font color=#1a73e8>作者：</font>** Jaymari Chua, Chen Wang, Liming Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A trained reinforcement learning policy does not determine the complete behavior that users encounter: deployment code still schedules, admits, suppresses, or replaces its proposed actions. We contribute \emph{runtime action interference} (RAI), an AI control mechanism that preserves policy parameters while regulating action pacing and filtering configured action patterns after inference. RAI releases a proposed action only when its cooldown condition is satisfied and its content detector does not flag the action; otherwise, it dispatches a no-op. The detector covers specified toxic behaviors, including worker-unit harassment, while the cooldown controls action rate. We implement RAI in a replication of AlphaStar this http URL and make the implementation and reproducibility materials available through an open source code repository. We deployed RAI in a \textit{StarCraft~II} human participant study that compared two presentations of the same opponent with high capability and rate limited actions; we withheld its capability claim in one presentation and disclosed it in the other. On response scales from 1 to 5, we observed pooled fairness, trust, and toxicity means of 3.90, 3.50, and 2.00 under claim withholding, compared with 2.62, 4.31, and 2.85 under disclosure. Disclosure corresponded with lower perceived fairness and higher perceived toxicity across every expertise group, whereas trust increased among novices and experts but decreased among intermediate participants. Our human evaluation therefore shows that perceptions of an opponent controlled through RAI can vary substantially with the capability information presented to users, even when the configured control remains constant. We conclude that human-computer evaluations must separate control within the execution stack from capability disclosure and assess fairness, trust, and toxicity as distinct dimensions of human experience.

---


### 7. [Federated Ensemble Forecasting Under Supply-Chain Market Volatility](https://arxiv.org/abs/2608.21399)

**<font color=#1a73e8>作者：</font>** Shunmukha Sagar Puppala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supply chain forecasting systems increasingly operate under market shocks, non-identically distributed regional demand, and limited willingness to centralize commercial data. This work proposes Federated Ensemble Forecasting with Negative-Correlation Learning (FEF NCL), a distributed method that trains specialized forecasting experts across client nodes while discouraging redundant model errors. The framework combines temporal feature encoders, client level drift scoring, reliability-weighted aggregation, and an explain ability layer that exposes the market and supplier variables most responsible for each forecast. A single synthetic dataset is used to evaluate the design. It contains 124,800 weekly SKU region observations from ten regional client nodes, 60 product families, 40 suppliers, five commodity groups, and a 2021-2024 volatility profile with explicit price-shock regimes. Because the dataset is synthetic, the reported results should be interpreted as controlled evidence of internal consistency rather than real-world validation. Across the synthetic test split, FEF NCL reduces weighted mean absolute percentage error from 13.9% for the best federated baseline to 12.4%, improves delay-risk macro-F1 from 0.755 to 0.801, and lowers the high volatility quintile error by 2.1 percentage points relative to SCAFFOLD. The analysis suggests that negative-correlation specialization is useful when clients face different supplier, freight, and commodity conditions, although deployment would require stronger privacy analysis, live drift monitoring, and operational calibration. Index Terms federated learning, ensemble learning, negative correlation learning, supply chain forecasting, market volatility, data drift, demand planning, risk governance

---


### 8. [The Abstention Protocol: RCA for Clos Fabrics](https://arxiv.org/abs/2608.21412)

**<font color=#1a73e8>作者：</font>** Madhava Gaikwad, Deepak Pandey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) in large datacenter networks is challenging because telemetry is noisy, partial, and asynchronous. Score-based approaches degrade under these conditions, often yielding unstable or incorrect attributions.
We present \textsc{CoreSec}, a production RCA system that replaces weighted fusion with a PAM-style abstention algebra. Telemetry agents are composed using control flags that yield deterministic decisions and explicit abstention when evidence is ambiguous. CoreSec combines this algebra with topology-aware configurations that capture failure surfaces across Clos fabrics and converge monotonically as evidence accumulates.
Deployed at hyperscale, CoreSec provides stable and explainable RCA behavior across diverse environments without retuning. Our experience shows that structured composition with abstention forms a practical foundation for automated RCA in real-world cloud networks.

---


### 9. [Composable Trust Infrastructure for Manufacturing Knowledge Graphs: Cross-System Provenance, Temporal Reasoning, and Decision Traceability](https://arxiv.org/abs/2608.21418)

**<font color=#1a73e8>作者：</font>** Grama Chethan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Manufacturing knowledge graphs that integrate data from heterogeneous industrial systems face a trust deficit: consumers cannot determine whether queried data is valid, whether it was valid when a decision was made, where it originated, or how it was acted upon. We argue that four trust capabilities -- SHACL validation, PROV-O provenance, domain-aware bi-temporal versioning, and graph-native decision objects -- compose through shared correlation identifiers to produce emergent trust properties that no single capability delivers alone. We present a composable trust infrastructure that integrates these four capabilities into a unified RDF architecture. Capabilities compose through shared entity URIs, ingestion activity identifiers, and temporal correlation keys, enabling compound queries spanning all four dimensions. An experimental ablation confirms that removing any single capability causes exactly three of six composition queries to fail, demonstrating that all four are equally load-bearing. Analysis of higher-order compositions reveals four emergent three-way properties and one irreducible four-way property (full-chain auditability, 31ms execution). The infrastructure is validated on a testbed integrating eleven industrial sources -- OPC UA, TIA Portal, eClass, AAS, ISA-95, ISA-18.2, SAP S/4HANA, Teamcenter, Opcenter EX, Insights Hub, and SCM -- under an 89-class ISA-95-aligned ontology. The unified graph contains 8,743 triples across five named graphs, stitched by 81 owl:sameAs identity edges. Evaluation uses simulated but structurally realistic data from purpose-built emulators; data structures and cross-system linkage patterns are representative of real industrial installations.

---


### 10. [Topology of a Smile: Persistent Homology in Dental Imaging](https://arxiv.org/abs/2608.21422)

**<font color=#1a73e8>作者：</font>** Leon Dahlmeier, Sara Kališnik, Albert Mehl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CBCT (Cone Beam Computed Tomography) scans provide detailed three-dimensional images, widely used in dentistry for diagnostic and treatment planning tasks. While invaluable, analyzing and documenting these scans is labor-intensive, prompting efforts to automate key steps like the classification and segmentation of anatomical structures to identify tooth types and associated pathologies. In this article, we propose an approach to automation that leverages persistent homology, a framework from topological data analysis that studies the shape of data by identifying features like connected components, holes, and voids across multiple scales. Persistent homology, together with a support vector machine, allows us to classify teeth in a CBCT scan and to perform diagnostics. Our method advances the state of the art, reaching average accuracy scores of 97.67% for tooth-labeling and 96.77% for diagnostic tasks, outperforming a CNN trained on the same data with accuracy of 70.27% and 86.67%, respectively.

---


### 11. [EditStream: A Unified Autoregressive Framework for Interactive Video Generation and Editing](https://arxiv.org/abs/2608.21424)

**<font color=#1a73e8>作者：</font>** Yuqian Zhou, Zhenghong Zhou, Zongze Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video generation and editing are becoming increasingly important for creative design. In this report, we introduce EditStream: a unified framework for interactive video generation and editing. EditStream unifies multiple video creation and manipulation tasks within a single DiT-based model through flexible task-specific conditioning, and further transforms it into a fast, few-step autoregressive model for efficient streaming. It supports Text-to-Video, Image-to-Video, Video-to-Video, Editing Propagation, Reference-guided Video Editing, and Camera Pose Change, enabling flexible control over video generation, transformation, and editing within one system. To make the unified model practical for interactive use, we develop a two-stage distillation approach that combines Velocity Moment Matching (VMM) with autoregressive unrolling. VMM matches conditional velocity moments at student-reached intermediate states to preserve generation quality and motion, while unrolling exposes the student to its own autoregressive predictions to improve temporal stability. Together, they alleviate common challenges in few-step autoregressive video generation, including over-saturation, degraded motion, temporal instability, and complex training. EditStream provides a practical and scalable solution that bridges high-quality diffusion-based video models with interactive creative workflows.

---


### 12. [AI Visual Inspection for Garment Production](https://arxiv.org/abs/2608.21426)

**<font color=#1a73e8>作者：</font>** Ray Wai Man Kong, Ding Ning, Theodore Ho Tin Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The garment manufacturing industry is under increasing pressure to improve product quality, reduce costs, and accelerate digital transformation toward Industry 4.0. One of the most challenging quality-control activities is sewing-line inspection, where defects such as broken stitches and skipped stitches are difficult to detect consistently through manual inspection. Human-based inspection is often affected by fatigue, subjective judgement, and inconsistent performance, resulting in defect leakage, rework, and reduced production efficiency.
This study presents the development and validation of an Artificial Intelligence (AI)-based visual inspection system for garment sewing-line quality control. The system utilizes Convolutional Neural Networks (CNNs) to detect sewing defects and was initially trained using black fabric and black sewing thread samples. Experimental testing was conducted on black, red, dark green, light blue, silver, and fluorescent yellow fabrics. The results demonstrated successful detection of jump sewing-line defects on black, red, and dark green materials, while performance limitations were observed for broken sewing-line defects and fabrics with significantly different visual characteristics, including light blue, silver, and fluorescent yellow colours. These findings indicate that model accuracy is strongly influenced by the diversity of training data and the ability to generalize across different fabric and thread colours.

---


### 13. [Few-Shot Cross-Dataset Adaptation for Tuberculosis Detection Using DenseNet](https://arxiv.org/abs/2608.21427)

**<font color=#1a73e8>作者：</font>** Bidhan Biswas, Shahadat Hossain Sohag, Nabil Ashab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tuberculosis (TB) is one of the most common and dangerous bacterial ailments. Every year, it causes a large number of deaths worldwide. Although many deep learning models can detect tuberculosis from chest X-rays quite accurately, severe domain shift across datasets makes the task challenging. Different imaging protocols, patient demographics, and equipment across domains make the task of generalization difficult. In real-world settings, a model may perform well on one dataset but show a noticeable drop in performance when tested on another. In this work, we address this domain adaptation challenge through a few-shot scaling study. A controlled cross-dataset evaluation is presented in this paper using TBX11K as the source domain and the Mendeley TB dataset as the target domain. It is investigated how varying the number of target samples affects model performance under three training regimes: frozen backbone adaptation, full fine-tuning of a source-pretrained DenseNet121 model, and training from scratch. The results indicate that the model can perform well even with limited data and can achieve 98.36\% accuracy with just 75 labeled samples per class. The adaptation curves demonstrate how fine-tuning effectively mitigates domain shift. These findings establish full fine-tuning of pretrained models as a highly effective and practical strategy for mitigating domain shift in low-resource clinical deployment scenarios.

---


### 14. [Measuring Gender Representation in Animated Films](https://arxiv.org/abs/2608.21429)

**<font color=#1a73e8>作者：</font>** David Bamman, Allison Cooper, Ruby Alvarez Rubio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animated films--often developed with an audience of children in mind--are an important vector for enculturation, and empirical work that has examined the representation of gender at scale in these films has largely focused on counting the gender composition of the cast rather than deploying a more fine-grained instrument (such as assessing the visibility of those characters in overall screentime). In this work, we develop a computational pipeline for recognizing animated characters in these films, and use it to test several hypotheses about gender representation in a corpus of 224 popular animated movies. We find that while the overall representation of female characters in animated films largely tracks with those of live-action films (over the period 1980-2025), we see stark differences between the representation of human characters (much greater representation among women and girls) and non-humans (largely male). Contrary to past work on Disney, we do not see female characters declining in antagonist roles in animated films, and characters who are women and girls are much more likely to share scenes together than their live action contemporaneous counterparts.

---


### 15. [DesignAgent3D: Interactive 3D Scene Editing via Designer-like Multimodal Reasoning](https://arxiv.org/abs/2608.21438)

**<font color=#1a73e8>作者：</font>** Xiujin Liu, Tianyu Yang, Yilun Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text guided 3D scene editing provides an intuitive interface for modifying reconstructed environments, but remains difficult because natural language design requests are often semantically underspecified and must be grounded in cluttered 3D scenes. Existing methods typically formulate the task as one-shot conditional generation from a single prompt, failing to resolve ambiguous user intents or achieve precise spatial grounding. Consequently, they suffer from severe object localization drift, tracking failure under occlusions, and the notorious multi-view "sticker effect." To overcome these limitations, we present DesignAgent3D, an interactive multimodal agentic framework that reformulates 3D scene editing as a designer-like Plan-Perceive-Act paradigm. The agent first plans by interacting with the user to clarify underspecified design goals, then perceives by grounding the intended edit to specific objects or regions in the 3D scene, and finally acts by applying controlled visual modifications while preserving scene consistency. The edits are further integrated into the underlying 3D representation, supporting persistent and multi-view consistent novel-view rendering. Extensive experiments across both NeRF and 3D Gaussian Splatting backbones demonstrate that DesignAgent3D significantly outperforms state-of-the-art baselines, delivering superior semantic intent alignment, impeccable spatial localization accuracy, and high-fidelity multi-view consistency.

---


### 16. [WorldMind: Decoupled Game World Model for State-Aware NPC Behavior](https://arxiv.org/abs/2608.21439)

**<font color=#1a73e8>作者：</font>** Zhiyang Deng, Boran Zhang, Danze Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Game world models have recently demonstrated promising capabilities in generating visually coherent and action-controllable gameplay videos. However, non-player character (NPC) behavior in existing models is either implicitly entangled with video generation or explicitly prescribed through external control signals. Consequently, a game world model has to jointly understand the state, plan the NPC's response and render its visual outcome, limiting its ability to produce responsive and state-aware NPC behavior. The challenge lies in the lack of an explicit interface for state-grounded decision-making. To this end, we introduce WorldMind, to our knowledge the first decoupled framework for state-aware NPC behavior in game world models. WorldMind separates interactive world modeling into four layers: an Understanding Layer that constructs a compact state from generated frames; a Decision Layer that reasons over the compact state to plan the NPC's next action; a Control Layer that translates the actions into temporally aligned conditions; and a Generation Layer that synthesizes their visual outcomes. By reconnecting layers in a closed interaction loop, WorldMind grounds NPC behavior in the evolving game state. We further introduce BOSS-140K, a dataset of gameplay videos paired with rich internal game states, together with an agent that automates the collection at scale. Experiments on BOSS-140K demonstrate reliable compact state reconstruction and mechanics-grounded planning, with WorldMind preferred over the baselines in approximately 70% of pairwise comparisons for its more tactically appropriate and coherent NPC behavior. Project page: this https URL

---


### 17. [Text-Guided Visual Dependency Graph Learning with Cross-Modal Attention Priors](https://arxiv.org/abs/2608.21443)

**<font color=#1a73e8>作者：</font>** Fei Wang, Yutong Zhang, Yang Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating interpretable conditional-dependence structures from multimodal visual-linguistic features remains largely unexplored. We propose CM-GLasso (Cross-Modal Graphical Lasso), a framework that bridges vision-language representation learning and sparse Gaussian Graphical Models. CM-GLasso introduces three key components: (i) a text visualization strategy that renders class-attribute descriptions as images and processes them through the same SigLIP-2 vision encoder as natural images, yielding prototype-indexed patch-level attention footprints in a shared feature coordinate system; (ii) a cross-attention distillation mechanism that condenses high-dimensional patches into a small set of semantic graph nodes, whose attention-footprint similarities yield cross-modal structural priors for non-uniform L1 penalization; (iii) a joint ADMM formulation that estimates shared and class-specific precision components within a single convex objective, avoiding the need to first estimate and then decompose separate class-wise graphs. The learned sparse graph topologies directly support a parameter-free, precision-based classification rule and a lightweight topology-aware segmentation head. Extensive experiments on eight benchmarks demonstrate that CM-GLasso achieves competitive or superior performance compared with strong feature-based and task-specific baselines. Under the matched controlled protocol, it attains the highest average classification accuracy (91.97%) and the highest segmentation mIoU among the controlled baselines on VOC (74.75%) and ADE20K (64.01%), while also yielding explicit sparse conditional-dependence graphs with common-specific decomposition.

---


### 18. [Software Frameworks for Explainable AI in Time Series Classification: A Systematic Review](https://arxiv.org/abs/2608.21449)

**<font color=#1a73e8>作者：</font>** Louis Peter, Nils Gumpfer, Jana Fischer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series arise in a wide range of application domains and are analyzed using machine learning in decision-critical settings. Time series classification (TSC) is one of the most widely studied and relevant tasks. In this context, ensuring the transparency and trustworthiness of TSC models has become an important requirement, motivating the use of explainable artificial intelligence (XAI) methods. Despite growing interest, research on XAI for TSC remains fragmented, and a systematic understanding of the available software frameworks for explanation generation, their evaluation practices, and practical limitations is still lacking. Prior work largely focused on individual explanation methods, while cross-framework consistency, time-series-specific evaluation, and reproducibility have received little attention. In this survey, we analyze existing software frameworks for explanation generation and evaluation in TSC. We compare them along multiple dimensions, including supported XAI methods, evaluation metrics, usability, benchmarking support, and reproducibility, providing the first time-series-specific survey of frameworks with implementation comparisons and an analysis of frequency-domain support. We identify six frameworks that explicitly support time series and reveal common limitations: only one method supports frequency-domain explanations despite their relevance; only two evaluation metrics have been developed specifically for time series; and identical XAI methods can yield substantially different explanations across frameworks. Based on these findings, we discuss open challenges and outline directions for future research, highlighting the need for unified, time-series-specific XAI frameworks that enable faithful, reproducible, and time-series-aware explanations.

---


### 19. [Multi-Scale Fruit Capsules: Dilated Convolutions and Dynamic Routing for In-the-Wild Explainable Fruit Recognition](https://arxiv.org/abs/2608.21454)

**<font color=#1a73e8>作者：</font>** Subhankar Chattoraj, Sawon Pratiher, Samiran Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The same fruit appears in a bunch, unpicked, peeled, bagged in plastic, or sliced on a dish, so automated fruit classification in the wild (AFCW) must absorb wide intra- class and narrow inter-class variability in shape, size, colour and texture. Convolutional networks route information through pooling, which discards the pose and location of the region of interest and therefore generalises poorly across these presentations. We propose FruitCapsNet, a capsule network whose Fruit Capsules replace the standard convolutional front end with dilated convolutions: the receptive field grows exponentially at constant parameter cost, so each capsule encodes multi-scale context before dynamic routing resolves part whole spatial agreement. Hyper-parameters, including the dilation factor, are selected by Bayesian optimisation rather than grid search. On three public datasets (SMP, FruitsGB, Fruits-360) and a new 19-class, 10,639-image in-the-wild dataset (PD-19), FruitCapsNet exceeds ten fine-tuned transfer-learning backbones at one-third the depth, with the largest margin (+2.7% over the nearest competitor) on the hardest set. Grad-CAM saliency propagated from the DigitCaps layer shows that the improvement comes from attributing decisions to whole-fruit regions rather than to object edges, giving post-hoc evidence that the gain is not a dataset artefact.

---


### 20. [Tomatoes, Potatoes, and Onions: Questioning the Need for Faces in Face Presentation Attack Detection](https://arxiv.org/abs/2608.21455)

**<font color=#1a73e8>作者：</font>** Guray Ozgur, Fadi Boutros, Naser Damer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face presentation attack detection (PAD) is traditionally formulated as a face-specific problem, although many of the visual artifacts introduced by print, replay, and recapture processes are not inherently tied to facial appearance. In this work, we investigate whether transferable PAD representations can be learned without using faces during downstream PAD training. To this end, we introduce TPO, a controlled face-free presentation attack dataset consisting of bona fide, print, and replay recordings of, almost randomly chosen, tomatoes, potatoes, and onions acquired under protocols that closely mirror conventional face PAD datasets. Using a foundation-model-based PAD architecture, we demonstrate that a detector trained on TPO achieves an average AUC of 92.70% across four standard cross-dataset face PAD benchmarks, outperforming training on synthetic faces and remaining competitive with models trained on real face datasets. Conversely, models trained on face PAD datasets transfer consistently above chance to TPO, suggesting that the learned representations capture characteristics of the presentation process rather than object semantics. Furthermore, incorporating TPO into conventional face PAD training consistently improves cross-dataset performance under fixed optimization budgets, indicating that face-free data provides complementary information rather than simply additional training samples. Finally, representation and frequency analyses provide further evidence that transferable PAD representations cannot be explained by a single spectral artifact but instead encode richer presentation cues shared across object categories. Together, these results provide empirical evidence that transferable presentation attack representations can be learned independently of facial content, opening new opportunities for privacy-preserving and identity-independent PAD development.

---


### 21. [CLSC DETR: Reliable Candidate Ranking via Cross Layer Geometric Support for UAV Small Object Detection](https://arxiv.org/abs/2608.21457)

**<font color=#1a73e8>作者：</font>** Junyan Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) object detection is critical for applications such as target search, where accurate detection of small objects in complex aerial scenes remains challenging. The limited spatial extent, dense distribution, and frequent occlusion of small objects make reliable candidate ranking particularly difficult. Existing Detection Transformer (DETR) based methods improve ranking by estimating localization quality from individual queries and incorporating it into classification scores. However, a single query often lacks sufficient geometric evidence for small objects with weak boundary cues, resulting in unreliable quality estimation and unstable ranking. To address this limitation, we propose Cross Layer Local Support and Consistency Calibration for DETR, termed CLSC DETR. Specifically, the Cross Layer Local Support module establishes correspondences between final layer queries and intermediate layer candidates to aggregate complementary geometric evidence for more reliable localization quality estimation, while the Classification and Localization Consistency Calibration module adaptively adjusts classification scores according to localization quality and classification reliability to improve candidate ranking. Experiments show that CLSC DETR improves AP and AP$_{75}$ over the baseline by 1.5\% and 2.0\% on VisDrone, respectively, while achieving consistent improvements on UAVDT.

---


### 22. [Enhanced Artificial Neural Networks Using QHAdamW in Air Quality Forecasting](https://arxiv.org/abs/2608.21463)

**<font color=#1a73e8>作者：</font>** Mary Joy Daniel Vinas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The study employed an Artificial Neural Network in combination with the optimized Adaptive Moment Estimation (Adam) algorithm, currently the only AQI forecasting model available in the Philippines. The modified QHAdamW - Quasi-Hyperbolic Momentum (QHAdam) and Adam with decoupled weight decay (AdamW) were both extensions of the Adam optimizer, and both offer unique advantages for training ANN. The proposed QHAdamW optimizer addresses the issues on convergence, generalization, and forecasting performance of Adam. Hyperparameter tuning results revealed that 0.01 and 0.001 were the most effective optimal values for the generalization performance of QHAdamW. The comparative analysis results using seven evaluation metrics revealed that the error value range is lower, and the regression coefficient, having a value approximately equal to 1, improved the model accuracy performance. Likewise, the model converges to a satisfactory level of performance with the convergence performance results of lower loss values as obtained from training and validation losses. Based on data from a real-time air quality tracking station in Manila, a feed-forward neural network is used to predict the AQI of PM2.5 and PM10 separately. This model can be used to forecast Particulate Matter (PM), to help the Department of Environment and Natural Resources-Environmental Monitoring Bureau (DENR-EMB) implement a comprehensive air quality management.

---


### 23. [Complexity Induction: Compositional Generalization via Structured Label Distortion](https://arxiv.org/abs/2608.21464)

**<font color=#1a73e8>作者：</font>** Aleksandr Abramov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We demonstrate that structured distortion of training data - which we term complexity induction - can induce compositional generalization in a standard CNN classifier without architectural modification. Using synthetic images of colored geometric shapes, we encode classes as flat string labels (e.g., "red-circle") with no explicit attribute decomposition, and exclude certain color-shape combinations from training entirely. We apply two distortion methods derived from Jaccard string similarity between class names: mixed labels (soft target distributions encoding inter-class overlap) and expanded dataset (false training samples with structurally motivated incorrect labels). Both methods induce the ability to predict unseen class combinations, and act at different levels: mixed labels activate the classifier for unseen combinations by exploiting the CNN's natural embedding structure, while expanded training improves the embedding factorization itself. A control with random (unstructured) false labels confirms that the effect depends on the structure of the distortion, not on noise per se. These results suggest that structured complication of training signals can influence both the internal organization of learned representations and their compositional interpretation - a principle that may underlie the role of natural language in cognitive development.

---


### 24. [3D Point Cloud from Close-Range Photogrammetry for Defect Characterisation of Rubberised Concrete](https://arxiv.org/abs/2608.21468)

**<font color=#1a73e8>作者：</font>** Jiacheng Liu, Mohammed Alnahhal, Ailar Hajimohammadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While three-dimensional (3D) point clouds are widely used in civil engineering, mainstream LiDAR systems such as Terrestrial Laser Scanning (TLS) are physically constrained to laboratory environments. Since their laser spot size typically exceeds the width of microcracks, the beam physically bridges over voids, rendering TLS unsuitable for fine-scale defect analysis. Alternatively, close-range photogrammetry utilising Structure-from-Motion (SfM) and Multi-View Stereo (MVS) algorithms offers a solution for testing highly tortuous materials, and its utility at fine-scale remains underexplored. This study adapts photogrammetric workflows specifically for rubberised concrete (RuC), a sustainable composite exhibiting high ductility and complex fracture morphologies. High-resolution image sets were captured using a Canon DSLR and an iPhone 16 to generate dense 3D models. Comparisons revealed that the DSLR-based reconstruction achieved sub-millimetre resolution, demonstrating superior performance for fine-scale surface monitoring. An RGB-guided crack extraction method was developed to enhance the identification of surface defects and isolate potential crack areas from the background. The extracted crack regions were visually distinguishable and provided a well-structured geometrical representation of defect morphology. Furthermore, a Pre and Post-Test deformation analysis was conducted to quantify surface displacement across testing stages. The results confirm that this close-range photogrammetry workflow is a flexible, high-resolution alternative to LiDAR for surface inspection and deformation monitoring of specimens in laboratory settings. Ultimately, this approach establishes a robust geometric baseline for future automated 3D feature characterisation and material performance evaluation.

---


### 25. [A Case-Control Measurement Study of OSINT Source Effectiveness for Critical Infrastructure Defense](https://arxiv.org/abs/2608.21471)

**<font color=#1a73e8>作者：</font>** Ekrem E. Emeksiz, Jeel Piyushkumar Khatiwala, Divyangkumar Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defenders of critical infrastructure (CI) subscribe to many public open-source intelligence (OSINT) feeds without an empirical basis for which feeds actually precede attacks. We provide one. Across 54 confirmed CI cyberattacks from 2010 through 2024 spanning twelve named CI sectors plus a cross-sector category (consolidation rules in Section IV), paired with 12 null-control vulnerability cases drawn from the same source space, we audit per-source attack coverage, null-case contamination, and signal lead time for ten public OSINT source classes that meet a minimum-volume threshold. Sources separate cleanly into three operationally distinct mission profiles (pooled Fisher exact p = 3.4x10^-8): precursor (six classes with zero observed null firings at coverage at or above 5%), disclosure-exposure (three classes whose null contamination meets or exceeds attack coverage), and one large broad-coverage class that mixes the two profiles but retains 91.3% within-corpus precision. The precision-side classification is stable across a 2019 temporal partition and across a US-versus-non-US geographic partition. Two sources, one broad-coverage and one precursor, cover 92.6% of corpus attacks; three cover 96.3%. The greedy portfolio at k = 3 outperforms the mean random three-source subset by 39.8 percentage points. Several source classes widely treated as canonical for industrial control system defense fall into the disclosure-exposure profile by operational mission, not by quality. Per-sector, per-actor, and per-jurisdiction portfolios diverge in rank order despite a shared rank-one source. The corpus, linkage protocol, and classification rules are released.

---


### 26. [Class-Conditioned Gaussian Mixture Modeling for Imbalanced Time Series Quantification](https://arxiv.org/abs/2608.21473)

**<font color=#1a73e8>作者：</font>** Md Shahriar Kabir, Mayesha Maliha R. Mithila, Anne H. H. Ngu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantification, estimating class prevalences in bags of unlabeled instances is vital in domains where aggregate statistics are more important than individual instance labels, such as biosignal monitoring, fall detection, and activity recognition. We investigate this issue in the challenging setting of imbalanced time series data and develop CC-GMNet-TS, a class-conditioned Gaussian mixture quantifier that combines a Transformer-based feature extractor with per-class latent mixtures. Unlike previous mixture-based quantifiers, which use a single Gaussian mixture shared by all classes, CC-GMNet-TS assigns each class its own compact mixture in a bounded latent space and scores segment embeddings against these class-specific components to create bag-level representations that emphasize rare but informative patterns. Bags are constructed from labeled pools using the Artificial Prevalence Protocol (APP) and prior shift bag sampling (PShift) to cover a wide range of class prevalence scenarios, and the model is trained end-to-end with a quantification-oriented loss. Experiments on three benchmarks: EMG Data for Gestures, SmartFallMM, and UCI-HAR show that CC-GMNet-TS achieves lower error across the three benchmarks compared to traditional aggregators and recent deep quantifiers, while ablations confirm the contributions of both the Transformer backbone and class-conditioned mixtures during PShift.

---


### 27. [Explainable Adaptive Zero Trust Framework for AWS with Adversarial Robustness Evaluation](https://arxiv.org/abs/2608.21477)

**<font color=#1a73e8>作者：</font>** Om Singh, Yagyaraj Pandey, Nandini Pathak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud environments built on Amazon Web Services face a structural security vulnerability: once a credential passes authentication, the resulting session is often treated as trusted for its entire duration. This assumption fails when credentials are stolen. We introduce the Explainable Adaptive Zero Trust Framework (EAZTF), a cloud-native security layer that continuously reevaluates the legitimacy of API actions throughout a session.
EAZTF combines Isolation Forest and XGBoost to evaluate eight CloudTrail and IAM-derived behavioral features in real time and produce a Trust Risk Score (TRS) that determines whether a session continues, requires step-up MFA, or is restricted. Each decision is accompanied by a SHAP or LIME explanation, providing human-readable audit records for security analysis and compliance. The framework is also evaluated against four adversarial evasion strategies: credential theft, behavioral mimicry, API rate evasion, and privilege escalation.
Experiments on an 8,500-record synthetic CloudTrail dataset show that Isolation Forest achieves 94.4% precision, 91.2% recall, and an F1 score of 0.928. Across the four adversarial scenarios, the mean detection rate is 91.0%, with behavioral mimicry being the most difficult at 83.9%. SHAP analysis identifies IP reputation, login-time deviation, and API call velocity as the three dominant features. A structured NIST SP 800-207 self-assessment gives EAZTF a mean compliance score of 93%, compared with 38% for a traditional perimeter baseline. Mean time to detect decreases from hours to under one minute. Because the evaluation uses synthetic data, these results should be interpreted as indicative rather than validated production performance.

---


### 28. [Congruence Decomposition with Neural Block Solvers for Large-Scale PCI Assignment](https://arxiv.org/abs/2608.21485)

**<font color=#1a73e8>作者：</font>** Yeqing Qiu, Chengpiao Huang, Ye Xue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical Cell Identity (PCI) assignment is essential for interference management in dense 5G networks. As cellular networks scale, PCI reuse becomes unavoidable, which may cause collisions, confusions, and multiple forms of modular interference. Jointly mitigating these effects gives rise to a large-scale, multi-objective combinatorial optimization problem that is difficult to solve efficiently at practical network scales. In this work, we propose a congruence decomposition framework with neural block solvers for large-scale PCI assignment. The proposed decomposition exploits the arithmetic structure of PCI values to decouple multiple modular interference objectives into a collection of blockwise Min-$k$-Partition subproblems, followed by a graph coloring procedure to resolve PCI conflicts. For the resulting NP-hard Min-$k$-Partition subproblems, we develop neural block solvers by parameterizing their relaxed quadratic formulations with graph neural networks, enabling efficient optimization at large scales. Discrete assignments are recovered through conditional expectation rounding with theoretical guarantees. Experiments on synthetic cellular graphs and real-world 5G networks show that the proposed method consistently outperforms existing modular-interference-aware baselines in modular interference reduction, conflict elimination, and computational efficiency.

---


### 29. [KAN-Robust-Bench: A Benchmark for Evaluating the Robustness of Kolmogorov-Arnold Networks](https://arxiv.org/abs/2608.21488)

**<font color=#1a73e8>作者：</font>** Mohammad Meymani, Roozbeh Razavi-Far  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While machine learning models have demonstrated strong performance in many domains, these models have shown profound vulnerabilities when they are exposed to adversarial threats. While adversarial attacks fall into various categories, the most prominent category in research studies is evasion. In evasion attacks, the adversary generates perturbed versions of samples, which might not be observable by human eyes. These samples generally fool the machine learning models with high confidence. This phenomenon poses a significant security violation against machine learning models. In this paper, we investigate the certified and empirical robustness of various Kolmogorov-Arnold network architectures against strong evasion attacks. At first, we provide the mathematical foundations for randomized smoothing and interval bound propagation, and report the $\ell_2$-certified robustness of the models under randomized smoothing. After that, we systematically evaluate the robustness of various defended and undefended KAN models under FGSM, PGD, and C&W attacks in order to find out the optimal defense strategies and architectures.

---


### 30. [The geometry of AI validation: Exact certification limits for iid best-of-N search](https://arxiv.org/abs/2608.21496)

**<font color=#1a73e8>作者：</font>** Ricardo Fitas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly generate alternatives, inspect evidence, and deploy a selected output. Validation is therefore target-relative: evidence certifies deployment only in directions resolved by the interventions that produced it. We represent validation and deployment rules as kernels over a reliability surface. Their span geometry separates replication, which reduces sampling noise, from new intervention directions, which reduce structural blindness. We make this principle exact for iid best-of-$N$ search. Under scalar ranking, randomized ties, maximum selection, bounded binary truth, and a stable rank-truth relation, knowing best-of-$n$ reliability through $n=m$ leaves exact ambiguity width $B_{m,N}=1+2\sum_{r=1}^{m}(-1)^r\cos^{2N}{r\pi/[2(m+1)]}$. Explicit bounded worlds attain the entire interval, and the complete prefix is information-maximal among reliability-mean audits confined to $n\le m$. The governing scale is $m^2/N$: when $m$ is proportional to $\sqrt{N}$, ambiguity remains about 0.83, while width $\varepsilon$ requires $m$ of order $\sqrt{N\log(1/\varepsilon)}$. Monotonicity gives an exact uniform-approximation frontier; a Lipschitz bound gives an exact capped-tail dual and order-sharp $L/m^2$ ambiguity. These results yield a two-gate audit rule: establish structural coverage, then add independent tasks for precision. Retrospective studies of mathematical reasoning and code selection construct compatible deployment values with wide separation and show that a score-tail audit rule frozen on 82 discovery tasks substantially reduces held-out error. Beyond iid search, the geometry applies only to known or independently estimated kernels; the empirical analyses are illustrative rather than prospective interventions.

---


### 31. [Selection of Heart Sound Segments for Synchronous Classification of Multi-channel Heart Sounds](https://arxiv.org/abs/2608.21499)

**<font color=#1a73e8>作者：</font>** Marcelo Nogueira, Jorge H. Oliveira, Carlos F. Ferreira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiac auscultation remains the most cost-effective screening procedure for cardiovascular diseases, and requires listening at the four main auscultation spots. Despite this, automatic heart sound analysis algorithms mostly classify patients using a single heart sound (single-channel), or, when using more than one (multi-channel), analyze each channel individually. To our knowledge, no prior work classifies patients through the synchronous analysis of multi-channel heart sounds, following the procedure used by physicians. This motivates us to study whether synchronous multi-channel analysis outperforms single-channel approaches, and whether it holds an advantage over asynchronous multi-channel methods that analyze channels one by one, potentially by capturing inter-channel interference phenomena. To answer these questions, we introduce a selection algorithm that identifies optimal heart sound segments from each of the four auscultation spots, which are then fed into a multi-input CNN that classifies patients by analyzing the four selected sounds simultaneously. Our synchronous approach, combining the proposed selection algorithm with a multi-input CNN, achieves a superior overall accuracy of 96.5\%, a 9.1\% gain over the best-performing single-channel and asynchronous multi-channel methods. The benefit of the proposed segment selection strategy over random selection is confirmed by a paired statistical significance test ($p = 0.003$). These results were obtained on 735 patients from the CirCor DigiScope dataset with complete recordings from all four spots, and their scope and generalizability are discussed in light of this and other methodological considerations.

---


### 32. [Multimodal Injury Risk and Performance Prediction in Tennis Using Weighted Ensemble Learning](https://arxiv.org/abs/2608.21530)

**<font color=#1a73e8>作者：</font>** Weihao Qu, Dongyang Wang, Ling Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has had a positive impact on the sports industry, with one of its most promising applications being the prediction of athlete performance and injury risk. Recent advances have employed state-of-the-art models to improve prediction accuracy, yet progress remains limited by data availability and the reliance on subjective observations or expert assessments. To address these limitations, researchers in sports such as soccer, basketball, and wrestling have begun integrating heterogeneous data sources, such as wearable device readings, with traditional subjective assessments. However, similar multimodal approaches remain underexplored in tennis. In this work, we propose a multimodal weighted ensemble learning framework, Predictive Athlete Readiness for Tennis (PART), to monitor athlete wellness and estimate near-term injury risk in tennis players. PART processes a wide range of inputs, including physiological metrics, training and match data, sleep information from wearable devices, self-reported questionnaires, vertical jump assessments, and motion analysis from match-play videos. From these modalities, specialized machine learning and deep learning models independently extract four athlete-specific characteristics: overall wellness, injury risk, physical capability, and playing style. To overcome the complexity of combining these diverse modalities, PART employs a supervised weighted ensemble integration strategy, assigning adaptive weights to each predictive model based on its reliability. Evaluation of multimodal data collected from nine collegiate tennis players demonstrates that PART achieves strong performance in monitoring athlete wellness and estimating near-term injury susceptibility. Beyond collegiate athletes, the framework also shows promise for recreational tennis players, offering personalized insights to mitigate injury risk and optimize performance.

---


### 33. [Federated Continual Learning as a Distributed Drift-Plus-Penalty Control Problem](https://arxiv.org/abs/2608.21539)

**<font color=#1a73e8>作者：</font>** Nazreen Shah, Naveen Kumar Reddy Somireddy, Zubair Shaban 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Continual Learning (FCL) is fundamental to real-world distributed learning systems, requiring models to adapt to sequential, non-IID data across clients while mitigating catastrophic forgetting and client drift. Existing approaches formulate continual learning (CL) as a sequence of per-task optimization problems, applied locally at each client and coupled through aggregation, using heuristic mechanisms such as replay, regularization, or projection-based constraints. However, forgetting in FCL is inherently a long-term, distributed phenomenon, arising from the interaction of temporal task evolution and cross-client heterogeneity, which is not explicitly regulated. In this work, we cast FCL as a stochastic control problem and propose Federated Queue-regulated Continual Learning (FedQCL), a framework based on Lyapunov drift-plus-penalty (DPP) optimization. FedQCL introduces virtual queues to track the accumulation of forgetting across tasks and clients, enabling explicit control of the stability-plasticity trade-off. By optimizing a DPP objective, the method jointly improves current-task performance while the queue-based formulation provides an interpretable and tunable mechanism to balance adaptation and retention through a single parameter, without requiring gradient projection or additional communication overhead. Empirical evaluations on standard benchmarks, including Split-CIFAR-10, Split-CIFAR-100, and Split-TinyImageNet, demonstrate that FedQCL outperforms state-of-the-art baselines with respect to accuracy while significantly reducing forgetting under heterogeneous data distributions.

---


### 34. [Loss-Parameterized Fisher Width Along Learning Trajectories](https://arxiv.org/abs/2608.21561)

**<font color=#1a73e8>作者：</font>** Vu Khac Ky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fisher width measures the Gaussian width of a probe set after deformation by the local Fisher geometry. We study its evolution along learning trajectories and ask when training loss can serve as an effective coordinate for this quantity.
We first derive an exact trace--shape factorization and a deterministic stability bound for fixed compact probes. In a population Gaussian-teacher logistic model, the teacher-aligned state is extremal on every loss level below $\log 2$: it has minimal parameter norm and maximizes both Fisher trace and Euclidean-ball Fisher width. We then show that population gradient flow asymptotically selects this branch, with explicit rates for the aligned and orthogonal coordinates. This yields, for $d\geq2$, \[
\frac{w_F(B_2^d;\theta(t))}
{\sqrt{L(\theta(t))}}
\longrightarrow
\frac{\sqrt6}{\pi}\mathbb E[\chi_{d-1}]. \] Controlled full-Fisher experiments support the matched-loss branch and the population predictions. In a nonlinear MLP with a diagonal model-Fisher approximation, GD and SGD remain close at matched loss, whereas Adam follows a substantially displaced branch; the fixed probes tested retain highly similar temporal shapes. These results support a branchwise, rather than universal, loss parametrization of Fisher width.

---


### 35. [Quantifying geographic domain shift to decouple the geospatial transferability of human mobility flow generation models](https://arxiv.org/abs/2608.21567)

**<font color=#1a73e8>作者：</font>** Zhiyong Zhou, Song Gao, Qianheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human mobility serves as an essential proxy for understanding social, economic, and environmental dynamics in urban systems. Geospatial transferability, which measures a model's capability in a new location or unseen region, is a critical dimension for comparing different human mobility generation models. However, few studies have studied the intrinsic characteristics of geospatial transferability. To this end, this study systematically investigates the geospatial transferability of four representative human mobility generation models using a large-scale benchmark dataset of census tract level commuting flows across 2265 counties in the United States. Inspired by the domain adaptation theory in machine learning, we introduce geographic domain shift to describe the intrinsic differences in geographic feature distributions and spatial structures between source and target regions, which may jointly affect model transferability. Moreover, we propose two metrics, mutual information and spatial shift, to quantify the geographic domain shift. To examine their associations with model transferability, we employ linear mixed-effects regression to analyze the associations between geographic domain shifts and transferability. Our results reveal substantial spatial heterogeneity and asymmetry in transfer performance across regions. Both information shift and spatial shift exhibit statistically significant and complementary explanatory power. This indicates that geospatial transferability depends not only on model design but also on intrinsic geographic differences. These findings provide a novel methodological framework for evaluating and improving the geospatial transferability of human mobility generation models and support more robust and fair human mobility data synthesis across diverse regions. It also offers insights on spatial transferability for GeoAI model development.

---


### 36. [Extending the Horizon of Early Diagnosis: Lung Cancer Prediction with Vision Transformers](https://arxiv.org/abs/2608.21571)

**<font color=#1a73e8>作者：</font>** Olivera Kotevska, Ian Goethert, Michael McGee 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung cancer remains a leading cause of cancer-related mortality worldwide, and early diagnosis is critical for improving survival. However, early-stage malignancies can be subtle on chest X-rays, creating challenges for radiologists. This study evaluates Vision Transformers (ViTs) for predicting lung cancer one to two years before clinical diagnosis. We analyzed 259,361 chest X-rays from 91,020 imaging studies at the Jamaica Plains VA Hospital in Boston, MA. The dataset showed extreme class imbalance, approximately 1:150 cancer to non-cancer, which was addressed using hybrid under- and over-sampling and class-weighted loss optimization. Three ViT configurations were evaluated: a model trained from scratch, an ImageNet-pretrained model, and a Corona-pretrained model fine-tuned on the lung cancer dataset. Transfer learning improved performance, with pretrained models exceeding the scratch baseline by 6-10 percentage points in AUC and about 10-12 percent in balanced accuracy. ImageNet-pretrained models showed the most stable overall performance, while Corona-pretrained models achieved higher sensitivity in some settings but greater variability. Moderate resampling ratios, including 1:1 undersampling and 1.5:2 oversampling, provided favorable trade-offs between sensitivity, precision, and computational efficiency, reducing runtime by up to 70 percent without major performance loss. These findings demonstrate the potential of ViTs for early lung cancer risk prediction from routine chest X-rays. Although performance remains below clinical deployment thresholds, the results support further development of ViT-based triage systems to flag high-risk patients for earlier evaluation.

---


### 37. [Sorting from Counterexamples](https://arxiv.org/abs/2608.21579)

**<font color=#1a73e8>作者：</font>** Noga Alon, Shay Moran, Shlomo Moran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consider the following problem of learning an unknown linear order on $n$ items. In each round, the learner guesses a complete ordering of the items and receives either confirmation that the guess is correct or a counterexample: a pair of items in the wrong order. The goal is to identify the unknown order using as few queries as possible. We study this problem when up to $k$ of the returned counterexamples may be untruthful, where $k$ is not known in advance. We determine the optimal query complexity up to constant factors: \[
\Theta(n\log n + nk). \] Thus, while the noiseless complexity matches the classical complexity of sorting, each untruthful counterexample incurs an additional cost of order $n$. The upper bound is based on a geometric representation of permutations and Grünbaum's theorem, while the lower bound combines sorting arguments with a Condorcet-type construction. We also study the case where the target ranking has a low-dimensional geometric representation: each item is represented by a point in $\mathbb{R}^d$, and the ranking is obtained by projecting the points onto an unknown direction. For these classes we give an upper bound of $O(d^2\log n+dk)$ and a lower bound of $\Omega(d\log n+dk)$, leaving a factor of $d$ gap in the noiseless term.

---


### 38. [Reading the Room: Implicit Confusion Encoding in Recurrent World Model States](https://arxiv.org/abs/2608.21582)

**<font color=#1a73e8>作者：</font>** Donald Aadithiyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models built on the RSSM architecture, such as DreamerV3, keep a recurrent hidden state $h_t$ trained only to reduce prediction error. We show this state also tracks its own confusion, hiding in plain sight: nearly orthogonal to $h_t$'s directions of greatest variance, invisible to any variance-based method. It is functionally distinct from ensemble disagreement, which flags new inputs, and reconstruction error, which flags bad predictions right now. On a test holding prediction error fixed while confusion varies, a linear probe on $h_t$ finds the signal (AUROC 0.72, 5 runs), while an ensemble baseline scores below chance. A discounted count of recent high-error steps explains 80% of the probe's output ($R^2=0.80$). We confirm the signal is causally used, not merely present, by editing $h_t$ directly and watching behaviour change, including a check using real values from other trajectories instead of synthetic edits. Its geometry and closed form generalize across three control tasks; the decisive dissociation test itself holds cleanly on only one, and its practical use, deciding when to check reality instead of trusting imagination, generalizes to only two of the three tasks.

---


### 39. [Robust Lightweight Deep Learning Models for Oral Cancer Screening](https://arxiv.org/abs/2608.21583)

**<font color=#1a73e8>作者：</font>** Siddhant Bharadwaj, Aakash Shedsale, Tejashree Subramanya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Oral cancer is a leading cause of mortality in low-to-middle-income countries, where a shortage of specialists delays diagnosis. While point-of-care screening via smartphones offers a scalable solution, developing robust AI for resource-constrained settings poses significant challenges, including class imbalance in training data, variable data quality, and computational constraints on edge devices. In this paper, we present the optimisation of lightweight deep learning models for smartphone-based oral cancer screening. Using a diverse, multi-centre retrospective dataset of approximately 30,000 images acquired over a decade, we systematically evaluate state-of-the-art convolutional, transformer, and hybrid architectures. Through rigorous pipeline ablation, we demonstrate that directly optimising hybrid architectures for the edge strictly outperforms computationally heavy paradigms, such as large models or knowledge distillation. Furthermore, interpretability analysis and simulated noise-stress tests revealed that the system anchors on clinical features and remains robust to unstructured sensor noise, despite vulnerabilities to impulse bit errors. In the held-out test set, our optimised MobileViTv2 models achieved an average sensitivity of 83.2 $\pm$ 1.5% and an average specificity of 86.0 $\pm$ 0.8%, with the best model exhibiting 87.4% sensitivity, 86.5% specificity, and a critical negative predictive value of 97.2% with reference to specialist labels. These results confirm that with targeted architectural selection and streamlined optimisation, interpretable and robust lightweight AI models exhibit high potential for edge deployment to enable automated triage in primary care settings.

---


### 40. [Predicting Early Functional Decline from Longitudinal Laboratory and Vital Sign Trajectories: A Large-Scale Study Using the All of Us Research Program](https://arxiv.org/abs/2608.21589)

**<font color=#1a73e8>作者：</font>** Rashmita Kudamala, Aravind V. Kuruvikkattil, Lalitha Pranathi Pulavarthy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional decline in older adults is typically recognized only after falls or observable gait impairment, closing the window for prevention. We investigated whether temporal trajectories of routine biomarkers, already recorded but rarely analyzed longitudinally, can identify patients in the pre-clinical phase of mobility decline. Using the All of Us Research Program (N = 297,861; 11.1% cases), we derived trajectory features (slope, variability, delta, mean) for twelve biomarkers over a three-year pre-index window. LightGBM models incorporating trajectories significantly outperformed static laboratory summaries (AUROC 0.797 vs. 0.755; DeLong p < 0.001; AUPRC 0.380 vs. 0.304). A 1:1 age- and sex-matched analysis confirmed an independent trajectory signal (AUROC 0.727 vs. demographics-only 0.680). A horizon analysis demonstrated sustained prediction 3-12 months before decline onset (AUROC 0.768-0.740). Because the model uses only measurements already ordered in routine care, it supports passive, zero-burden EHR integration for early detection of pre-clinical functional decline.

---


### 41. [Reaching the Tail: Calibration Diversity Drives Conformal Coverage under Data Scarcity](https://arxiv.org/abs/2608.21591)

**<font color=#1a73e8>作者：</font>** Donald Aadithiyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-horizon rare-event forecasting is hard under long macroeconomic series' data constraints: labeled events are scarce, and standard uncertainty quantification assumes an exchangeability that autocorrelation violates. A controlled ablation shows an apparent rare-event threshold for Adaptive Conformal Inference instead reflects calibration-set size. Across 200 random calibration sets, support width of the nonconformity-score distribution explains up to 85% of coverage variance versus 2% for rare-event count; the same, not the same magnitude, replicates across synthetic conditions and five countries (five-country Spearman $\rho$ 0.45-0.66 vs. 0.02-0.23). A diversity-maximizing selector built on this is the only strategy tested that improves long-horizon coverage (67.8% to 81.4% at six months); Mondrian, shift-robust, and extreme-value alternatives fail to close it. Mondrian even worsens coverage under oracle labels. A compact proposition explains why: coverage deficit reflects how closely the calibration set's upper quantile reaches the test distribution's. Diversity is necessary, not sufficient. Demonstrated on a two-stage U.S. recession-forecasting framework with RegressorChain, whether six-month coverage reaches 90% under honest scoring remains open, a question this paper quantifies rather than resolves.

---


### 42. [Generate in the Chart, Not on the Boundary: Function-Symbol Grounding for Hard Constraints in LTN-GANs](https://arxiv.org/abs/2608.21605)

**<font color=#1a73e8>作者：</font>** Nijesh Upreti, Vaishak Belle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logic Tensor Network-Enhanced Generative Adversarial Networks (LTN-GANs) inject background knowledge by grounding each logical axiom as a predicate and training the generator to raise its satisfaction, a fuzzy truth value in $[0,1]$. Previous LTN-GAN work grounded every constraint this way, at the predicate level, and improved constraint satisfaction. A predicate, however, only scores a sample, so it cannot embed hard structural constraints, rules such as orderings, positivity, and definitional identities that must hold in every generated sample. In this work, we investigate grounding each axiom as a function symbol inside the LTN framework. We compare against the state-of-the-art alternative, a constraint layer that clamps each violating sample onto the feasible boundary and so produces outputs that are always valid. Our investigation shows that a valid sample is not always a realistic one. An inequality is not merely satisfied or violated. It holds by a margin, and a faithful generator should also reproduce the margin's real distribution. We find that the resolution ratio $R$, the data's scale over the margin's spread, is a diagnostic, computable before training, of which constraints a chosen grounding can learn. When $R$ is large, the predicate receives no learning signal, the clamp pushes every sample onto the boundary, and the margin distribution is lost while every standard metric still looks fine. A function symbol avoids both failures, computing the constrained variable rather than scoring it. Together the function symbols form a chart, a coordinate system inside the feasible region, where every sample is valid by construction and the margin is learned like any other quantity.

---


### 43. [Subzero matrix completion for sparse data analysis: large-scale learning of latent low-rank structure](https://arxiv.org/abs/2608.21607)

**<font color=#1a73e8>作者：</font>** Lawrence K. Saul, Ningyuan Huang, Dennis Bollweg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate when a sparse nonnegative matrix can be recovered from a real-valued matrix of much lower rank by zeroing out its negative elements. The potential for such decompositions suggests a mathematical connection between sparsity and rank; we analyze a number of sparse matrices with this latent low-rank structure and use them to illustrate the geometric origins of this connection. Previous algorithms have discovered these decompositions via an alternating minimization over the factors of a low-rank matrix, but to do so, they have also needed to compute and store another matrix, neither sparse nor low-rank, that is the size of their product. We develop a stochastic, alternating least-squares algorithm that operates on smaller blocks of this dense matrix and scales as a result to much larger problems. We also show how to further accelerate this algorithm with sparse optimizations and customized CUDA kernels. As one example, we use the algorithm to analyze the sparse matrix of synaptic weights for the recently published $\textit{Drosphilia}$ connectome. The nonzero elements of this matrix, with 139,255 rows and columns, record the number of synapses between cells in the nervous system of a female fruit fly. Despite a slowly decaying spectrum of singular values, this matrix exhibits a latent low-rank structure that is predictive of cell categories across multiple levels of specificity.

---


### 44. [Hiding Directions, Leaking Structure: Breaking ArrowCloak through Low-Rank Structure](https://arxiv.org/abs/2608.21615)

**<font color=#1a73e8>作者：</font>** Beijie Liu, Junyi Ouyang, Haoxuan Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> TEE-shielded inference keeps sensitive state in a trusted execution environment (TEE) while offloading linear algebra to an untrusted accelerator. Wang et al., in Game of Arrows (USENIX Security 2025), showed that five widely adopted lightweight defenses preserve vector directions and introduced ArrowMatch to exploit this leakage. They then proposed ArrowCloak, which adds a different multiple of one shared mask direction to each vector and bases its weight-recovery hardness argument on Learning with Errors (LWE). ArrowCloak successfully reduces ArrowMatch to near-black-box levels.
In this paper, we revisit ArrowCloak from cryptographic and structural perspectives. Its LWE formulation does not by itself establish standard LWE hardness: the reduction direction, quantized arithmetic, and joint instance distribution do not meet the required conditions. Reusing one mask direction leaves a recoverable rank-one component across the released matrix. We exploit this structure with our proposed attack, an end-to-end, query-free recovery attack. Given a public checkpoint and the obfuscated weights, the attack removes the masking subspace, recovers the hidden one-to-one correspondence, and reconstructs protected weights without transformation secrets, victim queries, or fine-tuning data. Across six model-task pairs spanning classification, segmentation, and diffusion, the attack recovers 99.92%-100% of hidden vector correspondences. Reconstructed classification models achieve 94.39%-99.54% victim agreement and differ by at most 1.59 percentage points in accuracy; the recovered segmentation model achieves 98.35% output agreement. These findings suggest that lightweight protection should address both per-vector geometry and joint structure across released weights.

---


### 45. [FrugalSOT - Frugal Search Over the Models](https://arxiv.org/abs/2608.21621)

**<font color=#1a73e8>作者：</font>** Pradheep P, Yuvanesh S, Harish KB 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In on-device NLP tasks, limited resources of embedded hardware, such as the Raspberry Pi 5, require efficient inference strategies. This paper introduces FrugalSOT (Frugal Search Over The Models), a resource-aware model selection architecture for on-device NLP inference. FrugalSOT estimates each request's complexity by extracting features such as prompt length, named entity density, and syntactic complexity. The request is first made to the least complex model that is likely to pass a relevance threshold. If the output of that model falls short of the threshold, the request is made to a more complex model. It is important to note that the relevance threshold undergoes continuous updates in the background. using past validation outcomes in an adaptation process using a low-pass filtering mechanism, thus imparting adaptation to changing input patterns. Experimental results achieved on a Raspberry Pi 5 show that FrugalSOT reduces average inference time and overall computational resource use to a significant extent compared to a single-model baseline approach, without compromising output relevance to the same extent as the most sophisticated model. These results confirm that adaptive model selection can enable efficient, high-quality natural language processing inference on limited devices.

---


### 46. [Rethinking Communication Metrics: How Should We Measure Meaning?](https://arxiv.org/abs/2608.21626)

**<font color=#1a73e8>作者：</font>** Niloofar Tavakolian, Hakimeh Purmehdi, Jungyeon Baek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic communication shifts the objective of communication systems from accurate symbol reconstruction toward meaning preservation, task accomplishment, and efficient information exchange. However, its evaluation remains fragmented across telecommunications, natural language processing, computer vision, and machine learning, and no single metric can characterize semantic quality across modalities, tasks, and channel conditions. This article surveys key performance indicators (KPIs) for text- and image-based semantic communication systems from a unified, evaluation-centered perspective. Unlike prior surveys primarily organized around architectures, applications, or transmission strategies, this work focuses on how semantic success should be defined and measured. Existing KPIs are classified according to communication goal, source modality, receiver output, reference availability, evaluation level, and channel or resource constraints. The survey reviews reconstruction-based, task-oriented, reference-free, representation-level, perceptual, and channel-aware metrics, and presents a cross-modality comparison of their roles, strengths, and limitations. It further analyzes how unresolved semantic-KPI challenges affect monitoring, quality assurance, resource optimization, fault diagnosis, and standardization. Key open problems include the absence of universal semantic success criteria and standardized semantic ground truth, semantic drift, limited reference-free evaluation, weak integration of machine-learning metrics with communication constraints, and the lack of relation-level and multimodal KPIs. Finally, future research directions are outlined toward standardized, interpretable, adaptive, task-aware, and communication-aware evaluation frameworks.

---


### 47. [ChequeMark: An Ensemble Machine Learning Framework for After-Hours Business Deposit Fraud Detection](https://arxiv.org/abs/2608.21629)

**<font color=#1a73e8>作者：</font>** Ann Youduo Xu, Emily Yu, Justin Leski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cheque fraud is a material risk in after-hours business deposit operations because funds may be released within one business day, while cheque clearing takes several days. This timing gap creates a fraud exposure window for financial institutions. Prior mitigation relies on static, deposit-level checks and therefore miss historical client behavior and evolving patterns. To address this gap, we propose a multi-view ensemble ML framework that combines: Extreme Gradient Boosting (XGBoost) for known fraud patterns, Isolation Forest for label-free anomaly detection, and Graph Sample and Aggregate (GraphSAGE) for relational patterns associated with transaction activities. We then combine the three outputs into a single client-level risk score. Under stable conditions, performance is comparable to XGBoost; under a targeted distribution shift, our framework performs best (F1: 83.77%, FPR: 0.69%) versus XGBoost (F1: 82.77%, FPR: 0.72%). These results indicate improved robustness to distribution shift while preserving interpretability through plain-language explanations grounded in behavioural, anomaly, and relational evidence.

---


### 48. [Semantic Slots for Video Object-Centric Learning](https://arxiv.org/abs/2608.21636)

**<font color=#1a73e8>作者：</font>** Khalil Sabri, Guillaume-Alexandre Bilodeau, Nicolas Saunier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Object-Centric Learning (OCL) has traditionally focused on refining the encoder architecture to ensure temporal consistency. In this paper, we argue that the primary bottleneck lies in the decoder. We show that traditional decoders force slots to be spatially anchored, hindering their ability to adapt to motion. We propose SemanticSlots, which uses a Transformer-based decoder that leverages image context, relieving slots from encoding boundary precision and spatial location. This allows slots to function as semantic queries that are inherently object position invariant, retrieving matching features rather than memorizing coordinates. More importantly, this property allows slots computed from a single frame to decompose subsequent video frames, eliminating the need for complex temporal predictors or auxiliary temporal losses. Results on YouTube-VIS show that SemanticSlots improves upon VideoSAUR by 31 points in mBO and outperforms current state-of-the-art methods by 21 points, achieving 86.6% ARI and 62.8% mBO.

---


### 49. [Large-Scale Evaluation of Advanced Imputation Methods for Missing Values in Smart Meter Data](https://arxiv.org/abs/2608.21638)

**<font color=#1a73e8>作者：</font>** Daniela Stojcheska, Marija Markovska, Dimitar Taskovski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and reliable collection of electricity consumption data through Advanced Metering Infrastructure (AMI) is of great importance for the operation of smart grids, especially for the detection of non-technical losses (NTL). However, real-world datasets frequently suffer from missing values due to communication failures. This paper presents an empirical evaluation of three advanced algorithms for large-scale data imputation: the Optimally Weighted Average (OWA) method, Low-Rank Matrix Completion via SoftImpute, and a Shape-Modeling Autoencoder. Existing studies on missing value imputation in electricity consumption data often lack validation on larger datasets. Therefore, the goal of this paper is to validate the selected algorithms on a large-scale real-world electricity consumption dataset from North Macedonia that includes 17,428 commercial smart meters over two years. The robustness of each algorithm is evaluated by simulating continuous gaps in the data ranging from 1 to 168 hours. The results indicate that OWA provides the lowest overall reconstruction error across the evaluated gap sizes and strong stability in worst-case scenarios for gaps of up to one week. In contrast, the autoencoder exhibits higher variance, while SoftImpute has stable but inferior accuracy. These findings suggest that imputation methods should be selected based on the characteristics of load curve data and highlight the potential for hybrid algorithmic architectures in future grid management systems.

---


### 50. [Cross-Layer Roots of Trust: Integrating Biometrics, PUFs, and Hardware Obfuscation](https://arxiv.org/abs/2608.21643)

**<font color=#1a73e8>作者：</font>** Nima Karimian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern cyber--physical, Internet-of-Things (IoT), wearable, and edge systems increasingly require trust in three distinct entities: the human requesting access, the physical device executing the computation, and the hardware function that is permitted to operate. These requirements are usually studied in separate communities. Biometrics establish human identity but remain vulnerable to presentation attacks, intra-user variability, template leakage, and limited revocability. Physical unclonable functions (PUFs) provide device-specific physical identity and on-demand secret derivation, yet must address environmental instability, helper-data exposure, side channels, and modeling attacks. Hardware obfuscation and logic locking condition correct circuit behavior on an activation secret, but face oracle-guided, approximate, structural, removal, and physical attacks.
This survey develops a unified human--device--function view of trust. We first decompose each primitive into its complete processing chain and identify the corresponding security assumptions, implementation mechanisms, and evaluation metrics. We then formalize pairwise compositions---biometric--PUF, PUF--obfuscation, and biometric--obfuscation---and a three-way architecture in which correct functionality is bound jointly to an authorized user and a genuine device. Particular attention is given to biometric key reconstruction, PUF stabilization and modeling resistance, logic-locking attack evaluation, cross-layer error propagation, enrollment trust, key lifecycle, and interface leakage. The survey concludes with a taxonomy and research agenda for revocable human--device credentials, compositional security, leakage-aware integration, reconfigurable activation, and standardized end-to-end evaluation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
