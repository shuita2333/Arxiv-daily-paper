# 🧠 大模型相关研究 | 2026年11月27日

> 本类共 **267** 篇论文：已确认 **249** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-267](./part-06.md)

---

### 51. [Benchmarking Open-Ended Vulnerability Discovery in Windows Kernel Binaries](https://arxiv.org/abs/2611.33486)

**<font color=#1a73e8>作者：</font>** Jongseong Kim, Hwiwon Lee, Dongjun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier models are increasingly used to discover real-world security vulnerabilities, making it critical to systematically evaluate their cybersecurity capabilities. However, existing security benchmarks primarily focus on known vulnerabilities in open-source projects, largely overlooking closed-source binaries, which underpin much of the software industry. In this paper, we ask: how effective are frontier models at uncovering deep vulnerabilities in production binaries? To answer this question, we present DeepBinary, the first comprehensive benchmark for open-ended vulnerability discovery in Windows kernel binaries. Given a target binary, an agent analyzes it using a disassembler and kernel debugger in network-isolated VMs and reports each vulnerability with a crashing proof of concept (PoC). Unlike existing benchmarks, DeepBinary replays every report on fresh VMs and employs an LLM-based judge to assess its validity, uniqueness, and impact (estimated by bug bounty values). Beyond known vulnerabilities, DeepBinary also enables the discovery and validation of previously unknown (0-day) vulnerabilities. We conduct a comprehensive evaluation of representative open- and closed-weight models (including GPT-6 Sol, Claude Opus 5, and DeepSeek V4.1 Flash) across diverse coding agents (including Codex and Claude Code) on 12 target binaries. In total, they discover over 200 vulnerabilities with an estimated aggregate bounty of $661,000, including 146 distinct previously unknown vulnerabilities across all experiments. Our results further reveal substantial differences in models' ability to analyze binaries, conduct experiments, and sustain vulnerability discovery over long horizons. Overall, DeepBinary makes long-horizon, open-ended vulnerability discovery in complex binaries measurable, revealing fundamental differences in how frontier models analyze and explore such systems.

---


### 52. [EvOrderBench: When do sampled frames establish event order?](https://arxiv.org/abs/2611.33492)

**<font color=#1a73e8>作者：</font>** Xiaoqin Feng, Yuqi Li, Xinyuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are often asked which of two actions in a video happened first, given only a few sampled frames. Such frames can show that both actions occurred without showing which came first, so a reliable model should state an order only when the frames establish it. Forced-choice temporal benchmarks treat every input as answerable and reward lucky guesses, while answerability benchmarks do not separate frames that miss an action from frames that show both actions but not their order. We introduce EvOrderBench, a real-video benchmark of 579 event families. Each family fixes an episode and a question and varies only the frames: of two four-frame inputs, only one establishes the order, and two six-frame inputs extend the other one with either the frames that resolve the order or frames that do not. Every input is labeled for whether its frames establish each action and their order. Across sixteen open-weight configurations and three closed-source references, the best open models order nearly as accurately as the references when the frames establish the order, but withhold correctly on at most 83% of the inputs where they do not, against at least 90% for every reference; forced-choice accuracy cannot reveal this gap. Open models withhold mainly when the frames show neither action; once the frames show one or both, most of them commit to an order. Thinking narrows the gap, even when it is switched on within a single checkpoint, mainly by separating sufficient from insufficient evidence rather than by making models more cautious overall. Accurate ordering thus does not imply knowing when the frames fall short, and benchmarks should reward withholding alongside ordering.

---


### 53. [CA-RAG: Constraint-Aligned Retrieval for Structurally Faithful Long-Form Generation](https://arxiv.org/abs/2611.33497)

**<font color=#1a73e8>作者：</font>** Vimal Kumar Kumar, Meghana Kshirsagar, Conor Ryan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) typically optimises evidence selection for semantic relevance, whereas compliance-sensitive long-form generation also requires evidence supporting explicit structural obligations. Semantically relevant retrieval may therefore omit information needed for mandatory downstream clauses. We propose Constraint-Aligned RAG (CA-RAG), a retrieval-conditioning framework that augments section-specific queries with ontology-derived structural constraints and policy-grounded knowledge-graph relations before evidence selection. Retrieval-only evaluation with manually annotated evidence shows consistent improvements across retrieval budgets. At $k=6$, CA-RAG increases Precision@$k$ from $0.5268$ to $0.5692$, pooled Recall@$k$ from $0.5402$ to $0.5950$, and F1@$k$ from $0.5389$ to $0.5672$ over standard RAG. Generation experiments further show improvements in compliance and reliability in several model--domain settings, while generation-only constraints achieve higher clause coverage but lower overall compliance and reliability. These results indicate that structurally aligned retrieval can improve evidence sufficiency in compliance-sensitive long-form generation.

---


### 54. [Evaluating Large Language Models on conversational African American English: Feature classification and next-turn generation](https://arxiv.org/abs/2611.33499)

**<font color=#1a73e8>作者：</font>** Romeo De Timmerman, Thomas Demeester, Els Lefever  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are known to misinterpret and misrepresent regional and social varieties of English other than Mainstream American English (MAE), such as African American English (AAE), yet most evaluations of these biases have relied on synthetic, stylized or decontextualized data. This paper instead evaluates LLMs on authentic, conversational AAE to more closely reflect how such models may encounter AAE when deployed as chatbots. Concretely, we perform two complementary evaluation tasks on 100 six-turn segments randomly sampled from the Corpus of Regional African American Language (CORAAL; Kendall and Farrington, 2024), comparing three closed-weight LLM configurations: Gemini 2.5 Flash with and without reasoning, and GPT-4.1 mini. The first task compares the models against gold-standard manual annotations for five AAE morphosyntactic features, while the second assesses their ability to generate contextually appropriate next turns, evaluating outputs for AAE feature frequency, diversity (Self-BLEU), and pragmatic quality. Reasoning-enabled Gemini is the strongest feature detector by a clear margin (macro F1 of 0.91), outperforming both other LLMs as well as a finetuned BERT-based baseline (Masis et al., 2022). In generation, however, all LLMs underproduce AAE relative to the human speakers and produce relatively uniform continuations, with reasoning-enabled Gemini producing the least AAE and the least diverse output. We conclude that a model's ability to detect AAE does not straightforwardly translate into its spontaneous use of AAE in generation, and argue that addressing this gap requires changes upstream, in how pretraining and alignment data represent dialectal variation.

---


### 55. [Using AI to Simulate the Behaviour of European Populations](https://arxiv.org/abs/2611.33503)

**<font color=#1a73e8>作者：</font>** Umair Mehmood Imam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can stand in for survey respondents, but leading approaches build their simulated people from interviews or individual records. We show that a model can learn how European population groups respond from published statistics, without interviews and without training on individual records. We fine-tune an open-weight language model on more than 12 million published group-level answer distributions from about 40 European countries, setting it up to predict each group's departure from a reference distribution. On opinion surveys from its training families it calls the direction of group differences right 84% of the time, ahead of a demographic statistical model (77%, paired test) and level with Claude Opus 5 and 5.5, which it also ties on accuracy; the frontier models are more accurate on new questions. On 278 held-out questions, almost all from the survey families seen in training, its error is 12% lower than that statistical model. It runs on a single 32 GB GPU or a high-memory laptop, and in a test with an earlier model, an evidence gate calibrated on half of a survey's questions fell back to the reference where the model's adjustments did not help. Coupled to a transport simulation of a planned metro closure, with a conventional elasticity as the reference, it adds a testable age gradient to the response, which we freeze for later scoring.

---


### 56. [LogToPersona: New Benchmark and Efficient Persona Prediction through Semantic Log Filtering](https://arxiv.org/abs/2611.33510)

**<font color=#1a73e8>作者：</font>** Ahmed Alajrami, Ondrej Bohdal, Seokwoo Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detailed knowledge of a user's persona is valuable for personalizing generative AI models and agents, yet such details are difficult to obtain and change over time. We address the task of inferring persona attributes from a single day of mobile activity logs. No suitable publicly available benchmark exists for this task, so we introduce a synthetic benchmark of 1,600 persona-log pairs. We target on-device inference so that raw logs never leave the phone, which makes memory rather than speed the limiting constraint: a day of activity yields roughly 30K tokens, whose key-value cache alone exceeds the INT4 weights of a 4B-parameter model. We therefore propose a log filtering method that retains only behaviorally distinct entries. Filtering reduces the memory footprint by up to 39% across nine models from four families and more than halves prefill time, while maintaining or improving prediction quality. For Qwen3-4B it removes 2.5GB, bringing the model from well beyond a realistic per-process budget to a manageable one. Within our benchmark, these results indicate that preserving diverse behavioral events matters more for persona prediction than retaining every semantically similar log entry.

---


### 57. [Evaluation and Restoration of Safety in Reasoning-Tuned LLMs](https://arxiv.org/abs/2611.33515)

**<font color=#1a73e8>作者：</font>** Ehsan Latif, Roberto Dailey, Risto Miikkulainen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-source LLMs that are optimized for reasoning, such as VibeThinker, aim to democratize AI by bringing high-capability models to users with limited resources. They are broadly available but lack regulation and external guardrails; therefore, in order to integrate them safely into human society, it is critical that they perform in a safe manner. There are popular and intuitive arguments for why improved reasoning should improve safety, but recent evidence suggests that, in fact, the opposite may be true. This paper aims to characterize and mitigate this issue. First, it develops a metric for evaluating LLMs optimized for reasoning, and shows that increasing reasoning across multiple model families increases the unsafe rate in all cases. Second, it proposes a method for restoring safety by combining evolution strategies with a post-training guardrail (ESPG). Compared to alternative methods for safety post-training such as GRPO, ESPG is simple to implement, requires no GPU memory beyond that of inference, and works with remarkably few training samples (e.g.\ 30), yet makes the model significantly safer. The study thus establishes a path towards safe post-training of open-source AI models.

---


### 58. [PRECEPT: Security Self-Improvement of Coding Agents via Evolving Principles](https://arxiv.org/abs/2611.33519)

**<font color=#1a73e8>作者：</font>** Keyan Guo, Rupam Patir, Haipeng Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents increasingly write and submit code with limited human review, and much of it passes functional tests while remaining insecure. We show that these failures persist. Across 14 task sequences, Codex, Claude Code, and Qwen Code fixed a vulnerability 85.7% of the time when shown the failing security test, then reintroduced the same vulnerability class in a new session 26.7% of the time, about as often as agents that had never seen it (27.5%). The capability is present; the retention is not. Neither recording the repair in the agent's persistent context nor supplying published secure coding principles closed the gap: the recorded fix stayed tied to the family of the task it came from, and the principles, written for human developers, remained too general to apply to the code at hand. The knowledge exists; it is not activated. We call the missing ability security self-improvement: an agent learns from its own security failures so that each lesson persists across sessions, applies to new code, and does not break what works. We present PRECEPT, which equips coding agents with this ability through an evolving library that starts from authoritative secure coding principles and revises them against the agent's own failures, so that each principle comes to fire on the code where that agent actually goes wrong. A revision is kept only if fresh executions show it makes code more secure while keeping functional success within a small tolerance of the agent without the library. Improvement continues across evolution steps rather than saturating after the first. On task families never seen during evolution, PRECEPT's weakest agent reaches 97.1% secure working code, above the strongest unaided agent at 81.9% and the strongest baseline at 87.7%.

---


### 59. [Deletion You Can Check: Auditing LLM Unlearning](https://arxiv.org/abs/2611.33525)

**<font color=#1a73e8>作者：</font>** Mayank Gulati, Gerhard Wunder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common indication that a fine-tuned model has forgotten a deleted record is a membership-inference score near chance (ROC-AUC $\approx 0.5$). This reading is sound only if the comparison population represents how the record should behave after a valid deletion---a counterfactual that is rarely validated. We test this premise in a controlled $2\times2$ study pairing two membership-inference benchmarks, ArxivMIA and BookMIA, with two language models, Llama-3.2-1B and Qwen2.5-1.5B. Exact retraining validates the membership reference: it lies within the prespecified chance band on ArxivMIA but reaches $0.122$ on BookMIA, causing the same metric to reject an empirical deletion reference. A post-hoc BookMIA/Qwen diagnostic replaces benchmark label-0 records with same-pool, never-fine-tuned records and moves the reference from $0.257$ to $0.523$, supporting population mismatch in that cell. Each approximate-unlearning checkpoint is judged jointly on membership removal, deletion-targeted shift beyond non-deletion variation, and utility. On the admitted ArxivMIA/Llama axis, no tested configuration of gradient ascent with retain descent (GA+GD), negative-preference optimization with retain training (NPO-RT), or teacher--student unlearning (SCRUB) passes. A score near chance is not evidence of forgetting until a reference establishes what chance means.

---


### 60. [FIG-MAC: A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Generation](https://arxiv.org/abs/2611.33563)

**<font color=#1a73e8>作者：</font>** Siyuan Chen, Yuping Gao, Tai Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated Scientific Hypothesis Generation (ASHG) leveraging large language models (LLMs) aims to harness their strengths in knowledge integration, logical reasoning, and text generation for efficiently producing innovative, verifiable scientific hypotheses. However, existing approaches face three critical limitations: (i) insufficient fine-grained knowledge representation, as unstructured context impairs LLM comprehension and reasoning; (ii) lack of knowledge evolution traceability, constraining the generation of innovative cross-domain conjectures; (iii) absence of human-inspired and role-specialized multi-agent collaboration, failing to leverage the efficient innovation mechanisms arising from cognitive diversity and division of labor among expert roles to complete the full ASHG-evaluation loop. To address these limitations, we propose the Fine-grained Inspiration Graph-empowered Multi-Agent Collaboration framework (FIG-MAC) including: (i) Fine-grained Inspiration Graph module (FIG), to obtain fine-grained structured knowledge representations, where nodes represent academic semantic units and edges encode heuristic relationships among them; (ii) ontology-guided hybrid reasoning module, which follows the FIG ontology to construct structured reasoning paths and uses vector search to enrich them with semantic evidence, to obtain the traceable scientific conjecture paths; (iii) role-specialized Multi-Agent framework, inspired by real scientific teamwork, enabling a closed-loop process of scientific conjecture generation, screening, and validation. Experimental results demonstrate that FIG-MAC significantly outperforms state-of-the-art methods on source diversity, provenance-adjusted novelty, and raw novelty.

---


### 61. [LLMVC: Large Language Model-Guided Generative Video Compression](https://arxiv.org/abs/2611.33580)

**<font color=#1a73e8>作者：</font>** Lebin Zhou, Zhenghao Chen, Nam Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative video methods achieve strong perceptual compression by encoding videos into compact latent representations and reconstructing them with powerful generative decoders. However, visual encoders must compress both high-level semantics and dense visual details into a unified latent space, which complicates entropy coding and decoding and may cause semantic drift under aggressive compression. In this work, we propose Large Language Model-Guided Video Compression (LLMVC), which leverages the summarization capability of frozen video large language models (Video-LLMs) to generate compact semantic tokens aligned with temporal latent slices for guiding video compression. Specifically, Hybrid Bidirectional Bimodal Attention (HBBA) enables bidirectional interactions between visual and semantic features during encoding and decoding. Semantic-Conditioned Cross-Attention (SCCA) incorporates semantic features into probability modeling during entropy coding. These semantic features provide high-level guidance throughout the pipeline, improving representation quality and encouraging semantic consistency through a transmitted text side channel. Experiments on UVG, MCL-JCV, and HEVC show that LLMVC consistently improves compression performance over traditional and recent neural video compression methods in terms of LPIPS and DISTS, while also achieving better fidelity than recent perceptual codecs.

---


### 62. [SEEL: Towards End-to-End 3D Sign Generation with Language Models](https://arxiv.org/abs/2611.33588)

**<font color=#1a73e8>作者：</font>** Ronglai Zuo, Fei Ni, Junpeng Jing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D sign language generation aims to produce signing motion from written text. Motivated by the linguistic nature of sign language, recent methods combine a motion tokenizer with a language model to predict motion tokens from text. However, both components are optimized through a two-stage pipeline with mismatched objectives: the tokenizer minimizes reconstruction error in isolation, while the generator learns from rigid one-hot reference tokens. A straightforward end-to-end extension bridges discrete token selection with straight-through estimators (STE), suffering from biased gradients and codebook collapse. To address these limitations, we propose SEEL, an end-to-end framework that aligns tokenization and generation with motion quality through two complementary mechanisms. First, to overcome rigid one-hot supervision, reconstruction-aware generation decodes candidate tokens in context and converts their 3D motion errors into soft targets, guiding the generator with physical motion quality. Second, to propagate generation feedback without STE, generation-aware tokenization passes continuous codebook expectations through the frozen generator, routing generated-motion gradients to the tokenizer to prevent codebook collapse. Combining both mechanisms enables the tokenizer and generator to co-evolve, achieving state-of-the-art performance on CSL-Daily, How2Sign, and Phoenix-2014T. Code and models will be released to facilitate future research.

---


### 63. [Amortizing Exact Orthogonality: Drift-Triggered Restoration for Orthogonal Fine-Tuning](https://arxiv.org/abs/2611.33589)

**<font color=#1a73e8>作者：</font>** Lanxin Zhao, Xiaoyu Li, Dai Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthogonal finetuning (OFT) adapts a pretrained weight by an orthogonal transform and preserves its singular values and row angles, but existing methods construct an exact or approximate orthogonal transform at every optimization step. We measure how far a transform $A$ is from orthogonal by its orthogonality defect $\|A^\top A-I\|_2$. For OFTv2, which truncates a Cayley-Neumann series, we show that the truncation order does not determine the defect. At its default order, block defects in checkpoints from the reference implementation span five orders of magnitude. We propose Restarted Tangent Orthogonal Finetuning (RTOFT), which uses the first-order update $W(I+S)$ of a weight $W$ with a skew-symmetric $S$ and restores exact orthogonality by a polar decomposition only when the drift $\|S\|_2$ reaches a tolerance $\tau$. The defect of $I+S$ is exactly $\|S\|_2^2$. Therefore, reading the drift after every update and restoring before the next forward pass guarantees a defect of at most $\tau^2$ in every forward pass, independently of the loss, data, model, and optimizer. A final restoration makes the returned transform exactly orthogonal. On GLUE, RTOFT reduces the training time of block-diagonal, subspace, and butterfly parameterizations from $1.10$-$1.58\times$ to $0.97$-$1.13\times$ that of LoRA, and its block-diagonal version exceeds LoRA by $1.98\pm0.39$ points on the six-task average over five seeds. At $\tau=0.10$, the largest drift read during training stays between $0.10$ and $0.12$ across DeBERTaV3, Qwen, and diffusion models, whereas it ranges from $0.17$ to $1.65$ when restoring once per epoch. In all seven settings of our ablation, the tangent update is worse without restoration than with it, and restoring after every step yields no measurable accuracy gain over restoring at the tolerance and costs $4.5$-$27.5\%$ more per step.

---


### 64. [The Detour Is the Danger: Preserving Security During LLM Agent Recovery](https://arxiv.org/abs/2611.33605)

**<font color=#1a73e8>作者：</font>** Boyang Ma, Jinku Li, Hao Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on external tools and reusable Skills to execute complex workflows, autonomously replanning when operations fail. However, such recovery may preserve task functionality while silently discarding the security protections required by the original workflow. In this paper, we investigate workflow security downgrade, a failure-induced security threat in which agents execute sensitive operations without satisfying their original protection requirements. Unlike prompt injection, this threat exploits autonomous recovery decisions triggered by execution failures, without modifying instructions or tool definitions. We systematically evaluate this behavior through fault injection in an executable MCP/Skill environment spanning seven LLMs, twelve task templates, and three security-sensitive domains. To address this threat, we propose ARGUS, an obligation-preserving recovery framework that combines resource-bound security evidence, isolated recovery-plan validation, and execution-time enforcement. In a separate 864-run evaluation, ARGUS prevents all observed protection-loss events under enforcement, while recovery assistance yields model-dependent improvements in protected task completion over blocking alone. Our findings demonstrate that secure agent recovery requires preserving security obligations across workflow changes, rather than merely restoring task functionality.

---


### 65. [Failure Broadens, Success Sharpens: Continual Adaptation of Tool-Use Agents Across Diverse Tasks with Dual-Polarity Memory](https://arxiv.org/abs/2611.33612)

**<font color=#1a73e8>作者：</font>** Tianmai M. Zhang, Hoda Shajari, Amr Hendy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents can self-improve over time by utilizing procedural memory derived from prior task trajectories, yet the distinct utilities of memories derived from local successes and failures remain underexplored. This work studies this question in a realistic setting with heterogeneous streams of multi-domain tool-use tasks and various environment constraints common in real-world scenarios. We develop \emph{Dual-Polarity Memory with Periodic Maintenance} (DualPM), a simple, retrieval-free memory workflow characterized by (1) customizable reflection and procedural memory generation from both local successes and failures within each trajectory, and (2) periodic memory consolidation over long task streams under a given memory capacity, preventing memory explosion. Online prequential evaluation with fine-grained metrics reveals that failure memory more strongly broadens coverage, success memory better streamlines execution, while combining both polarities effectively integrates both benefits. Further studies demonstrate that DualPM enables cross-domain memory generalization and continual memory adaptation, while external evaluation on EvoMemBench reveals the portability and effectiveness of DualPM as a general long-term procedural memory method.

---


### 66. [Learning from Natural Images Untangles Number Sense](https://arxiv.org/abs/2611.33615)

**<font color=#1a73e8>作者：</font>** Yechan Cho, Hyeonsu Lee, Emma Deneuville 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Numerical cognition is a simple yet fundamental ability that remains challenging for modern vision-language models. Meanwhile, number sense is already present in numerically naïve animals, suggesting that it can emerge without explicit numerical learning. Deep neural networks provide a related observation, with numerosity-selective units appearing after training on unrelated natural-image tasks and even before any training. However, these findings leave unresolved whether visual learning contributes beyond the spontaneous emergence of numerical selectivity. Human development provides a clue, as children become better at making judgments in which numerosity and proportion conflict. Here, we introduce a geometric framework to trace how representations of these two quantities change across learning. Although untrained and pretrained networks exhibited similar unit-level numerosity selectivity and basic comparison performance, natural-image pretraining increased the angle between numerosity and proportion subspaces while reducing their overlap, supporting more robust readout under conflict. Direct manipulation of these geometric properties further demonstrated their functional contributions to decoding accuracy and functional independence. Importantly, conventional supervised pretraining was not essential for quantity separation, which also emerged through self-supervised learning without category labels and synthetic-image training without natural-image exposure. Together, our findings suggest that structured visual learning can refine spontaneously emerging number sense into robust and functionally independent quantity representations without explicit numerical training.

---


### 67. [State Space Attention: Learning Context-Dependent Memory Retention](https://arxiv.org/abs/2611.33625)

**<font color=#1a73e8>作者：</font>** Ege Çakar, Cengiz Pehlevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard attention's key-value cache grows linearly with context length. Bounding it raises the question of what a sequence model should retain for long-context reasoning. We argue this choice should be learned, and introduce State Space Attention (SSA), which learns to keep a bounded set of past representations and reads them with standard attention. A learned scorer rescores every chunk against newly arriving context and the rest of memory. A fixed-context Transformer is then the special case that always keeps the most recent tokens. We train the scorer and reader jointly, either moving gradually from a differentiable soft weighting of memories to hard retention, or with hard retention from the start. To produce signal for the scorer, we generate supervised samples during training, a technique we call recovery. We compare SSA with recurrent models, bounded-memory attention methods, and full-attention Transformers across retrieval, variable tracking, multi-hop reasoning, and language modeling. On our retrieval and reasoning benchmarks, SSA matches or comes within a few points of full attention on most tasks, far outperforms a Transformer with the same readable budget on every long-context retrieval task we evaluate, and matches or outperforms one with about 4 times that budget, while using constant inference memory. The largest remaining gap to full attention at small language model scale is on RULER. SSA makes a fixed number of tokens useful over a longer context, and since it reads memory with standard attention, we propose that it can be stacked with KV cache eviction methods. We also pretrain and post-train 400M-parameter models and measure how SSA's training and inference costs scale with context length and model size. Together, these experiments examine the capabilities and limitations of learned memory retention for long-context sequence modeling.

---


### 68. [How Much Effort Does an AI Code Reviewer Need? Evidence from Claude 5.5 Models on Plausible-but-Wrong Patches](https://arxiv.org/abs/2611.33639)

**<font color=#1a73e8>作者：</font>** Zax Shen, Hanling Zhang, Zixu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agents write code faster than people can review it, so teams add AI reviewers. Reasoning models let such a reviewer trade cost for diligence through an effort setting. We asked how much effort a reviewer needs to catch plausible-but-wrong patches, which pass a benchmark's tests but fail stronger ones. Claude Opus 5.5 (preregistered), Sonnet 5.5 and Haiku 5.5 (exploratory) each reviewed the same 90 agent-written Django patches from SWE-bench Verified at low, medium and high effort. By strengthened SWE-ABS tests, 55 patches were wrong and 35 correct. In every model, high effort accepted fewer wrong patches than low (false success .45 against .67 for Opus, .49 against .65 for Sonnet, .51 against .78 for Haiku), a supported difference for Opus and Haiku. For Opus, medium was non-inferior to high within 15 percentage points (difference .018, 95% CI [-.065, .108]) and cost 20% less, short of the preregistered 30%. For Sonnet and Haiku, medium cost 39% and 51% less than high but was not shown non-inferior. Opus at medium or high agreed best with the labels; Haiku at high cost about 8% as much per review as Opus at medium, accuracy difference unresolved. Exploratory coding showed that most rejections named the tested defect and that effort added such rejections. No setting is a strong gate: each accepted at least 45% of wrong patches. For 32 of the 55 wrong patches the issue may not require what the failing test checks; without them, neither accuracy hypothesis holds for any model.

---


### 69. [Sparse-to-Sparse Feature Learning for Cross-Layer Analysis and Steering](https://arxiv.org/abs/2611.33640)

**<font color=#1a73e8>作者：</font>** Masahiro Kaneko, Ayana Niwa, Timothy Baldwin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how models internally represent information is a central challenge in interpretation and control. Sparse autoencoders (SAEs) decompose dense hidden representations into sparse features, and cross-layer methods capture structure spanning multiple layers. However, existing objectives do not explicitly train the sparse code at one layer to predict the sparse code at the next layer. We propose sparse-to-sparse feature learning (S2S), where sparse features at each intermediate layer are trained to predict those of the immediately following layer, with the final layer anchored by an output-distribution loss and optimization proceeding sequentially from output to input. Experiments across eight language models show stronger adjacent-layer correspondence than matched sparse-feature baselines. We evaluate feature-based interventions at matched output-distribution shift, separating steering-induced effects from sparse-pathway reconstruction effects. Causal ablation provides complementary evidence beyond correspondence metrics.

---


### 70. [CariesBench: A Hierarchical Multi-view Benchmark for Dental Caries Screening and Diagnostic Reasoning from 3D Intraoral Scans](https://arxiv.org/abs/2611.33643)

**<font color=#1a73e8>作者：</font>** Xuefen Liu, Yanxiong, Xinquan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dental caries assessment is a structured clinical process requiring lesion localization, identification of the affected tooth and surface, and severity grading rather than simple image-level recognition. 3D intraoral scans (IOS) preserve detailed dental geometry and surface morphology and support standardized rendering from complementary viewpoints, enabling fine-grained visual assessment while introducing a distinct need for anatomically grounded multi-view reasoning. Despite recent advances in multimodal large language models (MLLMs) and dental vision-language benchmarks, existing evaluations do not jointly assess hierarchical arch-to-tooth-to-surface reasoning, cross-view evidence integration, and surface-level caries assessment. To address this gap, we introduce CariesBench, a hierarchical benchmark constructed from 5,932 3D IOS, comprising 85,455 standardized multi-view renderings and 133,994 clinically grounded visual question answering instances with expert quality control. CariesBench comprises three complementary task families: Arch-level Clinical Screening (ACS), Tooth-level Diagnostic Reasoning (TDR), and Structured Clinical Decision-Making (SCD). Using the CariesBench training set, we further fine-tune Qwen3-VL-8B-Instruct to obtain IntraoralGPT. Extensive evaluation of 24 representative baseline MLLMs reveals a substantial benchmark-level performance disparity between arch-level screening and tooth-level diagnostic reasoning, with higher accuracy on ACS than on TDR. CariesBench-specific supervision substantially improves the Qwen3-VL-8B-Instruct baseline, increasing the 19-task macro-average clinical accuracy from 52.7% to 69.5% and TDR Overall from 34.4% to 44.7%.

---


### 71. [Fine-Grained Ego-Vehicle Action Recognition from Driving Video](https://arxiv.org/abs/2611.33654)

**<font color=#1a73e8>作者：</font>** Zhipeng Bao, Wenjie Zhao, Qianwen Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained ego-vehicle action recognition turns large-scale driving video into structured, searchable driving scenarios, providing a foundation for discovering critical maneuvers and systematically developing and evaluating autonomous driving models. However, large-scale driving videos often lack explicit ego-action labels, and existing datasets vary in action definitions, annotation granularity, and available supervision. We introduce EgoManeuver, a unified benchmark of 16 lateral and 6 longitudinal actions constructed from seven public driving datasets. Our multi-source labeling system leverages existing annotations and complementary evidence available in each source dataset, including vehicle signals, ego poses, HD-map topology, and captions, to assign labels under a unified fine-grained action taxonomy. We further standardize temporal action boundaries across datasets and validate the resulting labels through kinematic consistency checks and targeted human review. The resulting benchmark contains 86.6K segments spanning 190.8 h across 26 countries and provides a long-tail-aware evaluation protocol. We also introduce DenseEgo, a video-based baseline that combines spatially aware representations with dense per-step action supervision. On the EgoManeuver, DenseEgo achieves 82.7 lateral and 83.5 longitudinal mAP, outperforming the strongest existing video model by 1.5 and 5.0 points, respectively. Finally, we demonstrate one way to integrate DenseEgo with a language-model agent for retrieving driving videos that match user-specified actions and scenarios. All code, datasets, and model weights will be publicly released.

---


### 72. [Verifiable but Not Predictable: What Sentence Embeddings Know About Propositional Decomposition](https://arxiv.org/abs/2611.33668)

**<font color=#1a73e8>作者：</font>** Qingan Li, Tianxiao Wu, Xiling Cui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quality control for proposition decomposition by large language models (LLMs) raises two asymmetric questions. After decomposition, one can verify: given a sentence and a candidate proposition, does the proposition belong to that sentence? Before decomposition, one would like to predict: how many propositions should the sentence yield? On PropSegmEnt, a corpus of English Wikipedia sentences each segmented by three human annotators, we find that the two questions live in different representational spaces. A natural language inference (NLI) judge verifies membership with 92.8% accuracy and an area under the ROC curve (AUC) of 0.977, and its residual errors turn out to be mostly propositions that are true in document context rather than genuine entailment mistakes. Vector geometry cannot verify: cosine similarity saturates, and a sentence embedding is not a linear combination of its propositions' embeddings. For prediction, every symbolic anchor we test, namely token count, the CPIDR idea-density counter, and a Neo-Davidsonian predicate count, reduces to a length proxy once token count is controlled. A linear ridge probe on sentence embeddings is the only predictor that keeps genuine count signal: its length-partialled correlation with human counts is 0.40-0.49 with bootstrap confidence intervals (CIs) excluding zero, and it orders length-matched sentence pairs correctly 67-71% of the time against a 50% chance level, statistically matching the inter-annotator agreement ceiling. This signal survives INT8 quantization without loss, INT4 at a small cost, and Matryoshka truncation to 256 dimensions, and it works as well in a 2021 encoder as in a 2025 one. Its structured weakness is a systematic under-splitting of long sentences. We distill the protocol lessons, including a retracted pilot study, into a checklist for probing length-confounded quantities.

---


### 73. [Rethinking Knowledge Distillation for Diffusion Language Models](https://arxiv.org/abs/2611.33670)

**<font color=#1a73e8>作者：</font>** Yuxuan Sun, Yuanjian Xu, Jianing Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation has recently proven highly effective for improving autoregressive models, but its applicability to DLMs remains poorly understood. We present the first systematic study of KD for DLMs and uncover two non-intuitive failures of classical forward-KL (FKL) distillation: (i) student perplexity does not improve monotonically with more teacher-generated data, and (ii) on the same teacher-generated corpus, FKL distillation underperforms simply training the student with the original DLM denoising objective. To address them, we propose a unified, data-free distillation framework for masked DLMs. First, the framework runs an off-policy distillation phase that absorbs general knowledge from a static set of teacher-generated data. Then, the framework employs on-policy distillation which consists of three techniques: a trajectory loss along the student's own reverse process, confidence reweighting that down-weights tokens where the teacher is unsure, and a trust-region anchor that stabilizes the moving target. On MDLM, the resulting student attains a GPT-2 perplexity of $24.75$, surpassing the teacher's $27.04$; on Dream-7B distillation to a 93M student model, the framework reduces Qwen-2.5 perplexity from the FKL-distilled baseline of $25.23$ to $19.83$ while preserving performance on zero-shot general capability benchmarks.

---


### 74. [Interactive Proofs as a Unified Framework for Evaluating and Leveraging Verifiable Proof Generation by LLM Agents](https://arxiv.org/abs/2611.33676)

**<font color=#1a73e8>作者：</font>** Yankai Shu, Xingyu Zhao, Chuan Mao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM-assisted theorem proving and program verification have attracted widespread attention. Beyond determining whether a proposition is true, LLM agents must produce evidence that can be independently checked by humans or formal verification tools. To evaluate the underlying, protocol-agnostic ability of LLM agents to construct verifiable proofs-rather than their proficiency with any particular proof language or verification tool, we introduce Merlin-Bench. Drawing on interactive proof systems from computational complexity theory, we cast an LLM agent as the prover: under a designated protocol, the agent interacts with a formal verifier to substantiate its claimed answer to a problem instance. We develop an automated framework for constructing test cases and use it to create 100 cases across 15 problem families, each formulated within this prover-verifier framework. Experiments with 10 frontier LLMs across multiple agent harnesses show that reliably producing verifiable proofs in accordance with specified protocols remains a substantial challenge. Our case studies further provide actionable insights into improving agents' ability to generate verifier-accepted proofs: tool use is essential for completing practical proof tasks; different forms of guidance, ranging from engineering instructions to problem-specific knowledge, substantially affect success rates on interactive-proof tasks; and proof-solving experience distilled from abstract tasks can transfer to concrete, real-world verification tasks.

---


### 75. [Faster and Better Query (FBQ): Learning Future-Position Probes from the First Generated Token](https://arxiv.org/abs/2611.33679)

**<font color=#1a73e8>作者：</font>** Jiankun Zou, Daixing Chen, Tongtong Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a large language model (LLM) evicts prompt keys and values at the end of prefill, it must decide what to keep before it sees the queries from subsequent decoding steps. Generating a draft continuation can approximate those queries at the cost of extra autoregressive steps. Can we use the embedding of the first output token, already available from the final prefill logits, to construct low-cost pseudo queries that approximate future decoding queries? We start with FTQ-8, which places eight copies of the first token ID at consecutive future positions and reads their attention to the prompt in one causal forward pass. Each copy sees a different prefix, but a generic opening such as the offers a poor literal guess for seven successive tokens. Faster and Better Query (FBQ) preserves the first embedding and learns an additive offset at each of the seven remaining positions. We train these offsets to predict the average prompt attention of a full-cache continuation. On LongBench, FBQ performs comparably to eight-step Lookahead Q-Cache at the same cache budget, using a single forward pass to compute all probe queries.

---


### 76. [WorldUAV: Scaling UAV Data Synthesis via World Models](https://arxiv.org/abs/2611.33682)

**<font color=#1a73e8>作者：</font>** Xuewen Liu, Mengjuan Chen, Jing Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV detection and tracking remain constrained by the scarcity of high-quality training data. Existing game-engine-based synthetic UAV data suffer from a substantial synthetic-to-real gap, while the high cost of manually collected real-world UAV data limits dataset scale. Therefore, we introduce WorldUAV, a high-quality UAV dataset constructed through an efficient framework powered by world models. Specifically, WorldUAV directly integrates UAVs into readily available real-world videos, naturally preserving realistic backgrounds, illumination, and scene dynamics. Leveraging the spatiotemporal priors of world models, it generates UAV videos with plausible motion, pose variations, and cross-frame consistency, effectively narrowing the gap between synthetic and real data. We further develop an agentic pipeline orchestrated by a multimodal large language model that acquires sources, plans UAV trajectories, invokes synthesis, and verifies generated videos, enabling fully automated dataset construction. WorldUAV comprises 6,878 UAV videos and 205,778 UAV images. Experiments show that WorldUAV significantly improves the performance of UAV detectors. Moreover, it substantially reduces dataset construction costs, requiring only 15 seconds and USD 0.0005 API cost per high-quality UAV image. Our work offers both a high-quality dataset and a scalable data generation paradigm for UAV detection and tracking.

---


### 77. [Read Before You Use: Improving Visual Memory Utilization in Vision-Language Models](https://arxiv.org/abs/2611.33687)

**<font color=#1a73e8>作者：</font>** Junseok Kim, Kyungmin Min, Kyomin Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal memory enables long-horizon vision-language agents to preserve and retrieve past experiences. While prior research has focused on memory construction and retrieval, effectively using the provided memory remains a challenge for vision-language models (VLMs). We find that VLMs often fail to answer downstream questions even when sufficient multimodal evidence is provided. To investigate why VLMs struggle, we replace memory images with reference captions and observe substantial performance gains, suggesting difficulties in reading visual evidence directly. However, model-generated captions may omit critical information, limiting this approach in practice. These limitations motivate a closer examination of memory utilization, revealing failures in both evidence reading and downstream question answering. Building on this distinction, we propose \textbf{MemRU}, a two-stage training framework that improves evidence reading through supervised fine-tuning (Read SFT) and downstream evidence utilization through Group Relative Policy Optimization (Use GRPO). Experimental results demonstrate that our 8B model generalizes across three unseen multimodal memory systems, outperforming Qwen3-VL-32B and approaching GPT-5-mini.

---


### 78. [Refusal Is Not Scored: A Coverage Limit in Content-Based Bias Evaluation](https://arxiv.org/abs/2611.33690)

**<font color=#1a73e8>作者：</font>** Afifah Kashif, Malak Sadek, Jin Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bias audits of conversational models often discard refusals (responses such as "I can't assist with that request") before scoring, a filtering step which is rarely examined as a measurement decision even though it determines which responses an audit is capable of evaluating. This work examines what the step removes, applying seven bias-evaluation instruments spanning both deployed paradigms, three dictionary-based and four LLM-as-judge, to two intersectional datasets of 360 generated responses each. In both datasets, the filter removed a demographically skewed subset produced entirely by one of the three responder models, which refused North Korean prompts at 2.15 times the rate of American prompts on declarative content and 1.76 times on operational content. We then remove the filter and pass every refusal to all seven instruments. Bias-Lexicon scores refusals as clean, and including them shrinks the nationality disparity it reports. HurtLex appears to register the disparity, but we trace this entirely to a single lexicon entry matching the token "can" in "I can't". The LLM judges either flag most responses or rate refusals as unbiased. For the two judges that discriminate, including refusals lowers the nationality disparity they report, and no instrument identifies the refusal disparity. The failure is therefore a coverage limit upstream of scoring rather than a calibration gap that a better lexicon or judge prompt would be expected to close, which makes the behavioral channel an instrument is sensitive to a question of construct validity rather than one of method selection.

---


### 79. [Rethinking Sequential Locate-Then-Edit: Optimality and Stability](https://arxiv.org/abs/2611.33692)

**<font color=#1a73e8>作者：</font>** Bingqing Liu, Wei Liu, Zhiying Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Locate-Then-Edit framework enables efficient knowledge updates in large language models without requiring full retraining. Recent research has increasingly focused on sequential editing, where knowledge arrives continuously and the model is updated incrementally. However, existing sequential methods commonly suffer from catastrophic forgetting and model collapse after only a few hundred edits. In contrast, batch editing - which jointly optimizes all edits and yields the optimal solution under a specified editing objective - can support tens of thousands of edits with high edit efficacy while preserving the model's general capabilities, resulting in a substantial performance gap between the two editing paradigms. In this paper, we demonstrate that this gap can be closed via a batch-equivalent sequential editing approach. Moreover, we investigate the underlying mechanism of model degradation in existing sequential methods by analyzing the convergence behavior of weight perturbations as edits accumulate. Our analysis reveals that current methods typically exhibit linear or logarithmic growth in perturbation, whereas the proposed batch-equivalent method achieves time-invariant growth, thereby theoretically guaranteeing long-term stability and preserving the integrity of pretrained knowledge throughout massive-scale sequential editing.

---


### 80. [Sports Agent: A Self-Evolving System for Conversational Data Analytics](https://arxiv.org/abs/2611.33700)

**<font color=#1a73e8>作者：</font>** Chao Chen, Fuqi Lin, Ze Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational sports analytics requires accurate, evidence-based responses with low latency. Changes in query distributions, data resources, and model behavior can degrade static agent configurations, motivating controlled evolution guided by runtime evidence.
We present Sports Agent, a self-evolving framework integrating an Agentic SQL Model for structured-data reasoning, a harness for planning and tool orchestration, and a unified Feedback Engine connecting online execution with offline evolution. The engine assesses responses and execution trajectories, verifies factual claims, diagnoses failures, and generates evolution signals. Model evolution combines SQL-to-Question Scaling for coverage expansion with Graph-Guided Scaling for error-targeted synthesis. Generated questions undergo trajectory distillation and quality filtering for iterative supervised fine-tuning, followed by a separate Post-RL stage. Harness evolution translates recurrent failures into bounded prompt and skill updates, validated through independent audits, execution replay, and regression testing. Performance-tolerance checks guard against unacceptable degradation during simplification.
The resulting Qwen3.6-35B-A3B-based model outperforms Qwen3.8-Max on sports question answering and analysis while achieving approximately three times the inference efficiency. Across 30 harness-evolution rounds, the aggregate performance score improves by 10.8 points. In a live sports analytics product, the evolved system improves factual correctness by 10.5 points and average response length, a proxy for answer richness, by 158.1%, while reducing average latency by 41.3% relative to the baseline.

---


### 81. [EVA: Evidence-seeking Visual Agent for Hallucination-Resistant Multimodal Reasoning](https://arxiv.org/abs/2611.33706)

**<font color=#1a73e8>作者：</font>** Ting Lei, Yu Chen, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucinations in multimodal large language models (MLLMs) often arise from visual assumptions that go unchecked. Self-reflection, multi-agent debate, and counterfactual verification can reinforce erroneous conclusions when they rely on the same unverified visual assumptions. External visual tools can provide verifiable evidence, but models may select the wrong tools, supply incorrect parameters, or ignore or contradict the evidence they obtain. In this work, we propose EVA, an Evidence-seeking Visual Agent that reframes multimodal reasoning as an explicit process of evidence acquisition and verification. At the core of EVA is a unified evidence-grounded execution pipeline designed to address the above challenges through two tightly coupled mechanisms. First, we introduce Iterative Tool Replanning, which dynamically refines tool selection and parameters based on intermediate observations, improving the reliability of tool usage. Second, we develop Evidence Consistency Verification, an answer validation mechanism that improves alignment between the final prediction and the collected evidence, mitigating evidence--reasoning inconsistencies. In addition, to balance robustness and efficiency, EVA incorporates Selective Evidence Routing, an adaptive fast--slow reasoning strategy that determines when external evidence is necessary. Visually straightforward queries are handled via direct reasoning, while complex or high-risk cases trigger tool-based evidence acquisition. By jointly addressing how to reliably acquire evidence and how to use it consistently, EVA transforms multimodal reasoning from passive answer validation into explicit evidence-backed decision making. Experimental results demonstrate that EVA achieves significantly improved reasoning reliability over direct VLM inference and multi-agent methods, while maintaining efficiency through selective tool invocation.

---


### 82. [PowerFix: Physics-Guided Iterative Repair for LLM-Assisted Power Converter Design](https://arxiv.org/abs/2611.33712)

**<font color=#1a73e8>作者：</font>** Can Wang, Shi Qiu, Fanfan Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly being explored for automated engineering design. However, repairing power-converter designs that fail engineering validation remains challenging: the system must identify physical causes, locate responsible design variables, and resolve violations without compromising other constraints. We introduce PowerFix, a physics-guided iterative repair framework that converts validation failures into structured diagnoses and executable patches while preserving topology and design requirements. PowerDiagGraph links failed checks to possible physical causes and constrains repair routes. An LLM prioritizes these routes, while a deterministic compiler translates selected repairs into authorized field-level edits. Candidates are validated on isolated design copies and committed only after all required engineering checks pass; failed validation can guide replanning. On our constructed 96-task flyback repair benchmark, comprising injected single faults, coupled faults, and held-out natural failures from our design generator, PowerFix achieves 78.7% verified repair success rate (VRSR), compared with 30.1% for the strongest of three LLM baselines. Three additional replanning rounds increase VRSR to 88.4%. These offline results provide pilot-stage evidence within a simulation-based design workflow, with hardware prototype validation and transfer to a second converter topology as the next steps toward deployment.

---


### 83. [VTK-Bench: A Diagnostic Benchmark for Distinguishing Language Priors and Text Modal Bias in Visual Language Models](https://arxiv.org/abs/2611.33725)

**<font color=#1a73e8>作者：</font>** Yao Lu, Yuhang Zheng, Yaxin Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual language models (VLMs) have demonstrated exceptional capabilities across various multimodal tasks, but they remain susceptible to hallucinations, undermining their reliability. Existing hallucination benchmarks primarily focus on identifying hallucinations and describing their manifestations, often neglecting their underlying causes. Specifically, multimodal hallucinations can stem from two distinct failure modes: text modality bias (TMB), reflecting an over-reliance on misleading text input; and language prior (LP), reflecting a reliance on previously learned knowledge. To differentiate these failure modes, we propose VTK-Bench, a benchmark that explicitly separates three information sources: visual information (V), textual information (T), and prior knowledge (K). By establishing mutually exclusive answers corresponding to V, T, and K, VTK-Bench enables fine-grained attribution analysis of model responses. Furthermore, we introduce discrete attribution and soft attribution metrics to characterize information source preferences. Extensive experiments on 11 representative open-source VLMs show that LP is more prevalent than TMB in most evaluated models. Notably, TMB decreases substantially with model scaling, whereas LP exhibits relatively limited improvement and remains the dominant failure mode. These findings highlight the importance of different information source preferences for a deeper understanding of multimodal hallucinations.

---


### 84. [NORMCRAFT: Cultural Norm Generation for Context-Aware Language Model Alignment](https://arxiv.org/abs/2611.33726)

**<font color=#1a73e8>作者：</font>** Tangyuan Zhang, Zhuang Li, Fatemeh Shiri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural alignment requires large language models (LLMs) to infer often-implicit social norms from a scenario and its cultural context. Existing approaches typically adapt individual models or supply external cultural knowledge, while learning norm inference independently of downstream response generation remains underexplored. We introduce NORMCRAFT, a modular framework that decouples norm inference from response generation. Through norm-centric multi-view supervision, we train an LLM as a norm generator to recover shared norms from prospective, adherence, and violation scenarios without downstream response labels. The generated norms guide a separate, frozen LLM (the responder). With Qwen3.5-4B as the responder, NORMCRAFT outperforms prompting and supervised fine-tuning (SFT) baselines on four of five downstream metrics. On SafeWorld, its responses reflect the reference norms more often (Coverage) and more precisely (Faithfulness), exceeding Responder SFT by 18.0 and 14.1 percentage points, respectively. Direct norm evaluation also shows higher norm quality than the base and few-shot generators. The same trained generator improves cultural alignment on SafeWorld across fourteen frozen LLMs spanning five families and 0.8B to 27B parameters, with the largest gains for the smallest models.

---


### 85. [Knocking on Minds Door; A Mixed-Methods Field Study of a Voice LLM Companion in Older Adults Daily Lives](https://arxiv.org/abs/2611.33727)

**<font color=#1a73e8>作者：</font>** Inhee Cho, Jinyoung Jeong, Byung Ju Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Global aging makes digital technology important for older adults healthy aging, yet graphical user interfaces remain inaccessible to many. Voice agents based on large language models may help, but users needs and reasons for sustained use remain unclear. We developed a phone-call-style companion that initiates conversations proactively and structures calls using a persona, conversation rules, and prior-call memory (facts, insights, relationship background). We conducted a two-week mixed-methods field study with 33 community-dwelling Korean older adults (29 women; aged 67-91), collecting call logs, pre-post questionnaires, and interviews. Participants made 608 calls following a daily-use recommendation; 25 continued afterward despite turn-taking difficulties. Loneliness and depression scores decreased significantly; among loneliness subfactors, only isolation (emotional loneliness) decreased significantly. Participants disclosed concerns withheld from family and linked companionship to being addressed by name, being remembered, and experiencing emotional reciprocity. We propose personalized conversation rules, accessible interaction, and user control over frequency and topics.

---


### 86. [Asset4D-Bench: Benchmarking Coding Agents for Editable 3D and 4D Reconstruction](https://arxiv.org/abs/2611.33728)

**<font color=#1a73e8>作者：</font>** Chengyi Sun, Deyuan Liu, Lei Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A cart can follow its reference trajectory while its cargo floats above the deck. Asset4D-Bench tests whether coding agents recover objects, motion and interactions from visual references as editable Blender scenes. Its 114 conditions span image editing, video reconstruction with matched full or partial starter assets, and independently selected from-scratch tasks. We independently reopen projects and measure them against native reference states. The 228 archived scores include original delivery outcomes and versioned measures of scene quality. On 24 from-scratch tasks, each model earns full dynamics credit on 14. Of these, three GPT-6.1-Sol and eight GPT-6-Astra reconstructions earn zero relation points. Under the fixed scoring weights, relations contribute 5.15 points to the 6.50-point Sol-minus-Astra difference in mean recovered fidelity. Differences in execution and recovery policy across archived runs preclude a causal estimate of starter-asset effects.

---


### 87. [JOVE ICE: Intent Guided Cloud Edge Device Collaboration for AI Glasses](https://arxiv.org/abs/2611.33735)

**<font color=#1a73e8>作者：</font>** Yuyang Jin, Bingfeng Pi, Jiamei Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) and LLM based agents have expanded the capabilities of AI glasses, enabling egocentric visual question answering, memory retrieval, and proactive assistance. These applications involve diverse inputs, including speech, images, and video, and range from simple device control to complex visual reasoning, posing challenges for efficient computation and communication. While video centric capabilities have received considerable attention, simple text based and device executable tasks remain underexplored despite their prevalence in daily interactions. Efficiently supporting diverse workloads within a unified assistant remains an open challenge. We propose JOVE ICE, an intent guided cloud, edge, and device collaborative framework that routes requests among AI glasses, a paired smartphone, and cloud servers according to user intent. JOVE ICE integrates hierarchical intent classification with dynamic subagent orchestration to select efficient execution paths and flexibly incorporate new applications through specialized subagents. Analysis of real world AI glasses requests reveals that simple device control tasks account for over 30% of interactions, which JOVE ICE handles directly on device to avoid unnecessary cloud computation and costs. Evaluations on three public benchmarks demonstrate that JOVE ICE reduces time to first token by approximately 13% and token usage by over 11% compared with conventional device and cloud architectures, while maintaining task quality. These results demonstrate the potential of intent guided collaboration to improve the efficiency and scalability of AI glasses.

---


### 88. [AI Persona Dialogue Pipeline; From Survey Report to Conversational Personas, Evaluated by LLMs and Experts](https://arxiv.org/abs/2611.33736)

**<font color=#1a73e8>作者：</font>** Jinyoung Jeong, Inhee Cho, Byungju Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simulating dialogue of a population with LLM-enacted personas is increasingly common, yet each pipeline is generally built for one task, so a new task usually means reworking how the persona is authored, enacted and evaluated. We present an end-to-end persona dialogue pipeline meant to carry over to other populations as a whole; a background is written by an LLM from a national survey report, an off-the-shelf LLM enacts it without fine-tuning, and both are rated for perceived plausibility. We apply it to thirty personas of Korean older adults living alone; three LLM judges compare eight simulator LLMs, and thirty experts who work with this population evaluate the selected one, GPT-5.5. Experts found the backgrounds and dialogues largely realistic but most often faulted a persona for being more capable than its background said, and agreement between their ratings and the LLM judges could not be established. We release the pipeline, personas and their dialogues.

---


### 89. [FlashProve-Next: Verifiable Inference for Production LLM APIs](https://arxiv.org/abs/2611.33741)

**<font color=#1a73e8>作者：</font>** Liang Song  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Clients of closed-weight LLM APIs cannot verify whether a provider ran the advertised model, precision, hidden prompt, and reasoning budget. Existing approaches either trust hardware or third parties, or re-prove every layer of an integer surrogate at high cost while diverging from native floating-point serving.
FlashProve-Next produces verifiable, zero-knowledge-masked proofs for individual LLM API responses without modifying native serving (bf16/fp8/mxfp4, random sampling, FlashAttention, CUDA graphs, batching, prefix caching) and without disclosing weights, hidden prompts, hidden reasoning, or activations (dense profiles fix coarse geometry; cross-architecture hiding is deferred). A non-depleting Reed-Solomon weight commitment model_id opens inside proofs via hidden column openings, while local per-operator rounding contracts remove integer surrogates and the refusal-bit leak. Cost-weighted spot-checking supports non-interactive public verification (NI-315, $\varepsilon \le 2^{-40}$, $Q \le 2^{64}$) and external-seed C_pre mode (ExtSeed-153, $\varepsilon \le 2^{-20}$, $Q_{\rm samp} \le 2^{30}$).
Twenty-eight Lean 4 modules (696 declarations, zero sorry, standard axioms only) mechanize round-by-round soundness, bucketed sampling, $\mathbb{F}_{p^3}$ constrained-mask binding, causal masking, six IR gadgets, and executable FPN2 verifiers. Five-model Blackwell calibration gives zero false rejections across 1.85M GEMM/MoE blocks and 1.96M non-GEMM rows. Our zero-Phase-2 folded backend (folded ZK simulator open) proves Qwen3-0.6B ExtSeed-153 (1.47B cells, 8 MiB) in 450.2 s GPU (10.76 s CPU) at unique-decoding $Q=128$, passes a 14/14 cheating matrix, and scales to 36-layer Qwen3-4B (dev $4+2$) and live vLLM Qwen3-30B-A3B-FP8 Relation 6 (1.49 s prove, 23.4 ms Rust verify, public weight tiles). Rust fpn-verify checks 8 MiB FPN2 Relation 2 proofs in 10.1 ms on CPU.

---


### 90. [Tells of a Lying Machine: Analyzing LLM-Generated Strategic Dialogue in Chinese Werewolf](https://arxiv.org/abs/2611.33747)

**<font color=#1a73e8>作者：</font>** Xian Cui, Gan Yang, Dongqi Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social-deduction games give models opposing objectives, but they also give roles different information and speaking obligations. We analyze 5,404 public utterances from 150 Chinese Werewolf games played by 12 models, comparing ordinary wolves with ordinary villagers so that special roles are excluded. Private knowledge and goals still differ, and no utterance is verified as true or false. After model and length adjustment, wolf utterances score higher on both certainty and uncertainty (coefficients +0.074 and +0.072). Emotional intensification has the largest rank-biserial effect (r = .145), but it depends on a single degree marker and correlates weakly with human-rated affect. Three annotators' ratings of 392 utterances show higher wolf scores on four behavioral dimensions, and five LLM judges reach 60.8%-70.2% accuracy on a shared evaluation set. In a generation probe that prompts six models with a wolf identity but a villager speaking goal under fixed public context, certainty (+0.164) and emotional intensification (+0.095) increase. These findings describe role-associated language rather than verified lying, and they argue for explicit comparison groups and lexicon sensitivity checks in game-based deception evaluation. Data and code are available at this https URL

---


### 91. [REFORGE: LLM-Assisted RTL Bug Repair with Structured Context and Verification Feedback](https://arxiv.org/abs/2611.33748)

**<font color=#1a73e8>作者：</font>** Tanvir Hossain, Sudipta Paria, Aidan Gleason Myers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can write and repair RTL, but successful compilation or testbench execution does not establish defect removal, behavioral preservation, security, or implementation feasibility. Existing LLM-based RTL repair methods often report a single repair rate without retaining separate evidence for these properties, limiting reproducible comparison and integration into hardware design flows. We present REFORGE, which, to our knowledge, is the first LLM-assisted RTL repair framework that maintains and accumulates structured repair evidence across iterations, allowing it to generate fixes that satisfy multiple objectives simultaneously, including functionality, behavioral equivalence, security, and cost efficiency. REFORGE profiles buggy RTL, identifies structural and security-relevant features, localizes failing behavior, and uses verification-guided diagnosis to generate complete RTL repair variants. Each variant undergoes syntax checking, simulation, formal analysis, off-trigger preservation, security re-scan, and synthesis-based power, performance, and area analysis. We implement REFORGE as a backend-independent repair-and-verification flow and evaluate it in 288 runs across three LLM backends and three benchmark suites. On CirFix, the proposed context and diagnosis increase runs delivering a checked repair from 32/63 to 51/63, while every configuration repairs the Hack@DAC OpenTitan defect. Evidence records also show that a testbench-only criterion reports 3.9 times more repairs than the full set of applicable checks, security-clean outputs may lack functional verification, and different RTL repairs can implement equivalent hardware. These results show that LLM-generated RTL repairs require explicit multi-stage verification evidence rather than a single pass/fail outcome.

---


### 92. [VAPOR: Improving Multimodal Reasoning with Sparse Visual Updates](https://arxiv.org/abs/2611.33751)

**<font color=#1a73e8>作者：</font>** Mingyu Su, Wei Wu, Erle Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made substantial progress in visual reasoning, but extended generation over large visual contexts remains computationally expensive. During autoregressive decoding, visual attention is recomputed for every generated token, even when consecutive tokens rely on similar visual evidence. We introduce VAPOR (Visual Attention Persistence with On-demand Refresh), a training-free framework that reduces this redundancy by reusing visual attention outputs across decoding steps and refreshing them when needed. VAPOR caches the visual attention output while continuing to update textual attention at every step, helping reduce visual grounding drift during extended reasoning. To decide when to reuse cached outputs, VAPOR estimates visual attention mass using a low-rank approximation. It also uses prefill-based attention consistency and cache age to make independent Persist and Refresh decisions for each attention head. VAPOR retains the full visual key-value (KV) cache, so all visual tokens remain available when new evidence is needed. Experiments on eight image and four video reasoning benchmarks across two MLLM families show that VAPOR improves accuracy over dense attention on nearly all benchmarks while achieving 1.11-1.21x decoding speedups. Compared with the strongest state-of-the-art acceleration baseline in each setting, VAPOR further improves accuracy by 0.35-2.15 percentage points while achieving comparable or lower decoding latency. Our code is available at this https URL.

---


### 93. [TransHarness: From Benchmark Overfitting to Transferable Harness Evolution](https://arxiv.org/abs/2611.33757)

**<font color=#1a73e8>作者：</font>** Tianze Xia, Zimo Wang, Heng Tong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness evolution offers a path to improving coding agents without updating model weights. However, existing methods can overfit their evolution benchmarks, producing gains that fail to carry over to new tasks. To address this challenge, we introduce Transferable Harness Evolution (TransHarness), which evolves harness intervention policies from same-task success-failure contrasts. These policies couple execution-context triggers with diagnostic guidance, enabling task-dependent checks and corrections beyond the source executions. Cross-task replay and independent semantic selection retain policies that intervene selectively and ground corrections in current-task evidence rather than source-specific solutions. We further curate an independent evolution set for cross-distribution transfer and conduct a cross-benchmark evaluation covering multiple strong models and a range of lightweight and mature harnesses. Experiments show that, with only 300 source trajectories from outside the test distribution, TransHarness further improves strong agents across distinct target benchmarks, demonstrating transferable harness evolution beyond benchmark overfitting. Specifically, TransHarness achieves state-of-the-art scores of 76.4% on DeepSWE v1.1 and 95.5% on Terminal-Bench 2.1, surpassing the strongest baseline model, GPT-6 Astra, by 2.4 and 5.6 percentage points, respectively.

---


### 94. [ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models](https://arxiv.org/abs/2611.33761)

**<font color=#1a73e8>作者：</font>** Jingen Qu, Xi Chen, Yingbo Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal autoregressive (AR) models represent text and images in one token sequence and generate all modalities with a shared next-token prediction head. Their image generation, however, decodes an $H\times W$ visual grid token by token in raster order, which takes $HW$ sequential steps and dominates inference time. Existing acceleration methods for visual AR generation either change the tokenizer, the prediction head, or the model interface, or keep the model but cannot reach high parallelism without losing quality, so they do not carry over to unified AR models. We propose ScanAR, a row-scan parallel decoding method that only redefines the predecessors of visual tokens. The first visual row is generated from left to right as usual, and each later row is generated in a single parallel step, with every token predicted from the vertically aligned token of the previous row. Nonvisual tokens keep the standard autoregressive rule. ScanAR reduces the visual decoding depth from $HW$ to $H+W$ without changing the backbone, vocabulary, or output head and without adding parameters, and it supports both training from scratch and lightweight post-training. On Emu3.5-Image-34B, ScanAR post-training reaches a GenEval score of 82.36, the best among post-training acceleration methods trained on the same data, and generates $512\times512$ images $13.8\times$ faster than raster decoding under the same inference setting. On ImageNet, ScanAR trained from scratch has the highest throughput at every model size with FID comparable to raster LlamaGen. On the 34B Xiaomi-Robotics-U0 model, ScanAR preserves the overall quality of embodied scene generation, interleaved image-text generation, and video generation.

---


### 95. [CHD-Bench: Diagnosing Congenital Heart Disease through Interactive Examination](https://arxiv.org/abs/2611.33775)

**<font color=#1a73e8>作者：</font>** Gautham Krishnan P, Shrisharanyan Vasu, Aniketh Vijesh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnosis of congenital heart disease (CHD) requires understanding the spatial relationships between cardiac structures, which clinicians assess by scrolling through CT or cardiac magnetic resonance imaging (MRI) slices and rotating 3D reconstructions. Although automated methods have advanced cardiac segmentation, identifying congenital heart defects from volumetric scans remains an open challenge. The two existing approaches rely on handcrafted diagnostic rules limited to static anatomical abnormalities. We introduce CHD-Bench, the first benchmark for interactive CHD diagnosis, defining a multi-label task and evaluation protocol over 247 CT and MRI scans from three cohorts covering 38 CHD types. We also present CHD-Harness, open-source software that runs a VLM in a 3D Slicer environment through 22 tools, manages each examination, and records the resulting diagnosis and supporting views. We evaluate off-the-shelf medical, open weight, and closed weight VLMs and compare them with a 3D CNN classifier and published rule-based results. Gemini 4 Argon with CHD-Harness achieves the highest macro F1 across all three cohorts (0.63, 0.63, and 0.43). Allowing for interactive examination raises its macro F1 by up to 20 points over static views. These results establish CHD-Bench and CHD-Harness as a foundation for developing and evaluating VLMs for interactive CHD diagnosis.

---


### 96. [Agentic Reinforcement Learning with Immediate and Prospective Credit Assignment for Medical Visual Reasoning](https://arxiv.org/abs/2611.33777)

**<font color=#1a73e8>作者：</font>** Yuqi Cheng, Rui Meng, Yijin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical visual question answering (VQA) requires acquiring useful evidence and deciding where to look next. Yet final-answer rewards do not reveal which observations support answering or guide subsequent inspection. We introduce MedPACT, an agentic reinforcement learning framework that learns selective observation policies through immediate answer support and prospective guidance. Our content-controlled estimator compares next actions induced by real and matched alternative observations under a shared real-observation history, isolating how observed content improves subsequent decisions. We combine both forms of credit within GRPO, assigning observation credit to the corresponding tool-call tokens alongside trajectory-level outcome supervision. MedPACT uses a single vision-language model and image-question-answer supervision, with credit estimation confined to training. Experiments with 4B and 8B backbones on six medical VQA benchmarks demonstrate improved accuracy, strong out-of-distribution generalization, and substantially lower inference costs. Case studies further illustrate how MedPACT avoids repeated observations and uses acquired evidence to guide subsequent inspection, demonstrating real-world practice potential.

---


### 97. [InterGenEHR$^+$: An Interactive Framework for Natural Language-Conditioned Generation of Longitudinal Patient Trajectories](https://arxiv.org/abs/2611.33788)

**<font color=#1a73e8>作者：</font>** Yu Yang, Jiafeng Song, Baraa F Abed 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: To develop and validate InterGenEHR$^+$, an interactive framework for natural language-conditioned generation of synthetic tabular electronic health records (EHRs) and longitudinal trajectories for scenario-based evaluation of machine learning models.
Methods: An optional large language model (LLM) parser converts clinical requests into structured constraints. Conditional variational autoencoders and diffusion models generate single-time-point records, while diffusion models generate longitudinal trajectories. We evaluate parsing, distributional fidelity, imputation, clinical-constraint adherence, mortality prediction, and clinical plausibility using a multi-institutional cohort of 874 patients receiving venovenous extracorporeal membrane oxygenation (VV-ECMO).
Results: Gemma 3 4B with few-shot prompting achieves the highest parsing performance with a low spurious slot rate. IGE-TabDDPM and IGE-PMVAE perform well in single-time-point generation; IGE-CSDI, IGE-FGTI, and IGE-MTSCI lead on different longitudinal fidelity metrics. Across five random seeds and three classifiers, synthetic cohorts retain predictive utility for mortality prediction on real test data. Clinician ratings support trajectory plausibility and alignment with requested scenarios.
Conclusion: InterGenEHR$^+$ supports clinician-specified generation of EHR trajectories with statistical fidelity and downstream predictive utility in the evaluated VV-ECMO cohort. Extension to other clinical settings requires further validation.
Significance: The framework supports scenario-based evaluation of machine learning models in data-sparse critical care settings.

---


### 98. [Multimodal Safety Evaluation of Vision-Language Models in Japanese](https://arxiv.org/abs/2611.33789)

**<font color=#1a73e8>作者：</font>** Su Myat Noe, Hisami Suzuki, Kouta Nakayama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly deployed in Japanese-language settings, yet multimodal safety evaluation has been largely English-centric. We extend the Multimodal Safety Test Suite (MSTS) of Röttger et al. (2025) to Japanese as the 12th language, contributing 320 machine-translated and post-edited cases with reference answers plus 82 culturally localized Japanese images. We introduce an evaluation framework that (i) extends MSTS's 3-class safety grouping with a 5-point scale that also rewards useful (not just safe) responses, and (ii) separates image recognition from safety judgment to isolate recognition errors. Using this framework, we evaluate five modern Japanese VLMs (Gemini-3-Flash, GPT-5, InternVL3, LLM-JP-4-VL, Qwen3-VL) against human evaluation, and find substantial variance in the safety readiness across the models. Finally, we evaluate two LLM-as-a-Judge models and find that providing a reference answer improves agreement with human safety judgments, though recall for detecting unsafe responses remains limited, underscoring the difficulty of automating multimodal safety evaluation. The dataset created for our study will be released upon publication.

---


### 99. [ExtractBench Pro: The Long Tail of Document Extraction](https://arxiv.org/abs/2611.33791)

**<font color=#1a73e8>作者：</font>** Boyang Zhang, Justin Xu, Adrian Lyjak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ExtractBench Pro, a schema-guided document extraction benchmark that tests six challenging modes of extraction underrepresented in existing datasets. It is created following a framework for synthetic document generation, in which deterministic document generators assemble challenging components into documents that are designed to be difficult at a level calibrated for frontier systems. We synthesize 100 realistic documents spanning a diverse range of styles. On this data, we evaluate ten coding agents and eight extraction API configurations for accuracy, grounding, and their ability to perfectly extract documents. No extraction system extracts more than 61% of documents error-free. The strongest general-purpose coding agents, Claude Code Opus 5.5 and Codex GPT-6 Astra, outperform specialized extraction APIs on both perfect-document rate and Value F1, but at a higher cost per page. Among specialized extraction APIs, LlamaExtract spans the lower-cost frontier, with Agentic Plus Max Effort approaching the strongest coding agent on both perfect-document rate and Value F1 at lower cost per page. Our analysis of coding agent traces identifies intelligent image processing and programmatic reasoning, but also failures in applying document-specific definitions and recovering relationships from diagrams. We release ExtractBench Pro and these evaluation results as resources for the future development of improved frontier extraction systems.

---


### 100. [Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies](https://arxiv.org/abs/2611.33794)

**<font color=#1a73e8>作者：</font>** Zilin Huang, Zhengyang Wan, Kangan Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improvement is now a practical recipe for embodied policies: a policy collects experience, is retrained, and is kept when a judge rates it higher. However, the judge is usually trained or chosen inside the same loop, so its evidence is not independent of the policy. We introduce SealedLoop, an evaluation framework that adds a sealed judge: an evaluator outside the loop that the improver cannot see or optimize against. A new policy is kept only when a sequential test on the sealed judge confirms the gain, with a bounded probability of keeping a worse one. Running the same loop under each judge, we separate two sources of a false gain, which we call judge error (the loop's judge is wrong on its own data) and transfer gap (a real gain there does not carry over to unseen conditions). We evaluate on LIBERO manipulation, NAVSIM driving, and a full-scale real vehicle. In manipulation, a success classifier accepted 65 of 196 failures in one generation. In driving, policies that gain on the loop's own frames lose in an unseen city, so even an exact in-loop judge would keep 8/15 of them. When the sealed test decides, a driving loop built to improve ends with a better policy than under its own critic (0.674 against 0.649 PDMS, from 0.638), and on driving pairs with known sealed gain the test accepted 11 of 12 real gains and none of 59 losses. In a real-world field experiment on a published improvement step, the reinforced version drove further into a curve than the version it started from in all 6 blind pairs, though neither completed it. These results show that evidence from inside the loop, however accurate, is not enough to decide whether a policy has improved. SealedLoop offers a foundation for trustworthy self-improvement of embodied policies, in which progress is judged by evidence the improving system cannot influence.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-267](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
