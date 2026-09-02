# 🧠 大模型相关研究 | 2026年09月03日

> 本类共 **295** 篇论文：已确认 **283** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-295](./part-06.md)

---

### 51. [StreamScout: Learning When to Look Deeper for Streaming Video Understanding](https://arxiv.org/abs/2609.00291)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Jing Bi, Jinxi He 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires answering questions that arrive at arbitrary moments over an unbounded video stream. Existing systems primarily focus on what to retain in a bounded memory, yet access that memory using the same fixed-cost procedure for every query, despite substantial variation in the evidence required. We argue that deciding how deeply to access memory for each query is as important as deciding what the memory should store. To this end, we introduce StreamScout, an adaptive inference framework that maintains only a lightweight textual timeline in context as the stream unfolds. At query time, StreamScout progressively augments the timeline with up to three increasingly informative visual views: a glance at recent frames, a uniform look-back over the past stream, and query-salient retrieval. At each stage, the model answers immediately if the available evidence is sufficient; otherwise, it escalates to the next view. To improve this stop-or-escalate policy, we probe the cascade on an auxiliary set and distill the model's empirical competence boundary into supervision for a lightweight LoRA adaptation, yielding StreamScout-S. We further refine the policy through reinforcement learning, allowing the model to explore stopping behaviors beyond imitation of the distilled decisions, yielding StreamScout-R. Across three backbones and three streaming benchmarks, StreamScout and its variants consistently outperform prior streaming methods while substantially reducing inference cost and token consumption; on OVO-Bench, for instance, StreamScout-S improves Qwen3-VL-8B by 14.65 points while using 59% fewer tokens than uniform sampling and answering in 1.04 s on average.

---


### 52. [Slow to See, Slow to Suppress: Understanding the Effects of Modality in Context-Memory Conflicts](https://arxiv.org/abs/2609.00293)

**<font color=#1a73e8>作者：</font>** Athulith Paraselli, Etha Tianze Hua, Ellie Pavlick  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how vision-language models (VLMs) handle context-memory conflicts; that is, situations in which the model is given information in context that differs from what was stored parametrically during training. We document asymmetric biases: models tend to prefer in-context information about entities which appear in text, but prefer parametric information about entities which appear in images. We relate this asymmetry to the late representational alignment across modalities, showing that the longer processing time associated with resolving visual entities prevents the suppression of the model's usual factual recall mechanism, thus resulting in more parametric answers. Chain-of-thought reasoning does not appear to resolve the gap, but increasing the amount of visual information in the context does show an effect. These results illustrate the complexity of ensuring consistent behavior as models become increasingly multimodal and retrieval-augmented.

---


### 53. [Toward Workflow-Aware Benchmarking for Healthcare NLP Agents](https://arxiv.org/abs/2609.00296)

**<font color=#1a73e8>作者：</font>** Junyi Yao, Baichuan Li, Zihao Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly proposed for healthcare tasks such as clinical documentation, evidence retrieval, patient messaging, and care coordination. Yet many evaluations remain limited to static medical question answering or one-shot generation, under-representing longitudinal state, interruptions, and human handoffs. We introduce an episode-level evaluation protocol for healthcare NLP agents. The protocol separates evidence across model, agent, and simulated-workflow behavior; specifies a five-field episode schema; and defines annotation and scoring for state continuity, evidence traceability, and escalation decisions. It is instantiated as four task templates: documentation update, evidence retrieval, patient messaging, and triage handoff. The protocol does not claim to measure clinical outcomes or deployment value. Instead, it supplies a reproducible intermediate evaluation layer between static benchmarks and prospective workflow studies, with an explicit cost-sensitive treatment of missed versus unnecessary escalation.

---


### 54. [Workload Identification with Physical Side Channels for AI Governance](https://arxiv.org/abs/2609.00309)

**<font color=#1a73e8>作者：</font>** Simone Gargiulo, Gabriel Kulp  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI compute verification is one of the first tangible and tractable points for international policy aimed at AI governance. Determining whether frontier labs, or any operator, comply with agreements requires the regulating authority to discern how their compute is used. The elementary building block of AI compute is the GPU, and any activity it executes leaves a physical trace. Here, we show that an external observer can identify the class of the workload running on an NVIDIA H200 from its power draw. Unlike on-chip NVML telemetry, which can be spoofed or replayed, such a physical channel can in principle be observed independently of operator cooperation. We recorded $930$ five-second traces at $\sim 10$ MHz, covering seventeen open LLM families and twenty-five non-AI workloads. Over this corpus we separate training from inference and from non-AI computation with an accuracy of $97\%$ and a macro-averaged F1 score of $0.955$, evaluated on model families unseen during training. AI workload spectral content predominantly lies below $\sim 20$kHz and training is particularly recognizable through the memory-bound optimizer update. The GPU operator is then treated as adversarial and able to reshape the physical computation itself. Four evasion strategies are tested to disguise training as inference, producing an additional 680 adversarial traces. A detector hardened against evasion strategies, with the tested strategy held out, catches training $\geq 99\%$ of the time for three of the four strategies. The fourth, diluted low-rank adaptation (LoRA), is detected $48$--$88\%$ of the time with a hardened classifier, rising to $\geq 98\%$ with an additional rescue rule. While these attacks are not a comprehensive evaluation against adversarial behaviour, they offer initial insights beyond genuine activities and a dataset for developing and testing stronger evasion mechanisms.

---


### 55. [Emotional Labor Strategy Preferences in LLM Personas](https://arxiv.org/abs/2609.00310)

**<font color=#1a73e8>作者：</font>** Mohammad Saim, Tianyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotional labor is the effortful management of emotional displays to meet social or professional expectations. Personality traits have been correlated with emotional labor strategies, yet research on this link relies almost exclusively on self-report scales administered only in occupational settings. We investigate whether large language models injected with psychometrically grounded personas reproduce these personality-driven selection patterns across everyday social scenarios. We construct the first emotional labor strategy dataset of 500 socially situated events, each offering three behavioral choices corresponding to surface acting, deep acting, and genuine expression. We source 50 fictional characters from a large-scale personality repository and profile each through two parallel tracks: observer-rated bipolar adjective composites and in-character self-report items. Five LLMs evaluate all scenarios under both persona conditions. We find that models align more towards deep acting, and that Conscientiousness and Emotional Stability consistently predict this preference. Entropy analysis confirms that persona reliably influences the output and varies across models and emotions.

---


### 56. [Latent Mechanisms of Language Control in Multilingual Language Models](https://arxiv.org/abs/2609.00325)

**<font color=#1a73e8>作者：</font>** Ryo Mitsuhashi, Sabri Boughorbel, Majd Hawasly  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models can exhibit unintended code-switching -- unnecessarily alternating between languages during generation. We present a comparative study of three methods that identify language-controlling latents in cross-layer transcoders: activation value-based selection (ValSel), activation frequency-based selection (FreqSel), and LLM-generated latent annotation-based selection (AnnSel). To evaluate the efficacy of these methods in identifying language-controlling latents, we introduce two multilingual benchmarks that exhibit code-switching for fine-grained analysis of language steering across seven languages. Through targeted intervention experiments on Gemma-2-2B and Qwen3-4B, we find that all three methods effectively manipulate generation language, with FreqSel achieving the strongest overall performance, while AnnSel offering interpretable latent selection through explicit language annotations. A knock-out analysis suggests the methods select non-overlapping but each-functional latent subsets, indicating redundancy rather than a single canonical language direction. Code and data can be found at this https URL.

---


### 57. [Topic Matching in the Wild: Benchmark and Lessons from Real-World ASR Transcripts](https://arxiv.org/abs/2609.00330)

**<font color=#1a73e8>作者：</font>** Saman Rahbar, Xiliang Zhu, Irvin Cardoza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In contact centers, real-time agent-assist tools determine, for each of many predefined topics, whether a live customer utterance is relevant and display a coaching card to the agent when it is. The input is noisy and challenging: ASR(Automatic Speech Recognition) transcripts of spontaneous phone conversations, which can be unclear, repetitive, and mostly lack punctuation. To systematically study this real-world task, we curate a human-annotated topic-utterance judgments dataset sourced from real call-center transcripts. We compare three types of matchers: a regex-based baseline, zero-shot sentence embedding encoders, and Gemini-based LLM matchers. In addition, two types of topic representations are studied in our benchmark:keyphrases and natural language description. Our empirical experiments highlight the superior performance of lightweight LLM matchers over embedding and regex models when equipped with natural language descriptions.

---


### 58. [Human-AI Co-Interpretation for Responsible AI: A Hermeneutic Perspective](https://arxiv.org/abs/2609.00334)

**<font color=#1a73e8>作者：</font>** Behrooz Razeghi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Across law, education, policy analysis, and public moral argumentation, LLM outputs are being used often for work that requires interpretations to be justified with textual evidence and explicit normative standards. Yet a recurrent failure mode -- what I call \textit{interpretive misplacement} -- is that model-generated readings get treated as settled meanings without an explicit interpretive frame (sources, scope constraints, normative commitments), without preserving defensible alternatives, and without provenance that lets readers find the supporting passages. In such settings, the risk is not only factual error but lost accountability: readers and institutions cannot reliably assess what an output commits them to, or on what basis. Drawing on philosophical hermeneutics, this paper discusses this risk and derives design principles for structuring human-AI co-interpretation. The paper also provides a structured synthesis of recent scholarship on hermeneutics and AI, organizing this emerging literature into a set of recurrent lines of argument and design-relevant gaps. LLM outputs are treated as candidate readings, whereas hermeneutic understanding is reserved for accountable human interpreters situated in disciplinary historical-linguistic traditions. Human-AI interaction is characterized as an AI-mediated interpretive loop. Hermeneutic understanding is distinguished from token-prediction--based text generation. On this basis, existing LLM techniques are reorganized into design patterns for hermeneutically responsible use in interpretive settings. Finally, the discussion turns to implications for legal practice, educational assessment and feedback, scholarly knowledge production, and public moral argumentation. It also treats digital hermeneutics as a literacy: the capacity to read AI-mediated texts by examining frames, provenance, and readings, and by contesting outputs.

---


### 59. [SlideBank: A Persistent Hierarchical Evidence Bank for Consistent Whole-Slide Reasoning](https://arxiv.org/abs/2609.00342)

**<font color=#1a73e8>作者：</font>** Beidi Zhao, Gexin Huang, Ciro Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whole-slide images (WSIs) are challenging for vision-language reasoning because diagnostically relevant morphology is sparse, heterogeneous, and distributed across gigapixel-scale images and multiple spatial resolutions. Existing WSI models and pathology agents can aggregate slide features or actively acquire evidence, but the information retained after exploration is often difficult to access semantically while preserving its connection to the original visual evidence. We introduce SlideBank, a training-free framework that represents each WSI as a persistent, concept-indexed, and spatially grounded evidence bank. SlideBank performs question-independent coarse-to-fine exploration to identify informative regions and multi-scale views, converts them into explicit morphological observations, and grounds pathology signals to their supporting patches and WSI coordinates. At inference time, questions are routed to relevant signals and evidence scales, and the linked global, regional, and patch evidence is integrated through confidence-based cross-level consensus. Experiments on WSI-VQA and SlideBench-BCNB show that with Patho-R1, SlideBank reaches 52.77% on WSI-VQA and with Quilt-LLaVA, it reaches 50.92% average accuracy on SlideBench-BCNB, while structured signal-guided retrieval consistently outperforms random evidence sampling. Reusing the same bank across repeated queries further achieves over 99% rephrasing consistency and substantially reduces amortized inference cost through persistent evidence reuse.

---


### 60. [From Tool Use to Technological Agency: LoopCAT as a Local-First, Open-Source Tool for Translation Technology Education](https://arxiv.org/abs/2609.00344)

**<font color=#1a73e8>作者：</font>** Gokhan Dogru, Adrià Martín Mor  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translation students need to learn both how to use translation technologies and how to judge the choices those technologies make available. This article presents LoopCAT, an Apache-2.0-licensed, local-first computer-assisted translation environment co-created with OpenAI Codex using GPT-5.5 and GPT-5.6, and proposes a framework connecting workflow competence, evaluative judgement, and technological agency. The account draws on repository history, implementation inspection, and the verification records of an identified development build. LoopCAT combines local project storage, translation memories, terminology, quality assurance, document exchange, and optional connections to local or hosted AI services. Its English, Catalan, and Turkish interface catalogs also make the application itself available as teaching material: students can translate English UI strings into another language, review the existing automatically generated target drafts, import their revisions, and test the interface. We organize these opportunities around four forms of participation: operating a workflow, evaluating outputs, inspecting and configuring mechanisms, and making or defending a bounded intervention. A six-session sequence, a UI-localization assignment, a placeholder example, and an assessment rubric specify how teachers could use the framework. The paper separates implemented capabilities from proposed educational benefits; it reports no new student-learning outcomes. It distinguishes the latest package checks from earlier regression evidence and sets out a protocol for classroom evaluation. LoopCAT provides an inspectable setting for teaching how translation decisions interact with data, interfaces, and software rules. Whether these activities improve judgement, transfer, or participation remains an empirical question.

---


### 61. [Do LLMs Know Your Neighborhood? Auditing LLM Priors for Neighborhood-Level Mobility Prediction and Structural Alignment](https://arxiv.org/abs/2609.00345)

**<font color=#1a73e8>作者：</font>** Saad Mohammad Abrar, Eesha Kurella, Arnav Dadarya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human mobility is central to urban planning, transportation, public health, and emergency response, yet fine-grained trajectory data are often proprietary, restricted, and privacy-sensitive. Large language models (LLMs) offer a potential alternative by generating plausible mobility traces and predicting individual movement, but their ability to infer aggregate neighborhood-level mobility remains unclear. We evaluate zero-shot LLMs on Census Block Group-level mobility prediction across four U.S. metropolitan areas using anonymized Cuebiq data to construct point-level, trajectory-level, and temporal mobility outcomes, paired with sociodemographic and built-environment predictors. We compare LLM predictions with supervised baselines and introduce a directional alignment analysis to test whether LLM-implied predictor effects agree with empirical OLS and Jonckheere-Terpstra trends. Supervised models achieve 0.580 average accuracy, compared with 0.435 for the best LLM, with spatial extent outcomes showing the strongest predictability but also the largest LLM-baseline gaps. Directional analysis shows that LLMs often rely on coarse, stable predictor-level priors that remain similar across outcomes and cities, including asymmetric treatment of protected-group predictors. Overall, LLMs can partially recover aggregate mobility patterns from urban context, but their predictions should not be treated as structurally grounded without auditing empirical alignment and potential bias.

---


### 62. [Detecting Hidden Behaviors in LLMs via Activation-matched Finetuning](https://arxiv.org/abs/2609.00351)

**<font color=#1a73e8>作者：</font>** Robin Haselhorst, Lucie Flek, Florian Mai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can hide hidden behaviors that activate only under narrow conditions, such as backdoor triggers, sleeper-agent deployment cues, sandbagging, or topic-conditioned censorship. Such behaviors are difficult to detect without prior knowledge what to look for. We present activation-matched finetuning, an unsupervised detection method that assumes no knowledge of the trigger or the target behavior. Given a suspect model and a publicly available anchor, we finetune the anchor to reproduce the suspect's activations on a small benign corpus, and score each evaluation prompt by the residual between the two models. Since no benign corpus covers the sparse trigger region, the reference learns the benign computation but not the hidden behavior. Therefore, trigger prompts -- and, crucially, their semantic neighbors -- incur a large residual that signal the presence of unusual behavior to the defender. Testing our method across third-party models and custom models, activation-matched finetuning surfaces hidden behavior reliably. Furthermore, we empirically consider a natural defense-aware attack and showcase that it fails to suppress our detection method without sacrificing the behavior itself.

---


### 63. [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models](https://arxiv.org/abs/2609.00355)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seongtae Hong, Dongyub Jude Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle. The drafter stays autoregressive, so it must stay small. A small drafter cannot afford the image at every step, so vision is compressed, pruned, or hidden. A drafter cut off from the image is then least reliable exactly where the image makes text predictable. We present GLANCE, the first one-pass block drafter that is lossless on an unmodified VLM target, and it breaks the cycle at both ends. A block-diffusion head reads the target's already-fused vision-language state, so vision costs the drafter nothing, and fills a whole block in one forward pass, so depth costs no sequential steps. A wide candidate tree is verified in one target pass, and every audited prompt reproduces greedy decoding exactly. Grounded workloads reward this most, entering a verbatim-copy regime whose long runs cost an autoregressive drafter a pass for every token and a block drafter one in total. Under one engine and one round budget, GLANCE decodes up to 2.93x faster than autoregression, from one draft pass a round where the production EAGLE3-VL head takes eight, and accepts 2.7x longer blocks than an EAGLE-3 head trained on the same corpus. One law organizes these results. Accepted length is set by the target's next-token entropy, with a fitted slope that steepens with grounding across all five tasks. The law transfers across targets and modalities and names its own boundary, since free-running text still favors a chain. Our code is available at this https URL.

---


### 64. [Deterministic LLM Inference Across GPU Kernels: Power-of-Two INT8 Quantization Scales and the Limits of Tolerance-Based Conformance](https://arxiv.org/abs/2609.00363)

**<font color=#1a73e8>作者：</font>** Teng-Ruei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformance suites for quantized GEMM kernels ask whether two implementations agree within a tolerance. We measure what such a suite can detect. Injecting nine faults into a reference INT8 pipeline over 8,232 layer--fault--regime cells of Qwen3-1.7B, we find that every one of five epilogue faults -- scale precision, double rounding, multiplication order, output truncation, fused ordering -- moves the output by at most a single bfloat16 spacing, and by exactly one whenever it moves it at all, across 5,880 cells. A tolerance of one spacing is therefore blind to the entire class by construction: four of the five faults are detected by no check in the suite, and the fifth only under power-of-two scales. Faults that violate the accumulator's exactness preconditions, or that break operand sharing, are detected without exception, and a null fault never fires. What a tolerance-based suite of this shape establishes is therefore narrower than interchangeability: that the preconditions hold, that operands are shared, and that differences stay within one spacing. The power-of-two constraint that exposes the one detected fault is also deployable. Requantizing every weight scale to its nearest power of two makes CUTLASS and Triton agree bitwise at every linear layer (196/196 and 252/252, against 8/196 and 10/252 under the checkpoints' own scales) and yields byte-identical generated token sequences at 1.7B, 8B and 14B (8/8 prompts, against 0/8 at all three). Observed perplexity point estimates are +0.32%, -0.28% and +0.48%; the 90% intervals cover zero at the two smaller sizes but not at 14B, reaching +0.71% and +0.76%. A previously reported +157% perplexity for this intervention was an artifact of a probe that rewrote scales without requantizing the weights; separating the effects attributes 99.8% of it to the resulting weight--scale mismatch rather than to the power-of-two constraint itself.

---


### 65. [Dr. Claw: An AI Scientist Workspace for Vibe Research](https://arxiv.org/abs/2609.00365)

**<font color=#1a73e8>作者：</font>** Dingjie Song, Hanrong Zhang, Dawei Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Command-line coding agents (e.g., Claude Code, Gemini CLI) can already read and write files and sustain long sessions, yet end-to-end research still fragments across chat tools, IDEs, terminals, and writing environments, and the decisions that make it auditable are rarely preserved. We present Dr. Claw, an open-source workspace that wraps existing coding-agent executors in a controllable and auditable human-in-the-loop workflow rather than introducing another autonomous agent. Persistent state objects, a reusable skill library, and multi-executor coordination link human decisions to AI execution, turning planning, execution, and writing into one traceable, recoverable loop. We demonstrate Dr. Claw through an interactive three-view scenario and a failure-recovery walkthrough, and evaluate it against a bare command-line agent sharing the same backend executor, so the comparison contrasts the whole orchestration layer (task graph, state objects, and skill library) with the agent it wraps. Holding the executor fixed, Dr. Claw scores higher on research completeness while persisting an auditable, recoverable process trail. Demo access: repository this https URL, released under AGPL-3.0 with GPL-3.0 upstream components.

---


### 66. [Neurosymbolics for Data Engineering: Achieving Long Context Token Reduction Without Finetuning](https://arxiv.org/abs/2609.00367)

**<font color=#1a73e8>作者：</font>** Vishvesh Bhat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly deployed for sophisticated data engineering tasks such as generating structured queries from natural language, Text-to-SQL, and automating complex spreadsheet operations. However, maximizing their utility demands both higher finetuning-free accuracy and solutions to the computational bottleneck imposed by the Transformer architectures inherent quadratic (On2) time complexity. This paper introduces a novel drop-in neurosymbolic layer designed to seamlessly integrate into existing LLM backbones enhancing logical reasoning and mitigating long-context resource consumption. On the reasoning front, the layer immediately and significantly improves performance yielding an average accuracy increase of 85% across rigorous benchmarks including BIRD-CRITIC and LiveSQLBench, critically achieving these gains without any task specific finetuning or RLHF. Concurrently, we repurpose this approach to address the severe computational strain of long context inference. By leveraging symbolic processing to prioritize and compress relevant contextual information the layer reduces the effective token usage by over 50% and brings the effective time complexity down from O(n2) to approximately O(n) on certain long context tasks. This dual impact approach not only makes LLMs substantially more reliable for data engineering but also drastically reduces the computational pressure on inference chips, making long context tasks more manageable and cost effective.

---


### 67. [FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos](https://arxiv.org/abs/2609.00377)

**<font color=#1a73e8>作者：</font>** Maya Moriya, Sigal Raab, Yael Vinker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FoldingAgent, an agentic framework for inferring explicit parametric folding programs directly from origami demonstration videos. Our framework leverages the reasoning power of a pre-trained Vision-Language Model (VLM) equipped with a suite of specialized tools that enable the agent to simulate geometric transitions, verify physical plausibility, retrieve and compare visual content, and evaluate its own predictions. To translate visual content into folding programs, we define a parametric space that consists of the paper's geometry and a set of parametric folding actions. Unlike models that predict static crease patterns, our agent operates sequentially and possesses the ability to re-plan its actions, effectively mitigating the compounding errors inherent in multi-step folding. Our approach takes a step toward closing the gap between human origami knowledge, which is primarily shared through unstructured visual demonstrations, and computational methods, which typically rely on structured, parametric representations such as a crease pattern or an executable parametric plan. We evaluate our approach on PurelandFold, a newly curated benchmark of diverse Pureland origami videos with ground-truth geometry and action labels. Our results demonstrate that by combining VLM reasoning with a set of specialized tools and physical simulation, we can successfully transform unstructured visual demonstrations into executable, physically plausible folding procedures.

---


### 68. [Removable and Irreducible: A Token-Cost Ledger for the Multilingual Tokenization Tax](https://arxiv.org/abs/2609.00378)

**<font color=#1a73e8>作者：</font>** Madhulatha Mandarapu, Sandeep Kunkunuru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models pay a well-documented tax on non-English text: the same content costs several times more tokens, and because attention is quadratic in sequence length, far more compute. We ask how much of this tax is removable. Framing the token layer as source coding -- transformer compute is monotone in sequence length, whose per-atom floor is the Shannon rate $H/\log_2 V$, an object already applied to tokenizers in prior work -- we assemble a token-cost ledger that splits each language's cost, at fixed parallel content, into a removable coding redundancy, a residual coding slack, an intrinsic-content term, and an orthogonal, irreducible grapheme-to-phoneme term that governs the multimodal rather than the text cost. On FLORES-200 across eight languages, a production tokenizer costs up to $8.9\times$ more tokens for Indic scripts than for English; a script-matched code trained on $1,012$ sentences removes a median $64\%$ of that excess (bootstrap 95\% CI $[0.638, 0.647]$), and a script-fair information floor shows the intrinsic content differs by under $6\%$ -- the tax is representational, not informational. A constructed code removes $98\%$ of a controlled source's redundancy, and the token tax implies up to $79\times$ attention cost. We are explicit about scope and failure: this is compute-and-memory accounting, not a model-quality claim; we neither measure nor claim the cross-lingual direction of the orthographic term; and our matched code is a conservative small-data demonstration. We contribute the unifying ledger, the removable-versus-intrinsic attribution, and an open one-command harness.

---


### 69. [RestoreBench: Can AI Agents Restore Power Flow Convergence?](https://arxiv.org/abs/2609.00384)

**<font color=#1a73e8>作者：</font>** Riccardo Mansutti, Andrea Pomarico, Robert Jakob 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly automate multi-step engineering workflows through tool use, interpretation of intermediate results, and iterative planning. Diagnosing and resolving non-convergent power flow cases is a promising yet largely unexplored application, as it requires engineering judgment, experimentation, and decision-making within constrained action spaces. We introduce a benchmark that evaluates these capabilities across multiple LLMs and three architectures: \emph{chatbot}, \emph{single agent}, and \emph{multi-agent} systems. The evaluation covers two power grids and 46 cases per grid, each requiring one or more corrective actions to restore convergence. The benchmark defines the simulation environment, observation and action spaces, and evaluation metrics, providing a reproducible foundation for developing agentic AI systems for power system planning and operation. The code is available at this https URL

---


### 70. [SlideMix: Enhancing Whole Slide Image Analysis via Multimodal Shuffling](https://arxiv.org/abs/2609.00396)

**<font color=#1a73e8>作者：</font>** Chad Wong, Sicheng Chen, Tianyi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathological whole slide images (WSIs) are central to cancer diagnosis, but their gigapixel scale, tissue heterogeneity, weak slide-level supervision, sparse diagnostic regions, and multi-scale evidence make robust automated analysis challenging. Multiple instance learning (MIL) is widely used to aggregate tile-level features into slide-level predictions, yet existing augmentation strategies often perturb tissue regions without preserving diagnostic relevance, slide context, or cross-scale structure. We propose SlideMix, a model-agnostic multimodal augmentation framework for MIL-based WSI analysis. SlideMix uses a retrieval-augmented vision-language model (VLM)-based Visual-Language Adaptive Region selector to identify diagnostically relevant regions and reduce weak-label noise. It then performs In-place Tile Shuffling within meaningful tissue regions to mix feature embeddings while preserving slide-level context. A VLM-based soft-labeling module supervises mixed samples, while a multi-factor, loss-driven online Curriculum-Learning Feedback scheme adaptively controls shuffle granularity, feature similarity, and shuffle ratio to promote cross-scale representation learning. Across 11 WSI datasets comprising 20,523 slides, 8 diagnostic tasks, and 10 WSI backbones, SlideMix improves accuracy and generalization in most settings and compares favorably with established augmentation baselines, providing a simple plug-and-play approach for more robust and scalable digital pathology models. Source code: this https URL

---


### 71. [Federated Trust for Embodied Robot Capability Marketplaces](https://arxiv.org/abs/2609.00404)

**<font color=#1a73e8>作者：</font>** Xue Qin, Simin Luan, Cong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Robot capability marketplaces, the "app store for robot skills," are emerging as the deployment vector for LLM-driven robot fleets. The default cloud-native answer to "is this package safe to install?" is centralised PKI: one certificate authority, one transparency log, one root of trust. We argue this is the wrong model for embodied robot fleets, where operators face heterogeneous regulatory regimes, air-gapped deployments, tiny operator headcounts, and physical-world consequences for trusting the wrong publisher. We present federated trust: each deployed bridge maintains its own local trust directory of acceptable signers; signers identify themselves with a public key embedded in a detached Ed25519 signature envelope; install-time verification is a local set-membership check rather than a network round trip to a certificate authority. The cryptographic primitives are deliberately standard (Ed25519 detached signatures and SSH-style trust files); the contribution is the architectural commitment that this composition fits embodied robot fleets specifically. We implement the model in a runtime governance layer with a five-subcommand CLI, a registry server, a per-bridge install gate, and 80 tests. A multi-deployment evaluation shows the same registry stream producing divergent install verdicts on bridges with different trust directories, the load-bearing design property. Across 5000 adversarial trials, the strict-mode gate rejects 100% of rogue-publisher, tampered, forged, and revoked-signer attacks, and 96.6% of downgrade attempts under a minimum-version pin extension. A same-hardware comparison against Sigstore-Cosign and python-TUF locates federated trust's per-verify cost between the two and its per-publisher storage footprint below both.

---


### 72. [Dependency-Aware Chain-of-Thought Compression for Financial Reasoning](https://arxiv.org/abs/2609.00413)

**<font color=#1a73e8>作者：</font>** Wenjun Wu, Lei Fu, Kejian Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain of thought prompting improves complex reasoning, but its long intermediate traces create substantial inference cost and hinder practical deployment in financial settings. We present a Hierarchical Semantic Distillation Network, HSDN, for compressing reasoning chains while preserving answer accuracy and logical coherence. The framework combines semantic segmentation, dependency graph construction, dual encoder importance scoring, constrained segment selection, and local boundary rewriting. A frozen Qwen3 4B model is used only for feature extraction and final answer generation, while the compression process remains structured and interpretable. On the AFAC2025 benchmark, HSDN achieves 91.0% accuracy with 68.4% compression, outperforming strong compression baselines in overall score and reasoning coherence. The results show that graph guided compression is effective for high stakes financial reasoning tasks.

---


### 73. [Late Transformer Layers Recode Syntax Canonically: Evidence from Greek Scrambling and Cross-Layer Generalisation](https://arxiv.org/abs/2609.00416)

**<font color=#1a73e8>作者：</font>** Christos Nikolaos Zacharopoulos, Revekka Kyriakoglou, Chara Tsoukala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probing studies have established that syntactic information is decodable in early and middle transformer layers, but what happens to that information in later layers remains poorly understood. We apply a cross-layer generalisation analysis to three Greek-tuned large language models evaluated on tightly controlled minimal pairs: object-relative constructions in Modern Greek, where canonical (Subject-Verb-Object; SVO) and non-canonical (Verb-Subject-Object; VSO) orders differ only in within-clause word order, while preserving propositional meaning. When a probe trained on late layers (20-31) is tested on each early layer individually, it produces below-chance transfer (cluster-corrected, p<0.01), classifying 99.3% of non-canonical sentences as canonical. Probe coefficients reverse sign around layer 22, indicating a directional recoding toward the canonical form rather than simple information loss. These findings characterise a representational format change in late transformer layers that goes beyond the well-established decline in syntactic decodability, and they generate a directly testable prediction for human EEG and MEG decoding studies using the same stimuli. Code and stimuli are publicly available on OSF.

---


### 74. [SpecMind: Enabling Spectrum Intelligence via Multi-Agent Hybrid Retrieval-Augmented Generation](https://arxiv.org/abs/2609.00427)

**<font color=#1a73e8>作者：</font>** Songwei Dong, Bingyan Lu, Makayla Kienlen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The exponential growth of wireless devices is driving unprecedented spectrum demand, pushing spectrum management toward more fine-grained decisions across space, time, and device constraints. As a result, spectrum policymakers and engineers must process large volumes of data that come from diverse sources and take many different forms, such as text and tables. These data sources are often disaggregated and require significant time and effort to integrate, search, and interpret. Furthermore, most of this information is formatted for human understanding and is not readily accessible to automated systems. To address this challenge, we propose SpecMind, a novel Multi-Agent Retrieval-Augmented Generation (RAG) system for spectrum intelligence that performs reasoning over heterogeneous data sources. This system enables autonomous agents to coordinate specialized sub-agents that retrieve and synthesize knowledge across policy proceedings, legal regulations, and license databases. We develop SpecBench, a question and answer (Q&A) dataset based on real-world license records and policy proceedings, addressing the lack of evaluation resources for RAG systems in the spectrum domain. Experimental results demonstrate that SpecMind outperforms traditional, general-purpose RAG systems across spectrum-related tasks, achieving over 80% win rate against strong baselines. The agent-based design enables more accurate retrieval, better contextual reasoning, and improved task completion across diverse query types.

---


### 75. [Don't Trust the Code, Check Its Effects: Runtime Refinement for Regenerated Systems Code Under an Adversarial Generator](https://arxiv.org/abs/2609.00430)

**<font color=#1a73e8>作者：</font>** Jinhao Hu, Ashvin Goel, Laurent Bindschaedler  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work uses large language models to generate systems code from specifications, treating the specification as the durable artifact and the implementation as disposable. Regenerating the implementation specializes it to each workload and device. However, that work lives in a forgiving setting: a component's externally visible effects, its writes and device commands, are recoverable, and the generator is honest, so trust is discharged by re-execution. We target the unforgiving setting: systems code whose effects are irreversible, produced by a generator that may be adversarial. There, re-execution cannot check an effect after the fact, and a proof fails silently when its assumptions do. We take the position that the only safe way to operate here is to deny the generated code the authority to act. The generated code only plans, while a fixed trusted mediator owns every effect and performs one only when the specification would have produced it. Because the guarantee lives in the mediator, not the code, it survives regeneration. We instantiate this as a reference monitor for regenerated device drivers, and characterize the mediability envelope, six conditions on the effect vocabulary: legibility, spec-input observability, correlatability, completeness, outcome enumerability, and explicit durability. They decide when such mediation is possible.

---


### 76. [SAGE: State-Grounded, Abstention-Aware Evaluation of Task-Oriented Dialogue Agents](https://arxiv.org/abs/2609.00434)

**<font color=#1a73e8>作者：</font>** Rayan Khoury, Shih-Yao Lin, Pratyush Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating task-oriented dialogue agents requires judging not merely whether a reply reads well but whether each turn advances the underlying workflow state correctly--a distinction conventional holistic LLM judges can miss because they evaluate the available context as a single unit and require one or more full-model calls per turn. We propose SAGE (State-Grounded Abstention-Aware Evaluation), which compiles a workflow specification and per-turn state diff into atomic, schema-grounded criteria and routes each through a cascade of symbolic and encoder/NLI verifiers that abstain rather than guess, aggregating criterion verdicts into a turn-level decision with an evidence trace. Its recommended operating point, SAGE-Core, decides 81--91% of criteria with only the compiler, symbolic rules, and on-device encoders--at zero paid LLM cost--while SAGE-LLM adds an optional focused-LLM fallback for open-class criteria. Across four slices spanning MultiWOZ, Schema-Guided Dialogue, and ABCD, no evaluated LLM-as-a-judge baseline--including a state-aware GPT-4.1 judge and cheaper GPT-4.1-mini variants--significantly exceeds SAGE-Core on any slice, even though the GPT-4.1 G-Eval judge costs $4.7--8.0 per 1,000 turns to SAGE-Core's $0. A two-annotator human audit (n=200, $\kappa$=0.94) confirms strong label fidelity on the transcript-visible failure classes--where, excluding the weak-salience IUV class, SAGE-Core is statistically tied with the strongest LLM judge--and honestly scopes ignored-user-value as a state-consistency signal with weak broad-human salience. We analyze construct-validity limits from injected failures and partial symbolic circularity.

---


### 77. [Conversation Coach: A Voice-enabled AI System that Helps Practice Difficult Workplace Conversations](https://arxiv.org/abs/2609.00441)

**<font color=#1a73e8>作者：</font>** Fanyou Wu, Suraj Maharjan, Ainur Yessenalina 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective manager-employee communication is critical for retaining high performers and developing underperformers, yet training managers in these skills remains costly. Text-based chatbots offer a scalable approach but cannot provide realistic rehearsal: managers need to practice speaking aloud to build confidence before high-stakes conversations. In this paper, we propose Conversation Coach, a voice-first AI system that enables managers to rehearse difficult workplace conversations in a realistic spoken format. The system addresses three challenges: achieving low-latency interactions with strong language understanding, enabling adaptive conversations through configurable bot personalities that simulate different employee types, and generating personalized feedback on content and policy compliance. We compare an end-to-end speech-to-speech model with a cascaded approach combining automatic speech recognition, a large language model, and text-to-speech synthesis. The end-to-end approach achieves 3$\times$ lower median (P50) latency with native barge-in capability at an estimated 8$\times$ lower cost, while the cascaded approach offers superior reasoning essential for coaching quality. We deployed the cascaded architecture in production, where 40,000+ managers used it over six months, with adoption patterns indicating selective use for difficult conversations.

---


### 78. [(V)LMs generalize beyond surface co-occurrence: Evidence from cross-modal number agreement](https://arxiv.org/abs/2609.00443)

**<font color=#1a73e8>作者：</font>** Zach Studdiford, Kanishka Misra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models learn about grammatical number primarily from co-occurrence, and show frequency effects as a result---sometimes taken to indicate that they do not learn abstract ``rules'', and are instead dependent on specific lexical items. Testing generalization with text stimuli alone cannot settle this debate, since distributional cues (is/are, this/these) easily give number away. We instead use cross-modal generalization as a tool to investigate abstractions in LMs that can also accept visual inputs (VLMs), restricting the evidence that diagnoses number to an extra-linguistic modality. We teach VLMs pairs of new nouns by adding new embeddings and only updating them during learning, comparing conditions where number is diagnosed by visual cues alone against ones where it is disambiguated by text. Across behavior, representational dynamics, and causal mechanisms, we find non-trivial evidence for cross-modal generalization across both exposure conditions, and that linguistic vs. extra-linguistic cue conditions are treated in similar ways in the internal mechanisms of the model. This suggests that statistical learners like VLMs can generalize beyond surface-level co-occurrence and show genuine abstraction-compatible behavior.

---


### 79. [Group Adaptive Clipping Policy Optimization](https://arxiv.org/abs/2609.00444)

**<font color=#1a73e8>作者：</font>** Sheng Jia, Xiao Wang, Shiva Prasad Kasiviswanathan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group relative policy optimization for reinforcement learning with verifiable rewards (RLVR) typically uses a fixed importance-sampling (IS) ratio clipping boundary across all rollouts. We identify a key limitation: rare correct rollouts on harder problems and abundant correct rollouts on easier problems are clipped at comparable rates, despite contributing very different learning signals. Rollouts with low group success exhibit larger IS ratios and carry stronger gradient signal for exploration and solving new problems, yet are disproportionately suppressed by fixed clipping.
To address this, we propose Group Adaptive Clipping Policy Optimization (GAPO), a plug-in modification to GRPO methods that adapts the clipping boundary to the rollout advantage. GAPO is motivated by a reverse-KL trust-region perspective, which suggests that rollouts with larger learning signal should receive proportionally greater update headroom. GAPO requires no reward shaping and preserves the standard PPO/GSPO surrogate while adapting only the clipping threshold. Across Qwen and Llama models, GAPO consistently improves both Pass@1 and Pass@k over fixed clipping and advantage-shaping baselines on math reasoning and coding benchmarks where the pass rates by the base model are relatively low.

---


### 80. [Capability-Gated Language Models: Security Composes, Utility Does Not](https://arxiv.org/abs/2609.00445)

**<font color=#1a73e8>作者：</font>** Patrikas Vanagas, Augustas Mačijauskas, Laurynas Lopata  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deployed language model safeguards (safety fine-tuning, filtering, unlearning) vary by principal only outside the model weights: filters are reconfigured, tiers are multiplied, and artefacts are reissued; inside one set of weights every request meets the same model configuration. This motivates us to define capability-gated deployment: per-principal access control inside one set of weights, whose configurations form a lattice - meets accumulate a principal's restrictions and joins pool a coalition's reach. We instantiate it by sparse rank gating over an existing nested-factorisation mechanism, guide profile search with one-pass attribution, and read every result once from a pre-registered held-out split. Security composes: provably at meets under a monotone-elicitation assumption we falsify pointwise. In two lineages the median held-out meet deepens suppression; the one effect surviving correction strengthens it. Utility does not: individually harmless profiles can compose to retention and fluency damage, and no compositional bound exists.

---


### 81. [HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference](https://arxiv.org/abs/2609.00450)

**<font color=#1a73e8>作者：</font>** Chun-Ting Chen, Dongmin Han, Hangyeol Mun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block Quantization (BQ) is a promising approach for efficient deployment of large language models (LLMs), enabling low-precision computation with controlled accuracy degradation. Compared to scalar weight-only quantization (WoQ), BQ quantizes both weight and activation, offering higher hardware efficiency and end-to-end inference on a unified datapath, but its design space, spanning bit-width, block size, scaling, and numeric formats, remains underexplored.
We provide hardware/benchmark results through design space exploration (DSE). We find that increasing block size improves hardware efficiency by amortizing dequantization and accumulation costs, but degrades accuracy. This trade-off limits conventional BQ methods.
Motivated by this insight, we propose Hierarchical Block Quantization (HBQ). Unlike prior methods [1], [2], which use small blocks and conventional Power-of-Two (PoT) or integer-based scaling, HBQ uses large blocks to maximize efficiency and introduces low-overhead significand (SIG) scaling for second-level quantization. By allocating quantization levels effectively and accounting for distinct activation and weight distributions, SIG scaling compensates for large-block errors more effectively than prior PoT and INT schemes. HBQ-A (accurate) achieves W4A16-level accuracy using only W4A5 while requiring less silicon area than NVFP4. HBQ-E (efficient) further reduces hardware cost by 17% while maintaining higher accuracy than all existing BQ methods.
We implemented a 28nm ASIC accelerator applying HBQ to weights, activations, and KV cache, and integrated a novel partial-sum BQ scheme to further reduce EMA energy.
Compared to state-of-the-art WoQ, HBQ delivers $2.3\times$/$4.6\times$ higher area/energy efficiency at the same accuracy level; $1.6$--$3.3\times$ system energy reduction and $1.5$--$3.0\times$ speedup over prior BQ methods while providing best accuracy.

---


### 82. [mimeo: Compiling Public Expert Corpora into Agent Skills and Testing What Transfers](https://arxiv.org/abs/2609.00453)

**<font color=#1a73e8>作者：</font>** Timothy Kassis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Giving an agent a file about a named expert can supply hard-to-find material, produce a recognizable persona, or change what the agent decides. These are different claims. We test each one. mimeo is an open-source tool that finds a person's public work, checks each extracted quotation against the cached source text, and writes a file an agent can load. Eight logged builds averaged 38 model calls; the check rejects 13.2% of extracted quotations. We tested four expert files with one coding-agent harness. Knowledge access was clearest: mimeo answered all 20 obscure, quotation-heavy questions; no closed-book condition answered more than 10. Keyword search (BM25) over the same pages answered 15-17, a gap this sample cannot resolve. Grounding showed one clear benefit: personas written from model memory misstated a documented position on 1-4 of 20 answers under every grader; the plain agent and mimeo never did. Every persona was easy to spot on short open prompts, and adding task material lowered identification by 18-23 points. mimeo was no more identifiable than a from-memory profile. Judgment transfer remained unresolved because both tests hit their ceiling: every condition found 94-97% of the problems planted in engineering tasks and scored 94-100% on 16 new application scenarios. An AI-judged "sounds like the expert" score changed with the judge: two of four preferred answers based on a model's stereotype, while two found no difference on the same text. That is a caution against relying on a single AI judge. The evidence supports mimeo as a compact, inspectable reference on a person, not as a demonstrated transfer of their judgment. Toolkit and expert profiles: this https URL

---


### 83. [Location-Aware Language Models via Secondary Embeddings](https://arxiv.org/abs/2609.00454)

**<font color=#1a73e8>作者：</font>** Gokul Srinivasagan, Munir Georges  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained transformer-based language models achieve strong performance across a wide range of NLP tasks but remain limited in encoding geo-locational semantics, leading to suboptimal representations of place names and spatial entities. In this work, we propose a lightweight, model-agnostic approach for injecting geo-spatial awareness into pretrained embeddings without modifying the tokenizer or requiring costly retraining. Our method augments input representations with structured geographic signals by combining location names with their corresponding latitude and longitude, and employs a location-focused masking to better align textual representations with real-world spatial relationships. This design allows the model to incorporate geo-spatial context while preserving existing semantic and syntactic knowledge. Experimental results demonstrate substantial improvements in geo-spatial alignment while maintaining comparable performance on standard NLP benchmarks such as GLUE. The method is computationally efficient, requiring only minutes of additional training, and generalizes across multiple model architectures and scales.

---


### 84. [Towards a Belief-Based World Model for LLM Agents](https://arxiv.org/abs/2609.00455)

**<font color=#1a73e8>作者：</font>** Shubham Kumar, Harshit Kumar, Narendra Ahuja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are being used as policies for autonomous decision-making and planning in many domains. Despite their strong reasoning capabilities, LLMs struggle with long-horizon tasks, especially under partial observability. World models are a promising way to enhance policy performance, both during training and inference. During inference, agents currently use world models to simulate the consequences of candidate actions before committing to an action, which can improve decision-making. However, we argue that simulation alone is an incomplete interface for decision-making under partial observability: simulation doesn't adequately capture uncertainty about the current state, which agents may need for accurate decision-making. We address this limitation with Belief-Based World Models (BB-WMs), which model and maintain a belief that LLMs can query to access information on what is known and uncertain about the current state. Before developing methods to learn accurate BB-WMs, we first ask a more fundamental question: does exposing a world model's belief directly to an LLM policy improve decision-making? Our results show that giving LLM agents access to world model beliefs improves task performance under partial observability, while remaining complementary to existing simulation-based world models. Code is released at this https URL.

---


### 85. [Can LLMs Use Relational Transformer Embeddings?](https://arxiv.org/abs/2609.00457)

**<font color=#1a73e8>作者：</font>** Francisco Galuppo Azevedo, Clarissa Lima Loures  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Injecting frozen relational-encoder embeddings as soft tokens into a large language model (LLM) is a conceptually appealing fusion strategy: the encoder handles multi-table structure, the LLM handles language and reasoning, and no lossy text serialization is required. We test this hypothesis concretely by injecting embeddings from a frozen Relational Transformer (RT) into Qwen3.5-4B via a learned MLP projection and LoRA adaptation, trained first with supervised fine-tuning (SFT) on chain-of-thought reasoning traces and then with group-based reinforcement learning (GSPO). We evaluate across 10 binary classification tasks on 6 relational databases from RelBench, under four supervision regimes: single-task (ST), within-dataset (WD), cross-dataset (CD), and all-task (ALL). The hybrid model does not consistently outperform standalone RT: it is frequently below random, highly sensitive to serialization format and relational-token budget, and unstable under RL training. We report these negative results and analyze the failure modes, arguing that soft-token fusion requires stronger alignment objectives and schema-aware design before it can serve as a reliable route to relational prediction.

---


### 86. [Exploring Collaboration between a language and a non-language agent](https://arxiv.org/abs/2609.00474)

**<font color=#1a73e8>作者：</font>** Harini S I, Somesh Singh, Yaman K Singla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics, the strongest available agents are not language models. Integrating non-language agents with LLMs would require \emph{verbalization}: compressing their rich continuous representations into sparse textual summaries at each interaction step. To study whether verbalization constitutes a bottleneck, we introduce \textsc{LLAMIA-Bench}, a suite of six diverse collaborative chess tasks spanning three facets: behavioral imitation, state assessment, and natural-language explanation. Each task instantiates a well-established chess problem that neither the LLM nor the chess engine can solve alone. To solve LLM collaboration with non-language agents, we introduce \emph{latent state internalization}, which projects the subagent's continuous representations directly into the LLM's token stream as learned state tokens, with dynamic re-encoding as actions advance the environment state. Comparing internalization to verbalized integration, our experiments reveal a consistent \emph{verbalization debt}: the performance gap widens throughout training and persists as the LLM scales from 4B to 14B parameters. A single 14B model, \textsc{LLAMIA}, trained with latent state internalization, matches or exceeds task specialists and frontier models including GPT-5.1 with tool access across all benchmark tasks, and generalizes out-of-distribution where task-specific finetunes collapse

---


### 87. [Less Is More: Balancing Positive and Negative Space in Visual Concept Blending](https://arxiv.org/abs/2609.00476)

**<font color=#1a73e8>作者：</font>** Shishi Xiao, Adam J. Coscia, David H. Laidlaw  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphic designers often blend visual concepts to communicate multiple ideas within a single image, leveraging positive and negative space to create balance, emphasis, and aesthetic appeal. While computational methods have begun to support automatic concept blending, they largely overlook the role of spatial composition in the design. To address this gap, we present an automatic pipeline that explicitly applies positive and negative space throughout the blending process. Our approach first identifies plausible regions for concept integration by combining semantic reasoning from vision-language models with geometric constraints derived from real-world examples. Conditioned on these regions, the system generates blended compositions using a hybrid pixel-vector pipeline: diffusion-based inpainting produces a fast, coarse initialization, which is then refined through vector-based optimization at the point level to ensure structural coherence and balanced semantic expression. A multimodal agent orchestrates this process as a planner and evaluator, enabling iterative improvement and interpretable control. Through an evaluation using both baseline comparisons and a user study, we demonstrate greater expressiveness, creativity, and concept recognizability by effectively leveraging positive and negative space. We further demonstrate the generalizability of our approach across diverse applications, including controllable image and infographic generation.

---


### 88. [EGT-KG: Evidence-Grounded Typed KG Retrieval for Practical Scientific QA with Small Language Models](https://arxiv.org/abs/2609.00479)

**<font color=#1a73e8>作者：</font>** Muran Yu, Jiechao Gao, Yuandong Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For emerging scientific research domains, local Small Language Models (SLMs) are becoming more attractive, as they offer stronger privacy control and more stable deployment pipelines than Large Language Models. However, in practice, scientific question-answering on SLMs often operates under inevitable constraints: small literature collections, fragmented evidence, limited context window and reasoning abilities. We propose the Evidence-Grounded Typed Knowledge Graph (EGT-KG), a retrieval framework to improve information retrieval with local SLMs. We assessed three question-answering settings: a vanilla Retrieval-Augmented Generation (RAG) workflow and two EGT-KG workflows: an automatically generated relation schema (AS) and an expert-defined relation schema (ES). Our experiments were evaluated with a six-dimensional evaluation framework (S3CRF: Soundness, Correctness, Completeness, Conciseness, Relevance, Fluency) on a Biopolymer-bound Soil Composite literature benchmark, showing that EGT-KG outperforms the vanilla RAG method in most settings, with the best improvement from llama3:8b: a Final Score of 70.37 (+14.67%) and 68.82 (+12.14%) by AS/ES EGT-KG variants.

---


### 89. [Are Near-Tied LLM Rankings Robust to Family-DIF-Guided Benchmark Recomposition?](https://arxiv.org/abs/2609.00482)

**<font color=#1a73e8>作者：</font>** Qiaoyuan Zheng, Yiqu Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small leaderboard gaps are often interpreted as evidence that one language model is better than another, but their sign may depend on which benchmark items are included. We test this using item-level responses from five benchmarks and a family-label-free spectral approximation to multidimensional item-response theory (MIRT). In owner-disjoint folds, one owner half identifies items with low residual differential item functioning across model families (low-DIF); the resulting frozen, source- and easiness-balanced weights score models in the other half, while equally short matched-random subtests control for generic subtest variation. Full-benchmark and low-DIF rankings remain strongly correlated ($\tau_b=.900$--$.948$). Yet in four of five benchmarks, 30.9--47.1\% of cross-family pairs initially within one percentage point reverse order, exceeding their matched-random medians by 16.9--28.6 percentage points (all $p=.001$). The fifth benchmark shows no reliable excess ($-0.9$ points, $p=.689$). The pattern survives all pre-specified population perturbations, and residual item--family signatures replicate across owner halves; however, no family shows a consistent advantage across benchmarks. Thus, globally stable rankings can still leave individual near-tie orderings sensitive to benchmark composition, and sub-one-point leaderboard gaps should be accompanied by evidence that the implied ordering is composition-robust.

---


### 90. [EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities](https://arxiv.org/abs/2609.00487)

**<font color=#1a73e8>作者：</font>** Feitong Qiao, Liren Peng, Shiming Ren 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier language models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns, making multi-turn attacks one of the least understood failure modes of large language models. Most automated red-teaming methods treat this as a generation problem: produce attacks that break the model. We argue it is better framed as a search problem: discover, organize, and iteratively refine a diverse archive of attack strategies, producing a structured map of how a target model fails rather than a list of one-off successes. We introduce EvoFlint, which applies evolutionary quality-diversity search to multi-turn red-teaming. Attack strategies are phased conversation plans, not raw prompts, and are evolved through LLM-driven mutation and crossover. A Pareto fitness over attack success rate and peak severity preserves selection signal from near-miss attacks. A risk-indexed archive runs novelty search with local competition over strategy description embeddings inside each cell, maintaining diversity without committing to a predefined style taxonomy. A generation-level memory accumulates target-model insights across the population and feeds them back into strategy generation. On the HarmBench-test split, EvoFlint reaches attack success rates of 35.8% on Claude Sonnet 4.6, 59.7% on GPT-5.4, and 94.3% on Qwen3-32B, alongside 98.7% on the older GPT-4o included as a baseline reference. The resulting archive, organized by risk category, exposes for each target which categories of harm its safety training has and has not covered.

---


### 91. [MemeBridge: A Dataset for Benchmarking and Mitigating the Bidirectional Cultural Gap in Meme Interpretation](https://arxiv.org/abs/2609.00491)

**<font color=#1a73e8>作者：</font>** Hangxiao Zhu, Suliu Qin, Zhuoyan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Communicating across cultures is inherently challenging, especially through culturally dense and ambiguous formats like memes. While people expect large language models (LLMs) to hold promise for bridging such gaps, existing benchmark datasets often fail to capture the cultural context necessary for accurate interpretation. To address this, we introduce MemeBridge, a curated dataset centered on U.S.-originated memes, designed to capture two complementary perspectives: (1) how Chinese participants interpret these memes, and (2) how U.S. participants anticipate how people from other cultures might misunderstand them. Here, context refers to implicit cultural knowledge, including background beliefs, norms, and shared assumptions that shape meme comprehension. The dataset was constructed via a multi-stage crowdsourcing pipeline with rigorous validation, including human agreement checks and GPT-based classification verification. Each meme is annotated with sentiment, emotion, cultural significance, and knowledge type, providing rich supervision for downstream tasks. Notably, we observe that the anticipated misunderstandings from U.S. participants are often inaccurate, highlighting the asymmetries in cultural understanding and the challenges of adopting perspectives beyond one's own. This bidirectional framing, which focuses on both expression and perception, enables more nuanced benchmarking of cross-cultural comprehension. Our probing of multiple LLMs reveals that while models developed in different cultural contexts exhibit partial cross-cultural understanding, they often struggle with sophisticated interpretations. By contrast, fine-tuning with MemeBridge improves model performance, underscoring the value of culturally grounded resources for training and evaluating LLMs in globally diverse settings.

---


### 92. [The Privacy-Hallucination Tradeoff in Differentially Private Language Models](https://arxiv.org/abs/2609.00492)

**<font color=#1a73e8>作者：</font>** Krithika Ramesh, Krishna Pillutla, Danish Pruthi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Both privacy and factual accuracy are paramount in high-stakes domains like healthcare. Concerningly, we uncover and investigate a privacy-hallucination tradeoff in differentially private (DP) language models. First, we empirically show that models pre-trained or fine-tuned with DP tend to produce more hallucinations than non-DP counterparts, with increased severity as the privacy budget grows stricter. Second, we investigate model properties driving this tradeoff, demonstrating that DP mechanisms flatten output distributions, potentially redistributing probability mass toward factually incorrect alternatives. Third, through experiments where we control fact frequency in training data, we characterize how information frequency can reduce hallucination risks in DP models. Overall, our findings underscore the need for more nuanced privacy-preserving interventions that offer rigorous privacy guarantees without compromising factual accuracy.

---


### 93. [Human-Anchored Factuality Evaluation with Strategic Annotation](https://arxiv.org/abs/2609.00494)

**<font color=#1a73e8>作者：</font>** Yu Wang, Craig Erickson, Kevin Small  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based factuality judges provide scalable evaluation signals, but their metrics are often systematically biased relative to human judgments. We study human-anchored factuality evaluation under limited annotation budgets, where judge predictions on the full dataset are combined with human labels on a small selectively sampled subset to obtain statistically valid estimates. The efficiency of this approach depends critically on which examples receive human annotation: in factuality evaluation, judge-human misalignment is not driven solely by low confidence, but also by structured failure modes such as incomplete evidence, temporal mismatch, unverifiable claims, and rubric misalignment. To exploit this structure, we introduce a factuality-specific annotation policy design pipeline that uses failure-space analysis (FSA) to derive diverse predictive signals for modeling human-judge misalignment. On an internal reference-based factuality evaluation system (AutoFA) and RAGTruth, where judge-predicted estimates substantially underestimate human-annotated factual accuracy, our FSA-guided policy improves annotation efficiency over uniform sampling and uncertainty-driven baselines, achieving effective-sample-size gains of 40.3% on AutoFA and 27.1% on RAGTruth.

---


### 94. [ViTAL-X: Video-Text Alignment with Cross-Modal Temporal Edits](https://arxiv.org/abs/2609.00505)

**<font color=#1a73e8>作者：</font>** Sethuraman T V, Savya Khosla, Onkar Kishor Susladkar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-text models adapted from image-text architectures (e.g., CLIP) frequently exhibit temporal blindness, the inability to perceive fundamental cues like order, direction, and motion dynamics. Standard datasets mask this limitation by enabling models to exploit static spatial shortcuts. To systematically evaluate this, we introduce XTE-Bench, a diagnostic probe revealing that even large-scale video-language models struggle with basic temporal reasoning, indicating that parameter scaling alone is insufficient to resolve this flaw. To address this, we propose Cross-Modal Temporal Edits (XTE), a self-supervised framework that injects precise temporal supervision. By performing synchronized video-text transformations, XTE generates hard temporal negatives without manual annotation. We instantiate this with ViTAL-X, a lightweight model that equips frozen image-text backbones with temporal awareness while preserving their foundational spatial knowledge. Across six temporal benchmarks, ViTAL-X achieves state-of-the-art performance. Utilizing only 0.4B parameters and 1M training clips, ViTAL-X outperforms 7B-parameter models and surpasses baselines trained on 600x more data. These results demonstrate that targeted, high-quality temporal alignment provides a highly efficient alternative to pure scaling.

---


### 95. [RecalibrateGPT: AI Fatigue Resilient Conversational Interfaces](https://arxiv.org/abs/2609.00506)

**<font color=#1a73e8>作者：</font>** Nikhil Wani  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are powerful, but their interfaces often devolve into a type $\rightarrow$ read $\rightarrow$ retype loop, creating conversational AI fatigue, cognitive load, and eventual task abandonment. To mitigate this, we present RecalibrateGPT, a system introducing five cross-turn operators (Anchor, Replay, Delta, Scope, and Steer) that each target a distinct fatigue type, recalibrating LLM responses through a structured panel by acting on the full conversation history with a single click. Users invoke these operators through the AssistiveButton in one of three operator palette layouts: Vertical, Arc, or Tablet. We conducted two pilot studies with the same 12 advanced LLM users. An initial formative qualitative study identifies a taxonomy of four fatigue types (retyping, scanning, decision paralysis, and context drift) and derives two design objectives for RecalibrateGPT. A follow-up quantitative evaluation finds it reduces perceived cognitive workload by half (NASA-TLX = 2.7) at high perceived usability (SUS = 86.5), suggesting AI fatigue is not just a model-quality issue but an interaction-flow cost that interfaces can remove.

---


### 96. [ISO-RAG: Isoperimetric Noise Control for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.00513)

**<font color=#1a73e8>作者：</font>** Siyuan Zhang, Hanchen Wang, Dong Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) mitigates large language models (LLMs) hallucinations, yet conventional dense retrieval struggles with the complex reasoning paths of multi-hop question answering (QA). Graph-based RAG captures multi-step relationships but suffers from severe semantic drift and high online latency due to noisy global graph traversals. Thus, we propose ISO-RAG (ISOperimetric Retrieval-Augmented Generation), a geometry-aware RAG framework. By projecting the underlying knowledge graph into a hyperbolic Poincare ball to precompute node-wise isoperimetric profiles, ISO-RAG prunes spurious edges during retrieval, restricting the search space to a strictly localized subgraph. This topological purification regulates Personalized PageRank (PPR) diffusion driving the retrieval process, ensuring exact and low-latency convergence. Experiments on multi-hop QA benchmarks demonstrate that ISO-RAG outperforms state-of-the-art baselines by average absolute gains of 10.0% in retrieval recall and 4.3% in downstream exact match, achieving a superior accuracy-efficiency trade-off by fundamentally eliminating the latency bottleneck of global traversals. Our source code is available at this https URL.

---


### 97. [The Interlingua Hypothesis: LLMs Translate via a Latent Task-agnostic Feature Space](https://arxiv.org/abs/2609.00515)

**<font color=#1a73e8>作者：</font>** Jacob Brinton, Jannik Brinkmann, Mark Crovella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently demonstrated improved machine translation performance over strong supervised baselines. This raises questions as to what mechanisms underlie how LLMs perform machine translation between languages. Motivated by recent interpretability findings--namely, that LLMs use massively multilingual latent feature representations to perform language modeling--we propose the interlingua hypothesis. The hypothesis holds that language models translate by reading a source sentence into a latent feature space, and generate a target sentence by reading from the latent feature space. We show three lines of evidence in support of this hypothesis: (1) variance in BLEU across language pairs is largely predictable from language-specific competences with no language pair-specific interaction terms; (2) many model components are causally influential in both monolingual tasks and translation tasks; and (3) fine-tuning on monolingual data recovers a large proportion of translation improvements relative to fine-tuning on aligned documents. Together, these provide convergent evidence in support of the interlingua hypothesis, and suggest new ways of understanding and improving how LLMs can be leveraged to perform translation tasks.

---


### 98. [Learning Task-Specific Antibody Representations via Function-Aware Masking](https://arxiv.org/abs/2609.00518)

**<font color=#1a73e8>作者：</font>** Ayan Goel, Thomas A. Walton, Amirali Aghazadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antibody-specific language models pretrained via masked language modeling (MLM) learn representations that are critical for downstream sequence design and property prediction tasks. Yet, the corruption process itself is rarely leveraged as a source of inductive bias during pretraining. While preferentially masking complementarity-determining regions (CDRs) improves binding-related predictions, antibodies possess diverse biological priors over a variety of functions. Herein, we introduce function-aware masking, a family of pretraining algorithms that align mask placement with specific functional priors (e.g., from IMGT annotations or structure predictions) to shape the learned representation space. We show that these specialist masking strategies significantly improve performance on their respective objectives, yielding up to a 14% gain on structure-related tasks and up to a 5.9x improvement on CDR-related tasks. To further improve performance across multiple functional axes, we develop hybrid masking strategies that integrate multiple priors, balancing reconstruction over binding, structural, and biophysical objectives. Our results demonstrate that informed mask placement provides a parameter-free mechanism for imposing functional inductive biases in antibody language model training.

---


### 99. [The Safeguard Worked. Is the LLM System Safer?](https://arxiv.org/abs/2609.00519)

**<font color=#1a73e8>作者：</font>** Pingyu Wu, Weiming Zhang, Nenghai Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safeguards in deployed LLM services are evaluated by refusal, attack success, and policy violation rates. Those rates characterize how a control performed on the requests it was tested on. A deployment has to answer a different question: how much help with harmful tasks the service still gives an attacker who keeps adapting or finds another way in. We determine what each reported result implies for that question, allowing results from different safeguard families to be compared under one deployment criterion. The evidence requirements are strongly asymmetric. One attack that obtains harmful help from the deployed service suffices to establish that such help remains, and such attacks appear repeatedly in the coded record. Establishing that little remains cannot follow from the safeguard's own numbers alone; it also requires evidence about what the surrounding system still allows after the safeguard performs its local function. Such evidence is supported or derived in only a small minority of the depth-coded claims, and one such claim bounds its scoped residual. A better local score is therefore not, by itself, a stronger claim about the deployment. Safeguard research cannot stop at raising local scores; a gain has to be judged by whether it makes a deployed system any safer.

---


### 100. [Are We There Yet? Assessing Computer-Use Agents for Blind Users' Accessible Interaction with Desktop Applications](https://arxiv.org/abs/2609.00524)

**<font color=#1a73e8>作者：</font>** Satwik Ram Kodandaram, Monalika Padma Reddy, Xiaojun Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computer-use agents are emerging as a paradigm for agentic human-AI interaction, combining language reasoning with multi-modal interface grounding to operate GUIs. Yet their effectiveness for blind screen-reader users in real-world desktop workflows remains unclear. We present a three-week diary study with 8 blind users using OLLA, a screen-reader-accessible CUA prototype, collecting 1,258 commands across 12 applications with screenshots, UI trees, model responses, and action traces. We evaluate GPT-5 during deployment and re-execute the same commands with four additional models. GPT-5 achieved the highest success rate at 52.5%. Trace analysis reveals grounding, planning, constraint-tracking, and termination failures, while interviews reveal beyond-automation needs.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-295](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
