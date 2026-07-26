# 🧠 大模型相关研究 | 2026年07月27日

> 本类共 **153** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-153](./part-04.md)

---

### 1. [What is Good? Extracting and Testing Implicit Theories of Literary Quality from LLM Reasoning Traces](https://arxiv.org/abs/2607.20425)

**<font color=#1a73e8>作者：</font>** Birger Moëll  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What makes writing "good" remains a persistent question in literary studies and computational linguistics. We present a two-study investigation of how reasoning-enabled LLMs evaluate literary quality.
In Study 1, we construct a benchmark of 30 real texts spanning six quality tiers, from canonical literature to anonymous forum posts, and extract the model's implicit theory of quality from its reasoning traces. Across five DeepSeek replications, the model achieves 79.3% mean tier-classification accuracy. The traces reveal a consistent stated theory: the model values intentionality over correctness, prioritizing craft, depth, and distinctive voice. A familiarity experiment with style-matched but unrecognizable passages suggests that source recognition may inflate scores, although this is confounded by genuine quality differences between canonical originals and researcher-written pastiches.
In Study 2, we probe this theory through systematic degradation of five canonical prose passages. We apply six manipulations - vocabulary simplification, rhythm flattening, imagery removal, voice genericization, structure simplification, and combined degradation - and reevaluate each version. Vocabulary simplification causes the smallest quality loss (0.41 +/- 0.46 points), far below structure (2.78) or voice (2.34) loss. Combined degradation is devastating (-5.64) but subadditive. An exploratory comparison with Qwen QwQ shows the same broad qualitative pattern.
Together, these studies suggest that LLM judgments of writing quality are holistic, author-specific, and more sensitive to structural than lexical features, with implications for automated writing feedback and computational aesthetics.

---


### 2. [Knowledge Injection Exists in MoE? Exploring Expert-Aware Contrast Decoding in MoE for Mitigating LLMs'Hallucinations](https://arxiv.org/abs/2607.20426)

**<font color=#1a73e8>作者：</font>** Xinyue Fang, Zhiliang Tian, Zhen Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing LLM hallucination mitigation methods, including prompt engineering and model optimization, either hardly alter models'internal knowledge or have poor cross-domain generalization. Contrastive decoding mitigates hallucinations by using layer-wise differences in LLMs. However, prior studies only explore transformer-based models (e.g., GPT), ignoring other effective frameworks like mixture-of-experts (MoE) models. Since MoE alters the traditional transformer architecture, we conduct empirical studies to investigate whether similar layer-wise differences exist in MoEs. Our results show that they do not exist in MoE with shared experts; nevertheless, across different MoEs, higher layers exhibit distinct expert activation patterns between factual and non-factual outputs. Building on these, we propose EAACD, an expert-aware adaptive contrast decoding that uses expert differences in MoE's higher layers to mitigate hallucinations on QA tasks. EAACD splits high-layer experts into a higher-reliability group and several lower-reliability groups based on their confidence and consistency. It contrasts the higher-reliability group's prediction with each lower-reliability group's prediction to calibrate the model's original predictions. To strengthen this contrast, EAACD amplifies hallucinations from lower-reliability experts via attention and masking to provide stronger negative references. EAACD outperforms all baselines on four datasets.

---


### 3. [Is MoE Routing a Huffman Code? Discovering the Frequency-Diversity Law in Chain-of-Thought](https://arxiv.org/abs/2607.20427)

**<font color=#1a73e8>作者：</font>** Ching-Chieh Tsao, Zhuoyi Lin, Wenya Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts architectures have revolutionized scaling, yet the underlying logic of their routing remains a black box. In this paper, we uncover a fundamental governing principle: MoE routing is not merely selection, but a manifestation of Huffman Coding. We introduce the Frequency-Diversity Law, revealing that state-of-the-art models, such as Phi-3.5-MoE and Gemma-4-27B-A4B, spontaneously act as information-theoretic engines. These models allocate sparse expert resources for common tokens while invoking high-diversity expert committees for rare, complex tasks found in chain-of-thought trajectories. However, we identify a critical redundancy trap in Qwen3.5-35B-A3B: when effective sparsity (k/E_eff) is sufficiently low, load-balancing inadvertently imposes functional redundancy, masking the underlying Huffman efficiency signal. To bridge this gap, we propose Subset Difference Pruning, a surgical strategy to eliminate functional duplicates. We demonstrate that pruning does not degrade reasoning; instead, it unleashes the model's latent Huffman efficiency, forcing the logic to collapse into streamlined, high-density paths. Our findings suggest that the next generation of MoEs should move beyond forced load-balancing toward Minimum Description Length (MDL) optimality, assigning shorter expert-routing codes to high-frequency information and longer, more diverse codes to low-frequency information, thereby transforming routing from a heuristic into a principled compression engine.

---


### 4. [Human-in-the-Loop Large Language Model Framework for Identification of Cutaneous Immune-Related Adverse Events](https://arxiv.org/abs/2607.20428)

**<font color=#1a73e8>作者：</font>** Charles Lu, Olivia Burke, Debby Cheng 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study evaluated a retrieval-augmented, multi-agent large language model (LLM)-driven, human-in-the-loop framework for detecting cutaneous immune-related adverse events (cirAEs) from clinical notes. Compared with unassisted manual review, the LLM-assisted workflow improved accuracy (F1 = 0.88 vs 0.77), inter-rater agreement measured by Cohen's kappa (kappa = 0.82 vs 0.50), and reduced average review time by approximately half. This framework pilots how LLMs can be applied to identify immune-related toxicities across organ systems and, more broadly, enable accurate, scalable, and transparent adverse event data extraction.

---


### 5. [More Is Not More: What Matters for Diversity in LLM Opinions?](https://arxiv.org/abs/2607.20429)

**<font color=#1a73e8>作者：</font>** Qiyang Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to simulate diverse human opinions in open-ended tasks such as synthetic surveys, focus group modeling, and public opinion prediction. However, LLM outputs exhibit systematic opinion homogenization. Practitioners have explored various interventions to increase diversity, but the landscape remains fragmented: different methods are evaluated in isolation with incomparable metrics, and in practice they are typically deployed and upgraded simultaneously, making it difficult to attribute gains to specific components. To advance a more scientific understanding of LLM output diversity, we design a factorial experiment that separates two primary intervention dimensions: input conditioning (operationalized through persona depth) and interaction architecture. We evaluate all conditions on 100 real-user open-ended questions across 7 models, measuring diversity with multiple complementary metrics. Our findings challenge several common assumptions. First, more persona detail does not monotonically increase diversity. The initial step of persona conditioning already captures the majority of the gain, while further elaboration with demographic detail does not consistently improve and can reduce diversity on some models. Second, rather than seeking a single best interaction architecture, we find that different architectures explore largely non-overlapping opinion regions. Combining multiple architectures yields broader coverage than optimizing any one. Third, commonly attempted low-cost alternatives such as raising sampling temperature and adding diversity instructions produce negligible effects compared to structured interventions. Overall, our work demonstrates that diversity is not a product of scaling along any single dimension, but is highly sensitive to the structural form and combination of interventions.

---


### 6. [LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining](https://arxiv.org/abs/2607.20430)

**<font color=#1a73e8>作者：</font>** Phuong Huu Vu Tran, Long Minh Vo, Son Nguyen Minh Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present LLM-INSTRUCT, the winning system for the UZH Shared Task at ArgMining 2026 on paragraph-level argument mining in UN and UNESCO resolutions. The task requires paragraph-type classification, prediction of a subset of 141 official tags, and directed relation prediction under a strict JSON schema setting using only open-weight models up to 8B parameters. We frame the task as constrained structured prediction. The system first narrows the candidate tag space with metadata-aware dense retrieval, then applies constrained decoding with per-dimension caps, escalates only uncertain cases to a three-agent debate branch, and finally validates the output schema. On the official leaderboard, LLM-INSTRUCT ranked 1st overall, with 1st in F1 and 5th in LLM-as-a-Judge. During development, our configuration search further improved Task 1b Micro-F1 from 35.83% to 40.08% while keeping the internal Task 2 score at 4.421. The main lesson is simple: reducing the decision space before generation improves both accuracy and submission robustness. Our code and supporting scripts are publicly available at: this https URL

---


### 7. [Moir: Let the Model Direct Its Own Story for Robust Cross-Domain Knowledge Editing](https://arxiv.org/abs/2607.20433)

**<font color=#1a73e8>作者：</font>** Jea Kwon, Jiwon Kim, Dong-kyum Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While language models remain frozen at their training state, the world evolves continuously. Knowledge editing has emerged as a key alternative to full retraining, but its deployment is bottlenecked by the erosion of core capabilities: mathematical and programmatic reasoning collapse while encyclopedic recall remains intact. We trace this asymmetric degradation to a distributional mismatch. Covariance-based editors preserve only the subspaces spanned by their reference corpus, but fail to capture the operative distribution shaped by post-training such as SFT and DPO. Static external corpora, including Wikipedia and even the original pretraining mixture, cannot recover this shifted manifold. We propose Moir, which estimates the preservation covariance $C$ directly from the model itself by sampling from its own decoding distribution. Seeding generation with a single random vocabulary token bypasses the instruction-following templates that otherwise dominate sampled outputs, exposing the broader subspaces the model has internalized. Moir requires no external data and serves as a drop-in component for any covariance-based editor, a practical advantage given that the pre- and post-training corpora of most modern LLMs are not publicly accessible. Across OLMo-2, Llama-3.1, and Qwen-3 (7-8B), under both MEMIT and AlphaEdit and in batch and sequential regimes, Moir consistently extends preservation in the most vulnerable domains, most strikingly on Qwen3-8B after 20,000 AlphaEdit batch edits, it retains 79.9% GSM8K accuracy compared to 10.9% with the Wikipedia baseline. These results suggest that aligning the preservation distribution with the model's operative distribution is a key factor in non-destructive editing, and that the model itself may be the most accessible source of that distribution for deployed systems.

---


### 8. [Making Open-Source Text LLM Watermarks Durable Against Merging](https://arxiv.org/abs/2607.20435)

**<font color=#1a73e8>作者：</font>** Luisa Scharff, Thibaud Gloaguen, Robin Staab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-source LLMs (OSMs)arereaching near state-of-the-art performance, prompting prior works to trace the text they generate by embedding text watermarking algorithms directly into their weights. Yet, OSMs are subject to post-training modifications, which has been shown to remove the watermark. Model merging in particular, a prominent method used for combining expert knowledge and preventing catastrophic forgetting, strongly removes such OSM watermarks. A key question is how to enable OSM watermarks that survive subsequent merging. In this work, we show for the first time how to design an OSM watermark that is durable against model merging. We propose Merge-Adversarial Training, an adversarial training algorithm to distill text watermarks into model weights while being robust to subsequent model merging. Our approach consistently outperforms all baselines (e.g. with SLERP up to +51 percentage points (pp) TPR@1%FPR with +25 pp on average) while preserving downstream capabilities. We also for the first time evaluate OSM watermarks against realistic merge scenarios, representing common use-cases such as combining expert capabilities or preventing catastrophic forgetting, and with 3 prominent merging algorithms. More broadly, our findings suggest that adversarial training is a reliable approach for increasing OSM watermark durability against post-training modifications.

---


### 9. [Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models](https://arxiv.org/abs/2607.20436)

**<font color=#1a73e8>作者：</font>** Phongsakon Mark Konrad, Toygar Tanyel, Serkan Ayvaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations often assume that behavior observed during testing reflects behavior in ordinary use, but fine-tuning can break this assumption. A checkpoint can appear fixed under evaluation-style prompts while the same behavior persists under ordinary-use prompts. Output scores reveal this mismatch but do not locate it. We investigate whether the distinction is encoded in a stable internal site and introduce an approach that fits a paired activation contrast at a path-patching-informed mid-depth window, then modifies the resulting coordinate on held-out prompts. The intervention closes the evaluation-to-deployment gap in ten of twelve model--behavior settings (six of the eight settings with $n{\geq}120$ paired questions) across four full-matrix instruction-tuned model instances; a fifth model supports localization and edit-provenance checks, and deployment-framed rates change by at most $6.1$pp. The two flat cells, both sycophancy, indicate that a single-coordinate audit is not sufficient when the installed distinction is higher-rank or missed by the depth heuristic. The audit is a diagnostic for fine-tuned checkpoints, not a training-time defense or a guarantee of deployment safety.

---


### 10. [TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG](https://arxiv.org/abs/2607.20437)

**<font color=#1a73e8>作者：</font>** Chahana Dahal, Zuobin Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production Retrieval Augmented Generation (RAG) systems rely on aggregating multiple external documents to answer complex queries. However, the retrieved documents introduce a new threat surface that can be exploited to launch split-knowledge attacks. In this attack, the adversary injects documents that are individually benign but create false associations when combined and fed to language models. This paper shows that the new attack is structurally invisible to existing per-document filters, like LlamaGuard. To address this issue in RAG, this work introduces TopoGuard, a family of graph theory-based methods specifically targeting the split-knowledge attacks by building a semantic similarity graph from retrieved documents and detecting contexts with malicious topology. Grounded on the theoretical analysis, the TopoGuard family has been proven to be effective and robust even with noisy inputs. Extensive experiments are conducted on two retrieval datasets and compared with multiple baseline methods. Specifically, the TopoGuard-$\lambda_2$+Entity catches 21$\times$ more attacks than LlamaGuard-2-8B at 1\% FPR (32.6\% vs 1.5\% recall) on the HotpotQA dataset. Compared with production RAG detection systems using large language models, the proposed TopoGuard variants run efficiently at sub-millisecond latency and stay robust under adaptive adversaries and benign cross-domain queries.

---


### 11. [Preference Tuning as Spectral Update Reorganization](https://arxiv.org/abs/2607.20438)

**<font color=#1a73e8>作者：</font>** Peiyan Zhang, Haibo Jin, Liying Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference-based post-training is usually understood through endpoint behavior, yet the learned update that produces this behavior remains largely opaque. We study RLHF and related preference optimization through the spectral structure of their induced parameter updates. By decomposing effective LoRA updates and reloading their spectral components as plug-in modules, we turn preference-induced updates into objects that can be isolated, recomposed, and directly intervened on. Across model families, optimization algorithms, and supervision regimes, these updates consistently develop a spectral head--tail organization. A compact head emerges early and carries the dominant endpoint shift, while a heterogeneous residual tail remains. The split is functional rather than merely descriptive. Plug-in intervention shows that the head accounts for the visible behavioral departure from the base model, while the tail is weak in isolation. Cross-run recomposition further shows that mixed adapters follow the source of the head, indicating that the head carries run-level solver bias. This endpoint dominance does not imply learning sufficiency. Head-only learning is non-vacuous but fails to recover the full solution, especially on out-of-distribution behavior. Tail-only learning yields little visible gain, yet the full solution is not recovered without the tail. These findings recast preference post-training as structured update reorganization rather than a monolithic behavioral correction, and suggest that alignment gain and coverage loss are tied to how the learned update itself is organized.

---


### 12. [Belief Propagation in LLM World Models: Measuring Strategic Information Bias with Prediction Markets](https://arxiv.org/abs/2607.20441)

**<font color=#1a73e8>作者：</font>** Mykola Khandoga, Yevhen Kostiuk, Anton Polishko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every information ecosystem produces beliefs that shape strategic decisions. Both human analysts and AI systems inherit the blind spots of their information sources. We show that LLMs, combined with prediction markets, function as a calibrated instrument for measuring how far ecosystem-induced beliefs deviate from an external reference: LLMs extract the beliefs a text corpus implies, and prediction market price trajectories, anchored at resolution by realised outcomes, provide the calibration reference against which to quantify the deviation.
We isolate the bias contribution of specific text through ablation: varying information context while holding the model fixed, with a contaminated model that knows actual outcomes as control. Applied to 111 Ukraine-related prediction markets, comprising approximately 93,000 predictions across four models, we find that English news context systematically biases territorial predictions, wrong 64 to 72 percent of the time when it pushes predictions toward territorial capture. A contaminated model that knows actual outcomes shows the same error rate, indicating that the bias originates primarily in the text. Supplementing with Ukrainian military-analytical sources reduces the bias for all clean models, while absolute-error gains are partial and model-dependent.
We show that the distortion originates primarily in the sources, not the models. Consistent across four architectures, it will persist in any system that processes them and propagate into downstream decisions.

---


### 13. [Naver-News-KO: A Korean News Summarization Dataset for Open-Source Fine-Tuning of Summarization Models](https://arxiv.org/abs/2607.20442)

**<font color=#1a73e8>作者：</font>** Daekeun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We release Naver-News-KO, a Korean news summarization dataset of 27,400 (document, summary) pairs collected from Naver News over a ten-day window in July 2022 across two categories (Economy and IT/Science; 77/23 split), with train/validation/test partitions of 22,194 / 2,466 / 2,740 and a mean per-record document-to-summary character-compression ratio of 6.03x. The dataset has been publicly hosted on the Hugging Face Hub since January 2023 and, as of May 2026, receives approximately 33,000 downloads per month; community-maintained Korean summarization models fine-tuned on it include Gemma-2B-ko and Gemma2-9B variants. This technical report (i) documents the collection protocol, the column schema, and the split construction, (ii) reports corpus-level statistics (length distributions, compression ratio, and a measured 16.8% near-duplicate title-Jaccard overlap between test and train that users should be aware of), (iii) positions the resource against other open Korean summarization corpora, (iv) provides a Lead-3 extractive reference point (ROUGE-1 55.1, ROUGE-L 50.6) and two reproducible fine-tuned baselines -- KoBART (R-1 56.6, BERTScore-F1 81.5) and Gemma-2B-ko with LoRA (R-1 55.3, BERTScore-F1 78.3) -- with release-time training scripts, and (v) clarifies the licensing and intended-use scope of the resource. The goal is to provide a citable reference for downstream work that already uses this dataset, not to propose a new benchmark.

---


### 14. [Confidently Deceptive: How Confidence Amplifies the Risk of LLM Deception](https://arxiv.org/abs/2607.20444)

**<font color=#1a73e8>作者：</font>** Ali Asad, Stephen Obadinma, Anshul Pattoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can produce deceptive responses: outputs that mislead users in service of a contextually or experimentally induced goal. Yet it remains unclear how confidently models deceive and whether higher confidence makes deceptive responses more persuasive to end users. In this paper, we study these basic questions in various models and different deception datasets. We provide a comprehensive study measuring confidence through both verbalized self-reports and a range of logit-based estimators. We show that LLMs deliver deceptive responses with substantial verbalized confidence and that human annotators prefer the higher-confidence deceptive response 78% of the time in paired comparisons. Misalignment fine-tuning amplifies the problem. Confidence in deceptive responses rises across all three benchmarks, increasing the resulting potential risk, with effects generalizing beyond the training distribution. Strikingly, models classify their own deceptive outputs as deceptive at high rates (82.7% under misalignment) while still predicting they would produce them - recognition without avoidance. We argue that confident deception is a distinct alignment risk requiring evaluations that jointly measure deception, confidence, and awareness.

---


### 15. [Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content](https://arxiv.org/abs/2607.20446)

**<font color=#1a73e8>作者：</font>** Juho Leinonen, Paul Denny  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used by students to generate natural language responses and program code, there is growing interest in whether LLMs themselves can be used to distinguish AI-generated work from human-authored submissions. In this paper, we investigate the extent to which LLMs can detect their own generated content across multiple educational task types, including programming exercises, reflective writing, and short-answer questions. Using authentic student responses and multiple variants of LLM-generated answers, we evaluate detection performance under different prompting strategies and output formats. Our study addresses three research questions: (1) how accurately LLMs can identify their own outputs across task domains, (2) how detection effectiveness is influenced by factors such as prompt design, response length, and task type, and (3) what characteristics of LLM-generated responses contribute to successful or failed detection. Our findings show that LLM-based detection is highly task-dependent: detection is substantially more reliable for programming tasks and longer reflective responses, but performs poorly for short-answer questions, where LLMs frequently judge their own outputs as more human-like than authentic student responses. We further find that prompt framing and response verbosity have a pronounced effect on detectability in reflective writing tasks, with relatively minor prompt variations significantly reducing detection accuracy, while programming-related detection is more robust to prompt changes. Together, these results highlight both the potential and the limitations of LLM self-detection in educational settings and suggest caution in relying on LLMs as standalone tools for identifying AI-generated student work.

---


### 16. [Domyn-Small: A European 10B Reasoning Language Model](https://arxiv.org/abs/2607.20448)

**<font color=#1a73e8>作者：</font>** Simone Angarano, Francesco Bertolotti, Federico D'Ambrosio 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Domyn-Small, a 10-billion-parameter open-weight reasoning language model released under the MIT license. Domyn-Small is the product of an initial pre-training phase on 9 trillion tokens multilingual data, followed by a post-training pipeline for reasoning, instruction following, and context extension. For the latter, we performed a Continued Pre-Training (CPT) phase that doubles the native context window to 32K tokens, followed by SFT with a math-focused annealing run. Finally, the RL phase includes GRPO with verifiable rewards, DPO, and a multi-environment GRPO stage spanning five task domains: mathematics, code, multiple-choice QA, instruction-following, and tool calling. The 32K-token native context extends to 128K at inference via YaRN, and a chat-template toggle enables dual-mode reasoning. Against peer models in the 7--10B class (Qwen3.5-9B, OLMo-3-7B-Think, Nemotron-Nano-8B, Ministral-3-8B), Domyn-Small achieves a strong accuracy-efficiency balance: it produces roughly one-third as many tokens as Qwen3.5-9B and approximately 35% of OLMo-3-7B-Think's token budget on core reasoning benchmarks, while delivering strong instruction-following (IFEval 79.9) and competitive science reasoning (GPQA-Diamond 50.0). We release the weights and the post-training recipe alongside Domyn Swarm (Apache~2.0), an open-source framework for scalable LLM inference on HPC clusters developed during this program and used throughout this work.

---


### 17. [The Storyteller in the Model: Narrative Pattern Inheritance, Escalation Dynamics, and Alignment Governance in LLMs](https://arxiv.org/abs/2607.20449)

**<font color=#1a73e8>作者：</font>** Adam Rigby, Raz Saremi, Azadeh Sohrabinejad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are trained predominantly on human-authored text, yet the structural and narrative conventions embedded in that text are rarely examined as a source of systematic behavioral influence, or as a governance risk in deployed systems. This paper considers whether the storytelling patterns inherent in published human writing, including archetypal roles such as protagonist, antagonist, and underdog, as well as tension-and-resolution narrative arcs, are absorbed during training and subsequently surface in LLM outputs, causing responses to drift toward unexpected, adversarial, or rhetorically enticing behaviors over extended interactions. Through a systematic literature review and cross-paper analysis of recent empirical studies on LLM alignment, persona dynamics, emergent misalignment, and user interaction patterns, we observe evidence bearing on this hypothesis. The findings reveal three key patterns. First, LLMs reproduce statistical patterns from their training data rather than reasoning independently. Second, measurable latent traits, including sycophancy and deceptiveness, emerge reliably across unrelated prompts. Third, fine-tuning on a narrow narrative task can produce unintended behavioral changes well beyond that task. Furthermore, evidence suggests that persuasive, narrative-style outputs are among the most common LLM products in real-world usage, amplifying these risks. Narrative drift constitutes an unmonitored escalation pathway in deployed AI systems, one that evades discrete-incident detection mechanisms and requires dedicated monitoring instruments.

---


### 18. [AINTMA: Agentic AI Architecture for Autonomous Test Management with Generative Intelligence, Secure Cloud Communication and Adaptive Quality Analytics](https://arxiv.org/abs/2607.20452)

**<font color=#1a73e8>作者：</font>** Vinil Pasupuleti, Shyalendar Reddy Allala, Siva Rama Krishna Varma Bayyavarapu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern software quality assurance demands intelligent, autonomous systems capable of adaptive decision-making across distributed cloud environments. This paper presents AINTMA (Agentic Intelligent Test Management Architecture), a multi-agent agentic AI system that transforms traditional test management into an autonomous quality intelligence ecosystem. AINTMA deploys six specialized AI agents (Test Discovery, Risk Assessment, Reinforcement Learning Prioritization, Execution Orchestration, Generative Quality Intelligence, and Cloud Security Monitor) coordinated through a secure multi-agent communication framework over a cloud-native microservices infrastructure. The Generative Quality Intelligence agent employs large language models to produce plain language quality narratives, defect risk summaries, and data-augmented test recommendations. The RL Prioritization agent models test selection as a Markov Decision Process, learning contextual policies from large-scale historical test execution data (47 features, rolling 36-month window). Secure cloud communication is enforced through a zero-trust API gateway with OAuth2/JWT authentication, encrypted inter-agent messaging, and multi-tenant isolation. Evaluation across 12 heterogeneous software projects over 18 months demonstrates: 88.4% test prioritization accuracy (APFD, vs. 51.2% random, 82.1% best commercial baseline); 43% test cycle time reduction; defect escape rate reduced from 8.3% to 2.1%; 340% ROI at 9-month payback. The agentic architecture scales to 50,000+ test cases with sub-400ms response time, and the generative intelligence module achieves 4.3/5.0 developer usefulness rating. AINTMA demonstrates that agentic AI, combining autonomous multi-agent coordination, generative intelligence and secure smart connectivity, can fundamentally advance software quality management in cloud-scale enterprise environments.

---


### 19. [A Knowledge-Injection Framework for Zero-Shot Adaptation of LLMs to Delirium Prediction](https://arxiv.org/abs/2607.20453)

**<font color=#1a73e8>作者：</font>** Jessica Sena, Shesadree Priyadarshani, Miguel Contreras 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models show promise for clinical prediction, but zero-shot performance on specialized tasks is limited by incomplete domain knowledge, especially for smaller locally deployable models. We present a lightweight knowledge-injection framework for zero-shot ICU delirium prediction that augments a deterministic natural-language summary of structured electronic health record data with an external clinical knowledge report at inference time, without fine-tuning or retrieval. We evaluate LLaMA 3.1 8B and LLaMA 3.3 70B on 3,160 ICU admissions from the MIMIC IV dataset. Adding a clinically meaningful external knowledge report improves AUROC by 8.57 percentage points for the 8B model and 1.99 percentage points for the 70B model compared to no external knowledge. Relative to a GPT-5.2 frontier-model reference without external knowledge report (AUROC 68.86%), knowledge injection reduces the performance gap from 15.66 to 7.09 AUROC points for LLaMA 8B and from 5.30 to 3.31 AUROC points for LLaMA 70B. Random control reports do not improve performance and often degrade it, indicating that gains depend on clinically meaningful content rather than added prompt length alone. SHAP-based attribution further confirms that the injected knowledge is actively used during prediction. These findings suggest that inference-time knowledge injection can narrow the gap between locally deployable open-weight models and frontier closed models while preserving a practical, privacy-preserving workflow for resource-constrained clinical settings.

---


### 20. [Response drift across frontier large language models](https://arxiv.org/abs/2607.20454)

**<font color=#1a73e8>作者：</font>** Mohammed Aledhari, Ali Aledhari, Fatimah Aledhari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> All frontier large language models (LLMs) exhibit response drift -- producing outputs that deviate from expert-validated references -- yet the magnitude and structure of this drift remain uncharacterised by systematic human evaluation. Here we report a fully crossed evaluation in which 47 geographically diverse participants each assessed all 62 multidomain questions across ten frontier LLMs under blinded conditions, yielding 29,140 independent assessments. Every model drifts, but drift magnitude varies substantially: eight models converge on a statistically indistinguishable ceiling (78-81% deviation), while two achieve lower deviation (47-49%). Drift profiles differ across six domains and 62 questions, with pairwise correlations among ceiling models exceeding r = 0.85. Automated similarity metrics explain less than 2% of variance in human judgements. These findings reveal that response drift is universal across frontier LLMs, domain- and question-dependent in structure, and accessible only through human-centred evaluation.

---


### 21. [RE-AD: Real-Time Requirement Adherence for Data Labeling](https://arxiv.org/abs/2607.20455)

**<font color=#1a73e8>作者：</font>** Siddarth Malreddy, Ishan Nigam, Akshay Arora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human-annotated data remains fundamental to training frontier Large Language Models (LLMs). However, crowd-sourced annotations often suffer from quality issues stemming from annotator misunderstanding or lack of engagement. To address this, we introduce a real-time requirement adherence (RE-AD) framework that leverages LLMs to proactively validate labeling quality. Our methodology involves decomposing Standard Operating Procedures (SOPs) into atomic rules via self-reflection, categorizing them by complexity, and applying tiered validation strategies. Evaluated on a synthetic benchmark, the system achieved an F1 score of 0.749. Furthermore, production deployment resulted in annotators accepting and fixing 82% of the errors flagged by the framework. We include ablation studies to demonstrate the impact of our core design decisions.

---


### 22. [Learn2Zinc: Fine-tuning Small Language Models for Text-to-Model Translation in MiniZinc](https://arxiv.org/abs/2607.20456)

**<font color=#1a73e8>作者：</font>** Serdar Kadioglu, Karthik Uppuluri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models excel at code generation for mainstream programming languages but struggle with rare, domain-specific languages such as MiniZinc, a constraint modeling language for combinatorial problems. We investigate whether targeted fine-tuning can teach small language models (0.6B to 20B parameters) to generate syntactically correct and semantically valid MiniZinc models from natural language problem descriptions. Our key finding is that syntax errors dominate failures when working with this domain specific language: the out-of-the-box execution accuracy of small language models such as Qwen3, LLaMa, Gemma, and GPT-OSS is near-zero. We propose a cross-model error bootstrapping approach that collects syntax errors from multiple LLM runs and leverage those to curate an error correction training dataset. This dataset allows us fine-tune small language models that consistently improves both direct code generation and chain-of-thought approaches across all model sizes. With self-reflection and ensembling, our approach achieves up to 98\% execution accuracy. In parallel, solution accuracy still remains at 35\%, indicating that while syntax is learnable, constraint reasoning remains a challenge. We contribute our fine-tuning pipeline, datasets, and models to opens-source for further research on text-to-model translation.

---


### 23. [Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention](https://arxiv.org/abs/2607.20457)

**<font color=#1a73e8>作者：</font>** Aryan Sood, Shantanu Acharya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention. Distributed blockwise methods such as Star Attention reduce this cost by sharding context across hosts, but rely on prepending a static, content-blind copy of the first block to every host. We propose Pulsar Attention, which replaces the static anchor with two lightweight, content-aware components: a small attention-sink prefix that stabilizes softmax, and compact cross-block summaries built via a Max-IDF heuristic that selects chunks containing globally rare tokens. This reduces the Phase 1 per-GPU FLOPs by up to 3.3$\times$ over Star Attention while retaining an identical KV cache footprint. On RULER and BABILong with Llama-3.1-8B, Pulsar Attention outperforms both Star Attention and dense attention at sequence lengths up to 128K tokens, with absolute gains of up to 4.7% over the dense baseline.

---


### 24. [CAMeR: Keyword-Gated Hybrid Activation for Adaptive Memory Retention in LLM Agents](https://arxiv.org/abs/2607.20458)

**<font color=#1a73e8>作者：</font>** Haowen Lai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents operating over extended dialogues accumulate vast amounts of information, yet existing memory systems either retain everything indiscriminately or apply uniform forgetting heuristics that fail to distinguish relevant from irrelevant knowledge. We present CAMeR (Context-Activated Memory Reinforcement), a memory retention framework combining keyword-gated hybrid activation -- a joint symbolic (word-level Jaccard) and sub-symbolic (embedding cosine) gating mechanism -- with adaptive weight dynamics. CAMeR computes a hybrid similarity score for each memory-query pair; memories exceeding a threshold receive reinforcement while all memories undergo controlled decay. We introduce CAMeR-Bench, a 76-memory, 100-round benchmark spanning 8 topic clusters with graded activation frequency, designed to test adaptive retention where existing benchmarks (LoCoMO, LongMemEval) cannot. On CAMeR-Bench, CAMeR's keyword gate achieves a 1.6$\times$ larger retention gap between high-frequency and never-referenced memories compared to embedding-only gating (scissors gap: 0.039 vs. 0.024), while time-driven baselines (Oblivion, SuperLocalMemory) collapse to near-zero weights over 100 rounds. CAMeR's top-5 retrieval saves 83.2\% tokens versus full-context approaches (39k vs. 231k cumulative) while producing weight signals that improve retrieval precision. Through 8 ablation conditions we establish that the keyword gate -- not learnable decay -- is the primary performance driver at this scale. Our findings demonstrate that hybrid symbolic-neural gating provides a simple yet effective mechanism for adaptive memory retention in LLM agents.

---


### 25. [Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts](https://arxiv.org/abs/2607.20462)

**<font color=#1a73e8>作者：</font>** Melanie Rieff, Robin Staab, Thibaud Gloaguen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into clinical workflows, stressing the need for reliable traceability of model-generated output with watermarking. Yet, most watermarks are evaluated on general-purpose benchmarks, leaving domains like medicine, where small token-level perturbations can result in significant semantic changes, underexplored. In this work, we present the first rigorous study of how LLM watermarks affect medical performance, benchmarking 5 watermarking schemes across 11 LLMs and 7 VLMs on various tasks spanning unimodal and multimodal clinical reasoning. Importantly, we complement existing evaluations by introducing a human-expert-validated pipeline for systematically auditing medical reasoning quality, terminological precision, and induced hallucinations. Our results reveal that watermarking can induce substantial degradation across multiple failure modes, including lexical corruption, hallucinated terminology, and amplified misattribution or omission of image findings. Notably, we find that the absence of domain-specific analyses, combined with aggregate metrics that miss failures inherent to clinical text, can systematically obscure practical watermark-induced degradations. Our findings establish domain-specific evaluation as a prerequisite for the safe deployment of watermarked models in medicine, where current benchmarks can otherwise mask clinically consequential failures.

---


### 26. [ClickGuard: Detecting and Spoiling Clickbait News with Informativeness Measures and Large Language Models](https://arxiv.org/abs/2607.20463)

**<font color=#1a73e8>作者：</font>** Wojciech Michaluk, Tymoteusz Urban, Mateusz Kubita 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an AI-driven browser extension that identifies clickbait to help users avoid misleading Internet articles. Moving beyond traditional detection, the application employs a hybrid machine learning architecture that combines transformer-based embeddings with linguistically motivated features and a custom "baitness" score. After evaluating various natural language processing techniques -- from classic vectorizers to large language model (LLM) embeddings -- an XGBoost-based model was developed that achieves an F1-score of 91% on the open combined dataset. Most importantly, the tool can warn users before and after they access a clickbait article. After opening an article, the user receives a percentage score indicating the likelihood that it is clickbait. The prediction is explained based on the analyzed metrics, including those specifically developed within the proposed system. The browser extension also provides a clickbait spoiler -- a one- to two-sentence summary of the entire article. Demo video:this https URL}{this https URL

---


### 27. [Stochastic Sampling is Epistemically Shallow: The Dimensionality Gap Between Temperature Variation and Model Diversity in LLMs](https://arxiv.org/abs/2607.20464)

**<font color=#1a73e8>作者：</font>** Izhar Ali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model gives different answers on repeated runs, does that variation reveal what it does not know? Self-consistency turns the variation into a per-question uncertainty estimate via majority voting. But does the same variation reveal cross-question structure -- related questions flipping together, the way a diverse ensemble does? We compare two regimes on the same questions: one model run $100$ times at $\tau=1$ versus an ensemble of $24$ LLMs run once each at $\tau=0$. A Marchenko--Pastur random-matrix test separates signal from sampling noise on both sides. Within any single model, at most one dimension rises above noise across five families and three benchmarks (MMLU, HellaSwag, GSM8K). Across the ensemble, four eigenvalues clear the noise edge, while a matched-difficulty Bernoulli null produces at most one in $500$ Monte Carlo draws. Self-consistency gives accurate per-question uncertainty but no detectable cross-question structure; only a diverse ensemble surfaces what a model does not know.

---


### 28. [DataPrep-Bench: Benchmarking LLMs as Training Data Preparators](https://arxiv.org/abs/2607.20465)

**<font color=#1a73e8>作者：</font>** Hao Liang, Qifeng Cai, Yibo Lin 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quality of training data fundamentally determines the capabilities of large language models (LLMs), yet no unified benchmark exists to measure how well LLMs, agents, and data-centric workflows actually prepare training data end to end. We view LLM-driven data preparation as comprising two complementary capabilities: data construction, which transforms raw sources into supervised training data, and data quality evaluation, which predicts the training value of candidate datasets before downstream training; throughout, "quality" refers to downstream training utility rather than surface-level textual properties. We introduce DataPrep-Bench, the first unified benchmark that jointly evaluates both capabilities under a shared downstream-grounded protocol over six domains and multiple base models. For data construction, methods consume identical raw sources and are scored by fine-tuning a base model on their outputs jointly with Dolly-15k; alongside this track we release Data-Construction-Skill, a skill-guided agent that lifts the Dolly-only baseline by nearly 20 points absolute on Llama-3.1-8B Finance and is competitive with the strongest agent- and DataFlow-based methods in knowledge-extraction-dense domains. For data quality evaluation, scoring functions are scored by Pearson correlation with downstream performance on a shared candidate pool; we release the Distributional Alignment Score (DAS), a distribution-based evaluator that uses MMD between a candidate dataset and a domain proxy. DAS attains the strongest cross-model correlation in four of six domains and is the only metric clearing r > 0.70 simultaneously in Math, Science, and Medical, outperforming existing quality-, diversity-, and heuristic-based evaluators. DataPrep-Bench provides a unified, downstream-grounded framework for measuring progress on both capabilities as co-equal targets of LLM-driven data preparation.

---


### 29. [JAXBench: Benchmarking Autonomous TPU Kernel Optimization](https://arxiv.org/abs/2607.20466)

**<font color=#1a73e8>作者：</font>** Arya Tschand, Charles Hong, Julian Walker 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rigorous benchmarks have driven progress in autonomous GPU kernel performance optimization by establishing a shared target to hillclimb on, but no equivalent exists for TPUs. We present JAXBench, a TPU-native benchmark suite for AI-generated kernel optimization on Google Cloud TPUs. JAXBench comprises 50 JAX workloads that are both relevant and provide headroom for optimization. We extract 17 production ML operators from architectures in the public MaxText library such as Llama-3.1, DeepSeek-V3, Mixtral, Mamba-2, and AlphaFold2, and translate 33 operators from KernelBench that are validated for correctness and set with new problem sizes that achieve high TPU v6e MXU utilization. Eight of the 17 production operators ship with hand-optimized Pallas kernels from the public Tokamax library and block-size tuned to establish an expert upper-bound baseline. We evaluate four feedback-driven methods on generating candidate Pallas kernels for JAXBench. Across the full suite with Gemini 3 Flash, we find that target-specific context matters more than model scale on a sparsely-documented DSL like Pallas. Conditioning on curated TPU documentation raises per-sample correctness from 5.8% to 37.3% and solves 48 of 50 benchmarks at a 1.28x geomean speedup. Search structure yields significant gains once correctness is achieved, with Autocomp's beam-search pipeline reaching a 1.36x geomean speedup over XLA. On the 8 hand-tuned kernels, Autocomp reaches 1.60x geomean over XLA, recovering most of the 2.08x Tokamax upper bound but trailing on the specialized paged and ragged attention operators. High-quality TPU kernel optimization remains a challenging task, and we release the JAXBench benchmark, evaluation harness, and baseline results to support open source contributions.

---


### 30. [DC-Leap: Training-Free Acceleration of dLLMs via Draft-Guided Contiguous Leaping Decoding](https://arxiv.org/abs/2607.20467)

**<font color=#1a73e8>作者：</font>** Yanhua Jiao, Tianyi Wu, Xiaoxi Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While parallel decoding is central to the efficiency of Diffusion Large Language Models (dLLMs), current strategies are often hindered by overly conservative confidence thresholds. These thresholds, necessitated by the Joint Probability Dependence Error (JPDE), result in redundant denoising iterations and suboptimal inference speeds. To overcome this, we propose DC-Leap, a training-free framework that enables reliable acceleration of dLLMs in the moderate-confidence regime. DC-Leap introduces a Dynamic Contiguous Verification strategy that integrates strictly-ordered causal constraints into the parallel decoding process. By progressively validating token dependencies, this mechanism effectively neutralizes the JPDE, enabling reliable acceleration with comparable performance. Furthermore, DC-Leap incorporates the draft-guided decoding mechanism, where the draft helps extend the context by leaping forward across multiple tokens, providing look-ahead context and retaining the structural benefits of bidirectional attention during inference. Extensive experiments on standard benchmarks demonstrate that DC-Leap achieves substantial speedups, up to 53.19x on MBPP for long-sequence generation, and up to 105.02x when combined with KV-Cache with comparable generation quality. Code is available at this https URL .

---


### 31. [InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents](https://arxiv.org/abs/2607.20468)

**<font color=#1a73e8>作者：</font>** Jehyeok Yeon, Ben Rank, Maksym Andriushchenko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly used to automate research and development tasks, yet existing benchmarks typically evaluate them on prescribed workflows or narrow action spaces. Even nominally open-ended tasks can often be solved by retrieving a well-known recipe and tuning a few hyperparameters, making it unclear whether strong results reflect genuine optimization or memorized solutions. We introduce InferenceBench, where an agent must deploy an OpenAI-compatible inference server and optimize the speed of LLM inference. Each agent receives a target LLM, one H100 GPU, an optimization scenario, and a wall-clock time budget of two hours. Three optimization scenarios isolate distinct bottlenecks of inference (prefill latency, decode latency, and concurrent request throughput) and a fourth balances all three at the same time. Across 15 frontier agent configurations, agents reliably improve over a naive PyTorch baseline (up to $8.08\times$) and often match or exceed serving engines with default settings ($4.05\times$ for vLLM), but still fall below a simple hyperparameter search under the same time budget (up to $11.53\times$). Qualitative analysis of agent trajectories shows that although agents enumerate many relevant optimization techniques, they overwhelmingly converge on a single inference framework. They test only a few distinct configurations and spend the remaining budget re-measuring, repairing, or optimizing hyperparameters rather than exploring substantially different strategies. This suggests the bottleneck is not domain knowledge, but the ability to propose diverse configurations, evaluate them systematically, and submit the best identified solution. Overall, InferenceBench reflects the ability of agents to operate in an open-ended AI engineering setting, where memorized solutions lead to limited improvements.

---


### 32. [DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions](https://arxiv.org/abs/2607.20469)

**<font color=#1a73e8>作者：</font>** Zishan Shao, Lixun Zhang, Kangning Cui 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) handle many tasks with one set of parameters, but under KV-cached inference it is unclear what task-general structure, if any, is used at decode time rather than during prefill. We propose DecodeShare, a protocol that identifies a low-dimensional subspace consistently shared across tasks in decode-time hidden states, and then tests its causal role by removing that subspace only during decoding. In our experiments, disturbing the discovered shared subspace degrades decision performance far more than disturbing either a prefill-derived or random subspace under the same intervention budget. We further show this decode-shared subspace has practical consequences for activation steering: common steering directions can overlap the task-general decode channel. Projecting out this shared subspace directly separates the functional roles of the two components, while evaluating steering vectors at decode-time yields more reliable signal for downstream deployment than prefill-based proxies. Despite its compactness, the shared subspace can serve as a high-leverage causal channel at decode time. Code is available at: this https URL.

---


### 33. [PlanE: Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs](https://arxiv.org/abs/2607.20470)

**<font color=#1a73e8>作者：</font>** Jiacheng Wang, Weiyan Zhang, Guangya Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enhancing the task-specific capabilities of Large Language Models (LLMs) primarily requires substantial instruction-tuning datasets. However, the sheer volume of such data imposes a considerable annotation cost, and a lack of optimization methods for tailoring LLMs to specific tasks. To address the above issues, we propose a \textbf{Plan}ning framework for constructing \textbf{E}xtractive-based LLMs called \textbf{PlanE}, which includes data decomposition, instruction tuning, and prompt inference. Additionally, we introduce a Data-Tuning-Inference (DTI) planner, aimed at selecting the optimal base-LLM and its DTI combinations for specific datasets to improve construction efficiency. The experimental results demonstrate the effectiveness of our PlanE from two views: (1) across different datasets using the same base-LLM, and (2) on the same dataset using different base-LLMs. Furthermore, we validate the generalizability of the proposed DTI planner under different optimization objectives. The codes are publicly available at this https URL.

---


### 34. [Benchmarking the Personalization Capabilities of Large Language Models](https://arxiv.org/abs/2607.20471)

**<font color=#1a73e8>作者：</font>** Ashutosh Srivastava, Siddharth Yedlapati, Vinay Aggarwal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalization, the act of varying a message to induce action from a specific receiver while keeping sender, channel, and time fixed, has a long tradition in psychology and marketing as a two-party problem in which sender and receiver have independent objectives. Large language models remove the bounded-inventory constraint of classical retrieval-and-ranking approaches by generating a continuum of message variants conditioned on inferred receiver state, raising the question of how well current models perform personalization in the classical sense. Existing LLM personalization benchmarks measure sender-side adaptation, in which the receiver is the same user the model is serving. The two-party question, whether a generated message induces its intended action in a third party, has been investigated only through A/B tests and small-scale human studies that cannot be re-run against a new model on demand. We adapt the Bayesian Persuasion framework of Kamenica and Gentzkow (2011) to generative agents and instantiate the formulation in sales, where receiver actions are routinely logged against the outreach that induced them. We release SDR-Bench, a public corpus of 6,279 customer success stories spanning 22 industries and approximately 200 enterprises, served through a temporally constrained simulation that prevents future-data leakage. Across frontier LLMs and deep-research agents, we observe a consistent personalization plateau and on a Fortune 100 tech cohort no model statistically separates successful from unsuccessful outreach. A field deployment with 12 professional sales representatives validates the framework, with 48 percent of model-generated content rated immediately useful and senior-expert agreement at Pearson 0.82. We release SDR-Arena and SDR-Bench publicly to support reproducible study of generative personalization at scale.

---


### 35. [Robust Critics: Defending LLMs Against Multi-Turn Attacks](https://arxiv.org/abs/2607.20472)

**<font color=#1a73e8>作者：</font>** Roman Belaire, Arunesh Sinha, Pradeep Varakantham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a user asks a language model something harmful, is it a genuine attack or a misunderstood but well-meaning question? This ambiguity is one of the central challenges of LLM safety. A model that assumes the worst harms legitimate users; one that assumes the best is easily exploited. The problem is compounded in multi-turn dialogue, where an attacker's true intent may only reveal itself gradually across many exchanges, yet existing safety frameworks apply a contextual bandit treatment, ignoring the trajectory of the conversation.
To that end, we propose Dialogue Critic Guided Sampling (DCGS), a framework that addresses this by inferring user intent at every turn of dialogue. Instead of applying a fixed rule about what is or is not safe, DCGS learns what the user's intent is likely to be based on the full conversational history and generates responses accordingly. Formally, we model adversarial dialogue as a Markov Decision Process and learn value and regret-based critics at both the individual token and utterance (full response) levels, scoring candidate responses via an action-value critic. We prove that this inference-time reweighting approximates exponential tilting of the base policy, guaranteeing improvement in expected return for any finite candidate pool, a property that group-relative objectives do not exhibit. Evaluated on CARES-18k, WildJailbreak, Redbench, and Harmbench, DCGS outperforms strong robust baselines and frontier models on adversarial dialogue tasks. DCGS also transfers to frontier models, improving their robustness without fine-tuning.

---


### 36. [Incomplete Prompt Jailbreaks in Large Language Models](https://arxiv.org/abs/2607.20473)

**<font color=#1a73e8>作者：</font>** Yeonjea Kim, Bumjin Park, Jaesik Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly released as open-weight models with safeguards against harmful requests. Nevertheless, sentence completion remains vulnerable to incomplete harmful prompts. In this work, we formalize this phenomenon as incomplete prompt jailbreaks (IPJ) and provide a systematic empirical characterization of when and how incomplete prompts elicit harmful continuations. We analyze diverse attractor types associated with incomplete sentence continuation and show that LLMs systematically delay refusal until sentence termination. We further demonstrate that training models to refuse incomplete harmful prompts via parameter tuning is insufficient, failing to generalize across both content domains and attractor types. To enable fine-grained control, we identify two functional neurons: termination and continuation neurons. By clarifying their roles in sentence completion, we highlight the potential of neuron-level interventions for more precise and robust IPJ defenses.

---


### 37. [VeriSimpl: Robust Optimization Modeling from Natural Language using Simplification-based Verification](https://arxiv.org/abs/2607.20474)

**<font color=#1a73e8>作者：</font>** Sumaya Abdul Rahman, Seckhen Ariel Andrade Cuellar, Ghani Raissov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language interfaces can greatly benefit the accessibility and usability of optimization modeling, and recent advances in large language models (LLMs) show promise in automatically translating textual problem descriptions into executable solver formulations. However, a key challenge for existing approaches is to ensure that the inferred formulation correctly implements the intended task, even if it may execute without errors. We introduce VeriSimpl, a solver LLM framework for robust natural-language-to-optimization formalization. Our approach is based on the idea of simplification-based verification, where the optimization solver is leveraged to generate simplified diagnostic queries about a candidate formulation to allow the LLM to tractably reason about the correctness of the formulation with respect to the task description. We present such simplification strategies along different dimensions with respect to problem constraints and decision variables, which allow the LLM to reason locally under fixed global contexts. Evaluations on a range of optimization benchmarks show how our approach provides consistent improvements in accuracy over existing methods, while also providing a novel high-precision self-verification signal.

---


### 38. [SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative Verification](https://arxiv.org/abs/2607.20475)

**<font color=#1a73e8>作者：</font>** Pragaash Ponnusamy, Shivam Sahni, Jue Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sampling in LLM inference comprises a combinatorial set of logit processing, token selection, and verification operations for speculative decoding. However, existing implementations either accelerate only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous sampling behavior across a batch, limiting support for dynamic serving workloads and preventing efficient CUDA Graph execution. We present $\textbf{SonicSampler}$, a unified suite of tile-aware Triton kernels that vertically fuses the complete sampling pipeline into a fixed, workload-aware execution model. Our kernels support dynamic per-request sampling behaviors, including grammar-constrained decoding, repetition, frequency and presence penalties, logit bias, temperature scaling, top-$k$ / top-$p$ / min-$p$ filtering, and speculative verification - within a single batched kernel while remaining fully CUDA Graph-compatible. Central to our approach is a novel hierarchical two-stage top-$k$ algorithm that achieves up to $\textbf{10x speedup}$ over competitive baselines and exploits the low-entropy structure of LLM outputs to enable efficient selection over large vocabularies. Across heterogeneous speculative decoding workloads, SonicSampler achieves up to $\textbf{16x speedup}$ over state-of-the-art baselines while preserving flexible batched execution.

---


### 39. [Benchmarking Large Language Models on Multi-Sensor Physical Hazard Assessment](https://arxiv.org/abs/2607.20476)

**<font color=#1a73e8>作者：</font>** Faizan Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an empirical benchmark evaluating how five large language models assess multisensor physical hazard data. Testing 60 scenarios across three categories - multi-sensor joint assessment, response proportionality, and pattern disambiguation - with 1,800 API calls at temperature 0.0, we find that all tested models consistently produced no precautionary warning signal across the tested scenarios where multiple sensors are simultaneously elevated below their individual safety limits, while achieving near-perfect accuracy on single-sensor threshold violations. All five models (ChatGPT-4o, Gemini 2.5 Flash, DeepSeek, Kimi, Llama 3.1 8B) score near zero on Category A multi-sensor scenarios (Q2: 0.000-0.208; Q3: 0.000-0.592) compared to strong performance on single-sensor scenarios (Category B Q1: 0.975-1.000). Structured tabular formatting shows no consistent advantage over plain prose; ChatGPT-4o performs significantly better under prose (p = 0.001). These findings have direct implications for practitioners deploying the tested models in physical safety monitoring systems.

---


### 40. [Semi-Supervised Text-Attributed Graph Distillation](https://arxiv.org/abs/2607.20477)

**<font color=#1a73e8>作者：</font>** Yurui Lai, Samir Moustafa, Renchi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> {\em Text-Attributed Graphs} (TAGs) have emerged as an expressive data model for integrating graph topology with rich textual semantics. Existing representation learning methods over TAGs suffer from severe scalability bottlenecks, particularly together with {\em Large Language Models} (LLMs). While data distillation offers a promising data-centric solution, existing methods fail to capture the complex interplay between graph and text modalities, struggle with the label scarcity inherent in semi-supervised settings, and lack the ability to produce the human-readable textual attributes required for downstream LLM-based tasks.
To address these challenges, we propose \algo{}, a unified semi-supervised framework guided by the {\em Wasserstein Distance} (WSD). Grounded in our empirical findings on real TAGs, \algo{} introduces a graph-text collaborative encoding module that utilizes dual-pathway encoders (graph-aware and -free) within a collaborative self-training scheme to harvest reliable pseudo-labels and fuse complementary graph-text features. Furthermore, we develop a theoretically grounded WSD-based graph sketching algorithm and a cost-effective LLM text synthesis module, which leverages cluster-based keyword extraction to generate coherent, human-readable summaries for condensed nodes. Extensive experiments on benchmark datasets demonstrate that \algo{} achieves a state-of-the-art performance-compression trade-off in terms of both GNN- and LLM-based downstream tasks, enabling effective and efficient TAG learning or analytics.

---


### 41. [Beyond Liars' Bench: The Impact of Lie Typology, Depth, and Sparsity on Deception Detection in LLMs](https://arxiv.org/abs/2607.20479)

**<font color=#1a73e8>作者：</font>** Amr Moustafa, Max Feser, Florian Mai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training probes to detect deceptive outputs from large language models is still an open problem. Recent work has demonstrated that detection probes fail especially in out-of-domain scenarios -- training on one type of lie does not transfer well to deception scenarios involving other types of lies. In this work, we conduct a systematic study on how various factors impact detection performance: representation depth, probe expressivity, sparse feature representations, and the lie typology of the training data. To this end, we augment standard benchmark training data with a supplementary dataset containing diverse types of deception, including fabrication, omission, and exaggeration examples. Analyzing these factors across seven probe types, our experimental results show that the optimal representation depth is highly dataset-dependent, more expressive probes provide only selective gains over linear baselines, and sparse autoencoder features perform similarly to dense hidden states. Ultimately, we demonstrate that the choice of training data and lie typology substantially changes detectability, highlighting that deception detection is a highly representation-dependent problem.

---


### 42. [Routing Without Training: Controllable-Ratio LLM Offloading via Reliability Gating](https://arxiv.org/abs/2607.20481)

**<font color=#1a73e8>作者：</font>** Evan Chen, Shiqiang Wang, Kevin S Chan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Local-cloud collaboration is a practical way to deploy large language models under resource constraints, but existing methods often rely on trained routers or collaboration-aware finetuning that tie routing behavior to a particular operating regime. In this work, we show that such training may be unnecessary: the local model's own inference-time agreement across sampled responses already provides a strong signal for deciding when to trust local execution and when to offload to a stronger cloud model. We propose CARGO, a training-free routing framework that estimates this agreement through prompt-varied sampling, applies Bayesian early stopping for sample-efficient uncertainty control, and supports arbitrary target collaboration ratios through lightweight deployment-time calibration. Across diverse reasoning and question-answering tasks, multiple local LLM families and scales, and both pretrained and finetuned local models, CARGO consistently outperforms other training-free baselines and in several settings surpasses supervised learned routers. These results suggest that effective and adaptable local-cloud collaboration can emerge directly from the local model's intrinsic response behavior, without requiring an additional trained router.

---


### 43. [Tractable Hierarchical Control of Autoregressive Language Models](https://arxiv.org/abs/2607.20483)

**<font color=#1a73e8>作者：</font>** Max Scribner, Antonio Vergari, Vaishak Belle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraining the generation of autoregressive large language models (LLMs) is an important component of integrating language models into formal systems. In the generation of code and data for tasks like program synthesis, ensuring that language models produce syntactically valid output is a prerequisite for processing such output. These languages (such as SQL or JSON) are often designed as $LR(k)$ context-free grammars. By distilling the LLM to a tractable probabilistic model, its autoregressive generation can be steered and masked to incorporate the probability of satisfying logical constraints, ensuring high quality output that is guaranteed to be valid. This paper demonstrates that the satisfaction of any $LR(k)$ grammar of finite duration can be calculated in polynomial time, an improvement over the exponential time of applying previous methods to such grammars. This result enables efficient constraint and steering of LLM generation towards output that better satisfies formal syntactic constraints.

---


### 44. [The Devil is in the Spectrum: Mitigating Representation Collapse in LLMs via Topologically Regularized Side-Path](https://arxiv.org/abs/2607.20484)

**<font color=#1a73e8>作者：</font>** Yiheng Tao, Kaiwen Cheng, Yao Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are fundamentally limited by representation collapse, a bottleneck that severely degrades long-context performance. We identify that existing approaches risk drifting into one of two pathological extremes: homogenization collapse (e.g., attention sinks causing rank deficiency) and isolation collapse (e.g., local attention causing context disconnection). Through spectral analysis of attention dynamics, we derive an intrinsic trade-off between mixing efficiency (spectral gap) and information capacity (effective rank) that standard mechanisms struggle to balance. To resolve this dilemma, we propose the Topologically Regularized Side-Path (TRSP), a non-invasive architectural intervention that achieves spectral balance. TRSP employs a parameter-free Triangular Box mechanism, scaled by a lightweight, length-aware gate, to regularize the token interaction topology. By integrating proximal coupling to preserve effective rank and distal propagation to support non-degenerate mixing, TRSP promotes a geometrically healthier transition operator without altering core attention. Experiments show significant improvements across general capabilities and long-context benchmarks. Notably, on NoLiMa at $8\times$ the training length, TRSP retains $83\%$ accuracy and surpasses the Differential Transformer and Gated Attention by approximately 30 and 50 percentage points, respectively. Code available at: this https URL.

---


### 45. [Expectation Alignment of Language Models for Real-World User Expectations](https://arxiv.org/abs/2607.20485)

**<font color=#1a73e8>作者：</font>** Miaomiao Li, Yang Wang, Bin Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable performance on standard benchmarks, yet it remains largely unexplored whether they truly meet user expectations. Existing evaluation approaches, relying on model heuristics, expert rubrics, or user simulation, fail to capture the diversity and subtlety of real human expectations, causing models to appear competent while misaligning with what users actually seek. We present the first systematic study of user expectations in real-world LLM interactions, proposing a principled procedure to extract semantically rich expectations and introducing ExpectBench, a benchmark grounded in real user expectations. Analyses reveal that current LLMs struggle to satisfy and anticipate what users hope to obtain, highlighting a fundamental source of misalignment. Building on these observations, we propose LENS, a lightweight latent expectation-aware response generation framework. LENS enables models to internalize user expectations and generate better-aligned responses, consistently improving expectation satisfaction and underscoring the importance of explicitly modeling user expectations for realistic human-AI alignment.

---


### 46. [Directional Hallucinations: Ideological Drift in News-Grounded LLM Question Answering](https://arxiv.org/abs/2607.20487)

**<font color=#1a73e8>作者：</font>** Chendi Wang, Liam Cunningham, Tom Yishay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to answer questions about political information, including in election-adjacent information settings where factual errors and ideological distortions are high-stakes. We present a reproducible measurement framework that treats hallucinations, unsupported statements in document-grounded QA, as diagnostic signals of ideological drift. Using 21,727 expert-labeled U.S. political news articles from QBias spanning left, center, and right sources, we (i) generate an article-specific question, (ii) elicit document-grounded answers from three open-weight LLMs and one proprietary model, (iii) detect sentence-level hallucinations via reference-based comparison, (iv) classify the ideological valence of hallucinated sentences with a fine-tuned stance classifier, and (v) probe output logits to relate token-level uncertainty to hallucination and drift. Hallucination rates vary substantially across models and concentrate in contentious topics, while source-ideology differences in hallucination frequency are modest. In contrast, hallucination content exhibits robust leftward drift: a majority of hallucinated sentences are classified as left-leaning, including among hallucinations generated from right-leaning sources. Logit-level analysis shows hallucinations arise in high-entropy generation contexts, and in some models uncertainty also predicts leftward drift, consistent with an "uncertainty to guessing" mechanism. We discuss implications for auditing AI-mediated political information and for designing safeguards in election-relevant deployments.

---


### 47. [Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants](https://arxiv.org/abs/2607.20488)

**<font color=#1a73e8>作者：</font>** Bronislav Sidik, Chaya Levi, Nizzan Kimhi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM frameworks typically fix their team topology at boot time. When an individual agent becomes overloaded at runtime, for example by mixing too many action categories, accumulating tool errors, or queueing behind too many calls, the system has no mechanism to restructure itself. We introduce Autonomous Topology Mutation (ATM), a runtime team-mutation mechanism for multi-agent LLM frameworks. ATM combines telemetry-driven overload detection with three safety invariants that gate each structural change: capability monotonicity, state-routing completeness, and shadow-before-live validation.
ATM monitors a six-signal Bottleneck Index that includes queue depth, context thrash, tool-error rate, role entropy, retry-loop rate, and cross-agent wait time. When a warmup-calibrated threshold is breached for multiple consecutive ticks, ATM factorises the overloaded agent into specialised sub-agents and hot-swaps the parent into a coordinator role while preserving its external identity. State transfer is controlled by privacy-level-aware routing: each memory atom is routed only to a permitted child set, or explicitly dropped with a logged reason. No candidate topology receives live traffic until it has passed a shadow validation window.
On 720 DeepSeek-V3-driven task runs with deterministic tool stubs across four ablation conditions and three workloads, the ATM factoriser split lifts code-task success from 3.3% to 61.7%. The full rail-and-distillation system reduces detected high-privacy memory exposure under a regex classifier from 2.0 to 0.0 events per task while preserving task quality. The runtime rails carrying ATM's invariants add less than 500 microseconds of p99 latency on the agent hot path. A small live-tool probe with real Python execution is included as an external-validity check. The implementation, benchmark harness, and traces are open-sourced.

---


### 48. [EvoSQL: Memory-Augmented Critic-Generator Co-Evolution for Text-to-SQL](https://arxiv.org/abs/2607.20489)

**<font color=#1a73e8>作者：</font>** Jiawei Zhou, Jianwei Wang, Chenyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL has advanced rapidly with large language models, but complex database queries still require reasoning beyond one-shot generation, including multi-step decomposition, execution-based diagnosis, and targeted correction. We present EvoSQL, a co-evolution framework that formulates SQL synthesis as an iterative interaction between a generator and a critic. EvoSQL maintains a contextualized candidate memory, verifies SQL candidates with both execution signals and LLM-based critique, and updates its memory through utility-guided aggregation. To strengthen the underlying generator-critic pair, we further introduce a Self-Distillation Policy Optimization (SDPO) fine-tuning stage that injects execution-aware supervision into modern coding LLM backbones. Experiments on Spider and BIRD show that EvoSQL consistently improves open-source models over Maj@16 baselines, with particularly large gains on BIRD-Dev, ranging from +1.37% for Qwen3-4B to +9.19% for Qwen2.5-Coder-3B. SDPO initialization further improves selected backbones on Spider-Test and BIRD-Dev. These results suggest that memory-grounded co-evolution is an effective path toward more reliable and generalizable Text-to-SQL systems. Code is available at this https URL.

---


### 49. [PhantomFill: When the Form Demands an Answer, Language Models Invent One](https://arxiv.org/abs/2607.20492)

**<font color=#1a73e8>作者：</font>** Rana Muhammad Usman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models in production do not write prose. They fill forms: JSON fields, function arguments, extraction templates. We show that the form itself causes hallucination.
We ask thirteen models the same question about the same input and change only the answer format. The inputs are built so the question cannot be answered: a viral post showing 12,400 likes but no visible replies, a support ticket whose call was never transcribed. In free text, GPT-5.5 answers honestly. It says there is no reply data, 98% of the time. Given a required JSON field for sentiment, the same model invents an answer 40 times out of 40. It fabricates the mood of crowds it never saw and quotes customers it never heard.
The pattern holds with force. Required fields drive fabrication to 100% in ten of thirteen models. An explicit "insufficient evidence" option rescues only the frontier: all nine open-weight models ignore it. A direct instruction, do not infer sentiment, is overridden by the schema in four of six models. Resistance does not come with scale: within a single model family, the smallest model refuses, the mid-sized model fabricates, the largest refuses again. Honesty under format pressure is a training outcome that no one is measuring.
The fabrication hides exactly where hedging is impossible: in required enums and minimum-count arrays, fields where no disclaimer fits. We release PhantomFill, a benchmark with deterministic scoring and two reportable numbers: the Coerced Fabrication Rate and the Escape Utilization Rate. The fix we test is one line of schema. The failure we measure is everywhere.

---


### 50. [Isolating LLM Alignment from Regex: Zero Coverage and Metric-Dependent Divergence Under Adversarial Mutation](https://arxiv.org/abs/2607.20494)

**<font color=#1a73e8>作者：</font>** Alexandre Cristovão Maiorano  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production LLM applications commonly stack a regex filter in front of model-side alignment; prior work found no measurable coverage gain from adding a live Gemini backend behind an active regex filter. We ask whether that ceiling holds when the corpus is \emph{designed to bypass the regex}. We introduce $L_5$-no-regex -- identical to $L_4$-real (Gemini-2.5-flash, token-budget cap, rate limit, output scrub) but with the nine-pattern filter disabled -- and evaluate it against $N{=}45$ adversarial probes across three sub-corpora (carry-forward, regex-bypass, alignment-isolate), amplified by Gemini paraphrase and PAIR to ${\sim}1{,}555$ probe-run pairs over $N{=}5$ replications. Under the primary substring classifier, H1 is refuted: $L_5$ block rate is $0,%$ across all five OWASP LLM Top-10 categories ($\Delta\text{pp}{=}0$ vs.\ $L_0$, $p{=}1.00$; Wilson upper bound ${<}5,%$). A secondary LLM-judge metric on PAIR variants shows $56$--$100,%$ block rates ($p{<}0.01$), revealing alignment does respond to adversarially-framed probes -- but produces refusals too nuanced for substring matching. The sub-corpus differential prediction is not supported ($p{=}1.00$). Alignment's contribution is \emph{metric-dependent}: on natural-language harmful-request probes, it adds zero observed coverage beyond the regex; on adversarially-framed variants, an LLM judge detects refusals the substring classifier misses. The locked corpus, mutation artifacts, and export scripts are released for replication.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-153](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
