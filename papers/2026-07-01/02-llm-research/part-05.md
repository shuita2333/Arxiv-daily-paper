# 🧠 大模型相关研究 | 2026年07月01日

> 本类共 **247** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-247**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-247**

---

### 201. [One Forward Beats Two: InnerZoom for Accurate and Efficient GUI Grounding](https://arxiv.org/abs/2606.30084)

**<font color=#1a73e8>作者：</font>** Chen Liu, Ling Chen, Hanzhang Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MLLM-based GUI grounding methods commonly formulate target localization as autoregressive coordinate generation, enabling models to leverage the strong instruction-following and semantic understanding capabilities of MLLMs. However, this formulation requires the model to retain region-level target evidence while decoding coordinate tokens with the spatial precision demanded by GUI clicking. Our diagnostic analysis reveals that target-region awareness emerges in intermediate decoder layers but is neither retained nor translated into the final coordinate prediction. Existing ZoomIn-style methods address this issue through an external crop-and-rerun pass, which improves localization but increases end-to-end latency and computational cost. To retain the accuracy benefits of two-pass zooming without this extra cost, we propose InnerZoom, a single-forward framework for cross-layer evidence bridging. InnerZoom transforms target-related cues from the original forward pass into a compact cross-layer evidence state, then preserves, refines, and reinjects this state throughout later decoding layers to guide coordinate prediction. Extensive experimental results suggest that InnerZoom-4B achieves state-of-the-art performance on all six GUI grounding benchmarks, obtaining 64.7 on OSWorld-G, 40.2 on UI-Vision, 73.1 on OSWorld-GR, and 87.6 on MMBench-GUI, surpassing the previous best results by 4.1, 3.2, 2.9, and 2.3 points, respectively. Under a controlled 4B setting, InnerZoom improves the same SFT+RL baseline by 5.3 points on average and outperforms two-pass ZoomIn by 1.3 points on average, while reducing end-to-end latency by up to 31.8% and TFLOPs by about 29%. Code and models will be publicly available.

---


### 202. [Not-quite-human tastes: the stylized omnivorousness of LLM survey surrogates](https://arxiv.org/abs/2606.30085)

**<font color=#1a73e8>作者：</font>** Xiangyu Ma, Mengmi Zhang, Shannon Ang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-language models have proven to be remarkable if inconsistent parrots of public attitudes and opinions. The extent to which LLMs are able to produce reasonable approximations of cultural taste remains an open empirical question that becomes more urgent by the day, with market research companies already offering provisional `synthetic' survey panels and the contamination of standard survey data from LLM-generated responses. In this study, we build on past work on silicon sampling by extending considerations of its algorithmic fidelity and alignment to the domain of cultural consumption. We use large-language models from OpenAI, Anthropic, and DeepSeek to each produce 277,470 (30x9249) silicon surrogates of survey respondents from the Survey of Public Participation in the Arts (SPPA). We find these silicon surrogates' tastes to be highly stylized facsimiles of human tastes. (1) Silicon samples have a systematic postive-bias for liking, resulting in inflated ecological estimates of tastes. The individual-level bias of silicon samples are not well-explained by the WEIRD-bias often discussed in the literature. (2) The complex relationality in real taste structures is completely lost among silicon samples. (3) Finally, very little of the known cultural alignment between tastes and social space are preserved. Silicon samples attenuate age-taste associations, resurrect anachronistic class-taste associations, caricaturize gender- and race-taste associations.

---


### 203. [Efficient Retrieval-Augmented Generation via Token Co-occurrence Graphs](https://arxiv.org/abs/2606.30093)

**<font color=#1a73e8>作者：</font>** Gianluca Bonifazi, Christopher Buratti, Michele Marchetti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) mitigates hallucinations in Large Language Models (LLMs) by grounding the generation process on external knowledge. However, standard RAG approaches struggle with multi-hop reasoning. While recent graph-based RAG methods improve the retrieval of interconnected chunks, they often rely on computationally expensive and error-prone LLM-based extraction pipelines. To address these issues, we propose TIGRAG (Token-Induced GraphRAG), an efficient graph-augmented RAG framework based on a token co-occurrence Knowledge Graph. TIGRAG directly models topological relationships between tokens using sliding-window co-occurrence statistics, thus enabling scalable graph construction. During inference, it combines graph-based semantic expansion and neural reranking to retrieve interconnected evidence for multi-hop reasoning. Specifically, it introduces an iterative entity-driven retrieval strategy that progressively expands the query using bridging entities extracted from previously retrieved contexts. We evaluated TIGRAG on three widely adopted multi-hop Question Answering (QA) benchmarks. Experimental results demonstrated that our framework consistently outperforms dense retrieval and graph-based RAG methods in both retrieval and downstream QA tasks, while substantially reducing indexing time, inference latency, and prompt footprint.

---


### 204. [Temporal Feature Extractors in EEG Foundation Models: A Controlled Comparison Including a Pretrained Time-Series Model](https://arxiv.org/abs/2606.30104)

**<font color=#1a73e8>作者：</font>** Ayşe Betül Yüce, Chris Joey Leffler, Sarun Varghese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models aim to learn generalizable representations from large-scale brain recordings. However, the role of temporal feature extractors and whether pretrained time-series foundation models (TSFMs) can be effectively transferred to this setting remains underexplored. We conduct a controlled comparison of three temporal feature extraction strategies, including a linear baseline, a convolutional encoder, and a frozen pretrained TSFM (MOMENT), within a unified EEG foundation model. We evaluate their impact on representation quality using two downstream tasks: motor imagery and emotion recognition. Results reveal different trends across the evaluated benchmarks. On the motor imagery dataset, simple temporal representations perform competitively, whereas the emotion dataset benefits from richer temporal modeling. Although not specifically adapted to EEG, the pretrained TSFM serves as an effective temporal feature extractor, suggesting that general-purpose time-series representations can be transferred as frozen temporal feature extractors within EEG foundation models.

---


### 205. [Structural Certification for Reliable Physical Design with Language Models](https://arxiv.org/abs/2606.30107)

**<font color=#1a73e8>作者：</font>** Nakul Vyas, Iliya D. Stoev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An unreliable language model can be made to produce reliable physical designs if the authority to assert is moved out of the model: the model proposes, and a deterministic engine alone certifies, returning certified, impossible, or unknown. We introduce Physics-Anchored Certification (PHACT), a propose-certify loop spanning five scientific domains, and identify what makes such a certificate trustworthy. A checker that accepts a model-supplied value can be forged; deriving the certified quantity from fixed inputs instead makes forgery impossible by construction. Across eighty adversarial trials spanning two models, two decoding temperatures, and a deliberately faulted engine, this contract produced zero false certifications.

---


### 206. [Open Problems in Constitutional Preference Reconstruction](https://arxiv.org/abs/2606.30116)

**<font color=#1a73e8>作者：</font>** Eleanor Clifford, Michael Amir, Arduin Findeis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pairwise preference data is widely used for training and evaluating language models (e.g., RLHF), but each datapoint records a \emph{choice}, not the rationale behind it. Methods such as Inverse Constitutional AI (ICAI) attempt to improve interpretability by compressing datasets into short ``constitutions'' of natural-language principles. We argue this framing is under-specified: a flat list of principles is not yet an executable decision rule because it leaves principle composition implicit. We use the pairwise setting as a testbed to empirically characterize three open problems in constitutional methods. First, principle quality is hard to measure: coverage and accuracy are useful but incomplete proxies for end-to-end reconstruction. Second, \emph{composition is ambiguous}: holding principles fixed, different executors (LLM judge versus majority vote) agree only $73\%$ of the time. Third, \emph{constitutions differ between LLMs}: cross-model vote agreement is $73\%$, whereas intra-model agreement is $81\%$. Across PRISM, AlpacaEval, and Chatbot Arena, we show that principle refinement (ICAI+) may be a first step towards ameliorating these problems: inter-executor agreement rises to $78\%$, and transparent executors match LLM judge accuracy ($66\%$ vs.\ $67\%$). Our results highlight that constitutions should be evaluated as \emph{constitution--executor systems}, with implications for LLMs-as-a-judge broadly.

---


### 207. [Latent Noise Mask for Reducing Visual Redundancy in Multimodal Large Language Models](https://arxiv.org/abs/2606.30168)

**<font color=#1a73e8>作者：</font>** Kai Jiang, Ruishu Zhu, Siqi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often fail in fine-grained visual reasoning, as question-relevant visual cues are diluted by dense and redundant image tokens. Recent multimodal reasoning methods usually extend chain-of-thought from language models into visual or latent spaces, seeking to add intermediate reasoning states while overlooking the negative impact of redundant visual tokens. We propose LatEnt Noise maSk (Lens), a question-conditioned visual evidence purification framework that empowers MLLMs to reason with cleaner visual cues in latent space. Lens introduces a lightweight Lens Evidence Token (LET) to score which visual tokens support the current question and preserve them during decoding. Guided by the LET scores, it injects adaptive latent noise into low-relevance tokens, softly suppressing distractors without changing the model backbone or token sequence. With only one temporary learnable control token and a lightweight noise generator, Lens adds minimal overhead while improving the base MLLM by 2.4-6.4 points on most VQA datasets and by 4.1-6.4 points on grounding tasks. These results show that multimodal reasoning can benefit more directly from cleaner question-relevant visual evidence than from simply extending the reasoning trace.

---


### 208. [CORTEX: High-Quality Cross-Domain Organization of Web-Scale Corpora through Ontological Corpus Graph](https://arxiv.org/abs/2606.30175)

**<font color=#1a73e8>作者：</font>** Chengtao Gan, Xiaoke Guo, Yushan Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The continuous evolution of large language models drives escalating demands on data scale and quality, and as different training stages impose increasingly tailored data requirements, systematic organization of high-quality corpora becomes indispensable. Existing corpus construction pipelines confine the resulting corpora to flat, undifferentiated document collections, universally lacking systematic knowledge organization. We present Cortex, to our knowledge the first framework that elevates web-scale corpus construction from flat document filtering to structured knowledge organization through an Ontological Corpus Graph (OCG), a three-layer heterogeneous structure unifying a quality-refined content layer, a hierarchical lightweight ontology layer via LLM-driven automated evolution, and a cross-domain alignment layer enabling inter-domain association at arbitrary taxonomic resolution. Comprehensive experiments confirm the effectiveness of Cortex. In particular, we leverage the OCG to synthesize CortexBench, a cross-domain search-and-reasoning benchmark whose evaluation across eight frontier LLMs validates the effectiveness of quality refinement, domain organization, and cross-domain data synthesis. We will publicly release the complete codebase, a 24.14B-token refined corpus with its OCG, and CortexBench.

---


### 209. [DAIN: Dynamic Agent-Based Interaction Network for Efficient and Collaborative Multimodal Reasoning](https://arxiv.org/abs/2606.30189)

**<font color=#1a73e8>作者：</font>** Xinxin Chen, Yuchen Li, Zihan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current multimodal fusion approaches, particularly those based on static Mixture-of-Experts (MoE) architectures, often struggle to provide the adaptive and efficient collaborative reasoning required by complex real-world applications. We introduce the Dynamic Agent-based Interaction Network (DAIN), which reconceptualizes multimodal fusion as a dynamic, multi-agent collaborative process. DAIN employs a context-aware Meta-Controller that dynamically schedules sparse activation of specialized interaction agents and orchestrates compressed inter-agent communication for consensus-building. The framework is guided by a multi-objective loss function that jointly optimizes task accuracy, agent specialization, and operational efficiency through sparse activation and communication regularization. Comprehensive evaluations across five diverse benchmarks -- ADNI, MIMIC-IV, MM-IMDB, CMU-MOSI, and ENRICO -- establish DAIN as a new state-of-the-art, delivering significant performance improvements including a 2.6\% accuracy gain on ADNI. Ablation studies verify the critical roles of both dynamic scheduling and agent communication. Furthermore, DAIN offers enhanced interpretability by exposing context-dependent agent roles and collaboration patterns while maintaining computational efficiency through sample-wise sparse agent activation. Our work demonstrates the promise of dynamic, agent-based paradigms for multimodal reasoning.

---


### 210. [EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures](https://arxiv.org/abs/2606.30219)

**<font color=#1a73e8>作者：</font>** Buğra Alperen Uluırmak, Rifat Kurban  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM evaluation and AI safety face a shared measurement problem: benchmark scores, reward-model signals, and reported safety metrics can improve while the latent properties they are meant to represent remain difficult to verify. This paper combines a hybrid survey - a systematic search paired with narrative synthesis and separately tracked grey evidence - with a conceptual framework and a structured ten-model audit. The synthesis spans eight evidence streams: benchmark validity, dynamic evaluation, LLM-as-judge reliability, safety evaluation, jailbreak/refusal robustness, reward hacking, mechanistic interpretability, and governance/auditability, covering 2018-2026 evaluation-safety measurement work. We introduce EvalSafetyGap as an organizing hypothesis for comparing evaluation-side and alignment-side proxy failures under optimization pressure, using Goodhart's Law together with two constructs we develop here - an Instability Decomposition and an Alignment Trilemma - as tools for generating testable comparisons. The audit shows how conclusions shift when capability, behavioral safety, and governance are measured separately. In this sample (n = 10), the association between capability and sustained adversarial robustness is statistically indeterminate using the displayed Table 3 inputs (Pearson r = +0.232, p = 0.520), and the apparent open-closed safety gap is modest, driven mainly by governance and disclosure rather than behavioral robustness, and sensitive to how a single borderline model is classified; attempt-budget results are protocol dependent. Because the public evidence uses heterogeneous protocols, the audit is diagnostic rather than rank-generating. The contribution is a shared vocabulary and evidence map to support dynamic evaluation, transparent source reporting, multi-attempt safety measurement, and auditable alignment practice.

---


### 211. [Semantic-Driven Scale and Spatial Selection for Efficient Cross-Modal Alignment in Referring Remote Sensing Image Segmentation](https://arxiv.org/abs/2606.30244)

**<font color=#1a73e8>作者：</font>** Kun Li, Shengxi Gui, Francesco Nex 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Remote Sensing Image Segmentation (RRSIS) seeks to localize and segment the target object or region specified by a natural language expression in a remote sensing image. While existing RRSIS models have benefited from large-scale foundation models, they predominantly rely on full fine-tuning. These approaches are computationally intensive and may weaken the generalization ability of pre-trained models, as extensive fine-tuning on significantly smaller downstream datasets can distort the well-structured feature representations learned during large-scale pre-training. Although Parameter-Efficient Tuning (PET) offers a potential alternative, existing PET frameworks primarily focus on single-modal optimization, failing to capture the complex cross-modal dependencies required for multimodal reasoning, while simultaneously struggling to bridge the substantial domain gap between natural scenes and aerial imagery. To address these limitations, we propose a novel framework, Semantic-driven Scale and Spatial Selection for Efficient Cross-modal Alignment (S4ECA), which enables effective and efficient cross-modal interaction through parameter-efficient adaptation. Specifically, we design a dual-encoder adapter architecture. The textual adapter employs learnable queries to distill highly semantic language proxies from word-level embeddings, facilitating early grounding. Simultaneously, the visual adapter refines hierarchical feature representations through a multi-scale dense extractor, followed by a language-guided scale and spatial selection mechanism that dynamically emphasizes relevant visual contexts, ensuring precise cross-modal alignment. By updating only 2.4% of the backbone parameters, our proposed model achieves state-of-the-art performance on the RRSIS-D and RefSegRS datasets, demonstrating superior efficiency and precision in complex aerial scenarios.

---


### 212. [Grounding LLM Reasoning under Incomplete Graph Evidence](https://arxiv.org/abs/2606.30247)

**<font color=#1a73e8>作者：</font>** Jiaqi Li, Fanghui Song  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs can guide large language models (LLMs) reasoning, but the graph seen by a system is usually a retrieved, linked, temporally scoped, and incomplete evidence state rather than a complete account of truth. We develop a theoretical perspective on grounding observable LLM trajectories under such incomplete graph this http URL evidence state induces entity anchors, typed relation residuals, path energies, and support regions, while the language model supplies a prior over candidate trajectories. We show that, under open-world incompleteness, no hard rule based only on the observed state can both reject every false unsupported trajectory and retain every true-but-unobserved this http URL then characterize soft grounding as a KL-regularized deformation of the LLM prior: finite slack preserves support for unsupported but non-contradicted trajectories, whereas hard conditioning appears as an infinite-penalty this http URL framework also yields stability bounds under evidence perturbations and clarifies the constraint regimes appropriate for GraphRAG, KGQA, graph agents, constrained decoding, and faithful generation. The claims are evidence-relative: KG compatibility is treated as declared support, not factual truth.

---


### 213. [TACO: Tool-Augmented Credit Optimization for Agentic Tool Use](https://arxiv.org/abs/2606.30251)

**<font color=#1a73e8>作者：</font>** Mingkuan Feng, Jinyang Wu, Hao Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic multimodal models perform diverse operations on an image via code and reason over the returned view, an effective paradigm for fine-grained visual question answering. However, code operations can be useful, redundant, or misleading. Outcome-only rewards cannot precisely distinguish these cases, and existing process rewards either fail to attribute final correctness to individual tool calls, or require an external judge model. To address this, we introduce Tool-Augmented Credit Optimization (TACO), a GRPO variant for code-tool agents built on two coupled advantage channels. The first, Differential Answer-Probe Reward (DAPR), is a self-supervised, judge-free tool-contribution advantage that credits each tool call by its own effect on answering correctly. Probe tokens inserted into the model's reasoning elicit its predictions with and without the tool, and the difference in outcome reward is taken as the call's value: positive for a useful call, negative for a misleading one, and zero for one that changes nothing. This reuses the existing answer checker with no auxiliary judge, and, being a difference rather than an absolute probe score, is naturally robust to probe-hacking. The second is the outcome advantage from the final answer, distributed by Outcome-Gated Advantage Routing (OGAR): a parameter-free rule that, conditioned on the call's outcome, delivers this credit only to the responsible segments, suppressing wasted tool calls without any cost term. We train TACO through a two-stage SFT+RL pipeline. Extensive experiments across perception, reasoning, and general multimodal benchmarks show that it yields consistent accuracy gains and learns to invoke its tools only when they help.

---


### 214. [KnowsTFM: Knowledge-Informed Fine-Tuning of Small Tabular Foundation Models](https://arxiv.org/abs/2606.30258)

**<font color=#1a73e8>作者：</font>** Boshko Koloski, Xiangjian Jiang, Senja Pollak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models have advanced deep learning for tabular data by delivering strong default performance across many small and medium tasks. Yet in niche domains, where data is scarce, high-dimensional, and shifted from the pretraining distribution, they may still fail to outperform carefully designed domain-specific methods. Many such domains also provide curated relational knowledge in the form of knowledge graphs and knowledge banks, but how to use this knowledge to improve and steer \textit{small} specialist tabular foundation models remains unclear. We address this problem through \textbf{Know}ledge-informed fine-tuning of \textbf{s}mall \textbf{T}abular \textbf{F}oundation \textbf{M}odels (\modelname). Specifically, we study nanoscale TabPFN- and TabICL-style variants, pretrained under controlled synthetic prior families and adapted using two complementary mechanisms: structural attention priors derived from knowledge graphs and parameter-efficient low-rank updates. We show that injecting domain-specific structural knowledge during fine-tuning yields meaningful gains over vanilla variants in specialist settings, whereas gains on general-domain tasks are marginal. We further observe that continual fine-tuning of frontier models can trigger collapse of pretrained knowledge and mechanisms.

---


### 215. [Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats](https://arxiv.org/abs/2606.30259)

**<font color=#1a73e8>作者：</font>** Sebastian Kula, Martin Tamajka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

---


### 216. [Intermediate Text Representation Guided Text-to-Image Generation for Enhancing One-and-Only Alignment](https://arxiv.org/abs/2606.30262)

**<font color=#1a73e8>作者：</font>** Soyoun Won, Aryan Yazdan Parast, Basim Azam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models often fail to faithfully render explicit textual descriptions, instead defaulting to strongly learned visual priors due to a phenomenon referred to as concept association bias. We show that such bias is particularly strong for one-and-only (OAO) objects, entities that exist in a single canonical form, such as celestial bodies, landmarks, and artworks. The deeply ingrained visual identity for these concepts often resists modification through prompting alone. Addressing this challenge, we first identify through an information-theoretic analysis that the final text embedding discards concept-level information present in the intermediate-layer text representations, reducing the mutual information available to the subsequent denoising process. We then propose Intermediate Text Representation (IR)-guided diffusion, which injects intermediate hidden states of the text encoder into the conditioning signal during early denoising steps, recovering suppressed concepts without any additional training, optimization, or external models. To systematically evaluate the challenging task of aligning generative outputs with unusual prompts for OAO objects, we introduce OAO-AttackBench, a benchmark comprising counterfactual prompts that directly conflict with the core visual identity of OAO objects. Experiments on four benchmarks, including OAO-AttackBench, show that our method achieves up to a 19.1 percentage-point improvement in VQAScore while preserving generation fidelity and human preference. Project page: this https URL.

---


### 217. [PromptGNN-sim: Deep Fusion and Alignment of GNN and LLMs for Text-Attributed Graph Learning](https://arxiv.org/abs/2606.30291)

**<font color=#1a73e8>作者：</font>** Zhifei Hu, Alexandra I. Cristea  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-Attributed Graphs (TAGs) combine textual semantics with graph structure and are central to many graph learning tasks. However, existing fusion methods often treat text and structure as separate inputs in a shallow, one-way pipeline, which limits deep interaction between modalities and weakens performance under sparse connectivity or cross-graph generalisation. To address this issue, we propose PromptGNN-sim, a bi-directional structure-semantic fusion framework for collaborative GNN-LLM learning. PromptGNN-sim uses a Graph Attention Network (GAT) for semantically aware neighborhood selection by combining structural attention with textual similarity. The selected structural context is then used to generate structure-aware prompts for an LLM, including the target node summary, label categories, and representative keywords from similar neighbors. During training, bi-directional cross-modal contrastive learning and cross-attention are introduced to jointly optimize the GNN and LLM components. Experiments on six public datasets, including Cora, Pubmed, and WikiCS, evaluate accuracy, generalisation, and robustness under cross-task transfer, cross-dataset generalisation, and sparse perturbations. Results show that PromptGNN-sim outperforms classical GNNs, LLMs, and recent GNN-LLM fusion methods, demonstrating the effectiveness of interactive structure-semantic collaboration for text-attributed graph learning.

---


### 218. [DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model](https://arxiv.org/abs/2606.30292)

**<font color=#1a73e8>作者：</font>** Daniyel Ayupov, Artur Markov-Tsoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present DreamForge-World 0.1 Preview, a preview foundational world model for real-time interactive world simulation. The system adapts the LongLive 1 autoregressive video stack, itself derived from Wan2.1-T2V-1.3B, with a residual action pathway inspired by the Matrix-Game family. DreamForge-World 0.1 Preview focuses on a complementary axis to frontier-scale world simulators: low-compute adaptation, consumer-GPU runtime, and broad interactive capability coverage. It supports live keyboard and mouse control, multimodal initialization, mid-stream reprompting, dual-view operation, and minute-scale interactive rollouts at native 480p resolution, reaching up to 14 to 15 FPS FPS on a single RTX 4090 with a low memory footprint. By leveraging open video backbones and applying targeted adaptation runs, we build the preview system with high cost-efficiency. DF-World 0.1 Preview is not yet a memory-complete or frontier-quality world simulator, but demonstrates a practical low-compute route toward real-time controllable world-model previews on consumer GPUs.

---


### 219. [ManimAgent: Self-Evolving Multimodal Agents for Visual Education](https://arxiv.org/abs/2606.30296)

**<font color=#1a73e8>作者：</font>** Wenjia Jiang, Zongyuan Cai, Yuanhang Shao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-round reflection lets agents built on large language models recover from failures within a single task, but each task remains an isolated episode: lessons learned across many reflection rounds on one task are discarded before the next begins. We study this gap on a code-generation task: from a scientific paper section, the agent writes Python in the open-source Manim library to render a mathematical animation. We present ManimAgent, a self-evolving multimodal agent that carries reflection experience across tasks through a dual-channel Episodic Memory Bank grown entirely from its own task stream, with no weight updates and no human seeds. After each animation converges, a vision-language model scores the rendered keyframes; the resulting signals populate a positive channel M+ that stores success rationales as soft Reference Examples, and a negative channel M- that stores validated failure patterns as hard Known Pitfalls. On a fixed-probe evaluation against no-memory, matched-budget retrieval-augmented generation, and shuffled-memory baselines, blind human Pass@1 rises and reflection rounds fall as memory size grows. We will release the code, frozen memory snapshots, and the task stream.

---


### 220. [Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents](https://arxiv.org/abs/2606.30306)

**<font color=#1a73e8>作者：</font>** Tianyu Ding, Aditya Nannapaneni, Bingfan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Always-on agents are systems whose future behavior depends on durable state accumulated across earlier interactions. We treat them as persistent-state systems: the operative system includes retrievable memories, but also task ledgers, permissions, credentials, commitments, provenance and audit records, shared state, trigger conditions, and externally committed effects linked to those records. The survey reads the literature through six diagnostic axes for each state item, authority, scope, mutability, provenance, recoverability, and actionability, and through a lifecycle in which state is written, validated, organized, retrieved, acted upon, updated, forgotten, audited, and sometimes rolled back. Across a 435-work coded corpus, treated as a scoped map rather than an exhaustive census, the literature concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it. We therefore introduce the Always-On Evaluation Protocol (AOEP-v0), a pilot evaluation contract that makes these governance requirements concrete by scoring state mutation and recovery obligations rather than answer quality alone. The resulting agenda connects always-on agents to databases, distributed systems, formal methods, capability security, and machine unlearning.

---


### 221. [FlexTab: A Flexible Encoder-Decoder Architecture for In-Context Learning Across Diverse Tabular Tasks](https://arxiv.org/abs/2606.30336)

**<font color=#1a73e8>作者：</font>** Marek Polewczyk, Maximilian Schambach, Marco Spinaci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce FlexTab, a flexible encoder-decoder architecture for in-context learning on tabular data that pairs a single, task-agnostic encoder with a suite of task-specific decoders. Unlike existing tabular in-context learners, which entangle feature representations with a specific prediction target, our design produces \textit{target-agnostic} row embeddings that can be leveraged across a wide range of downstream tasks within a table-native in-context learning setup. We demonstrate this flexibility on six distinct problems: classification, regression, anomaly detection, clustering, entity matching, and entity classification in relational databases. Both the encoder and the task-specific decoders are trained on a large corpus of real-world, unlabeled tables. FlexTab achieves state-of-the-art performance on classification, regression, anomaly detection and entity matching, while remaining competitive with specialized models on entity classification in a relational setting. These results demonstrate that a single shared encoder, paired with task-specific decoders, can serve as an effective general-purpose backbone for diverse tabular prediction problems. The inference code and checkpoints will be made publicly available at this https URL.

---


### 222. [REAR: Test-time Preference Realignment through Reward Decomposition](https://arxiv.org/abs/2606.30339)

**<font color=#1a73e8>作者：</font>** Fuxiang Zhang, Pengcheng Wang, Chenran Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with diverse user preferences is a critical yet challenging task. While post-training methods can adapt models to specific needs, they often require costly data curation and additional training. Test-time scaling (TTS) presents an efficient, training-free alternative, but its application has been largely limited to verifiable domains like mathematics and coding, where response correctness is easily judged. To extend TTS to preference alignment, we introduce a novel framework that models the task as a realignment problem, since the base model often fails to sufficiently align with the stated preference. Our key insight is to decompose the underlying reward function into two components: one related to the question and the other to preference information. This allows us to derive a REAlignment Reward (REAR) that selectively rescales the proportions of these two reward terms. We then show that REAR can be formulated as a linear combination of token-level policy log-probabilities, making it computationally efficient and easy to integrate with various TTS algorithms such as best-of-$N$ sampling and tree search. Experiments show that compared to other test-time baselines, REAR not only enables scalable test-time realignment for preference alignment tasks under diverse user requirements, but also generalizes to mathematical and visual tasks under appropriate preference settings.

---


### 223. [Residual-Guided Expert Specialization for Incomplete Multimodal Learning](https://arxiv.org/abs/2606.30355)

**<font color=#1a73e8>作者：</font>** Seunghun Baek, Jihwan Park, Jaeyoon Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As real-world prediction systems often face missing modalities at inference, incomplete multimodal learning (IML) remains a practical challenge. While prior methods aim to learn representations robust to missing inputs, representations from incomplete modalities inevitably deviate from their full-modality counterparts due to missing evidence. To explicitly leverage these deviations, we propose MARS (Missingness-Aware Residual-guided Specialization), a mixture-of-experts framework that guides expert specialization based on how representations are reshaped by missingness. By contrasting task representations derived from incomplete inputs with their complete counterparts during training, we derive a privileged residual signal that captures this representational gap. The residual signal guides a residual router to assign samples to experts specialized for the corresponding deviation patterns. In parallel, a feature router learns to imitate this routing behavior using only incomplete inputs, enabling deployment without access to full modalities. To mitigate this train-test router gap, we develop a discrepancy-aware noise regularization that adaptively perturbs the residual router's decisions when the feature router deviates, enhancing expert robustness under imperfect imitation. Experiments on multimodal classification (CASIA-SURF, CREMA-D, UPMC Food-101) and segmentation (MCubeS) under missing scenarios show that MARS consistently surpasses baselines while remaining efficient and extensible to diverse backbones and tasks.

---


### 224. [Using Large Language Models as Low-Cost Statistical Estimators for Human-Response Data](https://arxiv.org/abs/2606.30372)

**<font color=#1a73e8>作者：</font>** Haobo Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative research across the social and behavioral sciences depends on human subject experiments that are expensive, slow, and subject to sampling bias. Here we show that pretrained large language models induce risk-equivalent estimators of conditional expectations under squared loss, establishing restricted functional risk equivalence: under squared loss, the LLM induces an estimator whose risk matches the Bayes optimal risk for squared-loss prediction of conditional expectations for any inference that depends on the data only through the conditional mean. We formalize the LLM as a misspecified functional estimator $T(\hat{P}_n)$ trained on i.i.d.\ data, decompose the estimation error into representation bias $\epsilon_{\mathrm{rep}}$ and optimization error, and prove that under mild regularity conditions the LLM's expected error converges to the irreducible population variance plus the squared representation bias, with the representation bias bounded by the Pinsker inequality. The identifiability error $\delta$ propagates into the effective bias, inflating the asymptotic risk floor. We establish restricted functional risk equivalence via a bidirectional Le Cam deficiency analysis: the forward deficiency vanishes asymptotically while the reverse deficiency is exactly zero. We provide finite-sample concentration bounds and a calibration protocol with explicit decision rules. The result is a precise, provable statement: a well-calibrated LLM achieves the Bayes-optimal risk for conditional-mean-dependent inference, bounded by explicit scope conditions. In practical applications, this means that under satisfied conditions and well-calibrated models, large language models can be used in many prediction and decision-making tasks that originally relied on human experiments, approximating near-optimal statistical inference at lower cost.

---


### 225. [OmniCoT: A Benchmark for Global and Multi-Step Panoramic Reasoning](https://arxiv.org/abs/2606.30378)

**<font color=#1a73e8>作者：</font>** Haocong He, Chenfei Liao, Zichen Wen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated promising spatial reasoning capabilities, while these abilities remain underexplored in the emerging visual modality of panoramic imagery. The full 360°$\times$180° field of view of panoramas essentially supports complex global multi-step reasoning, which is also the fundamental advantage of panoramas in applications such as embodied intelligence. However, existing panoramic benchmarks largely focus on simplistic queries that rely on local cues or single-/few-step reasoning, thereby ignoring the fundamental advantage of panoramas and failing to fully exploit their potential. To address this gap, we introduce OmniCoT, a panoramic spatial reasoning suite designed to enable MLLMs to use global evidence and perform multi-step inference across viewpoints. It includes OmniCoT-B (6.7K data) for evaluation, which measures both answer accuracy and reasoning quality, OmniCoT-Real (1K data) as a manually annotated real-world subset to quantify the Sim-to-Real gap. For training, OmniCoT-T (14.3K data) is purpose-built with structured stepwise Chain-of-Thought annotations that explicitly link intermediate reasoning steps to panoramic evidence. Based on OmniCoT-T, we introduce OmniCoT-R1 and adopt a two-stage training strategy tailored to the geometrically complex panoramic space, where Supervised Fine-tuning (SFT) anchors reasoning to panoramic evidence (e.g., bearings, proximity) and GRPO penalizes geometrically incoherent paths to consolidate global 360° spatial consistency. Through OmniCoT, we aim to recalibrate the difficulty of panoramic spatial reasoning to better align with the intrinsic capabilities of panoramic imagery, thereby fostering meaningful progress in this research area.

---


### 226. [Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents](https://arxiv.org/abs/2606.30383)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A rapidly growing class of LLM agents is multi-party: the agent acts for a principal (who briefs it, sends follow-ups, and receives results) while also conversing in a separate channel with a counterparty whose interests may diverge (negotiating with a vendor, screening inbound requests, or mediating between employees). Here "help whoever you are talking to" is the wrong objective. The agent must stay loyal to the principal it represents without over-refusing the principal's own cooperative asks. We study this multi-party loyalty problem and contribute a measurement instrument, two mechanisms, and a structural lesson. PrincipalBench is a 75-item multi-turn benchmark with leak probes, dual judges, and an integrity-audit gate. Across 13 frontier subjects it exposes a sharp split (<=20% vs. 53.6-75.3% harm) invisible to single-turn safety evaluations: a selective cluster that declines adversarial probes while still following the principal's legitimate requests, and an over-refusing cluster that refuses broadly. (M1) A prompt-time loyalty scaffold (a fixed system prompt of seven prioritized rules, open-coded from 50+ failure trajectories) holds Claude-Sonnet to 19.4% harm and all nine selective subjects to <=20%. (M2) A per-token-KL distillation recipe transfers a prompted Qwen3-32B teacher into 8B Qwen3 and Llama-3.1 students, the strongest open-weight recipe we measure. (Lesson) Both mechanisms only move along a common leak/over-refusal trade-off rather than crossing it: improving one axis costs the other, and the jointly favorable outcome stays out of reach.

---


### 227. [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/abs/2606.30389)

**<font color=#1a73e8>作者：</font>** Tianyu Wang, Gourav Rattihalli, Aditya Dhakal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic sparse attention (DSA) accelerates long-context LLM decoding by attending to only the top-K KV blocks relevant to each query, but it introduces a serialized selection-to-attention dependency that emerges as a new latency bottleneck. We present PRR, a speculate-reuse-repair runtime that exploits temporal locality in DSA selections to predict likely blocks, speculate the attention over them while selection is in flight, and incrementally repair missed blocks once the true selected set is known. PRR uses a lightweight EMA-based predictor, a profiling-guided speculation budget that keeps speculative work off the critical path, and a FlashAttention-based repair kernel that folds missed blocks into the partial attention state using online-softmax statistics. Across long-context benchmarks and representative DSA methods, PRR reduces per-token decoding latency by up to 40% while preserving downstream task accuracy. Github: this https URL

---


### 228. [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406)

**<font color=#1a73e8>作者：</font>** Wenhan Ma, Jianyu Wei, Liang Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) rely on reinforcement learning during post-training to push specific capabilities, yet integrating multiple capabilities into one model remains hard. Existing methods, such as Off-Policy Finetune and Mix-RL, are either inefficient or lose performance. In this work, we propose Multi-teacher On-Policy Distillation (MOPD), a post-training paradigm for combining the capabilities of multiple domain RL teachers: we first run per-domain specialised RL to obtain a set of domain teachers, then distill these teachers into the student on its own rollouts. This eliminates exposure bias and provides a dense optimization signal. On Qwen3-30B-A3B, MOPD outperforms Mix-RL, Cascade RL, Off-Policy Finetune, and Param-Merge baselines, inheriting nearly all of each teacher's capability. MOPD also enables parallel, independent development of domain teachers, removing the cross-domain coupling typical of multi-domain post-training. MOPD has been deployed in the post-training of MiMo-V2-Flash, an industrial-scale frontier model, demonstrating its practical value for capability integration in frontier-scale LLMs.

---


### 229. [Beyond IID: How General Are Tabular Foundation Models, Really?](https://arxiv.org/abs/2606.30410)

**<font color=#1a73e8>作者：</font>** Lennart Purucker, Andrej Tschalzev, Nick Erickson 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for predictive machine learning on tabular data have recently gained significant traction in academia and industry. Research communities across disciplines are increasingly evaluating tabular foundation models on diverse datasets and tasks. However, these task- and discipline-specific evaluations remain largely inaccessible to model researchers because benchmark software and evaluation protocols are fragmented. As a result, model researchers rely on standard benchmarks, which are mostly defined for tasks where tabular foundation models already excel. The most challenging scenarios are excluded, limiting meaningful progress in the field by focusing on marginal improvements on IID data rather than on broader, more demanding challenges. To overcome this, we introduce BeyondArena, the first unified holistic benchmark for tabular data that supports diverse task types (IID, temporal, grouped), across sample size and feature dimensionality scales, with diverse feature types (with text, with high cardinality) from a broad range of disciplines. To enable unified benchmarking beyond standard benchmarks, we introduce Data Foundry, a Python framework and metadata schema for curating tabular datasets for predictive machine learning. Our results across 11 models and 142 curated datasets show that existing tabular foundation models excel on tiny- to medium-sized IID data, while traditional tree-based and deep learning models still dominate on non-IID, large, and high-dimensional datasets. BeyondArena guides model research for the most demanding challenges in tabular data, enabling progress towards truly foundational tabular models.

---


### 230. [Diffusion Fine-tuning with Rewarded Moment Matching Distillation](https://arxiv.org/abs/2606.30414)

**<font color=#1a73e8>作者：</font>** Alexis Jacq, Guillaume Couairon, Valentin De Bortoli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation and Reinforcement Learning (RL) fine-tuning are the primary pillars of diffusion post-training. While traditionally studied in isolation, the interaction between these phases remains poorly understood, and in particular how fine-tuning impacts the generative quality of distilled models. We introduce Rewarded Moment Matching Distillation (RMMD), a novel framework that simultaneously distills diffusion models and maximizes a reward function. RMMD preserves the high-fidelity ``naturalness'' characteristic of advanced distillation (such as 8-step Moment Matching) by adapting the sampling loop for on-policy training and repurposing the distillation loss as a proxy for integral KL regularization. By evaluating the FID-Reward Pareto fronts on ImageNet, we demonstrate that RMMD achieves superior trade-offs compared to single-step baselines (DI++) and multi-step competitors (DRaFT, HyperNoise). Finally, we apply RMMD to GenCast, a state-of-the-art weather forecasting model, to distill it while optimizing the Continuous Ranked Probability Score (CRPS) metric. The resulting distilled model achieves a 7.5x speedup while outperforming the teacher model on 93% of target weather variables, and being better calibrated. This proves that RMMD scales to complex, high-dimensional scientific domains.

---


### 231. [Experience Augmented Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.30420)

**<font color=#1a73e8>作者：</font>** Jinda Lu, Kexin Huang, Junkang Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is a powerful paradigm for improving the reasoning capabilities of large language models (LLMs). However, existing RLVR methods typically rely on on-policy optimization from scratch, resulting in high sampling costs and inefficient utilization of accumulated experience. As model capabilities and policy behaviors evolve during training, recent attempts to reuse experience via fixed reasoning trajectories further suffer from policy mismatch. Motivated by these limitations, we argue that experience in RLVR should not be reused as fixed reasoning trajectories, but instead expressed in a policy-adaptive manner. In this work, we propose Experience-Augmented Policy Optimization (EAPO), which leverages a prior RL-optimized policy as an action-level experience prior and selectively injects experience at critical decision points during rollout. To ensure stable and unbiased learning from experience-augmented rollouts, EAPO further incorporates an adapted importance sampling scheme. Experiments on using Qwen-2.5-math 7b and Qwen-3-8B on five different benchmarks demonstrate that EAPO consistently improves reasoning performance over state-of-the-art RLVR methods.

---


### 232. [OWMDrive: Causality-Aware End-to-End Autonomous Driving via 4D Occupancy World Model](https://arxiv.org/abs/2606.30421)

**<font color=#1a73e8>作者：</font>** Junjie Cheng, Ruiqi Song, Ye Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems are steadily moving toward end-to-end paradigms to mitigate the limited adaptability of rule-based pipelines in complex traffic environments. However, most existing learning-based methods still make decisions from static representations of the current scene, without explicit future rollouts or modeling of the temporal causal dynamics in traffic interactions. This limitation often results in unstable or overly conservative planning under high-uncertainty conditions, such as occlusions and unexpected events. To overcome these challenges, we introduce OWMDrive, a generative end-to-end driving framework built upon an Occupancy World Model for multi-step 3D occupancy forecasting, which serves as a conditional prior to guide diffusion-based planning. Conditioned on both current observations and predicted future states, the planner iteratively refines trajectory candidates to generate a reinforced driving trajectory. By explicitly modeling scene evolution over future horizons, OWMDrive captures key spatiotemporal causal dependencies, which leads to more foresighted and robust trajectory generation. Extensive experiments demonstrate that OWMDrive significantly improves planning reliability and safety, especially in challenging and partially observable driving scenarios.

---


### 233. [Arko-T: A Foundation Model for Text-to-Structured 3D Generation](https://arxiv.org/abs/2606.30429)

**<font color=#1a73e8>作者：</font>** Liang Wang, Zhaoyang Xi, Zekai Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-3D systems can now synthesize a mechanical part from a single sentence, yet the result is a shape to render, not a design to edit. We present Arko-T, a 4B-parameter text-to-design model that maps natural-language intent directly into executable, parametric CAD programs. Rather than optimizing for code executability alone, Arko-T aligns every stage of the pipeline to a formal notion of design state, so that data curation, code normalization, and execution-grounded supervision all work to preserve the features, parameters, and construction logic that make a CAD artifact editable. Benchmarked against seven frontier LLMs across 12 metrics, Arko-T attains the best score on 8 and the second-best on 3 more, at roughly one-tenth the per-benchmark cost. The results suggest that targeted design-level training at moderate scale can match frontier general-purpose models on structured CAD generation.

---


### 234. [Translating Natural Language to Strategic Temporal Specifications via LLMs](https://arxiv.org/abs/2606.30441)

**<font color=#1a73e8>作者：</font>** Marco Aruta, Francesco Improta, Vadim Malvone 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A rigorous formalization of system requirements is a fundamental prerequisite for the verification of Multi-Agent Systems (MAS). However, writing correct formal specifications is well known as an error-prone, time-consuming, and expertise-intensive task. This difficulty is further accentuated in MAS, where requirements must capture strategic abilities and temporal objectives. At present, there is no established methodology for deriving MAS specifications from natural language. We present a framework for translating Natural Language descriptions of strategic requirements into well-formed ATL/ATL* formulas using Large Language Models (LLMs). Since no available dataset supports supervised learning for the NL-to-ATL/ATL* translation task, we create and curate a novel expert-validated dataset, employed for training and evaluating fine-tuned models. On a held-out test set, evaluated under the LLM judge that best agrees with expert annotations, in-domain fine-tuning of small open-weight models (3 - 7B parameters) matches strong few-shot proprietary API baselines. Our best fine-tuned system reaches 0.84 semantic accuracy, statistically on par with 0.86 for the strongest few-shot proprietary baseline, while keeping requirements on-premises. We further find that judge reliability is inverse to generator strength. The open-weight Llama-3.3-70B tracks human verdicts most closely, whereas the strongest proprietary models are the least reliable judges, over-rejecting faithful paraphrases of the reference. To assess the practical applicability of the generated specifications, we embed our tool to an existing strategic logics model checker, enabling non-expert users to specify strategic properties in natural language.

---


### 235. [When Does Online Imitation Learning Help in LLM Post-Training? The Role of (Non-)Realizability Beyond Horizon](https://arxiv.org/abs/2606.30445)

**<font color=#1a73e8>作者：</font>** Huaqing Zhang, Jingchu Gai, Juno Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online imitation learning (IL), particularly on-policy distillation, has emerged as a strong LLM post-training approach, often outperforming offline supervised fine-tuning (SFT). Yet a principled understanding of when and why online interaction helps remains unclear. In this work, we challenge the view that error accumulation is the main source of online IL's advantage, and instead show that the benefits of online interaction depend critically on whether the setting is realizable, i.e., whether the student policy class can represent the expert policy. Under realizability, we empirically find that offline IL already matches expert performance. In contrast, in non-realizable (misspecified) settings, we prove that offline IL encounters an information-theoretic bottleneck even when horizon $H=1$, and propose a structural characterization of misspecification relative to the reward, under which online IL provably achieves high performance despite a large distributional mismatch between the expert and student policies.

---


### 236. [Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring](https://arxiv.org/abs/2606.30449)

**<font color=#1a73e8>作者：</font>** Max Fomin, Elad David, Amit LeVi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probes on model internals could help monitor agentic systems if they identify harmful text or tool actions before those actions are generated. We ask when an internal readout supports this stronger pre-action claim, rather than merely describing the prompt, construction contrast, or current trajectory. We test three methods across three model families: a Qwen2.5-Coder-32B-Instruct fine-tune/base direction, Llama-3.1-8B-Instruct probes at the last token of unsafe prefills, and Gemma-3-27B-IT emotion-concept vectors used for projection and steering in a blackmail tool-action scenario. Across these cases, construction validity, semantic legibility, and steering effects do not become robust pre-action monitors: each is undercut by a generalization or specificity check. The Qwen direction separates fine-tune from base at AUC 1.000, yet crosses its threshold on 0/143 audited pre-assistant turn contexts and on 0/342 Qwen prefill rows where the model continues the unsafe trajectory. The Llama features decode prompt domain almost perfectly (AUC 0.999), while the best future-behavior probe reaches AUC 0.801 and only +5.1 pp accuracy lift over majority; single-source cross-domain transfer is non-positive on five of six ordered pairs. Gemma emotion projections are semantically meaningful, but a shared-prefix minimal pair has indistinguishable states before the first differing input, and steering specificity weakens against unrelated learned directions such as cats}, weather, sports, and geography. We contribute a methodology for converting internal-readout claims into pre-action tests, and report scoped negative results: monitor claims must survive both scenario/action generalization and concept-specificity controls. Code is released at this https URL

---


### 237. [Field Order Should Not Matter: Permutation-Invariant Embedding Model Fine-Tuning for Structured Metadata Retrieval](https://arxiv.org/abs/2606.30473)

**<font color=#1a73e8>作者：</font>** Aivin V. Solatorio, Olivier Dupriez, Rafael Macalaba  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study retrieval over catalogs of structured metadata, where each record is a small schema whose fields answer different kinds of query. Embedding a record with a text encoder first serializes its fields into a string, which forces a choice of field order. We show this choice, usually treated as an implementation detail, silently controls retrieval quality once the encoder is fine-tuned. A standard fine-tune loses 7.4 nDCG@10 points when the index is rebuilt under a different field order, because it reads absolute position instead of the field labels. We propose permutation-invariant fine-tuning ($\textbf{PI-FT}$), which serializes each record under a freshly sampled field order with random field dropout, so meaning binds to the labels rather than to position. The change is about two lines in the data loader; it costs negligible in-distribution accuracy and cuts the order-change penalty to 0.2 points. We study this in the discovery of development statistics, a catalog of nearly 10,000 indicators that should be searchable in many languages by a model small enough to self-host. As AI assistants and agents increasingly mediate access to public data and statistics, this retrieval step decides whether an answer is grounded in the right indicator or series, making discoverability a precondition for disseminating data through AI. Because usage logs cannot provide training signal for indicators no one has searched, we generate the queries instead. $\textbf{DevDataBench}$ is a fully LLM-generated benchmark of grounded, facet-targeted queries across 15 languages, covering every indicator for both training and evaluation. A fine-tuned 118M-parameter CPU encoder outperforms every zero-shot baseline, including $\texttt{text-embedding-3-large}$ (0.707 vs.\ 0.556 nDCG@10), with the largest gains in low-resource languages. We release the benchmark, pipeline, models, and a reusable PI-FT framework.

---


### 238. [Regime-Aware Peer Specialization for Robust RAG under Heterogeneous Knowledge Conflicts](https://arxiv.org/abs/2606.30518)

**<font color=#1a73e8>作者：</font>** Bo Wang, Heyan Huang, Yaolin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves language models by grounding generation in external context. However, it can be fragile when the retrieved context conflicts with the model's parametric knowledge. Such conflicts span a reliability spectrum, ranging from reliable and partially reliable evidence to adversarial context. Existing remedies often handle such heterogeneous conflicts with regime-agnostic supervision, which can conflate incompatible learning signals across reliability regimes. To disentangle these signals, we propose RAPS-DA, a regime-aware peer specialization framework that addresses conflict at two complementary granularities. At the sample level, conflicts are divided into three regimes, including Grounding, Arbitration, and Resistance, with one same-scale peer specialist trained per regime from a shared base model. Each sample is then hard-routed to its regime-matched peer for on-policy reverse-KL supervision. At the token level, a dual-layer selector uses inter-teacher disagreement, student-teacher divergence, and student entropy to filter uninformative or unstable tokens, upweight confidently misaligned ones, and gradually focus supervision on high-conflict tokens as the student matures. Gains stem from specialization at a fixed model scale, not from a stronger teacher, and the peer specialists exist only during training, so the deployed student requires no regime labels or peer access. Experiments on five conflict scenarios and two out-of-distribution benchmarks show RAPS-DA surpasses all prompting, decoding, fine-tuning, RL, and single-teacher baselines.

---


### 239. [$μ$Flow: Leveraging Average Images for Improving Generalisation of Deepfake Faces Detectors](https://arxiv.org/abs/2606.30528)

**<font color=#1a73e8>作者：</font>** Orazio Pontorno, Mattia Litrico, Luca Guarnera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current generative models, including GANs and diffusion models, have reached an outstanding level of photorealism, posing significant risks to privacy and security. To ensure real-world applicability, deepfake detectors must generalise effectively to unseen generators. However, most existing approaches rely on supervised training with both real and fake images, which limits their generalisation especially across generators categories (e.g. GANs vs DMs). In this work, we introduce $\mu$Flow, a one-class deepfake detector trained only on real images without relying on pseudo-deepfakes or synthetic artifacts. Our approach builds on the observation that averaging multiple images amplifies consistent generative traces, producing highly discriminative feature representations. We leverage this property by modelling the distribution of features extracted from averaged images and training a normalizing flow to align the feature space of individual images with this distribution. This alignment yields a likelihood-based criterion that separates real and fake samples while promoting strong generalisation. We evaluate $\mu$Flow on a fully out-of-distribution setting, where both real and fake datasets are unseen during training. Experimental results show that our method significantly outperforms SOTA detectors. Project page: this https URL.

---


### 240. [Poller: Are LLMs Suitable for Evaluating the Poetry Understanding Task?](https://arxiv.org/abs/2606.30556)

**<font color=#1a73e8>作者：</font>** Shanshan Wang, Derek F. Wong, Jingming Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional automatic evaluation methods have been shown to be unsuitable for modern Chinese poetry because of the distinct nature of this literary genre. Human evaluation remains reliable, but is expensive and not applicable to large-scale data. In this paper, we propose Poller (Poetry LLM Evaluator), a novel method leveraging large language models (LLMs) to evaluate the poetry understanding task. Specifically, our method requires LLMs to play the role of a poem's author with detailed information, thereby emulating human evaluation and judgment by adopting the poet's perspective. We conducted comprehensive experiments on multiple LLMs, evaluating the interpretations of poems across eight specialized dimensions. Experimental results demonstrate that our method effectively reduces the evaluation error between LLMs and humans. Especially for specific dimension evaluation, Poller-based LLMs achieve a 94.55% and 89.53% error reduction for rhetorical techniques and defamiliarization, respectively, compared to baseline methods. These performances are unattainable by conventional LLM evaluation methods. Experimental results from multiple LLMs across various dimensions validate the efficacy of our method. This work bridges the gap between automated efficiency and human expertise, establishing a foundation for automated evaluation in poetry-related tasks.

---


### 241. [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560)

**<font color=#1a73e8>作者：</font>** Kan Zhu, Mathew Jacob, Chenxi Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents are rapidly becoming a major application of agentic LLMs, but serving them efficiently remains challenging. Progress on this challenge requires understanding real workload patterns, yet the data needed for such analysis is largely absent. Existing public traces and benchmarks do not capture real, day-to-day coding-agent usage across multiple agents and model families for serving-system analysis. To help fill this gap, we collect and release a trace of roughly 4,300 coding-agent sessions, containing about 350,000 LLM steps and 430,000 tool calls from our own day-to-day use of Claude Code and Codex. Our analysis shows that coding-agent workloads feature long autonomous loops, long contexts with short outputs, diverse and heavily-tailed tool calls, and high but imperfect prefix cache hit rates. These findings point to concrete opportunities for optimizing serving, including lower-overhead tool calling, append-length-aware prefill, semantic-aware tool-latency prediction, and improved KV-cache management around human-paced gaps. We release the dataset, trace collection pipeline, and analysis code at this https URL the project website is this https URL.

---


### 242. [Attractor States Emerge in Multi-Turn LLM Conversations](https://arxiv.org/abs/2606.30571)

**<font color=#1a73e8>作者：</font>** Ting-Wen Ko, Jonas Geiping  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in open-ended multi-agent settings, but the long-run dynamics of model--model interaction remain poorly understood. We study whether open-ended LLM discussions exhibit attractor-like behavior, i.e. topic-independent stable sets of behaviors which conversations settle into. Across 7 LLMs and 20 controversial topics, we compare self-play and mixed-play dyadic debates, tracking trajectories in representation space, discourse traits, and stances. We find self-play trajectories to be model-specific attractors that draw their conversation partners asymmetrically in mixed-play debates, influencing the other models' stylistic choices and behavior. For example, Claude Haiku is a strong attractor of other models in latent space, corresponding to other models taking on its traits like metacommentary, and models like GPT-4.1 nano are especially malleable. Our results suggest that open-ended LLM interactions are partially predictable from model-specific attractors, but shaped by structured and asymmetric partner influence. Overall, our analysis sheds some light on the complex behavior of open-ended multi-agent interaction, which we hope is helpful in designing, predicting, and monitoring autonomous agentic systems in the real world.

---


### 243. [Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent](https://arxiv.org/abs/2606.30616)

**<font color=#1a73e8>作者：</font>** Lei Bai, Zongsheng Cao, Yang Chen 等 50 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Agents-A1, a 35B Mixture-of-Experts Agentic Model that reaches trillion-parameter-level performance by scaling the agent horizon. We investigate agent-horizon scaling from two perspectives: scaling long-horizon trajectories and scaling heterogeneous agent abilities. To support this goal, we build a long-horizon knowledge-action infrastructure that connects external knowledge, actions, observations, and verifier outcomes, producing agentic trajectories with an average length of 45K tokens. Based on this, we train Agents-A1 with a three-stage recipe. First, we perform full-domain supervised fine-tuning to align the base model with broad agentic behaviors. Second, we train domain-level teacher models to capture specialized expertise in each domain. Third, we propose a multi-teacher domain-routed on-policy distillation with salient vocabulary alignment to improve knowledge transfer efficiency across different domains, unifying six heterogeneous domains into one deployable student model. Agents-A1 achieves strong and broad performance for long-horizon agent benchmarks. Compared with 1T-parameter model such as Kimi-K2.6 and DeepSeek-V4-pro, Agents-A1 achieves leading results on SEAL-0 (56.4), IFBench (80.6), HiPhO (46.4), FrontierScience-Olympiad (79.0), and MolBench-Bind (56.8), and remains highly competitive on SciCode (44.3), HLE (47.6) and BrowseComp (75.5). We hope this work provides the community with a practical path for scaling the horizon using a 35B agent that can reach or match the performance of 1T models on long-horizon tasks.

---


### 244. [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626)

**<font color=#1a73e8>作者：</font>** Xinlei Yu, Gen Li, Qingyi Si 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) offers superior capacity transfer by supervising student-sampled trajectories with dense token-level signals. To furnish high-quality supervision sources and thereby elevate the performance frontier of distillation, an intuitive direction is to infuse privileged information to either teacher or student itself. However, this additional input induces a potential failure mode we dub privilege illusion: a pattern that conflates the transferable capability gap that students are meant to close, and the information asymmetry gap that can only be mimicked but never replicated. This issue is further amplified by the inherent non-uniformity of token-level supervision, where only a small subset of tokens carries pivotal capability-bearing signals. To this end, we propose DOPD, an advantage-aware dual distillation paradigm that dynamically routes token-level supervision between privileged teacher and privileged student policies based on their advantage gap and relative probabilities. Each token receives supervision of different strength, objective, and strategy from either teacher or student itself, which transfers credible capability while simultaneously receiving auxiliary signals, to alleviate privilege illusion. Extensive experiments on both large language model (LLM) and vision-language model (VLM) settings demonstrate that DOPD consistently outperforms Vanilla OPD and other counterparts. Further results on stability, robustness, continual learning, and out-of-distribution tasks validate its superiority.

---


### 245. [Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models](https://arxiv.org/abs/2606.30627)

**<font color=#1a73e8>作者：</font>** Subramanyam Sahoo, Aman Chadha, Vinija Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conservative offline training is widely advocated as a safe foundation for subsequent online adaptation: if a policy stays close to well-supported behaviour, the argument goes, it is less likely to exploit imperfections in a learned reward model. We challenge this intuition empirically and mechanistically. We train a Qwen3-14B policy under Direct Preference Optimisation (DPO) with three levels of conservatism ($\beta \in \{\beta_{\mathrm{lo}}, \beta_{\mathrm{mid}}, \beta_{\mathrm{hi}}\}$ derived from empirical log-ratio percentiles), then adapt each checkpoint online against a learned reward ensemble (3\,$\times$\,Qwen3-1.7B) while measuring true performance on GSM8K exact-answer accuracy. We find that \emph{higher offline conservatism monotonically increases reward-hacking damage}, measured by the Goodhart gap and its area under the curve (AUGC), with Spearman $\rho = 1.0$ across all three conditions. Mechanistic analysis reveals a three-link causal chain: (i) high-$\beta$ DPO compresses policy entropy, (ii) Low-entropy policies generate responses with reduced diversity, concentrating in a narrow region of the reward model's training distribution (lower pairwise cosine distance), and (iii) despite this proximity, ensemble disagreement (epistemic uncertainty) increases with $\beta$ and is exploited faster during online optimisation. We further fit a power-law curve to the $(\beta, \augc)$ data and identify a practical optimal conservatism level $\beta^{\star}$ that balances alignment fidelity against hacking vulnerability. Our results suggest that the field needs \emph{calibrated}, not \emph{maximal}, conservatism.

---


### 246. [One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining](https://arxiv.org/abs/2606.30634)

**<font color=#1a73e8>作者：</font>** Philip Zmushko, Egor Petrov, Nursultan Abdullaev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large-scale LLM pretraining benefits from utilizing Pipeline Parallelism; however, synchronous implementations leave GPUs idle during pipeline bubbles, wasting computational resources. Asynchronous Pipeline Parallelism eliminates these bubbles, maximizing throughput at the cost of gradient staleness. Among asynchronous schedules, PipeDream-2BW is particularly appealing: unlike the original PipeDream schedule, it ensures a constant one-step gradient delay regardless of pipeline depth. However, its adoption remains limited due to the common belief that optimizing under staleness is fundamentally unstable. In this work, we challenge this assumption, demonstrating that degradation under one-step delay depends strongly on optimizer choice rather than being an intrinsic limitation. We provide the first comprehensive empirical analysis showing that while AdamW, the predominant optimizer at the time when PipeDream-2BW was introduced, indeed suffers from severe degradation, recent methods like Muon exhibit strong robustness under a one-step delay. We introduce an optimizer-agnostic Error Feedback-inspired correction to further mitigate delay effects. We provide supporting theoretical analysis demonstrating convergence for Muon with and without this correction. Extensive evaluation on models up to 10B parameters confirms that our strategies bridge the performance gap with synchronous training, highlighting the practical potential of asynchronous pipeline parallelism at scale.

---


### 247. [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639)

**<font color=#1a73e8>作者：</font>** Xuan Zhang, Wenxuan Zhang, See-Kiong Ng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory, which extracts persistent heuristic rules from prediction-observation mismatches; and (iii) Selective Foresight, which filters low-confidence predictions before integrating them into agent reasoning context. We evaluate WorldEvolver on ALFWorld and ScienceWorld, measuring world model prediction accuracy on Word2World and downstream agent success rate on AgentBoard. Extensive experiments show that WorldEvolver achieves the highest prediction accuracy across three backbones and leads other world model baselines on downstream agent success rate, demonstrating that test-time memory revision enhances both predictive fidelity and planning performance.

---


> [!TIP]
> 当前位于：**201-247**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-247**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
