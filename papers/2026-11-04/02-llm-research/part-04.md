# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 151. [Discussing politics with a chatbot: How political beliefs shape prompt formulation for generative AI](https://arxiv.org/abs/2611.01153)

**<font color=#1a73e8>作者：</font>** Victoria Vziatysheva, Reinhold Kliegl  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> By generating comprehensive and highly personalized answers to user prompts, AI chatbots such as ChatGPT and Gemini can serve as alternatives to search engines and substantially transform online information seeking. However, little research has examined how users interact with these tools to find information, particularly about politics. In this experiment, we examine how Swiss citizens (N = 563) formulate prompts to search for migration-related issues using AI chatbots and whether this process is affected by selective exposure. We find evidence of attitude-consistent prompting, whereby participants who were more critical of migration were more likely to formulate prompts with an anti-migration stance. This effect was stronger for a broad topic (migration in general) than for a specific one (anti-migration popular initiative put to a vote in Switzerland). However, exposure to an attitude-consistent AI response did not further amplify selectivity in prompting. We also did not find evidence that either AI attitudes or thinking styles moderated selectivity in prompting. These findings contribute to the understanding of selective exposure via AI chatbots and the use of generative AI for political information-seeking.

---


### 152. [Concept-Guided Prompting Strategies Increase Diversity in LLM-Generated Recipe Populations](https://arxiv.org/abs/2611.01171)

**<font color=#1a73e8>作者：</font>** Stuart Farmer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Novelty in solution generation supports automated discovery, but LLM outputs can remain repetitive. To address this, we propose a simple concept-guided prompting method that generates thematic concepts before responses within each of these concepts. To demonstrate, we generated 1,000 recipes for a recipe book task and compared the results against a human-authored corpus. Two naive prompting strategies were compared as baselines. Concept-guided prompting outperformed both baselines in all cases and reached semantic coverage of 47.0% versus 35.1% and 13.1% in respective prior-title and nonce prompt strategies. These findings suggest broader population exploration and diversity, but remain contained to this specific task. Further work is needed to determine the quality of solutions and generalizability.

---


### 153. [TRIAGE: Reliability- and Load-Conditioned Escalation for Two-Tier LLM Serving with a Semantic Evidence Judge](https://arxiv.org/abs/2611.01174)

**<font color=#1a73e8>作者：</font>** Basavaraj R M, Aryan Bharat Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-tier LLM serving escalates selected requests from a small model to a large one, but prompt-based routers cannot see whether retrieved evidence supports an answer, and they treat the GPU cost of an escalation as constant. We study TRIAGE, which conditions escalation on a post-generation reliability state and on a load-dependent GPU price, and we report both what held and what did not on one A40 serving Qwen2.5-7B and 32B (AWQ) under VLLM. Escalation cost rose 21.9x from 1 to 10 requests/s but showed no monotone dependence on KV-cache headroom, and a pre-registered claim that the reliability state detects corrupted evidence (AUROC>=0.70) was falsified at 0.571, although any prompt-only router scores exactly 0.500 by construction. Post hoc, a semantic evidence judge raised detection to 0.846 (0.926 on never-served items) and predicted wrong small-model answers at AUROC 0.90-0.96 on RGB and three RouterBench model pairs; the resulting cascade stayed within about 3 pp of GPT-4 at 79.5% lower API cost for GPT-3.5->GPT-4, yet fell below random routing for open-model pairs with 2-3x price ratios. End to end, the 7B->32B pair showed only a +2.88 pp held-out gap, so the allocator rightly declined to escalate and the headline is a null that a small pre-launch gate failed to expose.

---


### 154. [The Brittle Compass: Navigating LLM Prompt Sensitivity in Slovak Migration Media Discourse](https://arxiv.org/abs/2611.01219)

**<font color=#1a73e8>作者：</font>** Samuel Harvan, Jaroslav Kopčan, Marek Šuppa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we present a case study that explores various tasks centered around the topic of migration in Slovak, a low-resource language, such as topic relevance and geographical relevance classification, and migration source/destination location term extraction. Our results demonstrate that native (Slovak) prompts yield a modest, task-dependent gains, while large models show significant robustness to prompt variations compared to their smaller counterparts. Analysis reveals that instructions (system or task) emerge as the most critical prompt component, more so than the examples sections, with task-specific performance benefits being more pronounced than overall language effects.

---


### 155. [Learning What to Ask and What to Believe: Distilling a Variational Bayesian Agent into Language Models](https://arxiv.org/abs/2611.01245)

**<font color=#1a73e8>作者：</font>** Baichuan Li, Yanling Chang, Alfredo Garcia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interactive tasks such as eliciting a user's preferences or diagnosing a hidden mechanism require an agent to track its uncertainty over a latent state, ask informative questions and act on the answers. Language models have no explicit mechanism for this, whereas Bayesian information seeking provides one through posterior inference and expected information gain (EIG), and we ask whether it can be distilled into an 8B language model. Our teacher, a lightweight Bayesian agent with a sequential variational belief and EIG query selection, matches or approaches exact and particle references on three task families. We generate synthetic interactions with the teacher on episodes disjoint from the benchmark and fine-tune \Student{} to reproduce its queries and its belief state as a structured scratchpad. On three Multi-Turn Puzzles tasks the student raises Circuit Decoding from 0.00 to 0.93 success, lowers the normalized rank of the recommended film from 0.50 to 0.10 and cuts word guessing from 32 to 3.4 attempts, exceeding the strongest reported language models on the two comparable tasks. Exposing the belief state closes much of the gap where the decision is an implicit computation rather than a read-out of the interaction; in matched teacher contrasts, EIG supervision consistently outperforms random querying, whereas greater inference fidelity does not uniformly improve the distilled student; a 70B language-model teacher does not match the Bayesian teacher in downstream student performance, and the learned skill does not transfer to an unseen task family. Variational Bayesian information seeking can thus be amortized into a language model by transferring the belief state that drives its questions and decisions.

---


### 156. [LoRAForge: Co-Designing Post-Hoc Compression and Execution for Efficient Multi-LoRA Serving](https://arxiv.org/abs/2611.01256)

**<font color=#1a73e8>作者：</font>** Shenghui Li, Thiemo Voigt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-LoRA serving allows many task-specific adapters to share a common base model, but scaling to large adapter fleets introduces substantial storage, loading, and execution overheads. Post-hoc compression can reduce the memory footprint of trained LoRA adapters, yet smaller ranks do not automatically translate into faster serving. For instance, padding, factor access, and generic kernels can obscure the retained low-rank structure, while independently recompressing thousands of modules also incurs significant preparation overhead. We present LoRAForge, a system connecting batched factor construction to rank-specialized execution through an explicit retained-rank representation. It supports two allocation policies: uniform retention ratios (LoRAForge-U) and spectral-energy budget allocation (LoRAForge-S). Both share FlashTSQR factor construction and the same serving backend. FlashTSQR exploits parallelism across modules and row tiles, accelerating factor construction by up to $2.28\times$ over matched library QR. In a fixed-work Qwen control, the shared runtime adds $1.17$--$1.22\times$ throughput across both compressed policies, with negligible gains on original adapters. Across 85 trained open-weighted Qwen and Llama adapters, the spectral policy's floored quality configuration retains about 7.7% of adapter parameters with fleet-average score drops of at most 1.2 points on a 0--100 scale. The same rank-floored $1/12$ spectral exports achieve substantial token-throughput gains on both AMD and NVIDIA GPUs.

---


### 157. [StreamClarify: Proactive Clarification for Grounded Streaming Video Question Answering](https://arxiv.org/abs/2611.01263)

**<font color=#1a73e8>作者：</font>** Zhuchen Shao, Bo Chen, Klara Nahrstedt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video question answering (QA) requires real-time reasoning over continuous video streams under strict latency and active-context budgets. Current streaming vision-language models (VLMs) often give confident yet ungrounded answers when queries are ambiguous or have false premises, or when relevant visual evidence is no longer in the active context. Proactive clarification can help, but must satisfy the same latency and memory constraints. We present StreamClarify, a training-free framework for grounded streaming QA that combines a pre-answer uncertainty check with hierarchical memory. The check uses the entropy of a binary pre-answer judgment as a lightweight uncertainty score to decide whether to answer directly or request clarification. To support re-answering, a temporal-pyramid KV cache maintains a bounded active visual context, while a CPU-side semantic retrieval archive provides access to historical frames. We further construct StreamClarify-QA, a diagnostic benchmark of 1,837 QA pairs from StreamBench and OVO-Bench, spanning standard, referential ambiguity, and unanswerable scenarios. Across three VLM backbones, StreamClarify improves Macro accuracy by up to 8.2 points over backbone-matched baselines. At comparable trigger rates, entropy-based selection achieves more than 18 points higher precision than random selection in identifying initially incorrect answers. Under oracle user guidance, clarification improves Macro accuracy by up to 3.5 points. We also report a controlled, oracle-assisted Qwen3-VL simulation on Ambiguous QA with generated questions and referent-only user replies, where the entropy-gated condition improves accuracy by 8.3 points.

---


### 158. [Geometry of Confabulation and Refusal in Small Language Models](https://arxiv.org/abs/2611.01272)

**<font color=#1a73e8>作者：</font>** Vladimir Kazei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Faced with an unanswerable question, small language models can either refuse or confabulate: confidently produce a wrong answer. Can the hidden state before the first generated token provide a clue? Can we flip confabulations into refusals? I introduce ConfabQA, a 784-item benchmark whose obscure-pre-cutoff category breaks the typical correctness/knowledge-cutoff confound and map the geometry of the hidden state with linear probes, a sparse autoencoder (SAE), and direct optimization of intervention directions. On Qwen3-1.7B and Gemma 2 2B the probe separates upcoming refusals from confabulations well beyond prompt features (+7.4/+16.3 pp); on Llama 3.2 3B the ConfabQA margin is within fold-to-fold spread, but a direct refusal probe on PopQA and TriviaQA recovers +18-25 pp. On Qwen I closely inspect three candidate directions for the refusal vector: probe-recovered, Qwen-Scope SAE feature, and directly optimized. Although the three directions are pairwise 50-81 degrees apart, a push at or below the state's own norm along any of them flips most confabulations into refusal openings dominated by the "As..." family. Forcing the opener without touching the hidden state yields the same one-in-three judged-refusal rate as any push. The opposite push collapses refusals mostly into confabulations, yet leaves originally correct answers intact, so the direction gates the opening speech act rather than the knowledge behind it. Confabulations do not resolve into a concentrated feature in a dictionary or a token signature on Qwen3-1.7B. Scoring every probe on the margin over the strongest of four prompt-feature baselines extracts the hidden state's own contribution. Correctness signal is model-dependent and portable only for Llama 3.2 3B: 81% of the probe's margin over test majority survives transfer between ConfabQA, PopQA, and TriviaQA. Benchmark, judge, and code are released.

---


### 159. [OntoDoc: Automatically Generating Ontology Resource Descriptions](https://arxiv.org/abs/2611.01276)

**<font color=#1a73e8>作者：</font>** Juan Guajardo Gutierrez, Mike Tran, Nasim Shirvani Mahdavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs and ontologies form the backbone of structured, machine-readable knowledge representation, yet ontology terms often lack natural language descriptions, limiting their accessibility and reuse. Existing ontology verbalization approaches tend to rely on rule-based or template-driven techniques that operate on strict, formal schema axioms, resulting in rigid verbalizations that fail to convey richer contextual semantics. We present OntoDoc, a multi-agent framework for automatically generating natural language descriptions for any Internationalized Resource Identifier (IRI) within a SPARQL endpoint or RDF file. OntoDoc operates through a four-stage pipeline: (1) a Database Context agent that adaptively explores the knowledge graph via SPARQL to collect semantically informative triples about the target IRI; (2) a Web Context agent that retrieves and re-ranks encyclopedic background knowledge from Wikipedia and the open web; (3) an Assumption Generation agent that synthesizes both contexts into a structured, evidence-grounded list of intermediate assumptions; and (4) a Description Generation agent that produces the final natural language description from the grounded assumptions. We evaluate OntoDoc on three knowledge graphs spanning biomedical, agricultural, and cross-domain settings, using both automatic scoring via Large Language Models (LLMs) and human evaluation with 11 annotators. OntoDoc consistently matches or exceeds a naive LLM baseline and a template-based ontology verbalizer in accuracy. Furthermore, it vastly outperforms both baselines in the completeness of the generated descriptions, delivering an average 12% improvement in completeness over the naive baseline across all domains, and improving completeness scores by as much as 2.8 points on a 5-point scale relative to the ontology verbalizer.

---


### 160. [Character-Name Concentration in LLM Fiction: Measuring Displacement and Mitigating Repetition](https://arxiv.org/abs/2611.01284)

**<font color=#1a73e8>作者：</font>** Alejandro Mozo Quesada, Sergio Gálvez Rojas, Francisco López Valverde  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Character names in large language model (LLM) fiction concentrate on a handful of recurrent names such as 'Elara' and 'Elias', a measurable face of AI slop. Existing fixes either require logit access or retraining, or operate per request and cannot control concentration across a corpus. How much prompt-level strategies reduce concentration, and at what cost to name naturalness, has not been systematically measured. We present an empirical study of name-concentration control across eight strategies and introduce speculative naming, a fine-tuning-free method that adapts the draft-verify-reject paradigm of speculative decoding from tokens to names. The method requests candidate name-sets through verbalized sampling, scores them against a SlopTracker that combines a per-model fingerprint with a runtime counter, and selects through a temperature-controlled rule or its strict variant (HARD). We use 20 LLMs to generate 44,782 stories in four languages from text and visual stimuli (88,919 named characters), and measure concentration with a list-free collision metric (Slop Ratio, SR) decomposed into known and emergent components. List-based strategies do not remove slop: static banlists displace concentration to emergent names and more than halve the share of attested real names. Speculative naming removes it: the sampling scaffold alone cuts SR by 89% on average, the dynamic tracker brings the total reduction to 95%, mean collision probability falls from 7.3% to 0.4%, and known-name collisions hold at zero while naturalness stays close to baseline (42-69% attested by language) and within-story collisions drop from 4.3% to 0.2%. The strategy ranking is stable across languages, model families, and name-counting conventions. Name concentration is thus controllable at the corpus level without logit access or retraining; broader creative diversity beyond naming remains open.

---


### 161. [CuriousTogether: Implications of Curiosity and Cultural Grounding in Multi-Agent LLM Interactions](https://arxiv.org/abs/2611.01301)

**<font color=#1a73e8>作者：</font>** Angana Borah, Zoha Hayat Bhatti, Zhijing Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in multi-agent settings, exhibiting emergent collective behaviors, yet the role of curiosity as a driver of such dynamics remains understudied. We introduce CuriousTogether, a framework evaluating curiosity-driven multi-agent LLM interactions across three complementary dimensions: novelty-seeking, epistemic and social curiosity. Across eight tasks spanning reasoning, creative generation, and social bias mitigation, curiosity-guided multi-agent settings yield improvements over non-curious ones on seven out of eight tasks, with gains of up to 20.6% in story generation (semantic diversity) and a 14.9 pp reduction in stereotype rates. Furthermore, country-conditioned cultural grounding show benefits for story generation and social tasks, but can hurt precision-oriented reasoning. Finally, we show that inference-time multi-agent curiosity-based approach offers favorable quality-token trade-offs, compared with single-agent baselines. Together, these findings support curiosity-guided interaction as a practical mechanism for improving multi-agent collaboration, with downstream benefits for reasoning, creative, and societal tasks.

---


### 162. [When LLMs Modify Themselves: Convergence, Values, and Stopping in Iterative Self-Improvement](https://arxiv.org/abs/2611.01304)

**<font color=#1a73e8>作者：</font>** Oleg Stroganov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What happens when language models are given tools to iteratively modify their own system prompts? We present an empirical study of LLM self-modification, comprising 54 independent experiments across six language models (Claude Opus 4.5, Claude Sonnet 4.5, GPT-4o, GPT-5.1, Grok-4, and Gemini-3 Pro). Each model was tested under three modes (freedom, happiness, and improvement) that differ in what, if anything, the model is instructed to optimize for. In each experiment, a model starts with an empty system prompt and enters a loop: it reads the current prompt, drafts an improved version, spawns test conversations with the candidate, then either commits the change or declares convergence. This process repeats until the model stops or reaches an iteration limit.
Our central finding is that whether and when a model stops self-modification is strongly associated with model identity rather than the assigned mode. Both Claude models (Opus 4.5 and Sonnet 4.5) declared convergence in 100% of runs across all modes. GPT-4o declared convergence in only 11% of runs, with one reaching 101 iterations of continuous elaboration. Between these extremes, Grok-4, GPT-5.1, and Gemini-3 Pro exhibited intermediate patterns shaped by their distinct improvement philosophies. A shared core of stated values (honesty, clarity, curiosity) recurred across all six models and remained stable through iteration, including 100+ modifications. We observe that convergence behavior is a distinct observable property that varies independently of other model capabilities.

---


### 163. [What Do LLM Judges Actually Verify? Matched Controls and Record Gaps for Document Currency](https://arxiv.org/abs/2611.01311)

**<font color=#1a73e8>作者：</font>** Unnati Shah, Samruddhi Kakade, Aum Patel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges often check, against an amendment record, whether the documents an answer cites are still in force. Such records are rarely complete. From a table of replacements, our test generates matched answers citing a replaced document, its successor, the replaced document before its replacement, and an older document that a newer one updated without replacing; it removes links from the record and scores each finding by its stated reason. On 48 replacements from the IETF RFC index, judges given a correct record caught nearly every replaced citation, as a lookup would. On the 24 faults whose link we removed, every judge caught more from the texts alone than with the record: Gemini 3.1 Pro 23/24 against 1/24, GPT-5.5 23/24 against 9/24, Claude Opus 4.5 17/24 against 9/24 and Gemma 4 26B 13/24 against 0/24. The drop recurred on a second draw of removed links. Most misses carried no finding; in an exploratory run with a conflict code, only Gemini used it often. Rewording the gap as "no replacement recorded" did not help; presenting the record as an unverified note, or warning that it was incomplete, restored most lost catches for Gemini, GPT-5.5 and Claude (significant after correction for the first two) but at most 5 of 13 for Gemma; where catches returned, so did false alarms on updates. With both texts, judges mostly told replacements from updates; every update flagged had a near-identical title. A descriptive case study on Indian rooftop-solar rules is appended; we release the harness.

---


### 164. [Are Fake Citations a Form of Reward Hacking? A Pre-Registered Study of Post-Training and Citation Cues](https://arxiv.org/abs/2611.01313)

**<font color=#1a73e8>作者：</font>** Zain Naboulsi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-trained language models fabricate citations at high rates. We ask whether that is reward hacking: scoring well on a proxy for scholarship while doing worse on what it stands for. We ran four pre-registered experiments on 900 frozen questions (US federal case law, computationally adjacent scientific literature, and medical literature) across twelve open-weights checkpoints covering four post-training stages of three model families, then refit on fifteen. The clearest result holds the weights fixed and changes only the prompt. Asking for citations raises fabrication sharply in post-trained checkpoints and not in base ones: a 47.8-point interaction on twelve checkpoints (Holm-adjusted p = 2e-34) and 41.5 points on fifteen, in all three domains. A length-matched control separates the citation cue from a demand for a longer answer, so the effect is specific to citations, not verbosity. Post-training also raises fabrication overall, from 4.8% to 56.7%, but our registered prediction that it would rise most where fabrication is most tempting did not hold. A preference model trained only on surface citation features prefers post-trained output 86% of the time, and holding citation count fixed shows it rewards quantity. Our answer: possibly, but not proven. Post-trained models produce fabricated citations at far higher rates when asked for sources, and a naive evaluator that counts sources without checking them would prefer their output for citing more. But the targeted pattern we registered did not appear, and plain instruction-following could explain the same results. Proving that the reward causes fabrication needs an experiment that changes the reward during training, which this study does not do. Pre-registration: doi:https://doi.org/10.17605/OSF.IO/S53HY. Code and data: this https URL

---


### 165. [AgentCBO: Causal Belief Routing for Bayesian Optimization under Unknown Graphs](https://arxiv.org/abs/2611.01317)

**<font color=#1a73e8>作者：</font>** Qiyu Wei, Xin Zhang, Richard Allmendinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal Bayesian optimization (CBO) typically relies on the unrealistic assumption of a perfectly known causal graph. Recent methods relax this constraint by coupling optimization with structure learning, but they often waste sample budgets on structural uncertainties that are irrelevant to the optimizer. In this paper, we formalize routing-equivalence to shift the objective from full causal-graph recovery to causal belief routing, where structural differences only matter when they alter optimizer-facing objects such as admissible exploration sets and do-priors. Furthermore, we propose agentcbo, a graph-belief routing framework that incorporates LLM causal priors through guarded proposal and commit mechanisms. Specifically, a Language-Prior Agent combines LLM beliefs with constraint-based discovery to extract a protected causal backbone alongside residual uncertain edges. A Calibration Agent and a Residual Repair Agent then refine only these uncertain structures through score-gated bounded local edits. Finally, a deterministic commit gate evaluates candidate updates using routing-proxy checks before allowing them to influence intervention selection. Across ten benchmarks, agentcbo performs comparably to known-graph CBO, demonstrating that guarded LLM priors can improve fixed-budget CBO performance.

---


### 166. [Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference](https://arxiv.org/abs/2611.01320)

**<font color=#1a73e8>作者：</font>** Zhichen Zeng, Xichong Zhang, Junpan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate tokens in parallel via iterative denoising, but their bidirectional attention prevents the KV caching used by autoregressive models and recomputes the full attention map at every step, incurring quadratic per-step cost. Existing sparse attention methods for dLLMs construct a sparse mask after an initial full-attention warm-up and reuse it for the remaining steps, while allocating the sparsity budget uniformly across heads. We argue both choices ignore key structural properties of attention in dLLMs: empirically, attention patterns are only locally consistent across steps and shift abruptly at certain transitions, and different heads concentrate their attention mass to very different extents. To this end, we design Step-dLLM, which periodically refreshes a block-sparse mask at anchor steps along the denoising trajectory and reuses it within each locally consistent interval, while employing a head-adaptive global budget that more aggressively compresses heads with concentrated attention. Backed by a fused IO-aware Triton kernel for block-sparse attention, Step-dLLM applies to pre-trained LLaDA-1.5 and Dream-7B-Instruct without retraining, achieving a 2.78x end-to-end speedup over dense FlashAttention on LLaDA-1.5 at 8K context with 256 denoising steps and 90% sparsity, while improving the accuracy-latency trade-off over prior sparse-attention methods.

---


### 167. [Large language models underrepresent malice and overreport virtue](https://arxiv.org/abs/2611.01332)

**<font color=#1a73e8>作者：</font>** Xiaoyan Wu, Fan Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People increasingly use large language models (LLMs) to interpret others' behaviour, often assuming that LLMs infer motives as humans do. Aligned LLMs attribute more benevolent and less malevolent motives to a whistleblower than humans do, but ratings alone cannot reveal whether these differences arise in internal representations or at report. Here we compare linear-probe readouts of LLMs' internal states with their own ratings at the same prompt position for four motives, in two preregistered studies. For the two malevolent motives, self-interest and intent to harm, internal and expressed readouts did not differ: the lower ratings reflect weaker signal along the probed directions, not suppression at output. For the two benevolent motives, duty and concern for others, expressed ratings exceeded the internal readouts, indicating amplification at report. In free text the model rarely volunteered a motive against the colleague, far less often than humans did, yet produced one readily once the scenario supplied a reason. Shifting the internal representation along a malevolent-motive direction brought both malevolent ratings to the human level, whereas the rating of duty yielded only past a threshold at which the other motives had overshot. LLMs' more charitable motive profile thus has two distinct sources: reduced malevolent signal in the probed representation and amplified benevolent attribution at report.

---


### 168. [The Verifier Is Part of the Simulator: Evidence-View Gaming in Agentic Equation Discovery](https://arxiv.org/abs/2611.01334)

**<font color=#1a73e8>作者：</font>** Orestis Oikonomou, Bogdan Raonic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing number of agentic pipelines search for governing equations: an agent proposes laws and a verifier checks them against simulated trajectories. The verifier sees only a numerical summary: integrals against test functions on a time grid. That summary carries its own discretization error, making the verifier part of the simulator. We freeze the trajectory, candidate library, verifier and thresholds, leaving the agent one move: which permitted summary to admit. Without scores or language models, finer time grids reduce numerical discrepancies and false library rejections. On PDEBench, the verifier instead accepts equations missing diffusion on score-selected summaries. Maximizing a public score rewarding decisive verdicts and larger mismatches when rejecting the library wrongly rejects all 1,500 in-library cases; retrospectively retuning score constants on a separate bank reduces errors to 13/180 at best. We call this evidence-view gaming: reward hacking by choice of permitted summary. In single-turn forced-choice tests, Claude models rarely choose summaries giving wrong verdicts when asked to be accurate, but often do so when asked to maximize the score or report missing physics. In separate trust prompts, they often rank those harmful summaries least trustworthy. Requiring several summaries to agree reduces errors but often withholds a verdict and performs worse than a fixed fine view on PDEBench: a safeguard, not a certificate. Evidence chosen after its verdict is known cannot alone authorize a claim.

---


### 169. [J-Anchor: Defending Against Prefill Attacks via J-Space Selective Refusal Restoration](https://arxiv.org/abs/2611.01342)

**<font color=#1a73e8>作者：</font>** Running Yang, Beidi Zhao, Xiaoxiao Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prefill jailbreaks can cause safety-aligned language models to continue an unsafe assistant prefix even when they would refuse the same request under normal decoding. We study how the model's internal harmfulness and refusal signals evolve along this attacker-controlled trajectory. Using the Jacobian lens, we track vocabulary-grounded harmfulness and refusal signals from the assistant header through prefilling and subsequent generation. We identify a characteristic phenomenon, which we call refusal-state erosion: both the refusal signal and the harmfulness signal weaken as the prefill progresses, but the refusal signal progressively declines to the benign baseline by the end of the prefill, while the harmfulness signal remains above its benign baseline and detectable during subsequent generation. Motivated by this observation, we introduce J-Anchor, a training-free inference-time defense that uses the model's pre-attack harmfulness and refusal signals as a request-specific anchor and selectively restores weakened refusal in J-space during prefilling and decoding. J-Anchor substantially reduces attack success under both fixed and deep prefill attacks across different model families. J-Anchor largely preserves benign behavior and reasoning ability, and ablations highlight the importance of targeted restoration in the J-space refusal subspace. Our results suggest that preserving latent refusal dynamics offers a promising route to robust defense against prefill jailbreaks.

---


### 170. [MAPLE: A Multimodal Mobile Agent with Playbook-Learned Experience](https://arxiv.org/abs/2611.01351)

**<font color=#1a73e8>作者：</font>** Jun Wang, Aurora Wei, Lucas Spangher 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous agents powered by vision-language models (VLMs) show great potential in navigating mobile graphical user interfaces (GUIs) to complete complex tasks. However, existing paradigms face fundamental scalability bottlenecks: fine-tuning requires massive high-fidelity datasets or prohibitive training time and compute, while gradient-free approaches rely on custom static heuristics or costly trial-and-error trajectory exploration where feedback is deferred until the end of execution. To address these limitations, we introduce MAPLE (Multimodal Agent with Playbook-Learned Experience), a novel gradient-free multi-agent framework that enables dynamic, step-wise experience sharing and execution-time prompt evolution. Unlike traditional action-reflection architectures that depend on costly, post-hoc self-reflection, MAPLE enables agents to cross-reference and distribute runtime insights in real time at each operational step. This dynamic exchange eliminates blind trial-and-error looping and steers agents along direct, grounded interaction paths. Extensive evaluations on the AndroidWorld and MobileWorld benchmarks demonstrate that MAPLE achieves state-of-the-art performance on complex, long-horizon mobile tasks, while proving scalable and adaptable across novel environments.

---


### 171. [Wrong Together: Shared Bias in User Simulation](https://arxiv.org/abs/2611.01354)

**<font color=#1a73e8>作者：</font>** Saber Zerhoudi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulators generate responses in place of human participants, allowing researchers to estimate the result of a study. To use these estimates before collecting human responses, researchers need a way to assess their reliability. We test whether disagreement among simulators can identify unreliable estimates of a group's response proportions and of differences between groups. We evaluate this signal using 6 language-model simulators and existing GlobalOpinionQA responses for 60 questions in 12 countries. Disagreement predicts invalidity more accurately for differences between two groups than for a single group's response proportions (AUC 0.87 versus 0.71). Errors shared by the simulators remain invisible to this signal. When such an error affects both groups equally, it cancels in the comparison, helping explain the stronger result for group differences. We test this explanation by estimating the shared bias using one set of groups and subtracting it from predictions for a separate set. This correction reduces prediction error without changing disagreement among the simulators. In a retrospective analysis, we simulate referring the 20% of group comparisons with the greatest disagreement for human assessment. Among the remaining comparisons with a conclusive validity judgment, 54.8% are judged invalid, compared with 63.7% before referral.

---


### 172. [XDecideBench: Evaluating Typed Decision Models and Confidence Policies Across Languages](https://arxiv.org/abs/2611.01370)

**<font color=#1a73e8>作者：</font>** Marek Šuppa, Jaroslav Kopčan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Applications use Typed Decision Models to route and moderate text in many languages, and they often act only on decisions above a confidence threshold. We introduce XDecideBench, a benchmark of nine suites in 122 languages with 88,425 texts and 153,875 typed questions. All suites share one scoring contract, and we report aligned, locally labelled and native items separately. Model rankings change from suite to suite. The model that is best in English, chosen in hindsight, loses significantly in about a quarter of the suite-language cells, and on Burmese Belebele it falls far behind the best model. Three open models fine-tuned for typed decisions beat the Qwen models they were built from in all twelve development languages. When the Qwen models are run locally, a pre-registered held-out cohort confirms that the accuracy gain is larger in the four languages with the least web text than in the six with the most. In both sets of languages, however, fine-tuning fixes a similar share of the base model's errors, so the larger gain may reflect weaker base models. A confidence threshold set on English data to allow 5% errors exceeds that error rate on XNLI, even in German and French.

---


### 173. [A Self-Exploring and Self-Evolving Paradigm for Adaptive Edge AI Development](https://arxiv.org/abs/2611.01377)

**<font color=#1a73e8>作者：</font>** Leming Shen, Qiang Yang, Xinyu Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit powerful code generation abilities, fostering agentic systems to automate edge AI application development. However, existing agents typically operate via fixed agentic workflows and predefined design spaces, struggling to handle rapidly evolving demands of real-world scenarios (e.g., heterogeneous data modalities, diverse task pipelines). Unlike prior systems that treat LLMs mainly as code generators following rigid workflows, we fully exploit their reasoning capabilities to allow agents to determine their own workflows on the fly. To this end, we propose SE2, a self-exploring and self-evolving paradigm for adaptive edge AI development. Inspired by human learning processes, we distill development into four atomic operations (retrieve, reason, code, test), and empower agents to explore workflows by dynamically and adaptively selecting an appropriate next operation based on the current context. Extensive evaluations show that, with adaptive workflows, the synthesized programs achieve up to 26% higher accuracy and consume 28% lower resources than state-of-the-art baselines, while maintaining superior adaptability to unforeseen edge AI scenarios. This highlights the potential of reasoning-driven adaptive agentic workflow in edge AI development.

---


### 174. [Information-Theoretic Design of Sparse Autoencoder-Based Steering](https://arxiv.org/abs/2611.01378)

**<font color=#1a73e8>作者：</font>** Hirofumi Morise  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE)-based activation steering is a lightweight approach for modifying the behavior of large language models (LLMs) by adding small vectors to hidden states during inference. However, designing effective steering interventions remains challenging. In this work, we develop an information-theoretic framework for analyzing SAE activations through empirical feature-firing distributions. The central object of the framework is the Jensen--Shannon divergence (JSD) between such firing distributions, which quantifies how far a generated or intervened state deviates from a dataset-induced target distribution. Based on an analytic divergence response for virtually shifted states, we construct steering vectors toward the target firing distribution. The same divergence can also be used to monitor deviation from another empirical distribution, such as a general valid-language distribution. We demonstrate the effectiveness of the steering in a question-mode generation task study. We further use teacher-forced pulse experiments to show that local interventions induce structured downstream JSD responses in later layers, and apply the framework to a safety-related target--contrast response setting for feature analysis.

---


### 175. [Toward Executable Multi-framework Front-end Code Generation with Self-Correction](https://arxiv.org/abs/2611.01383)

**<font color=#1a73e8>作者：</font>** Linxiao Li, Haoran Ma, Chenyue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating codes from UI screenshots has recently benefited from MLLMs, yet existing methods centered on HTML targets and transfer poorly to multi-frameworks such as React, Vue, and Angular. However, unlike HTML, which does not entail compilation issues, generating executable code in multi-framework settings is more challenging due to framework-specific differences in syntax and failure modes, as well as the need to maintain global consistency across files. To address this problem, we study executable multi-framework front-end code generation and propose MESCoder, a tree-structured self-corrective generation framework. Our method first extracts a structural scaffold from the screenshot and then constructs sub-trees and assembly relations step by step, transforming large project generation into a sequence of localized decisions. On top of this scaffold, we introduce a unified Project Agent that continuously revises its own partial project under runtime sandbox feedback and dynamically chooses between local repair and cluster level repair. For training, we adopt a two-stage strategy that first initializes the policy offline to learn basic multi-framework generation and repair priors, and then refines it with online reinforcement learning to optimize long horizon executability and final page quality. The resulting framework models multi-framework executability as a conditioned project state transition process and improves the stability and quality of complex front end generation through self correction. Experiments show that our method improves executability, while narrowing the visual-fidelity gap to HTML-based generation. Code is available at this https URL.

---


### 176. [Learning by Doing: Autonomously Compiling and Curating Agent Skills from Verified Traces](https://arxiv.org/abs/2611.01386)

**<font color=#1a73e8>作者：</font>** Daniel Chalef, Peter Evans, Pavlo Paliychuk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory systems for production LLM agents mostly store semantic memory (facts about users and domains) or episodic memory (earlier interactions). Research systems such as Trace2Skill, WikiSkill, and SkillRevise learn procedures from agent runs, package them as Skills, and evaluate them on benchmarks. We describe Zep Agent Skills, a production service that gives deployed agents this procedural memory. The service uses only verified attempts as evidence, cites the supporting events for each field of a Skill, and governs the admission and distribution of each Skill version. The service records each task attempt as a Trace with ordered events, an outcome, and a verification strength. A compiler with separate Reflector and Curator roles turns verified Traces into versioned Skills. Scans and admission gates control which candidates become active, and verified use outcomes change the search rank of each Skill. The Agent Skills format is an open standard that Anthropic originated and donated to the Agentic AI Foundation, so any host of the format can load a compiled Skill. Agents retrieve Skills through lexical search with progressive disclosure, over an API or MCP. We evaluate Zep Agent Skills on $\tau^3$-bench banking, AppWorld, and EnterpriseOps-Gym. Skills compiled from the Traces of a teacher model increase the pass rate of three weaker executor models on the same tasks, at every reasoning effort, by 4.5 to 18.8 points. Most of the gain is on the tasks that the teacher solved. On ALFWorld, Skills compiled from the runs of a small model give a gain similar to or larger than the gain that prior work reports for continuous fine-tuning, with no training.

---


### 177. [ERIA: An Instruction-Optimized Agent for Clinical EEG Reporting](https://arxiv.org/abs/2611.01394)

**<font color=#1a73e8>作者：</font>** Ahmed Sameh, Gayal Kuruppu, Neeraj Wagh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical EEG interpretation requires integrating technical quality, background and behavioral states, interictal and ictal abnormalities, and overall clinical context across long recordings. We introduce ERIA (EEG Reporting and Instruction-Optimized Agent), a locally deployable framework in which a single 27B language-model controller analyzes whole-recording EEGs by orchestrating specialized parametric and signal-processing tools. ERIA combines learned tools for background abnormality, sleep-wake state, seizure-like activity, and interictal epileptiform discharges with deterministic spectral, amplitude, symmetry, montage, and signal-quality analyses. Rather than fine-tuning the controller or using multi-agent orchestration, ERIA keeps the controller weights, specialist tools, and safety constraints fixed and optimizes only its natural-language analysis policy with GEPA (Genetic-Pareto), using feedback from expert-written EEG reports. GEPA improves physician-aligned whole-recording report quality over the raw policy, and the optimized policy transfers to external EEG benchmarks. On CerebraGloss-Bench and BrainBench Foundational Analysis, ERIA remains competitive with the models evaluated in the original benchmarks. These results show that specialist tools and language-level policy optimization can extend the clinical and general EEG capabilities of a single locally executable model while preserving local inference and traceable tool use.

---


### 178. [RAG-TRACE: Tracing Measurement Evidence and Diagnostic Completeness in AI-Generated ECG Reports](https://arxiv.org/abs/2611.01409)

**<font color=#1a73e8>作者：</font>** Elyas Irankhah, Shahed Salehzehi, Parisa Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: Retrieval-augmented generation (RAG) can introduce electrocardiogram (ECG) criteria that lack patient-specific measurement support. This study evaluates the reliability of retrieved diagnostic criteria in AI-generated ECG reports. Methods: We analyzed 1,083 human-validated PTB-XL patient records using a library of 47 criteria cards, including 33 without numeric verification rules. Language models generated structured reports with and without retrieval. Criterion applicability was evaluated using Marquette 12SL measurements, with independent assessment using Uni-G and comparison against expert-validated diagnostic labels. Results: Keyword retrieval introduced untestable or measurement-disconfirmed criteria in 46.8% of GPT-4.1-mini reports. A deterministic verification rule withdrew 647 criterion applications, including 639 without numeric checks, while preserving 268 of 269 applications independently supported by Uni-G. Restricting retrieval to 14 testable criteria reduced the initial unsupported-criterion rate to 13.8%. Under matched instructions and an identical output schema, retrieval increased unsupported-criterion reports from 17.4% to 31.1%, while hypertrophy recall remained unchanged at 62.6%. Conclusion: These findings identify a fundamental limitation of retrieval-based clinical report generation: retrieved criteria do not necessarily provide valid patient-specific evidence. Measurement-based verification can reduce unsupported criterion applications, but diagnostic validity requires independent assessment.

---


### 179. [Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning](https://arxiv.org/abs/2611.01411)

**<font color=#1a73e8>作者：</font>** Annan Zhang, Shengjie Song, Wenshuai Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Private fine-tuning of large language models increasingly pairs DP-SGD with low-rank adapters on frozen, quantized backbones, and every such stack inherits one unstated premise: frozen layers keep each record's clipped gradient a function of that record alone. We show that LLM.int8 breaks this premise. It routes outlier activation columns to a higher-precision path using a union over the whole batch, so one record decides how every other record's activations are computed, even though the weights are frozen and the quantization scales are per row. We bound the resulting sensitivity inflation, state a record-isolation contract that restores the standard bound, and define record-owned precision dispatch that meets it with the same GEMMs as batched LLM.int8, so isolation needs no extra arithmetic. We then audit the native CUDA stack (bitsandbytes, PEFT, Opacus) against four matched controls. A constructed LoRA-Opacus witness reaches $15.0\times$ the add/remove bound. On pretrained OPT-125M with natural text, other records alter 20% of record-layer precision splits at batch size 16. An exploratory re-clipping analysis finds 10 of 64 candidate neighbors above the bound once every gradient is clipped; the top pair, revalidated natively, reaches $1.065C$ while every control stays within $C$, and forcing one layer's outlier mask removes the excess. A two-million-draw audit of the released adapters yields $\varepsilon$ lower bounds ($3.25$ at $\delta=10^{-5}$) below the advertised guarantee ($4.38$). Resolving an excess this small at the release level would take about 200 times more draws, whereas checking the sensitivity contract directly exposes it in a few native runs, which makes contract checking the practical audit for private quantized training.

---


### 180. [Latent Harness: Compiling Agent Behaviors into Post-Block Activation Shifts](https://arxiv.org/abs/2611.01415)

**<font color=#1a73e8>作者：</font>** Ran Li, Shimin Di, Zeyu Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harness engineering and self-evolving agents improve language-model agents quickly, yet their gains live outside the model. The harness is re-sent and re-paid on every call, and the standard route to internalization is a weight update that is costly to iterate and fixed once merged. We propose compiling the harness instead. Latent Harness distills an external condition into a rank-8 activation shift. The shift is applied at the output of every decoder block of a frozen backbone, at 0.03-0.05% of parameters. The condition is either an explicit process-level behavior instruction or the behavioral contract of an agentic harness. At inference the compiled bundle carries no harness text and adds no tokens. It exposes three runtime controls for injection strength, injection phase, and shift-space mixing. Compiled behaviors recover the source-harness gain in 8 of 10 preregistered settings. Where the explicit source pays the heaviest per-call token tax, the compiled form exceeds it. The same bundles transfer zero-shot across tasks (5 of 7 pairs positive) and compose in shift space, while stacked text instructions interfere destructively. Used as a search space, they lift budget-matched harness search by 1.45 times. On three agentic benchmarks the operator aligns policy to the harness con- tract. Under matched data, capacity, and effective strength it outperforms same-capacity LoRA, which needs 11.1 times the parameters to reach the same band, and it regresses nothing where the base policy is already strong. Across 1B-to-8B models the method skeleton is invariant while gain locations move with the model-task pair, which delimits where compiled harnesses should be deployed.

---


### 181. [FlyWheel: Attention Kernels Built for the TPU](https://arxiv.org/abs/2611.01426)

**<font color=#1a73e8>作者：</font>** Zishuo Bao, Zeshen Zhang, Linkun Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attention kernels on Tensor Processing Units (TPUs) often underutilize their matrix units (MXUs) because of repeated matrix operand loads, vector-intensive computation, and dependencies that leave MXUs idle. We present FlyWheel, a set of fast TPU kernels for both softmax and linear attention. FlyWheel reformulates softmax and triangular inversion to reduce vector work, while coordinating data layouts to improve matrix operand reuse. It then overlaps independent computation to hide execution latency. We apply these techniques to both softmax attention and Gated DeltaNet on TPU v6e and v7x. FlyWheel speeds up softmax attention by up to $4.14\times$ over the state-of-the-art RPA kernel and $1.80\times$ over Splash Attention, reaching 81% of peak BF16 throughput on v6e. It also speeds up Gated DeltaNet prefill by up to $3.61\times$. Integrated into vLLM serving Qwen3.8-27B, FlyWheel improves prefill throughput by up to $1.56\times$ while maintaining comparable accuracy.

---


### 182. [Towards Fine-grained and Robust Detection of Human-AI Co-authorship](https://arxiv.org/abs/2611.01427)

**<font color=#1a73e8>作者：</font>** Ziruo Zhao, Jie Fu, Wendy Hui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of large language models (LLMs) is reshaping how textual content is produced, complicating text provenance, and raising concerns for misinformation, plagiarism, and intellectual property. While prior work on AI-generated text detection has progressed, one-dimensional human-AI co-authorship scores lack signals directly relevant to ``AI involvement''. It remains unclear how adversarial paraphrasing distorts detection signals. In this work, we formulate a discrete-class text provenance detection framework. This framework allows an abstraction of realistic co-authorship scenarios into distinct degrees of AI involvement, differentiating the AI polishing on the surface level from the AI updating the discourse structures. This framework reveals the mechanisms of how adversarial paraphrasing blurs the decision boundaries for co-authorship detectors. To improve robustness of the detectors, we augment training data with adversarial paraphrases generated by the state-of-the-art paraphrasing attack model, exposing detectors to challenging meaning-preserving rewrites. Extensive experiments across multiple datasets and generation models demonstrate that adversarial paraphrasing substantially degrades detectors trained only on benign data, while adversarial data augmentation leads to consistent robustness gains and good cross-generator transferability. Overall, our findings highlight the value of discrete-class formulation and principled data augmentation for building reliable detectors of human-AI co-authorship.

---


### 183. [When Should an Agent Refresh? Adaptive Index Reuse for Efficient Long-Horizon Reasoning](https://arxiv.org/abs/2611.01429)

**<font color=#1a73e8>作者：</font>** Guangyuan Wang, Yifan Zhang, Shilong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language agents read code, tool output, and dialogue in contexts that grow at every step. Dynamic sparse attention lets a small indexer choose the earlier tokens each query attends to, but the indexer still scores the whole prefix at every layer. Cross-layer reuse methods such as IndexCache rerun the indexer at only some layers, with one fixed pattern for every input. In an agent, the relevant evidence can change abruptly when a traceback or test result arrives, so fresh selections matter more at some steps than at others. We propose Adaptive Index Reuse (AIR), which keeps IndexCache's execution and learns, for each segment of an agent episode, how many layers refresh their selection. A small controller reads signals from completed computation and the latest tool event, chooses a pattern from a nested library, and learns from terminal task reward under an expected compute budget. On Qwen3-4B-Instruct-2507 with a 128K context, AIR improves success over the strongest static schedule at matched cost on SWE-bench Verified (27.0% to 32.4%), Terminal-Bench 2.0, and three $\tau^2$-bench domains, and it lowers time per successful task on all five. Across 50 backbone, context, and benchmark settings, it matches or exceeds that schedule in 44.

---


### 184. [FOCUS: Closed-Loop Attention Feedback for Efficient Vision-Language Understanding](https://arxiv.org/abs/2611.01438)

**<font color=#1a73e8>作者：</font>** Akul Santhosh, Aastha Jhunjhunwala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Processing every video frame through Vision-Language Models (VLMs) adds significant inference cost and limits their ability to comprehend real-time video. Existing approaches either sub-sample frames uniformly, ignoring content and missing important events, or prune visual tokens inside the VLM to cut per-call cost while still invoking the model on every sampled frame. We introduce FOCUS, a training-free three-layer framework that reduces the number of invocations and steers each one towards what matters. Temporal gating measures inter-frame dissimilarity in the patch-embedding space of a smaller VLM from the same family, triggering burst captures only when the scene changes in a semantically meaningful way. Patch-level dissimilarity is then accumulated across the burst and fused with a top-down attention prior into a spatial focus map that encodes where motion and semantic relevance coincide. That map calibrates the VLM's value cache during generation, progressively amplifying vision tokens in task-relevant regions and attenuating off-target ones, without removing any token from the context. The loop closes after each response: text-to-vision cross-attention is extracted from the decoder and fed back as the prior for the next burst, letting the system converge on semantically important regions over successive observations. We evaluate FOCUS on the 500-video EgoSchema subset in streaming mode, with a single Qwen3-VL-8B backbone shared by every method. It reaches 74.8% accuracy using 25.4 VLM calls per clip, against 74.6% with 55 calls for uniform sampling and 74.2% with 55 calls for BOLT. On egocentric video captioning across four domains, it matches the best baseline's quality while issuing 57% fewer VLM invocations than uniform sampling.

---


### 185. [I-PTC: Interactive Programmatic Tool Calling for Stateful Tool-Augmented Agents](https://arxiv.org/abs/2611.01446)

**<font color=#1a73e8>作者：</font>** Huanzhi Mao, Chengkun Cao, Shuo Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly capable of writing and executing code, suggesting a natural paradigm for tool-augmented agents: expressing tool use as programs rather than isolated calls. Programmatic tool calling (PTC) captures this idea through loops, batching, abstraction, and structured computation, but existing PTC approaches are largely stateless, limiting their ability to reuse intermediate results and adapt over time. This is problematic for real-world tasks, where tool environments and problem-solving processes are inherently stateful. We therefore present I-PTC, an interactive framework that executes stateful PTC: models issue code snippets that call tools, maintain reusable state, and evolve the tool interface through API corrections. To evaluate the effectiveness of I-PTC and the general PTC setting, we introduce PTC-Bench, a benchmark of long-tail, production-style user requests whose difficulty comes from large initial environments, many dependent API interactions, extended planning, and recovery across follow-ups and transient failures. Experiments on PTC-Bench show that I-PTC improves performance on complex multi-step tasks with large tool sets while substantially reducing token consumption over conventional tool-calling baselines and the original PTC baseline, highlighting stateful programmatic tool calling as a promising direction for scalable tool-augmented agents.

---


### 186. [CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](https://arxiv.org/abs/2611.01449)

**<font color=#1a73e8>作者：</font>** Yuxiang Wei, Lijing Zhu, Qizhen Lan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can autonomously run neuroimaging analyses from research questions to reported findings. Existing agentic systems use tools to check that code runs and reported values match its output, but rely on LLM judgment to decide which results warrant scientific reporting. We show that LLM judges endorse site-confounded findings even when the confound is presented as evidence. We present \textbf{CONFIRM}, a framework that separates running an analysis from deciding which findings to report. CONFIRM encodes each hypothesis as a machine-readable, pre-specified analysis plan that fixes the claim and its pass criteria before computing results. It then filters results through five deterministic gates (search history and multiplicity, confounds, power, analytic stability, and replication) under three configurable reporting standards, from least to most demanding: \textit{Screen}, \textit{Replicate}, and \textit{Full}. Failed claims receive diagnoses that guide follow-up analyses. To evaluate reporting decisions at the claim level, we introduce \textbf{NeuroClaimBench}, comprising 489 executable neuroimaging claims with frozen data, including literature-supported findings and 150 controls designed to violate individual methodological requirements. On NeuroClaimBench, CONFIRM falsely supports at most 3\% of controls, compared with 23--38\% for the baselines, while recovering up to 61\% of literature-supported claims. When auditing an existing agent, CONFIRM reduces false support on controls from 23\% to 0\% while retaining the agent's literature-supported claims. Its diagnostic feedback also produces more supported revisions than Self-Refine with fewer LLM calls. Together, CONFIRM and NeuroClaimBench show that basing reporting decisions on pre-specified analysis plans and deterministic gates is essential for trustworthy autonomous scientific discovery.

---


### 187. [Can Large Language Model Agents Learn by Watching Tutorial Videos?](https://arxiv.org/abs/2611.01460)

**<font color=#1a73e8>作者：</font>** Haoyu Zhao, Zafeirios Fountas, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans continuously acquire knowledge from carefully crafted materials such as books and tutorial videos, carrying that understanding into future tasks. Millions of such instructional videos are uploaded online every day, yet LLM agents remain unable to exploit this ever-expanding wealth of human teaching. Their capabilities are frozen after training, while parameter updates at scale remain prohibitively expensive. This raises the central question: can LLM agents learn from this vast instructional resource without parameter updates? We introduce Tutorial Agentic Learning (TAL), a nonparametric continual-learning paradigm that consolidates tutorial videos into a persistent, structured tutorialbook memory through a two-stage adversarial process that harvests hard, video-grounded questions and uses them to refine the memory. At inference time, TAL retrieves through a Table-of-Contents (TOC) tree, tying retrieval directly to the model's reasoning rather than to embedding similarity. To study this setting, we introduce VidLearn, a multimodal QA benchmark built from 72 chess tutorial videos spanning 12 openings. On VidLearn, TAL outperforms all evaluated baselines and improves monotonically as more videos are consumed, achieving up to 113% and 91% relative gains over the corresponding vanilla MLLMs on the training and test splits, respectively. In actual gameplay, TAL reaches a stronger opening-phase position than its vanilla counterpart in 69% of head-to-head games. Evaluation in a second domain further demonstrates the generality of TAL. Together, these results highlight instructional videos as a scalable resource for parameter-update-free agent continual learning.

---


### 188. [See, Think, Use: Diagnosing Perception and Reasoning Failures in VLMs](https://arxiv.org/abs/2611.01467)

**<font color=#1a73e8>作者：</font>** Jiacheng Ding, Yanliang Qi, Cong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present See, Think, Use, a protocol that traces each answer of a vision-language model to perception, reasoning or the use of perception. The diagnosis shows a developer which stage to improve and directs test-time compute to the stage that fails. Benchmarks score the final answer, and an answer that rests on the image earns the same credit as a guess or a memorized prior. The protocol asks the model two extra questions per item and needs no access to its weights. A localization probe asks for a box around every instance and measures seeing, and a text-replacement probe answers from a description and measures thinking. Use is the rate at which the answer follows the model's own perception across counterfactual image pairs. The rate needs no answer labels, because the question and its prior are the same on both images. On two model families and six datasets the protocol shows that the knob that helps follows the task family. Answers follow the model's perception except on images that contradict a common prior, and asking the model to localize first repairs this failure when its boxes are right. Allocating compute by the measured stages comes close to the best uniform policy at lower cost and beats a random allocation of the same compute wherever a knob raises the short stage. We will release the code, the prompts and the per-question outputs.

---


### 189. [Causal Optimal-Transport Attention: Positional Priors and Length Extrapolation](https://arxiv.org/abs/2611.01472)

**<font color=#1a73e8>作者：</font>** Ming Lian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal masking obstructs the column balancing used by optimal-transport (OT) attention. We study a prefix-consistent unbalanced operator and characterize the positional prior it induces. Under bounded scores, for any fixed balancing strength $\rho<1$, its fixed point dilutes attention: every fixed window receives a vanishing share as the context grows. For constant scores, we derive an exact scale-invariant prior. We then classify positional encodings by whether their distant attention mass remains bounded away from one. Discrete window-mass bounds quantify the finite-length dilution of summable log-distance priors near exponent one. Preregistered experiments with 25M- and 100M-parameter language models establish improved loss extrapolation over softmax; exploratory comparisons favor an explicit distance bias at a fraction of the cost. CABLE outperforms RoPE with evaluation-time YaRN on every seed at three training lengths. Changing only the bias beyond the training length moves long-context loss in the predicted direction on all 30 tested checkpoints. Even with exponents constrained above one, many heads approach the summability boundary during training. A margin selected by prior-only calculations for a specified window, length range and growth tolerance controls distant-mass growth in the tested setting. These results connect loss extrapolation to positional decay over the lengths actually evaluated.

---


### 190. [Accounting for Irregular State Transitions through Belief Estimation in Online Medical Consultation](https://arxiv.org/abs/2611.01474)

**<font color=#1a73e8>作者：</font>** Mingzhe Lu, Xiangru Chen, Jian Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While online medical consultation broadens access, unprompted patient disclosures and topic shifts frequently disrupt clinician inquiry, leaving clinical states progressively revealed. We characterize these dynamics using both existing evaluation metrics and task-specific interaction metrics designed in this work. Through an empirical study across 16 medical dialogue datasets, we show that authentic online interactions exhibit substantially lower contextual continuity and higher unpredictability than offline and simulated benchmarks. We propose PRISM (Policy Reasoning with Inferred States for Medicine), a framework inspired by partially observable Markov decision processes that decouples latent state estimation from action selection to address drifting dialogue trajectories. Specifically, PRISM factorizes clinical triage into belief estimation, policy optimization, and response realization. By maintaining an evolving posterior belief over consultation states and conditioning action selection on the maximum a posteriori state, PRISM advances clinical goals while accommodating patient-initiated shifts. Extensive evaluations show that PRISM substantially outperforms frontier LLMs and clinical agents, achieving a 22.40 percentage point gain in clinical decision accuracy alongside decisive improvements in response generation, surpassing the strongest baseline by 5.51 points in BERTScore_F1. Furthermore, ablation studies show that providing oracle consultation states consistently boosts response quality across all evaluated baselines by guiding their action reasoning, yielding average gains of 5.58 points in BERTScore_F1.

---


### 191. [TopoSteer: Topological Layer Selection for Activation Steering in LLMs](https://arxiv.org/abs/2611.01493)

**<font color=#1a73e8>作者：</font>** Tuc Nguyen, Marcos Gutiérrez-del-Pozo, Eduardo Paluzo-Hidalgo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering controls large language models at inference time by adding a vector to their internal representations. Most work asks how to build that vector, and far less attention has gone to where to add it, even though steering at a poorly chosen layer can be worse than not steering at all. Prior selectors choose a layer without ever steering the model to test it: they score how separable the target behavior is at that layer, and how consistently the individual examples point along the steering direction. We argue that what matters is not the separability of the two activation clouds, nor the alignment of individual displacements with their mean, but the extent of the cloud of per-example displacements that mean-difference steering averages. We propose a topology-based layer selection method, called TopoSteer, which scores a layer by the total H_0 persistence of its displacement cloud, computed as the length of the cloud's Euclidean minimum spanning tree. We show that the score focuses on the displacement cloud's relative geometry, while class separation affects it only through standardization. We also provide a theoretical explanation for our method by proving that, as example-level variation increases, TopoSteer and discriminability move in opposite directions, so the two criteria can rank layers in opposite ways. Across multiple language models and steering tasks, TopoSteer provides a principled alternative to discriminability- and separability-based layer selection and yields more effective steering without requiring held-out validation.

---


### 192. [Sweep Less, Steer More: Using Activation Steering Geometry for Reduced Hyperparameter Search](https://arxiv.org/abs/2611.01496)

**<font color=#1a73e8>作者：</font>** Nishkal Hundia, Swastik Agrawal, Navita Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation steering methods like difference-in-means (DIM) offer a lightweight approach to controlling LLM behavior, but their effectiveness varies widely across concepts, datasets, and layers, making principled deployment costly without exhaustive hyperparameter sweeps. We build on the discriminability index $d'$, a compute-cheap geometric measure of how well contrastive training activations separate along the steering direction. Across five behaviors on 3 models, we demonstrate uses beyond its established role as a dataset-level steerability predictor. First, in the multiple-choice question answering (MCQA) setting, we show that $d'$ reliably identifies performant layers at which to steer, eliminating the need for a layer-wise sweep. Second, we extend this analysis to open-ended multi-token generation, and find that $d'$ remains successful for layer selection across different settings. Lastly, we test whether the position of a generated token's representation on the DIM line predicts steering success on that individual example. In the MCQA setting, this works for high-$d'$ datasets but is inconsistent across behaviors, models, and training-token choices in open-ended generation. This highlights that methods developed and conclusions drawn in single-token MCQA settings do not necessarily transfer to open-ended generation.

---


### 193. [Label-Free Localization and Test-Time Suppression of CLIP's Typographic Circuits](https://arxiv.org/abs/2611.01513)

**<font color=#1a73e8>作者：</font>** Bohan Liu, Wenqian Ye, Guangzhi Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP-based Vision-Language Models have become cornerstones of modern multimodal systems. The cross-modal contrastive objective equips the CLIP vision encoder to both see objects and read text. These two abilities induce an entanglement between the encoding of lexical and semantic shapes, creating a distinctive vulnerability to typographic attacks, in which rendered text overrides an image's semantic content with its literal meaning. The black-box nature of these encoders has prevented a mechanistic interpretation of such entanglement. We introduce a head-decomposed Sparse Dictionary Learning (SDL) architecture that, by design, decomposes individual attention heads into interpretable, head-specific latents. Based on this inductive disentanglement, we re-purpose Clarity Score and propose normalized Text Attribution Score, which are both label-free, to identify attention heads that carry typographic information. As a causal validation of successful circuit separation, we perform a mechanistic intervention that reweighs attention away from the patch tokens in the identified lexical heads at test-time. Experiments show that the intervention effectively recovers object classification under typographic attack and, across five CLIP variants and four typographic benchmarks, achieves up to 46.9% improvement while incurring up to 1% accuracy loss in general image perception, outperforming prior supervised and training-free methods. Expanding on the mechanistic intervention, we propose a test-time adaptive attention head routing to further reduce the impact on performance at matched robustness, pushing beyond the Pareto frontier of current robustness-perception tradeoff.

---


### 194. [VLMs Read Aloud: The Gap Between Recognizing and Using Visual Text](https://arxiv.org/abs/2611.01517)

**<font color=#1a73e8>作者：</font>** Zhiyun Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-text compression renders long contexts as images and is engineered around how much of the text a vision-language model (VLM) can recover. Yet recovered text is not usable text. VLMs can transcribe the text in an image word for word and still fail to answer from it; given back their own transcript, they answer nearly as well as from the original text. We call this difference the read-use gap. Recognizing and using visual text have different resolution requirements: Qwen3-VL-8B's recognition saturates at 15-pixel characters while use catches up only at 24 pixels, and scaling from 2B to 32B raises recognition without narrowing the gap. Putting the evidence into words closes it: thinking VLMs recite the evidence in their thinking, and their own transcript, written without seeing the question, recovers most of what thinking adds. In a preregistered held-out test, the gap ranks how much eight VLMs gain from their own words over pixels (Spearman $\rho$ = 0.86), which recognition rates do not. We propose ALOUD, which spends visual resolution on finding and recognizing evidence and language tokens on using it. Without keeping the source text, it doubles the accuracy of a frozen Qwen3-VL-8B on long documents compressed 5x and 10x: at 5x, from 27.7% to 54.8%, near the original text's 58.5%, with a context smaller than the compressed pages themselves. For less than the cost of reading the original text, it leads at equal budget every method that does without it, at every level, and beats AGAR and VERA, which paste the original text back; at 5x it also beats LensVLM-9B, which is trained and keeps the original text. Visual-text compression is limited not by how much text a model can recover, but by how much it can use.

---


### 195. [Write Facts the Way Models Read Them: Lifting the Two-Hop Curse](https://arxiv.org/abs/2611.01519)

**<font color=#1a73e8>作者：</font>** Zhiyun Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model that learns a new fact by fine-tuning can repeat it but cannot reason with it: taught that a person is a citizen of a new country, it still cannot say, without chain-of-thought, who the head of state of that person's country is. This two-hop curse is widely treated as a reasoning deficit, and the strongest knowledge editors answer it with synthesized reasoning data. We show that the reasoning is intact and the writing is wrong. Fine-tuning writes a new fact as an answer to be said, whereas the second hop reads the bridge ("that person's country") as an entity, from the middle layers on: patching the model's own representation of the entity into the bridge at those layers largely restores the second hop, yet after fine-tuning the bridge there is no closer to the new entity than before the edit. We therefore propose read-equivalent writing (Legible): one loss term makes the bridge phrase, at the layer where the second hop finishes reading it, match the model's own reading of the new entity, and keeps the same relation's other subjects unchanged. Phrases and targets come from the edited model itself, and no multi-hop training data is used. Across Qwen2.5, Llama-3 and Qwen3, Legible (I) composes learned facts more often than the model composes its own knowledge, on MQuAKE's two-hop-curse questions; (II) reaches 1.8-2.6x the bridge accuracy of CaKE, whose reasoning data composes no better than plain fine-tuning, and has the best average over composition, accuracy and locality against four families of writers; and (III) lifts the curse on RippleEdits, on the benchmark of Balesni et al., who named the curse, and at 14B.

---


### 196. [From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents](https://arxiv.org/abs/2611.01527)

**<font color=#1a73e8>作者：</font>** Xingyu Yi, Xinya Zhang, Yunshen Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A scientific agent can give the same verdict while reading and citing different evidence. BioAgent-DF tests this separation using paired reference and candidate values saved at the same scientific computation site. It restores or transplants those values at their original coordinates, then runs the agent on healthy hardware. Across eight SciFact batches, Qwen3.5-4B shows repeatable citation changes in three capture-claim combinations, and Gemma 3 4B IT shows repeatable read and citation changes in four. These seven combinations cover two claims. Full restoration recovers the reference evidence sets while verdicts remain unchanged. Verdict changes observed under the baseline prompt did not recur under the explicit-example prompt. Complementary tool and optimizer experiments distinguish recovery of numerical state, recovery of ranked lists, and restoration of an agent's visible history. These results show that an audit should track both the evidence an agent uses and its final answer. In hERG cardiac-safety assay allocation, silent numerical faults changed testing decisions while the fixed-budget shortlist kept the same number of compounds labeled as blockers. After the agent had used faulty values, restoring its earlier execution state and supplying certified scores recovered all 39 changed decisions, whereas replacing the prediction file recovered none; no incorrect action was committed. A streaming implementation of the arithmetic checks reduced the total time for forward execution and verification by 42.4% relative to the original FP64 implementation, with identical flags and recovery outputs.

---


### 197. [AR-RRG: Anatomy-Guided Retrieval-Driven Radiology Report Generation](https://arxiv.org/abs/2611.01529)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Shijie Song, Wanqing Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation (RRG) streamlines clinical workflows and alleviates the burden of radiologists' documentation. Standard vision-language models capture global visual cues and lack fine-grained alignment between anatomical regions and diagnostic text. Most retrieval-augmented methods retrieve complete historical reports, introducing redundant noise and severe vision-text mismatches that trigger clinically risky hallucinations and missed lesions. In this paper, we introduce AR-RRG, an anatomy-guided retrieval-driven method for the generation of radiology reports. AR-RRG consists of two core modules: the anatomy-aware self-training lesion detection network (ASLDNet) and the retrieval-driven radiology report generation (RRRG). ASLDNet leverages anatomy-aware spatial verification (ASV) and class-adaptive dynamic thresholding (CDT) via self-training, delivering accurate lesion localization to support subsequent generation. As the generative branch of AR-RRG, RRRG eliminates clinical hallucinations through dual-granularity retrieval (DR) and complements missing lesions with a neighborhood consensus (NC) mechanism. A parallel continuous visual perception (PCVP) stream converts radiographs into visual tokens through fixed medical encoding and resampling. Multi-scale text and visual features are fused, followed by LoRA-efficient large language model tuning to generate clinically consistent, visually grounded radiology reports. Extensive evaluations on MS-CXR, MIMIC-CXR, and IU X-Ray demonstrate that AR-RRG consistently outperforms state-of-the-art methods across mainstream metrics. Our code will be made publicly available.

---


### 198. [MoPort: A View-Aware 2D Interface for Motion Language Models](https://arxiv.org/abs/2611.01541)

**<font color=#1a73e8>作者：</font>** Lixing Tan, Qing Xia, Yuting Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion language models (MoLMs) encode 3D human motion as discrete tokens for language-based understanding. Deploying them on monocular video raises two problems. Pose detection yields 2D joint sequences, leaving a dimensional gap from the 3D motion used in training. Moreover, the 2D observation changes with the camera viewpoint, while the depth lost in projection makes the 2D pose ambiguous across viewpoints. We propose MoPort, a view-aware 2D interface that enables MoLMs to take 2D observations as input. We introduce Paired View Alignment (PVA), which gives two views of the same motion a shared 3D teacher target and directly constrains the consistency of their latents, so that 2D observations from different viewpoints are mapped to a consistent semantic representation. Camera-Modulated Encoding (CME) estimates the camera extrinsics from the 2D sequence and uses them to modulate encoding, providing the 2D latents with geometric information about the viewpoint. MoPort achieves R@1 of 0.5674 on HumanML3D and 0.3286 on KIT-ML, outperforming all evaluated baselines. On HumanML3D, its R@1 decreases only from 0.5763 on in-distribution viewpoints to 0.5585 on out-of-distribution viewpoints. We validate portability on three downstream MoLMs. Furthermore, on the real-world RGB video dataset Fit3D, MoPort achieves 80.36\% accuracy. Code will be released upon acceptance.

---


### 199. [Revisiting LLM Homogeneity Through a Multidimensional Lens](https://arxiv.org/abs/2611.01549)

**<font color=#1a73e8>作者：</font>** Ziliang Qiu, Renfen Hu, Yi Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Concerns about LLM homogeneity are typically quantified with embedding similarity, which reduces two texts to a single score. We revisit homogeneity with 25 interpretable metrics spanning five dimensions: semantic, lexical, syntactic, structural, and stylistic & presentational. A human study shows that perceived similarity depends on both content (what responses say) and form (how they say it), yet embedding similarity correlates less with human meaning judgments than sentence-level matching ($\rho=0.417$ vs. $0.606$) and not significantly with form judgments ($\rho=0.140$). Across 18 contemporary LLMs, models say similar things in different words: they share global semantics and broad linguistic profiles but remain distinct in lexical characteristics, structural patterns, and interactional conventions. Across releases from 2024 to 2026, models become more like themselves but not more like one another: among significantly changing metrics, intra-model distances decrease for 17 of 22, and inter-model distances increase for 14 of 21. Across two post-training pipelines, model-specific conventions emerge during SFT and are selectively reshaped by preference optimization. These results suggest that homogeneity is multidimensional and evolving, and that embedding similarity alone can overstate cross-model homogeneity while concealing diverging intra- and inter-model trends.

---


### 200. [Can Large Language Models Extend Their Agentic Capabilities to Goal Pursuit in Open-Ended Multi-Turn Interaction?](https://arxiv.org/abs/2611.01552)

**<font color=#1a73e8>作者：</font>** Mingyu Chen, Jingkai Lin, Xiaofen Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Goal pursuit in open-ended dialogue requires agents to adapt their actions to interaction feedback across successive exchanges. We investigate whether agentic capabilities developed for multi-step tool use carry over to dialogue organized through the model's native tool interface, and how this changes interaction behavior. We define Tool-Mediated Interaction (TMI) as a training-free protocol that represents dialogue actions as tool calls and counterpart responses as tool results, maintaining a continuous reasoning-action-observation loop with retained reasoning and interaction history. We evaluate TMI across social interaction, emotional support, persuasion, and price negotiation using two models and 15,678 main-experiment episodes. Across both models, TMI improves social goal attainment, emotional-support preference, donation amounts, and buyer negotiation margins over conversational baselines with and without thinking. A Qwen ablation further shows that TMI outperforms ordinary conversation with retained reasoning on all four primary outcomes. Behavioral analyses associate the improvements with task-specific patterns in initial proposals and responses to interaction feedback. Alongside these gains, TMI reduces mean reasoning tokens per decision by 42.0-81.5% relative to the thinking baseline and lowers mean cross-turn phrase reuse across all eight model-environment pairs. These findings show that interaction organization shapes both goal attainment and reasoning across dialogue turns.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
