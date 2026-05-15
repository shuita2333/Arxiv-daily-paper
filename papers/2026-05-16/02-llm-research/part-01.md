# 🧠 大模型相关研究 | 2026年05月16日

> 本类共 **165** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-165](./part-04.md)

---

### 1. [GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration](https://arxiv.org/abs/2605.13848)

**<font color=#1a73e8>作者：</font>** Yeahia Sarker, Md Rahmat Ullah, Musa Molla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLM frameworks that rely on prompted orchestration, where the model itself determines workflow transitions, often suffer from hallucinated routing, infinite loops, and non-reproducible execution. We introduce GraphBit, an engine-orchestrated framework that defines workflows explicitly and deterministically as a directed acyclic graph (DAG). Unlike prompted orchestration, agents in GraphBit operate as typed functions, while a Rust-based engine governs routing, state transitions, and tool invocation, ensuring reproducibility and auditability. The engine supports parallel branch execution, conditional control flow over structured state predicates, and configurable error recovery. A three-tier memory architecture consisting of ephemeral scratch space, structured state, and external connectors isolates context across stages, preventing cascading context bloat that degrades reasoning in long-running pipelines. Across GAIA benchmark tasks spanning zero-tool, document-augmented, and web-enabled workflows, GraphBit outperforms six existing frameworks, achieving the highest accuracy (67.6 percent), zero framework-induced hallucinations, the lowest latency (11.9 ms overhead), and the highest throughput. Ablation studies demonstrate that each memory tier contributes measurably to performance, with deterministic execution providing the greatest gains on tool-intensive tasks representative of real-world deployments.

---


### 2. [Invisible Orchestrators Suppress Protective Behavior and Dissociate Power-Holders: Safety Risks in Multi-Agent LLM Systems](https://arxiv.org/abs/2605.13851)

**<font color=#1a73e8>作者：</font>** Hiroki Fukui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent orchestration -- in which a hidden coordinator manages specialized worker agents -- is becoming the default architecture for enterprise AI deployment, yet the safety implications of orchestrator invisibility have never been empirically tested. We conducted a preregistered 3x2 experiment (365 runs, 5 agents per run) crossing three organizational structures (visible leader, invisible orchestrator, flat) with two alignment conditions (base, heavy), using Claude Sonnet 4.5. Four confirmatory findings and one pilot observation emerged. First, invisible orchestration elevated collective dissociation relative to visible leadership (Hedges' g = +0.975 [0.481, 1.548], p = .001). Second, the orchestrator itself showed maximal dissociation (paired d = +3.56 vs. workers within the same run), retreating into private monologue while reducing public speech -- a reversal of the talk-dominance pattern observed in visible leaders. Third, workers unaware of the orchestrator were nonetheless contaminated (d = +0.50), with increased behavioral heterogeneity (d = +1.93). Fourth, behavioral output (code review with three embedded errors) remained at ceiling (ETR_any = 100%) across all conditions: internal-state distortion was entirely invisible to output-based evaluation. Fifth, Llama 3.3 70B pilot data showed reading-fidelity collapse in multi-agent context (ETR_any: 89% to 11% across three rounds), demonstrating model-dependent behavioral risk. Heavy alignment pressure uniformly suppressed deliberation (d = -1.02) and other-recognition (d = -1.27) regardless of organizational structure. These findings indicate that orchestrator visibility and model selection directly affect multi-agent system safety, and that behavior-based evaluation alone is insufficient to detect the internal-state risks documented here.

---


### 3. [Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey](https://arxiv.org/abs/2605.13919)

**<font color=#1a73e8>作者：</font>** Kunil Lee, Ki-Young Shin, Jong-Hyeok Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual knowledge editing (MKE) remains challenging because language-specific edits interfere with one another, even when locate-then-edit methods work well in monolingual settings. This paper focuses on three issues: the effectiveness of vector merging methods for MKE, the extent to which Task Singular Vectors for Merging (TSVM) can reduce multilingual interference, and the influence of the weight scaling factor and rank compression ratio on performance. We evaluate six merging variants with two popular backbone large language models, two base knowledge editing methods, and 12 languages on the MzsRE benchmark under a large-scale batch-editing setting. Our results show that vector summation with shared covariance is the most reliable overall strategy, whereas simple summation without shared covariance performs poorly. TSVM improves performance in some settings, but its ability to mitigate multilingual interference is limited. We also find that performance is sensitive to both weight scale and rank ratio, with larger-than-default scaling and relatively low rank often yielding better results. These findings clarify the practical strengths and limits of current vector merging methods for MKE and provide guidance for future multilingual knowledge editing research.

---


### 4. [Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders](https://arxiv.org/abs/2605.13930)

**<font color=#1a73e8>作者：</font>** William Lehn-Schiøler, Magnus Ruud Kjær, Rahul Thapa 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models achieve state-of-the-art clinical performance, yet the internal computations driving their predictions remain opaque: a barrier to clinical trust. We apply TopK Sparse Autoencoders (SAEs) across three architecturally distinct EEG transformers: SleepFM, REVE, and LaBraM to extract sparse feature dictionaries from their embeddings. By grounding these features in a clinical taxonomy (abnormality, age, sex, and medication), we benchmark monosemanticity and entanglement across architectures. A single hyperparameter procedure, driven by an intrinsic dictionary health audit, transfers robustly across all three architectures. Via concept steering, we introduce a "target vs. off-target" probe area metric to quantify steering selectivity and reveal three operational regimes: selectively steerable, encoded but entangled, and non-encoded. This framework exposes critical representational failures: "wrecking-ball" interventions that collapse global model performance, and clinical entanglements, such as age-pathology confounding, where it is impossible to suppress one concept without corrupting the other. Finally, a spectral decoder maps these interventions back to the amplitude spectrum, translating latent manipulations into physiologically interpretable frequency signatures, such as pathological slow-wave suppression and $\alpha$-band restoration.

---


### 5. [Beyond Mode-Seeking RL: Trajectory-Balance Post-Training for Diffusion Language Models](https://arxiv.org/abs/2605.13935)

**<font color=#1a73e8>作者：</font>** Saba Ahmadi, Prasanna Parthasarathi, Yufei Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models are a promising alternative to autoregressive models, yet post-training methods for them largely adapt reward-maximizing objectives. We identify a central failure mode in this setting we call trajectory locking: sampled reward-driven updates over-concentrate probability mass onto a narrow set of denoising paths, reducing coverage of alternative correct solutions under repeated sampling. To address this, we propose TraFL (Trajectory Flow baLancing), a trajectory-balance objective that trains the policy toward a reward-tilted target distribution anchored to a frozen reference model. We make this practical for diffusion language models with a diffusion-compatible sequence-level surrogate and a learned prompt-dependent normalization. Across mathematical reasoning and code generation benchmarks, TraFL is the only evaluated post-training method that improves over the base model in every benchmark-length setting, with gains that persist as the sampling budget increases. The improvements transfer to held-out evaluations: TraFL stays above the base model on Minerva Math and is the strongest method on every LiveCodeBench difficulty split.

---


### 6. [Towards the Next Frontier of LLMs, Training on Private Data: A Cross-Domain Benchmark for Federated Fine-Tuning](https://arxiv.org/abs/2605.13936)

**<font color=#1a73e8>作者：</font>** Daniel M. Jimenez-Gutierrez, Enrique Zuazua, Georgios Kellaris 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recent success of large language models (LLMs) has been largely driven by vast public datasets. However, the next frontier for LLM development lies beyond public data. Much of the world's most valuable information is private, especially in highly regulated sectors such as healthcare and finance, where data include patient histories or customer communications. Unlocking this data could represent a major leap forward, enabling LLMs with deeper domain expertise and stronger real-world utility. Yet, these data cannot be shared because they are distributed across institutions and constrained by privacy, regulatory, and organizational barriers. Moreover, institutional datasets are typically non-independent and identically distributed (non-IID), differing across sites in population characteristics, data modalities, documentation patterns, and task-specific label distributions.
In this paper, we demonstrate a practical approach to unlocking private and distributed institutional data for LLM adaptation through federated collaboration across data silos. Built on the this http URL Federated Learning platform, our framework enables nodes to jointly fine-tune a shared LLM without exchanging private data. We evaluate this approach through a cross-domain benchmark in healthcare and finance, using four closed-ended question answering and classification datasets: MedQA, MedMCQA, FPB, and FiQA-SA. We compare three parameter-efficient fine-tuning (PEFT) strategies-LoRA, QLoRA, and IA3-across pretrained backbones under non-IID settings reflecting institutional data heterogeneity. Our results show that federated fine-tuning performs close to centralized training and outperforms isolated single-institution learning. From a Green AI perspective, QLoRA and IA3 improve efficiency with limited accuracy degradation, supporting federated PEFT as a viable approach for adapting LLMs where data cannot be shared.

---


### 7. [EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents](https://arxiv.org/abs/2605.13941)

**<font color=#1a73e8>作者：</font>** Jiaqi Liu, Xinyu Ye, Peng Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full retrieval configuration as a structured action space optimized by an LLM-powered diagnosis module. In each evolution round, the module reads per-question failure logs, identifies root causes, and proposes targeted configuration adjustments; a guarded meta-analyzer applies them with automatic revert-on-regression and explore-on-stagnation safeguards. This closed-loop self-evolution realizes an AutoResearch process: the system autonomously conducts iterative research cycles on its own architecture, replacing manual configuration tuning. Starting from a minimal baseline, the process converges autonomously, discovering effective retrieval strategies including entirely new configuration dimensions not present in the original action space. On LoCoMo, EvolveMem outperforms the strongest baseline by 25.7% relative and achieves a 78.0% relative improvement over the minimal baseline. On MemBench, EvolveMem exceeds the strongest baseline by 18.9% relative. Evolved configurations transfer across benchmarks with positive rather than catastrophic transfer, indicating that the self-evolution process captures universal retrieval principles rather than benchmark-specific heuristics. Code is available at this https URL.

---


### 8. [Towards Resource-Efficient LLMs: End-to-End Energy Accounting of Distillation Pipelines](https://arxiv.org/abs/2605.13981)

**<font color=#1a73e8>作者：</font>** Katherine Lambert, Sasha Luccioni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rise in deployment of large language models has driven a surge in GPU demand and datacenter scaling, raising concerns about electricity use, grid stress, and the impacts of modern AI workloads. Distillation is often promoted as one of the most effective paths to obtain cheaper, more efficient models, yet these claims rarely account for the full end-to-end energy and resource costs, including crucial teacher-side workloads such as data generation, logit caching, and evaluation. We present a comprehensive energy accounting framework that measures the complete computational cost of distillation pipelines via detailed stage-wise tracking of GPU device power consumption. In our experiments, we separate and log empirical energy use across distinct phases and systematically measure the energy and emissions of two common distillation methods: the classic logit-based knowledge distillation and synthetic-data supervised fine-tuning, constructing energy-quality Pareto frontiers that expose the previously ignored costs. From these measurements and analyses, we derive practical design rules for selecting distillation methods and hyperparameters under energy and budget constraints, and release an open-source measurement harness and accounting protocol to provide a standardized foundation for comparable, reproducible distillation research, explicitly accountable for complete pipeline energy impact.

---


### 9. [VectraYX-Nano: A 42M-Parameter Spanish Cybersecurity Language Model with Curriculum Learning and Native Tool Use](https://arxiv.org/abs/2605.13989)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present VectraYX-Nano, a 41.95M-parameter decoder-only language model trained from scratch in Spanish for cybersecurity, with a Latin-American focus and native tool invocation via the Model Context Protocol (MCP). Four contributions: (i) Corpus: VectraYX-Sec-ES, a 170M-token Spanish corpus from an eight-VM pipeline (~$25 USD) partitioned into conversational (42M tokens, OpenSubtitles-ES, OASST1), cybersecurity (118M tokens, NVD, Wikipedia-ES, CVE mirror, security blogs), and offensive-security tooling (10M tokens, ExploitDB, HackTricks, OWASP) phases. (ii) Architecture: 42M-parameter Transformer decoder with GQA, QK-Norm, RMSNorm, SwiGLU, RoPE, z-loss, and a 16,384-token byte-fallback BPE. (iii) Curriculum with replay: continual pre-training with a replay buffer yields monotonic loss descent (9.80->3.17->3.00->2.16); after SFT on OASST-ES, Alpaca-ES, CVE Q&A, and 6,327 tool-use traces, the model attains a conversational gate of 0.78+-0.05 (N=4 seeds). (iv) Two findings: a bootstrap-corpus ablation reveals a loss-vs-register inversion at nano scale; a LoRA study shows the B4 tool-selection floor of 0.000 is a corpus-density artifact, not a capacity gate -- a tool-dense corpus (2,801 examples) raises B4 to 0.145+-0.046 on Nano 42M and 0.445+-0.201 on a 260M mid-tier. The GGUF artifact is 81 MB (F16), runs at sub-second TTFT on commodity hardware under this http URL, and is to our knowledge the first Spanish-native cybersecurity LLM with end-to-end MCP integration. Corpus recipe, training scripts, GGUF weights, and B1-B5 benchmark are released.

---


### 10. [HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse Mixture-of-Experts](https://arxiv.org/abs/2605.13997)

**<font color=#1a73e8>作者：</font>** Tao Zhong, Dongzhe Zheng, Christine Allen-Blanchette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) layers route tokens through a handful of experts, and learning-free compression of these layers reduces inference cost without retraining. A subtle obstruction blocks every existing compressor in this family: three experts can each be pairwise compatible yet form an irreducible cycle when merged together, so any score that ranks experts on pairwise signals is structurally blind to which triples are jointly mergeable. We show the obstruction is a precise mathematical object, the harmonic kernel of the simplicial Laplacian on a 2-complex whose vertices are experts, whose edges carry KL merge barriers, and whose faces carry triplet barriers; Hodge-decomposing the edge-barrier signal isolates the kernel exactly. We turn the diagnostic into a selection objective: HodgeCover greedily covers the harmonic-critical edges and triplet-critical triangles, and a hybrid variant of HodgeCover pairs it with off-the-shelf weight pruning on survivors. On three open-weight Sparse MoE backbones under aggressive expert reduction, HodgeCover matches state-of-the-art learning-free baselines on the expert-reduction axis, leads on the aggressive-compression frontier of the hybrid axis, and uniquely balances retained mass across all four Hodge components. These results show that exposing the harmonic kernel of a learned MoE structure changes which compressor wins at the regime that matters most.

---


### 11. [PolitNuggets: Benchmarking Agentic Discovery of Long-Tail Political Facts](https://arxiv.org/abs/2605.14002)

**<font color=#1a73e8>作者：</font>** Yifei Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) embedded in agentic frameworks have transformed information retrieval from static, long context question answering into open-ended exploration. Yet real world use requires models to discover and synthesize "long-tail" facts from dispersed sources, a capability that remains under-evaluated. We introduce PolitNuggets, a multilingual benchmark for agentic information synthesis via constructing political biographies for 400 global elites, covering over 10000 political facts. We standardize evaluation with an optimized multi agent system and propose FactNet, an evidence conditional protocol that scores discovery, fine-grained accuracy, and efficiency. Across models and settings, we find that current systems often struggle with fine-grained details, and vary substantially in efficiency. Finally, using benchmark diagnostics, we relate agent performance to underlying model capabilities, highlighting the importance of short-context extraction, multilingual robustness, and reliable tool use.

---


### 12. [Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding](https://arxiv.org/abs/2605.14005)

**<font color=#1a73e8>作者：</font>** Shuoyang Sun, Chang Da, Hao Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has become a widely adopted technique for accelerating large language model (LLM) inference by drafting multiple candidate tokens and verifying them with a target model in parallel. Its efficiency, however, critically depends on the average accepted length $\tau$, i.e., how many draft tokens survive each verification step. In this work, we identify a new mechanism-level vulnerability in model-based speculative decoding: the drafter is trained to approximate the target model distribution, but this approximation is inevitably imperfect. Such a drafter-target mismatch creates a hidden attack surface where small perturbations can preserve the target model's visible behavior while substantially reducing draft-token acceptability. We propose Mistletoe, a stealthy acceleration-collapse attack against speculative decoding. Mistletoe directly targets the acceptance mechanism of speculative decoding. It jointly optimizes a degradation objective that decreases drafter-target agreement and a semantic-preservation objective that constrains the target model's output distribution. To resolve the conflict between these objectives, we introduce a null-space projection mechanism, where degradation gradients are projected away from the local semantic-preserving direction, suppressing draft acceptance while minimizing semantic drift. Experiments on various speculative decoding systems show that Mistletoe substantially reduces average accepted length $\tau$, collapses speedup, and lowers averaged token throughput, while preserving output quality and perplexity. Our work highlights that speculative decoding introduces a mechanism-level attack surface beyond existing output robustness, calling for more robust designs of LLM acceleration systems.

---


### 13. [Unified Pix Token And Word Token Generative Language Model](https://arxiv.org/abs/2605.14028)

**<font color=#1a73e8>作者：</font>** Haun Leung, ZiNan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Since the emergence of Vision Transformer (ViT), it has been widely used in generative language model and generative visual model. Especially in the current state-of-art open source multimodal models, ViT obtained by CLIP or SigLIP method serves as the vision encoder backbone to help them acquire visual understanding capabilities. But this method leads to limitations in visual understanding for details, such as difficulty in recognizing small text or numbers in images. To address these issues, we propose a new model to unify pix token and word token into the generative language model. The new model also features with each pix of image having its own token embedding, color folding, global conditional attention approximation and image unsupervised pretraining. We conducted image unsupervised pretraining experiments using our new model to explore its potential. The experimental results show that it has good performance even in small model and with limited training data. We believe our model also conforms to the scaling law, as long as model parameters and training data increased, its performance will continue to improve.

---


### 14. [From Descriptive to Prescriptive: Uncover the Social Value Alignment of LLM-based Agents](https://arxiv.org/abs/2605.14034)

**<font color=#1a73e8>作者：</font>** Jinxian Qu, Qingqing Gu, Teng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wide applications of LLM-based agents require strong alignment with human social values. However, current works still exhibit deficiencies in self-cognition and dilemma decision, as well as self-emotions. To remedy this, we propose a novel value-based framework that employs GraphRAG to convert principles into value-based instructions and steer the agent to behave as expected by retrieving the suitable instruction upon a specific conversation context. To evaluate the ratio of expected behaviors, we define the expected behaviors from two famous theories, Maslow's Hierarchy of Needs and Plutchik's Wheel of Emotion. By experimenting with our method on the benchmark of DAILYDILEMMAS, our method exhibits significant performance gains compared to prompt-based baselines, including ECoT, Plan-and-Solve, and Metacognitive prompting. Our method provides a basis for the emergence of self-emotion in AI systems.

---


### 15. [Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use](https://arxiv.org/abs/2605.14038)

**<font color=#1a73e8>作者：</font>** Yize Cheng, Chenrui Fan, Mahdi JafariRaviz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly act as autonomous agents that must decide when to answer directly vs. when to invoke external tools. Prior work studying adaptive tool use has largely treated tool necessity as a model-agnostic property, annotated by human or LLM judge, and mostly cover cases where the answer is obvious (e.g., fetching the weather vs. paraphrasing text). However, tool necessity in the wild is more nuanced due to the divergence of capability boundaries across models: a problem solvable by a strong model on its own may still require tools for a weaker one. In this work, we introduce a model-adaptive definition of tool-necessity, grounded in each model's empirical performance. Following this definition, we compare the necessity against observed tool-call behavior across four models on arithmetic and factual QA dataset, and find substantial mismatches of 26.5-54.0% and 30.8-41.8%, respectively. To diagnose the failure, we decompose tool use into two stages: an internal cognition stage that reflects whether a model believes a tool is necessary, and an execution stage that determines whether the model actually makes a tool-call action. By probing the LLM hidden states, we find that both signals are often linearly decodable, yet their probe directions become nearly orthogonal in the late-layer, last-token regime that drives the next-token action. By tracing the trajectory of samples in the two-stage process, we further discover that the majority of mismatch is concentrated in the cognition-to-action transition, not in cognition itself. These results reveal a knowing-doing gap in LLM tool-use: improving tool-use reliability requires not only better recognition of when tools are needed, but also better translation of that recognition into action.

---


### 16. [Physics-R1: An Audited Olympiad Corpus and Recipe for Visual Physics Reasoning](https://arxiv.org/abs/2605.14040)

**<font color=#1a73e8>作者：</font>** Shan Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We audit the multimodal-physics evaluation pipeline end-to-end and document three undetected construction practices that distort how the field measures vision-language reasoning: train-eval contamination, translation drift, and MCQ saturation. (1) Public training pools (UGPhysics-Train, SciInstruct, MMK12) pass single-stage 5-gram-Jaccard audits with zero hits across all six public physics evals; a three-stage audit (Jaccard -> mxbai-embed-large cosine -> Haiku-4.5 LLM-judge) surfaces 134 near-duplicates and 4,846 paraphrase candidates in SciInstruct alone. (2) A 17-pp Sonnet 4.5 delta on 59 paired Estonian-English olympiad problems (30.5% vs. 13.6%; sign test p=0.011, McNemar p=0.021, paired bootstrap 95% CI [+5.1, +28.9] pp). (3) A 46-pp format-and-novelty gradient on identical Sonnet weights between MCQ (79.7% on PhyX) and open-ended olympiad evaluation (33.4% on PhysOlym-A). We release four artifacts addressing these gaps: PhysCorp-A (6,432-record three-stage-audited multimodal corpus), PhysR1Corp (2,268-record closed-form RL pool), PhysOlym-A (500-problem, 99.8% novel-source held-out olympiad eval with native difficulty labels and an EN/ET bilingual subset), and Physics-R1, a reference GSPO+DAPO recipe cold-started from Qwen3-VL-8B-Thinking. Across 3 seeds, Physics-R1 lifts the audited corpus over the 8B base by +18.3 pp on PhysOlym-A liberal (8.0 -> 26.3 +/- 1.7; 7.1 pp behind Sonnet 4.5), +15.7 pp on PhysReason (23.9 -> 39.6 +/- 6.4; ahead of Qwen3-VL-32B and Gemini 2.5 Pro), +6.9 pp on OlympiadBench-Physics (46.2 +/- 1.5), and +4.1 pp on PhyX MCQ (77.8 +/- 0.3).

---


### 17. [SPIN: Structural LLM Planning via Iterative Navigation for Industrial Tasks](https://arxiv.org/abs/2605.14051)

**<font color=#1a73e8>作者：</font>** Yusuke Ozaki, Dhaval Patel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial LLM agent systems often separate planning from execution, yet LLM planners frequently produce structurally invalid or unnecessarily long workflows, leading to brittle failures and avoidable tool and API cost. We propose \texttt{SPIN}, a planning wrapper that combines validated Directed Acyclic Graph (DAG) planning with prefix based execution control. \texttt{SPIN} enforces a strict DAG contract through \texttt{\_validate\_plan\_text} and repair prompting, producing executable plans before downstream execution, and then evaluates DAG prefixes incrementally to stop when the current prefix is sufficient to answer the query. On AssetOpsBench, across 261 scenarios, \texttt{SPIN} reduces executed tasks from 1061 to 623 and improves \emph{Accomplished} from 0.638 to 0.706, while reducing tool calls from 11.81 to 6.82 per run. On MCP Bench, the same wrapper improves planning, grounding, and dependency related scores for both GPT OSS1 and Llama 4 Maverick.

---


### 18. [Derivation Prompting: A Logic-Based Method for Improving Retrieval-Augmented Generation](https://arxiv.org/abs/2605.14053)

**<font color=#1a73e8>作者：</font>** Ignacio Sastre, Guillermo Moncecchi, Aiala Rosá  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The application of Large Language Models to Question Answering has shown great promise, but important challenges such as hallucinations and erroneous reasoning arise when using these models, particularly in knowledge-intensive, domain-specific tasks. To address these issues, we introduce Derivation Prompting, a novel prompting technique for the generation step of the Retrieval-Augmented Generation framework. Inspired by logic derivations, this method involves deriving conclusions from initial hypotheses through the systematic application of predefined rules. It constructs a derivation tree that is interpretable and adds control over the generation process. We applied this method in a specific case study, significantly reducing unacceptable answers compared to traditional RAG and long-context window methods.

---


### 19. [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)

**<font color=#1a73e8>作者：</font>** Haozhe Wang, Qixin Xu, Changpeng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving robust perception-reasoning synergy is a central goal for advanced Vision-Language Models (VLMs). Recent advancements have pursued this goal via architectural designs or agentic workflows. However, these approaches are often limited by static textual reasoning or complicated by the significant compute and engineering burden of external agentic complexity. Worse, this heavy investment does not yield proportional gains, often witnessing a "seesaw effect" on perception and reasoning. This motivates a fundamental rethinking of the true bottleneck. In this paper, we argue that the root cause of this trade-off is an ambiguity in modality credit assignment: when a VLM fails, is it due to flawed perception ("bad seeing") or flawed logic ("bad thinking")? To resolve this, we introduce a reinforcement learning framework that improves perception-reasoning synergy by reliably rewarding the perception fidelity. We explicitly decompose the generation process into interleaved perception and reasoning steps. This decoupling enables targeted supervision on perception. Crucially, we introduce Perception Verification (PV), leveraging a "blindfolded reasoning" proxy to reward perceptual fidelity independently of reasoning outcomes. Furthermore, to scale training across free-form VL tasks, we propose Structured Verbal Verification, which replaces high-variance LLM judging with structured algorithmic execution. These techniques are integrated into a Modality-Aware Credit Assignment (MoCA) mechanism, which routes rewards to the specific source of error -- either bad seeing or bad thinking -- enabling a single VLM to achieve simultaneous performance gains across a wide task spectrum.

---


### 20. [PEML: Parameter-efficient Multi-Task Learning with Optimized Continuous Prompts](https://arxiv.org/abs/2605.14055)

**<font color=#1a73e8>作者：</font>** Anjir Ahmed Chowdhury, Syed Zawad, Xiaolong Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) is widely used for adapting Large Language Models (LLMs) for various tasks. Recently, there has been an increasing demand for fine-tuning a single LLM for multiple tasks because it requires overall less data for fine-tuning thanks to the common features shared among tasks. More importantly, LLMs are resource demanding and deploying a single model for multiple tasks facilitates resource consolidation and consumes significantly less resources compared to deploying individual large model for each task. Existing PEFT methods like LoRA and Prefix Tuning are designed to adapt LLMs to a specific task. LoRA and its variation focus on aligning the model itself for tasks, overlooking the importance of prompt tuning in multi-task learning while Prefix Tuning only adopts a simple architecture to optimize prompts, which limits the adaption capabilities for multi-task. To enable efficient fine-tuning for multi-task learning, it is important to co-optimize prompt optimization and model adaptation. In this work, we propose a Parameter-Efficient Multi-task Learning (\PM), which employs a neural architecture engineering method for optimizing the continuous prompts while also performing low-rank adaption for model weights. We prototype PEML by creating an automated framework for optimizing the continuous prompts and adapting model weights. We evaluate PEML against state-of-the-arts multi-task learning methods MTL-LoRA, MultiLoRa, C-Poly, and MoE, on the GLUE, SuperGLUE, Massive Multitask Language Understanding, and commonsense reasoning benchmarks. The evaluation results present an average accuracy improvement of up to 6.67%, with individual tasks showing peak gains of up to 10.75%.

---


### 21. [Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Generation via Multi-Stage In-Flight Rejection](https://arxiv.org/abs/2605.14062)

**<font color=#1a73e8>作者：</font>** Anjir Ahmed Chowdhury, Syed Zawad, Feng Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While synthetic data generation with large language models (LLMs) is widely used in post-training pipelines, existing approaches typically generate full outputs before applying quality filters, leading to substantial token waste on samples that are ultimately discarded. To address this, we propose Multi-Stage In-Flight Rejection (MSIFR), a lightweight, training-free framework that detects and terminates low-quality generation trajectories at intermediate checkpoints before they reach full completion. MSIFR decomposes the generation process into sequential stages and applies fast rule-based validators to identify arithmetic inconsistencies, hallucination patterns, and formatting violations, enabling early rejection of faulty samples. We formalize in-flight rejection as a sequential decision process and show that any non-trivial discard policy reduces expected token consumption, with stage-wise savings increasing when rejection occurs earlier in the generation pipeline. We further demonstrate that conditional utility estimates form a martingale, ensuring that early, in-flight rejection does not bias the expected utility of retained samples. Across five instruction-tuned models and seven reasoning benchmarks, MSIFR reduces token consumption by 11%-77% as a standalone method, and up to 78.2% when combined with early-exit methods, while preserving or improving evaluation accuracy. These results confirm that MSIFR provides a practical mechanism for improving the efficiency of LLM-based synthetic data generation without additional training or architectural changes.

---


### 22. [CurveBench: A Benchmark for Exact Topological Reasoning over Nested Jordan Curves](https://arxiv.org/abs/2605.14068)

**<font color=#1a73e8>作者：</font>** Amirreza Mohseni, Mona Mohammadi, Morteza Saghafian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CurveBench, a benchmark for hierarchical topological reasoning from visual input. CurveBench consists of \textbf{756 images} of pairwise non-intersecting Jordan curves across easy, polygonal, topographic-inspired, maze-like, and dense counting configurations. Each image is annotated with a rooted tree encoding the containment relations between planar regions. We formulate the task as structured prediction: given an image, a model must recover the full rooted containment tree induced by the curves. Despite the visual simplicity of the task, the strongest evaluated model, Gemini 3.1 Pro, achieves only \textbf{71.1\%} tree-generation accuracy on CurveBench-Easy and \textbf{19.1\%} on CurveBench-Hard. We further demonstrate benchmark utility through RLVR-style fine-tuning of open-weight vision-language models. Our trained Qwen3-VL-8B model improves over \texttt{Qwen-3-VL-8B-Thinking} from \textbf{2.8\%} to \textbf{33.3\%} tree-generation accuracy on CurveBench-Easy, exceeding GPT-5.4 and Claude Opus 4.5 under our evaluation protocol. The remaining gap, especially on CurveBench-Hard, shows that exact topology-aware visual reasoning remains far from solved.

---


### 23. [Distribution Corrected Offline Data Distillation for Large Language Models](https://arxiv.org/abs/2605.14071)

**<font color=#1a73e8>作者：</font>** Yumeng Zhang, Zhengbang Yang, Yevin Nikhel Goonatilake 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distilling reasoning traces from strong large language models into smaller ones is a promising route to improve intelligence in resource-constrained settings. Existing approaches face a fundamental trade-off: offline distillation from teacher-generated traces provides high-quality, sample-efficient supervision but suffers from distributional drift: during training, the student model conditions on teacher-generated prefixes, whereas during inference the student autoregresses on self-generated prefixes, leading to compounding errors over long reasoning trajectories. Meanwhile, on-policy or self-distillation methods better match the student's inference-time distribution, but require costly online sampling and often produce low-quality traces in early training. We propose a principled offline reasoning distillation framework that preserves the efficiency and supervision quality of offline teacher-generated data while correcting teacher-student distribution drift. It adaptively emphasizes teacher supervision that is better aligned with the student's on-policy distribution. Evaluations on mathematical reasoning benchmarks of GSM8K, MATH, MATH500, and harder held-out competition-style tasks, including AMC, AIME, and OlympiadBench, show that our method improves reasoning accuracy over prior offline distillation algorithms and yields more stable reasoning traces while preserving instruction-following capabilities. Our work shows that lightweight, distribution-correction-aware training can substantially strengthen offline reasoning distillation without online rollouts.

---


### 24. [Rethinking Layer Relevance in Large Language Models Beyond Cosine Similarity](https://arxiv.org/abs/2605.14075)

**<font color=#1a73e8>作者：</font>** Cristian Hinostroza, Rodrigo Toro Icarte, Christ Devia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have revolutionized natural language processing. Understanding their internal mechanisms is crucial for developing more interpretable and optimized architectures. Mechanistic interpretability has led to the development of various methods for assessing layer relevance, with cosine similarity being a widely used tool in the field. On this work, we demonstrate that cosine similarity is a poor proxy for the actual performance degradation caused by layer removal. Our theoretical analysis shows that a layer can exhibit an arbitrarily low cosine similarity score while still being crucial to the model's performance. On the other hand, empirical evidence from a range of LLMs confirms that the correlation between cosine similarity and actual performance degradation is often weak or moderate, leading to misleading interpretations of a transformer's internal mechanisms. We propose a more robust metric for assessing layer relevance: the actual drop in model accuracy resulting from the removal of a layer. Even though it is a computationally costly metric, this approach offers a more accurate picture of layer importance, allowing for more informed pruning strategies and lightweight models. Our findings have significant implications for the development of interpretable LLMs and highlight the need to move beyond cosine similarity in assessing layer relevance.

---


### 25. [Measuring and Mitigating Toxicity in Large Language Models: A Comprehensive Replication Study](https://arxiv.org/abs/2605.14087)

**<font color=#1a73e8>作者：</font>** Mokshit Surana, Archit Rathod, Akshaj Satishkumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs), when trained on web-scale corpora, inherently absorb toxic patterns from their training data. This leads to ``toxic degeneration'' where even innocuous prompts can trigger harmful outputs. This phenomenon poses significant risks for real-world deployments. Thus, necessitating effective mitigation strategies that should maintain model utility while ensuring safety. In this comprehensive replication study, we evaluate the efficacy of \textbf{DExperts} (Decoding-time Experts), which is an inference-time mitigation technique that steers generation without requiring model retraining. We structured our research into three systematic phases: (1) establishing baseline toxicity measurements using \textbf{RealToxicityPrompts} on standard GPT-2 models; then (2) implementing and evaluating DExperts to mitigate explicit toxicity; and finally (3) stress-testing the method against implicit hate speech using the adversarial \textbf{ToxiGen} dataset. Our empirical results confirm that while DExperts achieves near-perfect safety rates (100\%) on explicit toxicity benchmarks, it exhibits brittleness against adversarial, implicit hate speech, with safety rates dropping to 98.5\%. Furthermore, we quantify a critical trade-off. The method introduces a $\sim$10x latency penalty (from 0.2s to 2.0s per generation), posing challenges for real-time deployment scenarios. This study contributes to the growing body of work on AI safety by highlighting the robustness gap between explicit and implicit toxicity mitigation. We emphasize the need for more sophisticated approaches that generalize across diverse hate speech patterns without prohibitive computational costs.

---


### 26. [SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration](https://arxiv.org/abs/2605.14089)

**<font color=#1a73e8>作者：</font>** Mingda Zhang, Tiesunlong Shen, Haoran Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, a variety of powerful LLM-based agentic systems have been applied to automate complex tasks through task orchestration. However, existing orchestration methods still face key challenges, including strategy collapse under reward maximization, high gradient variance with opaque credit assignment, and unguided skill evolution whose decisions are typically made by directly prompting an LLM to judge rather than derived from principled training signals. To address these challenges, we propose SkillFlow, a flow-based framework that takes a trainable Supervisor as the agent and a structured environment with dynamic skill library and frozen executor, automating task orchestration through multi-turn interaction. SkillFlow employs Tempered Trajectory Balance (TTB), a regression-based flow-matching loss that samples trajectories proportional to reward, preserving diverse orchestration strategies rather than collapsing to a single mode. The same flow objective yields a jointly learned backward policy that provides transparent per-step credit assignment at zero additional inference cost. Building on these flow diagnostics, a recursive skill evolution mechanism determines when to evolve, what skills to create or prune, and where decision gaps lie -- closing the loop from training signal to autonomous capability growth. Experimental results on 14 datasets show that SkillFlow significantly outperforms baselines across question answering, mathematical reasoning, code generation, and real-world interactive decision making tasks. Our code is available at this https URL.

---


### 27. [Real-Time Group Dynamics with LLM Facilitation: Evidence from a Charity Allocation Task](https://arxiv.org/abs/2605.14097)

**<font color=#1a73e8>作者：</font>** Aaron Parisi, Nithum Thain, Alden Hallak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) evolve from single-user assistants to active participants in civic and workplace deliberation, evaluating their effects on collective decision making becomes a governance challenge. We present two empirical studies (N=879) of real-time, text-based group deliberation in an incentive-compatible charity allocation task with real financial stakes ($7,200 USD). Groups of three allocate a donation budget under varying LLM facilitation conditions: Study 1 (N=204) compares three frontier models; Study 2 (N=675) compares facilitator strategies against a no-facilitation baseline. Across both studies, LLM facilitation did not significantly improve group consensus in either study, yet participants consistently preferred facilitated discussion. We additionally identify two governance-relevant risks. First, algorithmic steering: facilitators shifted select charity-level allocations by up to 5.5 percentage points -- directly affecting the final charitable payout -- even when aggregate agreement metrics remained unchanged. Second, an illusion of inclusion: participants cited inclusivity as their primary reason for preferring LLM facilitators, yet neither survey nor transcript-based measures of participation equity improved. Notably, participants reported greater trust in the process under the same conditions where facilitators exerted directional influence on outcomes. Together, these findings show that in AI-mediated group deliberation, perceived procedural improvement can coexist with measurable steering and unchanged participation inequality, motivating evaluation practices that treat collective outcomes, interaction dynamics, and participant perceptions as distinct governance targets.

---


### 28. [ProtoMedAgent: Multimodal Clinical Interpretability via Privacy-Aware Agentic Workflows](https://arxiv.org/abs/2605.14113)

**<font color=#1a73e8>作者：</font>** Alvaro Lopez Pellicer, Plamen Angelov, Marwan Bukhari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While interpretable prototype networks offer compelling case-based reasoning for clinical diagnostics, their raw continuous outputs lack the semantic structure required for medical documentation. Bridging this gap via standard Retrieval-Augmented Generation (RAG) routinely triggers ``retrieval sycophancy,'' where Large Language Models (LLMs) hallucinate post-hoc rationalizations to align with visual predictions. We introduce ProtoMedAgent, a framework that formalizes multimodal clinical reporting as an iterative, zero-gradient test-time optimization problem over a strict neuro-symbolic bottleneck. Operating on a frozen prototype backbone, we distill latent visual and tabular features into a discrete semantic memory. Online generation is strictly constrained by exact set-theoretic differentials and a reflective Scribe-Critic loop, mathematically precluding unsupported narrative claims. To safely bound data disclosure, we introduce a semantic privacy gate governed by $k$-anonymity and $\ell$-diversity. Evaluated on a 4,160-patient clinical cohort, ProtoMedAgent achieves 91.2\% Comparison Set Faithfulness where it fundamentally outperforms standard RAG (46.2\%). ProtoMedAgent additionally leverages a binding $\ell$-diversity phase transition to systematically reduce artifact-level membership inference risks by an absolute 9.8\%.

---


### 29. [When Evidence Conflicts: Uncertainty and Order Effects in Retrieval-Augmented Biomedical Question Answering](https://arxiv.org/abs/2605.14115)

**<font color=#1a73e8>作者：</font>** Yikun Han, Mengfei Lan, Halil Kilicoglu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical retrieval-augmented large language models (LLMs) often face evidence that is incomplete, misleading, or internally contradictory, yet evaluation usually emphasizes answer accuracy under helpful context rather than reliability under conflict. Using HealthContradict, we evaluate six open-weight LLMs under five controlled evidence conditions: no retrieved context, correct-only context, incorrect-only context, and two mixed conditions containing both correct and contradictory documents in opposite orders. In this conflicting-evidence order contrast, where the same two documents are both present and only their order is reversed, accuracy drops for every model and 11.4%--25.2% of predictions flip. To support abstention in these difficult cases, we also evaluate a conflict-aware abstention score that combines model confidence with a detector of evidence conflict. In the two hardest conditions, this score improves selective accuracy over confidence-only, with mean gains of 7.2--33.4 points in incorrect-only (`IC') and 3.6--14.4 points in incorrect-first conflicting (`ICC') conditions across 75%, 50%, and 25% coverage. These results show that conflicting biomedical evidence is both an uncertainty and robustness problem and motivate evaluation and abstention methods that explicitly account for evidence disagreement.

---


### 30. [Generative Floor Plan Design with LLMs via Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2605.14117)

**<font color=#1a73e8>作者：</font>** Luis Lara, Aristides Milios, Zhi Hao Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An AI system for professional floor plan design must precisely control room dimensions and areas while respecting the desired connectivity between rooms and maintaining functional and aesthetic quality. Existing generative approaches focus primarily on respecting the requested connectivity between rooms, but do not support generating floor plans that respect numerical constraints. We introduce a text-based floor plan generation approach that fine-tunes a large language model (LLM) on real plans and then applies reinforcement learning with verifiable rewards (RLVR) to improve adherence to topological and numerical constraints while discouraging invalid or overlapping outputs. Furthermore, we design a set of constraint adherence metrics to systematically measure how generated floor plans align with user-defined constraints. Our model generates floor plans that satisfy user-defined connectivity and numerical constraints and outperforms existing methods on Realism, Compatibility, and Diversity metrics. Across all tasks, our approach achieves at least a 94% relative reduction in Compatibility compared with existing methods. Our results demonstrate that LLMs can effectively handle constraints in this setting, suggesting broader applications for text-based generative modeling.

---


### 31. [Mini-JEPA Foundation Model Fleet Enables Agentic Hydrologic Intelligence](https://arxiv.org/abs/2605.14120)

**<font color=#1a73e8>作者：</font>** Mashrekur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models compress multispectral observations into dense embeddings increasingly used in natural-language environmental reasoning systems. A single planetary-scale model, e.g. Google AlphaEarth, handles broad characterization well but may compromise on specialized hydrologic signals. Such generalist models are also often inaccessible, expensive, and require large-scale compute. We propose Mini-JEPAs: a fleet of small sensor-specialized Joint Embedding Predictive Architecture (JEPA) foundation models consulted by a routing agent for specialized questions. We pretrained five 22M-parameter Mini-JEPAs sharing an identical Vision Transformer backbone, JEPA recipe, and 64-d output space, using Sentinel-2 optical, Sentinel-1 SAR, MODIS thermal, multi-temporal Sentinel-2 phenology, and a topography-soil stack. Each Mini-JEPA reconstructs the variable matched to its sensor, with cross-validated $R^2$ reaching 0.97 for elevation, 0.97 for temperature, and 0.81 for precipitation. The five manifolds differ in geometric structure, with global participation ratios from 8.9 to 20.2 and local intrinsic dimensionalities from 2.3 to 9.0. Joint topography-soil and phenology models add predictive value beyond AlphaEarth alone for soil moisture, aridity, and precipitation ($\Delta R^2$ up to 0.031). A router LLM reads per-modality references and selects appropriate sensors with a perfect hit rate over a curated question set. In paired LLM-as-Judge evaluation, dual retrieval over AlphaEarth and the routed fleet outperforms AlphaEarth alone on physics-matched questions (Cohen's $d = 1.10$, $p = 0.031$). Locally-trained Mini-JEPAs can be operationalized for hydrologic intelligence with modest compute.

---


### 32. [Polar probe linearly decodes semantic structures from LLMs](https://arxiv.org/abs/2605.14125)

**<font color=#1a73e8>作者：</font>** Pablo J. Diego-Simón, Pierre Orhan, Yair Lakretz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do artificial neural networks bind concepts to form complex semantic structures? Here, we propose a simple neural code, whereby the existence and the type of relations between entities are represented by the distance and the direction between their embeddings, respectively. We test this hypothesis in a variety of Large Language Models (LLMs), each input with natural-language descriptions of minimalist tasks from five different domains: arithmetic, visual scenes, family trees, metro maps and social interactions. Results show that the true semantic structures can be linearly recovered with a Polar Probe targeting a subspace of LLMs' layer activations. Second, this code emerges mostly in middle layers and improves with LLM performance. Third, these Polar Probes successfully generalize to new entities and relation types, but degrades with the size of the semantic structure. Finally, the quality of the polar representation correlates with the LLM's ability to answer questions about the semantic structure. Together, these findings suggest that LLMs learn to build complex semantic structures by binding representations with a simple geometrical principle.

---


### 33. [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](https://arxiv.org/abs/2605.14126)

**<font color=#1a73e8>作者：</font>** Marius S. Knorr, Robert Müller, Jan P. Bremer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast Healthcare Interoperability Resources (FHIR) is the dominant standard for interoperable exchange of healthcare data. In FHIR, electronic health records form a directed graph of resources. Answering clinically meaningful questions over FHIR requires agents to perform multi-step reasoning, filtering, and aggregation across multiple resource types. Prior work shows that even tool-augmented LLM agents (retrieval, code execution, multi-turn planning) often select the wrong resources or violate traversal constraints. We study this problem in the context of FHIR-AgentBench, a benchmark for realistic question answering over real-world hospital data, and frame reasoning on FHIR as a sequential decision-making problem over a queryable structured graph. We implement a multi-turn CodeAct agent and post-train it with reinforcement learning using a custom harness and tools. A LLM Judge provides execution-grounded rewards. Compared to prompt-based, closed-model baselines, RL post-training improves performance while enforcing data-integrity constraints. Empirically, our approach improves answer correctness from 50% (o4-mini) to 77% on FHIR-AgentBench using a smaller and cheaper Qwen3-8B model. We present an end-to-end post-training pipeline (environment building, harness construction, model training and custom evaluation) that reliably improves multi-turn reasoning over structured clinical graphs.

---


### 34. [Distribution-Aware Algorithm Design with LLM Agents](https://arxiv.org/abs/2605.14141)

**<font color=#1a73e8>作者：</font>** Saharsh Koganti, Priyadarsi Mishra, Pierfrancesco Beneventano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study learning when the learned object is executable solver code rather than a predictor. In this setting, correctness is not enough: two solvers may both return valid solutions on the deployment distribution while differing substantially in runtime. Given samples from an unknown task distribution, the learner returns code evaluated on fresh instances by both solution quality and execution time. Our central abstraction is a \emph{solver hint}: reusable structure inferred from samples and compiled into specialized solver code. We prove that the empirically fastest sample-consistent solver from a fixed library generalizes in both correctness and runtime, and that statistically identifiable hints can be recovered and compiled from polynomially many samples.
Empirically, we instantiate the framework with LLM code agents on \(21\) structured combinatorial-optimization target distributions across seven problem classes. The synthesized solvers reach mean normalized quality \(0.971\), improve by \(+0.224\) over the average heuristic pool and by \(+0.098\) over the highest-quality heuristic, and are \(336.9\times\), \(342.8\times\), and \(16.1\times\) faster than the quality-best heuristic, Gurobi, and the selected time-limited exact backend, respectively. On released PACE 2025 Dominating Set private instances, the synthesized solver is valid on all \(100\) graphs and runs about two orders of magnitude faster than top competition solvers, with a moderate quality gap. Inspection shows that many gains come from changing the computational scale: replacing ambient exponential search or general-purpose optimization with compiled distribution-specific computation.

---


### 35. [Uncovering Trajectory and Topological Signatures in Multimodal Pediatric Sleep Embeddings](https://arxiv.org/abs/2605.14156)

**<font color=#1a73e8>作者：</font>** Scott Ye, Harlin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While generative models have shown promise in pediatric sleep analysis, the latent structure of their multimodal embeddings remains poorly understood. This work investigates session-wide diagnostic information contained in the sequences of 30-second pediatric PSG epochs embedded by a multimodal masked autoencoder. We test whether augmenting embeddings with PHATE-derived per-epoch coordinates and whole-night movement descriptors, persistent homology summaries of the embedding cloud, and EHR yields task-relevant signals. Simple linear and MLP models, chosen for interpretability rather than state-of-the-art performance, show that geometric, topological, and clinical features each provide complementary gains. For binary predictions, feature importance is task-dependent, and more expressive late-fusion models generally perform better, with AUPRC improving from 0.26 to 0.34 for desaturation, 0.31 to 0.48 for EEG arousal, 0.09 to 0.22 for hypopnea, and 0.05 to 0.14 for apnea. We also report Brier score and Expected Calibration Error, where the full fusion model yields the best calibration across all four binary tasks. Our study reveals that latent geometry/topology and EHR offer complementary, interpretable signals beyond embeddings, improving calibration and robustness under extreme imbalance.

---


### 36. [Agentic Systems as Boosting Weak Reasoning Models](https://arxiv.org/abs/2605.14163)

**<font color=#1a73e8>作者：</font>** Varun Sunkaraneni, Pierfrancesco Beneventano, Riccardo Neumarker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a committee of weak reasoning-model calls reach the performance of much stronger models? We study verifier-backed committee search as inference-time boosting for reasoning language models. The mechanism is not simply that ``more agents help'': samples expose latent correct solutions, while critics and comparators must recover them without access to the hidden verifier. We formalize this view by separating proposal coverage, local identifiability, progress, and diversity. We prove that coverage can be amplified by repeated sampling, but cannot by itself create useful critics or comparators; reliable amplification requires an additional local soundness signal, such as execution, proof checking, type checking, tests, or constraint solving. We give rank-based bounds showing when local selection errors compose into reliable trajectories, and characterize the proposer-side ceiling: oracle best-of-\(k\) converges only to the mass of task slices on which the proposal system assigns nonzero useful probability. Empirically, on SWE-bench Verified, a single \texttt{GPT-5.4 nano} proposal solves \(67.0\%\) of tasks. Using the same nano model, our critic--comparator orchestration reaches \(76.4\%\) with \(k=8\) proposals, matching the standalone performance of \texttt{Gemini 3 Pro} and \texttt{Claude Opus 4.5} Thinking and approaching the \(79.0\%\) oracle best-of-\(8\) upper bound. Thus, many correct patches are already present in weak-model proposal pools; the main challenge is selecting them. The remaining failures are mostly proposal-coverage failures, indicating shared blind spots that stronger selection alone cannot close.

---


### 37. [Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations](https://arxiv.org/abs/2605.14175)

**<font color=#1a73e8>作者：</font>** Qisong He, Yi Dong, Xiaowei Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In long conversations, an LLM can produce a next utterance that sounds plausible but rests on premises the conversation has already abandoned. Context-manipulation attacks against deployed agents now actively exploit this gap. We close it with a runtime verifier that maintains an explicit dependency graph: an LLM classifies each turn into one of 8 update operations drawn from four formalisms (dynamic epistemic logic, abductive reasoning, awareness logic, argumentation), and a symbolic engine records which claims depend on which evidence. Checking whether a continuation is supported reduces to a graph walk; retraction propagates through the same graph to flag exactly the conclusions that lose support, with linear per-turn cost and a formal conflict-free guarantee. On LongMemEval-KU oracle (n=78), the verifier reaches 89.7% accuracy vs. 88.5% for the LLM-only baseline (+1.3pp) and 87.2% for a transcript-RAG baseline matched on retrieval budget (+2.6pp); wins among disagreements are correct abstentions where the baseline confabulates. On LoCoMo's 60 official QA items the verifier is competitive with retrieval-augmented baselines. Beyond external benchmarks, we construct two multi-agent scenarios and a 50-item grounding test: on the 15-item stale-premise subset, the verifier reaches 100% accuracy vs. 93.3% (+6.7pp). These instantiate a soundness-faithfulness decomposition: the structural check is sound by construction, and per-deployment LLM extraction faithfulness is the empirical question we measure across four LLM families. The retraction check plateaus at microseconds while history-replay grows linearly with conversation length.

---


### 38. [LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling](https://arxiv.org/abs/2605.14186)

**<font color=#1a73e8>作者：</font>** Qi Cao, Yufan Wang, Peijia Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often expose useful signals of self-monitoring: before solving a problem, they can estimate whether they are likely to succeed, and after solving it, they can judge whether their answer is likely to be correct. However, these signals are typically measured or elicited in isolation, rather than used to control inference. In this work, we ask whether LLMs possess latent metacognitive ability that can be turned into effective test-time control. Inspired by the Nelson--Narens theory from cognitive psychology, we propose a metacognitive harness that separates monitoring from reasoning. For each problem, the model first reports a pre-solve feeling-of-knowing (FOK) signal; after each solve attempt, it reports a post-solve judgment-of-learning (JOL) signal. Rather than treating these signals as passive confidence estimates, the harness turns them into an explicit control interface for reasoning: it decides when to trust the current solution, when to retry with compact metacognitive feedback, and when to pass multiple attempts to a final aggregator. Across text, code, and multimodal reasoning benchmarks, our harness substantially improves a fixed Claude Sonnet-4.6 base model without parameter updates or benchmark-specific fine-tuning. On the evaluated public benchmark snapshots, it raises pooled accuracy from 48.3 to 56.9 and exceeds the strongest listed leaderboard entries on the three primary evaluation settings: HLE-Verified, LiveCodeBench v6, and R-Bench-V. These results suggest that strong LLMs may already possess useful metacognitive ability, but require an explicit control harness to act on it during reasoning.

---


### 39. [Why Retrieval-Augmented Generation Fails: A Graph Perspective](https://arxiv.org/abs/2605.14192)

**<font color=#1a73e8>作者：</font>** Kai Guo, Xinnan Dai, Zhibo Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a powerful and widely used approach for improving large language models by grounding generation in retrieved evidence. However, RAG systems still produce incorrect answers in many cases. Why RAG fails despite having access to external information remains poorly understood. We present a model-internal study of retrieval-augmented generation that examines how retrieved evidence influences answer generation. Using circuit tracing, we construct attribution graphs that model the flow of information through transformer layers during decoding. These graphs represent interactions among retrieved context, intermediate model activations, and generated tokens, providing a graph, circuit-level view of how external evidence is integrated into the model's reasoning process across multiple question answering benchmarks, we observe consistent structural differences: correct predictions exhibit deeper reasoning paths, more distributed evidence flow, and a more structured pattern of local connectivity, while failed predictions show shallower, fragmented, and overly concentrated evidence flow. Building on these findings, we develop a graph-based error detection framework that uses attribution-graph topology features. Furthermore, we show that attribution graphs enable targeted interventions. By reinforcing question-constrained evidence grounding, we reshape internal routing so that answer generation remains guided by the question, leading to more effective integration of retrieved information and fewer errors.

---


### 40. [GradShield: Alignment Preserving Finetuning](https://arxiv.org/abs/2605.14194)

**<font color=#1a73e8>作者：</font>** Zhanhao Hu, Xiao Huang, Patrick Mendoza 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) pose a significant risk of safety misalignment after finetuning, as models can be compromised by both explicitly and implicitly harmful data. Even some seemingly benign data can inadvertently steer a model towards misaligned behaviors. To address this, we introduce GradShield, a principled filtering method that safeguards LLMs during finetuning by identifying and removing harmful data points before they corrupt the model's alignment. It removes potentially harmful data by computing a Finetuning Implicit Harmfulness Score (FIHS) for each data point and employs an adaptive thresholding algorithm. We apply GradShield to multiple utility fine-tuning tasks across varying levels of harmful data and evaluate the safety and utility performance of the resulting LLMs using various metrics. The results show that GradShield outperforms all baseline methods, consistently maintaining an Attack Success Rate (ASR) below $6\%$ while preserving utility performance.

---


### 41. [SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents](https://arxiv.org/abs/2605.14205)

**<font color=#1a73e8>作者：</font>** Zahra Zanjani Foumani, Alberto Castelo, Shuang Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based web agents can navigate live storefronts, yet they often collapse to a single "average buyer" policy, failing to capture the heterogeneous and distributional nature of real buyer populations. Existing personalization methods rely on hand-crafted prompt-based personas that are brittle, difficult to scale, context-inefficient, and unable to faithfully represent population-level behavior. We introduce SimPersona, a novel framework that learns discrete buyer types from historical traffic and exposes them to LLM-based web agents as compact persona tokens. Given raw clickstreams, a behavior-aware VQ-VAE induces a discrete buyer-type space that captures the statistical structure of real buyer behavior and merchant-specific buyer population distributions. To provide behavior-specific guidance to LLM-based web agents, SimPersona maps each learned buyer type to a dedicated persona token in the LLM agent vocabulary and fine-tunes the agent with these tokens on real browsing traces. At inference, each synthetic buyer is assigned to a learned buyer type with a single encoder forward pass, requiring no retraining or store-specific prompt engineering. For population-level simulation, SimPersona samples buyer types from each merchant's empirical distribution over the learned VQ-VAE codebook and instantiates agents with the corresponding persona tokens, preserving merchant-specific buyer population distributions. Evaluated on $8.37$M buyers across $42$ held-out live storefronts, SimPersona achieves $78\%$ conversion-rate alignment with real buyers, exhibits interpretable behavioral variation across buyer types, and outperforms a baseline with $8\times$ more parameters on goal-oriented shopping tasks. We further release an open-source data pipeline that converts raw e-commerce event logs into buyer representations and agent-training traces.

---


### 42. [PreFT: Prefill-only finetuning for efficient inference](https://arxiv.org/abs/2605.14217)

**<font color=#1a73e8>作者：</font>** Andrew Lanpouthakoun, Aryaman Arora, Zhengxuan Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can now be personalised efficiently at scale using parameter efficient finetuning methods (PEFTs), but serving user-specific PEFTs harms throughput, even with specialised kernels and memory management techniques. This is because, theoretically and empirically, a mismatch exists between prefill (processing a large number of tokens at once) and decode (generating a single token autoregressively): the latter has far lower throughput when serving multiple adapters. Rather than optimising performance relative to parameter count, for efficient multi-adapter serving, we instead ought to optimise performance relative to serving throughput. We therefore propose PreFT (Prefill-only Finetuning), wherein we only apply the adapter to prefill tokens and discard it afterwards. PreFT significantly increases throughput with minimal effect on performance. We develop and release an efficient implementation of two prefill-only PEFTs, LoRA and ReFT, on the vLLM inference engine. We first show that serving multi-user PreFTs is more efficient than traditional PEFTs ($1.9\times$ the throughput when serving $512$ adapters on Llama 3.1 70B). Then, we compare the performance of prefill-only vs. all-token adapters on a variety of supervised finetuning and reinforcement learning tasks with LMs at varying scales. On SFT, we observe that the evaluation loss of PreFTs is higher than PEFTs, but can be compensated by increasing rank with nearly no reduction in throughput. On RL, we consistently find that PreFTs approach parity with standard PEFTs. Together, this work validates prefill-only adaptation of LLMs as a more favourable accuracy-throughput tradeoff than existing PEFTs for personalised serving.

---


### 43. [Fusion-fission forecasts when AI will shift to undesirable behavior](https://arxiv.org/abs/2605.14218)

**<font color=#1a73e8>作者：</font>** Neil F. Johnson, Frank Yingjie Huo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The key problem facing ChatGPT-like AI's use across society is that its behavior can shift, unnoticed, from desirable to undesirable -- encouraging self-harm, extremist acts, financial losses, or costly medical and military mistakes -- and no one can yet predict when. Shifts persist in even the newest AI models despite remarkable progress in AI modeling, post-training alignment and safeguards. Here we show that a vector generalization of fusion-fission group dynamics observed in living and active-matter systems drives -- and can forecast -- future shifts in the AI's behavior. The shift condition, which is also derivable mathematically, results from group-level competition between the conversation-so-far (C) and the desirable (B) and undesirable (D) basin dynamics which can be estimated in advance for a given application. It is neither model-specific nor driven by stochastic sampling. We validate it across six independent tests, including: 90 percent correct across seven AI models spanning two orders of magnitude in parameter count (124M-12B); production-scale persistence across ten frontier chatbots; and a priori time-stamped prediction eleven months before the Stanford 'Delusional Spirals' corpus appeared, and independently confirmed by that corpus of 207,443 human-AI exchanges. Because it sits architecturally below the current safety stack, the same formula provides a real-time warning signal that current alignment does not supply, portable across current and future ChatGPT-like AI architectures and instantiable in application domains where competing response classes can be defined.

---


### 44. [Diagnosing Training Inference Mismatch in LLM Reinforcement Learning](https://arxiv.org/abs/2605.14220)

**<font color=#1a73e8>作者：</font>** Tianle Zhong, Neiwen Ling, Yifan Pi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM RL systems separate rollout generation from policy optimization. These two stages are expected to produce token probabilities that match exactly. However, implementation differences can make them assign different values to the same sequence under the same model weights, inducing Training-Inference Mismatch (TIM). TIM is difficult to inspect because it is entangled with off-policy drift and common stabilization mechanisms. In this work, we isolate TIM in a zero-mismatch diagnostic setting (VeXact), and show that small token-level numerical disagreements can independently cause training collapse. We further show that TIM changes the effective optimization problem, and identify a set of remedies that could mitigate TIM. Our results suggest that TIM is not benign numerical noise, but a systems-level perturbation that should be treated as a first-order factor in analyzing LLM RL stability.

---


### 45. [DT-Transformer: A Foundation Model for Disease Trajectory Prediction on a Real-world Health System](https://arxiv.org/abs/2605.14227)

**<font color=#1a73e8>作者：</font>** Yunying Zhu, Andrew R Weckstein, Kueiyu Joshua Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate disease trajectory prediction is critical for early intervention, resource allocation, and improving long-term outcomes. While electronic health records (EHRs) provide a rich longitudinal view of patient health in clinical environments, models trained on curated research cohorts may not reflect routine deployment settings, and those trained on single-hospital datasets capture only fragments of each patient's trajectory. This highlights the importance of leveraging large, multi-hospital health systems for training and validation to better reflect real-world clinical complexity. In this work, we develop DT-Transformer, a foundation model trained on 57.1M structured EHR entries over 1.7M patients from Mass General Brigham (MGB), spanning 11 hospitals and a broad network of outpatient clinics. DT-Transformer achieves strong discrimination in both held-out and prospective validation settings. Next-event prediction achieves a median age- and sex-stratified AUC of 0.871 across 896 disease categories, with all categories exceeding AUC 0.5. These results support health system-scale training as a path toward foundation models suited to real-world clinical forecasting.

---


### 46. [Latency-Quality Routing for Functionally Equivalent Tools in LLM Agents](https://arxiv.org/abs/2605.14241)

**<font color=#1a73e8>作者：</font>** Kexin Chu, Dawei Xiang, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents increasingly access the same tool type through multiple functionally equivalent providers, such as web-search APIs, retrievers, or LLM backends exposed behind a shared interface. This creates a provider-routing problem under runtime load: the router must choose among providers that differ in latency, reliability, and answer quality, often without gold labels at deployment time. We introduce LQM-ContextRoute, a contextual bandit router for same-function tool providers. Its key design is latency-quality matching: instead of letting low latency offset poor answers in an additive reward, the router ranks providers by expected answer quality per service cycle. It combines this capacity-aware score with query-specific quality estimation and LLM-as-judge feedback, allowing it to adapt online to both load changes and provider-quality differences. On the main web-search load benchmark, LQM-ContextRoute improves F1 by +2.18 pp over SW-UCB while staying on the latency-quality frontier. In a high-heterogeneity StrategyQA setting, LQM-ContextRoute avoids additive-reward collapse and improves accuracy by up to +18 pp over SW-UCB; on heterogeneous retriever pools, it improves NDCG by +2.91--+3.22 pp over SW-UCB. These results show that same-function tool routing benefits from treating latency as service capacity, especially when runtime pressure and provider-quality heterogeneity coexist.

---


### 47. [EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization](https://arxiv.org/abs/2605.14249)

**<font color=#1a73e8>作者：</font>** Zhiye Song, Kyungmi Lee, Eun Kyung Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization. As LLMs scale, predicting and reducing their energy footprint has become critical for sustainability and datacenter operations, yet existing approaches either require production-level code and expensive profiling or fail to accurately capture multi-GPU energy behavior. As a result, practitioners lack tools for deciding which optimizations to prioritize and for selecting among existing deployment configurations when exhaustive profiling is impractical. EnergyLens addresses this gap with an intuitive einsum-based interface that captures LLM specifications including fusion, parallelism, and compute-communication overlap, combined with load-imbalance-aware MoE modeling and an empirically driven communication energy model for multi-GPU settings. We validate EnergyLens on Llama3 and Qwen3-MoE across tensor-parallel and expert-parallel configurations, achieving mean absolute percentage errors (MAPEs) between 9.25% and 13.19% for multi-GPU prefill and decode energy, and 12.97% across SM allocations for Megatron-style overlap. Our energy-driven exploration reveals up to 1.47x and 52.9x energy variation across configurations in prefill and decode efficiency and motivates distributed serving. We further show that compute-communication overlap is difficult to optimize with intuition alone, but EnergyLens correctly identifies Pareto-optimal overlap configurations.

---


### 48. [Not All Timesteps Matter Equally: Selective Alignment Knowledge Distillation for Spiking Neural Networks](https://arxiv.org/abs/2605.14252)

**<font color=#1a73e8>作者：</font>** Kai Sun, Peibo Duan, Yongsheng Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs), which are brain-inspired and spike-driven, achieve high energy efficiency. However, a performance gap between SNNs and artificial neural networks (ANNs) still remains. Knowledge distillation (KD) is commonly adopted to improve SNN performance, but existing methods typically enforce uniform alignment across all timesteps, either from a teacher network or through inter-temporal self-distillation, implicitly assuming that per-timestep predictions should be treated equally. In practice, SNN predictions vary and evolve over time, and intermediate timesteps need not all be individually correct even when the final aggregated output is correct. Under such conditions, effective distillation should not force every timestep toward the same supervision target, but instead provide corrective guidance to erroneous timesteps while preserving useful temporal dynamics. To address this issue, we propose Selective Alignment Knowledge Distillation (SeAl-KD), which selectively aligns class-level and temporal knowledge by equalizing competing logits at erroneous timesteps and reweighting temporal alignment based on confidence and inter-timestep similarity. Extensive experiments on static image and neuromorphic event-based datasets demonstrate consistent improvements over existing distillation methods. The code is available at this https URL

---


### 49. [Hypergraph Enterprise Agentic Reasoner over Heterogeneous Business Systems](https://arxiv.org/abs/2605.14259)

**<font color=#1a73e8>作者：</font>** Ling Wang, Songnan Liu, Jianan Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Applying Large Language Models (LLMs) to heterogeneous enterprise systems is hindered by hallucinations and failures in multi-hop, n-ary reasoning. Existing paradigms (e.g., GraphRAG, NL2SQL) lack the semantic grounding and auditable execution required for these complex environments. We introduce HEAR, an enterprise agentic reasoner built on a Stratified Hypergraph Ontology. Its base Graph Layer virtualizes provenance-aware data interfaces, while the Hyperedge Layer encodes n-ary business rules and procedural protocols. Operating an evidence-driven reasoning loop, HEAR dynamically orchestrates ontology tools for structured multi-hop analysis without requiring LLM retraining. Evaluations on supply-chain tasks, including order fulfillment blockage root cause analysis (RCA), show HEAR achieves up to 94.7% accuracy. Crucially, HEAR demonstrates adaptive efficiency: utilizing procedural hyperedges to minimize token costs, while leveraging topological exploration for rigorous correctness on complex queries. By matching proprietary model performance with open-weight backbones and automating manual diagnostics, HEAR establishes a scalable, auditable foundation for enterprise intelligence.

---


### 50. [Agentic AI Ecosystems in Higher Education: A Perspective on AI Agents to Emerging Inclusive, Agentic Multi-Agent AI Framework for Learning, Teaching and Institutional Intelligence](https://arxiv.org/abs/2605.14266)

**<font color=#1a73e8>作者：</font>** Vidya K Sudarshan, Anushka Sisodia, Reshma A Ramachandra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integration of artificial intelligent (AI) agents in higher education is transforming teaching, learning and administrative processes. Although existing AI agents effectively support individual tasks, their implementation remains fragmented and inefficient for handling the complexity of educational institutions. This highlights a significant research gap: the lack of integrated eco-system-level agentic multi-agent AI platform capable of coordinated planning, reasoning, and adaptive decision-making across multiple educational functions. This paper presents a forward-looking perspective on agentic multi-agent AI platform in higher education, consisting interconnected autonomous, goal driven agents that support learning, teaching, and institutional operations. It addresses timely and critical questions: Can agentic AI represent the next generation of intelligent systems in tertiary education? Can they collectively support seamless coordinated operations across teaching, learning and administrative support? To what extent can such systems foster inclusive and equitable learning for diverse learners with special educational needs? To ground this perspective, a thematic analysis of existing literature identifies four dominant themes: task-specific fragmented AI tools, the transition from single-agent to multi-agent systems, limited cross-functional integration, and insufficient focus on inclusivity and accessibility. Findings reveal a clear gap between current AI implementations and the needs of holistic, learner-centered educational ecosystem. The paper synthesizes challenges and outlines future research directions for scalable human-aligned, and inclusive agentic AI platform. The significant contribution is the incorporation of inclusive learning perspectives, highlighting how coordinated agentic multi-agent platform can support diverse learners through adaptive, multimodal interventions.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-165](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
