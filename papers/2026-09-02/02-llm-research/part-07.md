# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 301. [Auditing MCQA Benchmarks through Probability Landscapes](https://arxiv.org/abs/2608.30372)

**<font color=#1a73e8>作者：</font>** Minsoo Song, Chanjun Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models rapidly advance, performance on standard multiple-choice question answering (MCQA) benchmarks is reaching saturation. While the community has responded by developing increasingly difficult datasets, validating question quality and filtering flawed items remains a labor-intensive process. To provide a scalable diagnostic approach, we propose a two-component probabilistic framework for auditing MCQA benchmarks using model output distributions. First, for benchmark-level analysis, we characterize the probability landscape using the top prediction probability ($P_{top1}$) and normalized residual entropy ($H_{norm}$), summarized globally by Mean Pairwise Distance (MPD). Second, for item-level diagnostics, we introduce noise injection to reduce meaningful distractor competition, enabling us to flag candidate items for targeted human review and categorize residual failure patterns. Across four MCQA benchmarks, our landscape analysis reveals benchmark-level differences in model confidence and residual option competition. Concurrently, our noise-injection method flags potentially actionable item-level issues, showing alignment with expert error annotations from MMLU-Redux. These results suggest that our probability-based framework provides a lightweight audit lens for comparing macro-level benchmark structure and prioritizing individual items for targeted human review.

---


### 302. [Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agent LLM Judges for Subjective Evaluation](https://arxiv.org/abs/2608.30373)

**<font color=#1a73e8>作者：</font>** Minsoo Song, Chanwoo Kim, Sugyeong Eo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Debate (MAD) has been widely adopted to improve LLM-based evaluation by prompting multiple agents to negotiate and reach a consensus. However, for subjective rubric-based scoring, inter-agent agreement does not guarantee alignment with human judgments. In this paper, we compare a single-judge baseline against a consensus-based MAD protocol on subjective evaluation tasks and design three ablations to isolate the impact of role prompting, multi-round interaction, and explicit score sharing. Evaluations across six LLMs show that the single-judge baseline achieves the strongest human alignment on average across six judge models, whereas MAD shows degradation in human alignment on both tasks. Our ablations demonstrate that this performance drop stems primarily from asymmetric role prompting rather than the interaction itself. Specifically, assigning a strict judge role introduces a systematic downward bias that the consensus process fails to correct. The central finding is that this bias reflects strict-stance dominance beyond averaging: the consensus score falls well beyond the arithmetic midpoint of the standalone strict and lenient conditions, rather than averaging them out. Removing role asymmetry (Symmetric MAD) largely recovers baseline performance, while masking peer scores widens inter-agent disagreement on average and worsens average human alignment. These findings demonstrate that multi-agent consensus can enforce artificial agreement at the expense of true human alignment, revealing a structural limitation in consensus-style, role-specialized MAD protocols for subjective scoring.

---


### 303. [DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving](https://arxiv.org/abs/2608.30386)

**<font color=#1a73e8>作者：</font>** Yanqi Yu, Pingwei Sun, Jianchao Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid linear-attention architectures have recently scaled to large open-weight models, offering quality competitive with full attention while substantially reducing key/value (KV) cache growth. However, their in-place recurrent-state updates complicate cache management: prefix reuse requires state checkpoints alongside full-attention KV, while storing state checkpoints in full increases memory pressure, leading to more evictions and repeated prefill. By analyzing the decay structure of Gated DeltaNet (GDN) and Kimi Delta Attention (KDA), we find that different heads and channels retain prefix information over markedly different timescales, which we term \emph{retention horizons}. This variation suggests substantial compression potential in persistent state checkpoints. Building on this observation, we introduce \emph{Decay-Aware State Compression} (DASC), which derives retention horizons from model weights, selects long-horizon state units, and packs them into a ragged state checkpoint layout. To integrate efficiently with tensor-parallel inference engines, DASC furtherly balances compressed state checkpoints across TP ranks. On reuse, DASC either zero-fills omitted units or refreshes them from a bounded suffix with additional compute cost. Across retrieval and end-to-end reasoning benchmarks on Kimi-Linear, conservative DASC configurations remain close to full caching while compressing KDA recurrent state checkpoints by $2.63\times$. Under fixed state checkpoint memory budgets, the resulting capacity gains reduce mean Time to First Token (TTFT) by 42.6\% and improve input throughput by 68.4\%. At larger compression ratio, suffix refresh recovers much of the accuracy lost to more aggressive omission, at the cost of additional replay computation. Qwen with GDN exhibits a similar quality--efficiency trend, showing that DASC extends from channel-wise KDA to head-wise GDN.

---


### 304. [Attesting Outputs and Delegation Ancestry in Multi-Agent AI Systems](https://arxiv.org/abs/2608.30387)

**<font color=#1a73e8>作者：</font>** Lifei Liu, Haoran Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent applications delegate work across independently operated deployers. After an incident, a verifier must answer two questions: which deployer released the reported bytes, and whether each cross-deployer edge was authorized. Credentials establish who may act, but need not bind them to later output bytes or prove both deployers authorized a dynamically created edge. We present a two-layer attestation design for dynamic delegation without a shared authority, public log, or precommitted workflow. A trusted deployer runtime signs a hash of each released output; this records released bytes but does not prevent prompt injection. Ancestry evidence records edge authorization. Under a unified threat model, we compare a signed linked list, a Merkle-chain variant, and a co-signed DAG. The primitives are standard; the contribution is deployer-side binding and the evidence needed for the two questions. After child-key compromise, the single-signer designs permit an unauthorized parent binding, whereas the co-signed DAG rejects it because the parent must authorize the edge. Fixed adversary matrices and regression tests validate the composed verifier. On an Apple M1 Pro, ancestry-only checks take 24.3-499.2us per hop. In a live local multi-service workflow, a parent discovers the child's A2A Agent Card; the child calls an MCP tool and releases local-LLM output: all 30 signed-DAG tasks passed complete verification, while a controlled child-key-only claim was rejected; its mean end-to-end latency was 813.1ms versus 770.8ms without evidence. In a complementary three-availability-zone AWS deployment, all 1,000 valid co-signed-DAG paths verified; issuance averaged 3.651ms and complete verification 5.015ms. The cloud result excludes TLS/mTLS, KMS, and model-serving latency.

---


### 305. [Using Grounded Theory for Agent Behavior Analysis at Scale](https://arxiv.org/abs/2608.30391)

**<font color=#1a73e8>作者：</font>** Zhuoran Lu, Yangyang Yu, Zhuoyan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding agent behavior requires methods that scale to thousands of trajectories and surface new patterns in long, often unfamiliar tasks where pre-built classifiers fall short. We propose to bring grounded theory into agent trajectory analysis: a six-decade-old qualitative method from the social sciences, with a principled saturation criterion and an auditable trail from data to theory. We propose AutoTraceGT (Automated Trace analysis through Grounded Theory), the first multi-agent pipeline that automates grounded theory on agent trajectories. It iteratively performs open, axial, and theoretical coding until saturation, producing a behavioral taxonomy tailored to each task. Across six trajectory corpora, AutoTraceGT produces codebooks that recover 73-91 percent of the failure modes in human-annotated taxonomies and surface additional patterns that those taxonomies miss. The emergent theoretical narrative aligns with prior expert accounts. Used as a deductive feature space, the codebook outperforms zero-shot and few-shot LLM baselines on downstream failure prediction. These results suggest Grounded Theory offers a scalable analytic tool for ML researchers and agent developers studying what agents actually do.

---


### 306. [Quantitative Evidence Mining for Plausibility-Aware Biomedical AI](https://arxiv.org/abs/2608.30393)

**<font color=#1a73e8>作者：</font>** Negin Sadat Babaiha, Stefan Geissler, Marie-Christine Simon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical artificial intelligence (AI) systems increasingly extract, organize, and reuse scientific claims from literature, clinical trials, and regulatory documents. But automatic extraction alone does not make a claim reliable evidence: a claim becomes useful only when it can be traced to its source, linked to the quantitative details that support it, and read within its biomedical context and uncertainty. This matters as large language models (LLMs) and increasingly autonomous systems drive evidence synthesis, knowledge graph (KG) construction, and decision support. Many text-mining and LLM pipelines remain relation-centric: they capture entities and relations such as Drug--TREATS--Disease, but drop the dose, effect size, population, comparator, uncertainty, and conditions under which a claim holds. Such relations can look actionable yet remain hard to verify, compare, or reuse. In this perspective, we argue for a shift toward quantitative evidence mining---extracting values, units, measured entities and properties, context, uncertainty, provenance, and plausibility as structured evidence units that populate evidence-aware KGs and can be checked for source grounding, unit consistency, completeness, and biological plausibility. We outline a framework for plausibility-aware AI that treats extracted claims not as final answers but as auditable evidence objects, making clear what was measured, how much it changed, in which setting, with what uncertainty, and from which source. The central risk is not only incorrect extraction, but claims that look like evidence while lacking the structure needed to trust them.

---


### 307. [When LLM Meets Tree Search: A Systematic View of Inference as Search in Large Language Models](https://arxiv.org/abs/2608.30395)

**<font color=#1a73e8>作者：</font>** Jiaqi Wei, Xiang Zhang, Yuejin Yang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As pretraining scaling laws approach saturation, Test-Time Scaling (TTS) has emerged as an important direction for improving reasoning by allocating inference-time compute to a fixed model prior. Viewed at a high level, TTS reframes inference as search over a space of partial reasoning states. While Chain-of-Thought (CoT) exposes intermediate steps, common instantiations rely on single-trajectory decoding, limiting recovery from early errors and exploration. This survey systematizes recent progress in tree-search-based reasoning, viewing inference as instance-specific optimization rather than decoding. We trace the evolution from uninformed search to Monte Carlo Tree Search (MCTS), highlighting how sampling-based control supports principled exploration-exploitation trade-offs. To unify a fragmented literature, we introduce a Unified Design Space spanning search topology, evaluation signals, and control dynamics, and advocate a standardized compute-reporting abstraction to make compute-accuracy trade-offs explicit and comparable.

---


### 308. [Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation](https://arxiv.org/abs/2608.30396)

**<font color=#1a73e8>作者：</font>** Zixing Lei, Gengze Zhou, Xiong-Hui Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon physical-world agents must reason over distant goals while grounding decisions in reliable closed-loop behavior. Today's foundation models split these capabilities: vision-language models (VLMs) infer missing information and adapt high-level plans but remain brittle and inefficient at repeated navigation grounding, while navigation foundation models (NFMs) robustly execute semantic goals but operate as bounded episodes without persistent task-level reasoning. We introduce NavMCP, an agentic scaffolding framework that couples a VLM reasoning agent with an NFM executor for long-horizon exploration. The VLM decides what evidence to seek, where to search, and when to stop, while the NFM grounds each semantic sub-goal into closed-loop navigation. Three channels structure their collaboration: intent translates evidence needs into navigation calls, observation converts rollouts into source-grounded trajectory evidence, and memory accumulates findings, negative evidence, and unresolved goals across calls. This design turns isolated navigation rollouts into persistent embodied interaction without retraining either model. On Embodied Question Answering, NavMCP achieves state-of-the-art results on HM-EQA, MT-HM3D, and EXPRESS-Bench. Under matched agent and executor backbones, it outperforms an episodic interface by 14.9 percentage points on HM-EQA. On a Unitree Go2, NavMCP reaches 78.3% success, with its margin over the strongest baseline growing from 10 to 45 points as the task horizon increases. These results demonstrate the potential of scaffolding complementary foundation models into long-horizon physical-world agents.

---


### 309. [Beyond Polarization: The Generative Constraint of Chain-of-Thought in Pointwise Reranking](https://arxiv.org/abs/2608.30398)

**<font color=#1a73e8>作者：</font>** Xiaoyang Chen, Jie Liu, Haijin Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In pointwise document reranking, Chain-of-Thought models typically underperform direct scoring models. While existing diagnostics attribute this to inferior classification, score polarization, or calibration breakdown, whether targeted training can bridge this gap remains unclear. Our empirical study first confirms that this gap is stable across scales up to 32B parameters, ruling out model and data capacity confounders. We then apply stress tests utilizing reinforcement learning, fine-grained supervision, and architectural decoupling to explicitly repair these deviations. Although these interventions improve classification accuracy and absolute scores, the relative ranking gap persists. These findings suggest that, within the pointwise scoring paradigm, routing continuous relevance semantics through discrete text constrains ranking signal resolution, revealing a bottleneck that is stable and difficult to overcome under current standard methods, rather than an easily resolvable training bias.

---


### 310. [SemPOI-RL: Aligning LLM Semantic Reasoning for Interpretable Out-of-Town POI Sequential Generation](https://arxiv.org/abs/2608.30399)

**<font color=#1a73e8>作者：</font>** Yunqi Liu, Yang Zhang, Ruixing Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong semantic reasoning and open-ended generation abilities, but aligning these abilities with structured sequential generation remains challenging. This challenge is particularly evident in out-of-town (OOT) POI sequence generation, where a model must infer transferable travel intent from a user's hometown behaviors, adapt to cross-city interest drift, and generate a coherent destination trajectory under structural constraints. Existing approaches either rely on latent ID-based transfer with limited interpretability or directly use LLMs for sequence generation without explicitly grounding inferred semantics into position-aware predictions. To address this gap, we propose SemPOI-RL, a framework that aligns LLM semantic reasoning with structured sequence generation for interpretable OOT recommendation. Specifically, we first fine-tune an LLM to infer destination-oriented travel styles from users' hometown trajectories, using natural language as an interpretable semantic intermediate. We then introduce a Semantic POI Alignment Module (SPAM) to ground these inferred styles into a style-conditioned masked autoencoder for position-aware trajectory generation. Finally, we apply reinforcement learning with recommendation-oriented rewards to align LLM-generated styles with downstream sequence quality. Experiments on two real-world datasets show that SemPOI-RL consistently outperforms both traditional recommenders and direct LLM baselines, while providing interpretable style attribution across different phases of a trip. The code is available at this https URL .

---


### 311. [Dense Clinical Contrasts Enhance Medical Knowledge Updating in Large Language Models](https://arxiv.org/abs/2608.30405)

**<font color=#1a73e8>作者：</font>** Yangmin Huang, Shu Quan, He Geng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical knowledge changes continually, making large language models vulnerable to relying on outdated yet clinically plausible information. We study whether the format of supervision affects medical knowledge updating under a matched training-budget setting. We introduce SEER-Bench, a temporally anchored oncology-staging benchmark curated from the latest versioned SEER Research Data release, and render identical medical update events from NCCN oncology guidelines into four supervision formats: EMQ, MSQ, FITB, and SAQ. Across SEER-Bench and HealthBench Professional, EMQ gives the most stable external transfer and retention among same-budget SFT variants. With EMQ supervision, the updated 4B model produces competitive results on temporally anchored oncology staging, reaching 64.8% answer accuracy and 59.6% rationale accuracy on SEER-Bench. Diagnostic analyses suggest that EMQ exposes denser clinical contrast signals while preserving discriminative representations with smaller movement from the base model. These results show that medical knowledge updating depends not only on the update algorithm, but also on how knowledge is structured as supervision.

---


### 312. [DERELAB: Probing Defeasible Reasoning and Confirmation Bias in LLMs with a Generative Benchmark](https://arxiv.org/abs/2608.30413)

**<font color=#1a73e8>作者：</font>** Jayanta Sadhu, Sayem Shahad, Kenneth Marino  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Defeasible reasoning is a type of reasoning where inferences are drawn from plausible current evidence, but can be retracted upon the introduction of newer evidence. Although recent studies have examined language-model behaviors in defeasible reasoning, the datasets have been static and lack wide coverage of non-monotonic reasoning categories. We introduce DeReLab, a generative framework that produces multi-turn belief-updating conversations from parameterized graph structures across default and inheritance reasoning, with formally verified ground truth at every turn, enabling controlled measurement of how models respond to confirming and disconfirming evidence. This controlled generation process creates a testbed for experimental designs that isolate specific reasoning demands. Applying this capability to the study of confirmation bias, we evaluate nine open and proprietary large language models and find that nearly all exhibit a systematic tendency to accept congruent evidence while resisting incongruent updates, with several models correctly identifying a weakening update yet failing to revise their conclusion. We believe our work and findings will facilitate future research on evaluating language models in defeasible reasoning.

---


### 313. [Whole-Slide Image Analysis under Realistic Few-Shot Annotation Protocols](https://arxiv.org/abs/2608.30420)

**<font color=#1a73e8>作者：</font>** Tiffanie Godelaine, Maxime Zanella, Karim El Khoury 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating the analysis of whole-slide images has high clinical value, since characterizing cancers requires examining them in detail. Such analysis increasingly relies on vision-language models that provide patch-level zero-shot predictions. However, these predictions remain noisy and must be refined with a few annotations. A promising paradigm for this refinement is few-shot transduction. Rather than treating each patch independently, these methods leverage the relations between patches, together with a few annotations, to refine all predictions jointly. However, current transductive methods are evaluated under conditions that overlook key properties of whole-slide images: (i) datasets consist of independent patches extracted from multiple slides, ignoring the complex tissue organization; (ii) datasets are mostly balanced, whereas a single whole-slide image exhibits severe class imbalance, with several classes absent; and (iii) annotations are sampled at random, without reflecting how a pathologist annotates a limited number of regions. To align the transduction paradigm to realistic whole-slide settings, we introduce the following contributions. First, we propose SlideCRF, which adapts conditional random fields for whole-slide images by combining spatial and biological cues while accounting for classes that may be absent from a given slide. Second, we provide a set of realistic annotation protocols, based on spatially localized clicks and scribbles, modeling different pathologist interactions, such as the iterative correction of model errors. Across four datasets, we show that SlideCRF outperforms current transductive methods in macro F1, improving over the zero-shot predictions by +24.2% and +37.5% with one and 16 clicks per present class, respectively.

---


### 314. [Towards Cognitive Process-Aware Proactive Writing Support](https://arxiv.org/abs/2608.30424)

**<font color=#1a73e8>作者：</font>** Masahiro Yoshida, Atsuya Kobayashi, Kei Tateno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models can support writing, but existing tools require users to explicitly articulate prompts-particularly burdensome in creative writing, where intentions are often ambiguous. Proactive support that infers users' needs from writing interactions could alleviate this burden, but raises two challenges: determining what support to provide and when to intervene. This work focuses on the former. We hypothesize that Flower and Hayes' cognitive process theory of writing-which characterizes writing through six cognitive processes-offers an interpretable bridge between observable writing behavior and appropriate support types. Through a formative study and literature review, we identify 14 writing support types associated with these cognitive processes, along with characteristic interaction behaviors linked to each process. We then instantiate this framework in AToM CoWriter, which infers support needs from writing interactions and document context. Two within-subjects studies (N = 21) provide initial evidence that this approach improves expressiveness and idea exploration, and that cognitive process inference increases engagement with proactive suggestions. These findings suggest that cognitive processes can provide a promising basis for support selection in proactive writing systems.

---


### 315. [Learning to Reason and Use Tools through Unsupervised Fine-Tuning in Task-Oriented Dialog Systems](https://arxiv.org/abs/2608.30426)

**<font color=#1a73e8>作者：</font>** Markel Ferro, Oier Lopez de Lacalle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current dialogue systems struggle with dynamic information retrieval, often leading to hallucinations and lower response accuracy. We address this by adapting the ReAct framework for Task-Oriented Dialogue, enabling Large Language Models (LLMs) to access external knowledge and produce factual responses. Mainly, we propose an unsupervised fine-tuning pipeline that harvests reasoning trajectories via in-context learning inference. High-quality samples are filtered using an LLM-based judge to construct a robust training set. This is enhanced by a unsupervised self-improvement loop, where improved checkpoints generate increasingly better trajectories for subsequent fine-tuning iterations. Experiments on the SIMMC dataset demonstrate that ReAct-based systems outperform baselines due to superior reasoning and tool use. Notably, our fine-tuned 8B model surpasses a 70B in-context system. Finally, we present an error analysis, impact of scene complexity, and cross-domain generalization.

---


### 316. [Ceiling-Clipped Acceptance Histograms Indicate Stranded Speed-up in Block-Diffusion Speculative Decoding](https://arxiv.org/abs/2608.30427)

**<font color=#1a73e8>作者：</font>** Ephrem Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding speeds up generation with an efficient draft model (drafter) that proposes tokens for a target model to verify in one pass, preserving the target's output distribution. High-acceptance block-diffusion drafters such as DFlash and DFlare fill an entire block in one parallel pass. In many cycles, the target accepts the whole block, so the drafter exhausts its trained block horizon before verification fails. We call this unrealized acceptance stranded speed-up. A mean committed length, per prompt or per cycle, hides it, whereas the acceptance histogram exposes it as a spike in the ceiling bin, the fraction of cycles that accept the entire block. We recommend the histogram as a preflight check before spending training compute. Naively widening the block at inference does not recover the speed-up, because once the block outgrows its training size, the drafter's bidirectional attention shifts its distribution even at early positions and erodes front-of-block verification. Instead, we post-train the drafter on a longer block with a short curriculum that emphasizes the newly exposed positions, a method we call DBloom. Expanding the pretrained DFlash and DFlare drafters from block size 16 to 24 across Qwen3-8B and Qwen3-4B targets raises the per-prompt committed length on the high-ceiling benchmarks by a median of +0.8 tokens (up to +1.1). Once continuation fine-tuning precedes expansion, the increase reaches 1.37 tokens. The same expansion also lifts committed length on all seven benchmarks for Gemma-4-12B-IT, a different model family, by a median of +0.41 tokens (Arm A), and the full continuation-then-expand pipeline (Arm B) adds +0.29 to +0.98 tokens over the same B16 drafter. In a prompt-matched comparison against JetSpec, a contemporary tree-based drafter not used in our design, DBloom commits more tokens on every benchmark at tree budgets up to 64 nodes.

---


### 317. [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions](https://arxiv.org/abs/2608.30428)

**<font color=#1a73e8>作者：</font>** Jaewoo Ahn, Junseo Kim, Hyunseo Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Strategic deception by LLM and VLM agents has emerged as a central AI alignment and safety concern. Social-deduction games (where each player holds a hidden role and communicates with others to deduce identities) serve as the canonical testbed, particularly in multi-agent settings. Existing testbeds, however, are text-only and run on a single fixed agent configuration, missing the non-verbal sensorimotor channels treated as core by deception taxonomies and leaving it ambiguous whether an observed behavior reflects the underlying model or the surrounding harness. We introduce MineAmongUs, a 3D multimodal Among Us sandbox where imposter agents must deceive crewmates through joint verbal and non-verbal action. We also propose ARIA, a configurable VLM-agent harness that exposes five cognitive-component ablation axes; and an atom- and arc-level annotation scheme grounded in deception taxonomies and operationalized at scale by an LLM-as-a-Judge reaching near-human atom-labeling agreement. Empirical results show that VLM agents pursue imposter wins through joint verbal and non-verbal deception, with non-verbal channels emerging as the more decisive winning contributors across both harness ablation and cross-VLM evaluation. Taken together, our work opens a new path for embodied VLM-agent alignment research.

---


### 318. [Graph Evidence Is Not Enough: Diagnosing Native Decoder Use in Graph-Augmented LLMs](https://arxiv.org/abs/2608.30437)

**<font color=#1a73e8>作者：</font>** Xiaoyu Guo, Pengcheng Chen, Jiong Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-augmented large language models often assume that graph evidence produced by external computation and placed in the input can be used by the native decoder. We test this assumption with HopQA, a deliberately bounded diagnostic that asks for the shortest-hop distance between two query nodes. Because the answer is a small integer and the target is purely topological, failure cannot be dismissed as open-ended generation or ambiguous evaluation. Yet existing graph-augmented baselines still fail on this setting, showing that providing graph evidence is not the same as making it usable. We introduce an intervention triangle with three matched conditions: readable graph evidence, shuffled graph evidence, and no-graph input. This separates evidence inclusion, structural readability, and decoder-usable topology. Guided by this diagnosis, we present S$^2$GE as an instance showing that diagnosis-driven interface design can improve native decoder usability. S$^2$GE uses query-aware sampling, endpoint and proximity-based ordering, and structure-preserving alignment. Across DBLP, Biomedical, GoodReads, and PubMed, S$^2$GE achieves strict exact-match scores of $36.5\%$, $57.8\%$, $76.6\%$, and $52.0\%$, improving over the strongest native-generation baseline by $53.5$ points on average. The interventions further reveal harmful-shuffle, shuffle-robust, and no-graph-saturated regimes.

---


### 319. [Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal Geometry](https://arxiv.org/abs/2608.30457)

**<font color=#1a73e8>作者：</font>** Jiani Guo, Junjie Wang, Jie Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal geometry reasoning requires VLMs to extract precise visual relations and preserve them through multi-step deduction. Existing free-form traces obscure the decisions that determine the answer, and trajectory-level reinforcement learning distributes a single terminal signal across the entire response. We introduce credit-addressable reasoning, in which the semantic units exposed during inference also define where learning compares alternatives and assigns credit. We instantiate this principle with Code-CoT, which retains the diagram, represents visual relations as line-addressable executable code, and organizes reasoning into typed events, and CE-GRPO, which selects event boundaries using structural priors and type-normalized entropy, samples complete continuations from shared prefixes, and converts outcome differences into localized advantages. Across nine geometry benchmarks, CE-GRPO achieves an average accuracy of 76.04, outperforming Qwen3-VL-8B and trajectory-level GRPO by $8.09$ and 3.43 points, respectively. Its relative advantage increases with the number of intermediate events, demonstrating the value of representation--optimization co-design for long, dependency-heavy multimodal reasoning.

---


### 320. [From Final Artifacts to Trajectories: Retrospective Process Supervision for Evidence-Grounded Long-Form Generation](https://arxiv.org/abs/2608.30461)

**<font color=#1a73e8>作者：</font>** Junjie Huang, Jiarui Qin, Di Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Trajectory data is getting more vital for training large language models for boosting the agentic abilities. Unlike the verifiable domains such as coding or mathematics, scaling trajectory data for open-ended tasks is much more difficult because these tasks lack singular ground truth and are costly to annotate or verify. In this paper, we propose RetroGen, a self-improving framework of retrospective process supervision. Our key observation is that although expert trajectories are scarce, high-quality final artifacts such as literature reviews, analyst reports and legal judgments, are abundant in pre-training data and can be viewed as compressed traces of the evidence-seeking processes that produced them. RetroGen reconstructs candidate latent trajectories from expert artifacts, verifies them against both the artifact and supporting evidence, and trains models on their own successful reconstruction data, without requiring trajectory data from stronger models. Experiments show that RetroGen improves grounding, faithful synthesis, and long-form evidence-seeking agent tasks.

---


### 321. [Enhancing Low-Resource Language Reasoning via High-Resource Language Feature Transfer](https://arxiv.org/abs/2608.30462)

**<font color=#1a73e8>作者：</font>** Minju Song, Hyeon Hwang, Junhyun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit substantial performance variation across languages, even when solving semantically equivalent tasks. Existing analyses often treat this phenomenon as an observational disparity caused by differences in pretraining data, tokenization, or benchmark coverage. We study a complementary hypothesis: high-resource languages (HRLs) may more reliably elicit latent computations useful for task-specific (i.e. mathematical) reasoning, while lower-resource languages (LRLs) may under-activate those computations despite expressing the same task. To test this hypothesis, we introduce a mechanistic intervention framework for identifying and transferring task-relevant sparse latent features across languages. Using sparse autoencoders over residual-stream activations, we isolate features enriched in successful HRL task-specific reasoning while filtering out source-language and generic-generation features. We then construct steering directions from these features and inject them during LRL inference. The resulting interventions test whether the selected features are functionally involved in the observed reasoning gap: suppressing them should impair source-language reasoning, while activating them should partially recover target-language reasoning beyond random and non-task controls. Our framework reframes some cross-lingual reasoning gaps as failures of mechanism elicitation rather than capability absence, and offers a causally testable route to feature-mediated transfer without translation, fine-tuning, or changing the user-facing language.

---


### 322. [More Capable, Less Faithful: A Multilingual Analysis of Mathematical (Un)Solvability Detection in LLMs](https://arxiv.org/abs/2608.30463)

**<font color=#1a73e8>作者：</font>** Maria-Eleni Zoumpoulidi, Nikolaos Xiros, Georgios Paraskevopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Solvability detection is one of the most challenging aspects of mathematical reasoning for Large Language Models (LLMs). While prior work has studied this capability extensively, these analyses have been limited to English. Consequently, it remains unclear whether multilingual failures arise from differences in internal Solvability Belief or from language-dependent failures to express it. To address this gap, we introduce the first multilingual benchmark of paired solvable and unsolvable mathematical problems, extending ReliableMath to French and Greek. Using this, we train multilingual probes predicting Solvability Belief and analyze the solvability detection capabilities of state-of-the-art LLMs behaviorally, representationally, and in terms of faithfulness. We find that Solvability Belief is encoded as a largely universal, language-agnostic feature, and that higher-resource languages such as English, despite achieving stronger mathematical reasoning performance, exhibit lower solvability-detection faithfulness.

---


### 323. [CHASE: How Content Ecosystems Are Reshaped When Ranking Is the Only Target](https://arxiv.org/abs/2608.30466)

**<font color=#1a73e8>作者：</font>** Qianwen Gao, Zichang Su, Yiwen Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative Engine Optimization (GEO) is increasingly used to improve content visibility in LLM-based retrieval systems, yet its population-level effects under repeated optimization remain poorly understood. We introduce Content Homogenization under rAnking Signal Exploitation (CHASE), a controlled simulation framework for studying how content ecosystems are reshaped when creators repeatedly adapt documents to an LLM ranking signal. We use ranking as a proxy for source visibility and validate this abstraction against citations in grounded generated responses, obtaining a rank-citation AUC of 0.853 $\pm$ 0.093 across six domains. CHASE then iterates ranking, feature discrimination, rewriting, and evaluation over 20 rounds across different domains. Quality-ranking alignment decreases in all six domains: from R0 to R20, the change in Spearman's rho ranges from -0.107 to -0.018, with a mean change of -0.068, which means documents closer to the ranking feature profile become less aligned with independently judged document quality over the simulation horizon. A random-target control has shown that it is associated with adaptation toward ranking-derived incentives rather than iterative rewriting alone. The resulting ecosystem dynamics are strongly domain-dependent. Together, these findings show how repeated optimization against a fixed LLM ranking signal can reshape both content populations and the incentives faced by content creators.

---


### 324. [ImageEval 2026: Culturally Grounded Arabic Multimodal Evaluation](https://arxiv.org/abs/2608.30475)

**<font color=#1a73e8>作者：</font>** Samir Abdaljalil, Hunzalah Hassan Bhatti, Ahlam Bashiti 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an overview of the ImageEval 2026 shared task on culturally grounded Arabic multimodal evaluation. It includes two tasks: (i) AynVQA, covering spoken visual question answering and image-grounded hallucination detection in English and Modern Standard Arabic (MSA), and (ii) CRAI-Bench, evaluating the cultural accuracy of text-to-image generation. A total of 14 teams participated in the test phase, with 12 teams submitting system description papers. Participating systems used a range of approaches, including zero-shot prompting, fine-tuning of vision-language models, speech-recognition pipelines, ensembling, and score calibration. We describe the task setup, datasets, evaluation procedure, and participating systems, and summarize the main results across the different tracks. All datasets and evaluation scripts from the shared task are released to the research community. The shared task highlights the challenges of culturally grounded multimodal evaluation, particularly for Arabic speech and image-text reasoning.

---


### 325. [Agents in the Large: Perception-Centered Architecture for Persistent Agents](https://arxiv.org/abs/2608.30478)

**<font color=#1a73e8>作者：</font>** Shihan Dou, Haoxiang Jia, Shichun Liu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive language agents have achieved substantial progress by equipping language models with memory, tools, and decision-making procedures, enabling agents to reason and act in interactive environments. Existing frameworks largely cast these agents as systems for solving user-specified, bounded tasks. An increasingly important goal is for language agents to provide persistent assistance in long-lived settings where user needs, context, and service procedures persist and change, and to remain useful across the broad range of tasks that arise over time. Yet we still lack a framework to characterize persistent AI agents, organize existing work, and guide future development. To this end, we propose a Perception-Centered Architecture for Persistent Agents (Pera). Pera describes a persistent agent organized around perception and control components that continually perceive service-relevant signals from episodic task executions, internal context, and changes in the surrounding environment, and use these signals to construct lifecycle tasks. These tasks drive the ongoing operation and adaptation of the agent's service procedures. We use Pera to retrospectively organize recent work, examine a detailed case study, and offer forward-looking insights for building more capable persistent agents. Just as software engineering moved from programming in the small to programming in the large, Pera frames the evolution of language agents as an analogous architectural transition toward long-lived, adaptive intelligence systems.

---


### 326. [VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs](https://arxiv.org/abs/2608.30480)

**<font color=#1a73e8>作者：</font>** Afsaneh Hasanebrahimi, Hanxun Huang, Christopher Leckie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object hallucination remains a persistent reliability issue in large vision-language models, where generated object mentions may sound plausible but lack visual grounding. Recent training-free detectors use internal signals such as token likelihood, attention, visual confidence, or image-text similarity to identify hallucinated objects. These signals are useful, but they are often source-confounded. They measure how strongly an object is supported inside the model without distinguishing whether that support comes from object-specific visual evidence or the generated text prefix. In difficult cases, a hallucinated object can still receive high internal support because it fits the scene, is associated with nearby visual cues, or follows naturally from the generated text prefix. We propose VisER, a training-free two-sided metric for object-level hallucination detection. VisER evaluates each generated object mention from two complementary views. Visual Evidence measures whether object-context compatibility is backed by object-specific evidence from image tokens. Visual Reliance measures whether the object is supported more by the image than by the generated prefix. Combining these views gives a more source-aware grounding score, while avoiding additional object-level verification generations. Across multiple LVLMs and benchmarks, VisER improves AUROC and AUPR over a range of baselines.

---


### 327. [Two Centuries of Sexism in British Parliament: A Computational Analysis of Women's Representation in the Hansard Corpus](https://arxiv.org/abs/2608.30485)

**<font color=#1a73e8>作者：</font>** Mohammad Omar Khursheed, Mandira Sawkar, Ashiqur R. KhudaBukhsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The language a legislature uses to debate women's rights, even in favour of them, encodes systematic patterns of sexism that persist across two centuries. In this work, we analyse 6,531 speeches over 200 years of UK parliamentary debate (Hansard, 1803-2005) by using large language models to classify a speaker's perspective towards women's suffrage and political representation, as well as analyse sexist speech in parliament from the lens of the Ambivalent Sexism Inventory. We also release this parliamentary dataset, an organized and metadata-enriched version of the publicly available Hansard Corpus optimized for computational social science research, with 6.7 million speeches across 1.2 million debates, with 89% gender-matching for speeches by MPs from the House of Commons. We find that 54% of speeches opposing women's representation contain sexist content, compared to 21% of speeches that are for the cause, and that the two sides use fundamentally different types of sexism: anti-suffrage rhetoric combines hostile and benevolent framing, while pro-suffrage sexism is overwhelmingly benevolent. Female MPs support women's political rights at 93% compared to 70% for male MPs, a gap that closes only after enfranchisement. Our findings are evidence that benevolent and hostile sexism are used in different rhetorical contexts in a manner consistent with the theory of Ambivalent Sexism.

---


### 328. [CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent Framework](https://arxiv.org/abs/2608.30498)

**<font color=#1a73e8>作者：</font>** Qi Li, Zhaojie Kang, Yingjie He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown remarkable success in STEM domains, where progress is often driven by vertical, step-by-step deduction under relatively stable symbol systems. Their horizontal, interdisciplinary cultural reasoning, however, remains this http URL propose CM2, a multi-agent framework grounded in the cognitive pathway of human cultural interpretation. CM2 integrates multimodal perception, retrieval-augmented generation, networked reasoning, gated fusion, and reward-driven this http URL on CM2D across multiple MLLM backbones show consistent gains over CoT and typical reasoning paradigms; ablations validate each module's contribution, and conflict analyses confirm genuine cross-modal arbitration.

---


### 329. [Tensor Methods for Language Models: From Token Representation to Training, Adaptation, Inference, Compression, and Interpretability](https://arxiv.org/abs/2608.30505)

**<font color=#1a73e8>作者：</font>** Matvei Tarasov, Salman Ahmadi-Asl, Andre L. F. de Almeida 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are built from structured high-dimensional objects such as token representations, weights, adaptation updates, caches, and activations, whose multilinear structure is underexploited by the conventional matrix-centric view. Tensor decompositions and tensor networks provide a principled algebraic language for this structure, yet the literature often treats them as isolated compression mechanisms. This survey organizes tensor methods for LLMs through two complementary views: a seven-stage lifecycle taxonomy covering tokenization, embeddings, pre-training, adaptation, compression, inference, and interpretability, and a component view covering embeddings, attention, and feed-forward networks. We provide unified notation and theoretical foundations, analyze tensorization strategies for individual Transformer components, and compare methods at each lifecycle stage while making differences in evaluation protocols and model scales explicit. We further connect tensor methods to neighboring efficiency techniques and probabilistic tensor networks. Finally, we synthesize open challenges and introduce $\rho_{\rm gap}$, a metric for the compression-realization gap between theoretical memory reduction and measured system-level speedup. By treating tensorization as a common structural principle, the survey provides a structured entry point to tensorized language models and clarifies when parameter savings can plausibly translate into memory efficiency, computational efficiency, or interpretability. The GitHub page dedicated to this paper is accessible at \href{this https URL}{this https URL}.

---


### 330. [Lot Machine: Multimodal Lot Extraction from Auction Catalogs](https://arxiv.org/abs/2608.30510)

**<font color=#1a73e8>作者：</font>** Mathias Zinnen, Alisha Mund, Sabine Lang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For provenance research and art market studies, auction catalogs are an essential resource to trace specific objects over time and space. While historical auction catalogs follow established domain conventions, their internal formatting remains highly variable, and their large-scale analysis is currently restricted by the lack of machine-readable representations of the auction lots. We propose a pipeline to automatically extract structured lot-level metadata from German Sales, a large database of historical auction and sales catalogs from the 19th and 20th centuries. Using a manually annotated test set of representative catalog pages, we evaluate Vision-Language Models (VLMs) under varying prompt strategies and constrained decoding frameworks. To reflect the practical constraints faced by cultural heritage institutions, including budget, compute resources, and data privacy requirements, we benchmark the methods across different deployment modes ranging from commercial providers to locally hosted, quantized models. We find that commercial endpoints establish the performance ceiling, while institutional gateways offer a viable, privacy-preserving alternative. Local deployments remain feasible, but strictly require enforcing the output structure during generation to guarantee a valid JSON format. While varying degrees of human-in-the-loop correction are still necessary, this work demonstrates that a VLM-based pipeline can successfully unlock historical auction catalogs for large-scale automated analysis.

---


### 331. [ScienceArena: Benchmarking LLMs on Latest Scientific Olympiad Competitions](https://arxiv.org/abs/2608.30517)

**<font color=#1a73e8>作者：</font>** Guangxiang Zhao, Qilong Shi, Xusen Xiao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark saturation and data contamination increasingly obscure genuine scientific reasoning in frontier LLMs. We introduce \textsc{ScienceArena}, an olympiad-style benchmark from thirteen public science competitions in physics, chemistry, and biology, including IPhO and IChO 2025--2026, IBO 2023, USAPhO 2026, and USNCO 2025. Its open-ended, multi-step problems use process-credit rubrics, making faithful scoring difficult. We build ScienceArena through an expert-audited digitization pipeline that converts official exams, figures, solutions, and rubrics into structured items verified by olympiad medalists. To scale evaluation beyond costly human grading, we calibrate LLM-as-judge against medalist ground truth on archived answers from five models across IPhO and IChO; two strong judges stay within one point of expert total scores. Medalist notes show that failures often stem from visual grounding, structure fidelity, and global problem control rather than missing terminology. Evaluating fourteen recent LLMs with interleaved solving, we find that top models obtain medal-equivalent rubric scores on several public international exams, while chemistry and long-horizon consistency remain key bottlenecks. We provide an interactive \href{this https URL}{demo}.

---


### 332. [PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs](https://arxiv.org/abs/2608.30528)

**<font color=#1a73e8>作者：</font>** Yuanqiang Yu, Yanzhao Zheng, Zhentao Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is used to improve the reasoning abilities of LLMs, while training data span heterogeneous tasks. However, most RL post-training pipelines rely on fixed or manually designed task mixtures, even though task usefulness changes as training progresses. Online curriculum methods often define learnability by update magnitude, ignoring whether the update translates into reward gains, which can misallocate rollout budget toward tasks with large but ineffective updates. We propose PAC, a Progress-Augmented Advantage Curriculum for multi-task RL of LLMs that combines two task-level signals: advantage-derived learnability, which measures the magnitude of the policy update a task can induce, and recent reward gains, which show whether those updates have improved task performance. A Bayesian Thompson Sampling controller uses these signals to allocate rollouts across tasks during GRPO training. We evaluate PAC under two settings: a multi-level reasoning setting and a multi-domain reasoning setting. PAC improves sample efficiency and final performance: it reaches comparable validation scores with fewer rollout steps and achieves higher final averages than random sampling and advantage-based curriculum baselines in both settings. These results show that jointly tracking advantage signals and actual reward gains yields an effective online curriculum for LLM post-training.

---


### 333. [WebWorld: The Browser as a World Model for Self-Improving Web Code](https://arxiv.org/abs/2608.30530)

**<font color=#1a73e8>作者：</font>** Jiajun Wu, Jian Yang, Yaxin Du 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> VLM-driven self-improvement of web code has a structural flaw: the model that proposes the repair is the model that judges it, and visual plausibility under that judge is a poor proxy for whether the page actually works. What the loop is missing is a counterparty the VLM cannot fool, and the browser already is that counterparty: a deterministic, executable simulator of how an HTML artifact behaves under user actions, and in everything but name a world model for web code. We present WebWorld, the interface that lets a VLM prior interact with this browser-as-world-model autonomously and decides which interactions become supervision. Each round, the VLM emits a critique that the planner compiles into a typed interaction contract; the browser re-executes the candidate and issues an acceptance certificate only when both target progress and preservation of every previously verified capability hold; certified transitions accumulate as a quality ratchet that is the only thing the SFT export ever sees. Under matched training, WebWorld-27B improves Raw-27B by 5.3 points on HTMLBench-400 and 14.9 points on MiniAppBench-Val, and reaches the level of strong frontier systems such as Kimi-K2.6 and GPT-5.4 on interactive HTML generation. Equal-size ablations show that browser-backed admission carries the gain: without the certificate, the matched 9B lift nearly disappears.

---


### 334. [DiffPDE: Masked Diffusion Language Models as PDE Solver](https://arxiv.org/abs/2608.30532)

**<font color=#1a73e8>作者：</font>** Wenxuan Guo, Yuyang Hong, Lubin Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing approaches for synthesizing Partial Differential Equation (PDE) solvers predominantly rely on autoregressive models, yet their global left-to-right decoding incurs substantial redundancy when addressing inherently localized bugs. In this work, we challenge this inefficient paradigm and propose DiffPDE, a framework leveraging discrete diffusion language models for targeted code repair. By introducing a localized re-masking and infilling strategy, DiffPDE regenerates only erroneous regions while preserving correct context, naturally aligning generation with the sparse nature of PDE errors. Furthermore, to handle coupled bugs requiring sequential interventions, we present Iterative Debugging GRPO (ID-GRPO), a reinforcement learning scheme that enables multi-round debugging within single trajectories via intermediate rewards. Experiments on PDEBench show that DiffPDE achieves competitive accuracy, outperforms same-scale AR models, and significantly accelerates repair.

---


### 335. [Seeing the Unseen: Visual Similarity for Pixel Language Model Adaptation](https://arxiv.org/abs/2608.30541)

**<font color=#1a73e8>作者：</font>** Ran Zhang, Miryam de Lhoneux, Wessel Poelman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pixel-based language models (LMs) replace traditional tokenizers by processing rendered images of text, making cross-lingual transfer heavily dependent on the visual and structural properties of writing systems. However, the dynamics of adapting these models to low-resource languages with complex morphology and written in unique scripts are not yet explored. Using Tibetan as a case study, we analyze how continued pre-training of pixel-based LMs is influenced by data scale, initial script exposure, and cross-lingual transfer from languages written in other Brahmic scripts. We introduce four rendering-level metrics to quantify visual script similarity. We evaluate downstream performance across three tasks. Our results show that higher orthographic proximity enhances semantic transfer, even under severe data constraints. Additionally, we find a performance asymmetry based on the pre-training starting point: while multilingual pre-training PIXEL-M4 has stronger initial performance, its capacity for subsequent adaptation seems to be constrained, whereas adapting a monolingual model PIXEL with mixed scripts yields more gains on sentence-level tasks. Our metrics and case study offer empirical observations that could help inform data selection and script adaptation choices when working with pixel-based models in similar low-resource settings.

---


### 336. [Designing an Auditable LLM-Supported Workflow for Qualitative Thematic Analysis](https://arxiv.org/abs/2608.30543)

**<font color=#1a73e8>作者：</font>** Nadia Jul Jeldtoft, Tariq Yousef  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) offer new possibilities for scaling qualitative analysis, but existing applications often provide limited methodological transparency regarding how qualitative methods are translated into computational procedures. This paper presents an auditable and privacy-preserving computational operationalization of inductive and latent Thematic Analysis (TA). This paper first derives five design principles from the methodological requirements of TA and the conditions introduced by LLM-based inference: preserving interpretative context, maintaining traceable relationships between empirical material and analytical outputs, representing analytical constructs and reasoning explicitly, constraining LLM inference to interpretative tasks, and enabling privacy-preserving local deployment. Second, it presents a proof-of-concept for a two-phase workflow that operationalizes these principles by combining interpretative LLM inference with deterministic procedural control to generate codes, analytical justifications, themes, and theme descriptions while preserving explicit links to the source material. Third, it proposes an evaluation framework combining structural comparison with human-led TA and independent expert assessment of analytical quality. The evaluation is conducted on semi-structured Danish interview transcripts. and the results shows that the workflow produces code-level outputs with coverage broadly comparable to human annotations and highly rated analytical justifications, while generating a more compressed thematic structure characterized by fewer and broader themes. The findings demonstrate the feasibility of auditable LLM-supported TA through a modular workflow designed to scale to larger datasets, accommodate different LLMs, and support transfer across research domains, with domain adaptation primarily requiring adjustments to the prompting strategy.

---


### 337. [GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns](https://arxiv.org/abs/2608.30550)

**<font color=#1a73e8>作者：</font>** Yinwen Lu, Weihao Luo, Yueqi Zhong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Sewing pattern generation aims to infer executable sewing patterns from design cues such as sketches and textual descriptions. As an interpretable and simulation-compatible representation, sewing patterns are particularly valuable for digital garment creation. However, existing methods often model garment specifications as flat long sequences, which entangles garment structure with detailed parameters and leads to redundant components, inaccurate local details, and poor simulation compatibility. In this paper, we present GarmentWeaver, a schema-aware framework for multimodal Sewing pattern generation. GarmentWeaver constructs compact hierarchical targets by activating garment-relevant structural branches and predicts executable Sewing patterns in a structured manner. Specifically, we introduce a schema-aware target construction strategy, build the generator on top of a pretrained vision-language model for multimodal garment understanding, and impose feasibility-aware regularization to encourage structurally valid and simulation-compatible outputs. Extensive experiments show that GarmentWeaver produces more accurate and more executable sewing patterns than strong baselines, while also yielding better simulation results. These findings demonstrate the effectiveness of schema-aware structured generation for reliable multimodal Sewing pattern prediction.

---


### 338. [AdaPath: Query-Adaptive Path-Finding via Path-Bank for Multi-Hop Implicit Biomedical KGQA](https://arxiv.org/abs/2608.30556)

**<font color=#1a73e8>作者：</font>** Jun Hyeong Kim, Dongki Kim, Yinhua Piao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Path-finding over knowledge graphs has become an effective way to ground LLM reasoning on multi-hop questions. However, biomedical QA introduces two distinct challenges that general-domain methods are not designed for: (i) queries do not expose intermediate reasoning and can be answered through multiple valid pathways, and (ii) biomedical knowledge graphs are densely connected, so path-finding methods easily take wrong turns. To address these challenges, we propose AdaPath, a path-finding framework that retrieves query-adaptive meta-paths from Path-Bank, which captures both query semantics and biomedical knowledge graph structure. AdaPath provides the missing cues in biomedical queries while effectively pruning dense knowledge graph neighborhoods during multi-hop reasoning. We further release BioStrat-QA, a biomedical KGQA benchmark that stratifies multi-hop queries by how much intermediate reasoning they expose. Across biomedical KGQA benchmarks, AdaPath consistently outperforms baselines, sustaining meaningful path-finding even when multi-hop queries expose less surface information. The source code is available at this https URL.

---


### 339. [Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.30564)

**<font color=#1a73e8>作者：</font>** Deokjae Lee, Sihun Chu, Hyun Oh Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision quantization (MPQ) assigns a different bitwidth to each linear layer of a large language model (LLM) to minimize the quantization-induced quality loss under a fixed budget, but Mixture-of-Experts (MoE) models contain these layers in every expert of every MoE block, so the allocation space grows far larger than in a dense model. Existing methods either allocate within each block under a uniform per-block budget, or allocate across blocks through an additive proxy, and neither directly optimizes a model-level objective over the choices that couple the blocks. We propose Q-Strata, a bi-level allocator that ranks within-block assignments with a cheap proxy and allocates across blocks with a model-level objective evaluated on the assembled quantized model. Its inner stage caches a Pareto frontier of candidates per block over finely spaced budgets, leaving the outer stage to set one budget per block instead of a bitwidth for every linear layer. With the search reduced to one budget per block, the outer stage optimizes this model-level objective directly, capturing the inter-block coupling that additive proxies miss. On Mixtral-8x7B-Instruct, Qwen1.5-MoE-A2.7B, and DeepSeek-V2-Lite, Q-Strata consistently achieves lower WikiText2 perplexity than uniform-bitwidth GPTQ and the state-of-the-art MoE MPQ methods MxMoE and GEMQ in the low-bit regime. The code is available at this https URL.

---


### 340. [TuringLLM: Efficiently Scaling Foundation Models Toward Physical AI](https://arxiv.org/abs/2608.30567)

**<font color=#1a73e8>作者：</font>** Yuheng Zhang, Yizhao Wang, Da Zhu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Turing-20B-A2B, a 20B-parameter Mixture-of-Experts language model that activates approximately 2B parameters per token, designed for long-context and latency-sensitive physical AI applications. The model adopts Quantile Routing in a dynamic top-k configuration, enabling token-adaptive expert allocation while maintaining balanced expert utilization and a controlled average compute budget. During deployment, we further apply capacity-constrained routing to prompt prefill for more regular and efficient expert execution, while retaining dropless routing during pretraining. Turing-20B-A2B also employs a hybrid attention architecture that combines Lightning Attention with a small number of full-attention layers for efficient long-context modeling. The model is pretrained with a progressive three-stage curriculum and extended to a native context length of 128K through continued pretraining, with further inference-time extension to 512K using YaRN. Despite its compact active-parameter budget, Turing-20B-A2B achieves, at the base-model stage, overall general capability exceeding Qwen3-8B Base and approaching Qwen3.5-9B Base, while maintaining strong long-context performance and favorable prefill-latency scaling. These results demonstrate an effective balance among model capability, long-context scalability, and practical inference efficiency.

---


### 341. [Automated Testing of LLM-Based Post Hoc Explainers Using Model Checking as an Oracle](https://arxiv.org/abs/2608.30581)

**<font color=#1a73e8>作者：</font>** Dennis Gross, Helge Spieker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are used as post hoc explainers of sequential decision-making policies, producing natural-language explanations of why an action was chosen. However, LLMs often generate plausible but incorrect statements, and no existing approach systematically tests whether such explanations are faithful to the underlying environment. Two classic software testing challenges stand in the way: there is no oracle for the correctness of an explanation, and the test inputs, natural language queries about a policy's behavior, lack the structure needed for systematic test case generation. We address both. Probabilistic model checking provides the test oracle, computing exact reference results against which LLM answers are graded automatically. A taxonomy of post hoc query categories structures the input space around the environment-level facts from which policy explanations are composed; test cases generated from it are prioritized by question-specific diagnostic difficulty scores. Across seven MDP environments, the testing separates three open-weight LLMs: a reasoning model passes 85% of test cases, a mid-size model 70%, and a 1B model falls below the random baseline, while prioritization surfaces significantly harder cases than random selection. Our results indicate how trustworthy LLM-generated explanations are in model-free settings, where the same LLMs are used but no oracle exists to verify them.

---


### 342. [Learning Compositional Spatio-Temporal Video Grounding with Synthetic Curriculum](https://arxiv.org/abs/2608.30584)

**<font color=#1a73e8>作者：</font>** Xingjian Wang, Shijian Wang, Yibo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the impressive progress of recent MLLMs on spatio-temporal video grounding (STVG), existing evaluations and training data focus primarily on simple queries. They largely overlook the compositional queries prevalent in real-world scenarios, where a target must be disambiguated by jointly reasoning about its attributes and relations to other entities. To bridge this gap, we propose Compositional Spatio-Temporal Video Grounding (CompSTVG), a task that requires models to process complex textual queries where every intertwined attribute and relational cue is essential for disambiguation. To facilitate this task at scale, we build a synthetic data engine that leverages a spatio-temporal scene graph as a difficulty measure and casts difficulty-controlled query synthesis as a constraint programming problem, producing difficulty-graded data for both evaluation and training. Built on this engine, we introduce STVG-CompBench, a benchmark stratified by explicit difficulty levels that jointly capture temporal complexity and spatial interference. Evaluating 11 representative STVG models on STVG-CompBench reveals that current models perform poorly on compositional queries, exhibiting a sharp performance drop that is typically obscured by overall dataset-level averages. We further construct synthetic training data and propose CurrSTVG, a curriculum reinforcement learning framework that delivers consistent gains, with the largest improvements observed on the most challenging compositional queries.

---


### 343. [Reading the News: Adapting Large Language Models to Swedish Journalism Through Continued Pre-Training](https://arxiv.org/abs/2608.30609)

**<font color=#1a73e8>作者：</font>** Lukas Borggren, Jenny Kunz, Marco Kuhlmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly capable in general, but their utility can remain modest in niche or understudied areas. One approach to address this limitation is to specialise existing models through additional training on target-domain corpora. In this work, we investigate such continued pre-training for adapting large language models to Swedish journalism, using a high-quality dataset that we curate from millions of news articles. To evaluate the adaptation efficacy, we also construct a novel domain-specific benchmark that covers six editorial tasks. Through full and parameter-efficient fine-tuning across two model sizes, we find that continued pre-training yields benefits in the target domain, but only when paired with experience replay to mitigate forgetting. We observe consistent enhancements in the models' generation quality and factual knowledge, but not their proficiency in discriminative tasks. Exploring a training-free method to facilitate instruction following, we see further improvements, but exclusively for models trained with low-rank adaptation. Crucially, we demonstrate the importance of targeted evaluation in the adaptation process, as an existing Swedish benchmark largely fails to capture the models' in-domain performance gains.

---


### 344. [TaxCE : A Framework for Automated Taxonomy Construction and Evaluation at Scale](https://arxiv.org/abs/2608.30614)

**<font color=#1a73e8>作者：</font>** Sandeep Sricharan Mukku, Albert Aristotle Nanda, Rohit Pyati  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizing unstructured feedback text into hierarchical taxonomy is a fundamental challenge in NLP, particularly in domains where feedback arrives at massive scale in varied forms such as reviews, transcripts, and surveys. Existing approaches either produce shallow hierarchies, neglect long-tail topics, or lack rigorous evaluation frameworks. We present TaxCE, a fully automated framework that constructs multi-level hierarchical taxonomies from raw text through progressive condensation of corpus content into actionable segments, deduplicated semantic units, and granular topics with definitions, which are then organized bottom-up into a hierarchy with corpus-groundedness. We also introduce three corpus-grounded evaluation metrics, Exclusivity, Exhaustivity, and Granularity (EEG), and integrate them into a metrics-in-the-loop iterative refinement mechanism that diagnoses deficiencies and applies targeted corrections until convergence. Extensive experiments demonstrate that TaxCE consistently outperforms existing baselines spanning classical topic models, neural methods, and LLM-based approaches, with average improvements of 11.8, 20.5, and 15.7 percentage points in exclusivity, exhaustivity, and granularity respectively over the strongest baseline. Human evaluation further confirms superior taxonomy quality, actionability, and navigability.

---


### 345. [Hidden Threat in Synthetic Data: Covert Targeted Bias Injection through Benign Text](https://arxiv.org/abs/2608.30619)

**<font color=#1a73e8>作者：</font>** Minkyung Cho, Jihyo Kim, SeungWoo Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data is increasingly used to train large language models (LLMs), yet its security implications remain poorly understood. Prior work on subliminal learning suggests that models can inherit behavioral traits from seemingly unrelated training data. In this work, we investigate whether such mechanisms can be exploited to inject targeted social biases into aligned models through semantically benign synthetic data. We construct a pipeline in which a misaligned teacher model generates filtered synthetic datasets across domains such as creative writing and code generation, which are then used to fine-tune aligned student models. Our experiments show that benign-looking synthetic data can act as a covert channel for transmitting targeted biases while largely preserving the student model's general task capabilities. These results reveal a previously underexplored security risk in synthetic data-driven LLM training pipelines and highlight the need for improved safeguards. As one possible step toward this goal, we suggest that log-linearity-based scoring may provide a useful signal for screening seemingly benign synthetic data.

---


### 346. [REER-PT: Reverse-Engineered Reasoning for Perplexity-Guided Pre-training Data Augmentation](https://arxiv.org/abs/2608.30627)

**<font color=#1a73e8>作者：</font>** Haoran Que, Jiajun Shi, Ting Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language-model compute continues to scale, high-quality training data is becoming an increasingly important bottleneck. Conventional next-token prediction supervises what follows a context but leaves the intermediate reasoning behind that continuation implicit. We introduce \textbf{REER-PT}, a scalable framework that extends Reverse-Engineered Reasoning (REER) to raw pre-training data. REER-PT identifies continuations that are difficult to predict but can still be inferred from the preceding context, and inserts concise reasoning annotations that reconstruct the missing connection between context and continuation. Candidate annotations are generated and refined offline, with perplexity serving as the optimization signal. Constraints on length and target leakage filter out unhelpful or trivial annotations. This sparse transformation preserves the source text and remains compatible with standard next-token prediction, avoiding online reasoning rollouts during pre-training. We apply REER-PT to transform a source pre-training corpus into an augmented one. Across augmented-data, original-token, and selected-continuation comparisons, perplexity reductions range from 0.42 to 7.29, and only about 0.05\% of annotation 13-grams appear verbatim in the source text. We then train two 680M-parameter models with the same architecture and training configuration on the source and augmented corpora, respectively. The augmented-data model gains up to 2.07 percentage points on several knowledge and reasoning benchmarks. Together, the perplexity analysis indicates improved continuation predictability, while the controlled pre-training experiments suggest that this augmentation can improve model performance without changing the standard pre-training objective.

---


### 347. [GMTS: Gradient Magnitude-based Token Selection Improves RLVR Training for LLM Reasoning](https://arxiv.org/abs/2608.30632)

**<font color=#1a73e8>作者：</font>** Outongyi Lv, Yuanwei Zhang, Xiaoqun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL), particularly RL with Verifiable Rewards (RLVR), has recently emerged as a central paradigm for enhancing large language models' (LLMs) reasoning abilities, demonstrating remarkable effectiveness across reasoning tasks. Recent studies suggest that high-entropy tokens play an exceptionally important role in model training, since training with only the highest 20% entropy tokens yields significant performance gains. However, why such high-entropy tokens are beneficial remains insufficiently understood. In this work, we find that although high-entropy tokens within one answer tend to correlate with large gradient magnitude, entropy alone fails to consistently reflect token importance across different answers, considering the variations in the answer-level reward signals. Based on this observation, we introduce the Gradient Magnitude-based Token Selection (GMTS) method to quantify token importance, which leverages the entropy-gradient connection to approximate gradient-magnitude rankings for token selection. We find that training on the top 20% tokens ranked by GMTS consistently outperforms entropy-based token selection across three reasoning domains and various model sizes, suggesting that GMTS provides a more fine-grained estimate of token contribution for RLVR training.

---


### 348. [BiG-SURE - Bipartite Graph for Semantic Uncertainty and Reliability Estimation of LLMs](https://arxiv.org/abs/2608.30646)

**<font color=#1a73e8>作者：</font>** Debarpan Bhattacharya, Malay Phadke, Sriram Ganapathy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is a crucial requirement for deploying large language models (LLMs) and vision-language models (VLMs) in safety-critical settings, especially when the model parameters are not accessible (black-box). We propose BiG-SURE, an uncertainty estimator based on cross-temperature semantic agreement. The method samples low-temperature responses as stable semantic anchors and high-temperature responses as probes under meaning-preserving input transformations. It then constructs an anchor-probe Bipartite Graph (BiG) using NLI-based entailment scores and defines confidence through the normalized squared spectral energy of this matrix, with uncertainty given by its complement. This bipartite graph-based Semantic Uncertainty and Reliability Estimation (SURE) score measures whether high-temperature probes remain semantically aligned with the model's stable low-temperature belief or not. We evaluate BiG-SURE on text QA, multilingual QA, and multimodal QA tasks across multiple model families. In these experiments, BiG-SURE improves average abstention AUROC over prior black-box uncertainty estimators, while remaining simple, unsupervised, and applicable to black-box model settings.

---


### 349. [What It Costs to Compose, Rebuild, and Correct Precomputed Memory](https://arxiv.org/abs/2608.30647)

**<font color=#1a73e8>作者：</font>** Asa Shepard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can answer from precomputed memory, a model's saved reading of a body of material, reused across requests instead of read again at each. This paper maps where that practice preserves correctness and the conditions under which it fails. Across experiments on Llama-3.1-8B-Instruct using both saved key-value caches and trained compressions of them, precomputed memory degrades when assembled from separately prepared parts, stays current only through rebuilds costing a large fraction of full preparation in our measurements, and ignores corrections served beside it conditional on phrasing. If precomputed memories can be served alongside one another, be cost-efficiently rebuilt, and be superseded by new information arriving in real-time, they can serve as a way to avoid re-feeding context to a model over repeated queries. The implication of our results for a deployed system that deals with a variety of queries is that precomputed memories are best rebuilt on the cadence at which new information changes what the memory was originally computed from. Both warm-rebuilding trained compressions of key-value caches and serving specifically-phrased updates beside a memory, as pasted text or injected cache state, show particular promise for keeping precomputed memories current, the latter as an interim measure between rebuilds, and we measure the cost and name the remaining questions associated with each.

---


### 350. [Where Identity Lives: Localized, Retain-Free Identity Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2608.30649)

**<font color=#1a73e8>作者：</font>** Kangwook Ko, Jaehyuk Jang, Wonjun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Removing a specific individual's information from multimodal large language models (MLLMs) is often needed after deployment, but existing methods rely on a retain set, which is hardest to obtain at that point, and rebuilding it recreates the privacy exposure that unlearning aims to remove. Forgetting from the forget set alone instead damages the shared visual-language computation, harming perception. We cast retain-free unlearning as a localization problem: causal tracing, weight transplant, and Fisher overlap all point to early-to-mid decoder MLPs as the layers where identity information is stored and, unlike other module families, can be modified without substantially disrupting vision. We turn this into Pathway-Aware Visual-attribute Anchoring (PAVA), which confines updates to these layers and pairs a forget loss with a visual-attribute anchor that preserves image-grounded behavior by distilling the model's own pre-unlearning answers from the forget images alone. On MLLMU-Bench and ReMem, PAVA gives the strongest forget-retain trade-off among forget-set-only methods and remains competitive with retain-based baselines.

---


> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
