# 📦 其他研究 | 2026年05月02日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-234](./part-05.md)

---

### 151. [Machine Unlearning for Class Removal through SISA-based Deep Neural Network Architectures](https://arxiv.org/abs/2604.27804)

**<font color=#1a73e8>作者：</font>** Ishrak Hamim Mahi, Siam Ferdous, Md Sakib Sadman Badhon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of image generation models and other artificial intelligence (AI) systems has intensified concerns regarding data privacy and user consent. As the availability of public datasets declines, major technology companies increasingly rely on proprietary or private user data for model training, raising ethical and legal challenges when users request the deletion of their data after it has influenced a trained model. Machine unlearning seeks to address this issue by enabling the removal of specific data from models without complete retraining. This study investigates a modified SISA (Sharded, Isolated, Sliced, and Aggregated) framework designed to achieve class-level unlearning in Convolutional Neural Network (CNN) architectures. The proposed framework incorporates a reinforced replay mechanism and a gating network to enhance selective forgetting efficiency. Experimental evaluations across multiple image datasets and CNN configurations demonstrate that the modified SISA approach enables effective class unlearning while preserving model performance and reducing retraining overhead. The findings highlight the potential of SISA-based unlearning for deployment in privacy-sensitive AI applications. The implementation is publicly available at this https URL sisa-class-unlearning.

---


### 152. [Focus Session: Autonomous Systems Dependability in the era of AI: Design Challenges in Safety, Security, Reliability and Certification](https://arxiv.org/abs/2604.27807)

**<font color=#1a73e8>作者：</font>** Behnaz Ranjbar, Kirankumar Raveendiran, Sudeep Pasricha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The design of embedded safety-critical systems such as those used in next-generation automotive and autonomous platforms, is increasingly challenged by escalating system complexity, hardware-software heterogeneity, and the integration of intelligent, data-driven components. Ensuring dependability in such systems requires a holistic approach that spans multiple abstraction layers and encompasses both design- and run-time assurance. Traditional methods for reliability, safety, and security management often fall short in addressing the dynamic and uncertain behaviors introduced by Artificial Intelligence (AI) and Machine Learning (ML) components, especially under stringent real-time, power, and safety constraints. While AI and ML offer powerful predictive, adaptive, and self-optimizing capabilities that can enhance system dependability, their inherent non-determinism, data-dependence, and lack of formal guarantees introduce new challenges for verification, validation, and certification. This paper explores emerging methodologies, architectures, and frameworks for designing dependable autonomous and embedded systems in the era of AI. It highlight advances in reliability modeling, secure system design, and certification approaches that account for imperfect, learning-enabled components, aiming to bridge the gap between AI innovation and certifiable system-level dependability.

---


### 153. [Hyper-Dimensional Fingerprints as Molecular Representations](https://arxiv.org/abs/2604.27810)

**<font color=#1a73e8>作者：</font>** Jonas Teufel, Luca Torresi, André Eberhard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational molecular representations underpin virtual screening, property prediction, and materials discovery. Conventional fingerprints are efficient and deterministic but lose structural information through hash-based compression, particularly at low dimensionalities. Learned representations from graph neural networks recover this expressiveness but require task-specific training and substantial computational resources. Here we introduce hyperdimensional fingerprints (HDF), which replace the learned transformations of message-passing neural networks with algebraic operations on high-dimensional vectors, producing deterministic molecular representations without any training. Across diverse property prediction benchmarks, HDF outperforms conventional fingerprints in the majority of tasks while exhibiting greater consistency across datasets and models. Crucially, HDF embeddings preserve molecular similarity faithfully: at 32 dimensions, distances in HDF space achieve a 0.9 Pearson correlation with graph edit distance, compared to 0.55 for Morgan fingerprints at equivalent size. This structural fidelity persists at low dimensions where hash-based methods degrade, allowing simple nearest-neighbor regression to remain predictive with as few as 64 components. We further demonstrate the practical impact in Bayesian molecular optimization, where HDF-based surrogate models achieve substantially improved sample efficiency in regimes where Morgan fingerprints perform comparably to random search. HDF thus provides a general-purpose, training-free alternative to conventional molecular fingerprints, suggesting that the information loss long accepted as inherent to fixed-length fingerprints is a limitation of the hash-based encoding scheme rather than the fingerprint paradigm itself.

---


### 154. ["It depends on where AI is used": Players' attitude patterns and evaluative logics toward different AI applications in digital games](https://arxiv.org/abs/2604.27812)

**<font color=#1a73e8>作者：</font>** Ting-Chen Hsu, Jiangxu Lin, Wenran Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI becomes increasingly embedded in digital games, players' attitudes de-pend not only on whether AI is used, but also on where and how it intervenes in gameplay. This study examines players' evaluative patterns toward eight AI application contexts, including intelligent NPCs, emergent narrative, dynamic balancing, recommendation systems, review and governance, art asset generation, co-creation gameplay, and gameplay evolution. Based on 1,856 valid open-ended responses from 310 questionnaires, we conducted thematic analysis to identify reasons for acceptance, rejection, and conditional acceptance. Results show that players welcomed AI when it enhanced immersion, personalization, novelty, efficiency, or convenience, but resisted it when it threatened creativity, emotional authenticity, autonomy, fairness, system stability, authorship, or accountability. We further identify six evaluative logics: experiential enrichment, instrumental efficiency, system reliability, agency and control, authorship and compliance, and human oversight. These preliminary findings highlight the context-sensitive nature of AI acceptance in digital games.

---


### 155. [Probabilistic Circuits for Irregular Multivariate Time Series Forecasting](https://arxiv.org/abs/2604.27814)

**<font color=#1a73e8>作者：</font>** Christian Klötergens, Vijaya Krishna Yalavarthi, Lars Schmidt-Thieme  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint probabilistic modeling is essential for forecasting irregular multivariate time series (IMTS) to accurately quantify uncertainty. Existing approaches often struggle to balance model expressivity with consistent marginalization, frequently leading to unreliable or contradictory forecasts. To address this, we propose CircuITS, a novel architecture for probabilistic IMTS forecasting based on probabilistic circuits. Our model is flexible in capturing intricate dependencies between time series channels while structurally guaranteeing valid joint distributions. Experiments on four real world datasets demonstrate that CircuITS achieves superior joint and marginal density estimation compared to state of the art baselines.

---


### 156. [MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents](https://arxiv.org/abs/2604.27819)

**<font color=#1a73e8>作者：</font>** Haonan Li, Tianjun Sun, Yongqing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-server MCP agents create an information-flow control problem: faithful tool composition can turn individually benign read/write permissions into cross-boundary credential propagation -- a structural side effect of workflow topology, not necessarily malicious model behavior. We present MCPHunt, to our knowledge the first controlled benchmark that isolates non-adversarial, verbatim credential propagation across multi-server MCP trust boundaries, with three methodological contributions: (1) canary-based taint tracking that reduces propagation detection to objective string matching; (2) an environment-controlled coverage design with risky, benign, and hard-negative conditions that validates pipeline soundness and controls for credential-format confounds; (3) CRS stratification that disentangles task-mandated propagation (faithful execution of verbatim-transfer instructions) from policy-violating propagation (credentials included despite the option to redact). Across 3,615 main-benchmark traces from 5 models spanning 147 tasks and 9 mechanism families, policy-violating propagation rates reach 11.5--41.3% across all models. This propagation is pathway-specific (25x cross-mechanism range) and concentrated in browser-mediated data flows; hard-negative controls provide evidence that production-format credentials are not necessary -- prompt-directed cross-boundary data flow is sufficient. A prompt-mitigation study across 3 models reduces policy-violating propagation by up to 97% while preserving 80.5% utility, but effectiveness varies with instruction-following capability -- suggesting that prompt-level defenses alone may not suffice. Code, traces, and labeling pipeline are released under MIT and CC BY 4.0.

---


### 157. [WOOTdroid: Whole-system Online On-device Tracing for Android](https://arxiv.org/abs/2604.27830)

**<font color=#1a73e8>作者：</font>** Simon Althaus, Nikolaos Alexopoulos, Max Mühlhäuser 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System auditing on Android faces two problems. First, existing syscall tracers lose events under load, silently overwriting entries faster than a user space reader can drain them. Second, security-relevant application behavior is mediated through Binder, Android's kernel IPC mechanism, and is therefore hidden from the syscall layer. The Binder parcels that the kernel does see carry no method names or typed arguments, a disconnect between low-level events and high-level behavior known as the semantic gap. Existing approaches address the semantic gap either by modifying the Android platform, making them difficult to adjust to OS updates, or by instrumenting the traced application in user space, which sophisticated adversaries can evade by bypassing the instrumented framework APIs.
We present WOOTdroid, a design and prototype for on-device tracing on stock Android that addresses both problems without OS modification or application instrumentation. WDSys, an eBPF port of eAudit-style syscall auditing, runs on current Android with at most 3.6% Geekbench overhead and traces 33% more syscalls than ftrace. WDBind captures Binder parcels in the kernel and decodes them out-of-process against a framework signature table extracted via Java reflection. We demonstrate WOOTdroid on Pixel 9 devices running Android 16 with an end-to-end case study reconstructing ten security-relevant Binder transactions.

---


### 158. [Multi-Level Narrative Evaluation Outperforms Lexical Features for Mental Health](https://arxiv.org/abs/2604.27846)

**<font color=#1a73e8>作者：</font>** Yuxi Ma, Jieming Cui, Muyang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How people narrate their experiences offers a window into how the mind organizes them. Computational approaches to therapeutic writing have evolved from lexical counting to neural methods, yet remain fragmented: dictionary tools miss discourse structure, while embeddings conflate local coherence with global organization. No existing framework maps these techniques onto the hierarchical processes through which narratives are constructed. Here we introduce a three-level framework - micro-level lexical features, meso-level semantic embeddings, and macro-level LLM narrative evaluation - and show, across 830 Chinese therapeutic texts spanning depression, anxiety, and trauma, that macro-level evaluation substantially outperforms lexical and embedding features for mental health prediction. This challenges the field's emphasis on word-counting: formal structural features (Labov's story grammar, RST coherence, propositional composition) demonstrate that narrative organization per se carries predictive signal, while clinically-grounded narrative dimensions capture how psychological states are expressed through discourse. Semantic embeddings add minimal independent value but yield incremental gains in multi-level classification. By grounding computational levels in discourse processing theory, this framework identifies macro-structural organization as the primary locus of clinical signal and generates testable hypotheses for intervention design and longitudinal research.

---


### 159. [A Grid-Aware Agent-Based Model for Analyzing Electric Vehicle Charging Systems](https://arxiv.org/abs/2604.27849)

**<font color=#1a73e8>作者：</font>** Khalil Al-Rahman Youssefi, Marija Gojkovic, Walter Stefanutti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a configurable, grid-aware Agent-Based Model (ABM) for the systematic analysis of electric vehicle (EV) charging systems under configurable infrastructure and operational conditions. The model integrates heterogeneous EV behavior, charging column constraints, and a shared Energy Sandbox that regulates aggregate power allocation, enabling the joint study of user-centric charging dynamics and facility-level power behavior. Implemented in Python using the SimPy discrete-event framework, the approach supports scalable, event-driven simulations across varying system sizes, charger compositions, and scheduling strategies. A representative workplace charging scenario is investigated to illustrate how infrastructure configuration and coordination mechanisms influence energy delivery performance, infrastructure utilization, and aggregate load characteristics. The results highlight the context-dependence of infrastructure suitability and demonstrate how charging strategies and charger types reshape both service-level outcomes and grid-facing behavior. The proposed ABM provides a flexible and extensible simulation environment for exploring technical, operational, and grid-aware aspects of EV charging ecosystems, and for serving as a methodological basis for subsequent studies on advanced coordination strategies beyond the specific scenario analyzed in this study.

---


### 160. [Reasoning over Object Descriptions Improves Coreference Resolution in Task-Based Dialogue Systems](https://arxiv.org/abs/2604.27850)

**<font color=#1a73e8>作者：</font>** Oier Ijurco, Oier Lopez de Lacalle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-based dialogue systems assist users in achieving specific goals, such as executing actions or retrieving information, through natural language interactions. Accurate coreference resolution is essential, as it involves identifying object references within the dialogue - a task that becomes increasingly challenging in visually grounded environments characterized by complex scenes and diverse object metadata. However, coreference resolution in task-based dialogue remains limited by poor generalization across domains and heavy reliance on supervised models that often overfit to dataset-specific artifacts. In this work, we propose a unimodal test-time reasoning approach that enables large language models (LLMs) to reason over detailed object metadata and dialogue history to improve coreference resolution. Empirical results on the SIMMC 2.1 dataset demonstrate that LLMs can generate step-by-step reasoning processes that effectively align dialogue context with objects present in the scene. Extensive experiments highlight the models' ability to link conversations and objects accurately. Moreover, we show that test-time reasoning under few-shot settings generalizes effectively to unseen scenarios and novel objects, outperforming encoder-based supervised methods in cross-domain evaluations. These findings underscore the critical role of structured metadata and careful prompt engineering in enhancing the robustness and generalization of task-oriented dialogue systems.

---


### 161. [KellyBench: A Benchmark for Long-Horizon Sequential Decision Making](https://arxiv.org/abs/2604.27865)

**<font color=#1a73e8>作者：</font>** Thomas Grady, Kip Parker, Iliyan Zarov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are saturating benchmarks for procedural tasks with narrow objectives. But they are increasingly being deployed in long-horizon, non-stationary environments with open-ended goals. In this paper we introduce KellyBench, an environment for evaluating sequential decision-making in sports betting markets. Agents are placed in a sequential simulation of the 2023-24 English Premier League season and tasked with maximising their long-term bankroll growth. They are given detailed historical data, including advanced statistics, lineups, and public odds. To succeed they must build machine learning models, identify edge in public markets, and adapt as the environment changes over time. We find that all frontier models evaluated lose money on average over the course of the season for five seeds. The best performing model achieves an average return of -8%, and many models experiencing ruin across seeds. To judge strategy sophistication, we use a human expert rubric to grade each model and find their approaches to be unsophisticated compared to human baselines; Claude Opus 4.6 achieves a rubric score of 26.5%, which means there is significant room for improvement. KellyBench is available as an open-access API endpoint at this https URL.

---


### 162. [Parameter-Efficient Architectural Modifications for Translation-Invariant CNNs](https://arxiv.org/abs/2604.27870)

**<font color=#1a73e8>作者：</font>** Nuria Alabau-Bosque, Jorge Vila-Tomas, Paula Dauden-Oliver 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Networks (CNNs) are widely assumed to be translation-invariant, yet standard architectures exhibit a startling fragility: even a single-pixel shift can drastically degrade performance due to their reliance on spatially dependent fully connected layers. In this work, we resolve this vulnerability by proposing a lightweight 'Online Architecture' strategy. By strategically inserting Global Average Pooling (GAP) layers at various network depths, we effectively decouple feature recognition from spatial location. Using VGG-16 as a primary case study, we demonstrate that this architectural modification achieves a massive 98% reduction in trainable parameters (from 5.2M to just 82K) and a 90% reduction in total network size (138M to 14M). Despite this drastic pruning, our variants maintain competitive Top-1 accuracy on ImageNet (66.4%) while doubling translational robustness, reducing average relative loss from 0.09 to 0.05. Furthermore, our analysis identifies a fundamental limit to invariance: while GAP resolves macroscopic sensitivity, discrete pooling operations introduce a residual periodic aliasing that prevents perfect pixel-level stability. Finally, we extend these findings to Perceptual Image Quality Assessment (IQA) by integrating our invariant backbones into the LPIPS framework. The resulting metric significantly outperforms the retrained baseline in generalization across the KADID-10k dataset (Spearman 0.89 vs. 0.75) and achieves a near-perfect alignment with human psychophysical response curves on the RAID dataset (Spearman 0.95). These results confirm that enforcing architectural invariance is a far more efficient and biologically plausible path to robustness than traditional data augmentation. Data and code are publicly available. The data and code are publicly available to facilitate validation and further research.

---


### 163. [Frequency-Aware Semantic Fusion with Gated Injection for AI-generated Image Detection](https://arxiv.org/abs/2604.27875)

**<font color=#1a73e8>作者：</font>** Shuchang Zhou, Shangkun Wu, Jiwei Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated images are becoming increasingly realistic and diverse, posing significant challenges for generalizable detection. While Vision Foundation Models (VFMs) provide rich semantic representations and frequency-based methods capture complementary artifact cues, existing approaches that combine these modalities still suffer from limited generalization, with notable performance degradation on unseen generative models. We attribute this limitation to two key factors: frequency shortcut bias toward easily distinguishable cues associated with specific generators and cross-domain representation conflict between high-level semantics and low-level frequency patterns. To address these issues, we propose a Frequency-aware Gated Injection Network (FGINet) to improve generalization. Specifically, we design a Band-Masked Frequency Encoder (BMFE) that applies cross-band masking in the frequency domain to reduce reliance on generator-specific patterns and encourage more diverse and generalizable representations. We further introduce a Layer-wise Gated Frequency Injection (LGFI) mechanism to progressively inject frequency cues into the VFM backbone with adaptive gating, aligning with its hierarchical abstraction and alleviating representation conflict. Moreover, we propose a Hyperspherical Compactness Learning (HCL) framework with a cosine margin objective to learn compact and well-separated representations. Extensive experiments demonstrate that FGINet achieves state-of-the-art performance and strong generalization across multiple challenging datasets.

---


### 164. [Building Persona-Based Agents On Demand: Tailoring Multi-Agent Workflows to User Needs](https://arxiv.org/abs/2604.27882)

**<font color=#1a73e8>作者：</font>** Giuseppe Arbore, Andrea Sillano, Luigi De Russis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic AI are shifting automation from discrete tools to proactive multi-agent systems that coordinate multi-specialized capabilities behind unified interfaces. However, today's agent systems typically rely on hard-coded agent architectures with fixed roles, coordination patterns, and interaction flows that limit end-user personalization and make adaptation to individual needs and contexts difficult. Given this limitation, we argue that on-demand persona-based agent generation offers a promising path towards more efficient and contextually appropriate interaction within agentic workflows. By dynamically crafting agents and personas at run-time to match user characteristics, task demands, and workflow context, agentic platforms can move beyond one-size-fits-all configurations. We present a pipeline for on-demand persona generation in agentic platforms, detailing how real-time crafting of AI personas can be systematically integrated within agent systems, aiming to open new possibilities in agentic platform design paradigms.

---


### 165. [Noise2Map: End-to-End Diffusion Model for Semantic Segmentation and Change Detection](https://arxiv.org/abs/2604.27889)

**<font color=#1a73e8>作者：</font>** Ali Shibli, Andrea Nascetti, Yifang Ban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation and change detection are two fundamental challenges in remote sensing, requiring models to capture either spatial semantics or temporal differences from satellite imagery. Existing deep learning models often struggle with temporal inconsistencies or in capturing fine-grained spatial structures, require extensive pretraining, and offer limited interpretability - especially in real-world remote sensing scenarios. Recent advances in diffusion models show that Gaussian noise can be systematically leveraged to learn expressive data representations through denoising. Motivated by this, we investigate whether the noise process in diffusion models can be effectively utilized for discriminative tasks. We propose Noise2Map, a unified diffusion-based framework that repurposes the denoising process for fast, end-to-end discriminative learning. Unlike prior work that uses diffusion only for generation or feature extraction, Noise2Map directly predicts semantic or change maps using task-specific noise schedules and timestep conditioning, avoiding the costly sampling procedures of traditional diffusion models. The model is pretrained via self-supervised denoising and fine-tuned with supervision, enabling both interpretability and robustness. Our architecture supports both tasks (SS and CD) through a shared backbone and task-specific noise schedulers. Extensive evaluations on the SpaceNet7, WHU, and xView2 buildings damaged by wildfires datasets demonstrate that Noise2Map ranks on average 1st among seven models on semantic segmentation and 1st on change detection by a cross-dataset rank metric (average F1 primary, IoU tie-break). Ablation studies highlight the robustness of our model against different training noise schedulers and timestep control in the diffusion process, as well as the ability of the model to perform multi-task learning.

---


### 166. [In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks](https://arxiv.org/abs/2604.27891)

**<font color=#1a73e8>作者：</font>** Simon Dennis, Michael Diamond, Rivaan Patil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent orchestration frameworks -- LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, and others -- place an external orchestrator above the LLM, tracking state and injecting routing instructions at every turn. We present a controlled comparison showing that for procedural tasks, this architecture is dominated by a simpler alternative: putting the entire procedure in the system prompt and letting the model self-orchestrate. Across three domains -- travel booking (14 nodes), Zoom technical support (14 nodes), and insurance claims processing (55 nodes) -- we evaluate 200 conversations per condition using LLM-as-judge scoring on five quality criteria. The in-context approach scores 4.53--5.00 on a 5-point scale while a LangGraph orchestrator using the same model scores 4.17--4.84. The orchestrated system fails on 24% of travel, 9% of Zoom, and 17% of insurance conversations, compared to 11.5%, 0.5%, and 5% for the in-context baseline. While external orchestration may have been necessary for earlier models, advances in frontier model capabilities have made it unnecessary for multi-turn conversations following a defined procedure.

---


### 167. [HiMix: Hierarchical Artifact-aware Mixup for Generalized Synthetic Image Detection](https://arxiv.org/abs/2604.27903)

**<font color=#1a73e8>作者：</font>** Shuchang Zhou, Kaiwen Shen, Jiwei Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of generative models has enabled the creation of highly realistic and diverse synthetic images, posing significant challenges to reliable and generalizable Synthetic Image Detection (SID). However, existing detectors are typically trained on limited and biased datasets, resulting in poor generalization to unseen generators. To address this issue, we propose HiMix, a unified framework that enhances generalization by expanding the training distribution and promoting artifact-aware representations. Specifically, the Mixup-driven Distributional Augmentation (MDA) module constructs continuous transitional samples between real and fake images, improving coverage of low-confidence regions and exposing the model to more challenging samples, while the pixel-wise mixup operation smoothly perturbs semantics to enhance sensitivity to low-level artifacts. Moreover, the Hierarchical Artifact-aware Representation (HAR) module aggregates artifact information from both global and local levels through cross-layer integration and coarse-to-fine feature fusion, enabling the extraction of discriminative forgery representations under diverse distributions. Extensive experiments across multiple benchmarks demonstrate that HiMix achieves state-of-the-art performance, establishing well-separated logits for improved generalization to unseen forgeries.

---


### 168. [CoNewsReader: Supporting Comprehensive Understanding and Raising Critical Thoughts on Social Media News Through Comments](https://arxiv.org/abs/2604.27905)

**<font color=#1a73e8>作者：</font>** Kangyu Yuan, Guanzheng Chen, Sizhe Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Critical news reading (CNR), which requires grasping the holistic ideas of and raising critical thoughts on the news, is beneficial yet challenging for general people who usually get information on daily social media. Comments under the news can aid CNR by providing complementary information and other readers' diverse and critical thoughts. However, it is under-investigated how to leverage these comments to support users in CNR. In this paper, we first derive user requirements for a comment-based CNR tool from literature and a formative study (N=12). Then, we develop CoNewsReader, a comment-based interactive CNR tool powered by a large language model. CoNewsReader supports users in grasping the news idea with complementary information from comments, filtering useful comments for CNR, and getting questions generated based on the comments to conduct critical thinking. Our within-subjects study with 24 university students indicates that compared to a baseline news reading interface in social media, participants with CoNewsReader have a more engaging CNR experience and perform better on comprehending the news and raising critical thoughts. We discuss design considerations for supporting reading tasks with user- and machine-generated content.

---


### 169. [From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction](https://arxiv.org/abs/2604.27906)

**<font color=#1a73e8>作者：</font>** Alex Petrov, Alexander Gusak, Denis Mukha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent AI memory is often reduced to a retrieval problem: store prior interactions as text, embed them, and ask the model to recover relevant context later. This design is useful for thematic recall, but it is mismatched to the kinds of memory that agents need in production: exact facts, current state, updates and deletions, aggregation, relations, negative queries, and explicit unknowns. These operations require memory to behave less like search and more like a system of record.
This paper argues that reliable external AI memory must be schema-grounded. Schemas define what must be remembered, what may be ignored, and which values must never be inferred. We present an iterative, schema-aware write path that decomposes memory ingestion into object detection, field detection, and field-value extraction, with validation gates, local retries, and stateful prompt control. The result shifts interpretation from the read path to the write path: reads become constrained queries over verified records rather than repeated inference over retrieved prose.
We evaluate this design on structured extraction and end-to-end memory benchmarks. On the extraction benchmark, the judge-in-the-loop configuration reaches 90.42% object-level accuracy and 62.67% output accuracy, above all tested frontier structured-output baselines. On our end-to-end memory benchmark, xmemory reaches 97.10% F1, compared with 80.16%-87.24% across the third-party baselines. On the application-level task, xmemory reaches 95.2% accuracy, outperforming specialised memory systems, code-generated Markdown harnesses, and customer-facing frontier-model application harnesses. The results show that, for memory workloads requiring stable facts and stateful computation, architecture matters more than retrieval scale or model strength alone.

---


### 170. [Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918)

**<font color=#1a73e8>作者：</font>** Zujin Guo, Zhenhui Ye, Yi Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing talking avatar methods typically adopt an image-to-video pipeline conditioned on a static reference image within the same scene as the target generation. This restricted, single-view perspective lacks sufficient temporal and expression cues, limiting the ability to synthesize high-fidelity talking avatars in customized backgrounds. To this end, we introduce Talking Avatar generation from Video Reference (TAVR), a novel framework that shifts the paradigm by leveraging cross-scene video inputs. To effectively process these extended temporal contexts and bridge cross-scene domain gaps, TAVR integrates a token selection module alongside a comprehensive three-stage training scheme. Specifically, same-scene video pretraining establishes foundational appearance copying, which is subsequently expanded by cross-scene reference fine-tuning for robust cross-scene adaptation. Finally, task-specific reinforcement learning aligns the generated outputs with identity-based rewards to maximize identity similarity. To systematically evaluate cross-scene robustness, we construct a new benchmark comprising 158 carefully curated cross-scene video pairs. Extensive experiments show that TAVR benefits from flexible inference-time video referencing and consistently surpasses existing baselines both quantitatively and qualitatively. This work has been deployed to production. For more related research, please visit \href{this https URL}{HeyGen Research} and \href{this https URL}{HeyGen Avatar-V}.

---


### 171. [Taming the Centaur(s) with LAPITHS: a framework for a theoretically grounded interpretation of AI performances](https://arxiv.org/abs/2604.27927)

**<font color=#1a73e8>作者：</font>** Matteo Da Pelo, Alessio Donvito, Claudio Frongia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a framework called LAPITHS (Language model Analysis through Paradigm grounded Interpretations of Theses about Human likenesS) and use it to show that several major claims advanced by models such as CENTAUR, proposed as an artificial Unified Model of Cognition, are not theoretically or empirically justified. LAPITHS provides a principled reference point for counteracting the current behaviouristic tendency in AI research to interpret the human level performances of transformer based language models as evidence of human like underlying computation and, by extension, as signs of cognitive abilities. The novelty of LAPITHS lies in making explicit the arguments grounded in two quantitative assessments: (i) the Minimal Cognitive Grid, a theoretically motivated method for estimating the cognitive plausibility of artificial systems, and (ii) a behavioural comparison showing that results similar to those reported for CENTAUR like models can be reproduced by other systems that do not satisfy the structural constraints typically associated with cognitive plausibility, and whose outputs do not provide independent explanatory insight into human cognition.

---


### 172. [Training-Free Tunnel Defect Inspection and Engineering Interpretation via Visual Recalibration and Entity Reconstruction](https://arxiv.org/abs/2604.27928)

**<font color=#1a73e8>作者：</font>** Shipeng Liu, Liang Zhao, Dengfeng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tunnel inspection requires outputs that can support defect localization, measurement, severity grading, and engineering documentation. Existing training-free foundation-model pipelines usually stop at coarse open-vocabulary proposals, which are difficult to use directly in interference-heavy tunnel scenes. We propose a training-free framework TunnelMIND. Specifically, language-guided defect proposals are not treated as final outputs; instead, their spatial support is recalibrated at inference time through dense visual consistency, so that coarse semantic anchors can be transformed into more reliable prompts under tunnel-specific hard negatives. The resulting masks are further reconstructed into structured defect entities with category, location, geometry, severity, and context attributes, which are then mapped to retrieval-grounded explanation and engineering-readable report generation under expert knowledge constraints. On visible, GPR, and road defect tasks, TunnelMIND achieves F1 scores of 0.68, 0.78, and 0.72, respectively. Overall, TunnelMIND shows that training-free tunnel inspection can move beyond coarse localization toward structured defect evidence for engineering assessment.

---


### 173. [MM-StanceDet: Retrieval-Augmented Multi-modal Multi-agent Stance Detection](https://arxiv.org/abs/2604.27934)

**<font color=#1a73e8>作者：</font>** Weihai Lu, Zhejun Zhao, Yanshu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Stance Detection (MSD) is crucial for understanding public discourse, yet effectively fusing text and image, especially with conflicting signals, remains challenging. Existing methods often face difficulties with contextual grounding, cross-modal interpretation ambiguity, and single-pass reasoning fragility. To address these, we propose Retrieval-Augmented Multi-modal Multi-agent Stance Detection (MM-StanceDet), a novel multi-agent framework integrating Retrieval Augmentation for contextual grounding, specialized Multimodal Analysis agents for nuanced interpretation, a Reasoning-Enhanced Debate stage for exploring perspectives, and Self-Reflection for robust adjudication. Extensive experiments on five datasets demonstrate MM-StanceDet significantly outperforms state-of-the-art baselines, validating the efficacy of its multi-agent architecture and structured reasoning stages in addressing complex multimodal stance challenges.

---


### 174. [Beyond the Baseband: Adaptive Multi-Band Encoding for Full-Spectrum Bioacoustics Classification](https://arxiv.org/abs/2604.27936)

**<font color=#1a73e8>作者：</font>** Eklavya Sarkar, Marius Miron, David Robinson 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Animals hear and vocalize across frequency ranges that differ substantially from humans, often extending into the ultrasonic domain. Yet most computational bioacoustics systems rely on audio models pre-trained at 16 kHz, restricting their usable bandwidth to the 0-8 kHz baseband and discarding higher-frequency information present in many bioacoustic recordings. We investigate a multi-band encoding framework that decomposes the full spectrum of animal calls into band features and fuses them into a unified representation. Similarity analyses on models show that certain encoders produce decorrelated band embeddings that improve class separation after fusion. Classification experiments on three bioacoustic datasets using eight pre-trained models and five fusion strategies show that fused representations consistently outperform the baseband and time-expansion baselines on two datasets, showing the potential of multi-band methods for full-spectrum encoding of animal calls.

---


### 175. [A Collective Variational Principle Unifying Bayesian Inference, Game Theory, and Thermodynamics](https://arxiv.org/abs/2604.27942)

**<font color=#1a73e8>作者：</font>** Djamel Bouchaffra, Faycal Ykhlef, Mustapha Lebbah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collective intelligence emerges across biological, physical, and artificial systems without central coordination, yet a unifying principle governing such behaviour remains elusive. The Free Energy Principle explains how individual agents adapt through variational inference, while game theory formalises strategic interactions. Here we introduce the Game-Theoretic Free Energy Principle, a unified framework showing that multi-agent systems performing local free-energy minimisation implicitly implement a stochastic game. We prove that, under bounded rationality and local information constraints, stationary points of collective free energy correspond to approximate Nash equilibria of an induced game. Conversely, a broad class of cooperative games admits a variational representation in which equilibria arise as Gibbs distributions over coalitions, establishing a bridge between Bayesian inference and strategic interaction. To characterise higher-order effects, we introduce a free-energy formulation of the Harsanyi dividend, isolating irreducible multi-agent synergy. This yields a predictive theory of cooperation, including a falsifiable non-monotonic relationship between sensory precision and agent influence. We validate this prediction across neural, biological, and artificial multi-agent systems. These results identify a common variational principle underlying inference, thermodynamics, and game-theoretic equilibrium.

---


### 176. [Calibrating Attribution Proxies for Reward Allocation in Participatory Weather Sensing](https://arxiv.org/abs/2604.27944)

**<font color=#1a73e8>作者：</font>** Mark C. Ballandies, Michael T. C. Chiu, Claudio J. Tessone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale IoT weather sensing networks require incentive mechanisms to sustain participation, yet determining how much value individual data contributions bring to the network remains an open problem. Existing approaches address data quality but not data valuation; in operational meteorology, adjoint-based methods derive value from the forecast model itself but require full data assimilation infrastructure. We propose to utilise differentiable AI weather models to fill this gap and characterise gradient-based attribution on gridded GFS analysis inputs as a candidate value signal, evaluating fidelity, calibration, cost, and gaming vulnerability across more than 400 configurations. Attribution captures near-optimal sensor placement utility with monotonically faithful payments, but can be inflated by adversarial inputs, with detection requiring external baseline data. These findings establish gradient attribution as a computationally validated signal for model-informed reward allocation in participatory weather sensing.

---


### 177. [MyoKin3X: A Myoelectric Framework for Full-Hand 3D Force Recording](https://arxiv.org/abs/2604.27949)

**<font color=#1a73e8>作者：</font>** Charlotte Rohleder, Raul Sîmpetru, Annika Wünsch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simultaneous multi-directional force measurement across all five digits is essential for studying hand coordination, compensatory forces, and myoelectric control, yet existing systems trade off digit coverage, force dimensionality, and anatomical adaptability. Reliable full-hand acquisition remains challenging because multi-axis calibration, hand-size adjustment, and consistent digit-specific force reconstruction are technically demanding. We present MyoKin3X, a customizable full-hand framework for simultaneous 3D force measurement of up to five digits providing robust and validated force reconstruction. It combines an anatomically versatile structure with five integrated 3D force sensors and a standalone software for synchronized electromyography and force acquisition. MyoKin3X provides in-place cross-calibration of all five sensors, single- and multi-digit maximal voluntary contraction recording, and automated coordinate transformation to digit-specific coordinate systems for standardized analysis across subjects and tasks. Calibration validation demonstrates high stability of the axis-specific calibration factors, with a mean coefficient of variation of 0.04% and maximum force error of +- 0.06N at 50N. It also shows effective inter-axis decoupling (mean crosstalk reduction: 92.71%; residual crosstalk below 0.02% for most axis pairs) and high predictive accuracy (R2 > 0.99 across sensors). The software includes four feedback modes: 1D ramps, fatigue protocols, 2D arbitrary target ramps, and 2D exploratory tasks. MyoKin3X therefore enables standardized full-hand force acquisition with validated measurement reliability, flexible protocol control, and real-time visualization for high-fidelity studies of hand motor control, muscle synergies, and human-machine interfacing.

---


### 178. [GUI Agents with Reinforcement Learning: Toward Digital Inhabitants](https://arxiv.org/abs/2604.27955)

**<font color=#1a73e8>作者：</font>** Junan Hu, Jian Liu, Jingxiang Lai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents have emerged as a promising paradigm for intelligent systems that perceive and interact with graphical interfaces visually. Yet supervised fine-tuning alone cannot handle long-horizon credit assignment, distribution shifts, and safe exploration in irreversible environments, making Reinforcement Learning (RL) a central methodology for advancing automation. In this work, we present the first comprehensive overview of the intersection between RL and GUI agents, and examine how this research direction may evolve toward digital inhabitants. We propose a principled taxonomy that organizes existing methods into Offline RL, Online RL, and Hybrid Strategies, and complement it with analyses of reward engineering, data efficiency, and key technical innovations. Our analysis reveals several emerging trends: the tension between reliability and scalability is motivating the adoption of composite, multi-tier reward architectures; GUI I/O latency bottlenecks are accelerating the shift toward world-model-based training, which can yield substantial performance gains; and the spontaneous emergence of System-2-style deliberation suggests that explicit reasoning supervision may not be necessary when sufficiently rich reward signals are available. We distill these findings into a roadmap covering process rewards, continual RL, cognitive architectures, and safe deployment, aiming to guide the next generation of robust GUI automation and its agent-native infrastructure.

---


### 179. [Real-Time Control of a Virtual Orchestra by Recognition of Conducting Gestures](https://arxiv.org/abs/2604.27957)

**<font color=#1a73e8>作者：</font>** Mert Mermerci, Emile Pascoe, Fredrik Edström 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present a museum installation in a 180° dome theater, which gives the museum visitor the experience of conducting a symphony orchestra. We have pre-recorded a short music piece performed by a professional orchestra. This recording is played back in the dome with the visitor standing in the conductor's position. The visitor's gestures are captured with a vision-based skeleton tracker, steering the recording playback pace via a gesture recognition module that translates the gestures into a time control signal. This is sent to a playback module that plays the recording in the dome at the corresponding speed. The gesture recognition module is based on a hierarchical LSTM network, trained with recorded sequences of multiple conductors with different level of expertise conducting the same recording. The system is evaluated with a quantitative study of the estimated timing accuracy, a user study evaluating the musical realism and usability of the real-time control, and a field study to evaluate the performance of the entire system with real museum visitors.

---


### 180. [TripVVT: A Large-Scale Triplet Dataset and a Coarse-Mask Baseline for In-the-Wild Video Virtual Try-On](https://arxiv.org/abs/2604.27958)

**<font color=#1a73e8>作者：</font>** Dingbao Shao, Song Wu, Shenyi Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the scarcity of large-scale in-the-wild triplet data and the improper use of masks, the performance of video virtual try-on models remains limited. In this paper, we first introduce **TripVVT-10K**, the largest and most diverse in-the-wild triplet dataset to date, providing explicit video-level cross-garment supervision that existing video datasets lack. Built upon this resource, we develop **TripVVT**, a Diffusion Transformer-based framework that replaces fragile garment masks with a simple, stable human-mask prior, enabling reliable background preservation while remaining robust to real-world motion, occlusion, and cluttered scenes. To support comprehensive evaluation, we further establish **TripVVT-Bench**, a 100-case benchmark covering diverse garments, complex environments, and multi-person scenarios, with metrics spanning video quality, try-on fidelity, background consistency, and temporal coherence. Compared to state-of-the-art academic and commercial systems, TripVVT achieves superior video quality and garment fidelity while markedly improving generalization to challenging in-the-wild videos. We publicly release the dataset and benchmark, which we believe provide a solid foundation for advancing controllable, realistic, and temporally stable video virtual try-on.

---


### 181. [Splitting Assumption-Based Argumentation Frameworks](https://arxiv.org/abs/2604.27964)

**<font color=#1a73e8>作者：</font>** Giovanni Buraglio, Wolfgang Dvorak, Stefan Woltran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assumption-Based Argumentation (ABA) is a well-established formalism for modelling and reasoning over debates, with a wide range of applications. However, the high computational complexity of core reasoning tasks in ABA poses a significant challenge for its applicability. This issue is further aggravated when ABA frameworks (ABAFs) are instantiated into graph-based argumentation formalisms, such as Dung's Argumentation Frameworks (AFs) and Argumentation Frameworks with Collective Attacks (SETAFs). In knowledge representation and reasoning, a key strategy to address computational intractability is to optimise reasoning over a given knowledge base through divide-and-conquer algorithms. A paradigmatic example of this approach is splitting, where extensions of a given framework are computed incrementally, by restricting the search space to sub-frameworks only, and then combining the obtained results. This approach has been successfully applied to AFs, for which also a parametrised version has been introduced under stable semantics. However, the exponential growth produced by the instantiation might undermine the usefulness of splitting on the argument graphs induced by ABAFs. To address this issue, our work investigates the concept of splitting on the knowledge base rather than on its graph-based instantiation. Furthermore, we generalise splitting to its parametrised version for ABAFs.

---


### 182. [Differentiable latent structure discovery for interpretable forecasting in clinical time series](https://arxiv.org/abs/2604.27967)

**<font color=#1a73e8>作者：</font>** Ivan Lerner, Jean Feydy, Alexandre Kalimouttou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Timely, uncertainty-aware forecasting from irregular electronic health records (EHR) can support critical-care decisions, yet most approaches either impute to a grid or sacrifice interpretability. We introduce StructGP, a continuous-time multi-task Gaussian process that couples process convolutions with differentiable structure learning to uncover a sparse, ordered directed acyclic graph (DAG) of inter-variable dependencies while preserving principled uncertainty. We further propose LP-StructGP, which augments StructGP with latent pathways-shared, temporally shifted trajectories inferred via subject-specific coupling filters and a softmax gating mechanism-to capture cross-patient progression patterns. Both models are trained under sparsity and acyclicity constraints (augmented Lagrangian, Adam) using scalable low-rank updates. Results: In simulations, the approach reliably recovers ground-truth graphs (Structural Hamming Distance approaching 0 as cohorts grow) and pathway assignments (high Adjusted Rand Index). On a MIMIC-IV septic shock cohort (n=1,008; norepinephrine, creatinine, mean arterial pressure), StructGP improves short-horizon (6 h) forecasting over independent-task baselines (average RMSE 0.68 [95%CI: 0.63--0.74] vs. 0.88 [0.83-0.94]) and, with 15 additional inputs, markedly outperforms unstructured kernels (0.63 [0.58-0.69] vs. 3.02 [2.85-3.18]) with superior calibration (coverage 0.96 vs. 0.84). On the PhysioNet Challenge (12k patients, 41 variables), StructGP attains competitive accuracy (MAE 3.72e-2) relative to a state-of-the-art graph neural model while maintaining calibrated uncertainty. Conclusion: These results show that structured process convolutions with latent pathways deliver interpretable, scalable, and well-calibrated forecasting for irregular clinical time series.

---


### 183. [ClimateVID -- Social Media Videos Analysis and Challenges Involved](https://arxiv.org/abs/2604.27968)

**<font color=#1a73e8>作者：</font>** Shiqi Xu, Moritz Burmester, Katharina Prasse 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The pervasive growth of digital content, specifically short videos on social media platforms, has significantly altered how topics are discussed and understood in public discourse. In this work, we advance automated visual theme detection by assessing zero-shot and clustering capabilities on social media data. (1) We evaluated the capabilities of notable VLMs such as VideoChatGPT, PandaGPT, and VideoLLava using zero-shot image classification and compared their performance to the baseline provided by frame-wise CLIP image classification. (2) By treating clustering as a minimum cost multicut problem, we aim to uncover insightful patterns in an unsupervised manner. For both analysis strategies, we provide extensive evaluations and practical guidance to practitioners. While VLMs are currently not able to detect climate change specific classes, the clustering results are distinct visual frames. %Given that VLMs are not currently capable to grasp the climate change discourse, we focus the clustering evaluation of image embedding models. We find that both ConvNeXt V2 and DINOv2 produce meaningful clusters, with DINOv2 focusing more on style differences and abstract categories, while ConvNeXt V2 clusters differ in more fine-grained ways. Code available at this https URL.

---


### 184. [TransVLM: A Vision-Language Framework and Benchmark for Detecting Any Shot Transitions](https://arxiv.org/abs/2604.27975)

**<font color=#1a73e8>作者：</font>** Ce Chen, Yi Ren, Yuanming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional Shot Boundary Detection (SBD) inherently struggles with complex transitions by formulating the task around isolated cut points, frequently yielding corrupted video shots. We address this fundamental limitation by formalizing the Shot Transition Detection (STD) task. Rather than searching for ambiguous points, STD explicitly detects the continuous temporal segments of transitions. To tackle this, we propose TransVLM, a Vision-Language Model (VLM) framework for STD. Unlike regular VLMs that predominantly rely on spatial semantics and struggle with fine-grained inter-shot dynamics, our method explicitly injects optical flow as a critical motion prior at the input stage. Through a simple yet effective feature-fusion strategy, TransVLM directly processes concatenated color and motion representations, significantly enhancing its temporal awareness without incurring any additional visual token overhead on the language backbone. To overcome the severe class imbalance in public data, we design a scalable data engine to synthesize diverse transition videos for robust training, alongside a comprehensive benchmark for STD. Extensive experiments demonstrate that TransVLM achieves superior overall performance, outperforming traditional heuristic methods, specialized spatiotemporal networks, and top-tier VLMs. This work has been deployed to production. For more related research, please visit HeyGen Research (this https URL) and HeyGen Avatar-V (this https URL). Project page: this https URL

---


### 185. [D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery](https://arxiv.org/abs/2604.27977)

**<font color=#1a73e8>作者：</font>** Hanane Nour Moussa, Yifei Li, Zhuoyang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in language models and agents for scientific data-driven discovery, further advancing their capabilities is held back by the absence of verifiable environments representing real-world scientific this http URL fill this gap, we introduce D3-Gym, the first automatically constructed dataset with verifiable environments for scientific Data-Driven Discovery. D3-Gym comprises (1) 565 tasks sourced from 239 real scientific repositories across four disciplines where (2) each task is equipped with a natural language instruction, an executable environment with pre-installed dependencies, input dataset and artifact previews, a reference code solution, and an automatically synthesized evaluation script. Rigorous evaluation of the quality of the verification signal in D3-Gym confirms that our evaluation scripts achieve 87.5% agreement with human-annotated gold standards and strong alignment in domain-specific evaluation logic, showing their scientific soundness. Further, training on trajectories sampled from D3-Gym yields consistent and substantial gains across Qwen3 models of varying sizes on ScienceAgentBench, boosting Qwen3-32B by 7.8 absolute points and substantially shrinking the gap with strong proprietary models. All D3-Gym artifacts (environments, creation workflow, trajectories, and models) can be found at this https URL.

---


### 186. [ITS-Mina: A Harris Hawks Optimization-Based All-MLP Framework with Iterative Refinement and External Attention for Multivariate Time Series Forecasting](https://arxiv.org/abs/2604.27981)

**<font color=#1a73e8>作者：</font>** Pourya Zamanvaziri, Amirhossein Sadr, Aida Pakniyat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting plays a pivotal role in numerous real-world applications, including financial analysis, energy management, and traffic planning. While Transformer-based architectures have gained popularity for this task, recent studies reveal that simpler MLP-based models can achieve competitive or superior performance with significantly reduced computational cost. In this paper, we propose ITS-Mina, a novel all-MLP framework for multivariate time series forecasting that integrates three key innovations: (1) an iterative refinement mechanism that progressively enhances temporal representations by repeatedly applying a shared-parameter residual mixer stack, effectively deepening the model's computational capacity without multiplying the number of distinct parameters; (2) an external attention module that replaces traditional self-attention with learnable memory units, capturing cross-sample global dependencies at linear computational complexity; and (3) a Harris Hawks Optimization (HHO) algorithm for automatic dropout rate tuning, enabling adaptive regularization tailored to each dataset. Extensive experiments on six widely-used benchmark datasets demonstrate that ITS-Mina achieves state-of-the-art or highly competitive performance compared to eleven baseline models across multiple forecasting horizons.

---


### 187. [When and How AI Should Assist Brainstorming for AI Impact Assessment](https://arxiv.org/abs/2604.27997)

**<font color=#1a73e8>作者：</font>** Jarod Govers, Sanja Šćepanović, Daniele Quercia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A key task in AI practice is to assess potential impacts to prevent harm. Current AI tools assisting AI impact assessment have not been designed or evaluated for collaborative team brainstorming, and they do not capture the range of views in diverse teams. We studied how AI can support team brainstorming during AI impact assessment and made three contributions. First, we adapted two structured methods from strategic foresight and co-designed AI interventions for them in five in-person workshops with 28 participants in total. Second, we evaluated the interventions in ten in-person workshops with 54 participants, finding that AI improved impact assessment quality and brainstorming perceptions for a general-purpose AI use (a chatbot companion) but not for a specialised one (a kidney allocation application). Third, our findings result in broader design guidance for AI assistance in brainstorming: AI should only offer hints and not solutions during early ideation, initiating interaction only when participants face fixation or saturation; it should facilitate structuring ideas during convergence; leverage expertise to refine ideas; and overall, it should serve more in support of tedious brainstorming process tasks, rather than ideation that teams value to do themselves.

---


### 188. [Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning](https://arxiv.org/abs/2604.27998)

**<font color=#1a73e8>作者：</font>** Jingcheng Deng, Zihao Wei, Liang Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning offers a more efficient alternative to explicit reasoning by compressing intermediate reasoning into continuous representations and substantially shortening reasoning chains. However, existing latent reasoning methods mainly focus on supervised learning, and reinforcement learning in latent space remains highly unstable. We study this problem through the lens of Group Relative Policy Optimization (GRPO), and show that directly adapting GRPO to latent reasoning is fundamentally non-trivial: latent reasoning changes both the probability density and the sampling mechanism, causing three coupled bottlenecks: absence of intrinsic latent manifolds, where unconstrained exploration pushes rollouts off the valid latent manifold; exploration-optimization misalignment, where trajectory-level rewards can induce incorrect token-level updates; and latent mixture non-closure, where jointly reinforcing multiple correct latent paths can produce an invalid averaged state. To address them, we propose \textbf{Latent-GRPO}, which combines invalid-sample advantage masking, one-sided noise sampling, and optimal correct-path first-token selection. Across four low-difficulty benchmarks (e.g., GSM8K-Aug) and four high-difficulty benchmarks (e.g., AIME), Latent-GRPO improves over its latent initialization by 7.86 Pass@1 points on low-difficulty tasks and surpasses explicit GRPO by 4.27 points on high-difficulty tasks while using 3--4$\times$ shorter reasoning chains. It also achieves stronger pass@$k$ performance under Gumbel sampling. These results establish Latent-GRPO as an effective approach for stable and efficient latent reasoning.

---


### 189. [A Pattern Language for Resilient Visual Agents](https://arxiv.org/abs/2604.28001)

**<font color=#1a73e8>作者：</font>** Habtom Kahsay Gidey, Alexander Lenz, Alois Knoll  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating multimodal foundation models into enterprise ecosystems presents a fundamental software architecture challenge. Architects must balance competing quality attributes: the high latency and non-determinism of vision language action (VLA) models versus the strict determinism and real-time performance required by enterprise control loops. In this study, we propose an architectural pattern language for visual agents that separates fast, deterministic reflexes from slow, probabilistic supervision. It consists of four architectural design patterns: (1) Hybrid Affordance Integration, (2) Adaptive Visual Anchoring, (3) Visual Hierarchy Synthesis, and (4) Semantic Scene Graph.

---


### 190. [Learning from Disagreement: Clinician Overrides as Implicit Preference Signals for Clinical AI in Value-Based Care](https://arxiv.org/abs/2604.28010)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Abhishek Gupta, Chris Betz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We reframe clinician overrides of clinical AI recommendations as implicit preference data - the same signal structure exploited by reinforcement learning from human feedback (RLHF), but richer: the annotator is a domain expert, the alternatives carry real consequences, and downstream outcomes are observable. We present a formal framework extending standard preference learning with three contributions: a five-category override taxonomy mapping override types to distinct model update targets; a preference formulation conditioned on patient state s, organizational context c, and clinician capability kappa, where kappa decomposes into execution capability kappa-exec and alignment capability kappa-align; and a dual learning architecture that jointly trains a reward model and a capability model via alternating optimization, preventing a failure mode we term suppression bias-the systematic suppression of correct-but-difficult recommendations when clinician capability falls below the execution threshold. We argue that chronic disease management under outcome-based payment contracts produces override data with uniquely favorable properties-longitudinal density, concentrated decision space, outcome labels, and natural capability variation-and that training environments combining longitudinal outcome measurement with aligned financial incentives are a necessary condition for learning a reward model aligned with patient trajectory rather than with encounter economics. This framework emerged from operational work to improve clinician capability in a live value-based care deployment.

---


### 191. [Faster 3D Gaussian Splatting Convergence via Structure-Aware Densification](https://arxiv.org/abs/2604.28016)

**<font color=#1a73e8>作者：</font>** Linjie Lyu, Ayush Tewari, Jianchun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has emerged as a powerful scene representation for real-time novel-view synthesis. However, its standard adaptive density control relies on screen-space positional gradients, which do not distinguish between geometric misplacement and frequency aliasing, often leading to either over-blurred high-frequency textures or inefficient over-densification. We present a structure-aware densification framework. Our key insight is that the decision to subdivide a Gaussian should be driven by an explicit comparison between its projected screen-space extent and the local structure of the texture it seeks to represent. We introduce a multi-scale frequency analysis combining structure tensors with Laplacian scale space analysis to estimate the dominant frequency at each pixel, enabling robust supervision across varying texture scales. Based on this analysis, we define $\eta$, a per-Gaussian, per-axis frequency violation metric that indicates when a primitive may be under-resolving local texture details. Unlike methods that perform isotropic splitting (e.g., splitting each Gaussian into two smaller ones with uniform shape), our approach performs anisotropic splitting. For each axis with high $\eta$, we compute a split factor to better resolve the local frequency content. We further introduce a multiview consistency criterion that aggregates $\eta$ observations across multiple views. By performing densification early and faster, we skip the lengthy iterative densification phases required by baseline methods and achieve significantly faster convergence. Experiments on standard benchmarks demonstrate that our method also achieves superior reconstruction quality, particularly in high-frequency regions.

---


### 192. [Cost-Aware Learning](https://arxiv.org/abs/2604.28020)

**<font color=#1a73e8>作者：</font>** Clara Mohri, Amir Globerson, Haim Kaplan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of Cost-Aware Learning, where sampling different component functions of a finite-sum objective incurs different costs. The objective is to reach a target error while minimizing the total cost. First, we propose the Cost-Aware Stochastic Gradient Descent algorithm for convex functions, and derive its cost complexity to attain an error of $\epsilon$. Furthermore, we establish a lower bound for this setting and provide a subset selection algorithm to further reduce the cost of training. We apply our theoretical insights to reinforcement learning with language models, where the computational cost of policy gradients varies with sequence length. To this end, we introduce Cost-Aware GRPO, an algorithm designed to reduce the cost of policy optimization while preserving performance. Empirical results on 1.5B and 8B LLMs demonstrate that our approach reduces the tokens used in policy optimization by up to about 30% while matching or exceeding baseline accuracy.

---


### 193. [Are DeepFakes Realistic Enough? Exploring Semantic Mismatch as a Novel Challenge](https://arxiv.org/abs/2604.28022)

**<font color=#1a73e8>作者：</font>** Sharayu Nilesh Deshmukh, Kailash A. Hambarde, Joana C. Costa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current DeepFake detection scenarios are mostly binary, yet data manipulation can vary across audio, video, or both, whose variability is not captured in binary settings. Four-class audio-visual formulations address this by discriminating manipulation type, but introduce a unresolved problem: models may rely solely on data source integrity to detect DeepFakes without evaluating their semantic consistency. If the DeepFake origin is not in the data source but in its content, can semantic mismatch be assessed by the state-of-the-art? This paper proposes a new evaluation setup, extending the four-class formulation by explicitly modeling semantic-level inconsistency between authentic modalities with the introduction a new class: Real Audio-Real Video with Semantic Mismatch (RARV-SMM). We assess the robustness of state-of-the-art models in this new realistic DeepFake setting, using the FakeAVCeleb dataset, highlighting the limitations of existing approaches when faced with semantic mismatch data. We further introduce three RARV-SMM variants that expose distinct architectural vulnerabilities as audio-visual divergence increases. We also propose a semantic reinforcement strategy that incorporates the semantic mismatch class and ImageBind embeddings to improve DeepFake detection in both our proposed and state-of-the-art settings, on FakeAVCeleb and LAV-DF, paving the way to more realistic DeepFake detectors. The source code and data are available at this https URL.

---


### 194. [FedHarmony: Harmonizing Heterogeneous Label Correlations in Federated Multi-Label Learning](https://arxiv.org/abs/2604.28024)

**<font color=#1a73e8>作者：</font>** Zhiqiang Kou, Junxiang Wu, Wenke Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Multi-Label Learning is a distributed paradigm where multiple clients possess heterogeneous multi-label data and perform collaborative learning under privacy constraints without sharing raw data. However, modeling label correlations under heterogeneous distributions remains challenging. Due to client-specific label spaces and varying co-occurrence patterns, correlations learned by individual clients inevitably deviate from the global structure, a phenomenon we term label correlation drift. To address this, we propose FedHarmony, a framework that harmonizes heterogeneous label correlations across clients. It introduces consensus correlation, capturing agreement among other clients and serving as a global teacher to correct biased local estimates. During aggregation, FedHarmony evaluates each client by both data size and correlation quality, assigning weights accordingly. Moreover, we develop an accelerated optimization algorithm for FedHarmony and theoretically establish faster convergence without sacrificing accuracy. Experiments on real-world federated multi-label datasets show that FedHarmony consistently outperforms state-of-the-art methods.

---


### 195. [ResiHMR: Residual-Limb Aware Single-Image 3D Human Mesh Recovery for Individuals with Limb Loss](https://arxiv.org/abs/2604.28025)

**<font color=#1a73e8>作者：</font>** Jiaying Ying, Heming Du, Kaihao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image human mesh recovery provides a compact 3D, person-centric representation that supports analysis, animation, AR and VR, rehabilitation, and human-computer interaction. However, prevailing systems impose an intact-limb prior and degrade on people with limb loss, because fixed-topology models cannot represent residual limbs. In this work, we present ResiHMR, a residual-limb aware framework for single-image 3D human modeling. ResiHMR adopts residual-limb keypoints and introduces two components: (i) a topology-adaptive Residual Anchor-Factor Optimization module that constrains estimation to the observed kinematic subgraph of anatomically valid structures, and (ii) a geometry-based Residual-Limb Reconstruction module that estimates residual-limb boundaries and convex limb-termination geometry. These components introduce topology-aware optimization and explicit termination geometry as tools for human mesh recovery under non-standard limb anatomy. Unlike joint-removal methods in a fixed topology, ResiHMR explicitly reconstructs residual-limb surfaces and aligns optimization with limb-loss topology, which better matches prosthetic biomechanics and real-world use. To the best of our knowledge, this is the first single-image HMR system that explicitly reconstructs residual-limb surfaces and performs topology-adaptive optimization for individuals with limb loss. On a curated dataset of real-world images with limb loss, ResiHMR improves reconstruction quality under both SMPLify-X and HSMR backbones, reducing intact-joint 2D MPJPE from 41.32 to 37.40 with SMPLify-X and residual-limb 2D MPJPE from 73.61 to 23.19 with HSMR.

---


### 196. [MIFair: A Mutual-Information Framework for Intersectionality and Multiclass Fairness](https://arxiv.org/abs/2604.28030)

**<font color=#1a73e8>作者：</font>** Jeanne Monnier, Thomas George, Frédéric Guyard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness in machine learning remains challenging due to its ethical complexity, the absence of a universal definition, and the need for context-specific bias metrics. Existing methods still struggle with intersectionality, multiclass settings, and limited flexibility and generality. To address these gaps, we introduce MIFair, a unified framework for bias assessment and mitigation based on mutual information. MIFair provides a flexible metric template and an in-processing mitigation method inspired by the Prejudice Remover, defining group fairness as statistical independence between prediction-derived variables and sensitive attributes. We further strengthen its information-theoretic foundation by establishing equivalences with widely used fairness notions such as independence and separation. MIFair naturally supports intersectionality, complex subgroup structures, and multiclass classification and employs regularization-based training to reduce bias according to the selected metric. Its key advantage is its versatility: it consolidates diverse fairness requirements into a single coherent framework, enabling consistent benchmarking and simplifying practical use. Experiments on real-world tabular and image datasets show that MIFair effectively reduces bias, including previously unaddressed multi-attribute scenarios, while maintaining strong predictive performance across the evaluated settings.

---


### 197. [Shuffling-Aware Optimization for Private Vector Mean Estimation](https://arxiv.org/abs/2604.28032)

**<font color=#1a73e8>作者：</font>** Shun Takagi, Seng Pei Liew  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study $d$-dimensional unbiased mean estimation in the single-message shuffle model, where each user sends a single privatized message and the analyzer only observes the shuffled multiset of reports. While minimax-optimal mechanisms are well understood in the local differential privacy setting, the corresponding notion of optimality after shuffling has remained largely unexplored. To address this gap, we introduce the recently proposed shuffle index and use it to formulate the post-shuffling mechanism design problem as an explicit optimization problem. We then establish a minimax lower bound on the achievable mean squared error in terms of the shuffle index, which implies that mechanisms that are optimal under LDP can become suboptimal once shuffling is applied. Finally, we construct an asymptotically minimax optimal mechanism in the high privacy regime, which as a consequence achieves a privacy-utility trade-off nearly identical to that of the central Gaussian mechanism.

---


### 198. [Ease of dependency distance minimization in star-like structures](https://arxiv.org/abs/2604.28034)

**<font color=#1a73e8>作者：</font>** Emília Garcia-Casademont, Ramon Ferrer-i-Cancho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The syntactic structure of a sentence can be represented as a tree where edges indicate syntactic dependencies between words. When that structure is a star, it has been demonstrated that the head should be placed in the middle of the linear arrangement according to the principle of syntactic dependency distance minimization. However, hubs of stars tend to be put at one of the ends, against that principle. Here we address two questions: (1) How difficult is it to minimize dependency distance? (2) Why anti dependency distance minimization effects have been found in star structures but not in path structures? The ease of optimization is determined by the shape of the optimization landscape. It was demonstrated that the landscape of star structures is quasiconvex (Ferrer-i-Cancho 2015, Language Dynamics and Change). As for (1), here we show that it is indeed convex (a particular case of quasiconvexity) both for star trees and quasistar trees and thus the distance-based optimization problem is simpler than previously believed. As for (2), we argue that (a) competing principles, rather than the difficulty of optimization, must be the actual reason for anti-dependency distance minimization effects and that (b) dependency distance minimization on star-like structures is less rewarding compared to other structures.

---


### 199. [Exponential families from a single KL identity](https://arxiv.org/abs/2604.28036)

**<font color=#1a73e8>作者：</font>** Marc Dymetman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exponential families encompass the distributions central to modern machine learning -- softmax, Gaussians, and Boltzmann distributions -- and underlie the theory of variational inference, entropy-regularized reinforcement learning, and RLHF. We isolate a simple identity for exponential families that expresses the KL difference $\mathrm{KL}(q \| p_{\lambda_2}) - \mathrm{KL}(q \| p_{\lambda_1})$ in terms of the log-partition function $A(\lambda)$ and the moment $\mu_q$. Remarkably, this identity together with the single fact that $\mathrm{KL} \geq 0$ (with equality iff $p = q$) suffices, by direct substitution and rearrangement, to derive a cluster of results that are classically obtained by separate, heavier arguments: a generalized three-point identity for arbitrary reference distributions, Pythagorean theorems for I-projections and reverse I-projections, convexity of the log-partition function, identification of its Legendre dual in KL terms, the Gibbs variational principle, and the explicit optimizer in KL-regularized reward maximization, including the exponential tilting formula underlying entropy-regularized control and RLHF. Beyond these purely algebraic consequences, standard analytic arguments recover the gradient formula for the log-partition function, the Bregman representation of within-family KL divergence, and the surjectivity of the moment map. The note is self-contained.

---


### 200. [Early Detection of Water Stress by Plant Electrophysiology: Machine Learning for Irrigation Management](https://arxiv.org/abs/2604.28038)

**<font color=#1a73e8>作者：</font>** Eduard Buss, Till Aust, Heiko Hamann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose: Fast detection of plant stress is key to plant phenotyping, precision agriculture, and automated crop management. In particular, efficient irrigation management requires early identification of water stress to optimize resource use while maintaining crop performance. Direct physiological sensing offers the potential to detect stress responses before visible symptoms appear. Methods: In this study, we recorded electrophysiological signals from greenhouse-grown tomato plants subjected to water stress and developed a framework based on machine learning for online stress detection. The recorded time-series data were processed using a processing pipeline that includes statistical feature extraction and selection, automated machine learning or alternatively deep learning, and probability calibration. Results: Across multiple input time horizons, we found that a 30-minute look-back window strikes the best balance between rapid decision-making and classification performance. Using automated machine learning, the framework achieved classification accuracies of up to 92%, outperforming deep learning approaches. Sequential backward selection reduced the feature set while maintaining performance. Importantly, the framework detects transitions from healthy to stressed states in recordings that were not included in the training set. Conclusion: Overall, we provide a decision-support tool for farmers and establish a foundation for biofeedback-driven irrigation control to improve resource efficiency in (semi-)autonomous crop production systems.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
