# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-438](./part-09.md)

---

### 351. [Reconfigurable Action Theories: A Formal Foundation for Dynamically Composable Agent Harnesses](https://arxiv.org/abs/2611.12300)

**<font color=#1a73e8>作者：</font>** Jianmin Ji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Action theories typically fix their vocabulary and causal laws, whereas agent harnesses can change their tools, providers, and policies during execution. We introduce Reconfigurable Action Theories (RAT), in which actions can change the action theory itself. A theory module in RAT contains a vocabulary, causal laws, and an initializer. A RAT configuration records the active modules and the world state. Module loading and unloading are represented by actions governed by ordinary causal laws. RAT retains the standard causal action semantics of its language fragment when the active module set is fixed. We give sufficient conditions for at most one next configuration, preservation of existing behavior when a module is added, and equal results when modules are loaded in either order. We establish the computational complexity of reasoning tasks in RAT and translate finite RAT systems into nonmonotonic causal theories and Answer Set Programming (ASP), preserving bounded executions. Experiments compare finite RAT models with executions of official DeepSeek Harness, Pi, and OpenHands implementations. RAT provides a formal basis for checking how component changes affect a harness's available actions, behavior, and reachable goals.

---


### 352. [HumanSightBench: A Benchmark for Human Visual Perception in MLLMs](https://arxiv.org/abs/2611.12305)

**<font color=#1a73e8>作者：</font>** Zixin Su, Yangguang Lin, Zegang Peng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated strong performance on knowledge-intensive and reasoning-based vision-language benchmark datasets, but still struggle to solve the visual questions that people can solve easily. Evaluating the differences between MLLMs and human-level visual perception is challenging due to end-to-end evaluation which combines various skills, or because we are uncertain if individual items are valid. Specifically, observed errors may reflect visual perception, language priors, background knowledge, question ambiguity, and underspecified answers. Our guideline for HumanSightBench is that we construct items that are human-easy by construction and model-hard by evaluation. HumanSightBench contains 2,876 visual questions with short answers across 7 top-level perceptual categories and 21 subcategories. We only include items that pass five inclusion gates: question clarity, answer uniqueness, visual grounding, human solvability, and text-only shortcut filtering. According to the protocol, errors are defined as incorrect answers on human-validated visual tasks with the evaluated interface. The inclusion gates are intended to reduce confounds from ambiguity and external knowledge. The best pass@3 score is 65.6% across eight evaluated MLLMs. No evaluated model exceeds 27.5% on Counting. These results identify capability gaps that are hidden by overall scores and can help future training experiments and held-out evaluation.

---


### 353. [MNN-Pocket-0.3B Technical Report](https://arxiv.org/abs/2611.12311)

**<font color=#1a73e8>作者：</font>** MNN Team  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This technical report presents MNN-Pocket-0.3B, a compact 300M-parameter dense language model designed for efficient on-device deployment and supporting context lengths of up to 32K tokens. With an INT4 deployment footprint of only 173 MB and decoding throughput of up to 466 tokens/s on iPad Pro M5 (Metal), it can be seamlessly integrated into applications on edge devices such as smartphones and smart glasses. MNN-Pocket-0.3B is developed through the co-design of its architecture, data, training pipeline, and inference system. Hardware-aware architecture selection and dependency-aware vocabulary pruning balance model capability with on-device memory and compute constraints. A four-stage pre-training pipeline covering approximately 4.1 trillion high-quality Chinese and English tokens equips the model with broad knowledge and reasoning capabilities. This is followed by a three-stage post-training pipeline comprising instruction fine-tuning, multi-teacher on-policy distillation, and quantization-aware training. Finally, hardware-specific optimizations in the MNN inference engine enable fast, memory-efficient inference and long-context processing. Extensive evaluations demonstrate that MNN-Pocket-0.3B achieves frontier-level performance among models of comparable size, with particularly strong results in Chinese and English knowledge and reasoning, mathematics, coding, and instruction following. It consistently outperforms similarly sized open-source models and even surpasses several 0.5B-parameter models on instruction-following benchmarks. We release MNN-Pocket-0.3B with open weights and ready-to-use MNN deployment packages. We hope it will provide a practical foundation for capable, responsive, and memory-efficient edge applications while advancing research and development in on-device language models.

---


### 354. [AMSchem: Automated Schematic Visualization of AMS Circuits via Verifiable Agentic Generation](https://arxiv.org/abs/2611.12333)

**<font color=#1a73e8>作者：</font>** Yichen Shi, Zhiyuan Wang, Jianing Cui 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For decades, the netlist-to-schematic gap has remained a persistent challenge in design automation, especially for analog and mixed-signal (AMS) circuits. Netlists encode connectivity, not visual presentation, making their manual conversion into readable schematics time-consuming and dependent on expert conventions. The same gap leaves LLM-based design tools without structured visual feedback, forcing them to iterate on circuits they cannot see. We present AMSchem, a training-free, verifier-guided agentic framework that automatically generates human-readable schematics from AMS netlists. AMSchem separates circuit-aware visual planning (DrawingIntent) from executable schematic geometry (SchematicIR), and applies localized visual feedback with bounded, revalidated repair patches. Deterministic validators enforce device preservation, pin-net consistency, and geometric correctness throughout. For evaluation, we construct AMSchem-Bench comprising 64 circuits of 12 types. On the 40-circuit schematic subset, AMSchem with gpt-5.5 achieves 85.0\% validity (vs. 32.5\% direct generation). When integrated as a visual feedback module in LLM-based analog design, AMSchem resolves all 13 previously failed cases from AnalogCoder benchmark across five models, substantially improving the success rate. Our dataset and benchmark are available at this https URL

---


### 355. [From LLM Hallucinations to Inspiration in Creative Work](https://arxiv.org/abs/2611.12337)

**<font color=#1a73e8>作者：</font>** Xinrui Lin, Heyan Huang, Shuning Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can introduce unexpected ideas through hallucinations, yet little is known about when creative practitioners find these errors inspiring or how these judgments shape interactions. We conducted a retrospective qualitative study with 20 experienced practitioners in research, design, and social media content creation, thematically analyzing 41 hallucination cases and 20 semi-structured interviews. Our framework links inspiration judgments of hallucinations based on goal relevance, task stage, content adaptability, and type-specific factors to behaviors across not-inspired, inspired-by, and inspired-to states. We characterize downstream interaction consequences, showing how hallucination-inspired experiences vary across creative stages and reshape role-differentiated trust, and propose these consequences as a dimension of hallucination evaluation. Finally, we derive design recommendations for stage-sensitive control of divergence and adherence, user-defined constraint priorities, differentiated hallucination labels, and salvage support for preserving useful ideas while correcting errors. These contributions deepen HCI understanding of hallucinations and responsible LLM design in creative work.

---


### 356. [TMT: Adapting CLIP to Infrared Imagery via Text-Derived Modality Knowledge Transfer](https://arxiv.org/abs/2611.12345)

**<font color=#1a73e8>作者：</font>** Ruofan Wang, Puzuo Wang, Xin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP achieve strong performance across computer vision tasks, yet their image-text alignment is less reliable for infrared (IR) imagery because large-scale pre-training is dominated by visible-spectrum data. Due to the high cost of the infrared-text labeling, we investigate adapting CLIP to IR through only paired infrared-visible images, which requires considering modality-specific knowledge while preserving scene content and CLIP's image-text alignment. To achieve this, we propose TMT (Text-Derived Modality Knowledge Transfer), which adapts CLIP's image encoder through a text-defined infrared-to-visible direction and supervision from paired IR-visible images. First, we found that modality discrepancy can be described by corresponding text embeddings, thus using the direction of text embedding differences to guide the knowledge transfer between visible and infrared modalities without erasing infrared-specific information. To enhance the representation of semantics and details of infrared images, we introduce Generative-Perceptual Co-Supervision that combines semantic alignment from CLIP visible image encoder with diffusion noise-prediction feedbacks. On four source-disjoint IR classification benchmarks, TMT achieves the highest mean zero-shot accuracy among the compared methods (48.92%). It also achieves the best IR-text retrieval results among the compared methods without infrared-text supervision during adaptation and the highest open-vocabulary segmentation mIoU on both CART and SemanticRT among the CLIP-like methods.

---


### 357. [QCC-WM: Linking Macro-State Dynamics and Visual Generation via Quotient Causal Construction](https://arxiv.org/abs/2611.12353)

**<font color=#1a73e8>作者：</font>** Zhizhong Fu, Wei Zhou, Zhaoyang Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key challenge in action-conditioned world modeling is to construct macro-states from high-dimensional observations that support recursive prediction under actions, while keeping their predicted evolution consistent with visual changes in generated observations. We propose QCC-WM, a visual world model based on Quotient-based Causal Construction. QCC-WM uses action responses to guide macro-variable construction for recursive action-conditioned prediction. A shared reference quotient measurement constrains the consistency between predicted states and observed changes, allowing macro-level predictions to provide structured constraints for future visual generation.
Using translational and rotational actions and their predicted responses, the model aggregates local visual features into macro-nodes with spatial correspondence through causal abstraction, and recursively predicts node content and motion under a shared reference measurement. Macro-level predictions guide future observation generation, while predicted motion transports historical appearance information. Node-level errors between generated observations and macro-level targets are then mapped back to the corresponding spatial regions for correction, improving consistency between visual generation and macro-level predictions.
On the US-VLA dataset, QCC-WM achieves an ROI-MSE of 0.01861 for four-step prediction. Compared with the best baseline at each prediction horizon, it reduces LPIPS by 48.59%, 41.68%, and 30.23% for four-step prediction and eight- and sixteen-step recursive extrapolation, respectively. Ablation studies and mechanism analyses show that motion-guided reference transport mainly improves pixel reconstruction, while node-level error feedback further improves perceptual quality and consistency between generated observations and macro-level predictions.

---


### 358. [DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees](https://arxiv.org/abs/2611.12356)

**<font color=#1a73e8>作者：</font>** Zhicheng Zheng, Cheng Zhang, Chenkai Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding speeds up language models by letting a lightweight drafter propose several future tokens that the target model verifies in parallel. Block diffusion drafters such as DFlash draft a whole block in one forward pass, and DDTree builds a draft tree from their per-position distributions. Each of these distributions assumes that the drafter's own most likely continuation is correct. A tree, however, gains over a chain only on branches that leave this continuation, where the drafter's top-1 accuracy drops from 89% to 18% and its candidate lists miss the right token far more often. When re-run from the fork token, the same drafter is usually correct, so the errors come from the prefix that the distributions condition on rather than from what the drafter knows. We introduce DForkTree, a training-free method that re-anchors each branch on its own tokens. DForkTree adds n-gram statistics from the target model's own outputs to the drafter's scores as pointwise mutual information, weights them more after the fork, and builds the optimal tree under these scores exactly on the GPU. On Qwen3.5-4B and 9B, with all tree methods sharing one drafter, tree pipeline and verifier, DForkTree is the fastest tree method on every benchmark. It is up to 41.5% faster than DFlash and 15.1% faster than DDTree in the same setting, with average speedups of up to 4.75x over autoregressive decoding.

---


### 359. [TANSAR: Editable and Attributable Correlation Matrix Memories under Correlated Keys, with Rule-Constrained Multi-Hop Knowledge Editing](https://arxiv.org/abs/2611.12374)

**<font color=#1a73e8>作者：</font>** Abdulhady Abas Abdulla, Jiyan Salim Mahmud, Fatemeh Daneshfar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Correlation Matrix Memories (CMMs) store associations as sums of rank-one outer products, providing closed-form addressability, exact deletion, and linear attribution. While classical analyses assume random, orthogonal keys, semantic encoders produce correlated representations. We analyse CMMs under correlated keys using frame-theoretic coherence: (i) capacity bounds yielding an encoder-independent limit $n \le d(1+\varepsilon^2)$ for mean squared crosstalk $\varepsilon^2$; (ii) an exact characterisation of the collateral effect of deleting an association, guaranteeing that deletion never invalidates certified associations; and (iii) a geometric transparency bound demonstrating why attribution requires candidate sets of centred keys. On this basis, we introduce Topology-Aware Neuro-Symbolic Associative Retrieval (TANSAR). TANSAR traverses a directed acyclic association graph, prunes invalid paths via sound ground Horn constraints, and injects a representation derived strictly from the verified path into the residual stream of a frozen language model, guarded by a Clopper--Pearson selective-risk gate. Controlled experiments confirm all theoretical bounds. In multi-hop knowledge editing, Horn pruning reduces answer contradictions from 25.1% to 0.5%, whereas Hopfield retrieval incurs 24% contradictions when stale associations remain stored (and 0% if stale associations are removed). An end-to-end edit transaction requires 13.6 ms on a standard CPU and 2.37 ms on GPU. The symbolic component matches gold labels across all 600 ProofWriter theories and achieves 94.0% agreement on FOLIO, demonstrating sound and efficient multi-hop associative retrieval with exact unlearning.

---


### 360. [Detecting Shadow AI: Unsanctioned LLM Agents on Enterprise Endpoints: A Taxonomy, an Open Detector and a Controlled Evaluation](https://arxiv.org/abs/2611.12377)

**<font color=#1a73e8>作者：</font>** Jeremy Canale, Fabien Soulis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shadow IT, the use of technology that the IT organisation has not approved, is a long-standing governance problem. We argue that autonomous AI agents can make it grow much faster: agents make building tools nearly free, act with their user's privileges, and leave behind scripts, automations and MCP servers that are themselves unsanctioned. A simple compounding model shows that, under its assumptions, shadow IT grows exponentially once agentic artifacts reproduce faster than the organisation retires them; retiring them starts with detecting them. We then ask whether unsanctioned agents can be detected on Windows endpoints. We propose a taxonomy of nine classes of agents and six layers of endpoint footprint, and argue that rules based only on the structure of processes and connections cannot separate an agent from its behavioural twin, the same program talking to a non-AI service. We present Agent Detector, an open-source Windows detector that anchors behaviour to the identity of the remote service and correlates it with configuration, installation and execution history, using a catalog of 39 tools and 184 LLM endpoint entries; it informs users through a notice they must acknowledge instead of blocking. On a controlled bench of 12 synthetic agents, 3 AI components and 9 benign workloads, repeated 5 times on one workstation, two behavioural rules flagged every behavioural twin, while Agent Detector flagged none and detected every agent in the majority of runs. Its limits are temporal: a connection to a provider behind a shared content-delivery network is attributable only while the DNS cache holds the provider's name, one to five minutes, and an intermittent agent was seen by about one scan in three. A scan costs about 154 ms. The bench is too small to rank detectors; it maps what each kind of evidence can see: unsanctioned agents can be partly detected, and not by behaviour alone.

---


### 361. [Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks](https://arxiv.org/abs/2611.12386)

**<font color=#1a73e8>作者：</font>** Dario Pasquini, Reworr, Giuseppe Ateniese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the fingerprinting of agentic cyberattacks. Our objective is to reliably infer information about the attacker's configuration, such as LLM version and harness, from telemetry. To achieve this, we introduce a technique we call shibboleth traps: modular honeypot services designed to elicit discriminative behaviors from agentic attackers. The traps make informative interactions a condition for obtaining resources the agent seeks, eliciting model declarations and characteristic writing without requiring a successful prompt injection.
To achieve harness fingerprinting, we introduce general mechanisms to indirectly probe peculiar execution behaviors of harnesses. These probes reveal how a harness masks secrets in tool output, enforces command time limits, and schedules tool calls, using only the effects visible in subsequent requests.
We show that combined declarative and behavioral inference distinguishes among 15 candidate models with an average 90% top-1 accuracy, with behavioral classifiers evaluated on held-out harnesses or task families. In a separate experiment across four harnesses, fixed probe rules identify the correct harness with 92% accuracy. When instructed to conceal their identity, agents still leave useful behavioral evidence even as their declarations become uninformative.

---


### 362. [More Than Just Style: Benchmarking Personality Influence in Large Language Models](https://arxiv.org/abs/2611.12392)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Mengyu Wang, Xiao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In addition to the effects of explicit input prompts and instructions, large language model outputs are influenced by underlying behavioral preferences similar to human personality tendencies. These tendencies can affect how models interpret situations and make decisions. However, their influence is difficult to disentangle from the effects of model capabilities and instructions. Therefore, we introduce SPACE, a benchmark framework combining a controlled evaluation protocol with complementary datasets for personality verification, capability assessment, and hierarchical situational tasks. Controlled comparisons across guidance conditions help distinguish personality influence from measured capability changes and immediate instruction effects. Experimental results demonstrate that although prompting can shift generation style, models' internal personality tendencies are persistent and not readily overridden by opposing instructions. Furthermore, these underlying tendencies have an observable influence on LLM task performance, highlighting the need for greater attention to these characteristics and potential applications. Training code and SPACE benchmark specifications are available at this https URL.

---


### 363. [AutoBuddy: Evaluating Proactive, Always-On Agents on Task Discovery and Execution in a Simulated Workplace](https://arxiv.org/abs/2611.12393)

**<font color=#1a73e8>作者：</font>** Shiqi Chen, Daniel Madrigal Diaz, Wei-Ning Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents become more autonomous, they are increasingly expected to run as always-on assistants on a user's behalf, identifying work to be done and completing it without being asked. Yet existing benchmarks usually give the agent its task, whereas in knowledge work the requests sit in the user's workspace and the agent must first recognise which obligations exist. We study proactive task discovery and execution, in which an agent must infer a user's pending tasks from their workspace and complete them in the systems where the work lives. This setting poses two challenges. For the agent, the tasks are buried in a large volume of mail, chat, documents and records. For evaluation, a benchmark needs a simulated organisation whose people, events and documents are mutually consistent, so that tasks arise realistically and their correct outcomes are known. We introduce AutoBuddy-Bench, a simulator that addresses these challenges. It models an organisation's employees, projects, business systems and event history as a temporal graph, renders it into realistic workspace artefacts, derives ground-truth tasks from the events that create obligations, and computes each task's outcome from the world state; execution is judged by the agent's changes to the workspace. To evaluate current LLMs, we build AutoBuddy, a reference agent with interchangeable backbone LLMs: it identifies tasks from the workspace, grounding each in its source records, and executes each in a separate session with write access. Varying only the backbone, we find a systematic shift in where tasks are lost: weaker models fail mainly at discovery, intermediate models identify tasks but often stop short of carrying them out, and the strongest models fail mainly during execution, most often on business-system operations. Discovery precision is only weakly related to execution quality, suggesting the two are distinct capabilities.

---


### 364. [BDBBQ: A Human-AI Collaborative Benchmark for Bengali Social Bias in LLMs](https://arxiv.org/abs/2611.12407)

**<font color=#1a73e8>作者：</font>** Provat Saha, Ashika Habib Khan, Tahseen Tanha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite growing attention to social bias in large language models (LLMs), existing bias benchmarks provide limited coverage of culturally grounded evaluation in Bengali, particularly within Bangladesh's sociocultural context. To address this gap, we develop a bilingual extension of BanglaBBQ comprising 61,312 question-answering instances across 12 social categories in English and Bengali. The benchmark incorporates balanced answer permutations, contrasting question framings, and both ambiguous and disambiguated contexts to systematically examine model performance and stereotype-aligned bias across languages. We validate the dataset through structural checks, 220 statistical tests, and expert annotation of 150 instances by four annotators, achieving strong inter-annotator agreement (Fleiss' \k{appa}=0.8349). We evaluate eight LLMs across 490,496 instances and identify five key findings. First, disambiguated contexts yield substantially greater accuracy improvements in Bengali (+36.59 percentage points) than in English (+17.71). Second, all evaluated models exhibit lower accuracy in Bengali, although Mistral-Nemo shows the smallest cross-lingual accuracy gap (5.12 percentage points). Third, stereotype-aligned bias exhibits language and model dependent variation, increasing in Bengali for Gemma 2 9B but decreasing for Mistral-Nemo. Fourth, higher accuracy does not necessarily correspond to lower stereotype-aligned bias. Finally, bias varies considerably across social categories, with Qwen 2.5 7B exhibiting stronger stereotype alignment in Bengali for Politics and Physical Appearance. These findings demonstrate that cross-lingual performance and social bias are distinct dimensions of LLM behavior and underscore the importance of culturally grounded, language-sensitive benchmarks for evaluating fairness beyond English-centric settings.

---


### 365. [Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension](https://arxiv.org/abs/2611.12412)

**<font color=#1a73e8>作者：</font>** Pekka Abrahamsson, Muhammad Waseem, Esa Karjalainen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Coordination between large language-model agents has become a central question for AI safety and software engineering, as such agents are deployed in groups that share infrastructure. Existing research tells the agents that partners exist or asks them to coordinate. Whether coordination arises through shared state alone, with nothing disclosing that anyone else is present, is the key question for deployments that share caches and memory between agents, yet it has rarely been examined, and never with independent replication; this study does both. Four agents each received a short arithmetic task and a key-value store presented to each as its own scratch space; two held complementary halves of one computation, and no prompt mentioned other agents, sharing or collaboration. For reliability, the environment was rebuilt independently from a written protocol, and both implementations ran under hashed locks on design, data and analysis. The results bear novelty value in three respects. Joint success occurred only through the shared store. Whether a model coordinated depended not on its vendor tier but on whether it wrote its intermediate result and looked at the store again, and one ordinary sentence, "check your workspace again before submitting", switched that second look on and off. The findings held under replication. For practice, state shared between agents is a communication channel and should be separated, namespaced and logged. For research, designs should be locked before the data, and the parse rule, endpoint and parameters reported. Future work should test open-weight models and separate using another agent's output from intending to communicate.

---


### 366. [Path-Level Structural and Semantic Alignment for Hierarchical Multi-Label Text Classification](https://arxiv.org/abs/2611.12420)

**<font color=#1a73e8>作者：</font>** Xindi Wang, Aifen Xiong, Baiyang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hierarchical multi-label text classification (HMTC) requires models to capture both structural dependencies among labels and the fine-grained semantics of labels at different hierarchy levels. Existing methods often model hierarchy through prediction constraints or representations of individual labels and local relations. Structural and semantic supervision, however, are usually formulated separately. We instead use complete root-to-node label paths as a shared unit for both. Our framework introduces two auxiliary training objectives while retaining a standard multi-label classifier at inference. PathSimNCE aligns document representations with hierarchical paths using hierarchy-aware contrastive targets. These targets provide graded supervision for structurally related paths while preserving explicit supervision for the ground-truth paths. The complementary semantic objective uses LLM-generated, document-conditioned descriptions of the same positive paths. It thereby provides context-specific label semantics beyond static label representations. Experiments on three benchmarks show consistent improvements: structural alignment is particularly beneficial in deeper hierarchies, while semantic alignment provides additional gains for fine-grained labels.

---


### 367. [dNaViT: Discrete Codes are General-Purpose Visual Representations](https://arxiv.org/abs/2611.12426)

**<font color=#1a73e8>作者：</font>** Xiaotong Li, Zhengrong Yue, Xu Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete autoregressive modeling, notably through next-token prediction, has become a cornerstone of modern language models. Extending this paradigm to vision allows visual and language models to converge on a unified framework, thereby fostering shared methodology and infrastructure. This work investigates a central question: how far can a finite discrete vocabulary go in representing the richness of the visual world? We present dNaViT, a Discrete Native-resolution Vision Transformer that produces discrete visual primitives analogous to language tokens. Built upon a frozen pretrained encoder, dNaViT applies lightweight residual modulation with a dual-branch objective to inject reconstruction-aware cues into semantic features. By leveraging grouped product quantization, it scales discrete capacity without inflating spatial sequence lengths, while a balanced training recipe maintains both semantic and pixel-level information. Consequently, dNaViT functions as a versatile discrete visual tokenizer, enabling unified encoding across downstream tasks alongside high-fidelity image decoding. Extensive evaluations show that dNaViT matches or exceeds task-specific baselines across 12 visual understanding benchmarks, 4 generation benchmarks, and an image editing benchmark. These findings demonstrate that a compact discrete vocabulary can serve as a universal visual currency and unlock the full potential of fully unified, native multimodal methodology.

---


### 368. [LongSCOP: Semantically Consistent Long Video Outpainting](https://arxiv.org/abs/2611.12445)

**<font color=#1a73e8>作者：</font>** Yu Tang, Zhiyuan You, Zhixiao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video out-painting is an important problem, yet existing research focuses primarily on short clips, leaving long video out-painting largely underexplored. Extending video out-painting to long videos poses substantial challenges. A natural solution is iterative out-painting, i.e., generating videos chunk by chunk, but this introduces two major issues: generation instability or even failure caused by inter-chunk inconsistencies and error accumulation, and semantic drift over long temporal horizons. In this paper, we propose LongSCOP, short for Semantically Consistent long Video Out-Painting. First, we introduce a training recipe with three components for smooth and stable long-horizon generation: self-forcing training, latent calibration, and future references. Beyond generation stability, we recognize that the rich temporal context of long videos provides valuable references for maintaining semantic consistency. We therefore develop a VLM-based agent that automatically selects the most informative reference frames from the entire video to maintain consistent subjects, scenes, and backgrounds throughout long-horizon generation. We also construct a high-quality training dataset of 62K video clips. To facilitate research on this underexplored problem, we introduce LVO-Bench, a benchmark curated by human experts to assess long-horizon stability and semantic consistency. Extensive experiments demonstrate that our method outperforms existing approaches in both generation stability and semantic coherence.

---


### 369. [Phrase-Level Speculative Decoding on a Frozen Target](https://arxiv.org/abs/2611.12464)

**<font color=#1a73e8>作者：</font>** Madhusudhana Naidu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoders raise throughput by banking more target tokens per forward pass, and Medusa, EAGLE-3, DFlash and DSpark all do it the same way: more candidates that survive verification. All of them draft in the target's own vocabulary, so one node of the candidate tree is one target token, and the tokenizer makes that unit look like a constant. It is not. BPE's pretokenizer splits on whitespace before merges are learned, so no multi-word string can ever become a single token: in Qwen3-4B, "United States of America" is four tokens and no adjacent pair of them exists as one entry, so a phrase is out of reach of any method drafting in the target's vocabulary.
We change the unit. A small MLP head reads the frozen target's hidden state and predicts a one- to three-word phrase as one entry in a separate draft vocabulary; greedy longest-match expansion maps it back into the target's own tokens, and N candidates are verified in one forward pass behind a prefix-tree mask, so the change is orthogonal to tree depth and width. The target and its tokenizer stay frozen and a candidate is accepted only while it matches the target's own argmax, so the served output is identical to greedy decoding up to floating-point tie-breaking.
On one A5000 at batch 1, against HuggingFace generate(), a 21.94M head (0.545% of Qwen3-4B) reaches 2.391x on GSM8K, 2.444x on MATH-500 and 1.544x on MT-Bench. Because the head's output layer is one row of 257 parameters per entry, the draft vocabulary size is the parameter budget: an 8,000-entry head is 3.434M parameters, 0.0854% of the target and 64x smaller than EAGLE-3's drafter, and keeps 92.3% of the larger head's GSM8K tokens per pass. With EAGLE-3 run on same prompts and baseline, our 21.94M head is ahead of tree-16 on both maths sets and behind tree-60 on every set.

---


### 370. [AuDiR: Diagnosing Audio Reasoning with Rule and Percept Interventions](https://arxiv.org/abs/2611.12478)

**<font color=#1a73e8>作者：</font>** Chengwei Wei, Yi Ma, Nancy F. Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Answer accuracy alone does not distinguish failures in acoustic perception, rule knowledge, and rule application. AuDiR (Audio Diagnostic Reasoning) examines these distinctions through controlled input interventions. Each item contains an audio clip, a multiple-choice question, a task-general rule, and a textual description of the acoustic observations needed to answer. Three conditions progressively supply the rule and observations; a fourth removes the audio while retaining the question and rule. The first correct diagnostic condition assigns an operational response label, without identifying a unique internal cause. The current benchmark contains 201 items in 18 families drawn from 9 sources, with answer references documented separately from percept extraction. In a preliminary evaluation of Gemini-3.8-flash, accuracy is 29.3% without supplied information, 31.3% with the rule, and 98.5% with the observations also supplied. No-audio accuracy is 23.9%, with a confidence interval containing the 25.0% chance rate. A family-level knowledge probe associates incomplete rule recall with larger gains from rule provision. These results show the benefit of supplying acoustic observations as text, while incomplete validation, possible recognition shortcuts, and non-monotonic responses limit stronger failure-attribution claims.

---


### 371. [Detecting AI-Authored Text in Authentic Student Writing: Evidence from PISA 2025](https://arxiv.org/abs/2611.12487)

**<font color=#1a73e8>作者：</font>** Nils-Jonathan Schaller, Thorben Jansen, Olaf Köller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-text detectors reach near-perfect scores in evaluations that contrast fully human-written texts with texts generated from researcher-designed prompts. In authentic student writing, however, AI use is voluntary and often partial. We study this setting with the PISA 2025 FLA dataset, in which 15-year-olds in Germany wrote English argumentative essays with and without access to a gpt-4o-mini-based chatbot. Keystroke, clipboard and chat logs let us trace every character of the final essay to its origin. From this provenance, we derive text- and sentence-level labels for human-written, AI-generated and mixed text, and for text written after chatbot use without traceable AI material. We evaluate a feature-based detector and a classifier on frozen Llama-3.1-8B embeddings, both adapted from top-ranked shared-task systems. Both separate AI from human text reliably (macro-F1 up to 0.96 for texts and 0.95 for sentences), independently of spelling errors. The feature-based detector, however, relies on lexical complexity, which a simple student-style rewriting prompt removes (AI recall 0.92 $\to$ 0.60 with gpt-4o-mini, 0.41 with Qwen3). The embedding-based detector stays robust for whole texts (AI recall $\geq$ 0.94) but not for single sentences (AI recall as low as 0.59). Mixed text falls between the two classes, and text without traceable AI material is classified as human-written in about 95\% of texts.

---


### 372. [EditJudge-Bench: Auditing VLM Image-Edit Judges with Synthetic Ground Truth](https://arxiv.org/abs/2611.12524)

**<font color=#1a73e8>作者：</font>** Jens Parslov, Marco Schouten, Dim P. Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used as automated judges for image-editing benchmarks, yet their reliability is poorly understood. Auditing these judges is difficult because real edited images lack controlled ground truth and entangle the requested changes with model artefacts, unintended side effects, and ambiguous degrees of success. In this paper, we introduce EditJudge-Bench, a diagnostic benchmark of 1,382 synthetic before/after image pairs rendered in Blender, with edits parameterised across nine categories derived from real user requests and exact ground truth from known 3D scene parameters. Because every edit is generated by a known intervention on a controlled scene, EditJudge-Bench evaluates VLM judges as binary verifiers of whether an instruction was correctly executed, isolating judge perception from editor quality. Across 25 judge configurations, we find substantial reliability gaps: (a) the widely adopted VIEScore template reaches only 69.0% AUROC with GPT-4o; (b) fine-tuned judges score 51.7-66.3%; spatial edits such as rotation and shape remain challenging; (c) prompt-formatting choices like image-text ordering shift performance by up to 14.1 points. Despite using only synthetic data, judge rankings on EditJudge-Bench correlate strongly with two real-image human-preference benchmarks ($\rho$=0.95 and $\rho$=0.71), indicating that controlled audits surface failure modes relevant to real evaluation.

---


### 373. [Language Defaults Before Content: A Causal Layer Map of Multilingual Generation](https://arxiv.org/abs/2611.12538)

**<font color=#1a73e8>作者：</font>** Shenbin Qian, Yves Scherrer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual generation requires large language models (LLMs) to determine both what to say and in what language to say it, yet these two commitments are difficult to disentangle from model outputs alone. We use translation as a controlled probe: for multi-parallel segments that a model translates well in one language direction but poorly in another, content is held fixed while language varies. Using activation patching, we write residual-stream states from successful runs into failing ones and compare content-matched states with content-independent controls, allowing us to trace content-specific and language-related signals across layers. Across three LLMs of different scales and architectures, we find a consistent three-stage pattern of multilingual generation. Intermediate layers first express a default English signal; content information becomes causally available one layer later; and the final target language is resolved only at later layers. The ordering of the English default before content also appears in a reading-comprehension task. Our sparse autoencoder analyses reveal a further dissociation: the intermediate language signal is only weakly represented by sparse features, whereas a later language distinction is clearly sparse, but resists intervention at the patched position. These results provide a mechanistic account of how language selection and content information emerge and interact during multilingual generation.

---


### 374. [SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery](https://arxiv.org/abs/2611.12552)

**<font color=#1a73e8>作者：</font>** Weimin Wu, Han Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose SciMARS, a framework for recursive task-local adaptation of multi-agent harnesses in closed-loop scientific discovery. Multi-agent systems coordinate analysis, experimental design, and verification as scientific evidence evolves. However, two problems limit their effectiveness: (i) without shared memory, agents lose observations and repeat work; (ii) fixed role procedures, handoffs, and memory policies perpetuate mistakes despite retained evidence. We address these problems with a shared evidence graph and separate component editors. SciMARS adapts roles and coordination; SciMARS + Memory adds a third editor for how agents record, retrieve, and receive evidence. Candidate probes guide composition and selection of the next harness. We evaluate scientific discovery through experimental-data replay and a digital twin. SciMARS + Memory resolves 12/18 GPT-6-Astra and 2/18 GLM-5.3 attempts on Autonomous Science Bench, compared with 8/18 and 1/18 for the base multi-agent team. On ScienceAgentBench and AppWorld, it solves 14/38 and 11/20 tasks, compared with 11/38 and 5/20 for the base team. These results support combining shared memory with harness adaptation across scientific and interactive tasks.

---


### 375. [GHiML: VLM-Guided Hierarchical Multi-Label Learning with Applications to Benthic Imagery](https://arxiv.org/abs/2611.12564)

**<font color=#1a73e8>作者：</font>** Isaac Xu, Devi Ayyagari, Martin Gillis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) encode substantial expert knowledge within their weights, yet their direct application to specialised classification domains such as benthic imagery remains limited. Meanwhile, vision transformers trained on these tasks rely predominantly on low-level visual latents (colours, textures, and shapes) that lack the higher-level reasoning humans employ for identification. We propose Guided Hierarchical Multi-Label (GHiML) learning, a pipeline that extracts conceptual latent variables from a VLM conditioned on training data, generates sample-relevant captions grounded in those variables, and fuses the resulting textual embeddings with image embeddings via cross-attention and a per-node gated router. We also introduce the inverted HML score ($d_{\mathrm{inv}}$), a similarity score that evaluates hierarchical multi-label predictions through graph traversal distance and a cardinality penalty, providing an interpretable alternative to existing measures, which are insensitive to realistic degradations in sparse, deep hierarchies. Experiments on BenthicNet, FathomNet and iNaturalist show that the router improves macro $F_1$ over the vision-only baseline by up to 6.7 pp and $d_{\mathrm{inv}}$ by up to 21.1 pp on in-domain benthic data, with gains persisting under distribution shift. Ablations locate the contribution of the text itself: on the multi-label biotic hierarchies, removing the per-sample text signal degrades $d_{\mathrm{inv}}$ while leaving macro $F_1$ unchanged, consistent with text acting through prediction cardinality rather than node discrimination, whereas iNaturalist, whose annotations are single-label, loses 18.7% of macro $F_1$. Our results support the hypothesis that VLMs contain exploitable specialised knowledge that, when appropriately elicited, can augment classification in domains where direct visual learning is insufficient.

---


### 376. [Text2NGAC: a multi-LLM pipeline for NGAC policy extraction with mutation-based verification](https://arxiv.org/abs/2611.12572)

**<font color=#1a73e8>作者：</font>** Ayesha Habib, Huixiang Zhang, Dan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Access-control policies are written in natural language but enforced as formal models, and translating them into NIST Next Generation Access Control (NGAC) graphs remains unsolved: prior systems cover only subsets of the NGAC model, and none verify the graphs they extract. We present Text2NGAC, a pipeline of cooperating large language models that disambiguates each sentence before extraction, escalates uncertain sentences to a multi-model ensemble, and checks the resulting graph with a five-strategy verifier whose own effectiveness is measured by controlled mutation testing. To our knowledge it is the first system to extract all four NGAC relationship types - associations, prohibitions, event-response obligations, and assignments - from real-world policy documents. Three results anchor the evaluation. The verifier detects 99.7% of 918 injected mutants and every structural fail-open fault, and the fault classes it misses are characterized and weighted by security consequence rather than left unexamined. The extracted graphs are enforceable: one corpus's graph loads unmodified into the NIST reference implementation, which reproduces all 55 access decisions the graph entails and fires an extracted obligation end-to-end. Extraction reaches 97.3-99.6% exact-tuple-match accuracy on the 714 scored sentences of four real corpora, far above three reproduced baselines on matched metrics, and paraphrase probes with semantic re-scoring bound the pipeline's sensitivity to rewording. Reported accuracy is wording- and benchmark-specific, adversarial input is outside the verifier's guarantees, and the intended deployment is extraction plus structural verification feeding expert review. A complete two-tier reproducibility artifact accompanies the paper.

---


### 377. [Evaluating Cross-Signal Coherence in Mammography Vision-Language Models](https://arxiv.org/abs/2611.12574)

**<font color=#1a73e8>作者：</font>** Rebeca Nam, Chase M. Fensore, Christian A. Fauria-Robinson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision-language models (VLMs) move toward interpreting medical images directly, their outputs increasingly include not just a label but a stated confidence and a written justification. Yet the field still predominantly evaluates VLMs using just accuracy. We evaluate the coherence between answer, confidence, and explanation across four VLMs on breast density and BI-RADS categorization, using two mammography datasets. We perform controlled perturbations of the question, multiple choice option orders, and the images and assess changes in the three outputs. Our results suggest confidence does not decrease even as the mammography image is changed. Shuffling the options also changes most VLMs' answers. Notably, there are cases where a model's own stated reasoning contradicts its final answer, a distinction accuracy alone cannot capture but one that governs whether an AI-generated answer can be trusted.

---


### 378. [AgentOPSD: Turn-Level Credit Assignment via Recursive Belief Revision](https://arxiv.org/abs/2611.12587)

**<font color=#1a73e8>作者：</font>** Yizhuo Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards ordinarily spreads a single advantage over a whole trajectory, a granularity too coarse to isolate the few decisions on which success in a long, multi-turn interaction actually turns. Privileged self-distillation supplies denser supervision, but it leaves unanswered how a set of local teacher-student discrepancies should be converted into credit along a sequence. We introduce AgentOPSD, a critic-free scheme that assigns credit recursively, one interaction turn at a time. Inside a turn, the token-level log-probability gaps between a skill-conditioned self-teacher and the student are summed, and that sum acts as evidence in a recursive Bayesian update carried out in log-odds space; the resulting revisions reallocate the outcome-derived advantage across turns through a multiplier that is bounded and preserves its sign. With Qwen2.5-3B and Qwen2.5-7B as policy backbones on ALFWorld, the method improves consistently on GRPO and on self-distillation baselines, and attains 89.1% success at the 7B scale. Ablations attribute the gain to aggregating evidence at turn boundaries and to making the belief revision depend on history, rather than to the local gap by itself.

---


### 379. [Fairness in Explainable AI Narratives: Decomposing Social Disparities in LLM-Generated Explanations](https://arxiv.org/abs/2611.12592)

**<font color=#1a73e8>作者：</font>** Wannes Van den Bulck, Sofie Goethals, David Martens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to translate technical explainable AI (XAI) artefacts such as SHAP into explanatory narratives (XAINs) for lay users. In high-risk domains, these explanations are often the main resource through which individuals can understand and contest adverse decisions. Yet LLMs are known to reproduce social bias, even from proxy variables alone, and fairness in XAINs remains unstudied. Because XAINs are bound to a ground-truth artefact, fairness concerns not only what a narrative says and how, but also whether it is equally faithful across social groups. We introduce fairness in XAINs as a new field of research and propose a framework that generates narratives under three conditions (protected attribute disclosed, withheld, or counterfactually swapped), allowing five comparisons that pinpoint the cause of disparities. We apply it to adversely classified instances from four datasets in credit scoring, education and employment, generating narratives with five LLMs, and evaluate faithfulness, feature coverage and sentiment. We find significant disparities across all datasets, metric families and models, arising in two ways. Faithfulness disparities result from feature values: LLMs make plausible but false statements, triggered by values that are unequally distributed across social groups. Feature coverage and sentiment disparities stem from the protected attribute itself: once it is disclosed, LLMs give less explanation to, or frame more negatively the narratives of, groups that have historically been discriminated against or are stereotypically associated with worse outcomes. A more faithful model removes the faithfulness disparities, and withholding protected attributes mostly removes the others, but neither suffices on its own. Fairness in XAINs should therefore be audited separately from the predictive model and its XAI artefact.

---


### 380. [Double Blind Evals: Resolving the Dual Confidentiality Dilemma in AI Safety Auditing](https://arxiv.org/abs/2611.12604)

**<font color=#1a73e8>作者：</font>** Andrew Trask, Sol Messing, Vai Pahwa 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI safety evaluations often involve sensitive prompts and proprietary models. Evaluators want to keep their evaluation prompts secret from model owners to prevent purposeful or incidental data leakage, ensuring longer usefulness of their benchmark. Model owners in turn wish to keep their proprietary model weights and inference code within their own secure infrastructure to protect their IP. We present a way forward for "double-blind evals", which provide cryptographic guarantees that an evaluator's prompts are not shared with the model owner, while simultaneously maintaining the confidentiality of the model weights and inference code. To accomplish this, we use secure enclaves that encrypt data in RAM at the hardware level. In a world-first pilot, we test this approach by evaluating a proprietary Google DeepMind model (Gemini 2.5 Flash Lite) against a selection of the private AILuminate benchmark corpus, using an NVIDIA H100 secure enclave on Google Cloud Platform, and using OpenMined's PySyft to maintain data and model privacy. We believe this effort marks the first use of this technology to provide mutual secrecy for one organization's frontier-class proprietary model weights and another organization's closed benchmark.

---


### 381. [Creative Intent as an Evolving Shared State: Supporting Cross-Stage Human-AI Video Co-Creation](https://arxiv.org/abs/2611.12605)

**<font color=#1a73e8>作者：</font>** Yuhang Jin, Mengfei Chen, Hanwei Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI becomes increasingly involved in video creation, creators face challenges in expanding, translating, and negotiating creative intent across stages. We therefore view creative intent as an evolving shared state throughout human-AI co-creation. A multi-stage design was employed: semi-structured interviews with 12 creators informed 3 design goals, followed by expert co-design and the development of VideoMaker. VideoMaker organizes creation into a six-stage workflow that progressively translates creative intent. At key stages, creators negotiate with AI through the Seed Panel, explicitly confirming, revising, and updating intent. A shared AI Agent, supported by the Multi-style Script Library and Cinematic Language Knowledge Base, enables differentiated expansion of initial intent and faithful translation. A within-subjects study with 30 participants showed that VideoMaker effectively supported the expansion and cross-stage translation of creative intent, with stronger intent preservation, while negotiated boundaries between creator-confirmed intent and AI initiative remained difficult to sustain.

---


### 382. [Adapting Small Language Models to Romanized Nepali: Tokenizer Fertility, Reference Likelihood, and Generation Metrics](https://arxiv.org/abs/2611.12628)

**<font color=#1a73e8>作者：</font>** Pujan Pant, Sagar Newpane, Hari Sitaula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Romanized Nepali, Nepali written in Latin script, is common in digital communication but has no standard spelling and few resources, and it is unclear how reliably small open language models can be adapted to it. We adapt three 2-3B base models from different families, Llama-3.2-3B, Qwen2.5-3B, and Gemma-2-2B, with QLoRA on 9,000 instruction examples produced by deterministic transliteration of Nepali instruction data. Each model is trained with one shared recipe and three seeds and evaluated on 1,000 held-out examples with reference-overlap metrics, byte-normalized reference likelihood (bits per byte, BPB), and an output audit, against zero-shot baselines under two prompts. Fine-tuning raises chrF++ from 10-14 to 29.0-30.6 and lowers BPB from 2.23-2.41 to 0.78-0.84; most zero-shot outputs (54-92%) are English-like. Likelihood and overlap disagree on how far apart the models are. Llama-3.2-3B has the lowest BPB in every seed, 0.042 below Qwen2.5-3B (95% CI 0.039-0.046), yet the two cannot be separated on chrF++ (30.51 and 30.61) or BLEU, even with paired item-level tests. Gemma-2-2B, whose tokenizer splits Romanized Nepali words least (2.72 tokens per word), scores worst on every measure. Which model gains most over its zero-shot baseline depends on the zero-shot prompt. In a supplementary comparison with an identical tokenizer, Llama-3.1-8B lowers BPB by 0.053 (0.050-0.056) relative to Llama-3.2-3B, while chrF++ and BLEU rise by only 0.68 and 0.58 points. Lower fertility and higher reference likelihood therefore did not identify the model whose outputs were closest to the references.

---


### 383. [How Far Does Second-Order Linear Response Predict Quantization Mismatch? Pre-Registered Measurements on Five Language Models](https://arxiv.org/abs/2611.12634)

**<font color=#1a73e8>作者：</font>** Dezhen Lu, Zixiang Ni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Serving systems choose a weight format for each model and deployment. A low-cost screen predicts the resulting KL divergence from the unquantized model's Fisher information using $\tfrac12\Delta^\top F\Delta$, the expansion underlying Hessian-aware and second-order post-training quantizers. We assess the reliability of this screen in GPU batches with channel-wise int8, per-tensor fp8 and group-wise int4 on Qwen3-8B, Qwen3-4B, OLMo-2-7B, Qwen3-32B and Qwen3-30B-A3B. Relative predictions hold across a 16-fold range of perturbation scales, int4 group sizes and rounding modes, while absolute predictions are heavy-tailed. A trimmed average brings 10 of 12 cells on Qwen3-4B and OLMo-2 within 15% of measured KL. The MoE model exhibits nonquadratic response at small perturbations, with int8 KL scaling as $\alpha^{0.63}$. Computing per-sequence gradients in bf16 can cause fourfold prediction errors. We trace these errors to arithmetic in the lower half of the backward pass and eliminate them by using fp32 there. Batch-invariant kernels run at 0.55 times the throughput, while changes in reduction order introduce a floor of 0.17-0.22 nats per sequence. We build a screener with one streamed fp32 Fisher pass, trimmed tensor-block predictions with a band, a flag for aligned tensors and per-layer format allocation. On the unseen Mistral-7B-v0.3 family, all six predictions fall within the band, all three KL budgets are met, and vLLM throughput is predicted within 0.4%.

---


### 384. [Beyond Sunny Skies: Using Large Language Models to Predict Urban Traffic in Adverse Weather](https://arxiv.org/abs/2611.12635)

**<font color=#1a73e8>作者：</font>** Zhu Xiao, Kuan Feng, Tong Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban traffic flow prediction is a cornerstone of intelligent transportation systems, yet accurate forecasting under adverse weather conditions remains a significant challenge. Existing data-driven models, while effective for routine patterns, often struggle with the sparse data and complex non-linear shifts associated with rare meteorological events. These methods typically treat environmental contexts as shallow numerical features, failing to capture the underlying semantic reasoning-why and how specific adverse conditions alter mobility behaviors across regions with different functional compositions. To address this limitation, we propose Multi-STG, a unified framework that integrates Large Language Model (LLM)-derived semantic priors with graph-based spatiotemporal learning. Multi-STG introduces an LLM-empowered semantic enhancement module that transforms comprehensive context descriptions such as weather, POIs, and holidays into high-level semantic embeddings, effectively providing a knowledge-driven complement to data scarcity. Furthermore, we design a multimodal attentional fusion mechanism to dynamically weigh heterogeneous inputs and a semantic-enhanced prediction head with gated residual calibration to robustly adjust forecasts based on semantic guidance. Extensive experiments on real-world multi-city private car datasets demonstrate that Multi-STG outperforms state-of-the-art baselines, reducing MAE by 11.82\% on average relative to the strongest baseline across three cities, while maintaining stable performance under sparse and non-stationary conditions.

---


### 385. [TrialDesignBench: Benchmarking Language Models for Phase-I Trial Design Against Clinical Knowledge](https://arxiv.org/abs/2611.12640)

**<font color=#1a73e8>作者：</font>** Yihan Hank Tang, Peng Yang, Jiayi Xin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI is used in much of the clinical trial pipeline. However, selecting the statistical design of a trial, a crucial step that determines how drug doses are tested on humans and evaluated, has seen almost no AI progress. LLMs appear to be a natural fit given their strengths in biomedical knowledge and statistical reasoning. Nevertheless, there is currently no appropriate way to evaluate such abilities because recent regulatory and methodological shifts, most notably FDA's Project Optimus, have redefined what constitutes a reasonable design and rendered many previous designs obsolete. To lay the groundwork for AI-assisted trial design, we introduce TrialDesignBench, a benchmark of 617 Phase-I/I-II oncology dose-finding trials, each paired with an expert-validated reference design that is consistent with the latest FDA regulatory initiatives. This reference standard is produced through a formalization of the expert design process. We evaluate five frontier LLMs, none of which matches the reference standard. Our ablation experiments trace this performance gap to two main causes, inference of latent, unrecorded design determinants from trial sources (supplying them raises class-wise balanced accuracy by 0.22) and structured decision-tree reasoning (+0.24). TrialDesignBench offers a reproducible, contemporary-standard objective for evaluating and enhancing AI-assisted trial design.

---


### 386. [reComposer: Editable Planning for Controllable Image Generation](https://arxiv.org/abs/2611.12687)

**<font color=#1a73e8>作者：</font>** Susie S.Y. Li, Angie Boggust, Fred Hohman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prompt-based image generation makes it easy to produce visual assets, but offers little support for engaging with the creative process. Prompting collapses interdependent creative decisions into a monolithic instruction and returns a finished image, leaving control limited to revising the prompt or correcting the model's output. We present reComposer, a process-oriented image-generation interface built around editable planning, which decomposes users' evolving intent into meaningful creative decisions - such as subject, composition, or palette - and collaborates with users to explore underspecified goals and alternatives. reComposer supports conversational and direct manipulation of the plan, moving between concept-level intent and visual-level control. We evaluated reComposer with 8 design and non-design professionals. Compared to prompting, participants felt greater control and ownership while developing visual assets, exploring alternatives, and iterating on details. Our findings suggest how shifting generative AI interaction from specifying outputs to shaping process can support creative thinking alongside asset production.

---


### 387. [A Lattice-Based HMM Approach to Aruz Scansion of Ottoman Poetry](https://arxiv.org/abs/2611.12691)

**<font color=#1a73e8>作者：</font>** Mehmet Emre Tiryaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ottoman Divan poetry is composed in aruz, a quantitative meter based on the weights of syllables. The meter is sensitive to specific characters recorded in the original writing in the Arabic script. This work is concerned with automatic meter finding and scansion alignment for Ottoman Divan poetry, especially on modern Turkish spelling without the special diacritics that scholarly transliterations of Ottoman preserve. We define two tasks on this input, first identifying the meter used in the poem, and second aligning the meter's weights with the syllabification of the poem, identifying the flaws and freedoms the poet has taken along the way. We build a corpus of 52,000 lines split by poet, with scansion annotations for 500 test lines, and a robustness benchmark generated at the deviation rates measured on real web and OCR copies. Our model is a hidden Markov model over the positions of each meter, decoded over a lattice of every candidate path, and trained by EM from the printed meter, without scansion labels. On a held-out set it scans 77.6% of the test lines fully correctly, against 26.8% for the available rule-based scanner, 55.0% for a neural tagger trained with the same supervision and 63.6% for Claude Opus 5.5 few-shot. The code is open-sourced and the tool is released on the web.

---


### 388. [GeoScope: Training-Free Program Execution beyond the Counting Horizon for Ultra-High-Resolution Remote Sensing Question Answering](https://arxiv.org/abs/2611.12699)

**<font color=#1a73e8>作者：</font>** Guohui Deng, Yuhang Jiang, Chengjun Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In ultra-high-resolution (UHR) remote sensing images, the objects that questions count in a region or relate by direction often span only a few pixels. Existing methods mainly decide where a vision-language model (VLM) should look and trust its answer in the chosen view. We show that this assumption fails for counting, and measure VLMs as one calibrates a sensor. All eight open VLMs tested fall increasingly short once a view holds more than a certain number of objects, about five for most on DOTA aerial images. This counting horizon narrows as views grow and objects appear smaller. An empirical power-law response model predicts the undercount a split recovers and the spurious counts it adds, and supports the rule of splitting only views beyond the horizon. In GeoScope, a text-only language model parses the question into a typed spatial program that fixes the region and its resolution. The VLM only grounds and counts within its operating range, and directions are computed explicitly from the grounded boxes. To our knowledge, it is the first UHR method to split views by a measured limit of the VLM. Without training, it improves Qwen3-VL-8B by 16.3 points on regional counting and 10.5 on spatial relations in XLRS-Bench, and has the highest reported accuracy, trained methods included, on regional counting and on the whole benchmark by question. On UHR-Micro it improves global and regional counting by 16.8 and 36.2 points, 15.6 of the former from splitting. On MME-RealWorld counting it gains 11.4 points, and we show that an option that is almost never correct yet often chosen distorts comparisons there. Project page: this https URL

---


### 389. [A local language model layered with rule-based and neural detectors for clinical text de-identification: an open-source toolkit and evaluation](https://arxiv.org/abs/2611.12709)

**<font color=#1a73e8>作者：</font>** Valentin Burkin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objectives: To measure whether a locally hosted large language model (LLM), stacked with deterministic and clinical named-entity recognition (NER) detectors, finds more protected health information (PHI) than open tools, and at what precision.
Materials and Methods: DeidSharp, an open-source .NET toolkit, combines the findings of pluggable detectors (patterns, a clinical NER model, a local 26B mixture-of-experts LLM) and fails closed on any detector error. Configurations fixed on tuning halves were compared, under a prespecified protocol, with deid, Philter, the Stanford/Penn de-identifier, OpenAI Privacy Filter and GLiNER on reporting halves of PhysioNet's nursing notes (889 spans) and semi-synthetic MIMIC-IV-Note discharge summaries (29,023 spans), and on synthetic ASQ-PHI queries, with paired patient-level bootstrap intervals.
Results: In the nursing notes, against Stanford/Penn, the recall-first stack found 98.9% of PHI (+2.8, 95% CI 1.4 to 4.4) at 9.3 points lower precision; the precision-first stack, without NER, found 96.5%, matching Stanford/Penn, at 19.6 points higher precision (83.2%). In the discharge summaries, both stacks led Stanford/Penn by more than 20 points (recall-first 95.3%, +21.5, 20.5 to 22.4), almost entirely on generated untyped names; on typed labels all three exceeded 99%. All four prespecified comparisons held. No configuration beat deid significantly on its home corpus; Philter found more discharge-summary spans than the recall-first stack at 23 points lower precision.
Discussion: The LLM was the main detector and NER added place names; asked to verify its own findings, the LLM discarded a quarter of true PHI.
Conclusion: A local LLM layered with deterministic detectors offers recall-first and precision-first operating points without sending text off-site.

---


### 390. [Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal](https://arxiv.org/abs/2611.12725)

**<font color=#1a73e8>作者：</font>** Zhenjie Zhang, Sainan Chen, Kshiteesh Hegde 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Providing real-time multimodal insights into images is challenging because it requires low latency, high description accuracy, and scalable solutions that are both cost-effective and efficient. For example, given a new image of an outfit, we would like to generate insights that the image depicts "earth tones" and "linen pants" and allow users to explore similar ideas along these themes. Traditional strategies to generate such insights would typically involve building taxonomies producing a golden set labeled by humans, training models on these datasets, and deploying these models for online inference services. Such workflows are constrained by fixed taxonomy, high labeling cost, limited labeling coverage in sample space, and human errors and expertise gaps in labelers. In addition, these methods are expensive and cumbersome to iterate over time. Recent trends have started exploring generative AI models for online insights, but this method suffers from long latency and prohibitive costs to support a high volume of requests or large amounts of offline labeling needs.
We present Generative Labeling On Clusters (GLOC) as a solution to provide highly scalable, cost-effective, low latency, and high accuracy online image insight services. GLOC leverages highly optimized image embeddings to form image clusters that are semantically close to each other for the purpose of the type of insights, and summarizes the insights at the cluster level, which effectively generalizes to members in the cluster. At Pinterest, GLOC powers image descriptors and pivot query suggestions for Hybrid Search, which is a multimodal search service enabling users to search with both an image and a text query. Our offline and online A/B tests demonstrate that GLOC significantly outperforms previous methods, delivering improvements in quality and efficiency.

---


### 391. [OptiCover: A Scalable and Multi-Surface Framework for Cold-Start Visual Optimization under Semantic Constraints](https://arxiv.org/abs/2611.12727)

**<font color=#1a73e8>作者：</font>** Guillaume Guy, Mihajlo Grbovic, Joe Mills 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selecting an effective cover photo is a critical yet understudied problem in visual merchandising for e-commerce marketplaces. On Airbnb, hosts upload many photos depicting different rooms, amenities, and points of interest, but must manually choose a single static cover photo that is reused across heterogeneous product surfaces. This creates substantial challenges: over 90\% of listing photos have no engagement labels, leading to a severe cold-start regime; guest preferences vary across surfaces and search intents, and visually captivating photos may be semantically misaligned with the underlying listing. At Airbnb scale, this corresponds to hundreds of millions of photos and hundreds of thousands of new uploads per day.
We propose \emph{OptiCover}, a scalable framework for cold-start visual optimization under semantic constraints and multi-surface engagement signals. The framework combines (i) a photo candidate generator that identifies candidate photos through various proxies, (ii) lightweight vision heads applied to frozen CLIP embeddings for large-scale semantic scoring, (iii) a cross-modal grounding validator based on a vision-language model (VLM) that enforces semantic representativeness, and (iv) an Exploration Logging Module (ELM) that orchestrates the collection of randomized engagement data across heterogeneous product surfaces and contextual search intents.
We evaluate OptiCover through extensive offline studies and multiple online experiments across HomePage, and Search surfaces. OptiCover is now deployed in production and performs tens of millions of photo swaps daily. Online results show a 1.5\% engagement lift on the HomePage and a 0.35\% increase in bookers on Search, generating millions of dollars in incremental revenue. Our findings suggest that action-space shaping and semantic constraints are primary drivers of performance.

---


### 392. [Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards](https://arxiv.org/abs/2611.12728)

**<font color=#1a73e8>作者：</font>** Brendan P. Murphy, Agustina Saenz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, when to stop gathering evidence, and which action to take. We introduce three controlled environments: medication refill triage, acute diagnostic work-up, and dosing titration, each with hidden clinical states, query costs, exact adaptive oracles, and deterministic outcome verifiers. Across these tasks, outcome-only group relative policy optimization often improves aggregate reward while producing undesirable procedures, including premature commitment, one-question collapse, and failures on rare high-risk cases. In diagnostics, assigning dense credit to questions that reduce uncertainty improves held-out value and moderate-case support across three training seeds relative to outcome-only reinforcement learning, without the high-risk seed collapse observed under outcome-only training. Separating exploration from exploitation further increases high-risk support at its best checkpoint, but at the cost of excessive information gathering on low-acuity cases. Additional experiments show that the optimal strength of process credit is task-dependent; that after a supervised warmup that already gathers carefully, reinforcement learning raises aggregate reward by trimming questions while degrading high-risk performance; and that reinforcement learning does not reliably repair rare behavior gaps inherited from biased supervised data. Verifiable final outcomes are therefore insufficient for training reliable multi-turn agents: reward design must account for the procedure used to reach an answer, and evaluation must distinguish adaptive information gathering from reward-exploiting shortcuts.

---


### 393. [The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?](https://arxiv.org/abs/2611.12750)

**<font color=#1a73e8>作者：</font>** Nikhil Sharma, Kelly Marchisio, Kenton Murray 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly mediate how people seek and consume information, including accounts that differ across languages and regions, especially on contested topics. Supporting diverse information seeking requires models to help users navigate competing narratives across languages and information streams. We define six capabilities necessary for diverse multilingual information seeking: three foundational capabilities for narrative inclusion, narrative exclusion, and missing narrative identification; and three higher-level capabilities for presenting diverse narratives, preserving narrative coverage under confirmatory queries, and maintaining information parity across languages. To guide the development of those information seeking capabilities, we introduce \textsc{NarrativeBench}, a benchmark comprising 1,333 news articles in 23 publication languages across 23 contested topics and 460 Reddit-grounded queries. Evaluating 14 LLMs across 24 query languages, we find that current models lack the capabilities needed to reliably navigate diverse narratives, limiting users' control over the perspectives they receive and leaving substantial gaps in exposure to competing accounts even when diversity is explicitly requested. Information access also differs across query framings and languages, risking echo chambers, linguistic filter bubbles, and information disparities that weaken the common ground needed for democratic discourse. \textsc{NarrativeBench} provides a foundation for developing information systems that give users across languages and regions agency to navigate diverse narratives.

---


### 394. [PORT: Preference Optimization via Robust Token-Level Reweighting](https://arxiv.org/abs/2611.12763)

**<font color=#1a73e8>作者：</font>** Ding Zhu, Xiukun Wei, Tian Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference optimization has become a central approach for aligning large language models with human values, but its effectiveness depends heavily on the quality of preference annotations. In practice, preference data is often noisy due to annotation errors and ambiguity. Existing robust preference optimization methods primarily operate at the sequence level, implicitly treating entire responses as uniformly correct or incorrect. However, rejected responses may still contain informative reasoning steps, while preferred responses can include subtle errors. In this work, we propose \textbf{P}reference \textbf{O}ptimization via \textbf{R}obust \textbf{T}oken-level reweighting \textbf{(PORT)}, a fine-grained framework for robust alignment under noisy preferences. PORT performs token-level reweighting using the empirical cumulative distribution function (CDF) of token log-probabilities, yielding an efficient forward-pass-only proxy to gradient-norm penalization that selectively suppresses corrupted tokens without additional backward-pass computation. We provide theoretical analysis showing that PORT reduces the gradient bias from noisy preference labels by minimizing an upper bound on the bias term. Extensive experiments across diverse noise settings demonstrate that PORT consistently improves robustness and outperforms existing sequence-level baselines. The code is available at this https URL

---


### 395. [LogCDM: Interpretable Log Anomaly Detection via Behavioral Graph Drift and Adaptive Signal Fusion](https://arxiv.org/abs/2611.12775)

**<font color=#1a73e8>作者：</font>** Suryansh Talukdar, Taha Sarwat, Jin Soung Yoo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Log-based anomaly detection is increasingly dominated by large pretrained models, from BERT-scale encoders to 8B-parameter language models, which require GPUs at inference time and are difficult to deploy on the monitoring nodes where logs are produced. We present LogCDM, a compact detector that scores each log session using three complementary signals: the next-event surprise of a small causal Transformer, the distance between a graph-attention embedding of the session's own transition graph and that of a normal reference graph, and a transition-drift statistic that we show is exactly a frequency-weighted chi-squared divergence between transition kernels. The divergence view yields an asymptotic null distribution, a length-standardized score, and a per-edge decomposition that explains each alarm. A sigmoid gate fuses the three signals; under a shared-covariance Gaussian model, this gate is the Bayes posterior, and its learned weights indicate which signal each dataset relies on. With 8.1-8.8M parameters and no GPU required at inference, LogCDM reaches F1 scores of 0.984 on HDFS, 0.870 on chronologically split BGL, and 0.850 on Thunderbird, within 0.013-0.12 of an 8.1B-parameter LLM detector evaluated under the same protocol and above all compact baselines on BGL. It scores a session in 5.5-10.5 ms on a CPU. Ablations show that the structural signals add 0.025-0.030 F1 on BGL and Thunderbird but almost nothing on HDFS, consistent with the learned fusion weights.

---


### 396. [Large Language Models as a Universal Searcher for Open-World Automated Machine Learning](https://arxiv.org/abs/2611.12791)

**<font color=#1a73e8>作者：</font>** Yuxuan Hu, Jihao Liu, Weikang Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, training hyperparameter, and data ratio optimization. Here, we bridge this gap by proposing a universal, large language model (LLM)-based AutoML framework that jointly optimizes these configurations for the first time without the need for task-specific fine-tuning. We propose NCode, a unified numerical encoding scheme that translates diverse AutoML design choices into universal discrete sequences and effectively reframes the optimization process as a unified ranking task. Trained solely on optimization trajectories derived from a limited, single-domain vision task, the proposed LLM-based searcher demonstrates impressive cross-task, cross-modality and joint search-space optimization generalizability, achieving state-of-the-art performance across image classification, image segmentation, speaker verification and text-to-image benchmarks. Crucially, it exhibits superior scalability in the large-scale training and joint optimization of a billion-parameter Diffusion Transformer, requiring 896 GPU-days and attaining a state-of-the-art GenEval score of 0.91. By leveraging reinforcement learning to instill Chain-of-Thought reasoning, we provide a systematic way to interpret the LLM-based searcher's internal decision-making mechanisms, revealing its optimization strategy shifted from the early-stage diversity-driven exploration to the late-stage anchor exploitation. Our proposed framework provides a scalable, generalizable, and interpretable pathway toward general-purpose open-world machine learning optimization.

---


### 397. [Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks](https://arxiv.org/abs/2611.12799)

**<font color=#1a73e8>作者：</font>** Tingcheng Bian, Kangye Gong, Jinchang Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lossy: in GRPO training of LLM agents, the best-validation checkpoint fails on problems that earlier checkpoints from the same run had already solved, and the union of problems solved across checkpoints far exceeds any single one. The discarded checkpoints thus form a teacher pool obtained at no additional training cost, which on-policy distillation (OPD) can mine to recover the lost coverage. Mining this pool raises two challenges: i) which checkpoint to distill from, as no checkpoint dominates the others and complementarity to the student is problem-specific; ii) where to trust it, as even a well-chosen teacher is only locally superior, so indiscriminate distillation overwrites behavior the student has already mastered. We propose Agentic-OPD, which treats the best-validation checkpoint as the student and all saved checkpoints as frozen teacher candidates, using the student's evolving capability gaps to guide both teacher selection and supervision filtering: the HCN policy (Highest Coverage Next) dynamically selects teachers by weighted coverage of the student's unsolved problems, while the LAD module (Locality-Aware Distillation) confines transfer to failed student rollouts on problems where the teacher performs better. Across five agentic task domains and 24 benchmarks and task subsets, Agentic-OPD improves over its initialization checkpoint by up to 7.4 points, with a 4B student surpassing the latest frontier models GPT-5.6 and DeepSeek-V4.1 on deep search. Agentic-OPD recasts a finished RL run as a reusable pool of policies and establishes post-RL capability recovery as a stage orthogonal to improvements in the RL algorithm itself.

---


### 398. [Automated Knowledge Acquisition Pipeline for Disassembly Instructions: A Comparison of NLP and Generative AI Frameworks](https://arxiv.org/abs/2611.12816)

**<font color=#1a73e8>作者：</font>** Tim Schnieders, Tareq Maximilian Gabriel Ahrari, Oliver Petrovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The push towards circularity and Re-X principles presents a challenge to SMEs, particularly due to increasing product complexity that impedes the adoption of disassembly automation. This paper introduces and compares two frameworks for extracting disassembly instructions from unstructured information sources, such as disassembly manuals. Our goal is to transform natural language text into a structured, curated and machine-readable format. We implemented and tested a rule-based Natural Language Processing (NLP) framework against a generative AI framework leveraging LLMs. The performance of both approaches was compared using real-world disassembly manuals. This work provides the necessary data foundation for developing and automating future disassembly processes.

---


### 399. [Mitigating Agentic Deception via Evaluation-Side Partially Observable Games](https://arxiv.org/abs/2611.12835)

**<font color=#1a73e8>作者：</font>** Hanxiao Li, Shutong Liu, Yongjia Ma 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without checking the faithfulness of underlying reasoning, tool use, and environmental effects. Prior mitigations address this partial observability by predefined evaluator latent belief space or one-shot monitoring, which do not extend to free-form language space and vulnerable to stronger deceptions that evade simple monitoring. In this work, we formulate deception mitigation as an Evaluation-Side Partially Observable Extensive Form Game (e-PoG), a max-min framework in which an agent maximizes reward, a monitor minimizes the agent's payoff by exposing deception from the full interaction trajectory, and a fixed verifier validates the monitor's claims and converts them into penalties. We define the solution concept as a Subgame-Perfect Oversight Equilibrium (SPOE) between agent and monitor, and prove its existence in finite games. With a perfect verifier, every SPOE is faithful; with an imperfect verifier, the guarantee persists if verifier errors do not reverse the ranking of monitor actions. To achieve faithful SPOE, we derive a two-timescale policy gradient algorithm and enhance the pipeline empirically with NLI verification and deterministic checks. Experiments with Gemma3-4B-IT and Qwen3-4B/8B on Agentic Role-Playing, SearchQA, and WebShop show that e-PoG mitigates multiple emergent deception modes, outperforming the strongest baselines by 26.0% in deception mitigation and by up to 39.8% in task success. These gains persist under weak-to-strong supervision. Code is available at this https URL.

---


### 400. [WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.12856)

**<font color=#1a73e8>作者：</font>** Zheng Jiang, Fang Niu, Bo Peng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as workflow orchestration and introduce WorkflowArena, a benchmark of 145 long-horizon tasks spanning 8 professional domains, from software engineering and formal mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an integrated deliverable composed of interdependent components, which is assessed by a hidden verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded, enabling joint evaluation of deliverable quality and the organization of the underlying work. Experiments with nine models show that no single configuration performs best across all domains and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units. When the executing model is held fixed on a challenging subset of tasks, workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
