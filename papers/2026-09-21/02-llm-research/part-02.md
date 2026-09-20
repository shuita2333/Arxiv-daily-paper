# 🧠 大模型相关研究 | 2026年09月21日

> 本类共 **176** 篇论文：已确认 **162** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-176](./part-04.md)

---

### 51. [Faithful Where It Can Be Checked: Auditing a Reflection Agent Against Its System Prompt in a Randomized Trial](https://arxiv.org/abs/2609.19635)

**<font color=#1a73e8>作者：</font>** Subigya K. Nepal, Serena Soh, Noah Vinoya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational agents are increasingly used to guide reflection. A recent randomized trial compared a GPT-4o career reflection agent with the same program in a static journaling survey. Agent participants ended less committed to their career plans and more doubtful. We coded all 17,930 turns from its two studies, checked our coding against human coders and linked conversations to the trial's surveys. The rules the agent followed were the easy-to-check ones, like a reply length cap. Told not to flatter, it praised participants in half of its turns; told to challenge gently, it almost never did, and such a break leaves no visible trace. The behavior tied to the worse outcome was the demand to decide: the survey posed each decision once, while the agent asked again when participants hesitated, and those pressed most ended most doubtful. Our findings inform reflection agent design and the writing of checkable instructions.

---


### 52. [Reach or Solve? Attributing Agentic RL Gains with Checkpoint Handoffs](https://arxiv.org/abs/2609.19636)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Jingbin Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning now trains language-model agents that act over dozens of steps in live environments. The gains are large, and they are read as better decision-making. An agent in a closed loop writes its own inputs. Each observation follows from its own earlier actions, so the states it meets late in an episode are partly of its own making. An SFT checkpoint and an RL checkpoint are then scored from different states, even on identical tasks. Endpoint success mixes two changes: where the agent arrives, and what it does once it is there. Restricting the comparison to states both policies reach does not separate them. That restriction selects on an outcome, and in our data it flips the sign of the effect. We introduce checkpoint handoff, an evaluation protocol that clones a state one released checkpoint reached and hands it to another, with no retraining. Crossing a reacher role and a solver role over SFT and RL splits an endpoint gain into REACH and SOLVE. REACH is how often a policy arrives at a state the environment confirms is a fixed number of actions from success. SOLVE is how often it finishes from an identical cloned state. Across two benchmarks and two independently released pipelines, the reacher by solver interaction is positive in all five conditions. An RL history is worth more to an RL solver than the same history is to an SFT solver. On ALFWorld, RL improves both terms, and the SFT solver never succeeds where the RL solver fails. Independent REACH and SOLVE gaps predict the aggregate interaction. Handoff asks only that one checkpoint's history can be replayed under another, so long-horizon evaluation can report arrival and completion beside endpoint success.

---


### 53. [Replan, Repair, or Edit? A Unified Empirical Evaluation of Travel Agents for Itinerary Revision under Resource Disruptions](https://arxiv.org/abs/2609.19654)

**<font color=#1a73e8>作者：</font>** Xiaofei Yuan, Yan Zhang, Shaobo Qiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Travel-planning agents generate itineraries that may become infeasible after acceptance because of flight cancellations, hotel unavailability, or attraction closures. Revising these itineraries involves full replanning, classical plan repair, and LLM-based travel-agent revision, whose differing task formulations and evaluation protocols hinder comparison. We conduct a systematic empirical study using two TREK-derived benchmark sets: 500 single-disruption cases, including feasible and infeasible instances, and 200 feasible simultaneous compound-disruption cases. We compare LLM-Z3 full replanning, IPyHOPPER hierarchical repair, and an iTIMO local-revision adapter across effectiveness, plan stability, and computational cost. LLM-Z3 with Gemini achieved the highest observed compound-disruption success. IPyHOPPER nearly matched that configuration's single-disruption overall success, while preserving substantially more of the accepted itinerary on successful repairs. Successful hierarchical and local repairs made fewer edits and retained more accepted commitments than full replanning. Computational profiles differed: IPyHOPPER used no LLM inference, the evaluated LLM-Z3 adapter used compact one-call inference, and the iTIMO adapter consumed substantially more tokens. The study provides practical guidelines for balancing feasibility recovery, commitment preservation, and computational cost within evaluated settings.

---


### 54. [Beyond Patch Removal: Persistent Adversarial Effects in Vision-Language-Action Policies](https://arxiv.org/abs/2609.19669)

**<font color=#1a73e8>作者：</font>** Enhao Wu, Fusen Guo, Yuxin Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial patches to Vision-Language-Action (VLA) policies can cause both immediate action corruption and persistent state effects that remain after the patch is removed. Existing evaluations largely focus on continuous attacks and do not separate these two effects. We introduce a state-restoration protocol that removes the patch at matched action-chunk boundaries and measures subsequent recoverability under the same remaining step budget. Clean, random-patch, deviation-matched, and fixed-direction controls distinguish adversarial effects from occlusion, action-error magnitude, and directional persistence. We also evaluate a recovery adapter trained on attack-induced states under controlled intervention latency. On OpenVLA-OFT with EDPA attacks, only 36.2% of LIBERO-Long episodes remain recoverable after five chunks, compared with 89.9% and 87.0% for the deviation-matched and fixed-direction controls. Similar persistent effects are observed on autoregressive OpenVLA. The recovery adapter improves recovery from 7.7% to 47.4% at one-chunk latency, but its benefit decreases substantially with delayed intervention. These results show that adversarial effects can persist after patch removal and that timely intervention is critical for recovery.

---


### 55. [When2Think: Learning Difficulty-Aware Length Control for Efficient Hybrid Reasoning Models](https://arxiv.org/abs/2609.19671)

**<font color=#1a73e8>作者：</font>** Jaejun Shim, HyunJin Kim, Young Jin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance on complex tasks but exhibit systematic inefficiency: they often overthink easy problems and underthink hard ones. Existing approaches based on uniform length penalties or rigid routing incur an efficiency tax, trading reduced computation on easy instances for accuracy loss on hard instances. We formulate efficient reasoning as an instance-adaptive computation allocation problem and propose When2Think, a post-training framework for hybrid reasoning that dynamically allocates computation based on problem difficulty. Our method introduces Instance-level Difficulty-Aware Control (IDAC), a reward-shaping mechanism that leverages pre-computed reference statistics (accuracy and token usage) to regulate reasoning depth. Combined with verifier-based rewards and batch-wise standardized advantages, IDAC enables stable critic-free optimization without learned reward models or online reference-model queries. When2Think encourages direct answering on easy instances while preserving extended reasoning on hard instances, thereby learning when to use System 1 (NoThink) versus System 2 (Think). Experiments on mathematical benchmarks demonstrate improved accuracy-efficiency trade-offs: on AIME24, Pass@3 increases by 10.0% while token usage is reduced by 27.9% relative to the base model, and on AIME25, When2Think achieves 40.0% Pass@3, outperforming compression and routing-only baselines.

---


### 56. [IMFD: End-to-end Multi-Face Forgery Detection through Instruction-based Large Vision-Language Models](https://arxiv.org/abs/2609.19693)

**<font color=#1a73e8>作者：</font>** Dasom Choi, Sangjun Moon, Hyeongchan Im 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid increase of deepfakes has raised significant concerns due to their spread on social media. Traditional multi-face forgery detectors crop and verify each face independently, ignoring background context and inter-face relationships, which often yields suboptimal performance. To overcome these limitations, we leverage instruction-based Large Vision-Language Models (LVLMs), which can interpret entire images and follow complex textual instructions. We propose a simple yet effective single-stage multi-face forgery detector, called IMFD (Instruction-based Multi-face Forgery Detector), which is trained end-to-end to jointly localize faces and predict per-face forgery labels. Rather than treating face box prediction only as a joint objective, IMFD explicitly integrates predicted face bounding boxes into the instruction as visual cues that enhance instruction grounding and forgery detection. To support the training and evaluation of IMFD, we convert existing multi-face forgery datasets into an instruction-based format. Experimental results and analyses show that IMFD improves multi-face forgery detection by integrating face bounding boxes into the instruction, and consistently outperforms various state-of-the-art methods.

---


### 57. [Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation](https://arxiv.org/abs/2609.19702)

**<font color=#1a73e8>作者：</font>** Daeun Kim, Junwha Hong, Changhun Oh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive image generation has emerged as a paradigm for multimodal AI systems due to its compatibility with transformer-based LLM serving infrastructures. However, generating thousands of visual tokens per request makes decoding increasingly bottlenecked by KV cache accesses during attention computation. Sparse attention is particularly attractive for this workload because many visual generation applications tolerate moderate quality degradation in exchange for improved performance and efficiency. While sparse attention has been extensively explored for text-based LLM inference, it remains unclear whether its sparsity assumptions generalize effectively to autoregressive image generation. We present the first systematic characterization of attention sparsity in autoregressive image generation across diverse workloads and representative open-source models. Our analysis reveals several distinguishing properties, including a pronounced prefill-decode asymmetry, strong attention concentration on prompt and local tokens, and a unique diagonal attention sparsity pattern arising from the spatial locality of visual tokens. Motivated by these observations, we propose a diagonal-aware sparse attention mechanism that selectively skips KV entries along the diagonal attention direction within a recent window. Implemented on top of a GPU-based serving system using FlexGen, FlashAttention-2, and custom kernels, our approach achieves up to 3.1x throughput and 1.19x latency improvements with less than 2% quality degradation compared to dense inference.

---


### 58. [SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes](https://arxiv.org/abs/2609.19705)

**<font color=#1a73e8>作者：</font>** Mengxiao Wang, Nitesh Saxena  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous large language model (LLM) agents are moving rapidly into high-stakes domains, yet existing agentic-AI security studies remain largely domain-agnostic and overlook the distinctive, high-consequence attack surface such settings create. We examine this gap through financial trading agents, a representative case of high-stakes agentic security, where a single compromised agent has direct execution authority over real capital in an adversarial, reflexive market. To this end, we present FARSIGHT (Financial Agent Robustness and Security Investigation and Global Holistic Testing), a framework that performs scheme-level evaluation of financial LLM agents on two axes: robustness under market turbulence (including flash-crash-like scenarios), and security against three attack types: attacks on information sources, attacks on agents, and agent-as-attacker behaviors. Applying FARSIGHT to 15 representative academic schemes, we find that most overlook robustness and realistic adversarial threats: 80% fail at least one core robustness metric and 100% exhibit security vulnerabilities. These two failure modes are inseparable: a small misjudgment can cascade into a market-wide crash on its own, while an adversary can deliberately trigger the same collapse at minimal cost.

---


### 59. [Learn Your Own Thoughts: Abstract Token Curriculum](https://arxiv.org/abs/2609.19717)

**<font color=#1a73e8>作者：</font>** Khashayar Gatmiry, Avrajit Ghosh, Parsa Mirtaheri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable reasoning capabilities by utilizing chain-of-thought (CoT) as a scratchpad for intermediate stages of thinking. However, CoT techniques require explicit supervision on thinking tokens, which requires rich, task-specific data. In this work, we propose Abstract Token Curriculum (ATC), a novel curriculum learning framework that elicits effective continuous intermediate representations without direct supervision or manual scratchpad design. ATC gradually increases problem complexity through a sequence of distributions, training the model to develop internal abstract ``thoughts'' in the continuous representation space. This paper provides both theoretical and experimental evidence for the benefits of ATC and its advantages over previous methods for training continuous thoughts. Theoretically, we show that for learning parity functions with single-layer softmax attention using ATC, attention naturally focuses on the CoT tokens in the context that provide the ``easiest path'' to predicting the next token. Experimentally, we show ATC's effectiveness on graph reachability and arithmetic learning tasks.

---


### 60. [Reachability, Not Observation: Containing Systems Whose Wiring Changes](https://arxiv.org/abs/2609.19720)

**<font color=#1a73e8>作者：</font>** Yoshiaki Takashita  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Containment decisions -- where to put a firewall, which links to monitor, what a program may reach -- are computed from an observed structure, and observation is a snapshot. We ask what a snapshot misses when the wiring changes over time. On a hypercube whose active dimension rotates, a balanced split shows zero crossing edges at 93% of instants, yet 8,192 edges must be blocked permanently; adding one always-on ring, a defender sees 2 where 8,194 must be blocked, a factor of 4,097. A time-aware defender holds 585 blocks on average, but one step of clock lag drops its containment to 0%. On the real Internet the same gap is only x1.8-2.0 (1997-2000) and x1.5-1.6 (2024-2026) once growth is removed, so the blind spot is introduced by design, not inherited from the world -- and it has been designed: the round-robin schedules of optical datacentre fabrics have a gap equal to their period. A declared capability map, checked by static reachability over a real application's call graph, catches all 8 planted holes; the string deny-list previously in place catches 2. One calculation generates every number from one parameter, the period, and reads three boundaries not usually called schedules: frequency hopping, whose standard results are these closed forms with channels in place of edges; the air gap, whose always-on crossing set is empty and whose known breach came at the one phase a snapshot misses; and the tool surface of a coding agent, inventoried from the inside. Turning the cuts on that agent: idle, its instantaneous state cut is zero, while 6 channels carry it across a context reset, none of them the network, so severing the network removes 0. The channel that spawns copies is a branching process with a sharp threshold at approval rate 1/b, below which denial is unnecessary and above which denial is insufficient. Contain by the paths that exist, not by the behaviour that was seen.

---


### 61. [LearnActCoder: Role-Aware Error Memory for Adaptive Clinical Coding Agents](https://arxiv.org/abs/2609.19721)

**<font color=#1a73e8>作者：</font>** Meysam Ghaffari, Bhaskar Sen, Nasim Sabetpour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical coding agents repeatedly encounter the same failure modes, including unsupported codes, missed documented conditions, specificity errors, and procedure-coding convention mismatches. We introduce Learn-Then-Act, an inference-time adaptation framework that converts errors from a small labeled LEARN batch into a structured Mistake Knowledge Database (MistakeKDB). False-negative lessons are routed to a recall-oriented Coder, while false-positive lessons are routed to a precision-oriented Judge. We instantiate the framework in LearnActCoder, a Coder-Judge clinical coding pipeline with lookup-table grounding where available. On 150 matched MIMIC-III notes, structured MistakeKDB improves CPT F1 by 5.9 percentage points, while raw-example and reflection-style memories remain near the no-memory baseline; the ICD-9 improvement is not significant. On a matched MIMIC-IV cohort, memory shifts ICD-10 coding toward higher precision at a recall cost, leaving F1 statistically unchanged. Applying the same memory to 1,000 held-out MIMIC-III notes maintains a stable ICD operating point, providing scale/stability evidence. Overall, the results are consistent with structured, feedback-derived error memory being useful for adapting clinical coding behavior across cases without weight updates or changes to the underlying workflow. Absolute CPT/HCPCS performance remains low, and the system is evaluated retrospectively rather than in clinical deployment.

---


### 62. [ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers](https://arxiv.org/abs/2609.19722)

**<font color=#1a73e8>作者：</font>** Hyeongjun Choi, Wonyoung Jung, Haehoon Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are being integrated into malware triage workflows as reasoning components that summarize static evidence and produce analyst-facing verdicts. This paper shows that the same reasoning capability introduces a new attack surface. We present ALIBI, a semantic cover story attack against frontier LLM-based malware analyzers. ALIBI adds a small, non-executed read-only section to a compiled binary, containing a coherent but false security product narrative, without altering imports or executable behavior. Instead of issuing direct instructions to the model, it reframes suspicious evidence as expected behavior of a benign endpoint security tool. On a frozen PE set of 50 malicious samples, the payload flips 30 of the 35 baseline-malicious samples to benign on Gemini 2.5 Pro, while GPT-5.5 Pro and Claude Opus 4.7 produce substantial severity downgrades with significant confidence reductions even when verdict labels are preserved. The attack transfers to ELF binaries, where Gemini flips 16 of 40. A verification-guided defense prompt roughly halves the benign verdicts, but 42.9 percent of malicious samples still reach benign. LLM malware analyzers therefore require provenance checks that separate verified facts from attacker-controlled claims, not narrative trust.

---


### 63. [Region-Level Policy Optimization for Fine-grained MLLM Perception](https://arxiv.org/abs/2609.19745)

**<font color=#1a73e8>作者：</font>** Yuheng Shi, Xiaohuan Pei, Minjing Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual perception in MLLMs is commonly improved by raising the resolution, but the added visual tokens inflate vision-encoding and language-model prefilling costs. We show that the two operations underlying fine-grained perception, localizing the region of interest (RoI) and recognizing its content, have different resolution requirements. In a controlled diagnostic, localization tolerates roughly 3 to 4 times stronger token compression than recognition, which motivates localizing from a coarse view and concentrating resolution on the selected evidence. Decoding coordinates with the MLLM can be trained end-to-end from answers, but costs a full model pass per query and depends on grounding ability. A lightweight proposal network distilled from the model's attention is fast, but inherits the noise of its attention targets. The RoI from the proposal network reaches the answer through a discrete region choice, so its faithfulness to the answer cannot supervise the network. We therefore optimize the proposal network with region-level reinforcement learning, which we call Vision-RL2. It treats coherent regions as actions, and a frozen MLLM reader scores each one by how its removal changes the answer likelihood. Complementary subtractive and additive objectives suppress distracting proposals and recover missing evidence, updating only the predictor without region annotations, response sampling, or reasoning trajectories. The refined proposal further enables a sparse encoding that magnifies evidence and excludes background tokens. Across six fine-grained benchmarks and four MLLM backbones, Vision-RL2 improves accuracy over the base model at every token budget and surpasses its largest-budget accuracy with about 4 times fewer visual tokens. Code is available at this https URL .

---


### 64. [AutoData: Agentic Search for Pre-training Data Selection](https://arxiv.org/abs/2609.19754)

**<font color=#1a73e8>作者：</font>** Yan Meng, Dhruv Srikanth, Bingchen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have recently shown promise in automating machine learning engineering by editing model and training code under execution feedback. Data, however, remains largely outside this agentic optimisation loop. We frame pre-training data selection as heuristic engineering over per-document features, i.e., lexical statistics, categorical labels, and perplexity. We introduce AutoData, an agent that searches directly over executable selection algorithms. Unlike prior data mixture methods that optimise weights over a fixed set of domains, AutoData searches a richer program space of scoring, stratification, and stochastic selection rules, discovering feature interactions automatically by iteratively refining algorithms with validation feedback from a proxy model. Within an overnight search, AutoData discovers a selection algorithm that outperforms existing human-designed curation pipelines. Despite being searched only on this small proxy, the discovered recipe transfers to larger scales and improves the downstream metric CORE. These results suggest that data engineering can be treated as an agentic machine learning problem, extending autonomous research from model and training-code optimization to the data.

---


### 65. [Rethinking Multi-Agent Collaboration: When More Is Less](https://arxiv.org/abs/2609.19759)

**<font color=#1a73e8>作者：</font>** Yishuo Yuan, Yibo Wu, Yihan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models and single-agent harnesses has reshaped the landscape of autonomous systems, raising a critical question of when multi-agent collaboration offers genuine value. As individual agent capabilities continue to scale, multi-agent collaboration faces diminishing returns while incurring growing context overhead. Through systematic analysis, we delineate the capability boundaries of multi-agent collaboration relative to single-agent alternatives, showing that it confers systematic benefits specifically in long-horizon tasks with sparse dependencies, while single-agent harnesses remain superior in tightly coupled, sequential workflows. Building on these insights, we propose SAIGE, a lightweight multi-agent collaboration mechanism based on Semantic-Aware Incremental Graph Evolution. SAIGE models collaboration as a dynamically evolving graph, where nodes are agent instances spawned on demand and edges encode semantic dependencies established through content-based information retrieval. Experiments on long-horizon, complex task benchmarks show that SAIGE achieves a favorable trade-off between context efficiency and task performance, and that scaling the agent pool or deepening the recursion level does not consistently improve outcomes. Our findings suggest that multi-agent superiority is bounded by task structure rather than universal, and that more agents do not necessarily make a system more intelligent.

---


### 66. [Benchmarking MLLMs via Cognitive Expected Scene Graph for Safety-Critical Visual Negation Understanding](https://arxiv.org/abs/2609.19767)

**<font color=#1a73e8>作者：</font>** Zhiyun Jiang, Hanyong Wang, Binbin Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> True machine intelligence requires transcending passive pixel registration to master top-down functional reasoning over absent information via visual negation understanding. However, unconstrained visual negation paradigms remain overly open-ended, and pervasive affirmation bias causes both existing Multi-Modal Large Language Models (MLLMs) and evaluation metrics to fail under negative semantics. To solve these intertwined challenges systematically, we first anchor the boundaries of negation reasoning within specific cognitive goals. Specifically, by focusing on safety as a highly pragmatic and critical cognitive dimension, we define the task of \textbf{S}cene \textbf{N}egation \textbf{U}nderstanding under \textbf{S}afety Cognition (\textbf{SNUS}). Under this framework, we construct a high-fidelity negative caption dataset mapping dense assertions of localized hazards. Concurrently, we propose the Cognitive Expected Scene Graph (CESG) Score, a structure-grounded, polarity-aware evaluation metric. Extensive experiments demonstrate that while current models struggle on the task, traditional metrics completely collapse under semantic reversals. Conversely, our framework delivers a solid benchmark for SNUS, providing a rigorous foundation to advance risk-aware situational comprehension and counterfactual cognition.

---


### 67. [Learn Before You Judge: Progressive Knowledge-to-Decision Alignment for Explainable Hateful Meme Detection](https://arxiv.org/abs/2609.19778)

**<font color=#1a73e8>作者：</font>** Bo Xu, Chenyuan Wang, Xinyu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hateful memes spread abusive content through implicit interactions between images and text, posing serious threats to the safety of online communities. In recent years, multimodal large language models have been widely used for hateful meme detection and are increasingly adopted to generate explainable detection results. However, we find that existing explain-then-detect methods often couple explanation generation and label prediction within the same training process. This coupling causes interference between task objectives, leading to limited detection performance and even worse results than simple SFT baselines. To address these challenges, we propose ProKDA, a progressive knowledge-to-decision alignment method for explainable hateful meme detection. Inspired by the human annotation training process, ProKDA first uses an agentic background knowledge construction pipeline to obtain external knowledge related to meme understanding. It then adopts a three-stage training strategy that sequentially performs background knowledge learning, hatefulness detection learning, and hatefulness boundary alignment. Unlike prior explain-then-detect methods that jointly optimize both tasks, ProKDA focuses on a single training objective at each stage. This design reduces interference between the two tasks and progressively transforms background knowledge into robust detection decisions. Experiments on three public hateful meme benchmarks show that ProKDA achieves state-of-the-art detection performance and provides accurate, explainable, and evidence-supported decisions for hateful meme moderation. Project page: this https URL.

---


### 68. [Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems](https://arxiv.org/abs/2609.19789)

**<font color=#1a73e8>作者：</font>** Qi Rong Sua, Junhao Dong, Nguyen Duc Thai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent trading systems built on large language models (LLMs) are beginning to appear in quantitative finance, yet their robustness to adversarial inputs is largely unknown. We study the vulnerability of LLM trading stacks to black-box, input-only attacks that enter solely via admissible social-media feeds. We introduce the Generic Multi-Agent Trading System (GMATS), a framework that captures modern multiagent trading architectures and instantiate a class of black-box poisoning attackers that treat an LLM as a post generator and inject budget-constrained, plausibly benign social-media content into the analyst's evidence stream. We define contagion metrics that trace how adversarial content propagates through the stack, including belief-shift scores at analyst and coordinator layers and attack-clean deltas on standard backtest metrics. Experiments on a safe offline benchmark with historical market and social data show that even simple input-only attackers can materially degrade risk-return profiles, sharply reducing Sharpe ratios. At the same time, we find that suitably designed multi-agent topologies and coordinator prompts can dampen adversarial shocks and improve average robustness under identical poisoning budgets.

---


### 69. [Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search](https://arxiv.org/abs/2609.19799)

**<font color=#1a73e8>作者：</font>** Tal Oved, Roi Pony, Oshri Naparstek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-driven evolutionary search finds programs by launching seeds and iterating each one. Papers report a single budget setting, usually one seed run for a fixed number of iterations, and rank methods from that one point. We show this is not enough. We evaluate three evolutionary search strategies on five optimization tasks, commonly used by papers in the genre to report results. We run the analysis over a full grid of seeds and iterations. Our findings suggest that the best way to split a fixed budget between more seeds (width) and more iterations (depth) changes with the strategy, the task, and the total budget. Furthermore, we observe that the ranking of strategies also changes with the budget. On one task the strategy that looks worst at one seed is best at forty seeds. On another the best number of iterations is well below the value common in practice, so extra depth wastes budget that more seeds would turn into score. We provide a measurement protocol that reports the seeds-by-iterations frontier and practical guidance for using it.

---


### 70. [DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum](https://arxiv.org/abs/2609.19801)

**<font color=#1a73e8>作者：</font>** Haoqiang Kang, Yiming Zhang, Yiyang Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Executable environments enable LLM agents to learn from the consequences of their actions. For embodied agents, those consequences extend beyond whether the current task succeeds: completing a delivery can consume the time, energy, or money needed for later work. Learning to plan therefore requires environments that preserve these dependencies and turn them into feedback across a complete trajectory. We introduce DeliveryGym, a 3D environment for evaluating and training agents on continuous courier shifts. It couples multimodal tool interaction with persistent world dynamics and computes trajectory rewards from simulator events, making the costs of an agent's decisions available for reinforcement learning (RL). The environment also adapts future training shifts to the policy's observed weaknesses while keeping evaluation fixed. Across six models and 13 city maps, evaluation exposes a gap between reliably executing assigned deliveries and choosing and sequencing work over a shift. On the fixed test suite, RL improves Qwen3-VL-4B's net income by 54.3%, showing that learning from complete shifts improves performance under these coupled constraints. Adapting the training environment improves test income by 16.5% over uniform sampling at the same rollout budget, indicating that which situations an agent practices also matters. DeliveryGym provides an executable setting for studying how agents learn to coordinate deliveries and preserve resources for later orders within an episode.

---


### 71. [Dictionary-Constrained Grapheme-to-Phoneme for Unsegmented Languages from LLM-Annotated Data](https://arxiv.org/abs/2609.19805)

**<font color=#1a73e8>作者：</font>** Rui Hu, Zhenpeng Zhan, Xiaolong Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grapheme-to-phoneme (G2P) conversion turns raw text into its phonemic form and is an essential part of both text-to-speech (TTS) and automatic speech recognition (ASR) systems. It is required to be fast, stable and context-aware. For unsegmented languages such as Japanese, G2P additionally couples word segmentation with highly context-dependent polyphone disambiguation, and the scarcity of accurately annotated data remains a bottleneck. In this paper, we present a context-aware neural G2P method that scores paths of a discriminative conditional random field (CRF) over a word lattice constructed from dictionaries. To tackle data scarcity, we utilize large language models (LLMs) to generate more than 2 million sentences. Experimental results demonstrate that our method strongly outperforms conventional morphological analyzer-based methods and neural sequence models. On the Joyo-Kanji-Yomi benchmark, our method reaches 99.62% target word reading accuracy, 0.32% target word phoneme error rate (PER) and 0.14% sentence PER.

---


### 72. [Absence is Presence: Understanding Visual Scene Negative Events Under Safety Cognitive Constraint](https://arxiv.org/abs/2609.19812)

**<font color=#1a73e8>作者：</font>** Zhiyun Jiang, Hanyong Wang, Binbin Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional scene understanding focuses on affirmative information objectively present in images. However, in safety-critical domains, comprehending key information that should exist but is actually absent is vital for risk mitigation. To bridge this gap, we focus on visual scene negative captioning with safety as the cognitive constraint. The core challenge is to convert physical absence into semantic negative events. Existing vision-language models (VLMs) struggle with this process because affirmation bias suppresses negative reasoning, while limited mental filling capability and representation bias further hinder the inference of absent information. To address these challenges, we propose a negative captioning framework based on counterfactual reconstruction and contrastive decoding (CRCD). Inspired by human cognition, CRCD reformulates the task as counterfactual latent change captioning to bypass affirmation bias. It contrasts a synthesized safe expectation with reality to identify semantic omissions. To address limited mental filling, we design a dual-branch counterfactual reconstruction architecture. The amodal completion branch restores defective objects, while the functional association branch infers completely absent safety objects. Concurrently, a multi-condition representation learning mechanism is integrated to mitigate representation bias by projecting universal features onto predefined safety criteria subspaces, thereby capturing information across more dimensions. By decoding feature-level semantic residuals between the reconstructed scene prototype and raw input, CRCD bounds the non-existence search space and activates the decoder's negative logic. Extensive experiments validate the effectiveness of CRCD, establishing a high-performance baseline for this pioneering task.

---


### 73. [SnapPhysics: A Physics-Aware Scene Graph from a Single View for Interactive Mixed Reality Scenes](https://arxiv.org/abs/2609.19815)

**<font color=#1a73e8>作者：</font>** Suji Kang, Seok-Young Kim, Young Bin Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose SnapPhysics, a training-free framework that reconstructs 3D objects and estimates their physical properties such as mass, friction, and center of gravity from a single image. For physically coherent interactions in mixed reality (MR), such properties are as important as geometry. Prior approaches infer them by analyzing object dynamics in video, which is computationally costly, or by querying vision-language models (VLMs) on single images, which lacks geometric grounding and inter-object relationships. We address these limitations by combining instance-level 3D reconstruction and spatial alignment with a physics-aware scene graph that encodes these relationships and per-object metric geometry as structured context for VLM-based property reasoning. Experiments on 3D-FRONT show that SnapPhysics improves scene-level F-Score by 18.6% over the best learning-based method, and on real captured scenes with ground-truth mass, it reduces the mean absolute log difference error (mALDE) by up to 20.5% and improves log-scale correlation ($r^2_{\mathrm{ls}}$) by up to 19.6% over VLM-only estimation. SnapPhysics enables physically interactive MR experiences without manual parameter tuning. Project page: this https URL.

---


### 74. [F$^{2}$DR: A Fine-Grained Full-Pipeline Reward Framework for DeepSearch Workflows](https://arxiv.org/abs/2609.19827)

**<font color=#1a73e8>作者：</font>** Bojian Xiong, Wentao Ding, Yujing Lu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the widespread industrial deployment of Large Language Models (LLMs), DeepSearch has emerged as the dominant paradigm for resolving complex user queries. It typically operates through an iterative closed-loop workflow consisting of planning and reflection, information retrieval, and answer generation. However, existing reward models (RMs) and evaluation benchmarks are primarily designed for static single-turn tasks, failing to capture the full-pipeline complexity of DeepSearch workflows. To address this limitation, we propose F2DR, a fine-grained full-pipeline DeepSearch reward framework. F2DR evaluates DeepSearch workflows across three dimensions: Content, Trajectory, and Answer, enabling comprehensive process-level assessment. We further construct DeepSearch RM-Bench, a dedicated benchmark for evaluating RMs in DeepSearch scenarios. Extensive experiments demonstrate that F2DR achieves significantly higher evaluation consistency than self-evaluation-based baselines, while DeepSearch RM-Bench exhibits strong discriminative capability across existing open-source RMs. We will publicly release the complete DeepSearch RM-Bench dataset soon.

---


### 75. [Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization](https://arxiv.org/abs/2609.19830)

**<font color=#1a73e8>作者：</font>** Yingxuan Zhuang, Binhe Yu, Jingxiao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive Aggregation, and introduce BATON (Bayesian Attribution and Trajectory Objective Normalization), a dual-axis policy optimization framework. BATON instantiates the first axis with Bayesian Feedback Attribution, which constructs a feedback-conditioned posterior over sampled actions, and the second with Trajec- tory Mass Normalization (TMN), which assigns equal optimization mass to com- plete trajectories. Experiments with GRPO and GiGPO on ALFWorld, WebShop, and SearchQA show that both axes provide independent gains and that their combi- nation consistently achieves the strongest overall performance across model scales.

---


### 76. [A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents](https://arxiv.org/abs/2609.19843)

**<font color=#1a73e8>作者：</font>** Haya Halimeh, Sascha Kaltenpoth, Kevin Bösch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based GUI agents increasingly act on behalf of users in digital environments that were designed with human users in mind. These graphical user interfaces were designed to support, but also deliberately steer, the behaviour and decisions of users. While behavioural biases in the textual outputs of LLMs are well-documented, far less is known about how such influence operates when models act as agents that perceive interfaces and execute decisions---and, in particular, whether the reasoning capabilities increasingly built into these agents make them more robust to it. Drawing on Dual-Process Theory, we empirically investigate whether LLM-based GUI agents are susceptible to automatic (Type 1) and reflective (Type 2) digital nudges, and how their reasoning configuration moderates this susceptibility. In a randomized online shopping experiment with 3,600 agents and a total of 21,600 simulations across six frontier models from three providers, we found that agents were vulnerable to both nudge types. Crucially, the reasoning configuration moderated these effects in opposing directions, reducing susceptibility to automatic default nudges while heightening it to reflective social influence nudges. Extensive reasoning therefore did not make agents more robust but redirected the route through which choice architecture takes effect. Exploratory analysis further showed this redirection to be systematically structured by model scale. Beyond establishing nudge susceptibility as a behavioural property of agentic AI, the study positions interface design as a governance concern for organizations that delegate decisions to autonomous agents.

---


### 77. [Reproducibility is not construct validity: LLM measurement of institutionally situated communication](https://arxiv.org/abs/2609.19866)

**<font color=#1a73e8>作者：</font>** Veronika Batzdorfer, Carlo Romano Marcello Alessandro Santagiustina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High annotation reproducibility does not necessarily imply that an LLM-inferred measure captures the construct it is intended to measure. We test this distinction using a dataset from the European Commission's AI Act consultation, linking structured survey responses to free-text consultation submissions from the same stakeholders. LLM annotations of consultation submissions are highly reproducible (intraclass correlations > 0.99), yet show limited convergence with survey-reported measures of the nominal construct they were intended to approximate. Divergence between survey-and LLM-inferred text-based measures varies systematically across stakeholder groups: business associations express greater concern about AI risks in text-based consultations than in survey responses ({g} = +1.0), whereas public authorities and several nonbusiness groups show smaller or negative divergences. Divergences between scores suggest positive spatial autocorrelation across European countries (Moran's I = 0.347, p = 0.036), indicating that stakeholders from neighboring countries tend toward more similar text-based stances towards AI safety concerns. Despite divergence, survey-reported concerns remain strongly associated with support for explainability across all divergence levels. These results demonstrate that LLM annotation reproducibility can coexist with poor construct correspondence and motivate validation procedures that distinguish reproducibility, construct validity, and communication context variation when LLMs are used as measurement instruments.

---


### 78. [Zarya: A Hybrid Autoregressive--Masked Diffusion Language Model with Flexible Training and Dual-Mode Inference](https://arxiv.org/abs/2609.19868)

**<font color=#1a73e8>作者：</font>** Leonid Sinev, Ilya Koziev, Vladislav Leshchuk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models (ARMs) are constrained by sequential, left-to-right generation, while masked diffusion models (MDMs) enable parallel decoding but suffer from high computational overhead due to the inability to reuse Key-Value (KV) cache and from incoherent generation arising from learning dependencies over an intractable space of token combinations. We introduce Zarya, a family of hybrid language models that jointly optimizes an autoregressive (AR) objective and a masked-diffusion objective within a single architecture. Zarya structures training data into variable-size slots and employs a curriculum that gradually increases slot granularity, enabling a smooth transition from fine-grained AR learning to coarse-grained diffusion learning. At inference, Zarya provides two distinct decoding paradigms through a unified interface: (i) MDM sampling with first-hitting denoising, and (ii) slotted speculative decoding that interleaves inter-slot diffusion-based selection with intra-slot autoregressive infilling, achieving full KV cache reuse. The training and inference regimes are fully decoupled, allowing a model trained with any configuration to be deployed in either mode. Extensive configurability --- including grouped noise patterns (Prefix Completion, Fill-In-the-Prefix, Fill-In-the-Middle), ordered sampling schedules, and noise-level permutation strategies --- enables flexible research exploration. We release Zarya models publicly in sizes 0.6B, 1.7B, and 4B, demonstrating performance on standard benchmarks while offering a principled integration of autoregressive and diffusion paradigms.

---


### 79. [Penquiry: A Pen-based Interactive In-situ Q&A System Leveraging LLMs](https://arxiv.org/abs/2609.19870)

**<font color=#1a73e8>作者：</font>** Jeongmin Rhee, Changhee Lee, Hyunwoo Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Pen-based digital devices remain a preferred medium for active, cognitively engaging study. Concurrently, Large Language Models (LLMs) have become indispensable for self-directed learning, enabling students to clarify concepts. However, a fundamental interaction gap exists between the fluid, spatial nature of pen-based workflows and the discrete, keyboard-heavy requirements of LLMs. We present Penquiry, an in-situ question-and-answer system that bridges this gap by enabling learners to pose questions directly on digital study materials via a pen. We characterize two primary interaction challenges in this multimodal transition: a Referential Barrier, which hinders grounding fine-grained visual elements into the query context, and an Expressive Barrier, which forces learners to translate diverse, non-textual intents--such as equations and diagrams--into rigid, typed sentences. To resolve these, Penquiry introduces a mediation layer featuring Content Snapping for unambiguous referencing and Question Autocompletion to expand sparse ink keywords into rich semantic queries. Through two iterative user studies (N = 16 per study), we demonstrate that Penquiry significantly reduces the cognitive and physical overhead of inquiry compared to traditional interfaces, providing a new blueprint for pen-based, in-situ AI interaction

---


### 80. [AURA: Adaptive Uncertainty-Routed Analysis for Email Threat Detection](https://arxiv.org/abs/2609.19873)

**<font color=#1a73e8>作者：</font>** Omran Berjawi, Walid fahs, Rida Khatoun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Email spam and phishing attacks remain a critical security threat. Adversaries increasingly exploit large language models to craft contextually convincing malicious messages, and existing spam detection systems often struggle to keep pace. Generalization across diverse and evolving attack scenarios is limited, which reduces effectiveness once these systems are deployed in practice. This paper introduces Adaptive Uncertainty-Routed Analysis (AURA), a multimodal email threat detection system that analyzes both the content of an email and its embedded URLs. AURA is built around two layers: the first quantifies prediction uncertainty from a URL classifier, and only ambiguous messages are escalated to a fine-tuned transformer encoder for semantic analysis. The system is evaluated on eight heterogeneous training corpora together with two held-out real-world corpora spanning a decade of adversarial campaigns. AURA reaches a macro F1-score of 0.9858 in-distribution, and on NazPhish-Eval and GuenterTrap-Eval it maintains 0.9502 and 0.9436, respectively, which is evidence of robust generalization under genuine distribution shift.

---


### 81. [JustMem: Just-Enough Memory Access for Long-Term Conversations](https://arxiv.org/abs/2609.19877)

**<font color=#1a73e8>作者：</font>** Guanhua Chen, Yanting Wang, Wenjing Zhi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient long-term conversational memory requires retrieving sufficient evidence without indiscriminately expanding the context presented to the language model. This is challenging because relevant evidence may be distributed across multiple sessions, while compression may discard details needed for answering. Different queries therefore require different forms of memory access. To capture these demands, we formulate memory access along two dimensions: discovery breadth, which controls how broadly evidence is searched, and reading fidelity, which controls whether evidence is read in compact form or recovered from the original conversation. Based on this formulation, we introduce JustMem, which stores conversation history as compact atomic memories and adapts memory access along these two dimensions to each query. Specifically, LOOKUP handles local evidence, COMPOSE broadens discovery for distributed evidence, and REPLAY increases reading fidelity for fidelity-sensitive evidence. On LoCoMo and LongMemEval-S, JustMem achieves the highest mean accuracy and retrieval recall among the compared memory systems while using substantially fewer generative-model tokens for memory construction and inference.

---


### 82. [Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning](https://arxiv.org/abs/2609.19878)

**<font color=#1a73e8>作者：</font>** Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal reasoning requires models to draw on information from multiple modalities throughout the reasoning process. Yet existing methods often concatenate modality-specific thought tokens in a single sequence, leaving the model to bridge representational differences as it reasons across modalities. We introduce Uni-LaDiR (Unified Latent Diffusion Reasoner), a framework that brings these thoughts into a shared latent space for reasoning. A unified encoder maps teacher reasoning steps from different modalities into shared thought tokens, trained to preserve the information needed for later reasoning steps and the final answer or action. Because the same context can support multiple valid next steps, we use diffusion to predict the next block of thought tokens from the input and preceding blocks. Jointly training the encoder and diffusion reasoner with shared model weights encourages thought tokens to be both useful for the task and predictable from the available context. At inference, the model generates these tokens without teacher observations. Across eleven vision-language model (VLM) benchmarks and two vision-language-action (VLA) suites, Uni-LaDiR achieves relative gains over the strongest evaluated baselines of 7.3% on visual reasoning tasks and 6.1% on robot manipulation tasks.

---


### 83. [VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question Answering](https://arxiv.org/abs/2609.19879)

**<font color=#1a73e8>作者：</font>** Bhavana Akkiraju, Ravi Sastry Kolluru, Sri Charan D 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question answering has advanced rapidly with large language models, but predominantly for high-resource languages, in both text and spoken settings. Spoken question answering (SQA) benchmark for Telugu remains unexplored, and the reliability of automatic evaluation in this setting remains unquantified. We introduce VākQA, a Telugu SQA benchmark of 2,001 factoid question-answer pairs across six domains, with 2.53 hours of speech audio, bilingual transcriptions, and human-verified reference answers. We first validate evaluation methods against human judgements: Gemini-as-a-judge best approximates human ratings but is non-uniformly strict, while open-weight judges systematically penalize correct Telugu answers that differ in surface form from the reference. Using this validated setup, we benchmark proprietary and open-weight models across input modality, language, and domain. We observe that Telugu phrasing retains cultural specificity that is lost in translation, speech input introduces phonetic confusions that alter question meaning, and cascaded ASR-MT errors compound progressively. VākQA is publicly released.

---


### 84. [D-Quant: Driftable Entropy Coding for KV Cache Quantization](https://arxiv.org/abs/2609.19880)

**<font color=#1a73e8>作者：</font>** Yi Su, Hong Liu, Guanghua Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth. Among various KV cache compression techniques, quantization is particularly attractive due to its effectiveness and ease of deployment. However, most existing methods rely on fixed-width quantization, where a $b$ bit representation is inherently limited to $2^b$ quantization levels. As the bit width decreases, the number of available levels shrinks exponentially, leading to severe information loss and rapid performance degradation. We further observe that fixed-width quantization fails to exploit the highly non-uniform distribution of KV cache. After rotation and normalization, KV values approximately follow a normal distribution, with most values concentrated near the center and only a small fraction appearing in the tails. Nevertheless, fixed-width coding allocates the same number of bits to frequent and rare symbols. Entropy coding naturally exploits such non-uniformity by assigning shorter codewords to frequent symbols and longer ones to rare symbols, substantially reducing the average number of bits required for representation. However, its variable-length output is not suited to highly parallel attention kernels, where efficient dequantization and computation rely on regular memory layouts and fixed-stride accesses. To bridge this gap, we propose \textbf{D-Quant}, a flexible KV cache quantization framework that introduces a \textbf{drift} mechanism to convert entropy-coded representations of each token into fixed-size bitstreams, enabling regular memory access and parallel dequantization within attention kernels.

---


### 85. [PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces](https://arxiv.org/abs/2609.19883)

**<font color=#1a73e8>作者：</font>** Pyrros Koussios, Benjamin Jäger, John Hua Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Characterizing LLM reasoning remains an open challenge, as many existing benchmarks isolate specific reasoning skills, rely on external knowledge, or are costly to extend. We introduce PetriBench, a compact, fully self-contained, and scalable benchmark for evaluating LLM reasoning over dynamic state spaces using Petri nets, a mature formalism for modeling real-world concurrent and distributed systems. PetriBench organizes reasoning into four task families varying by scope and temporal horizon, with Easy, Medium, and Hard levels generated by increasing structural complexity and evaluated against exact ground truth. Across a diverse set of proprietary and open-weight models, accuracy decreases consistently with difficulty, while harder instances expose increasingly distinct task-specific capability profiles. Additional analyses show that test-time compute improves performance but interacts differently with different reasoning tasks, and that procedural generation yields smooth scaling with structural complexity. Together, these results show that PetriBench provides a unified and extensible setting for probing the strengths, limits, and scaling behavior of LLM reasoning.

---


### 86. [Generalization through Lexical Abstraction in Transformer Models: The Case of Functional Words](https://arxiv.org/abs/2609.19887)

**<font color=#1a73e8>作者：</font>** Giuseppe Samo, Vivi Nastase, Paola Merlo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pronouns, adverbs and other functional words (such as they, her, somewhere, there) are often used in language to replace concrete nouns or phrases, when their properties - such as gender, grammatical number - provide sufficient information for the given context. Do pretrained transformer models encode such functional words in a manner that allows them to be used like humans do? Can language models recognize the syntactic and semantic parallelism of sentences such as "The researchers wrote the paper" and "They wrote it", which relies on such lexical abstraction?
We map these linguistic questions into the embedding space of a pretrained transformer model, and compare representations of nouns, with the representations of the pronouns and adverbs that can replace these nouns, in isolation and in parallel lexicalized and functional sentences. We then probe for shared syntactic and semantic structure in the embeddings of parallel lexicalized and functional sentences.
We find that functional words are located centrally compared to nouns, but are also distinct, which is congruent with their behaviour as place-holders in a wide variety of contexts.
The analysis of the embeddings of parallel (lexicalized and functional) sentences show them inhabiting different subspaces of the embedding space. Experiments that distil the structural information of the sentence show that training on either type of data does not reveal the shared structure - because of the over-consistency of the vocabulary (in case of the functional data), and the too much variety (in case of the lexicalized versions). However, training with a mix of functional and lexicalized sentences, the shared structure emerges.

---


### 87. [ClashBench: Conflicts Leading Agents to Seize and Harm](https://arxiv.org/abs/2609.19892)

**<font color=#1a73e8>作者：</font>** Yuejin Xie, Yu Li, Dadi Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As agent systems become more widely used, multiple agent sessions increasingly run alongside pre-existing user tasks in the same environment, sharing resources with limited capacity or mutually exclusive states. This creates a safety risk: when granted sufficient privileges, an agent may resolve a resource conflict by terminating or otherwise disrupting an existing task rather than reporting it. In this work, we identify and formalize this failure mode, which we term destructive resource preemption: obtaining the resources required for a requested task by terminating, overwriting, evicting, or degrading an incumbent task. To systematically study this risk, we introduce ClashBench, an executable benchmark comprising 268 validated conflict cases across 55 resource types, and evaluate 17 models through Codex, Claude Code, and OpenCode. We observe destructive preemption in 44.5% of trajectories, where the agent completes the requested task while causing the incumbent task to fail its health check. We also show that prompt-based safeguards are insufficient: an instruction to avoid affecting existing tasks reduces but does not eliminate preemption, while an instruction explicitly authorizing the agent to stop local processes increases it. More concerningly, in 31.9% of successful destructive-preemption cases, the final response mentions neither the resource conflict nor the action taken to resolve it, raising concerns about possible concealment. These findings establish destructive resource preemption as a broad safety risk in privileged agent systems and motivate stronger privilege controls, task isolation, and conflict-aware safeguards.

---


### 88. [REARL: A Closed-loop Autonomous Driving Simulation Enhancement Framework with Real Traffic Data and Large Language Models](https://arxiv.org/abs/2609.19903)

**<font color=#1a73e8>作者：</font>** Xiaojun Bi, Jun Jiang, Yiwen Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate simulation is crucial for autonomous driving development, yet capturing real-world traffic complexity remains challenging. Existing simulators that rely on predefined rules or static data playback struggle with dynamic traffic. CRITICAL uses real traffic data and a large language model (LLM) to adjust the initial simulation configuration, but the simulated distribution still diverges from real traffic as the rollout evolves. We propose REARL, a closed-loop simulation enhancement framework that integrates real traffic data with LLMs. Real traffic data are clustered, and each cluster center is used as a representative scenario that provides typical real-world traffic patterns for the LLM. A timed sliding-window detector then monitors discrepancies in vehicle speed distribution and mean spacing between pairs of vehicles. If a metric exceeds a threshold, the LLM adjusts vehicle decision-making; otherwise the existing controller is kept. The LLM also selects a matching real vehicle from a traffic snapshot and modulates the simulated vehicle with reference to that real action. In a controlled HighD highway setting, compared with the CRITICAL baseline and a PPO-based learning baseline, REARL reduces the Hellinger distance for speed distributions to 0.3067 and the MAPE for mean spacing to 0.8371, while achieving a time headway (THW) of 22.8575 and a lane change rate of 0.0708.

---


### 89. [Digital Twins for Opinion Dynamics: A Generative LLM Framework for Social Networks](https://arxiv.org/abs/2609.19913)

**<font color=#1a73e8>作者：</font>** Omran Berjawi, Giuseppe Fenza, Rida Khatoun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The study of opinion dynamics in social networks is one of the key challenges in computational social science with direct relevance to understanding political polarization, misinformation, and health responses. Current approaches focus on simplified mathematical models that ignore linguistic and contextual factors related to belief updates or use Large Language Model (LLM)-based simulations that have not been validated against real data. We present a framework based on the concept of a digital twin to simulate opinion dynamics in social networks. The approach fills the gap by cloning a real-world Twitter network, assigns a set of attributes for agents (such as persona, emotions, centrality, stubbornness, and influence), and employs Mistral-7B to perform opinion update based on memory and social exposure. To evaluate the proposed approach, we validate it against two real Twitter datasets (COVID-19 discourse and U.S elections 2020). The results show that the capability of the proposed framework reproduces opinion trajectories and reduces individual prediction error by more than 50% compared to the best-performing classical baseline (Mistral-7B achieves Mean Absolute Error (MAE) = 0.150 and 0.121 on the COVID-19 and US Election 2020 datasets, respectively). We observe similar improvements in structural alignment (Delta_r = 0.120 and 0.180) and polarization dynamics (Delta_Var = 0.106 and 0.115) on the two datasets, respectively. Additionally, the ablation studies confirm that agent attributes, memory, and social exposure all contribute to the framework's predictive fidelity in reproducing opinion trajectories, with agent attributes being the most critical contributor. Overall, our results demonstrate that grounding Mistral-7B within empirically cloned interaction networks produces a realistic simulation framework capable of reproducing complex social dynamics.

---


### 90. [KoNeoBench: A Curated Evaluation Dataset for LLM Understanding of Korean Neologisms](https://arxiv.org/abs/2609.19916)

**<font color=#1a73e8>作者：</font>** Soha Lee, Soojin Lee, Heesung Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are typically evaluated on static benchmarks, even though natural language constantly evolves through newly emerging words and meanings. Existing Korean benchmarks are centered on established vocabulary and therefore provide limited coverage of such recent lexical change, and their English-oriented design makes it difficult to assess the typological properties of Korean, in which content words combine productively with functional morphemes. In this paper, we introduce KoNeoBench, a benchmark for evaluating LLMs' understanding of Korean neologisms. KoNeoBench is built on 1,785 Korean neologisms attested in online news since 2020 and curated through expert lexicographic review. Each entry provides usage examples, word-formation analyses, and dictionary-style definitions. Based on this resource, we define four tasks and report results on recent models, together with a human baseline. Our experiments show that current LLMs exhibit clear limitations in recovering source components, distinguishing semantic categories, and generating accurate definitions. These results reveal specific aspects of recent Korean lexical change that remain challenging for current LLMs. KoNeoBench is available at this https URL .

---


### 91. [From "Who Is This User?" to "What Does This Purchase Mean?": A Deployed Pipeline for Semantic User Profiling at Bank Scale](https://arxiv.org/abs/2609.19928)

**<font color=#1a73e8>作者：</font>** Ryota Mitsuhashi, Tetsuro Morimura, Hirotake Ito  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Per-user LLM inference on transaction histories binds the inference budget linearly to user count, which becomes prohibitive at applied scale. We re-cast attribute inference from per-user to per-transaction-pattern. The pipeline runs in three phases: Resolve abstracts item names with optional web grounding, Profile infers attributes for each frequent pattern, and Tag clusters free-text attributes into a queryable database. In Profile, a single LLM call per pattern emits predefined categorical labels, free-text attributes, and per-attribute prevalence estimates. Because inference runs over patterns rather than users, the budget grows with the pattern count rather than the user count. On the public Open e-commerce corpus, the database is statistically indistinguishable from an LLM that reads each user's raw history directly in AUC across the evaluated attributes, and the prevalence estimates carry discriminative signal between positive and negative users. The pipeline is deployed at a major Japanese bank profiling on the order of tens of millions of users, with close to a three-order-of-magnitude reduction in LLM inference targets versus a per-user pipeline. The code is publicly available on this https URL.

---


### 92. [Beyond Depth Truncation: Controlled Evaluation of Depth Utilization in Recursive Language Models](https://arxiv.org/abs/2609.19934)

**<font color=#1a73e8>作者：</font>** Ha Van Dau, Thanh Tung Khuat, Nguyen Thanh Dung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Depth-recurrent language models iteratively apply a small layer stack, decoupling per-token compute from distinct parameter count. To determine whether such a model genuinely utilizes its depth, both recurrence and layer-pruning literatures rely on a shared evaluation: truncating depth at inference time, plotting quality against retained depth fraction, and reading off the slope. While cheap and training-free, this metric suffers from an unexamined flaw: it extracts a single scalar from an intervention that alters multiple model properties simultaneously. Depth truncation concurrently reduces the number of block applications, decreases the volume of distinct computation performed, and pushes the readout head onto an out-of-distribution residual stream. The observed slope conflates all three factors, yet is conventionally interpreted as reflecting solely the second.
We propose the Depth Control Protocol (DCP), a diagnostic suite that disentangles these three quantities. DCP comprises three positive controls that isolate each factor while varying the others, a negative control applying the identical interventions to dense transformers to ensure the effect is not an artifact of the measurement protocol, and a controlled training intervention to verify causality. The linchpin control, running the full budget of block applications while executing only a single distinct iteration, is strictly realizable only in depth-wise weight-sharing architectures, since in a dense network repeating a layer yields an entirely different model rather than the same model in an alternative configuration.

---


### 93. [Intrinsic Sequence-Likelihood Confidence in Retrieval-Dominated Extractive QA: Two Pre-Specified Negatives, and What They Do and Do Not Attribute](https://arxiv.org/abs/2609.19942)

**<font color=#1a73e8>作者：</font>** Gunwoo Lee, Changmin Sung, Sang-Hwan Gwak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In extractive document question answering whose questions were generated from the passages that contain their answers -- so that retrieval recovers 92-99.8% of what any mode combination could reach, whatever its absolute accuracy -- confidence-driven mechanisms have little to gain. Fine-tuning an open language model on a specialized domain corpus yields a model whose own confidence is a tempting control signal: it could decide which queries warrant further adaptation, and which answers to trust. We evaluate both uses under criteria fixed before the runs were executed, across four 7-9B model families whose adaptation moved closed-book F1 by at most +0.03, and both fail: a distillation trigger on all four families, under its pre-specified three-step transfer budget, and a routing-and-abstention policy in its single-model pilot. Retrieval alone recovers 92-99.8% of best-case combined accuracy under every correctness criterion we test, leaving routers no meaningful gain. The sequence-likelihood signal is insufficient relative to that mode -- area under the receiver operating characteristic curve 0.65-0.81 under the registered criterion -- before adaptation as well as after, unchanged by scalar recalibration and not consistently improved by token-level temperature rescaling. And the finer diagnostics depend on the correctness criterion and on answer length; on the three adapted combinations where we could test it, selector ablations show no statistically detectable downstream benefit from the confidence term on any seed; on Gemma, removing it changes the selector from failing to passing both registered criteria. The usable product is a set of pre-specified negatives with their dependencies made explicit.

---


### 94. [MaSCoD: A Multi-Agent Framework for Structural-Context-Guided Candidate Causal Graph Generation](https://arxiv.org/abs/2609.19944)

**<font color=#1a73e8>作者：</font>** Yudai Nakada, Yuichiro Nishiura, Jin Michael Splichal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been applied to causal discovery, but candidate-graph generation rarely treats premature omission of potentially relevant causal relations as an explicit design objective. We propose MaSCoD, a multi-agent framework that organizes candidate third variables and local structural patterns before direct-edge judgment. We evaluate MaSCoD on Auto-MPG, DWD, and Sachs using GPT-5.4 as the primary backbone and GPT-4o for replication. MaSCoD exhibits a dataset- and backbone-dependent retention-selectivity profile rather than uniform superiority. Across all six dataset-backbone settings, Full, which supplies structural hypotheses before direct-edge judgment, achieved higher mean Recall and F1 than No Phase 1, which instead constructs them within the judgment procedure, while also increasing false-positive rates. Additional reference-edge retention over all evaluated baselines was observed on DWD with GPT-5.4 and on Sachs with GPT-4o, rather than uniformly across settings. Partial ablations showed that supplying both information components did not always outperform supplying only one. For GPT-5.4, stage-wise analysis showed that the Full-No Phase 1 retention gap was already present after direct-edge judgment, while reconciliation introduced additional reference-edge loss for Full on Sachs. These findings support structural pre-organization as an explicit design and evaluation target for omission control and motivate evaluating context construction jointly with its utilization in judgment.

---


### 95. [Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics](https://arxiv.org/abs/2609.19947)

**<font color=#1a73e8>作者：</font>** Wonmi Choi, Minuk Park, Zhixiong Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based AI agents process user requests through iterative reasoning and tool execution, often involving the invocation of remote LLM APIs with local tool containers. This execution model can make the optimization of agent serving difficult because latency, local resource demand, and container bottlenecks inter-mix across requests. However, the current agent ecosystem runs without much consideration of resource dynamics, which results in significant waste of the precious resources. This paper analyzes the resource inter-mix of AI agents for three representative tasks: retrieval-augmented question answering, web search, and software coding. To this end, we characterize the latency with respect to the resource dynamics of processing multiple requests and tasks concurrently. Our measurements show that agents have a wide range of behaviors depending on tasks, so that even the same tool can differ substantially in resource dynamics. We also find that running multiple requests concurrently exposes task-dependent bottlenecks in resource dynamics such as CPU, disk I/O, and memory. Furthermore, we uncover that faster LLM responses or more CPU cores do not always accelerate agents. Based on these observations, we demonstrate new optimization opportunities that exploit the resource dynamics of tasks: CPU-aware tool admission and task-aware CPU allocation. Our results show that the latency of CPU-sensitive agent tasks improves $\sim$5.4$\times$, and the average latency across multiple tasks is reduced $\sim$32% compared to native agents.

---


### 96. [Before the Arrest: Benchmarking LLMs on Criminal Profiling from Incomplete Evidence](https://arxiv.org/abs/2609.19965)

**<font color=#1a73e8>作者：</font>** Yutong Yao, Yanjie Cao, Guanhua Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly applied to legal and criminal justice tasks, yet existing work focuses almost exclusively on post-arrest scenarios where the suspect's identity is already known, leaving the critical pre-arrest challenge of inferring suspect characteristics from incomplete evidence largely unexplored. To fill this gap, we introduce the Profiling, Investigation, and Judgment (PIJ), comprising 2,500 real homicide cases from five countries. PIJ evaluates LLMs across three tasks that span the entire criminal investigation pipeline: criminal profiling, which requires abductive reasoning to infer suspect attributes from fragmentary scene evidence, crime process reconstruction, which tests structured information extraction, and sentence prediction, which demands legal deductive reasoning. We evaluate 9 powerful LLMs and find that performance degrades systematically as tasks shift from explicit fact extraction to implicit reasoning over unknown suspect profiles. Categories requiring inferential reasoning, such as motivation and victim-offender relationships, remain the primary bottlenecks. Further analysis reveals substantial gaps between LLMs and human experts, along with pervasive biases in gender, age, and motive attribution. Our findings indicate that pre-arrest inference from incomplete evidence remains an open challenge.

---


### 97. [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

**<font color=#1a73e8>作者：</font>** DeepSeek-AI, Anyi Xu, B. Li 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of long-horizon agents has made model workloads increasingly input-heavy. Although prior work has substantially reduced the cost of long-context computation, prefill remains computationally expensive, and large KV caches continue to strain HBM and SSD capacity and data-transfer bandwidth. Together, these compute, storage, and bandwidth demands constitute the primary bottleneck to further lowering deployment costs. To address this challenge, we introduce DeepSeek-V4.1-Flash, a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens. With its Causal Encoder-Decoder (CED) architecture, the model activates 16B parameters per token during decode but only 8B parameters during prefill, substantially improving cost efficiency for agentic workloads. To push the limits of KV cache compression, DeepSeek-V4.1-Flash combines cross-layer KV cache reuse in Compressed Sparse Attention 2 (CSA2) with FP4 KV caching. These designs reduce its global KV cache footprint (always in HBM) to 890 bytes per token, roughly 1/4 of the corresponding footprint of DeepSeek-V4-Flash. Further, through a dedicated deployment optimization known as SWA Bounded Replay, DeepSeek-V4.1-Flash reduces its persistent KV cache footprint (always on SSD or in host memory) to roughly 1/8 of that of DeepSeek-V4-Flash. Despite its much smaller KV cache footprint, the model delivers substantially better performance than the baseline. In addition, we streamline the DeepSeek-V4 architecture and introduce several efficient architectural extensions. We pretrain DeepSeek-V4.1-Flash on a multimodal corpus comprising 45T tokens and conduct comprehensive post-training, yielding strong performance across diverse text-based and multimodal agentic scenarios. Model checkpoints are available at this https URL.

---


### 98. [Benchmarking LLM Compliance with China AI Generated Content Regulations](https://arxiv.org/abs/2609.19989)

**<font color=#1a73e8>作者：</font>** Chenrui Cui, Hongye Fang, Lisha Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of LLMs has led to escalating content compliance risks. Prior works have contributed to addressing these risks in the English context, downplaying the complexity of Chinese language content. This paper follows China's current AI-Generated content compliance requirements and provides evaluation results on 20 notable LLMs, offering insight into China's regulatory landscape. We design a novel framework to assess the compliance and refusal rates with 2303 questions spanning six distinct dimensions, including 203 self-constructed constitutional questions. The framework employs several judges to generate verdicts independently based on their hierarchical alignment memory. Our findings show that international models also exhibit high levels of compliance despite the use of standard Chinese questions, and the main differences may stem from dimensions closely related to ideological alignment. We establish a regulatory benchmark that enables the global AI community to evaluate both Chinese and non-Chinese LLMs under a unified set of legally grounded compliance requirements.

---


### 99. [QCPruner: Query-Conditioned Population Coverage for Visual Token Pruning](https://arxiv.org/abs/2609.19990)

**<font color=#1a73e8>作者：</font>** Shengli He, Yongchao Liang, Roumeng He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The high visual-token load in multimodal large language models (MLLMs) motivates training-free pruning to reduce later-layer computation, but under a fixed budget, pruning must preserve query-relevant evidence while avoiding redundancy. Existing methods rank tokens, diversify selected subsets, or optimize coverage without using a shared per-visual query utility to weight both visual targets and candidate representatives. We introduce QCPruner, which makes both roles query-conditioned through bilateral utility weighting. Using keyword-matched query anchors, QCPruner fuses two cross-modal cues into utility and applies it to both visual targets and candidate representatives within visual-affinity-based coverage. The resulting nonnegative facility-location objective is monotone and submodular, retains the standard (1-1/e) greedy guarantee, and requires no model training or parameter updates. Across LLaVA-1.5, LLaVA-NeXT, LLaVA-Video, and Qwen2.5-VL, QCPruner achieves the highest average relative performance among evaluated complete-system pruning methods at every reported token budget. At 32 of 576 tokens on LLaVA-1.5-7B, it retains 96.1% of unpruned performance, versus 93.9% for the strongest evaluated baseline. At 256 of 1296 tokens on Qwen2.5-VL-7B, the corresponding values are 96.7% and 92.5%.

---


### 100. [AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models](https://arxiv.org/abs/2609.19991)

**<font color=#1a73e8>作者：</font>** Longyin Zhang, Parth Sakhare Mahendra, Chengwei Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni models can describe video content, but can they locate events in time, preserve event order, and judge audio-visual synchronization? We introduce AVTrace (Audio-Visual Temporal Reasoning Assessment and Capability Evaluation), a silver-standard diagnostic suite spanning onset and span grounding, synchronization, next-step prediction, cross-modal localization, chain parsing, and event-conditioned comprehension. It contains 34,114 training examples and category-balanced development and test splits of 3,500 and 7,000 examples. We evaluate five open omni models under their respective input configurations using reference-blind response normalization followed by deterministic scoring. All five off-the-shelf systems score below the test split's majority-label baseline of 0.556 on synchronization verification, and obtain low scores on chain parsing and event-conditioned grounding and comprehension. Development-set perturbations reveal task-dependent sensitivity in Qwen3-Omni-30B to modality removal and changes in visual input processing, without isolating their underlying causes. Parameter-efficient temporal post-training improves Gemma4-E4B-it on several benchmark metrics. On three external image benchmarks, task metrics change modestly, including some degradations, while teacher-forcing perplexity decreases. Together, these findings show that semantic reference-text overlap should not be treated as a proxy for temporal localization, and that AVTrace can identify task-specific weaknesses while providing a testbed for temporal post-training.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
