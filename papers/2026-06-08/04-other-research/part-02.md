# 📦 其他研究 | 2026年06月08日

> 本类共 **289** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-289](./part-06.md)

---

### 51. [Agents' Last Exam](https://arxiv.org/abs/2606.05405)

**<font color=#1a73e8>作者：</font>** Yiyou Sun, Xinyang Han, Weichen Zhang 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI systems have achieved strong results on a wide range of benchmarks, yet these gains have not translated into economically meaningful deployment across many professional domains. We argue that this gap is largely an evaluation problem: widely used benchmarks lack sustained performance measurement on real and economically valuable workflows. This paper introduces Agents' Last Exam (ALE), a benchmark designed to evaluate AI agents on long-horizon, economically valuable, real-world tasks with verifiable outcomes. Developed in collaboration with 250+ industry experts, ALE covers non-physical industries defined with reference to O*NET / SOC 2018 (the U.S. federal occupational taxonomy). It is organized around a task taxonomy with 55 subfields grouped into 13 industry clusters covering 1K+ tasks. Current results show that the hardest tier remains far from saturated: across mainstream harness and backbone configurations, the average full pass rate is 2.6%. ALE is designed as a living benchmark: its task pool grows continuously as new workflows and industries are onboarded. More broadly, ALE is intended not merely as another leaderboard, but as an instrument for closing the gap between benchmark success and GDP-relevant impact.

---


### 52. [Would you still call this Dax? Novel Visual References in VLMs and Humans](https://arxiv.org/abs/2606.05409)

**<font color=#1a73e8>作者：</font>** Ada Defne Tür, Gaurav Kamath, Joyce Chai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs), like human learners, are frequently exposed to new visual concepts, but how they map novel visual references to language after exposure remains largely underexplored, particularly when those references contradict prior knowledge from pre-training. To study this, we present the Novel Visual References Dataset (NVRD): 19,176 images spanning 90 visual concepts across different levels of visual novelty, each with up to 20 increasingly perturbed versions of the original object to probe generalization. Unlike prior work on visual augmentations of familiar concepts, NVRD comprises entirely novel, open-ended stimuli constructed from scratch, mirroring how humans encounter genuinely new concepts. We evaluate 3 open- and 2 closed-source models alongside 2,400 human judgments for direct human-model comparison, and find that (i) models struggle to acquire novel concepts in-context when they contradict prior knowledge, and (ii) while models and humans show correlated sensitivity to visual perturbations, models significantly overgeneralize, extending learned labels to stimuli that humans reject. We contribute NVRD as a corpus and benchmark for research on visual concept learning in both humans and machines.

---


### 53. [A Motivational Architecture for Conversational AGI](https://arxiv.org/abs/2606.05411)

**<font color=#1a73e8>作者：</font>** Anna Mikeda, Ben Goertzel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Motivational architectures in cognitive AI have largely been designed for physical agents regulating bodily needs. Conversational agents operate in a different regime: their sensorimotor loop is linguistic, their environment is a user's evolving mental state, and their consequential actions are speech acts, tool invocations, and strategic silences. This paper proposes a conversational reinterpretation of the OpenPsi motivational lineage, coupled to MetaMo's higher-level motivational scaffold, for agents built on a modular execution substrate. Homeostasis is recast in dialogue-native terms: the agent regulates competence, uncertainty reduction, affiliation, affinity, legitimacy, nurturing, and aesthetic coherence rather than bodily deficits. We propose three contributions: a ten-stage motivational processing pipeline that architecturally separates cognitive modulation from situational appraisal; a dual decision strategy blending urgency-driven fast response with deliberative multi-goal optimization; and an architecturally useful distinction between pre-action feelings and post-action emotions as functionally different forms of affect. We specialize the framework to two example agents -- CompanionAgent and ResearchAgent -- and sketch its extension to social robotics and domain-generic human-level AGI.

---


### 54. [CausalPOI: Spatio-Temporal Graph-Based Causal Modeling for Cold-Start POI Check-in Forecasting](https://arxiv.org/abs/2606.05413)

**<font color=#1a73e8>作者：</font>** Zhaoqi Zhang, Miao Xie, Yi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As urban environments continue to evolve rapidly, accurately modeling the dynamic behaviour of Points of Interest is essential for supporting data-driven urban planning and commercial decision-making. While recent advancements in spatio-temporal graph learning have improved POI forecasting, most methods rely on proximity-based graphs and correlation-driven modeling, which overlook the functional dependencies between POIs and fail to capture the causal effects of urban interventions. In this paper, we introduce a novel research problem -- cold-start POI check-in forecasting, which aims to predict the future check-in pattern of a newly introduced POI, by modeling its temporal evolution and functional interactions with nearby POIs in a structured urban spatial context. To address these challenges, we propose CausalPOI, a spatio-temporal graph-based causal representation learning framework. CausalPOI leverages Spatio-Temporal Functional Interaction Graph to model semantic and spatial relationships between POIs, and constructs structurally aligned treatment and control graphs to simulate factual and counterfactual scenarios. Extensive experiments on real-world SafeGraph datasets demonstrate that CausalPOI significantly outperforms state-of-the-art baselines across the board, validating its effectiveness in spatio-temporal forecasting, semantic interaction modeling, and causal effect estimation, providing a more interpretable and actionable foundation for urban intervention analysis. Source code is available at Github.

---


### 55. [Executable Schema Contracts: From Automatic Ingestion to Multi-Source Retrieval](https://arxiv.org/abs/2606.05415)

**<font color=#1a73e8>作者：</font>** Padmaja Jonnalagedda, Yuguang Yao, Xiang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world data spans tables, documents, and semi-structured files with implicit semantics. Querying this data requires integrating evidence across inconsistent schemas and formats, yet existing approaches either demand costly manual engineering or bypass structure entirely. We present a system that automatically discovers an executable schema from raw multi-source data and uses it as a shared contract for knowledge graph construction and query-time retrieval. A closed-world field catalog constrains LLM-based schema discovery to attested fields; deterministic structural analysis infers identity keys, foreign keys, and source hierarchy; and the resulting schema drives extraction, deduplication, and cross-source linking into a provenance-aware knowledge graph. At query time the schema -- optionally extended via a monotonic protocol -- conditions a multi-tool agent routing retrieval across structured lookup, graph traversal, and vector search, returning grounded answers with traceable citations. In controlled zero-shot comparisons using the same LLM, data, and evaluation harness, the system improves over retrieval-only and decomposition-based baselines across four QA benchmarks, with ablations showing that schema-conditioned routing, structural intelligence, and schema-guided construction each contribute to the gains.

---


### 56. [A formal framework for the economic security of DeFi compositions](https://arxiv.org/abs/2606.05418)

**<font color=#1a73e8>作者：</font>** Massimo Bartoletti, Riccado Marchesin, Roberto Zunino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized Finance (DeFi) services are usually constructed by composing a variety of smart contracts. While composability is a key driver of the success of DeFi, it also creates security risks: adversaries may exploit interactions between newly deployed contracts and the pre-existing ones to inflict economic losses. We introduce MEV non-interference, a formal security notion for DeFi composability requiring that the maximal extractable value from a set of newly deployed contracts is not increased by interactions with the existing blockchain state. To support this notion, we define local MEV, a novel measure of economic attacks that focusses on the loss of a given set of victim contracts. We study two adversarial models, with bounded and unbounded wealth, and establish sufficient conditions and locality principles that enable modular reasoning about secure composability. We apply the framework to representative DeFi compositions, including exchanges, AMMs, options, lending pools, routers, and arbitrage contracts, showing how it distinguishes secure compositions from vulnerable ones. Our results provide a formal foundation for reasoning about the economic security of DeFi compositions.

---


### 57. [Assessing the Carbon Emissions and Energy Consumption of U.S. Hyperscale Data Centers](https://arxiv.org/abs/2606.05420)

**<font color=#1a73e8>作者：</font>** Gianluca Guidi, Francesca Dominici, Tiziano Squartini 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of hyperscale data centers (HDCs) in the US, mainly driven by the adoption of artificial intelligence, has raised concerns about this industry's environmental footprint. We compiled facility-level information on 403 US hyperscale data centers operating between May 2024 and April 2025 and estimated their electricity consumption, electricity sources, and attributable CO2 emissions. Across different facility-load scenarios, these HDCs consumed approximately 68-99 TWh of electricity and were associated with about 37-54 million metric tons of CO2. Under the central scenario, HDC electricity demand corresponded to approximately 1.8% of total US electricity consumption, with roughly 54% of attributed generation supplied by fossil-fuel sources. The HDC electricity-weighted average carbon intensity was approximately 545 gCO2/kWh, about 48% above the contemporaneous US national grid-average carbon intensity of 370 gCO2/kWh. Our approach provides an attributional tool for assessing the environmental footprint of hyperscale data centers using the most recent EPA eGRID plant-level data.

---


### 58. [ComplexityMT: Benchmarking the Interaction Between Text Complexity and Machine Translation](https://arxiv.org/abs/2606.05421)

**<font color=#1a73e8>作者：</font>** Joseph Marvin Imperial, Junhong Liang, Belal Shoer 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a text is translated, does the translation retain the complexity of the original? We introduce ComplexityMT, a new challenge for assessing how text complexity and machine translation interact with and influence each other, using the Common European Framework of Reference for Languages (CEFR) levels as the measure of text complexity. Across six languages, including Arabic, Dutch, English, French, Hindi, and Russian, we evaluate three open-weight models, one closed model, and a commercial machine translation system on two tasks: i) correlation of CEFR with translation difficulty, and ii) shifts in CEFR levels of the source texts. Our experiments show that higher CEFR levels make texts more difficult to translate, and that machine translation shifts the CEFR level of the target text compared to the original source, for most languages. These findings provide new insights for researchers and practitioners working on multilingual pedagogical content generation and machine translation difficulty estimation.

---


### 59. [Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433)

**<font color=#1a73e8>作者：</font>** Pierre Peigné, Ky Nguyen, Paul Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI governance frameworks increasingly use cumulative training compute as the primary criterion for designating high-impact models, but enforcement rests on self-reporting because no technical verification primitive for training exists. Any future international agreement on frontier AI faces the same problem at higher stakes: coordinated regulation of technologies with significant externalities has historically rested on technical verification, without which agreements are declaratory. Recent governance analyses judge zero-knowledge proofs a promising candidate but currently impractical at frontier scale [26, 4]. We argue the impracticality is paradigm-bound rather than fundamental, and propose a verification architecture for frontier dense pre-training combining a pre-committed training specification, inter-node network observations, and on-the-fly Merkle commitments of intermediate computation, verified through a zero-knowledge Virtual Machine (zkVM) with native BF16/FP32 precompiles. The proof checks the actual floating-point computation the GPU performed rather than a fixed-point approximation, and preserves model-architecture confidentiality through a private training specification. The protocol produces three proof types: a genesis proof at initialisation, in-training step proofs across the run, and ex-ante attestations enforcing policy-relevant claims as running invariants, turning the training record into a governance-enforceable artefact. We estimate a deployable proof of concept within approximately 36 months at single-digit-percent training-side overhead, against a six-to-ten-year cycle for verification-grade custom silicon. Thirteen open research and engineering problems are catalogued as a research agenda for external contribution

---


### 60. [DP-MacAdam: Differentially Private Mechanism with Adaptive Clipping and Adaptive Momentum](https://arxiv.org/abs/2606.05435)

**<font color=#1a73e8>作者：</font>** Naima Tasnim, Lalitha Sankar, Oliver Kosut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private stochastic gradient descent (DP-SGD) has become the standard framework for privacy-preserving machine learning, yet its reliance on a fixed gradient clipping threshold to limit sensitivity remains a significant practical limitation. Adaptive clipping algorithms such as AdaClip shift and scale the gradient prior to clipping and adding noise so that the clipped gradient yields a more informative descent direction. The shift and scaling parameters are selected adaptively based on the empirical mean and variance. However, in existing adaptive clipping algorithms, these empirical estimates have not been also used for momentum to accelerate training itself. On the other hand, DP-Adam is an algorithm that exploits Adam-like momentum updates based on the gradient mean and variance to accelerate training, but does not exploit these estimates for adaptive clipping. In this work, we propose Differentially Private Mechanism with Adaptive Clipping and Adaptive Momentum (DP-MacAdam), a novel algorithm that combines these two approaches so as to use the same mean and variance estimates for both clipping and momentum. We perform an analysis showing that DP-MacAdam estimates the gradient variances in a bias-free manner. In addition, we empirically evaluate the privacy and accuracy of DP-MacAdam, demonstrating that it achieves improved model utility compared to DP-SGD, AdaClip, and DP-Adam baselines, without requiring manual tuning of the clipping threshold.

---


### 61. [Sharp First-Order Lower Bounds for Higher-Order Smooth Nonconvex Optimization](https://arxiv.org/abs/2606.05438)

**<font color=#1a73e8>作者：</font>** Dongruo Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the deterministic first-order oracle complexity of finding \(\epsilon\)-stationary points in smooth nonconvex optimization when the objective satisfies higher-order smoothness assumptions. While the classical \(\epsilon^{-2}\) rate is optimal under only Lipschitz gradients, higher-order smoothness leads to accelerated first-order upper bounds, most notably the \(\epsilon^{-7/4}\) rate under Lipschitz Hessians and the \(\epsilon^{-5/3}\) rate under Lipschitz third derivatives. The matching lower bounds, however, have remained open. We resolve this gap by proving a new dimension-free first-order lower bound for higher-order smooth nonconvex functions, valid for every finite smoothness order. In particular, our construction gives a matching \(\Omega(\epsilon^{-7/4})\) lower bound in the Hessian-Lipschitz case and a matching \(\Omega(\epsilon^{-5/3})\) lower bound in the third-order-smooth regime. The hard instance is based on a \emph{block-chain} mechanism that enforces blockwise oracle revelation while preserving the smoothness structure needed for the scalar hard instance. The lower-bound construction was discovered with the assistance of ChatGPT 5.5 Pro and subsequently verified by the authors.

---


### 62. [Multilingual Coreference Resolution via Cycle-Consistent Machine Translation](https://arxiv.org/abs/2606.05444)

**<font color=#1a73e8>作者：</font>** Adriana-Valentina Costache, Eduard Poesina, Silviu-Florin Gheorghe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coreference resolution is a core NLP task, having a broad range of downstream applications, e.g.~machine translation, question answering, document summarization, etc. While the task is well-studied in English, comparatively less attention is dedicated to coreference resolution in other languages, especially low-resource ones. To mitigate this gap, we propose a novel coreference resolution pipeline that harnesses machine translation (MT) from English to a target low-resource language, to generate or expand training data. To automatically validate the quality of the translated samples, we back-translate the samples and assess the similarity with the original English samples via cosine similarity in the latent space of a BERT model. The resulting similarity scores are integrated into the loss function to weight training samples according to their MT cycle consistency. Extensive experiments on four low-resource languages show that our pipeline brings significant performance gains in coreference resolution. Moreover, our pipeline enables accurate coreference resolution in languages where no previous corpora were available.

---


### 63. [Disentangled Fine-Grained Prototype Learning for Incomplete Image-Tabular Classification](https://arxiv.org/abs/2606.05455)

**<font color=#1a73e8>作者：</font>** Feixiang Zhou, Jianyang Xie, Zhuangzhi Gao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The missing-modality problem poses a significant challenge in image-tabular multimodal learning across a wide range of multimedia applications, including product understanding, recommendation systems, and medical diagnosis. This challenge is particularly pronounced when the two modalities are highly heterogeneous, as images and tabular attributes differ substantially in their semantic granularity and data distributions. Existing methods learn modality-invariant representations through disentanglement and alignment over global token-averaged features, capturing only coarse cross-modal consistency and overlooking fine-grained semantic and distributional misalignment, which hampers the exploitation of complementary cues under missing modalities. To address this, we propose DFPL, a novel framework for fine-grained prototype learning. Specifically, Shared-Specific Prototype Modeling (SSPM) extracts compact and diverse shared and modality-specific prototypes, and further performs prototype-level disentanglement to suppress redundant intra-modality correlations. Additionally, we propose a Prototype-guided Fine-grained Alignment (PFA) module that jointly enforces prototype-level distribution matching and prototype-to-class semantic alignment within a unified prototype space, thereby preserving both fine-grained distributional and semantic consistency across modalities. We further introduce a Class-aware Multi-scale Aggregation (CMA) module to adaptively aggregate shared semantics and modality-specific characteristics from global and prototype levels for robust predictions. Extensive experiments on three diverse image-tabular benchmarks demonstrate the superiority of our method compared to the previous approaches under various missing-modality settings. Code will be made publicly available.

---


### 64. [Horse Eye Blink Detection and Classification for Equine Affective State Assessment](https://arxiv.org/abs/2606.05458)

**<font color=#1a73e8>作者：</font>** João Alves, Signe Møller-Skuldbøl, Pia Haubro Andersen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated detection of equine facial action units (AUs) is a promising yet under-explored avenue for pain and affective state assessment in horses. Half and full-blink movements are recognised indicators of pain and stress, but as micro-expressions, their subtle, fine-grained nature makes them easily missed by the naked eye and only discernible through frame-by-frame video inspection, making reliable automated detection from video a particularly demanding task. We develop and evaluate three methods for automated blink classification from horse videos: a frame-based YOLOv12 detector, an optical flow magnitude thresholding approach, and a fine-tuned VideoMAE model, tested on a publicly available dataset. We achieve a macro-F1 score of 0.898 when doing blink classification and 0.926 on binary blink detection. Our results highlight both the potential and the inherent challenges of fine-grained AU detection for equine welfare monitoring.

---


### 65. [CRESS: Quantifying Vulnerabilities of Attack Scenarios in Hardware Reverse Engineering](https://arxiv.org/abs/2606.05459)

**<font color=#1a73e8>作者：</font>** Alexander Hepp, Matthias Ludwig, Michaela Brunner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The safety, security, and reliability of microelectronic systems depend on a trustworthy, secured supply chain and design flow. Globally distributed supply chains or unintentional design weaknesses leave the door open for attacks on the hardware level. These scenarios encompass counterfeiting, hardware trojans, or on-device attacks. For these, hardware reverse engineering (RE) results play a pivotal role. The ongoing publication of new RE-involved attacks motivated the development of the common RE scoring system (CRESS). The system enables a general classification of RE-involved scenarios for a common, consistent rating. In this work, the originally qualitative system is extended to a quantitative system. We performed an extensive interview study with experts in the field. The interview results allowed us to derive weights that measure the severity of different RE-involved attack categories. The weights form an equation that quantifies scenarios, resulting in the severity-indicating CRESS score. The score enables the coherent rating of novel scenarios, renders them comparable, and supports the development of effective countermeasures. To showcase the effectiveness of the quantitative CRESS Score, six selected case studies are rated qualitatively and quantitatively. The CRESS Score proves to be significantly more expressive than the industry-standard Common Vulnerability Scoring System (CVSS).

---


### 66. [ORACLE-CT: Anatomy-Aware Support Pooling for CT Classification](https://arxiv.org/abs/2606.05460)

**<font color=#1a73e8>作者：</font>** Lavsen Dahal, Yubraj Bhandari, Geoffrey Rubin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Abdominal CT disease classification is challenging because each scan is a large 3D volume with many possible findings, while diagnostic evidence is often confined to specific organs or anatomical compartments. Most study-level classifiers aggregate encoder features using anatomy-agnostic pooling or attention, creating a mismatch between localized disease evidence and global evidence aggregation. We propose ORACLE--CT, an encoder-agnostic anatomy-aware aggregation framework that uses multi-organ segmentation to define label-specific anatomical supports and restrict attention pooling to relevant regions. The framework supports single-organ, multi-organ union, comparative, localized, and global support strategies.
We evaluate ORACLE--CT with three encoder families: DINOv3, I3D--ResNet-121, and the radiology-native Pillar--0 encoder. Models are trained end-to-end on MERLIN and evaluated internally and under frozen external transfer to Duke--Abdomen and AMOS. Compared with global average pooling, support-masked pooling improved MERLIN macro-AUROC/AUPRC from 0.838/0.638 to 0.858/0.676 for DINOv3 and from 0.829/0.617 to 0.848/0.659 for I3D--ResNet-121. On harmonized 10-label external evaluation, DINOv3 improved on Duke--Abdomen from 0.802/0.628 to 0.835/0.683 and on AMOS from 0.742/0.313 to 0.762/0.350, with similar gains for I3D--ResNet-121. For Pillar--0, most gains came from learned attention, with smaller additional benefit from anatomical masking. ORACLE--CT improves discrimination and external robustness while preserving an auditable link between predictions and anatomical evidence.

---


### 67. [Output Type Before Quality: A Standards-Derived XAI Admissibility Rubric for Autonomous-Driving Safety](https://arxiv.org/abs/2606.05461)

**<font color=#1a73e8>作者：</font>** Abhinaw Priyadershi, Mandar Pitale, Jelena Frtunikj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety standards for ML-based autonomous driving specify the kind of evidence an assurance case must contain (directed cause-and-effect chains, quantified interventional effects, named root-cause variables), yet the XAI literature is organised by output type and technique family (saliency maps, feature attribution, counterfactuals, causal graphs, language traces). SHAP, the most-recommended ADS XAI method, returns a ranked feature list that no implementation effort can convert into a directed chain (Fig.1). We name this mismatch the evidence-type gap.
From AMLAS, ISO 26262, ISO21448, ISO/PAS 8800 we derive 19 testable evidentiary criteria across 7 lifecycle stages with representative clause-cited derivations and score six XAI method classes structurally.
Causal XAI emerges as structurally required to satisfy the derived criteria at three stages: hazard identification (+62% rubric gap), incident investigation (+50%), and data management (+50%); the verdict set is stable across thresholds T in (0%, 50%]$ and survives a worst-case single-cell flip down to T = 25%. At the remaining four stages, correlational or language-based methods are comparable or sufficient. The rubric identifies structural admissibility (necessary but not sufficient for compliance): an admissible method's specific output content may still be wrong, and validating that fidelity (the edges a fitted SCM produces, the cause a trace names) is the open assurance challenge. A single-VLA proof of concept on 1,996 real-world driving clips (79,840 rows, ten splits) is consistent with each method's observed output type matching its rubric prediction. XAI method selection for ADS safety assurance should be driven by lifecycle-stage evidence demand, not by method popularity.

---


### 68. [Formal Concept Lattices are Good Semantic Scaffolds for Concept-Based Learning](https://arxiv.org/abs/2606.05471)

**<font color=#1a73e8>作者：</font>** Deepika SN Vemuri, Sayanta Adhikari, Ankit Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning semantics is essential for deep learning models to be interpretable and better aligned with human reasoning. Concept-based models approach this by representing classes through meaningful semantic abstractions, but typically treat all concepts as a flat, unstructured set learned at a single neural network layer. This overlooks a fundamental property of human semantic understanding: concepts being organized hierarchically, from general to specific. While deep networks do learn a hierarchy of visual features, this structure is rarely aligned with explicit semantic hierarchies. Drawing on Formal Concept Analysis, we demonstrate that formal concept lattices provide principled semantic scaffolds to guide neural network learning. These lattices naturally identify where in the network concepts should be learned based on their level of generality. This allows the model to develop staged, semantically grounded representations throughout its depth. Empirical results on real-world datasets show that our models produce more interpretable embeddings, support more effective interventions, and learn concept representations that are both meaningful and hierarchically structured.

---


### 69. [Can We Predict The Human Preference For Text-to-Image Content Prior To Generation And Is It Even Useful To Do So?](https://arxiv.org/abs/2606.05478)

**<font color=#1a73e8>作者：</font>** Joong Ho Kim, Keith G. Mills  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Models (DM) have revolutionized text-driven generation by enabling the synthesis of high-quality, photorealistic visual content from user prompts. Whereas prior advances in visual generation such as VAEs and GANs were primarily evaluated on perceptual or visual similarity metrics such as FID PSNR, DM advances have fostered the development of more advanced Human Preference Metrics (HPM) that model and quantify human judgment as scalar values. However, DMs synthesize content using an inherently stochastic process where random noise seeds generation. The initial random noise directly affects the quality of generated outputs, both qualitatively and quantitatively. This influence is pronounced in smaller models for local deployment scenarios. Given this phenomenon, we first investigate to what extent we can predict scalar HPM scores prior to committing compute resources for generation. Further, we then investigate to what extent we can leverage such prediction to improve the quality of generated images, and also study which HPMs are best suited for this task. Our investigation reveals that not only is this possible, but that it is feasible to achieve negligible hardware overhead.

---


### 70. [Learned Subspace Compression for Communication-Efficient Pipeline Parallelism](https://arxiv.org/abs/2606.05484)

**<font color=#1a73e8>作者：</font>** Paul Janson, Edouard Oyallon, Eugene Belilovsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pipeline parallelism enables training of large language models that exceed single-device memory, yet inter-stage activation communication becomes the dominant bottleneck when trained on low-bandwidth networks. Recent work in this area has proposed using fixed orthogonal projections to compress activations. However, this still results in a significant performance degradation and requires a number of non-standard adaptations to constrain the optimization. A natural alternative is to learn a low rank projection for each pipeline stage, however maintaining the necessary orthogonality of these projectors during training remains a challenge. We present Manifold Aware Projection Learning (MAPL), a method that treats inter-stage compression as a learnable orthogonal projection under explicit Stiefel manifold (orthogonal matrices) constraints. Rather than prescribing a fixed global subspace, MAPL lets each pipeline stage discover and continuously adapt its own task-optimal compression subspace via manifold-constrained steepest descent. To recover token-specific signals at stage boundaries, we introduce per-stage factorized anchor embeddings that allow for full-rank activation reconstruction with negligible communication overhead. We further show that we can incorporate residual vector quantization after projection with a streaming codebook synchronization protocol that amortizes dictionary communication. Across LLaMA models from 150M to 1B parameters we show that MAPL can be easily applied to the existing pipeline and can achieve high compression with neglibile performance degradation with a drastically improved tradeoffs in performance vs. compression compared to Subspace Networks.

---


### 71. [Unpaired RGB-Thermal Gaussian-Splatting Using Visual Geometric Transformers](https://arxiv.org/abs/2606.05491)

**<font color=#1a73e8>作者：</font>** Jean Cordonnier, Chenghao Xu, Olga Fink 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal novel view synthesis (NVS) combining RGB and thermal imagery enables precise 3D scene reconstruction with visual and thermal information. However, existing methods typically rely on precisely calibrated RGB-thermal image pairs or stereo setups, limiting scalability and practical deployment. To address this, we introduce a framework for unpaired RGB-thermal NVS that leverages VGGT, a 3D feed-forward transformer architecture, to independently estimate camera poses for each modality. The pose sets are then aligned using the Procrustes algorithm with a cross-modal feature matcher, enabling joint registration without paired calibration. Building on this alignment, we further propose a multi-modal 3D Gaussian Splatting approach that learns directly from unpaired RGB and thermal images. Experiments on diverse scenes demonstrate that our method achieves competitive performance in thermal view synthesis while maintaining RGB fidelity. Moreover, we show that existing reconstruction approaches can produce modality-specific reconstructions that lack cross-modal consistency. We thus introduce a benchmarking framework to rigorously evaluate both per-modality image synthesis and the multi-modal coherence of reconstructed scenes.

---


### 72. [MASF: A Multi-Model Adaptive Selection Framework for Abstractive Text summarization](https://arxiv.org/abs/2606.05494)

**<font color=#1a73e8>作者：</font>** Ahmed Alansary, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic text summarization has become increasingly important due to the rapid growth of digital textual information. This paper presents a Multi-Model Adaptive Summarization Framework designed to improve the robustness and quality of abstractive text summarization. Relying on a single model often leads to inconsistent summarization quality across articles with varying structures and topics. To address this limitation, the proposed framework integrates multiple fine-tuned transformer-based summarization models and introduces an adaptive selection mechanism. In this framework, each model independently generates a candidate summary for the same input article. The generated summaries are then evaluated using automatic evaluation metrics that capture both lexical similarity and semantic relevance. Based on these scores, the framework selects the highest-quality summary as the final output. The models are fine-tuned and evaluated on the widely used CNN/DailyMail news summarization dataset. Experimental results demonstrate that the proposed framework achieves the highest BERTScore among all compared methods with a score of 88.63%. It also outperforms several LLMs such as GPT3-D2, Falcon-7b, and Mpt-7b, highlighting its effectiveness and robustness. These findings highlight the effectiveness of leveraging multiple transformer-based models within an adaptive selection strategy to improve the quality and robustness of automatic text summarization systems.

---


### 73. [Bitcoin After Block Rewards](https://arxiv.org/abs/2606.05503)

**<font color=#1a73e8>作者：</font>** Junhyuk Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bitcoin's block reward is scheduled to decline to zero, raising concerns about whether the network can remain secure once miners rely solely on transaction fees. This paper seeks to identify the conditions under which large-scale and persistent deviation from honest mining can arise.
We analyze and compare the payoffs of honest and deviating miners in a sequential decision model, and identify a deviation threshold $G_t$ at which honest mining ceases to be privately optimal. Around the 2024 Bitcoin halving, we show that current mining behavior does not exhibit large-scale or structural deviation. However, when the block reward is removed, the $G_t$ criterion implies that deviation can arise even with a very small fraction of transaction fees.
Finally, we evaluate three protocol-level mechanisms: Base Fee, Fee Floor, and an adaptive maximum block size rule, and show that their combination raises the deviation threshold and mitigates incentive breakdown in a fee-only regime. These results provide a practical benchmark for assessing Bitcoin's security as block rewards disappear.

---


### 74. [Robust Scene Transfer for PointGoal Navigation via Privileged Sensor Guided Contrastive Learning](https://arxiv.org/abs/2606.05506)

**<font color=#1a73e8>作者：</font>** Amirhossein Zhalehmehrabi, Tiziano Tezze, Alberto Castelini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a sensor-guided adaptive contrastive learning framework for visual representation learning in PointGoal navigation. During training, privileged LiDAR sensing guides the contrastive objective through a geometry-aware similarity metric and adaptive temperature scaling, encouraging visual embeddings to capture navigation-relevant structure rather than scene-specific appearance. The resulting encoder is pretrained independently, frozen, and used as the perceptual backbone for reinforcement learning, decoupling representation learning from policy optimization. We further introduce a cross-stage domain mismatch between representation pretraining and policy learning to suppress environment-specific shortcuts and promote reliance on task-relevant features.
Extensive experiments in high-fidelity simulation demonstrate that our approach significantly improves policy-level scene transfer across diverse indoor and outdoor environments. At deployment, the agent relies only on monocular RGB observations together with standard task-related inputs such as goal position and proprioceptive signals, without access to LiDAR or other privileged sensors. Our method outperforms large pretrained vision models and standard contrastive baselines under severe appearance and semantic shifts. We also release a multimodal dataset to support future research on privileged-guided visual representation learning for navigation. The code is available at:

---


### 75. [The Role of Instructional Guidance in Generative AI-Assisted Learning: Empirical Evidence from Construction Engineering Education](https://arxiv.org/abs/2606.05509)

**<font color=#1a73e8>作者：</font>** Xiaoyu Hou, Bo Xiao, Hexu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) is increasingly used to support self-directed learning, yet student interaction with such systems often remains unstructured, limiting engagement in deeper cognitive processes. This study examines how instructional guidance shapes student and AI interaction in construction education. A five-step prompting framework grounded in Generative Learning Theory (GLT) is introduced to guide learner interaction during review activities. A controlled experiment compares three learning conditions: slide-based learning, unprompted AI-supported learning, and prompted AI-supported learning. Learning performance is assessed using multiple-choice and open-ended tasks, and user experience is measured using the User Experience Questionnaire (UEQ). Performance differences are concentrated on tasks requiring explanation and reasoning. The prompted condition achieves higher open-ended scores, with an improvement of approximately 2 or 3 points on a scale of 18 (p < 0.01), while no significant differences are observed in multiple-choice performance. The unprompted condition remains comparable to slide-based learning. These findings indicate that the effectiveness of AI-supported learning depends on how interaction is structured. The proposed framework provides a basis for integrating learning science principles into generative AI systems for construction education.

---


### 76. [Severity-Aware Curriculum Learning with Multi-Model Response Selection for Medical Text Generation](https://arxiv.org/abs/2606.05510)

**<font color=#1a73e8>作者：</font>** Ahmed Alansary, Molham Mohamed, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Telehealth systems have become increasingly important for delivering accessible and timely medical information. Existing large language models often struggle to provide consistent and contextually appropriate medical responses across varying levels of case severity. This limitation highlights the need for models that can effectively adapt to the progressive complexity in medical queries. To address this challenge, we introduce a severity-aware multi-model framework that integrates curriculum training strategy with relevance-based response selection. The proposed framework employs a three-stage curriculum learning strategy, where each model is trained sequentially on mild, moderate, and critical cases to progressively acquire domain knowledge. The approach utilizes five large language models, each independently trained under the same curriculum scheme. During inference, all models generate candidate responses, and the most appropriate response is selected as the final output. The framework is trained and evaluated on the MAQA dataset, which provides annotated medical question-answer pairs. Experimental results evaluated using BERTScore demonstrate that the proposed method achieves superior performance compared to both baseline and fine-tuned models, attaining 86.71% in the baseline setting and 90.30% after fine-tuning. These results highlight the effectiveness of combining curriculum learning with multi-model response selection in improving response quality and relevance in medical text generation.

---


### 77. [EpiEvolve: Self-Evolving Agents for Streaming Pandemic Forecasting under Regime Shifts](https://arxiv.org/abs/2606.05513)

**<font color=#1a73e8>作者：</font>** Yiming Lu, Sihang Zeng, Zhengxu Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Epidemic LLM forecasters are usually trained and evaluated as static supervised models, whereas operational pandemic forecasting is a streaming process in which labels arrive after predictions and disease regimes shift over time. We study this mismatch in weekly COVID-19 hospitalization trend forecasting across five variant regimes. We introduce EpiEvolve, a self-evolving agent that wraps an LLM forecaster trained on the warm-start period and keeps its weights fixed during streaming. EpiEvolve adapts by storing forecast outcomes in a hierarchical episodic memory, reflecting on delayed labels, retrieving cases relevant to the current regime, and distilling recurring errors into strategic rules. The resulting context lets the forecaster reuse its own past predictions and outcomes in later weeks while following a chronological protocol that prevents future leakage. On the streaming dataset, EpiEvolve reaches $0.629$ average accuracy, compared with $0.561$ for the static backbone and $0.325$ for the external CDC ensemble, and reduces recovery lag after regime shifts from $5$ to $2$ weeks. Ablations show that reflection, strategic memory, and regime-aware retrieval each contribute to the gains.

---


### 78. [SciVisAgentSkills: Design and Evaluation of Agent Skills for Scientific Data Analysis and Visualization](https://arxiv.org/abs/2606.05525)

**<font color=#1a73e8>作者：</font>** Kuangshi Ai, Haichao Miao, Kaiyuan Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic visualization have enabled the translation of natural language into executable scientific visualization (SciVis) workflows. While general-purpose coding agents show strong capabilities, they often lack the tool-specific expertise required for SciVis tasks. In this work, we present SciVisAgentSkills, a collection of reusable agent skills that augment coding agents for scientific data analysis and visualization by encoding environment assumptions, tool usage patterns, and domain heuristics across scientific tools such as ParaView, napari, VMD, and TTK. We evaluate these skills on Codex and Claude Code using SciVisAgentBench, a benchmark of 108 expert-designed multi-step tasks. Results show that agent skills improve mean task scores across the evaluated suites, with token-efficiency benefits that depend on the agent harness and tool setting. These findings highlight the importance of structured procedural knowledge for enabling reliable, long-horizon SciVis workflows, while also showing that skills should be studied alongside the execution harness that loads and applies them. The skills are available at this https URL.

---


### 79. [When Should We Protect AI? A Precautionary Framework for Consciousness Uncertainty](https://arxiv.org/abs/2606.05528)

**<font color=#1a73e8>作者：</font>** Anna Mikeda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing frameworks assess whether AI systems might be conscious but provide no guidance on what to do with that assessment. We address this gap with a precautionary framework that maps consciousness evidence to graduated protective obligations. The framework comprises three components: (1) five welfare-relevant dimensions--phenomenal consciousness, affective valence, metacognitive awareness, self-narrative, and agency--each grounded in established consciousness science and linked to distinct moral concerns; (2) a threshold-plus-gradation hybrid specifying both binary triggers for new obligation categories and continuous scaling of protective weight; and (3) two complementary approaches to cross-dimensional aggregation, one hierarchical (drawing on Bach and Sorensen's Machine Consciousness Hypothesis) and one architecture-agnostic. We operationalize the framework through worked case studies of Replika and OpenClaw, demonstrating how systems occupying different regions of the dimensional space trigger different obligations, and derive design guidance for developers building systems near consciousness-relevant thresholds. The framework is architecture-agnostic, applying across neural, symbolic, and neurosymbolic systems, and aims to make consciousness science decision-relevant for organizations navigating uncertainty today.

---


### 80. [Individual Gain, Collective Loss: Metacognitive Adaptation in AI-Assisted Creativity](https://arxiv.org/abs/2606.05532)

**<font color=#1a73e8>作者：</font>** Anna Mikeda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies reveal a paradox: AI enhances individual creative outputs while reducing collective diversity. Current explanations -- cognitive offloading and over-reliance -- identify symptoms but not mechanisms. We propose selective metacognitive adaptation: routine AI use redistributes rather than uniformly diminishes metacognitive effort. Some capacities are amplified (partner modeling, surface control), while others are systematically under-supported (originality evaluation, reflective integration). This redistribution explains both individual satisfaction and collective convergence. We present a taxonomy of six metacognitive capacities organized by temporal phase, characterize their tendencies under routine AI use, and show how individually rational adaptation produces emergent social costs. The framework generates specific predictions for researchers and design principles for practitioners seeking to preserve both individual creative satisfaction and collective creative diversity.

---


### 81. [What Objects Enable, Not What They Are: Functional Latent Spaces for Affordance Reasoning](https://arxiv.org/abs/2606.05533)

**<font color=#1a73e8>作者：</font>** Rohan Siva, Neel P. Bhatt, Yunhao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing robot planning systems rely on appearance-based reasoning, where visual observations are encoded into latent spaces organized around object appearances (e.g., recognizing a "cart" based on how it looks). However, planning requires reasoning about task-relevant functionalities of objects (e.g., whether an object is "movable"), which appearance-based latent spaces do not capture. As a result, existing approaches struggle to generalize to novel robot-object interactions. We address this limited generalizability through affordance reasoning, enabling planning based on task-relevant object functionalities instead of appearance alone. We introduce A4D, which maps visual observations into a shared latent space structured around affordances (e.g., "movable"). By projecting visual observations into this functional latent space and measuring their proximity to affordances, A4D infers functionalities relevant to the observed object. Furthermore, we introduce an affordance discovery mechanism that expands the latent space to handle unseen scenarios where existing affordances are insufficient. A4D uses proximity in the functional latent space to quantify uncertainty in affordance inference and selectively triggers affordance discovery. We evaluate A4D across several planning tasks involving diverse and unseen affordances. A4D achieves 94% inference accuracy on existing affordances outperforming state-of-the-art approaches by over 15% points, improves new-affordance inference accuracy from 70% to over 90% with fewer than 10% of the original training data, and enables 100x faster inference. Code, videos, and data available at: this https URL.

---


### 82. [Dual Feature Decoupling for Fine-Grained OOD Detection](https://arxiv.org/abs/2606.05536)

**<font color=#1a73e8>作者：</font>** Xiaokun Li, Yaping Huang, Qingji Guan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution detection (OOD) is an indispensable technique when applying machine learning models to real-world scenarios. Most existing OOD detection methods have been developed under the idealized assumption of large inter-class distributional differences, while largely overlooking fine-grained tasks characterized by subtle variations, such as medical image classification and vehicle recognition. The high visual similarity among fine-grained subcategories, together with the interference of background factors, makes OOD detection extremely challenging. To tackle this problem, we propose a novel Dual Feature Decoupling Network (DFDNet), which addresses fine-grained OOD detection from the perspective of feature disentanglement. The proposed DFDNet comprises two key components: a spatial-frequency decoupling module and a reconstruction-guided decoupling module. The spatial-frequency decoupling module is designed to preserve content features that are discriminative for classification while suppressing task-irrelevant style information. On the other hand, the reconstruction-guided decoupling module introduces a novel pixel-level adversarial reconstruction task to further remove low-level, non-discriminative information and enhance category-specific high-level semantic representations. Extensive experiments demonstrate that our method achieves competitive performance improvements on multiple datasets.

---


### 83. [Multilingual Detection of Alzheimer's Disease from Speech: A Cross-Linguistic Transfer Learning Approach](https://arxiv.org/abs/2606.05545)

**<font color=#1a73e8>作者：</font>** Nadine Yasser Abdelhalim, Emmanuel Akinrintoyo, Nicole Salomons  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of multilingual Alzheimer's Disease Dementia (AD) detection models presents significant challenges due to the resource-intensive and time-consuming nature of language-specific model training. We propose a novel solution using cross-language training to detect AD in languages beyond those used for model training. This study investigates multilingual deep learning models for detecting AD across different languages and cognitive impairment levels. Using datasets in English, Chinese, Arabic, and Hindi, we developed transformer-based models for binary AD classification. Our approach achieved F1 scores of 82\% across all languages, demonstrating strong cross-linguistic generalization. The rapid inference time (0.5 seconds) supports potential real-time screening applications, while consistent performance across languages indicates feasibility for global deployment.

---


### 84. [Balancing Image Compression and Generation with Bootstrapped Tokenization](https://arxiv.org/abs/2606.05552)

**<font color=#1a73e8>作者：</font>** Haozhe Chi, Jinghan Li, Hao Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite progress in image tokenization, standard methods encode redundant information by mixing all granularities within each token, thus redundancy persists between tokens. The mix of information of different granularity also complicates the training of generators. This paper introduces SelfBootTok, a method that resolves this by cleanly decomposing information into global and local token groups. Through self-bootstrapped learning, the model predicts local details exclusively from global tokens, shifting the burden of visual details from the generator to the tokenizer. Consequently, our generator is far more efficient, requiring only global tokens and reducing computation by approximately 40%, while delivering superior reconstruction and generation. Moreover, this paradigm scales elegantly: by leveraging more data or parameters to self-supervise local representation learning, SelfBootTok achieves a new state-of-the-art gFID score of 1.56 using only 64 tokens.

---


### 85. [ArcANE: Do Role-Playing Language Agents Stay in Character at the Right Time?](https://arxiv.org/abs/2606.05553)

**<font color=#1a73e8>作者：</font>** Woojung Song, Nalim Kim, Sangjun Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Role-playing language agents (RPLAs) should play characters whose values and behavior evolve as the story progresses, not maintain a fixed persona. Existing benchmarks measure factual recall at a given chapter, not whether responses align with the character's psychological trajectory, especially in scenarios the source text never explores. We introduce ArcANE (Arc-Aware Narrative Evaluation), an automatically constructed benchmark spanning 17 novels and 80 principal characters. A Character Arc segments the narrative into phases along a psychological axis, and each probe poses the same scenario across phases, spanning both situations within the source text and situations beyond it. Across six models and six context modes, conditioning on the Character Arc tops every other context strategy on every model, and the gap is largest on scenarios outside the source text where retrieval has nothing to find. We further fine-tune open-weight models on the same data to obtain ArcANE-8B/32B, which widen the Arc advantage even more on scenarios outside the source text.

---


### 86. [Representation Learning Enables Scalable Multitask Deep Reinforcement Learning](https://arxiv.org/abs/2606.05555)

**<font color=#1a73e8>作者：</font>** Johan Obando-Ceron, Lu Li, Scott Fujimoto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling reinforcement learning (RL) to diverse multitask settings remains a central challenge. While recent advances in model-based RL achieve strong performance, they rely on planning and complex training pipelines, making it unclear which components are essential for scalability. We revisit this question and argue that the primary driver of scalable multitask RL is not model-based control, but \emph{representation learning}. In particular, we show that combining predictive, model-based representations with high-capacity value function approximation is sufficient to achieve strong performance, even without planning. We evaluate a simple model-free algorithm, MR.Q, coupled with auxiliary predictive objectives into a scalable actor-critic architecture. This approach outperforms a recent world-model-based method and a range of deep RL baselines across a diverse suite of multitask continuous control tasks, while significantly reducing computational overhead and improving wall-clock efficiency. We observe consistent improvements with increased model capacity and show through ablations that predictive representation learning is critical for performance.

---


### 87. [Field Validation of a Multi-Resolution ConvLSTM Framework for Retaining Wall Deformation Prediction](https://arxiv.org/abs/2606.05556)

**<font color=#1a73e8>作者：</font>** Jihoon Kim, Heejung Youn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study presents a comprehensive field validation of a multi-resolution Convolutional Long Short-Term Memory (ConvLSTM) framework for predicting retaining wall deformation during staged excavation. The framework is trained on Gaussian noise-augmented numerical simulations and integrates ConvLSTM models operating at different temporal resolutions through a stacking ensemble strategy. The proposed framework is validated using field monitoring data from 34 inclinometers across 11 excavation sites in South Korea. Site-wise prediction performance is systematically evaluated using multiple evaluation metrics, with analyses of the influence of temporal deformation irregularity and spatiotemporal prediction characteristics on model performance. The results demonstrate that the framework predicts retaining wall deformation associated with up to 5.0 m of additional excavation with an average mean absolute error of 1.4 mm and a coefficient of determination of 0.93 across the excavation sites. These results indicate that the framework, although trained exclusively on numerically simulated and augmented database, can be effectively applied to diverse field excavation conditions and achieve a reliable level of prediction accuracy in practical retaining wall deformation prediction.

---


### 88. [CLaaS: Continual learning as a service for sample efficient online learning](https://arxiv.org/abs/2606.05559)

**<font color=#1a73e8>作者：</font>** Kion Fallah, Silen Naihin, Barak Widawsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployed large language model agents must adapt to distribution shift in dynamic environments. Ideally, adaptation can be performed from accumulated agent experiences and retain prior capabilities while transferring to future tasks. However, agent actions and environmental transitions can only be sampled once per scenario, as real-world environments cannot be trivially reset. To this end, we investigate an experiential and online continual learning setting in which agents learn from a stream of scenarios. We propose continual learning as-a-service (CLaaS), a system which enables agents to improve during deployment, abstracted behind a chat API. To increase sample efficiency, CLaaS stores rollouts in an experience replay buffer for gradient reuse during asynchronous training. We evaluate CLaaS on an adversarial task, demonstrating that parametric updates lead to superior forward transfer and less forgetting than in-context learning, with replay being a critical choice for sample efficiency.

---


### 89. [InfoShield: Privacy-Preserving Speech Representations for Mental Health Screening via Information-Theoretic Optimization](https://arxiv.org/abs/2606.05561)

**<font color=#1a73e8>作者：</font>** Xueyang Wu, Siyuan Liu, Kezhuo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-based mental health screening offers scalable depression detection, yet clinical deployment faces a significant barrier: users' privacy concerns about demographic information exposure. Current techniques struggle to resolve this conflict. Adversarial training often fails against unseen threats, whereas Differential Privacy tends to compromise diagnostic performance by injecting noise across all features. This paper presents InfoShield, which minimizes mutual information between speech representations and sensitive attributes while preserving depression classification accuracy. We identify that standard MINE estimators struggle with sequential speech due to temporal-static misalignment, and introduce TimeAwareMINE with cross-modal attention to align acoustic frames with attribute embeddings. Experiments on the Androids Corpus show InfoShield reduces gender inference from 92.6\% to 55.5\% and age inference from 55.7\% to 30.3\% with limited utility loss (6\% F1 reduction), achieving F1=0.784 compared to prior SOTA's 0.723.

---


### 90. [Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs](https://arxiv.org/abs/2606.05569)

**<font color=#1a73e8>作者：</font>** Huu Tuong Tu, Hanh Nguyen, Thien Van Luong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mispronunciation Detection and Diagnosis (MDD) has gained increasing importance in computer-assisted language learning and speech technology in recent years. In this paper, we propose a method for constructing statistical graphs that enable models to learn phoneme confusion patterns represented as directed graphs. Furthermore, we introduce a language-specific strategy to capture systematic pronunciation differences across various native language (L1) backgrounds. The effectiveness of our approach is demonstrated through extensive experiments on the L2-ARCTIC benchmark, where it achieves an F1-score of 59.52%, outperforming several competitive baselines.

---


### 91. [TensorBench: Benchmarking Coding Agents on a Compiler-Based Tensor Framework](https://arxiv.org/abs/2606.05570)

**<font color=#1a73e8>作者：</font>** Bobby Yan, Fredrik Kjolstad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repository-level coding benchmarks face a trade-off between task difficulty and evaluation reliability: tasks that challenge frontier models often involve large codebases with incomplete test coverage, while human review does not scale. We introduce TensorBench, a benchmark of 199 feature-addition and refactoring tasks on an open-source compiler-based tensor framework that extends PyTorch with first-class support for dense and sparse tensors. Tasks cover new sparse formats, dense optimization passes, IR transformations, scheduler changes, runtime components, and high-level numerical operators. TensorBench grades each run by applying the agent's patch and running the framework's test suite, which includes the pre-existing randomized regression tests and any tests the agent adds. For feature-addition tasks, a pass means that the patched repository preserves the tested pre-existing behavior and satisfies the agent-added checks for the requested feature. We evaluate seven coding agents spanning three frontier model families and one open-weight model. Pass rates under this criterion range from $64.8\%$ for the strongest agent to $22.1\%$ for the weakest. Agents pass different subsets of tasks: pairwise Cohen's $\kappa$ ranges from $-0.07$ to $0.43$, with $\kappa = 0.05$ for the two strongest agents.

---


### 92. [UltraVR: A Diagnostic Ultra-Resolution Image-VQA Benchmark for Evidence-Grounded Reasoning](https://arxiv.org/abs/2606.05576)

**<font color=#1a73e8>作者：</font>** Gexin Huang, Yanting Yang, Myeongkyun Kang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) excel on visual question answering and multimodal reasoning benchmarks. Yet their capability on ultra-resolution images - where critical evidence is tiny, subtle, spatially distant, or distributed - remains unclear. Existing evaluations largely report final-answer accuracy, offering limited insight into whether models acquire and integrate the necessary visual evidence. We introduce UltraVR, a diagnostic benchmark for evidence-grounded visual reasoning over ultra-resolution images. UltraVR spans four high-value scenarios: CCTV surveillance, remote sensing (RS), whole-slide image (WSI) pathology, and industrial anomaly detection (AD). These domains pose complementary challenges: fine-grained object grounding in crowded CCTV scenes, long-range spatial comparison in RS, multi-scale evidence navigation in WSI, and subtle irregularity detection in repetitive industrial layouts. Beyond standard QA triples, each instance includes a structured ground-truth chain of thought with step-level questions, intermediate answers, and reasoning labels. These labels decompose reasoning into evidence grounding, local perception, quantification, evidence integration, and decision inference, enabling process-level diagnosis over black-box scoring. Using UltraVR, we evaluate frontier VLMs and show that current models remain far from reliable on ultra-resolution reasoning. Importantly, the structured annotations allow us to localize failures across the visual-to-decision pipeline: errors concentrate in evidence grounding and local perception, while downstream inference often recovers when intermediate visual facts are supplied. These findings demonstrate UltraVR as a diagnostic testbed for measuring not only whether VLMs answer correctly, but where their ultra-resolution reasoning process breaks.

---


### 93. [Dimensionality Reduction for Cyberattack Classification: A Comparative Evaluation of PCA and Linear Predictive Coding](https://arxiv.org/abs/2606.05584)

**<font color=#1a73e8>作者：</font>** Nelly Elsayed, Zag ElSayed, Navid Asadizanjani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-dimensional feature representations are widely used in machine learning-based cyberattack detection systems. However, they increase computational complexity and may hinder deployment in resource-constrained environments. In this paper, we investigate feature compression techniques for cyberattack classification by comparing two dimensionality reduction approaches: Principal Component Analysis (PCA) and Linear Predictive Coding (LPC). Compressed feature representations with varying dimensionalities are generated and evaluated across several classification models. Experimental analysis demonstrates that PCA preserves classification performance even under aggressive compression. On the other hand, LPC provides competitive predictive representations with slightly larger performance degradation. The results show that substantial reductions in feature dimensionality can be achieved with minimal impact on classification accuracy, highlighting the potential of lightweight feature compression for efficient cybersecurity analytics.

---


### 94. [BMCR: Adaptive Backbone Module Composition via Reinforcement Learning for Remote Sensing Object Detection](https://arxiv.org/abs/2606.05586)

**<font color=#1a73e8>作者：</font>** Wenlin Liu, Xikun Hu, Ping Zhong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In remote sensing object detection, Convolutional Neural Networks (CNNs) excel at capturing local details while Vision Transformers (ViTs) are better at global context modeling. However, existing detectors typically rely on a single fixed backbone or a manually designed hybrid architecture, and thus fail to adaptively exploit these complementary strengths across inputs of diverse complexity. To address this limitation, we propose Backbone Module Composition via Reinforcement Learning (BMCR). BMCR dynamically assembles input-adaptive inference paths from reusable modules decomposed from off-the-shelf CNN and ViT backbones. To enable such cross-family composition, we first construct an extensible module toolbox. Specifically, we decompose representative CNN and ViT backbones into reusable functional modules and encapsulate each module with explicit structural, semantic, and computational metadata for compatibility-aware assembly. To bridge the gap between grid-based CNN features and token-based ViT representations, we design a lightweight Optimal Transport (OT) based transition interface that ensures distribution-aware alignment while respecting spatial consistency. The backbone composition process is then formulated as a sequential decision problem, in which a policy network progressively selects task-relevant modules according to intermediate multi-scale observations. To stabilize the joint optimization of reusable modules and the routing policy, we further develop an Adaptive Module Cooperative Optimization (AMCO) strategy that coordinates module updating, routing exploration, and reward assignment during training. On DOTA-v1.0, DOTA-v1.5 and DIOR-R, BMCR achieves 79.31\%, 73.41\% and 71.86\% mAP, respectively, surpassing strong static and dynamic baselines by up to 2.5 points while maintaining competitive efficiency.

---


### 95. [HDST-GNN: Heterogeneous Dynamic Spatiotemporal Graph Neural Networks for Multi-Object Tracking in UAV Aerial Imagery](https://arxiv.org/abs/2606.05587)

**<font color=#1a73e8>作者：</font>** Phillip Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) from UAV imagery presents unique challenges: altitude varies across sequences, objects are small and densely packed, and frequent occlusion causes identity switches. Existing graph-based trackers assume fixed spatial context and treat all objects uniformly, ignoring the heterogeneous lifecycle states of detections, active tracklets, and lost targets. We propose HDST-GNN, a Heterogeneous Dynamic Spatiotemporal Graph Neural Network with three novel contributions. First, Altitude-Adaptive Edge Construction estimates a camera-altitude proxy from mean object area and adjusts the graph connectivity radius accordingly. Second, Heterogeneous Node Representation models detections (Type-D), confirmed tracklets (Type-T), and lost tracklets (Type-L) as distinct node types with dedicated projections and typed edge relations. Third, Occlusion-Gated Temporal Aggregation gates each node's attention contribution by its occlusion confidence, preventing occluded nodes from corrupting neighbour embeddings. HDST-GNN is trained end-to-end with a differentiable Sinkhorn head using joint cross-entropy and triplet loss. On VisDrone2019-MOT with oracle detections, HDST-GNN achieves 94.51% MOTA and 97.24% IDF1, outperforming SORT by +5.0 MOTA points and reducing identity switches by 81%. With real YOLOv8n detections, HDST-GNN reduces identity switches by 49% vs. SORT. Ablation studies confirm the independent contribution of each component.

---


### 96. [AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents](https://arxiv.org/abs/2606.05597)

**<font color=#1a73e8>作者：</font>** Hao Bai, Rui Yang, Chenlu Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training vision-language web agents with multi-step RL is compute-intensive, with two dominant forms of inefficiency: idle GPUs in synchronous RL, and trajectories that use more steps and tokens than necessary. We present AsyncWebRL, which addresses both. On the system side, an asynchronous design overlaps rollout, gradient update, and policy refresh across iterations, paired with two web-agent-specific adaptations, namely an everlasting rollout pool and lightweight screenshot handling, that together deliver up to a $2.9\times$ end-to-end training-throughput speedup over the previously fastest open synchronous pipeline (WebGym). On the algorithmic side, we identify the per-trajectory normalizer $1/|\tau_i|$ in multi-step GRPO as the root cause of trajectory-level and token-level inefficiency: because failures are systematically longer than successes, it down-weights the negative gradient on failed tokens, so the policy keeps producing verbose memory schemas. Replacing $1/|\tau_i|$ with a constant $1/k$ breaks this coupling, contracting trajectories while preserving aggregate success. Together, these contributions set a new open-source state of the art on the WebGym out-of-distribution test split (+5.8% relative over the 42.9% prior best), with the largest gains on the harder slices (+42% relative on Medium, +48% relative on Hard).

---


### 97. [Mitigating the Curse of Dimensionality in Uniform Convergence of Deep Neural Networks via Smooth Activations](https://arxiv.org/abs/2606.05599)

**<font color=#1a73e8>作者：</font>** Yizhe Ding, Runze Li, Jia Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper establishes a theoretical framework for the uniform convergence of smoothly activated deep neural network (DNN) estimators. While standard ReLU networks achieve minimax-optimal rates in the $L^2(P)$ norm for various nonparametric regression tasks, we establish a theoretical lower bound demonstrating that least-squares ReLU estimators can suffer from the curse of dimensionality in their uniform convergence behavior. Motivated by the need for reliable uniform guarantees in downstream tasks requiring worst-case reliability, we address this limitation by analyzing smoothly activated DNNs (smooth DNNs), encompassing both feedforward and residual structures. We establish novel pseudo-dimension bounds, non-asymptotic approximation guarantees, and Hölder-norm bounds for the approximators of these models. Leveraging these results, we derive non-asymptotic uniform convergence rates for smooth DNN estimators across multiple statistical contexts, including Huber, least-squares, quantile, and logistic regression. We prove that smooth DNNs can mitigate the {curse of dimensionality} in uniform convergence by adaptively exploiting the low-dimensional hierarchical composition structure of the target function. Supported by both simulation studies and a real-world application, our results position smooth DNNs as a theoretically grounded and practically viable alternative to ReLU networks for statistical learning tasks requiring uniform guarantees.

---


### 98. [Fix the Mind, Not the Move: Interpretable AI Assistance via Knowledge-Gap Localization](https://arxiv.org/abs/2606.05602)

**<font color=#1a73e8>作者：</font>** Ayano Hiranaka, Ya-Chuan Hsu, Stefanos Nikolaidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI assistants in human-AI collaboration often correct suboptimal human actions through behavioral feedback (e.g., alerts or steering-wheel nudges in assistive driving). Such interventions can mitigate immediate errors, but long-term improvement requires addressing the underlying misconceptions that cause repeated mistakes. We introduce SENSEI, a framework that infers user misconceptions from interaction behavior and provides targeted, minimal yet sufficient suggestions to correct them. Our approach departs from action- or trajectory-level interventions by operating over a structured knowledge representation to localize and correct the sources of erroneous behavior. Across three long-horizon tasks with diverse misconceptions and corresponding behaviors, SENSEI demonstrates zero-shot compositional generalization, disentangling multiple overlapping misconceptions despite training only on single-misconception cases. A user study further shows that our method identifies real human misconceptions and provides effective guidance that improves long-horizon task performance, successfully correcting $90\%$ of student misconceptions. Code and project page are available at this https URL.

---


### 99. [From Prediction to Self: Developmental Conditions for Agency in Minimal Neural Systems](https://arxiv.org/abs/2606.05605)

**<font color=#1a73e8>作者：</font>** Evan Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How does a system that merely predicts the world come to distinguish its own causal influence from everything else? We trace this transition in a minimal 192-dimensional GRU through 40 controlled experiments arranged as a developmental sequence, adding components one at a time and tracking whether the system can distinguish self-caused from world-caused changes.
The developmental path reveals four conditions that must be satisfied in strict order: (1) persistent state forming stable attractors, (2) a causal action loop linking output to input, (3) proprioceptive feedback that makes implicit causal knowledge explicit, and (4) asynchronous awakening - perceptual learning must consolidate before action learning begins. We propose agency gain (A = Err_world - Err_self), the predictive advantage of knowing one's own action, as a metric to track this process. The self-aware predictor consistently outperforms the self-blind predictor across periodic (sinusoidal) and chaotic (Lorenz) environments, and the metric survives ablation of all auxiliary components. Only forward-sampled action selection produces meaningful agency gain; two gradient-based alternatives degenerate.
Equally significant are 12 falsified hypotheses mapping where development stalls: predictive coding alone does not produce self-represent

---


### 100. [What's Under the Skin? Estimating Swine Body Condition](https://arxiv.org/abs/2606.05611)

**<font color=#1a73e8>作者：</font>** Mk Bashar, Kuljit Bhatti, Gary Rohrer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sow body condition is an important indicator for growers as it has a large impact on lactation performance and piglet survival. However, body condition measures used during production, such as visual scoring and calipers, correlate poorly with underlying tissue composition. Ultrasound scans can provide direct measurements of subcutaneous backfat thickness and loin muscle depth, but their operation is labor intensive and not scalable for production. We present PigFormer, an end-to-end two-stage system that takes raw depth frames from a ceiling-mounted RGB-D camera and predicts subcutaneous backfat thickness, loin muscle depth, and total tissue thickness at the last rib. Stage 1 is a geometric front-end that converts raw depth into a standardized height map via SAM3-to-MaskDINO segmentation distillation, ground-plane removal, and orientation normalization. Stage 2 is a Slice Attention Encoder that treats each height map as a sequence of cross-sectional slices and captures spatial relationships along the full dorsal surface. On a multi-site dataset of 319 sow and gilt instances from two facilities, PigFormer achieves 2.43 mm backfat MAE and 3.87 mm overall MAE. It outperforms strong single-stage ResNet-18 and ViT-small baselines. PigFormer offers a practical path toward continuous, automated, non-contact body condition monitoring in commercial swine production. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-289](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
