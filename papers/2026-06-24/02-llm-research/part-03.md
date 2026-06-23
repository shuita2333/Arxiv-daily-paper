# 🧠 大模型相关研究 | 2026年06月24日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 101. [Evaluation of Small Language Models for Arabic Language Processing](https://arxiv.org/abs/2606.21460)

**<font color=#1a73e8>作者：</font>** Jumana Alsubhi, Ahmed Alhusayni, Abdulrahman Gharawi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper evaluates the performance of twelve Small Language Models (SLMs) on Arabic natural language processing tasks. The study introduces a benchmark of 240 Arabic test items distributed across eight domains and ten language skills, covering both comprehension-oriented and generation-oriented tasks. All models were evaluated under a controlled zero-shot setting using a standardized Arabic-only prompt template. Model responses were assessed through a multi-model LLM-as-a-judge framework involving GPT-4.1 Mini, Claude Haiku 4.5, and DeepSeek-Chat, with scores aggregated across judges and analyzed by task, skill, and model family. The results show that Gemma 3 (12B) achieved the highest overall score (4.548/5), followed by Aya and C4AI Command Arabic. The observed results suggest that model size alone does not explain Arabic SLM performance. Models with stronger Arabic alignment and more reliable instruction-following behavior tended to perform better across tasks. Common failure patterns among lower-performing models include prompt leakage, hallucination, language drift, incomplete generation, and weak task adherence. Overall, the benchmark provides a structured reference for evaluating compact Arabic language models and supports future work on efficient, reliable, and culturally appropriate Arabic AI systems.

---


### 102. [Balancing Performance and Diversity in GRPO Autoregressive Text-to-Image Post-Training](https://arxiv.org/abs/2606.21498)

**<font color=#1a73e8>作者：</font>** Yuanhao Chiang, Hongbo Duan, Chunru Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive text-to-image (T2I) generation has recently advanced rapidly, yet aligning generated images with human preferences remains challenging. GRPO-style online reinforcement learning provides an effective framework; however, existing methods typically treat reference-policy divergence as fixed, despite its direct impact on policy optimization. We study this overlooked factor within a unified f-divergence framework, encompassing forward KL, reverse KL, and JS divergence, for GRPO-style autoregressive T2I alignment. Our systematic theoretical analysis reveals that different divergences reshape token-level updates in distinct ways. In particular, under the sampled-token shaping form used, JS regularization achieves a favorable trade-off by mitigating uniform bias relative to the reference policy while still discouraging large deviations. Extensive experiments on LlamaGen and Janus-7B show that JS divergence achieves the strongest or highly competitive optimization performance on most evaluation metrics while maintaining favorable generation diversity. The code is available at this https URL.

---


### 103. [Towards Pedagogically Aligned LLM Tutors for Math Mistake Remediation](https://arxiv.org/abs/2606.21502)

**<font color=#1a73e8>作者：</font>** Kseniia Petukhova, Tien Dat Nguyen, Ekaterina Kochmar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have strong potential for use in intelligent tutoring systems, but they often fail to follow effective pedagogical strategies, such as guiding students without revealing final answers. We study the application of a two-stage alignment pipeline for math mistake remediation, combining supervised fine-tuning on tutoring dialogs with Direct Preference Optimization on synthetic preference pairs. We construct a dataset that integrates existing tutoring corpora with synthetic data generated along pedagogical dimensions, such as scaffolding and factuality, and study different input configurations that incorporate solution correctness and gold answers. Experiments show that this approach improves both factual accuracy and pedagogical quality over base models and existing tutoring models. Human evaluation further indicates that our best model is competitive with a strong proprietary baseline, while providing additional benefits in terms of openness, transparency, and reproducibility. Our results highlight the effectiveness of preference-based pedagogical alignment, while also revealing challenges in reliably evaluating tutoring quality.

---


### 104. [Dissecting Agentic RAG: A Component Ablation for Multi-Hop QA with a Local 7B Model](https://arxiv.org/abs/2606.21553)

**<font color=#1a73e8>作者：</font>** Sheroz Shaikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) systems combine iterative reasoning loops, query decomposition, and adaptive retrieval to tackle multi-hop question answering. However, the contribution of each component remains poorly understood, particularly under resource-constrained settings using only local language models. Many agentic designs add adaptive retrieval routing and deeper retrieval loops on the assumption that the added complexity helps. To test whether it does, we run a controlled ablation study of a full agentic RAG pipeline evaluated on 5,000 questions from the HotpotQA distractor development set using a local 7B parameter model (Qwen2.5-7B-Instruct). Our full pipeline achieves EM=53.2% and F1=61.6%, compared to a single-pass dense-retrieval baseline of EM=43.1% and F1=54.0%. Across eight ablation conditions, we find that: (1) fixed hybrid retrieval via reciprocal rank fusion consistently outperforms rule-based adaptive routing (+1.8 EM, +1.9 F1), as the routing heuristic over-routes to BM25 by firing on named entities present in nearly all multi-hop sub-questions; (2) two retrieval iterations over the decomposed sub-questions capture 95% of the gains of five, with no meaningful benefit from deeper loops; and (3) query decomposition and cross-encoder reranking each contribute statistically significant but smaller gains (p<0.01 and p<0.001 respectively). Taken together, on a fixed local-model budget, the simpler and fixed choices turn out to be competitive with or better than their adaptive versions: most of the gain comes from running a short retrieval loop, not from adaptive routing or from many iterations. We use no proprietary APIs or large-scale compute.

---


### 105. [Rubric-as-Experts: Case-Specific MQM Rubrics for Translation Quality Evaluation](https://arxiv.org/abs/2606.21559)

**<font color=#1a73e8>作者：</font>** Weilu Xu, Yunzhi Shen, Xinye Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential in fine-grained translation quality evaluation (QE), yet existing MQM-based approaches typically rely on fixed rubric configurations shared across all translation samples. However, translation instances often differ substantially in error complexity, ambiguity, and required evaluation granularity, making static rubric allocation suboptimal for span-level error detection. We find that larger MQM subtype spaces improve error coverage but also introduce more false positives, while different translation instances prefer different rubric granularities, suggesting that evaluation spaces should be allocated dynamically for each case. Motivated by these observations, we propose a case-specific dynamic rubric framework that adaptively constructs MQM evaluation spaces for individual translation instances. Unlike fully free-form rubric generation methods, our framework remains grounded in the predefined MQM taxonomy while dynamically selecting suitable subtype spaces and evaluation granularity for different cases. Experiments on WMT span-level QE benchmarks across multiple model scales demonstrate that the proposed framework consistently improves MCC and produces cleaner span-level error localization compared with static rubric settings. Our results suggest that combining structured MQM rubrics with case-specific adaptive allocation is an effective strategy for fine-grained LLM-based translation evaluation.

---


### 106. [Composing Verifiable Conceptual Models via Building Blocks: Towards Design-Time Verification of Agentic AI Workflows](https://arxiv.org/abs/2606.21565)

**<font color=#1a73e8>作者：</font>** Noe Y. Flandre, Alexander C. Nwala, Philippe J. Giabbanelli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems orchestrate multiple LLM-based agents through workflow architectures that coordinate decisions, tools, and external actions. While current platforms emphasize runtime safeguards, little support exists for verifying workflows during system design. From a Modeling \& Simulation perspective, this gap is analogous to composing conceptual models without verifying whether their building blocks interact coherently. We propose a design-time verification approach that models agentic workflows as compositions of reusable building blocks and checks their compatibility through twelve structural rules. We implemented these rules in a software prototype and evaluated them using two openly released datasets: 48 workflows with known design flaws and 168 variants that preserve workflow logic but alter graph structure. Results show that our verifier reliably detects violations even when flawed designs are obscured through structural transformations such as splitting tasks between agents. Future works could combine our verification with community repositories of building blocks to compose safe agentic workflows.

---


### 107. [$μ$Match: Foundation Models for Semi-supervised Learning and Domain Adaptation in EM](https://arxiv.org/abs/2606.21605)

**<font color=#1a73e8>作者：</font>** Marei Freitag, Olesia Korchevaia, Luca Freckmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have substantially advanced computer vision, enabling state-of-the-art performance in zero- and few-shot settings. They have been successfully applied to biomedical imaging tasks ranging from organ segmentation in computed tomography to cell segmentation in light microscopy. Electron microscopy (EM) is a central modality for analyzing cellular ultrastructure due to its nanometer-scale resolution. However, the application of foundation models in EM has so far been limited to specific organelles, such as mitochondria, largely due to the diversity of segmentation tasks and the scarcity of comprehensively annotated data. As a result, EM segmentation still predominantly relies on supervised learning, requiring extensive manual annotation and limiting ultrastructural analysis. To address this gap, we propose $\mu$Match, a framework for semi-supervised learning and domain adaptation that leverages foundation models. We implement state-of-the-art student-teacher-based methods and evaluate multiple foundation models (SAM, SAM2, $\mu$SAM, DINOv2/v3) on challenging EM tasks, including mitochondrion, nucleus, and neurite segmentation. Our results demonstrate consistent improvements over strong baselines and highlight a path toward substantially reducing the annotation effort in EM.

---


### 108. [LLM and Human Modes of Representation](https://arxiv.org/abs/2606.21616)

**<font color=#1a73e8>作者：</font>** Shalom Lappin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Much work on the cognitive foundations of AI has focussed on comparisons between the ways in which Large Language Models (LLMs) and humans process information and represent it. One aspect of this comparison involves determining the extent to which LLMs can achieve or surpass human performance on a variety of cognitively interesting tasks. A second explores points of convergence and divergence between LLM and human systems for processing information. Here, I consider some recent research that has addressed both issues in two informational domains. The first is the representation of linguistic knowledge. The second is real world reasoning and planning. While LLMs frequently achieve impressive levels of performance and fluency on linguistic applications, they tend to handle linguistic content in ways that are distinct from human processing. They are also, for the most part, less efficient than humans in learning and generalisation for reasoning tasks.

---


### 109. [CulMind: Benchmarking Multimodal Understanding and Reasoning in Chinese Cultural Heritage](https://arxiv.org/abs/2606.21618)

**<font color=#1a73e8>作者：</font>** Zhangwei Cao, Shuhan Fan, Yuting Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating Multimodal Large Language Models (MLLMs) in Chinese Cultural Heritage (CCH) requires fine-grained reasoning over visual, textual, stylistic, and historical clues. However, existing CCH benchmarks mainly emphasize final-answer accuracy, while the accuracy and completeness of reasoning processes remain underexplored. To address this gap, we introduce CulMind and CulMind-R: a high-quality benchmark for multimodal CCH covering 50 tasks from collections of more than 100 museums, and a 24-task reasoning subset that adaptively defines task-specific dimensions for reasoning process evaluation. To evaluate reasoning quality, we propose ReaScore, a task-adaptive metric that evaluates reasoning by automatically weighting task-relevant dimensions. Experiments on 14 leading MLLMs reveal a substantial gap between answers and reasoning, especially on challenging tasks. Further analysis shows that task-adaptive dimension selection and weighting better align evaluation results with expert judgments. Overall, our benchmark and metric support a more expert-aligned assessment of CCH understanding and offer a transferable reference for broader evaluations of cultural heritage. We publicly release the data, code, and evaluation scripts at this https URL to facilitate reproducible research.

---


### 110. [Counsel: A Meta-Evaluation Dataset for Agentic Tasks](https://arxiv.org/abs/2606.21627)

**<font color=#1a73e8>作者：</font>** Sashank Pisupati, Henry Broomfield, Eujeong Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic systems tackle increasingly complex multi-step tasks, evaluating their trajectories presents a major bottleneck - human annotation of a single trajectory on popular agentic benchmarks can take hours, making it difficult to scale evaluations for measuring performance or curating training data. This has driven widespread reliance on automated approaches such as LLM-as-a-judge (LLMJ) to critique agents at the process and outcome-levels at scale, however, the soundness of LLMJ critiques often goes unmeasured. Here, we introduce Counsel, the first public dataset of meta-evaluations for agentic tasks. Counsel consists of process-level critiques from open-weight LLMJs on two agent benchmarks: tau-bench (customer support agents) and DA-Code (coding agents), and human meta-evaluations of these critiques. Human annotators label critiques on each flagged error as "spot on", "correct location but poor reasoning", or "should not have flagged", achieving reliable inter-annotator agreement (Krippendorff's alpha of 0.78). The resulting dataset stratifies LLMJ critiques by human alignment across both error location within a trajectory and reasoning quality, serving as valuable data to calibrate, improve, or train LLMJs for agents. Comparing open-weight judges, we find that more capable judge models and more reasoning effort both enabled improved human agreement, with the strongest judge reaching ~88% agreement on location and ~65% on reasoning. Counsel is generated using open-weight models and is permissively licensed for broad community use, which we hope will enable rigorous study and improved alignment of LLM-based evaluators for agentic systems.

---


### 111. [CuratorKIT : Data Curation and Synthetic Data Generation for LLM Post-Training](https://arxiv.org/abs/2606.21631)

**<font color=#1a73e8>作者：</font>** Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data curation is a critical part of post-training pipelines for large language models, yet existing tools often treat ingestion, deduplication, synthetic generation, and quality filtering as separate stages. This fragmentation makes it difficult to audit pipeline decisions or understand why individual samples are rejected. CuratorKIT is an open-source Python library that covers this full lifecycle in a single configurable pipeline. The framework is composed of six source format readers and automatic schema detection, a pre-generation data hygiene layer for credentials, PII, and toxic content, eight LLM-powered generation tasks, three complementary quality gates with provenance-exact hallucination verification, structured adaptive recovery, and five training-ready export formats compatible with TRL, Unsloth, and AlignTune. Every pipeline decision is recorded in an append-only per-sample provenance chain, and rejected samples carry structured failure reasons rather than being silently discarded. CuratorKIT supports 100+ LLM providers through LiteLLM, exposes both a Python API and a YAML-driven CLI, and is designed for practitioners who need reproducible, auditable data pipelines at scale .

---


### 112. [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633)

**<font color=#1a73e8>作者：</font>** Omin Kwon, Doyeon Kim, Jongseok Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion LLMs (dLLMs) improve GPU utilization over autoregressive decoding by generating multiple tokens per forward pass, but their KV cache still grows linearly with context, limiting throughput at long contexts. KV cache offloading to host DRAM alleviates this memory pressure, but the limited PCIe bandwidth necessitates recalling only a sparse subset of KV entries. In block dLLMs, the relevant KV entries remain consistent across denoising steps within a block, enabling high-accuracy selection by identifying the top-k entries once and reusing them throughout all denoising steps. This property appears attractive for offloading as it amortizes the selection overhead across the entire block, but it requires exact attention over the full KV cache, which is too expensive under offloading. We present HERALD, a KV offloading system for block dLLMs that resolves this through two opportunities that reduce the required selection compute by a factor of the block size and enable selection to be overlapped with denoising. Across three block dLLMs and five long context tasks, HERALD achieves near-lossless accuracy at 5-10% KV budget and up to 1.59x lower per block latency and 2.47x higher throughput over GPU-only inference, with speedups growing with context length.

---


### 113. [When Is an LLM Worth It for Hyperparameter Optimization? A Budget-Matched Study on Tabular Data Finds the Warm-Start Is a Default Configuration, Not the Model](https://arxiv.org/abs/2606.21641)

**<font color=#1a73e8>作者：</font>** Carson Rodrigues, Oysturn Vas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been proposed as hyperparameter-optimization (HPO) advisors that "warm-start" search from prior knowledge, proposing strong configurations in very few evaluations. We test that claim under a budget-matched, multi-seed protocol on eight PMLB tabular benchmarks, comparing an LLM advisor (LLM-OptFlow) against four classical baselines (random search, Optuna-TPE, Gaussian-process Bayesian optimization, and successive halving) over one shared search space, with paired tests and bootstrap 95% CIs across 8 x 5 = 40 (task, seed) units. The finding is cautionary. The advisor's strong first point is not an LLM output at all: like prior LLM-HPO systems the loop is seeded with a fixed default configuration, evaluated before any model call, which alone reaches 88.7% mean best-CV, identical to within 0.01 pp across all seven advisor models tested. The LLM's own proposals add only +0.40 pp of cross-validation accuracy over that seed and nothing on held-out test (LLM-Default = -0.01 pp, p = 0.92). When the same seed is granted to classical search, the apparent lead collapses: against seeded random search it leads by +0.20 pp at 2 evaluations, is tied by 5, and is behind by 12 (-0.37 pp). Without the seed, classical search ties the advisor by 12 evaluations and beats it by 40 (+0.6 to +0.8 pp, p <= 1e-4). Two LLM-specific behaviors survive: a single-task exploration failure (vehicle), and a rule-based confidence filter that removes ~33% of wasted compute without changing accuracy. The recommendation is deflationary: on tabular HPO, seed classical search with a sensible default; an LLM advisor adds no measurable generalization benefit and is overtaken within a handful of evaluations. We release the harness and a script that reproduces every statistic.

---


### 114. [Behavioral and Representational Evidence of Binomial Ordering Preferences in Large Language Models](https://arxiv.org/abs/2606.21645)

**<font color=#1a73e8>作者：</font>** Zhiqing Yang, Yilun Liu, Yunpu Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can readily reproduce conventional expressions, yet their ability to model gradient frequency distributions remains underexplored. We investigate this using linguistic binomials, such as men and women, where both word permutations are grammatically valid but exhibit distinct, cross-linguistic variations in conventionality. We formalize binomial ordering as a distributional alignment problem, and construct a multilingual dataset of 600 binomial pairs across 8 languages. With categorical and distributional metrics, we measure and compare the corpus-derived preferences with model-induced ordering probabilities of 6 open-weight LLMs. While models often behaviorally recover the dominant corpus-preferred order, particularly for strongly conventionalized pairs, they align less well with the exact corpus preference distributions. This suggests that apparent directional order overstates how faithfully LLMs capture the statistical nuances of language use. Sparse probing verifies that the concept of preference strength is partially encoded among middle-to-late layers, and steering along probe-derived directions alters model-induced ordering distributions, demonstrating that the statistical behavioral preference of LLMs can be mechanistically measured and manipulated via internal representations.

---


### 115. [EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory](https://arxiv.org/abs/2606.21649)

**<font color=#1a73e8>作者：</font>** Chang Nie, Chaoyou Fu, Junlan Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing embedding models are inherently static: they encode text segments in isolation, ignoring their surrounding context and temporal order. This paper introduces EvoEmbedding, a novel embedding model that generates evolvable representations for retrieval. It is tailored for long-context scenarios, where information is dynamic, sequential, and requires continuous state tracking. Our design is simple: EvoEmbedding maintains a continuously updated latent memory as it sequentially processes inputs, and uses it alongside the raw content to jointly generate evolvable embeddings. Consequently, for the same query, our model adapts its representation to retrieve distinct targets based on the evolving context, going beyond static semantic search. To equip the model with this capability, we construct EvoTrain-180K, a diverse dataset for the joint optimization of latent memory and retrieval. Furthermore, we introduce a memory queue to prevent representation collapse during recurrent encoding, alongside segment-batching techniques that tackle significant length variance and accelerate training by 3.8$\times$. Extensive experiments show that our model not only outperforms larger-scale specialists (e.g., Qwen3-Embedding-8B and KaLM-Embedding-Gemma3-12B) across a range of long-context retrieval benchmarks, but also generalizes well to downstream tasks (e.g., personalization) with contexts 10$\times$ longer than its training window. Notably, EvoEmbedding seamlessly integrates into agentic workflows to boost performance. For instance, a naive RAG pipeline equipped with our model surpasses dedicated agentic memory systems. Project Page: this https URL.

---


### 116. [Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.21666)

**<font color=#1a73e8>作者：</font>** Carson Rodrigues  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems routinely produce hallucinated outputs that cannot be explained by model deficiencies alone. A significant class of these failures arises not from model incapacity but from context drift: the divergence of internal knowledge states between concurrent agents. When agents enter a collaborative task with mismatched or stale representations of shared world state, their joint reasoning produces contradictions that manifest as hallucination. We define the Context Divergence Score (CDS), a lightweight scalar metric quantifying knowledge-state discrepancy between agent pairs across spatial, temporal, and task dimensions, and propose the Shared State Verification Protocol (SSVP), which lets agents periodically exchange compressed state summaries and flag high-divergence conditions before joint reasoning. We evaluate SSVP across two domains (multi-agent travel and software project planning) using Claude Haiku. In controlled experiments (n=30 per condition, travel; n=10, software) across 8 scenarios, naive full-broadcast synchronization increases hallucination rate by 34% above the no-sync baseline (HR: 0.658 vs. 0.492, p=0.0022, d=1.18), a contamination effect from propagating erroneous agent states. SSVP avoids this failure mode while showing modest, consistent reduction (HR: 0.463, d=0.30) and achieves significantly lower hallucination than full-broadcast (p=0.0005, d=1.47) using 58% fewer API calls. The contamination effect does not replicate in the software domain, where all conditions converge to low HR (<0.2), confirming it is specific to tasks where one erroneous shared belief cascades across evaluation dimensions. Our results reframe hallucination mitigation as a distributed systems problem and establish context synchronization as a first-class primitive in multi-agent LLM design.

---


### 117. [TACO: Task-Aware Column Description Generation Using LLMs](https://arxiv.org/abs/2606.21685)

**<font color=#1a73e8>作者：</font>** Ting Cai, Rakesh R. Menon, Yiru Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating accurate and informative column descriptions (e.g. "membership status of customers" for the column name "cust_mem") is essential for a wide range of downstream NLP tasks on tabular data, including NL2SQL, table question answering, and entity linking. This problem arises in enterprises, domain sciences, government data portals, and so on. Despite its importance, most real-world datasets suffer from missing or cryptic documentation, often due to abbreviated column names or domain-specific jargon. Existing approaches largely rely on single-prompt large language models (LLMs), which struggle with three key issues: (i) inconsistent or incorrect handling of abbreviations, (ii) hallucinated or incomplete descriptions, and (iii) redundancy or vagueness that hinders downstream performance. We present TACO, a task-aware framework for automatic column description generation using LLMs. TACO introduces a three-step pipeline: (1) abbreviation expansion, which standardizes column names; (2) description generation, which produces initial semantic descriptions enriched with synonyms and search-oriented keywords; and (3) description revision, which refines these outputs using simulated downstream tasks. In addition, we investigate human-in-the-loop extensions and release new evaluation datasets for entity linking and schema enrichment. Extensive experiments across public and proprietary datasets show that TACO consistently outperforms existing methods, improving downstream task performance by up to 32%.

---


### 118. [Clinical Term Extraction using Open-Source Small Language Models](https://arxiv.org/abs/2606.21689)

**<font color=#1a73e8>作者：</font>** Noah Marchal, William E. Janes, Mihail Popescu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical information for amyotrophic lateral sclerosis (ALS) care documented in unstructured clinical notes limits downstream analysis without extraction into structured formats. Open-source small language models with few-shot prompting for detecting the presence of ALS-relevant clinical terms in patient documentation were evaluated without task-specific training data. The detection task targeted 17 categories spanning functional scores, respiratory measures, medications, and related clinical and non-clinical attributes. Clinical note content was normalized from JSON-encoded discharge summaries and processed with a prompt template having structured JSON outputs. We compared 26 open-source models using aggregate, label-level, and manual-validation multilabel classification metrics. Manual validation showed that a regex rule baseline had higher overall micro-F1 and lower Hamming loss than any single SLM or TF-IDF baseline, while Qwen3-4B-Instruct-2507 was the highest-performing SLM by micro-F1. Model rankings varied by metric and label category, with the TF-IDF baseline showing high recall but low precision, some SLMs showing higher precision but lower recall, and Hammer2.1-7b showing strong performance for ALSFRS-R subscore detection. These findings support targeted hybrid extraction workflows rather than replacement of existing rule-based methods.

---


### 119. [PrivacyAlign: Contextual Privacy Alignment for LLM Agents](https://arxiv.org/abs/2606.21710)

**<font color=#1a73e8>作者：</font>** Manveer Singh Tamber, Abhay Puri, Marc-Etienne Brunet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents acting on behalf of users are constantly making decisions, and for users to trust their agents, those decisions must align with what they actually want. Privacy is an important alignment problem for agents: every message, post, or tool call an agent makes is a contextual judgment about what is appropriate to share, with whom, and under which conditions. Because such judgments depend on social expectations and norms, human judgment does not merely label privacy violations but also helps define them. While existing work relies on unreliable proxies for both training and evaluation, we place human judgment at the center of agentic privacy alignment. We introduce PrivacyAlign, a dataset of 1,350 samples with 3,516 detailed annotations from 599 unique annotators across diverse scenarios where current LLMs actually leak, and use it to ground both alignment training and automated evaluation in human privacy norms. Building on these annotations, we first show that conditioning LLM judges on human annotations and explanations for reference responses to the same prompt makes their judgments more reliable. We then introduce annotation-conditioned reward modeling, which uses these annotations to score new responses during RL, and show that small open-weight agents trained with this reward better align with human privacy norms, with strong gains on PrivacyAlign and existing privacy benchmarks for agents.

---


### 120. [Leveraging LaBSE with Progressive Curriculum Learning for Multicultural Polarization](https://arxiv.org/abs/2606.21718)

**<font color=#1a73e8>作者：</font>** Sachin Sundar, Sandeep Kumar, Mothish M  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting online polarization remains a critical challenge, particularly in multilingual and multicultural contexts where intergroup hostility is prevalent. The problem is particularly challenging due to the data scarcity for these tasks in the low-resource languages. Identifying such phenomena has become an active area of research and is addressed in SemEval-2026 Task 9: Multilingual, Multicultural Online Polarization Detection. To address this problem we propose an architecture that leverages LaBSE embeddings - an unconventional choice typically reserved for retrieval tasks, to obtain strong cross-lingual learning which enhances scores in low-resource language by a score up to 0.2 macro F1. Furthermore, we provide a comprehensive ablation study evaluating the performance of diverse encoder models in the Qwen model family within a retrieval-based prompting framework. Our code will be soon available at this https URL.

---


### 121. [Denoising Iterative Self-Correction: Structured Verification Loops for Reliable LLM Reasoning](https://arxiv.org/abs/2606.21724)

**<font color=#1a73e8>作者：</font>** Shen Yin, David Ken, Joel Stremmel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models produce fluent but often incorrect multi-step reasoning, and naive correction methods risk degrading already-correct answers. We introduce Denoising Iterative Self-Correction (DISC), a test-time procedure that treats verification question outputs as noisy measurements of where a solution may be corrupted. Using these signals, DISC progressively reduces errors across multiple verify-judge-correct passes, analogous to traditional iterative denoising. A binary judgment gate controls correction precision by blocking rewrites that would damage already-correct answers while the verifier and corrector together repair errors. We evaluate this trade-off using two paired diagnostics: an improvement-to-degradation ratio (precision) and a repair rate (recall). Across three benchmarks (BIG-Bench Mistake, HotpotQA, GPQA Diamond) and four models, DISC dominates Chain-of-Verification and Self-Refine on the precision-recall trade-off, reaching 81.6% accuracy with 13x more improvements per degradation than Chain-of-Verification and 5x more than Self-Refine on BIG-Bench Mistake (Sonnet~4.5). On GPQA Diamond, we identify a capability floor below which judges acknowledge contradictions in evidence but cannot translate that recognition into a correction. We further show that cross-model role allocation -- assigning verification and judgment to a model different from the generator -- mitigates self-confirmation bias.

---


### 122. [Training the Orchestrator: A Supervised Approach to End-to-End PDDL Planning with LLM Agents](https://arxiv.org/abs/2606.21740)

**<font color=#1a73e8>作者：</font>** Rajesh Mangannavar, Zachary Coalson, Pranay Dugar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Translating natural-language planning intent into verified plans is a longstanding challenge: people communicate goals in language, while classical planners require formal PDDL specifications. Recent agentic frameworks bridge this gap by orchestrating a pool of specialized repair agents inside a verifier-checked refinement loop, but the orchestrator at the centre is itself a prompted frontier LLM, paying a frontier-LLM API call at every refinement step. We present HALO (Hybrid Agent-Learned Orchestrator), which trains the orchestrator from refinement trajectories that an external verifier has certified as ending in valid plans, across 11 PDDL domains. HALO pairs a small QLoRA-tuned policy with three hardcoded rules for trivially decidable selections, and operates over an expanded 21-agent action space. Unlike approaches that prompt a frontier LLM at every step or learn an orchestrator from sparse end-of-episode rewards, our key observation is that the verifier already provides strong guidance: every accepted trajectory is a sequence of demonstrably correct (state, agent) decisions, directly usable as supervision. Across PlanBench, Natural Plan, and classical planning benchmarks, HALO matches or exceeds the GPT-5-mini prompted baseline on success rate, sits within three percentage points of the stronger Gemini-3-Flash prompted baseline, reduces orchestration cost by more than an order of magnitude (\$0.18 to \$0.004 per task against GPT-5-mini, roughly 45$\times$ cheaper; roughly 15$\times$ cheaper than Gemini-3-Flash), and cuts total LLM calls per episode by 40 to 50 percent.

---


### 123. [Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning](https://arxiv.org/abs/2606.21775)

**<font color=#1a73e8>作者：</font>** Tianqi Du, Qi Zhang, Yifei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, world models have emerged as a promising paradigm for building intelligent agents by learning predictive models that estimate future environment states conditioned on observations and actions. In particular, JEPA-style latent world models provide an efficient alternative to pixel space prediction by learning action-conditioned dynamics in compact representation spaces. However, existing latent world models typically rely on one-step prediction and must be recursively rolled out for long-horizon planning, which leads to compounding errors and a mismatch between training objectives and downstream planning tasks. To address this limitation, we propose Variable-length Latent World Models (VLWMs), a framework that learns to predict future latent states conditioned on action sequences of variable lengths. Instead of training only on one-step transitions, VLWMs directly model temporally extended dynamics, allowing the same predictor to evaluate action plans over different horizons. We further introduce a curriculum training strategy that progressively expands the action horizon, stabilizing optimization from short-range dynamics to long-range prediction. At test time, we design planning methods tailored to VLWMs to better exploit their variable-length predictive capabilities. Experiments on long-horizon control tasks show that VLWMs significantly improve latent space world models, achieving 13\% average improvement over the state-of-the-art LeWM across different datasets, with especially large gains on tasks requiring extended planning. These results suggest that VLWM provides a simple yet effective paradigm for improving long-horizon prediction and planning in latent world models.

---


### 124. [RocketPFN: Accurate Time Series Classification via In-Context Learning](https://arxiv.org/abs/2606.21786)

**<font color=#1a73e8>作者：</font>** Franco Martino O'Rourke, Ana Trisovic, Dimitris Bertsimas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce RocketPFN, a training-free pipeline for time series classification that combines random convolutional feature extraction (Rocket) with in-context classification via a pretrained tabular foundation model (TabPFN v2.5). On 92 UCR datasets (30-resample protocol), RocketPFN matches HC2, the strongest published method on the archive, in mean accuracy (both 0.900, Wilcoxon p=0.50), with no training on the target data and a median inference time of 30 seconds per fold. It also significantly outperforms every individual classifier in the HC2 ensemble. On UEA (20 datasets) the difference is likewise not statistically significant. A separate comparison concerns TSC foundation models: when paired with the same downstream classifier, MOMENT, Mantis, and MantisV2 are all significantly outperformed by RocketPFN using fewer extracted features and no learned parameters (p<0.001 in each case). This holds even when the encoders were pretrained on corpora that include the UCR training samples. We propose this two-stage pipeline as a reference point for evaluating zero-shot TSC foundation models.

---


### 125. [When to Plan, When to Polish: Noise Level as a Granularity Axis for Diffusion Language Models](https://arxiv.org/abs/2606.21802)

**<font color=#1a73e8>作者：</font>** Peihong Li, Yuanjie Shi, Yan Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard tokenwise diffusion LMs keep training corruption and inference commitment at token granularity throughout denoising. At high noise, this leaves scattered local fragments rather than coherent evidence, making it hard to form early coarse structure, exactly what planning-sensitive generation requires. Hierarchical planning methods add coarse stages to separate planning from wording, but they need extra planners, block latents, or two stage designs. We propose Noise Dependent Granularity Control (NDGC), a single-level diffusion method that uses the noise level as a granularity cue. NDGC aligns training exposure and inference commitment with denoising progress. High noise steps use coherent token groups to support early meaning commitment, while low noise steps return to token level refinement. This creates planning like coarse to fine denoising without an explicit planner or hierarchical architecture. Across controlled tests, ablations, and WritingPrompts, NDGC shows earlier skeleton formation, better ordered recovery, and healthier outputs.

---


### 126. [Test-Time Training with Next-Token Prediction](https://arxiv.org/abs/2606.21803)

**<font color=#1a73e8>作者：</font>** Xuan Ouyang, Zefan Cai, Junjie Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Next-token prediction is the self-supervised signal that trains language models, and every observed prompt token provides the same signal at test time. We study whether this signal can define the inner-loop objective for test-time training (TTT) in pretrained long-context language models. Many TTT architectures require models to be trained with test-time adaptation in mind, limiting their direct applicability to released LLM checkpoints. While recent in-place TTT methods make fast-weight adaptation possible for pretrained LLMs without redesigning the backbone, they leave a central question unresolved: what should each test-time write store? Existing recipes train the fast weight to match a learned local value proxy but they are not directly tied to the self-supervised next-token prediction signal. We introduce Test-Time Training with Next-Token Prediction (TTT-NTP), a drop-in fast-weight adaptation method for pretrained LLMs that instead supervises updates using the model's own next contextual hidden state. This makes each local write follow the same causal computation that supports next-token prediction: the value target is a pointwise linear projection of a single next-position contextual state. On RULER Full-13 (averaged over 4k, 8k, 16k, and 32k context lengths), TTT-NTP is the only method that consistently improves the released backbone across four models spanning three families and a 0.6--8B size range: Llama-3.1-8B (+3.9), Mistral-7B-v0.3 (+3.0), and the Qwen3 series (Qwen3-4B +4.1, Qwen3-0.6B +2.9). On the real-world LongBench-v2 long-document QA benchmark, TTT-NTP improves over the base model on both Llama-3.1-8B (+5.6) and Mistral-7B-v0.3 (+3.7), while preserving commonsense and knowledge performance.

---


### 127. [Fixed RAG Compression Collapses Measured Reader Scaling](https://arxiv.org/abs/2606.21807)

**<font color=#1a73e8>作者：</font>** Sugam Panthi, Rabab Abdelfattah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) compression papers often evaluate a compressor on one to three readers and treat the compressed evidence layer as evaluation-neutral. We show this assumption is false: fixed compression can raise average accuracy while hiding reader upgrades and reversing model rankings. Across 20 readers and ten domain-method settings over four QA benchmarks and one summarization benchmark, compression gain decreases with reader baseline (nine of ten settings significant, p < 0.05). Generic summarization flips 31% of pairwise model rankings on LongMemEval-S, and a fixed HotpotQA compressor hides 80% of the raw upgrade from Qwen 7B to GPT-4.1-mini. Two opposing forces explain this paradox: compression rescues weak readers by removing noise they cannot filter, and harms strong readers by dropping details they would have used. The pattern appears across structured compilation, generic summarization, three trained compressor families, query-focused summarization, and an external audit of nine published compression papers. We release ragscale, a toolkit built on 177,000 row-level compression transitions, so any compression paper can audit reader scaling with three readers in one day.

---


### 128. [AgentCAT: Simulating Computerized Adaptive Testing via Multi-Agent Large Language Models](https://arxiv.org/abs/2606.21832)

**<font color=#1a73e8>作者：</font>** Weiyuan Zhou, Haiping Ma, Xiaoshan Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computerized Adaptive Testing (CAT), as a key technology for personalized education, aims to accurately assess examinee proficiency by retrieving exercises dynamically matching current ability estimates. However, existing CAT research is constrained by limitations of static offline data and isolated component optimization. Restricted by partial labels in offline logs, researchers degrade the dynamic assessment process into static sequence prediction. Current research focuses on isolated perspectives, e.g., selection or diagnosis, neglecting the overall CAT interaction process. To address this, we propose AgentCAT, a Large Language Model-based multi-agent simulation system, to construct a high-fidelity benchmarking environment for dynamic testing. This framework comprises three modules: (1) The examinee agent with memory retrieval and Chain-of-Thought reasoning simulates responses based on cognitive profiles; (2) The selection agent uses coarse-to-fine bucketing and knowledge graph exploration to balance local difficulty and global coverage; (3) The supervisor uses dual-auditing and robust update to ensure convergence and validity. To validate the framework, we evaluated on two real-world datasets across three dimensions: macro-level ability convergence, micro-level interaction logic, and data sparsity resilience. Results show AgentCAT achieves effective ability estimation, and its selection strategy balances difficulty adaptation and instructional coherence, aligning with human pedagogical intuition.

---


### 129. [Inverse Turing Bench: Evaluating Language Models as Judges of Human vs. AI Dialogue](https://arxiv.org/abs/2606.21844)

**<font color=#1a73e8>作者：</font>** William Hager, Ishika Rathi, Masum Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI systems integrate into online spaces, differentiating them from humans in conversations is increasingly important. We present Inverse Turing Bench, a benchmark that evaluates LLMs and other models on their ability to differentiate humans and AI in multi-turn text. The benchmark provides a collection of paired dialogue transcripts, wherein one dialogue is between two humans and the other is between a human and an AI. The task is to correctly identify which dialogue is human-only vs. human-AI. We evaluated a preliminary set of models against this benchmark, and found that GPTZero, Claude Opus-4.6, and GPT-5.5 achieve the highest accuracy: 89.41%, 77.92%, and 75.94% respectively. Our results suggest that statistical approaches to detection have semantic blind spots, but semantic approaches are susceptible to persona-prompting. Our work speaks to the Inverse Turing Test as a probe of LLM theory of mind, and motivates human-AI differentiation as a critical capability for AI systems. Our live benchmark can be found at this https URL (anonymity preserved).

---


### 130. [UniRank: Unified Rank Allocation for Low-Rank LLM Compression](https://arxiv.org/abs/2606.21847)

**<font color=#1a73e8>作者：</font>** Chao Han, Haozhe Hu, Fei Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank decomposition serves as a promising compression paradigm for large language models, however, rank allocation remains challenging: manual rules lack generalizability, and learning-based approaches incur heavy computational overhead. To address these issues, we formulate global low-rank allocation as a sorting-and-truncation pipeline, and score each singular component via dual criteria: \textbf{Local} singular energy ratio that quantifies the intrinsic importance within the decomposed parameter matrix and \textbf{Global} functional importance (measured by input-output cosine similarity) that evaluates the functional significance of decomposed modules. We verify the strong correlation between high input-output cosine similarity and low effective rank through geometric interpretation and experimental validation. Furthermore, we propose rank-preserving fine-tuning, which performs direct LoRA tuning on decomposed weights and avoids extra information loss caused by re-truncation in conventional merging pipelines. Empirical results confirm that our method delivers sustained performance enhancements when combined with models featuring distinct decomposition schemes, model sizes and architectural designs, e.g. in one-shot compression without further fine-tuning, our method reduces perplexity by up to 50\% compared with uniform and heuristic allocation baselines. Code will be available at this https URL.

---


### 131. [Zero-Shot Vision-Language Models for Classroom Engagement Recognition: A Benchmark Study of Prompt Sensitivity and Cross-Dataset Generalization](https://arxiv.org/abs/2606.21861)

**<font color=#1a73e8>作者：</font>** Aman Goyal, Kshama Nitin Shah, Kemmannu Vineet Venkatesh Rao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classroom engagement recognition holds substantial promise for scalable learning analytics, yet the suitability of modern Vision-Language Models (VLMs) for this task under zero-shot conditions remains largely unexplored. We present a systematic benchmark that evaluates five widely-used VLMs: CLIP, BLIP-VQA, GPT-4o, LLaVA-1.5-7B, and Qwen2.5VL-7B-Instruct across two complementary educational datasets: DAiSEE, an individual-student video dataset (300 sampled test clips), and the Student Classroom Behaviour dataset (SCB, 1,168 scene-level images). Each model is probed with three prompt variants spanning minimal, rubric-anchored, and chain-of-thought designs. Our experiments reveal three primary failure modes of zero-shot VLMs for engagement recognition: (1) near-random performance on individual students, with Cohen's kappa never exceeding 0.10 on DAiSEE; (2) severe class collapse, where models assign 85-100% of predictions to a single engagement level regardless of visual content; and (3) extreme prompt sensitivity, with accuracy swings of up to 32 percentage points on identical images depending solely on prompt phrasing. Remarkably, scene-level classification on SCB is substantially more tractable: CLIP and GPT-4o achieve kappa approximately 0.60 when prompted with behaviorally-grounded rubrics. We also document a practical barrier for deployment: GPT-4o's safety filters reject 98% of chain-of-thought requests involving individual student faces. Our findings provide a calibrated baseline and surface critical design considerations for the use of VLMs in educational observation systems.

---


### 132. [The Language-Energy Divide: Measuring Energy Costs of Multilingual LLM Inference](https://arxiv.org/abs/2606.21869)

**<font color=#1a73e8>作者：</font>** Naihao Deng, Alissa Shen, Yiming Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in multilingual settings, yet the energy costs of serving these models across different languages remain poorly understood. We present a systematic study of inference energy consumption across languages with this http URL framework (Chung et al., 2026). We find striking disparities: energy consumption per output token varies by up to 8.3 times across languages, while total energy for a fixed set of requests varies by up to 179 times between the cheapest (English, 17.6 kJ) and the most expensive (Pashto, 3,147 kJ) languages. Our analysis shows that this disparity is driven by two compounding factors: (1) higher per-token energy costs for languages using complex or rare scripts, and (2) more tokens generated for low-resource languages. Moreover, we find a double cost + performance penalty: languages with the highest energy footprints also tend to achieve the lowest task accuracy. We reveal that the energy divide persists across models, hardware, and tasks, suggesting a systemic energy inequity in multilingual LLM deployment. Finally, we recommend that the community treat energy as a first-class evaluation axis, extend reporting checklists and model cards to include it, and adopt deployment-side mitigations for better energy efficiency.

---


### 133. [AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems](https://arxiv.org/abs/2606.21877)

**<font color=#1a73e8>作者：</font>** Srimonti Dutta, Akshata Kishore Moharir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems retrieve private context, invoke tools, write files, call external services, coordinate with other agents, and may act without human approval. Existing bill of materials artifacts improve transparency for dependencies, model metadata, and training provenance, but leave an agentic transparency gap: capability opacity, the absence of a structured account of what a deployed agent can access, remember, change, delegate, and prove afterward. This paper introduces AgentRiskBOM, a security BOM for risk-scoping tool-using AI agents. It is an additive layer over SBOM, AIBOM, and MLBOM artifacts, referencing them where authoritative while adding fields for runtime authority: autonomy, tool permissions, memory, credential scope, approval gates, audit signals, inter-agent communication, and external action capability. We implement AgentRiskBOM as a JSON-schema artifact with a reproducible corpus, risk scenarios, scorer, diff detector, control mapper, and reports. We evaluate AgentRiskBOM on 13 open-source agents spanning coding, RAG, and multi-agent archetypes, plus 52 risk scenarios across 14 categories. The schema validates all 13 corpus artifacts. Coverage analysis gives AgentRiskBOM a native-equivalent score of 14 across 16 capability dimensions, vs. 1 for SBOM, 1.5 for AIBOM and 2 for MLBOM. Across modeled risk categories, AgentRiskBOM exposes 100% risk-category visibility vs. 10.5% for SBOM-like and 20.9% for AIBOM-like views. To test agentic authority drift, we inject 33 structured deployment mutations; the diff detector identifies the correct change type for all mutations. A secondary penalty-based scorer yields a Spearman correlation of 0.73 with the primary scorer, supporting rank-level consistency while showing that thresholds require human calibration. The results show that agentic AI security needs a machine-readable authority-and-risk artifact before incidents occur.

---


### 134. [Cohort-Anchored Foundation Models for Electronic Health Records: From Risk Scores to Auditable Peer Cohorts](https://arxiv.org/abs/2606.21885)

**<font color=#1a73e8>作者：</font>** Kaiping Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models have achieved remarkable performance across medical question answering, imaging, and electronic health record (EHR) tasks, yet reliable clinical deployment remains challenging due to limited interpretability, vulnerability to distribution shift, and weak alignment with clinician reasoning. We argue that these limitations arise because existing approaches prioritize representation learning while treating patient comparison as an emergent property rather than a primary source of clinical evidence. To address this gap, we propose CAFM, a Cohort-Anchored Foundation Model framework that elevates patient cohorts to a first-class object throughout the learning pipeline. The framework consists of four stages: deviation-aware data curation, cohort-conditioned pretraining, multimodal cohort alignment, and clinician-in-the-loop refinement. Together, these stages improve data quality, organize representations around clinically meaningful cohort structure, preserve modality-specific relationships, and support auditable clinical decision-making. The framework is compositional and can augment existing EHR foundation models without modifying their underlying encoders. We illustrate CAFM through four clinical case studies spanning acute kidney injury prediction, cardiovascular risk stratification from electrocardiograms, optic neuropathy triage from orbital imaging, and electroretinogram-grounded report generation. We further present five empirically testable hypotheses and identify open challenges in data quality, irregular temporality, multimodal learning, distribution shift, and evaluation beyond predictive accuracy. We argue that explicitly anchoring foundation models to patient cohorts provides a principled path toward trustworthy clinical AI.

---


### 135. [Scaling Performance and Low-Resource Annotation with Many-Shot In-Context Learning for Named Entity Recognition](https://arxiv.org/abs/2606.21890)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Fangping Lan, Cornelia Caragea 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) with large language models (LLMs) has emerged as a powerful alternative to fine-tuning for Named Entity Recognition (NER), achieving strong performance with minimal annotation and no additional training. However, prior work has shown that despite their adaptability, LLMs still lag behind fully supervised models such as fine-tuned BERT in structured tasks like NER. While existing studies on ICL for NER have mainly explored few-shot settings, the potential of scaling to hundreds of demonstrations has not been thoroughly investigated. To address this gap, we conduct a comprehensive investigation of many-shot ICL for NER and further explore its effectiveness in annotating and refining data for low-resource NER tasks. Specifically, we evaluate various LLMs across multiple domains using hundreds of ICL examples and then assess the feasibility of using many-shot ICL as a data annotation framework. Our experiments demonstrate that: (1) scaling to hundreds of in-context examples enables LLMs to match or even surpass the performance of fully supervised BERT models; and (2) using about one hundred human-labeled examples as demonstrations, many-shot in-context annotation can generate high-quality labeled data, leading to approximately 10% absolute F1 improvement over existing state-of-the-art approaches when used to fine-tune BERT on low-resource NER.

---


### 136. [Learning the ARTS of Search for Automated Discovery](https://arxiv.org/abs/2606.21891)

**<font color=#1a73e8>作者：</font>** Gurusha Juneja, Arnav Kumar Jain, Deepak Nathani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery can be formulated as an iterative search process over the space of hypotheses and experiments. Contemporary methods navigate this space using heuristics such as MCTS. These algorithms conflate the merit of a hypothesis with the quality of its experimental execution. A promising hypothesis with preliminary execution is therefore ranked below a modest hypothesis whose execution is refined. Moreover, prior methods prune the search logs as the search progresses because the accumulated history outgrows the context window. We propose Agentic Reasoning for Tree Search (ARTS), where we deploy a reasoning language model to navigate this space. The model inspects prior execution logs, diagnoses whether earlier failures arose from faulty implementations or bad hypotheses, and selects the hypothesis to build on next. To mitigate challenges with context length, ARTS uses test-time training to instill the knowledge of search tree in the model weights. Across 22 tasks from MLGym and MLEBench, we show that ARTS outperforms leading algorithms, with over 15.3% relative improvement in the normalized score. With test-time training we show that a Qwen3-4B agent can match performance with closed-source frontier models like Gemini-3 Pro and GPT o3-reasoning with upto 5x lower inference cost. We further observe that on partially observable RL tasks, the test-time trained Qwen3-4B scientist surpasses ARTS with the o3 scientist by rediscovering the human-best recurrent-memory solution that heuristic methods prune away.

---


### 137. [Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding](https://arxiv.org/abs/2606.21906)

**<font color=#1a73e8>作者：</font>** Xuanming Zhang, Sining Zhoubian, Yuxuan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive generation in large language models (LLMs) conventionally decodes from the final layer, assuming that deeper representations yield more reliable next-token predictions. We revisit this assumption by revealing a recurring Guess-Refine-Perturb dynamic: early layers form coarse guesses, intermediate layers refine reasoning-relevant semantics, and final layers can perturb these refined predictions toward generic or alignment-preferred tokens. We introduce Confident Decoding, a training-free decoding strategy that dynamically selects the most reliable near-final layer through entropy-guided conservative backward search. We further provide a theoretical formulation of layer selection as an optimal stopping problem, showing that under bounded projection noise and dominant late-stage alignment perturbation, our search rule filters perturbation while bounding the loss relative to the oracle refinement layer. Experiments across dense and Mixture-of-Experts LLMs demonstrate consistent gains on challenging reasoning benchmarks, including GPQA-Diamond, Omni-MATH, and HLE, with zero memory overhead and less than 2% latency increase. These results suggest dynamically bypassing final-layer perturbations can unlock stronger reasoning behavior from aligned LLMs.

---


### 138. [Rethinking the Adaptation of Vision Foundation Models for Efficient Cell Segmentation](https://arxiv.org/abs/2606.21913)

**<font color=#1a73e8>作者：</font>** Qing Xu, Xiangjian He, Wenting Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cell segmentation is critical for computational pathology and biomedical discovery. While recent Vision Foundation Models (VFMs) have demonstrated remarkable universal feature representations, unlocking their full potential for cellular imaging is currently bottlenecked by resource-intensive adaptation paradigms. Existing methods typically rely on fine-tuning heavy visual encoders, leading to extensive computational overhead and a dependency on large-scale annotations. To address this, we propose the EffiCell-Seg framework for highly efficient cell segmentation without re-training the visual encoder. Our core insight is that pretrained VFMs intrinsically encode complementary structural priors: global saliency for localizing potential cells, and local morphological patterns for delineating cellular structures. To harness these priors, we devise a Cell Structure Prompt Encoder (CSP-Encoder) that synthesizes semantic-aware saliency and principal morphological features from frozen VFM representations into explicit structural prior maps. Moreover, we propose a Synergistic Mask Decoder (SM-Decoder) that enforces contextual consistency by jointly predicting geometric distance fields and semantic maps via mutual cross-guidance. Extensive experiments demonstrate that EffiCell-Seg outperforms state-of-the-art methods across diverse cell imaging modalities while requiring only ~5M trainable parameters, over 130x fewer than fully fine-tuned VFM counterparts. The code is available at this https URL.

---


### 139. [GTA-Net: Cooperative Game Theory for Vision-Language Alignment in Chest X-Ray Report Generation](https://arxiv.org/abs/2606.21915)

**<font color=#1a73e8>作者：</font>** Saif ur Rehman Khan, Imad Ahmed Waqar, Sebastian Vollmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated chest X-ray report generation requires precise cross-modal grounding to ensure clinically reliable descriptions. However, existing vision-language models rely on implicit attention mechanisms that fail to enforce explicit region-word correspondence and disease-level consistency. We propose Game-Theoretic Alignment Network (GTA-Net), a vision-language framework that formulates report generation as a cooperative game-theoretic alignment problem. The model introduces a BinaryGameAligner that models interactions between image regions and text tokens using similarity-based payoff matrices with Shapley-inspired importance weighting. To enforce clinical semantics, we further develop a Disease-Aware Ternary Aligner, which captures joint interactions among images, reports, and structured disease concepts. GTA-Net combines a Swin-based visual encoder with a LoRA-adapted large language model and is trained with a unified objective for generation and alignment. Experiments on CheXpertPlus and IU-XRay demonstrate state-of-the-art performance across standard generation metrics and improved clinical consistency, highlighting the effectiveness of explicit game-theoretic alignment for medical vision-language generation.

---


### 140. [Pre-Generation Hallucination Detection in Large Language Models via Soft-Target Attention Probing](https://arxiv.org/abs/2606.21917)

**<font color=#1a73e8>作者：</font>** Amina Miftakhova, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting hallucination risk before generation enables abstention, retrieval augmentation, and routing decisions without incurring the cost of decoding.
While prior work has shown that such risk can be estimated from a model's internal representations, existing approaches treat this as binary classification over a single decoded output. We instead formulate it as a risk-estimation problem. Under this formulation, we introduce soft-target supervision based on the empirical answer error rate over stochastically sampled outputs - an estimator we prove to be the unique unbiased minimum-variance estimator of the model's per-prompt error probability under its sampling distribution.
We further adapt attention probing to the pre-generation setting, enabling the detector to selectively aggregate hallucination-relevant prompt representations. Across three question-answering benchmarks and five models, attention probing outperforms linear probing on short-answer tasks. Replacing binary labels with soft-target supervision further and consistently improves detection quality.

---


### 141. [Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts](https://arxiv.org/abs/2606.21939)

**<font color=#1a73e8>作者：</font>** Jingting Zheng, Yuqi Ren, Linhao Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in contexts requiring complex moral reasoning and value trade-offs. However, existing evaluations typically rely on item-level behavioral metrics, which fail to capture how models structurally prioritize competing values as a cohesive system. To address this, we propose a symmetric human-LLM evaluation framework, grounded in Q methodology, to measure value-structure alignment. Under our protocol, humans and models sort an identical 140-item moral statement set into a shared nine-column forced distribution; for LLMs, we elicit strict rankings and deterministically map them to Q-sort buckets. Using a human reference sample ($N=35$), we establish a stable three-factor reference geometry specific to this instrument and sample. We evaluate 12 LLMs across four model families via 240 replicated Q-sorts at two temperature settings, quantifying structural alignment via Procrustes similarity ($\phi$) and RSA-based Spearman correlation ($\rho$). Our results reveal significant cross-family heterogeneity, model-specific sensitivity to generation stochasticity and localized misalignment, which demonstrate that favorable global scores can obscure underlying regional distortions. While rank- and bucket-based analyses remain highly consistent, prompt phrasing introduces notable variance. Ultimately, assessing value-structure alignment provides a crucial structural complement to traditional itemwise moral benchmarks.

---


### 142. [Modularized Reinforcement Learning on LLMs: From MDP Creation to Exploration and Learning](https://arxiv.org/abs/2606.21943)

**<font color=#1a73e8>作者：</font>** Zhao Yang, Yuxuan Jiang, Ting-Chih Chen 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become central to LLM post-training, yet the methods that dominate current pipelines, PPO and GRPO, represent only a narrow slice of what RL offers. Understanding why these methods prevail, and what alternatives exist, requires a principled examination of the design decisions that underlie any RL algorithm.
This survey organizes that examination around three stages of algorithm construction. We begin with MDP creation: how the reward function, state space, action space, termination condition, and discount factor are, or could be, defined for LLM training. We then turn to exploration, covering temperature sampling, entropy regularization, intrinsic motivation, tree search, and curriculum learning. Finally, we address learning along four classical RL dimensions: model-free versus model-based, value-based versus policy-based versus actor-critic, on-policy versus off-policy, and credit assignment, including both Monte Carlo methods, which rely on full return estimates, and bootstrapping methods, which update estimates using other learned predictions.
Mapping the LLM literature onto this taxonomy reveals a strikingly non-uniform distribution of research effort. Critic-free policy gradients and Monte Carlo credit assignment are densely populated, while value-based methods, off-policy actor-critic training, and bootstrapping-based credit assignment remain largely unexplored despite well-established counterparts in classical RL. These gaps represent concrete opportunities for transferring proven RL techniques to LLM training.
By making these gaps explicit alongside the methods that have proven effective, this survey offers researchers in both RL and LLMs a shared framework for understanding current practice and identifying promising directions for future work.

---


### 143. [VegSim: A Geospatial World Model for Scenario-Conditioned Vegetation Simulation](https://arxiv.org/abs/2606.21961)

**<font color=#1a73e8>作者：</font>** Irene Iele, Elena Mulero Ayllón, Paolo Soda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vegetation monitoring under climate stress requires answering not only how it will evolve given the expected weather, but how it would respond to alternative meteorological conditions. Forecasting models return the expected vegetation state for the observed weather and cannot answer these scenario-conditioned questions, because future weather is fixed to the recorded trajectory. We present VegSim, a geospatial world model for scenario-conditioned vegetation simulation. VegSim infers a latent vegetation state from sparse satellite-derived NDVI histories, past meteorological covariates, and static spatial context, propagates it forward under future weather forcing through recurrent latent dynamics, and decodes predictive NDVI quantiles at each lead time. Because future forcing enters as a controllable input, the same trained model supports probabilistic forecasting under observed weather and conditional simulation under user-defined meteorological forcing, without supervision on scenario responses. We evaluate VegSim on GreenEarthNet across in-distribution data and spatial, temporal, and joint spatial-temporal shift, where it achieves strong point and probabilistic accuracy against time series and Earth observation forecasting baselines while using a compact architecture. We then simulate vegetation responses across Europe under four meteorological scenarios, and in a France summer 2022 case study, obtaining spatially coherent patterns consistent with known sensitivity to temperature and precipitation. The code is available at this https URL.

---


### 144. [Holmes: Multimodal Agentic Diagnosis for Mixed-Language Mobile Crashes at Industrial Scale](https://arxiv.org/abs/2606.21963)

**<font color=#1a73e8>作者：</font>** Jia Li, Wenyuan Ma, Ting Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnosing mobile crashes in ultra-large-scale industrial applications is a formidable challenge due to the sheer volume of code, the complexity of mixed-language environments, and the inability to reproduce failures locally. Traditional static analysis struggles with scalability, while existing LLM-based agents often rely on reproducible environments unavailable in post-mortem scenarios. We present Holmes, a multi-agent system that automates root cause analysis by synthesizing multimodal runtime signals--stack traces, logs, and thread states--to reconstruct failure contexts without reproduction. Holmes introduces a hierarchical Retrieve-Explore-Reason architecture that leverages low-level artifacts (e.g., registers, assembly) to bridge the semantic gap between open-source business logic and closed-source system frameworks. By dynamically compressing the search space using runtime clues, Holmes precisely navigates 70-million-line codebases to identify non-local defects. Evaluated on real-world crashes from WeChat, Holmes achieves 87.6% accuracy in function-level fault localization and reduces average investigation time by over 98% (to ~77 seconds), demonstrating its effectiveness in transforming labor-intensive debugging into an efficient verification workflow.

---


### 145. [Look Before You Zoom: Adaptive Routing for the Resolution-Context Trade-off in Visual RAG](https://arxiv.org/abs/2606.21968)

**<font color=#1a73e8>作者：</font>** Oanh N. Tran, Thanh Quoc Hung Le, Oscar Chew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) struggle as query-relevant objects become smaller. To address this, recent training-free approaches dynamically retrieve and zoom into local image regions. However, we show that indiscriminately applying retrieval ignores a critical vulnerability: the resolution-context trade-off. Patch-based zooming recovers details for small targets, but can split large objects and destroy global spatial context; attention-based retrieval better preserves large objects, but remains less reliable on tiny details; and global perception is often fastest when retrieval is unnecessary. Motivated by these failure modes, we introduce ViRGo (Visual Retrieval or Global Perception), a lightweight framework that formulates visual retrieval as an adaptive routing problem. ViRGo estimates object scale from the VLM's intrinsic localization heads during the initial forward pass and combines it with semantic token confidence to select between global perception, patch-based retrieval, and attention-based retrieval with minimal additional computation. Experiments across multiple VQA benchmarks and object-size groups show that ViRGo improves the accuracy-efficiency trade-off: it matches patch retrieval on small details, leverages attention-based retrieval for larger objects, and reduces inference time by routing to the global baseline when zooming is unnecessary.

---


### 146. [Can LLMs Control Readability? A Multi-Dimensional Evaluation Framework for CEFR-Controlled Arabic Generation](https://arxiv.org/abs/2606.21981)

**<font color=#1a73e8>作者：</font>** Nour Rabih, Chatrine Qwaider, Ted Briscoe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) can generate fluent Arabic text, their ability to reliably control readability levels remains unclear. We propose a multi-dimensional evaluation framework for Common European Framework of Reference for Language (CEFR)-controlled Arabic text generation, assessing whether instruction-following LLMs can serve as reliable generators for adaptive language learning. Our framework integrates controlled prompting, automatic readability prediction using a validated Taha-19 model, lexical constraint validation, and syntactic complexity profiling. Results show that structured prompting substantially improves CEFR alignment. In particular, CEFR-guided prompting with lexical constraints achieves the highest conformity to reference linguistic profiles (0.91 cosine similarity) and near-perfect agreement with predicted readability levels (0.99), while unconstrained prompting exhibits weak control. These findings establish an empirical foundation for integrating readability-aware Arabic text generation into adaptive educational systems.

---


### 147. [One-Shot Data Selection for Medical Image Classification via Graph Coverage](https://arxiv.org/abs/2606.22002)

**<font color=#1a73e8>作者：</font>** Zahiriddin Rustamov, Nadia Badawi, Rafat Damseh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training medical image classifiers on entire datasets is wasteful when annotation budgets are limited: not all samples contribute equally, yet acquiring expert labels is expensive. Active learning reduces annotation cost through iterative querying, but assumes repeated access to an oracle and requires multiple rounds of model training. One-shot geometry-based methods such as facility location avoid retraining but operate on pairwise distances that ignore the local structure of the data manifold. We propose a graph-based one-shot selection method that operates entirely on frozen foundation model embeddings. Given embeddings from a pretrained encoder, we construct a k-nearest neighbor graph over all training samples and derive a two-term coverage kernel from the heat diffusion kernel, capturing both direct and two-hop neighborhood relationships. Greedy facility location on this kernel selects class-balanced subsets that maximize coverage of the data manifold. The two-term kernel matches the full spectral heat kernel in selection behavior while reducing computation to sparse matrix operations with a single hyperparameter. We evaluate on five MedMNIST datasets spanning histopathology, radiology, and microscopy, comparing against both training-dynamics and geometry-based baselines. Our method achieves the highest balanced accuracy on nine of ten dataset-ratio conditions, with the largest gains on class-imbalanced datasets where global graph construction captures cross-class structure that per-class methods miss, all without any model training during selection. Code is available at this https URL.

---


### 148. [Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study](https://arxiv.org/abs/2606.22009)

**<font color=#1a73e8>作者：</font>** Tomoki Koriyama  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grapheme-to-phoneme (G2P) conversion is essential for controllable and robust text-to-speech, and large language models (LLMs), with broad linguistic knowledge, offer a promising approach. We benchmarked over 30 LLMs on Japanese G2P, comparing them with conventional morphological analyzers on 3000 manually annotated sentences. We evaluated two prompting strategies: a parse mode, where the LLM performs morphological analysis followed by rule-based kana conversion, and a direct mode, where the LLM directly predicts kana readings. The results show that model size, version, and Japanese-specialized training are key factors, with the best LLMs achieving kana character error rate below 0.52\% vs. the best conventional tool (1.03\%). Parse mode outperforms direct mode for most models, as rule-based post-processing relieves the LLM of handling complex pronunciation rules. We also show that feeding LLM-predicted kana into a kana-input TTS yields better pronunciation than end-to-end TTS.

---


### 149. [Channel Location Constrains the Auditability of Subliminal Learning](https://arxiv.org/abs/2606.22019)

**<font color=#1a73e8>作者：</font>** Tamas Madl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal learning lets a student inherit a teacher's hidden trait from distillation data that never names it. We ask when such transfer can be audited before training. The answer is not model identity or scale alone, but channel location: the carrier through which the trait reaches the student. We find three regimes. In a controlled initialization-dependent body channel, a pre-training screen works. Coverage, the cosine between the student's initial distillation update and the teacher's fine-tuning displacement, predicts held-out transfer (Spearman $\rho \approx 0.95$; AUROC 0.997). In pretrained language models, masked single-token traits instead ride convergent vocabulary geometry. This channel is initialization-independent, so initialization-alignment screens, including coverage, are not mechanistic; the useful handles are post-hoc detection and targeted mitigation. Even when a single-token named entity is removed from the loss, the student's held-out probability for that entity rises to 0.40 on average ($\sim 2500\times$), and a related semantic class transfers. In an untied-head model, orthogonalizing the trait's output row against entangled neighbours collapses leakage, while equal-size random-subspace edits do not. Thus removing a target string from distillation labels does not remove the corresponding preference: neighbouring tokens can carry it. Finally, conditional behaviours can route through the network body. For sycophancy, with agreement and correction markers masked from the loss, transfer reaches about 0.63 of the teacher's effect, localizes to body computation, and evades four audits across two model families. We scope this as masked transfer of a condition-present policy. Channel location is necessary for deciding which audits can be sound. It is not a deployment-ready screen: an audit used outside its carrier regime can give false assurance.

---


### 150. [Nous: A Predictive World Model for Long-Term Agent Memory](https://arxiv.org/abs/2606.22030)

**<font color=#1a73e8>作者：</font>** Pranav Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Nous, a novel agent memory architecture grounded in the principle that knowledge is prediction, not storage. Rather than persisting facts as database records, vector embeddings, or knowledge-graph triples, Nous maintains a predictive world model: a collection of categorical probability distributions, called dimensions, one per entity-attribute pair observed in conversation. Each incoming observation is scored by its information-theoretic surprise S = -log2 P(obs | D), and the distribution is updated via a closed-form Bayesian posterior. The primary stored artifact is the delta, a record of the shift from prior to posterior belief, rather than the fact itself. Forgetting emerges naturally as entropy decay toward the uniform distribution, and identity resolution is handled through mutual information between entity dimension sets. Evaluated on the LoCoMo long-term conversational memory benchmark across ten conversations (1,540 questions) using GPT-4o-mini as backbone, Nous achieves F1 of 63.50 (single-hop), 55.32 (multi-hop), 58.57 (temporal), and 62.50 (open-domain). Against A-MEM's self-reported GPT-4o-mini numbers, Nous shows substantial gains in three of four categories, though we note that independent citations of A-MEM's results disagree with each other on category assignment, a reproducibility issue we discuss openly rather than resolve unilaterally. We additionally compare against BeliefMem, a concurrently developed system built on the same core premise of belief-based rather than deterministic memory; on the same benchmark and backbone, Nous's self-reported numbers exceed BeliefMem's self-reported numbers on all four categories, though we flag several uncontrolled differences between the two evaluation pipelines that prevent this from being a fully controlled comparison. Nous requires no external vector database or graph engine.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
