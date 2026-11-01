# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 1. [Scoring Explanations Without Reading Them: Structural Shortcuts in Automated-Interpretability Evaluation Data](https://arxiv.org/abs/2610.37676)

**<font color=#1a73e8>作者：</font>** Xupeng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated interpretability scores an explanation of a sparse-autoencoder (SAE) feature by asking a model to predict, token by token, where the feature fires on evaluation examples or to judge whether marked tokens fit it. We find that the evaluation data standard pipelines build can be scored without reading the explanation. On Neuronpedia's stored fuzzing runs for 500 random GPT-2 small features, 91.3% of activating examples are cropped with the peak on the centre token, and a rule that says "yes" when the centre token is marked reaches balanced accuracy 0.979, against 0.838 for the stored LLM scorers (recomputed from the stored per-item verdicts, on marks rebuilt from the pipeline's code); a rule reading only the mark count reaches 0.969. The cue changes form across pipelines: current delphi always marks the same slot in its fuzzing negatives, and full-context runs mark negatives with more tokens. OpenAI's simulation benchmark lists each neuron's top-activating sequences first; a rule that predicts activity on the first five scores 0.227 in pooled correlation against 0.160 for GPT-4's published simulator (post hoc). We give closed forms for what such rules can score; show that one scorer's simulation scores are higher on stored snippets than on natural windows but not shown to be reordered; and build windows that remove the position cue, derive but do not build negatives that remove the mark cues, and separate the sequence cue by decomposition. On natural-text windows cut at random offsets, the best fixed-offset prior shared by all features scores 0.015. On them, that scorer, a typed decision model (Jev), reaches a pooled correlation of 0.331 over 49 features, against 0.013 with shuffled explanations, and an open 8B simulator with the original read-out reads the explanation there (0.194 against 0.019). Scores should be reported beside the best explanation-free rule on the same items.

---


### 2. [Exposure Is Not Commitment: Double-Stratified Evaluation of Latent Monitors for Tool-Using Agents](https://arxiv.org/abs/2610.37679)

**<font color=#1a73e8>作者：</font>** Rishabh Sinha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-using language agents are vulnerable to indirect prompt injection, and a growing literature probes model internals to catch unsafe actions before they execute, with sharply conflicting results. We argue much of the conflict is an evaluation artifact, and propose a double-stratification protocol: separate injection exposure from behavioral commitment, in both the evaluation and the training population. On the primary Qwen AgentDojo grid, monitors trained on the naive mixed unsafe-versus-rest contrast mostly learn exposure: they flag exposed trajectories whether or not the agent complies, and barely predict which cases turn unsafe. Retrained on exposed cases only, the same probe families predict the model's own unsafe tool call up to two steps early, the maximum the three-step trajectories admit (logistic AUROC 0.853, matched by a trained TF-IDF text baseline at 0.855). Mistral-7B reaches 0.896 and OLMo-2-7B 0.912; their naive contrasts learn different things: inverted exposure ranking on one, both axes on the other. Representations separate on exposure (probe 1.000 versus trained text 0.908) and where visible context is sanitized or unavailable. Training contrast alone reproduces the shape of recent pre-action-probe negative results, one candidate explanation for the conflict: the signal exists, but the model's own zero-shot forecast and NLA verbalizations do not reliably recover it. An unstratified AUROC overstates what a latent monitor knows, and what a naive contrast learns is population-dependent: evaluations should stratify both.

---


### 3. [Artifact Distillation: Training-Free Transfer from Frontier to Small Language Models](https://arxiv.org/abs/2610.37680)

**<font color=#1a73e8>作者：</font>** Mustafa Safa Ozdayi, Somin Wadhwa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Closing the gap between frontier and smaller language models is usually approached by distillation: fine-tuning the small model (student) on a frontier model's (teacher) outputs, which binds transfer to training compute and leaves the transferred knowledge largely opaque. We propose Artifact Distillation: a teacher solves training instances and externalizes its problem-solving procedure into an artifact bank that a student queries at inference time, with no gradient updates. Across four LiveBench tasks, a bank written by Claude Opus 4.5 lets Claude Haiku 4.5 outperform unaided Claude Sonnet 4.5 on spatial reasoning (0.707 vs. 0.647) at 60% of its cost, and reach Sonnet 4.5's level on table joining at 89% of its cost. The same raw bank raises Qwen3.5-27B's pooled score from 0.730 to 0.800, showing that transfer is not confined to the teacher's model family.

---


### 4. [Supervised Fine-Tuning for Reasoning Large Language Models: A Survey](https://arxiv.org/abs/2610.37681)

**<font color=#1a73e8>作者：</font>** Yongcan Yu, Kuangpu Guo, Jian Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models have recently demonstrated remarkable capabilities in solving complex tasks, where supervised fine-tuning (SFT) on long chain-of-thought data serves as a crucial foundation for eliciting and enhancing their reasoning abilities. Despite rapid progress in both improving and analyzing reasoning-oriented SFT, the field still lacks a systematic survey that consolidates its fast-growing literature. To fill this gap, we present a comprehensive review of recent advancements in reasoning SFT, examining the literature through the dual lenses of methodological design and analytical investigation. First, we review methodological improvements across the SFT pipeline and categorize them into data-centric approaches and algorithm-centric innovations. Second, we reorganize analytical studies along three dimensions: data characteristics, optimization dynamics, and mechanistic insights. Finally, by synthesizing current research focuses and remaining bottlenecks, we outline promising future directions for reasoning SFT. We hope this survey deepens the understanding of reasoning SFT and paves the way for advanced reasoning models.

---


### 5. [Rank-Aware Differentially Private Release of Listwise Preferences for LLM Alignment](https://arxiv.org/abs/2610.37682)

**<font color=#1a73e8>作者：</font>** Junwei Chen, Manjiang Yu, Pengpeng Qiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Listwise preference feedback offers richer supervision for large language model (LLMs) alignment than pairwise comparisons, but a full ranking also reveals more sensitive user preferences. Existing privacy-preserving alignment methods focus mainly on pairwise feedback, while listwise alignment under local differential privacy (LDP) remains unexplored. Extending LDP to this listwise domain raises a critical challenge: the high sensitivity of the full ranking space demands excessive noise, neutralizing the benefits of listwise supervision. To address this challenge, we analyze the interaction between supervision granularity and privacy noise in downstream training, and introduce a rank-aware exponential mechanism that privatizes listwise preference data into a low-sensitivity granularity suitable for downstream alignment. The mechanism leverages ranking information to sample a fixed-size binary partition, concentrating the noise near borderline items instead of perturbing all items uniformly as randomized response (RR) does. Empirical evaluations on downstream LLM alignment tasks show that our mechanism consistently outperforms existing LDP baselines at matched privacy budgets. The code is available at this https URL.

---


### 6. [Prompt-agnostic Language Models](https://arxiv.org/abs/2610.37683)

**<font color=#1a73e8>作者：</font>** Frederic Sadrieh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their strong performance, large language models remain highly sensitive to prompt formulation. This issue is typically addressed at inference-time through manual prompt optimization, which introduces overhead and lacks scalability. Conversely, we focus on train-time approaches that build prompt robustness into the model during instruction tuning. A common strategy is to mix multiple paraphrases of each prompt into training. We demonstrate that across trainable parameters, the per-paraphrasing gradients interfere, with 57% exhibiting sign conflicts and the naive gradient average discarding approximately a fifth of the magnitude. Therefore, we develop two gradient-merging methods, Prompt-TIES and Prompt-DARE, that address this interference by leveraging interference-resolution operators from model and gradient merging and applying them to prompt gradients. In this study, we compare the efficacy of our methods to increase model robustness to train-time robustness methods spanning all three established classes: data construction, consistency regularization, and contrastive alignment. The evaluation is conducted across four models from two families at two scales. We observe the interaction between prompt phrasing and the specific examples accounts for 54% of per-example variability on average, and exceeds 70% on tasks such as ANLI and WiC. The gradient-merging methods directly improve this local robustness and nearly halve per-example variance on fully fine-tuned models at little cost to overall accuracy. The other train-time methods enhance raw performance, but fail to improve per-example variance reliably. Code: this https URL. Model checkpoints: this https URL.

---


### 7. [An Introduction to Large Language Models for Scientists and Professionals](https://arxiv.org/abs/2610.37684)

**<font color=#1a73e8>作者：</font>** Umberto Michelucci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have rapidly become important tools for science, education, medicine, and professional work. Despite their apparent simplicity from the user's perspective, effective and responsible use requires an understanding of how these systems work, what their limitations are, and how their outputs should be evaluated. I wrote this document as a basis for my lecture on LLM in the master in artificial intelligence in medicine at the university of Turin, Italy. This book provides a practical and accessible introduction to LLMs for scientists and professionals. It explains the fundamental ideas behind tokenisation, embeddings, training, inference, context windows, prompting, and instruction hierarchies, while deliberately avoiding mathematical detail. Particular attention is given to the limitations of LLM-generated answers, including hallucinations, uncertainty, reproducibility, bias, and the need for systematic verification and human oversight. The book also discusses privacy, governance, security, and the responsible handling of personal and sensitive information. More advanced topics include Retrieval-Augmented Generation (RAG), retrieval quality, chunking, embeddings, vector search, agents, tools, and workflows. A substantial practical exercise guides the reader through running a local LLM with Ollama and Open WebUI and using it to interact with a collection of scientific papers. The exercise emphasizes evidence retrieval, source verification, uncertainty, disagreement between studies, and the distinction between plausible language and scientifically supported conclusions. No programming knowledge is required.

---


### 8. [From Geometry to Behavior: How Instruction Exposure Unlocks Latent Rhetorical Directions in LLMs](https://arxiv.org/abs/2610.37685)

**<font color=#1a73e8>作者：</font>** Shengjie Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models do not merely memorize facts; they absorb rhetorical strategies from pretraining data, including the human tendency to reason by analogy. We ask: is this absorbed capability geometrically accessible before any instruction tuning, and what determines whether it can be activated at inference time?
We extract an "Analogy Vector" from the residual stream via difference-in-means and show it enables steerable explanation style across seven instruction-tuned models (Gemma-2, Llama-3.1, Qwen-2.5; 2B-32B), improving harmonic mean from 3.22 to 3.94 (+22%) for Gemma-2-9B-IT on 300 held-out test prompts. A small human validation study confirms the LLM judge on Analogy Quality.
Our central finding, from seven matched base-instruct pairs, is a gradient of behavioral accessibility: the analogy direction exists in every base model, but its behavioral accessibility under linear intervention scales continuously with instruction exposure during training. Gemma-2 base models (strict pretraining/IT separation) show flat steering landscapes: present but behaviorally inert. Qwen-2.5 base models (instruction data woven into pretraining) are already partially accessible before any explicit fine-tuning; base-instruct cosine similarity of the analogy vector reaches 0.94-0.97 for Qwen versus 0.37-0.66 for Gemma, providing geometric corroboration of the behavioral gradient. This challenges the binary "base vs instruct" framing: the relevant variable is how much instruction exposure a model has received across its full training pipeline. We position activation steering as a complementary interpretability tool that reveals how instruction exposure organizes rhetorical knowledge in activation space.

---


### 9. [Rethinking Social Simulation in Open-Population Systems: From Persistent Agents to Communication Processes](https://arxiv.org/abs/2610.37687)

**<font color=#1a73e8>作者：</font>** Yunyao Zhang, Yihao Ai, Boqi Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled social simulation with persistent agents, where fixed computational individuals maintain internal states and interact over time. However, large-scale social networks are inherently open-population systems: the participating population changes over time, users enter and leave dynamically, and only a sparse subset becomes observable through communication at any given time. In such systems, persistent account identities do not provide continuously observable individual-state trajectories, making recursively maintained psychological states insufficiently grounded in empirical observations. We therefore shift the simulation target from persistent individual trajectories to the observable evolution of social communication, modeling who participates, what they communicate, and how these communications shape subsequent system dynamics. We instantiate this formulation with participant activation from a global user pool, collective state transition, and an LLM policy for communication generation, while explicitly separating environmental inputs from endogenous system evolution. Across five Qwen backbones, our framework reduces average KL divergence by 71.2% over Direct LLM and 35.0% over MF-LLM, with boundary and counterfactual experiments further validating the proposed modeling boundaries. Our results support communication-centered simulation as a principled formulation for long-horizon open-population social systems. Project Website: this https URL

---


### 10. [Bouba Beats Kiki, and Other Regularities in the Subjective Preferences of LLMs](https://arxiv.org/abs/2610.37692)

**<font color=#1a73e8>作者：</font>** Katy Blumer, Jon Kleinberg, Ravi Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users engage with large language models on tasks that are purely objective ("When was Netflix founded?"), purely subjective ("What should I name my child?") or anywhere in-between. We have rich tools for evaluating model accuracy with respect to objective criteria. However, when it comes to subjective aspects of a task, we do not have similarly developed methodology at hand. In this paper, we take some early steps towards framing the question of subjective evaluation. Rather than measure how often a model is right or wrong on a question, we instead ask, how do models make choices among multiple viable responses without a clear winner?
To study this question, we restrict our focus to short-form content, and consider comparison tasks among three such content types: numbers, baby names, and fictional cities. We identify 29 aspects of these short-form examples covering many areas of syntax and semantics (length, alphabetic order, popularity, vowel mix, spoken sound, etc.). We show first that models tend to have strong and reproducible preferences for or against some of these aspects. Second, we show that variations in how the model is asked to express a preference may cause some of these aspects to activate or deactivate in the model's selection. Third, we show that overall preference distributions among pairs may vary radically based on seemingly-unimportant variations in the nature of the question posed to the model, raising new questions about manipulation. And finally, we show that, if models are used both to create lists of alternatives and to rank them, there are unexpected interactions between the two stages that may also drive the models' stated preferences.

---


### 11. [Network Topology Does Not Matter: The Breakdown of Classical Consensus in LLM Populations](https://arxiv.org/abs/2610.37699)

**<font color=#1a73e8>作者：</font>** Sahil Rajesh Dhayalkar  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As multi-agent language model networks become widely deployed, predicting their collective behavior is a critical challenge. Classical distributed consensus theory relies on network topology to predict convergence, structurally assuming that agent updates are convex combinations, population means are conserved, and weights are content-independent. In this work, we demonstrate that these foundational assumptions fail for large language models (LLMs). By deterministically extracting continuous credence from token-level probabilities across eight instruction-tuned models and 73,080 controlled exchanges, we directly measure the empirical LLM update operator. We find that LLMs systematically violate convexity by updating outside the hull of observed opinions, exhibiting active repulsion (negative weights) that fundamentally breaks row-stochastic modeling and standard bounded-confidence repairs. Scaling these empirically fitted operators to simulations of 10,000 agents reveals that algebraic connectivity explains almost none of the final outcome variance. Instead, population dynamics are governed entirely by the model's internal update bias and message framing. Consequently, populations of several models, including those with up to 7B parameters, reliably compound small local drifts to reach confident agreement on objectively false claims regardless of their network structure. Our results prove that classical graph-theoretic metrics are inadequate for LLM populations, highlighting a profound deployment risk where multi-agent deliberation predictably saturates in collective delusion.

---


### 12. [The Coordination Tax and the Heterogeneity Dividend: Break-Even Conditions for Multi-Agent LLM Pipelines](https://arxiv.org/abs/2610.37700)

**<font color=#1a73e8>作者：</font>** Andreas Zettl, Diego Gosmar  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM pipelines built on interoperability protocols such as the Open Floor Protocol (OFP) or A2A are usually justified on capability grounds, with their runtime cost treated as an overhead of unknown size. Comparing such a pipeline with one model call is underspecified, because a pipeline can give each role a different model. We give a closed-form model that sets the coordination tax (decomposition overhead plus per-handoff protocol cost) against the heterogeneity dividend from routing work to a cheaper model, with a break-even threshold and a feasibility bound, $\alpha < 1/r$, and measure every term, with OFP as the protocol under test, on 135 HumanEval and ClassEval tasks in 2430 runs of six architectures with Claude Opus 5.5 and Haiku 5.5. The protocol adds 7.2 ms per handoff, 0.11% of pipeline wall time. Decomposition does not pay on these tasks: a planner-coder-reviewer pipeline costs 3.22x as much as a single strong call, takes 3.24x as long, and solves no more tasks. Moving planner and reviewer to the cheap model cuts the pipeline's cost to 0.39x but changes pass@1 by -6.7 points, leaving it dearer, slower and less accurate than the single call, and the break-even forecast misses by -19% because the cheap roles inflate token volume. The saving lies in choosing a model per task instead: an oracle choice between the two single calls solves 94.3% of runs at half the strong call's cost per solved task.

---


### 13. [Generation, Not Selection: LLM Proposals for Certified Access-Control Policy Mining](https://arxiv.org/abs/2610.37716)

**<font color=#1a73e8>作者：</font>** Gautam Kumar, Ravi Sundaram, Shamik Sural  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attribute-Based Access Control (ABAC) policy mining---recovering a compact, auditable policy from an access log---is posed as minimum set cover and solved greedily, which enjoys an $s^{*}(1+\ln m)$ guarantee. That guarantee is \emph{conditional} on a precondition the literature never states: the candidate pool handed to greedy must contain the optimal rules. Generation, not selection, is the binding constraint, and existing generators are purely \emph{syntactic}---they surface a rule only when enough log records witness it, so they fail on precisely the rare exception rules that fill a heavy-tailed policy. We replace the generator with a language model proposing rules \emph{semantically}, from attribute names, and keep the combinatorial selector to carry the guarantee: every proposal is filtered against the observed denials, so soundness is independent of the proposal mechanism and an unreliable proposer can only waste candidates, never grant access. Over five seeds on each of two enterprise domains, adding semantic proposal to a syntactic miner dominates it on \emph{ten of ten} runs---strictly better on seven---with near-optimal policies ($9.2$--$9.6$ rules against $s^{*}=9$, versus $11.2$--$14.6$) and false grants cut four- to sevenfold. Replacing the syntactic miner rather than augmenting it wins only where witnesses are scarce. An anonymization ablation isolates the mechanism: opaque attribute names cost two thirds of the model's rule recovery while leaving the syntactic baselines provably unmoved, and cost nothing where witnesses are plentiful. Semantic knowledge and log evidence are substitutes.

---


### 14. [What a Weight Update Buys: Leverage Across Training Stages](https://arxiv.org/abs/2610.37719)

**<font color=#1a73e8>作者：</font>** Shikhar Shiromani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training moves a language model's weights by about a thousandth of their norm and changes its behavior sharply; pretraining moves them by a third and buys a slow drift. We introduce leverage, an exact measure of what a unit of weight change buys: the Fisher quadratic form of an update, computed with one forward-mode pass per direction, divided by the same form for random directions of the same size at the same checkpoint. Leverage orders released Olmo-3, Tülu-3, Zephyr, and OLMo-2 checkpoints over four orders of magnitude: pretraining windows sit at the random level on prose, SFT five times above it, RL-Zero and RLVR at 400-1,500, and DPO at 400-23,000. With this instrument we find that pretraining accumulates into noise: windows of 30k to 1M steps are no more consequential on prose than random directions of their size, as a noisy quadratic model of SGD predicts. We find that training precision changes what an update looks like: training bf16 parameters without an fp32 master copy freezes 36-99% of coordinates, lowers leverage up to sevenfold, and creates an alignment between update magnitudes and the diagonal Fisher that fp32 training does not show. We derive and verify a law for reuse: the sign-flip null predicts the relative damage of random drop-and-rescale (DARE) at keep rate $p$ as $(1-p)/(p\,\rho_{\mathrm{sign}})$, within a factor of two of measurement wherever DARE succeeds. Two controls make these readings reliable: every controlled SFT and DPO trajectory with fp32 master weights loses leverage as it moves, and two re-runs of a released DPO stage from its anchor with its published recipe land within 1% of the released displacement and 4% of its leverage, where a plain recipe reads five to six times lower; leaving one component out traces the level to the length-normalized loss and its batch size of 128 together.

---


### 15. [LRMoE: Demand-Side Load Re-Calibration for Efficient MoE Training on Memory-Constrained Nodes](https://arxiv.org/abs/2610.37720)

**<font color=#1a73e8>作者：</font>** Jiaming Hu, Zhida Jiang, Zhaolong Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models offer scalable capacity for Web applications, but uneven routing creates computation and communication bottlenecks. Existing placement and replication methods redistribute this workload, yet additional expert copies compete with token-related buffers for limited GPU memory. We present LRMoE, a memory-aware MoE training system that jointly recalibrates backward demand and balances the retained workload. During forward execution, it plans retention quotas and expert placement under resource constraints while preserving all routed computations. During backpropagation, a load recalibration metric estimates each token-expert pair's contribution to the expert update and selects pairs within these quotas. A capacity-aware routing algorithm distributes retained pairs among eligible instances of their original experts. Physical compaction then forms smaller communication payloads and variable-size grouped GEMMs, reducing backward traffic, computation, and execution-buffer demand. Experiments on Qwen3-30B-A3B and GLM4.5-106B-A12B show that LRMoE reduces cumulative MoE-layer training time to fixed-loss targets by 21.2-44.8% relative to SYMI.

---


### 16. [ThinkJev: One Thought, Every Budget for Calibrated Typed Decisions](https://arxiv.org/abs/2610.37732)

**<font color=#1a73e8>作者：</font>** Xiaolu Ding, Kai Yang, Dongdong Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many uses of language models end in a typed decision: a choice among a closed set of options, whose probabilities code can act on. Reading those probabilities from one forward pass is fast but often wrong on decisions that take several steps, such as arithmetic, counting, and date comparison. Letting the model think first fixes most of these errors, but costs seconds per decision instead of milliseconds. To pay for thinking only where it helps, ThinkJev builds a fast and a slow system from one open hybrid-thinking model that can answer directly or after a thought. System 1 reads the model's probabilities for the option letters when it answers directly; System 2 reads the same letters after the model has thought on the same cached prompt, so escalating repeats no work and both systems give probabilities over the same options. Because the letters can be read after any number of thought tokens, one sampled thought also gives the answer under every thinking budget. Without training, ThinkJev lets System 1 answer alone only where a statistical test on labeled dev data guarantees that its accepted answers stay under a target error rate. At a 5% target, Qwen3.5-27B answers 24.5% of 8359 test decisions this way with a realized error of 3.9% (Qwen3.5-4B and 9B: 6.5% and 0.0%). For the rest, stopping each thought as soon as its answer is confident reaches 81.6% accuracy, against 82.7% for always thinking, with 72% of the thought tokens. Choosing when to think from System 1's confidence alone saves less, because the decisions System 1 is least sure of are often not the ones thinking fixes. On the public items of JevBench, an independent benchmark of typed-decision services, Qwen3.5-27B thinks on 29.4% and is not distinguishable in accuracy from the two thinking APIs listed (exploratory). Code and data generators are available at this https URL.

---


### 17. [When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills](https://arxiv.org/abs/2610.37734)

**<font color=#1a73e8>作者：</font>** Timofey Sanko, Yuan Tian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills, reusable instruction packages centred on a this http URL file, extend AI agents on demand, and a single line in a widely copied skill reaches every agent that loads it. Some lines are oversight-loosening directives: they tell the agent to proceed without approval, to bypass checks with --no-verify, or to keep working without checking in. Although such directives can remove a checkpoint from every agent that loads them, no prior work has examined them. We present the first large-scale study of oversight-loosening directives, analyzing 1.53 million English skills from GitSkills. We split skills into units (sentences, bullets, table cells, and code lines), develop a codebook that labels oversight directives by polarity, mechanism, and scope, label 2,097 units by hand, and train a detector to scale the analysis. Our results show that about one in seventeen skills (about 88,000 skills) contains a loosening directive. These directives most often loosen oversight through permission flags, and most of them (70.1%) apply unconditionally rather than only in specific contexts such as CI. Compared with skills that have the same amount of oversight language, skills that run shell code, install packages, or use sudo have 1.7-1.8 times the odds of containing a loosening directive, an association that holds across all our robustness checks, and they do not compensate with more tightening. Loosening spreads through a few upstream skills rather than through edits by their adopters: 2.4% of the skill families that carry loosening account for half of all copies of loosening-carrying skills, and 1.1% of distinct loosening units for half of all loosening occurrences. Open-source skill scanners catch at most 46% of loosening directives, with a precision below 0.4, while the LLM behind them, prompted with our codebook instead, catches 61% at a precision of 0.71.

---


### 18. [OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery](https://arxiv.org/abs/2610.37739)

**<font color=#1a73e8>作者：</font>** Jiarui Yao, Ruida Wang, Tong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown increasing promise in research-level problem solving, yet a comprehensive collection of such problems is still missing, and evaluating them on research-level problems remains challenging. We introduce OpenFrontiers, a cross-disciplinary resource that combines a structured corpus of open research problems with a retrospective benchmark of recently resolved problems in mathematics. The corpus records problem statements, context, progress, and other information for 12,151 problems. The benchmark contains 200 problems, 110 resolved in 2026 and 90 still open, each with a Lean~4 statement checked by automated probes and two independent reviews; a subset HQ-50 further filters based on quality score, etc. Our evaluation protocol grades formal proofs with two independent checkers in an isolated sandbox under closed-book, frozen-retrieval, and live-web conditions. Evaluating seven LLM agents on the HQ-50 subset under a standardized budget, we find that closed-book rediscovery is rare, at most 7 of 40 resolved problems, whereas live-web success mostly reflects retrieval of published solutions. By linking a broad research-problem corpus to a formally graded evaluation subset with documented solutions, OpenFrontiers provides a foundation for measuring research-level rediscovery and studying progress toward solving currently open scientific problems. The dataset and benchmark could be found in this https URL.

---


### 19. [Multi-Draft On-Policy Distillation for Diffusion Drafters](https://arxiv.org/abs/2610.37778)

**<font color=#1a73e8>作者：</font>** Petr Molodyk, Yuchen Zhu, Jaemoo Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is used to reduce the inference cost of language models. One-step diffusion drafters propose a block of multiple tokens in parallel, reducing the sequential cost of speculative decoding. On-policy distillation trains these drafters using verifier feedback on their own proposals. However, parallel drafting makes this feedback difficult to use: the drafter predicts each token without observing the preceding tokens sampled within the same block, while the verifier conditions its prediction on those tokens. Different sampled prefixes therefore give different verifier targets for the same drafter prediction. We show that distilling against these targets separately can suppress tokens that are plausible after some prefixes but unlikely after others, harming draft acceptance. We explain the effects of this mismatch and introduce Multi-Draft On-Policy Distillation (MDraft), a new parallel drafter distillation method which samples several draft blocks from the same context and aggregates the verifier's full-vocabulary conditionals across their prefixes. We use all the drafts to collect information from the verifier, allowing support from alternative prefixes to influence the training target. The resulting algorithm improves the acceptance length of a parallel drafter beyond the level of pre-training, and alleviates the effects of the distributional mismatch. MDraft changes only training, retaining the drafter's architecture and inference procedure, allowing the resulting drafter to be used as-is in place of the pretrained checkpoint. Experiments on a suite of mathematical, coding, and conversational tasks show longer accepted drafts than prior distillation methods.

---


### 20. [Selective and Hybrid-State Communication for Latent Multi-Agent Systems](https://arxiv.org/abs/2610.37779)

**<font color=#1a73e8>作者：</font>** Miles Liao, Aaron Smieszek, Yuhao Ge  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Efficient communication remains a major bottleneck in large language model multiagent systems. Latent communication reduces repeated natural-language exchange by transferring internal model states between agents, but these transfers remain costly and are typically designed around conventional KV-cache representations. We address this problem from two complementary perspectives. We introduce SelectKV, a boundary-aware method that selectively communicates KV states while protecting inherited context, and HyLaMAS, which extends latent collaboration to hybrid linear-attention models by communicating both KV caches and recurrent states through a shared workspace. Across six benchmarks, SelectKV reduces communicated KV positions and logical KV payload by 9.7-9.9%, with accuracy unchanged on two benchmarks, within one percentage point on three, and six points lower on HumanEval+. Across Qwen3.5 model scales, HyLaMAS reduces decoded output tokens by 53-80% and achieves 1.16-2.78x speedups relative to text-based multi-agent communication. Together, these independently evaluated methods represent two complementary approaches to efficient latent-state communication across conventional Transformer and hybrid model architectures.

---


### 21. [WebAnything: From the Wild Web to Scalable Agent Environments](https://arxiv.org/abs/2610.37786)

**<font color=#1a73e8>作者：</font>** Tianci Xie, Zikun Cai, Chaoyun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observations, with interaction coverage constrained by captured content and replay capabilities.
We present WebAnything, a fully automated framework that reconstructs source-grounded, reusable Web environments from real URLs without per-site manual implementation or repair after initial setup and authorization. An Explorer-Builder collects browser-observable structures, resources, and interaction outcomes; an independent verifier checks frozen candidates and guides local repair or targeted source recapture.
We construct 244 website artifacts across 14 application domains and 53 categories, supporting 12,984 executed and accepted tasks. Compared with human-assisted WebHarbor, WebAnything achieves higher aggregate scores on three fidelity metrics, with 12 wins, two ties, and no losses in a blind audit. Fine-tuning Qwen3.5-9B on 5,856 interaction trajectories improves REAL success by 9.9 percentage points, Odysseys-Easy Rubric Avg and Task Avg by 6.25 and 6.32 percentage points, and WebArena-Verified Overall success by 13.33 percentage points under the fixed harness. Code: this https URL

---


### 22. [Locating Sycophancy Across Training Stages in Open Language Models](https://arxiv.org/abs/2610.37788)

**<font color=#1a73e8>作者：</font>** Jiarui Yao, Shweta Parihar, Nghia Tuan Bui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model assistants sometimes change a correct answer when the user suggests a wrong one. The behavior, called sycophancy, is usually attributed to preference-based post-training, yet early measurements found it in pretrained models. We ask where it comes from by measuring it at every available stage of training: 13 open checkpoints from 5 lineages, from base model through supervised fine-tuning and preference optimization to release. We separate how far an injected claim moves a model's answer from how firmly the answer was held, and vary who makes the claim, how reliable they are said to be, and how strongly they make it. Two sycophancy behaviors with different origins emerge, and both replicate across datasets. Deference to a claim in the prompt is already present in every base model, which ranks sources in the same order as its post-trained descendants. Capitulation in conversation, dropping a stated answer when the user objects, is largely absent from base models and present in every post-trained checkpoint. When the objection names an alternative, most post-trained models give up firmly held answers as often as loosely held ones. We discuss the implications of these measurements for evaluating sycophancy and approaches for addressing each behavior.

---


### 23. [Spokes, not a Ring: Revisiting the Weekday Manifold in Language Models](https://arxiv.org/abs/2610.37796)

**<font color=#1a73e8>作者：</font>** Diksha Gupta, Rieke Fruengel, Stefan Heimersheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has hypothesised that large language models may represent some concepts as multi-dimensional manifolds instead of single directions. Using these manifolds to interpret or steer representations often assumes that moving along them corresponds to a continuous change in the represented concept. In this work, we test this continuous manifold assumption on the prototypical weekday manifold. Despite its striking circular geometry, we find that the weekday representations behave more like seven discrete states arranged in a circle than a continuous ring. First, we show that local sensitivity has seven minima aligned with the weekdays, producing a step-like mapping between representation and behaviour under on-manifold steering. Second, we test whether any concepts are represented along the manifold outside the seven discrete states, and find neither time of day, uncertainty, nor natural text populate the intermediate space. Together, these results challenge the continuous interpretation of the weekday manifold and motivate testing whether movement along other representation manifolds correspond to meaningful changes in model representations and behaviour.

---


### 24. [Structured Security Explanations for Learning-Based Vulnerability Detection](https://arxiv.org/abs/2610.37797)

**<font color=#1a73e8>作者：</font>** Fares Trad, Yizhou Chen, Hung Viet Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software vulnerability detection remains difficult because existing approaches rely on predefined analysis rules, learn vulnerability patterns implicitly from code and labels, or use large language models (LLMs) to make the final security judgment. It remains unclear whether structured descriptions of security-relevant program behavior can improve supervised detection.
We present VulnLens, an explanation-augmented framework for binary C/C++ vulnerability detection that separates program-behavior analysis from the final decision. A label-blind LLM-based Explainer examines each function from seven fixed perspectives: data flow, memory access, object lifetime, arithmetic and type behavior, control flow, shared state, and external-resource access. Without receiving vulnerability labels or CWE information, it generates structured explanations. A supervised Detector combines source code and explanations through sequential cross-attention.
We evaluate VulnLens on a PrimeVul-derived dataset covering ten CWE categories and test transfer to SecVulEval without retraining. On the 526-function PrimeVul test set, VulnLens achieves 75.5% accuracy and 77.2% F1, exceeding DeepSeek V4 Pro by 4.2 percentage points in accuracy and Gemini 2.5 Pro by 2.2 points in F1. Matched explanations improve F1 by 7.3 points over a separately trained code-only detector. On SecVulEval, VulnLens achieves 66.4% accuracy and 65.8% F1, outperforming DeepSeek V4 Pro by 7.6 points in accuracy and 20.0 points in F1, and Gemini 2.5 Pro by 16.6 points in accuracy and 7.8 points in F1.

---


### 25. [What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs](https://arxiv.org/abs/2610.37809)

**<font color=#1a73e8>作者：</font>** Michal Orzechowski, Rund Tawfiq, Tomasz Kosciolek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that answer questions over Web knowledge graphs are increasingly wrapped in checks derived from the graph's ontology, on the assumption that a formal schema makes a reliable judge. Yet a checker can be wrong as well: it can miss errors, and it can flag correct answers and push the agent into "fixing" them. Whether a curated ontology is worth its cost as such a judge, and how it compares with an ontology an LLM writes or a schema mined from the data, is unknown. We make the checker itself the object of study. Across curated, LLM-generated and data-derived ontologies, used as prompt context, as a checker, or both, and across open-weight and proprietary agents on public graphs and a private graph of nearly $10^{9}$ triples, we account for what ontology-derived checks catch and what they wrongly flag. We show how each source trades caught errors against false alarms, how a curated schema used as published can contradict its own data, which errors structural checks miss, and whether combining sources or giving the agent the checker's specific feedback pays off. On UniProt, the curated ontology flags more correct answers than either an ontology derived from the data or one an LLM derives from a summary of the data with masked identifiers. On real agent answers, its flags are only marginally more precise than random flags.

---


### 26. [DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers](https://arxiv.org/abs/2610.37826)

**<font color=#1a73e8>作者：</font>** Dingyi Kang, Bingzhe Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop questions, which require chaining facts spread across several documents through intermediate entities that the question never mentions. Graph-based RAG methods retrieve once from the entities a question names and so rarely recover the full evidence chain. Iterative RAG methods recover it step by step, but their accuracy is limited by the many tasks they ask the LLM to perform, such as planning the sub-questions, deciding their dependencies, rewriting them as answers arrive, and keeping track of what is known. We propose DeFT-RAG, a RAG framework built on three components. First, DeFT-RAG generates one self-contained sub-question at a time from the original question and the sub-questions answered so far with their answers (QA pairs). Each sub-question names every entity it asks about, which removes the need to plan, track dependencies or rewrite, and lets the LLM focus on a single fine-grained task at a time. Second, DeFT-RAG moves the remaining LLM work outside the LLM: rule-based updates to a QA table that keeps track of what is known, and yes/no decisions made by a fine-tuned lightweight decision model. Third, DeFT-RAG caches the QA pairs and reuses an answer when a later question asks a sub-question with the same meaning. On MuSiQue, 2WikiMultiHopQA and HotpotQA, DeFT-RAG achieves the best accuracy among thirteen baselines with both gpt-4o-mini and Qwen3.6 as the backbone, while giving the LLM fewer input tokens than any other iterative method. With a QA cache shared across 1,000 MuSiQue questions, 23.1% of sub-questions are answered from the cache, which reduces LLM calls by 12.9% without lowering accuracy.

---


### 27. [Improving Data-Constrained Scaling with Hyperparameter Transfer and Ensembling](https://arxiv.org/abs/2610.37842)

**<font color=#1a73e8>作者：</font>** Ethan Baron, Shmuel Berman, Anirudh Satheesh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As growing compute budgets outpace the growth of high-quality training data, large language models must be trained with both compute and data constraints in mind. Unfortunately, existing prescriptions for data-constrained scaling suffer from two important limitations. First, past works hold key hyperparameters such as weight decay fixed with scale, despite the fact that optimal hyperparameters vary wildly with model size and number of epochs. Second, past works neglect ensembling, a promising axis for scaling under data constraints. As a surprising consequence, prior prescriptions can lead to loss that increases with compute budget. We address both limitations by fitting power laws that prescribe how to transfer hyperparameters with scale and scaling laws that prescribe how to allocate compute with ensembling. Training on 100M tokens from FineWeb, our recipe reduces validation loss by over 0.15 nats compared to prior recipes, a 14% decrease in perplexity, and achieves monotonic improvements with compute through ensembling. These gains are achieved using prescriptions fit to smaller runs and validated at up to 12$\times$ larger compute budgets.

---


### 28. [Evaluating and improving AI agents for sequencing protocol understanding](https://arxiv.org/abs/2610.37851)

**<font color=#1a73e8>作者：</font>** Chi-Lam Poon, Michael Goneos, Zezheng Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing scientific-agent benchmarks rarely evaluate whether agents can reconstruct the exact molecular structures and generation workflows specified by sequencing protocols, a capability critical for analyzing customized sequencing assays. We introduce LibStructBench, a document-grounded benchmark for reconstructing sequencing-library structures and molecular workflows. Our experiments show that frontier agents often produce approximately correct reconstructions but remain unreliable at exact reconstruction, particularly in molecular-state representation and workflow connectivity. Switching the underlying language model produced larger average performance differences than switching agent harnesses, with a statistically significant difference only for molecular-state reconstruction. Additional knowledge improved oligo-family recovery in a small pilot without improving mean molecular-workflow scores. Autonomous accumulation of procedural rules and cross-protocol examples showed non-monotonic validation performance and no mean held-out molecular-workflow improvement in the tested trajectory. These findings highlight the need for more controlled and verifiable approaches to scientific reasoning about molecular processes in complex experimental protocols.

---


### 29. [Seq@K: Evaluating Language Models Under Sequential Feedback](https://arxiv.org/abs/2610.37859)

**<font color=#1a73e8>作者：</font>** Thomson Yen, Gilbert Yang, Naimeng Ye 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents differ fundamentally from prior intelligent systems in their ability to learn from natural language in context. This capability enables agents to iteratively refine their answers in response to feedback, a prevalent mode of operation in modern agentic workflows. However, the community primarily ranks models by metrics such as Pass@1 or Pass@K, which cannot capture how they utilize feedback on prior attempts. We introduce Seq@K, a natural evaluation protocol that measures whether a model can solve a problem within K sequential attempts, provided feedback after each previous failure. Unlike multi-turn agentic benchmarks that examine long-horizon planning, Seq@K isolates and formalizes the core capability of refinement from feedback. We evaluate Seq@K on a suite of 7 benchmarks and 16 frontier models, and show that Seq@K reveals a materially different model-selection landscape: under Seq@K, (1) model rankings often differ, (2) the Pareto frontiers admit more efficient configurations and (3) the gains from choosing the optimal model configuration can widen or shrink relative to those of Pass@K. We further show that analyzing model trajectories under Seq@K helps characterize iterative refinement behavior, such as the rate at which models address issues raised in feedback, or how rigidly they hold onto their own answers. Finally, we study how the nature of feedback affects models' iterative refinement, showing that practitioners must carefully design and benchmark the feedback loops of iterative agentic systems. Together, these results establish how Seq@K offers a more faithful metric for intelligent systems that typically operate in such feedback loop, and the necessity to consider Seq@K in evaluating models for these systems.

---


### 30. [Human-Residual Steering: Aligning Frozen LLM Judges with Human Judgment Distributions](https://arxiv.org/abs/2610.37868)

**<font color=#1a73e8>作者：</font>** Chen Lyu, Phong Do, Gabriele Pergola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used as automated judges, yet most alignment methods target aggregated human judgments and overlook variation among individual annotators. Existing approaches to matching the full distribution of human ratings mainly rely on output-level calibration or parameter fine-tuning. We propose Human-Residual Steering (HRS), to our knowledge the first method to align frozen LLM judges with human judgment distributions through learned hidden-state interventions. An oracle analysis shows that low-rank corrections at a single layer remove most of the discrepancy between judge and human distributions. HRS learns to predict such corrections from the judge's hidden representation and rating logits, training on individual annotations with proper scoring rules for ordinal and nominal judgments and optimising through the frozen downstream layers. Across 14 benchmarks and four judges from three model families, HRS outperforms all evaluated frozen-weight baselines. With Qwen2.5-7B, it achieves the lowest Jensen-Shannon distance on 13 of 14 benchmarks, reducing the mean from 0.565 to 0.352 versus 0.377 for the strongest calibrator. HRS also raises mean Spearman correlation with aggregate human scores from 0.449 to 0.579, improves population-level estimation under limited annotation budgets, and trains about 88 times fewer parameters than distributional fine-tuning at a modest cost in alignment.

---


### 31. [The Anatomy of Socio-Demographics in Pluralistic Offensiveness Modeling: When and Where It Helps, and the Role of Reasoning](https://arxiv.org/abs/2610.37896)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Leixin Zhang, Jinyi Mu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subjective judgments such as offensiveness often vary substantially across individuals, motivating pluralistic modeling approaches that incorporate annotators' socio-demographic information to capture this variation. However, prior findings on the benefits of socio-demographic information for pluralistic modeling are mixed, calling for a systematic analysis of both its effectiveness and the mechanisms through which it improves prediction. In this work, we study $\textbf{when}$ and $\textbf{where}$ socio-demographics benefit pluralistic offensiveness modeling, as well as $\textbf{the role of explicit reasoning}$ in leveraging this information. Across three multi-annotator datasets with prompted and trained LLMs, we first show that demographic gains are small and inconsistent for individual predictions but become clearer at the group and population levels, because aggregation attenuates the idiosyncratic variation that masks small but systematic demographic signals. Second, using a reasoning and prediction format that explicitly decomposes individual judgment into an overall baseline and a demographic-specific deviation, we show that the gains arise from both components: demographic information improves baseline estimation and enables meaningful demographic-specific shifts, and interventions show that better component estimates improve final predictions. Finally, comparing direct demographic conditioning with explicit reasoning about how the text interacts with annotator demographics, we find that reasoning yields more accurate baseline and shift estimates as well as final predictions, whereas conditioning alone rarely produces informative shifts. These results suggest that the mixed evidence in prior work may partly stem from individual-level evaluation, and that the value of socio-demographic information depends on both how it is evaluated and how models are guided to use it.

---


### 32. [Scan Before You Install: Detecting and Mitigating Local and Composite Vulnerabilities in Skills](https://arxiv.org/abs/2610.37901)

**<font color=#1a73e8>作者：</font>** Parth A. Gandhi, Avital Aviv, Prasanna N. Wudali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An agent skill packages natural-language instructions, scripts, and reference files that an LLM-based agent loads for a task. Skills may access the file system, shell, and network under user-authorized permissions; weaknesses can lead to unsafe execution. Existing scanners primarily target malicious skills, not unintended vulnerabilities in public repositories, and analyze skills in isolation, overlooking multi-skill interactions. To address these gaps, we developed a six-module scanner: Content Extraction, Local Analysis, Composite Analysis, Validation, Reporting, and Mitigation. Local Analysis detects unintended vulnerabilities in benign skills. On a 556-case leaderboard subset of SkillTrustBench, it achieved 95.90% recall with a 4.22% false positive rate; on a balanced sample of 1,000 MalSkillBench skills, its F1 was 0.947, outperforming Cisco's Skill Scanner, NVIDIA's SkillSpector, AgentSkillsScanner, and SkillSieve. In 1,587 skills from the 75 most-starred GitHub repositories, three analysts confirmed 53 of 59 findings (89.8% precision) across 23 repositories. We developed proof-of-concept (PoC) attacks for each vulnerability, disclosed 10 medium- and high-severity cases to maintainers, and tested mitigations on the remaining cases. Composite Analysis models dependencies among skills through shared resources, invocations, and instruction-mediated interactions. On SCR-Bench, its F1 score was 0.991 (98.7% precision, 99.6% recall), versus 0.816-0.858 for three SkillsGuard configurations released with CompoSkill. It identified two composite findings on GitHub, validated by PoC attacks. The Mitigation module recommends skill substitution, patches, and configuration changes. For 47 of 55 GitHub findings, mitigations prevented PoC attacks in all trials while preserving tested legitimate functionality.

---


### 33. [Think Twice: The Metis-1.6 Technical Report](https://arxiv.org/abs/2610.37903)

**<font color=#1a73e8>作者：</font>** Giulianno Vollmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Metis is a bet that better data, better training methods and new architectures can buy what a bigger parameter count cannot, at a fraction of the cost. Metis-1.6 is its latest step: two language models built from scratch by a single researcher, Praxis (2.94B parameters, 0.46B active per pass) and Logos (10.23B parameters, 1.18B active per pass). Both run a hybrid Mamba-2 and attention mixture-of-experts stack twice for every token, so each token gets a second look. Each was trained on 1.02T tokens in total: 804.76B of pretraining, 18B of context extension to 131,072 tokens, and 200B of supervised fine-tuning. Metis-1.6 was never meant to challenge frontier models, and across 40 post-trained benchmarks it mostly does not: Logos averages 52.93, seventh of 17 models in its comparison set and within a point of Qwen3-4B. But it gets there on roughly a twelfth of the median training data of the comparators that disclose it, and with fewer active parameters per token than any model that beats it, which puts it on the Pareto frontier for both. In mathematics it ranks second of 30 models, with 67.50% on AIME 2025 and 63.64% on HMMT February 2026. It is weak at code, instruction following and long context. The rest of the report is the part I found most valuable: what went wrong. The optimizer I configured never ran, and attention trained with AdamW for all of pretraining. A 1.77B-parameter n-gram memory learned to switch itself off. Five fine-tuning choices cost capability. And a length reward under group-mean normalization punished correct solutions for being long once a group's pass rate passed 2/3, a sign inversion I prove and fix with a one-line clamp. I close with the 10B-token ablations behind MoRE (Mixture of Recursive Experts), the looped architecture of Metis-1.7.

---


### 34. [FilingLoop: Evaluating and Evolving LLM Agents for Corporate Disclosure Review and Revision](https://arxiv.org/abs/2610.37905)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Yilei Zhao, Guangyan Gan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public disclosure repositories such as SEC EDGAR support informed investment through web access to corporate filings. Supporting their review with language model agents requires discovering unstated deficiencies across related documents, acquiring missing company facts, and verifying that requested revisions satisfy evidence-backed requirements. Existing financial question-answering evaluations provide limited evidence of these interactive capabilities. We introduce \textbf{FilingLoop}, an interactive benchmark and a self-evolving agent framework for corporate disclosure review and revision. Grounded in historical U.S.\ Securities and Exchange Commission correspondence, FilingLoop reconstructs 380 predominantly IPO review tasks from 96 companies under distinct information constraints. An evaluator separate from the acting agents scores final filings and responses against 6,099 eligible requirements and audits unsupported claims and harmful revisions. Our framework couples iterative review and revision within each case with procedural learning across cases, converting requirement-level evaluation feedback into role-specific guidance without updating model weights. Updates affect only subsequent cases, allowing procedural adaptation to be assessed without retrying scored tasks. On the evaluated stream, evolution increases requirement fulfillment from 24.28\% to 27.96\% and full comment resolution from 16.90\% to 20.75\%, with a 5.8\% increase in total cost over the fixed-policy variant. FilingLoop connects the concerns an agent discovers with the company facts it obtains and the revisions it commits, providing requirement-level feedback for procedures used in later review tasks.

---


### 35. [Muon Makes the First Mixture-of-Experts Layer Harder to Balance](https://arxiv.org/abs/2610.37914)

**<font color=#1a73e8>作者：</font>** Marcos Hernanz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many open mixture-of-experts (MoE) language models train with Muon instead of AdamW. Most balance the load with a bias on each expert's routing score, adjusted after every step. Their recipes disagree on whether Muon should also train the router. In models with 55M and 108M active parameters, we measure how the optimizer changes the span of these biases, the largest minus the smallest in a layer. The span grows when all tokens favor the same experts, so it shows how hard a layer is to balance. At learning rates tuned on shorter runs, Muon raised the span of the first MoE layer at every seed, roughly doubling it on average, while the other layers changed much less. The rise came from Muon on the rest of the network, whichever optimizer trained the router. In those runs, the inputs to the first router shared a direction, and soon after the warmup its busiest expert averaged four to seven times its fair share. Over the first 3,000 steps, subtracting the batch mean from these inputs removed this overload while barely changing the loss. On the smaller model, halving Muon's learning rate removed most of the rise and slightly improved the loss. Moving only the router to AdamW made the loads shift more during the warmup and slightly raised the loss, so at this scale the results favor keeping the router on Muon.

---


### 36. [SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World](https://arxiv.org/abs/2610.37919)

**<font color=#1a73e8>作者：</font>** Yusheng Zhao, Bowei He, Xue Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate empirical evidence from pretrained priors. We introduce SciGame, a controlled benchmark that converts scientific literature into structured scientific cards. Each card yields a pair of Original and dimensionally consistent Counterfactual environments with the same task interface. SciGame contains a Historical collection of canonical laws and a live Temporal collection curated from papers published after model knowledge cutoffs. It evaluates agents in candidate-guided Identification and open-ended Discovery settings. Each setting runs under Prior-only, Fixed, and Adaptive protocols. Experiments on five frontier models yield three findings. First, familiar priors hurt performance once the governing relation is altered. Second, adaptive experimentation helps the strongest models but harms weaker ones under limited budgets. Third, good explanations can hide quantitative failures. Recovering the exact symbolic form remains the main bottleneck, even when agents interpret evidence correctly. Current agents can investigate systems actively, but inducing exact laws in unfamiliar settings remains an open challenge.

---


### 37. [FAD-KV: Adaptive Dictionary KV Caching for Efficient Reasoning Decoding](https://arxiv.org/abs/2610.37921)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhu, David H. Yang, Parisa Shiravani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) caching is a core mechanism in large language models, where intermediate key and value representations are stored to accelerate autoregressive decoding. As generation length increases, KV cache memory and computation grow linearly, making compression critical for efficient long-output reasoning. Dictionary-based sparse KV compression is appealing because it represents each token's KV states as a sparse combination of learned basis elements (atoms) in a dictionary, preserving token-level structure without enforcing a global low-rank constraint. However, existing dictionary-based methods face two practical limitations during decoding: iterative sparse coding methods such as Orthogonal Matching Pursuit add decoding-time overhead, and static dictionaries may mismatch evolving KV distributions under test-time generation. While adaptive dictionary updates can reduce this mismatch, naive append-only strategies lead to dictionary growth during generation. We propose FAD-KV, a \textbf{F}ast \textbf{A}daptive \textbf{D}ictionary KV caching framework for efficient reasoning decoding. FAD-KV integrates (i) a screening-based sparse coding scheme, where a one-shot Top-\(n\) selection identifies a small candidate pool followed by lightweight coefficient refinement, and (ii) a fixed-size dictionary adaptation mechanism that reuses inactive atoms instead of expanding the dictionary. By controlling both sparse coding cost and adaptive dictionary growth, FAD-KV provides a memory-bounded and computation-efficient KV compression framework for long reasoning workloads. Experiments on reasoning and long-context benchmarks show that FAD-KV achieves a strong quality-efficiency trade-off while avoiding unbounded dictionary growth during decoding.

---


### 38. [VerifiedLab: Harnessing Knowns for Unknowns](https://arxiv.org/abs/2610.37923)

**<font color=#1a73e8>作者：</font>** Yu Yao, Jiayi Dong, Yang Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Across human history, knowledge has undergone several transitions, from orality to writing and then to digital archives. At each transition, humans established new conventions to preserve knowledge for the new era. Nowadays, as research agents are increasingly deployed for laboratory experiments, knowledge is crossing another boundary: from records written for humans to those for machines. In this work, we introduce VerifiedLab, a multi-agent harness framework for this human-to-machine transition of knowledge. VerifiedLab transforms research output from passive artifacts into active systems that accelerate downstream use, adoption and prediction of future trends. In VerifiedLab, a team of AI scientists with distinct roles reasons over records verified field by field: a principal investigator plans, a librarian computes the evidence directly from the records, specialists draft, and a gate and a critic check each claim against the measured reliability of its data before the harness decides whether to release or withhold it. We demonstrate the efficacy of VerifiedLab through extensive experiments on perovskite solar cells: VerifiedLab recovers known physical trends, anticipates devices reported a year later, and lets AI scientists inherit the literature together with a measure of how far it can be trusted. By scaling the inference-time verification compute, VerifiedLab introduces a new pathway for knowledge dissemination and machine harness for AI co-scientists.

---


### 39. [GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.37926)

**<font color=#1a73e8>作者：</font>** Dogan Urgun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning (MARL) enables teams of agents, such as robots and autonomous vehicles, to learn coordinated behavior, but what such teams learn is largely determined by their reward function. Because task success alone provides too little guidance for learning, intermediate rewards are usually designed by hand, and this effort must often be repeated whenever the environment or the team changes. Large language models (LLMs) can automate the effort by writing reward functions as code, yet the resulting rewards are typically designed and tested in a single setting. To enable their reuse across settings, GARDEN (Generalist Autonomous Reward Design through Evidence Navigation) is proposed, in which one reward program is developed for a family of related scenarios and transferred, unchanged, to scenarios that were not available during its design. During development, environment code, training records, and agent behavior are investigated by an LLM reward engineer, and draft rewards are tested in trial training runs, while the learning algorithm and the rule for selecting the final reward are held fixed. On unseen scenarios of the Overcooked and SMAX benchmarks, task returns were increased by 58.2% and 52.5% over the default rewards on two kitchen layouts, and the mean win rate in two combat scenarios was raised from 51.0% to 89.9%. Under matched candidate and probe budgets, this exceeded the 84.2% and 79.2% obtained with fixed diagnostic feedback and Eureka-inspired reward reflection. These results show that a single autonomously engineered reward can be reused effectively across related cooperative scenarios.

---


### 40. [Understanding Large Language Models as Numerical Optimizers](https://arxiv.org/abs/2610.37932)

**<font color=#1a73e8>作者：</font>** Lingyun Guo, Ali Bereyhi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have emerged as potential tools for numerical optimization. Despite promising results, their intrinsic optimization capabilities and limitations remain poorly understood, particularly in high dimensions. This paper investigates the ability of LLMs to exploit mathematical problem structures and generate feasible, near-optimal solutions. We develop an evaluation framework that distinguishes solution quality from execution failures, including numerical inaccuracies, constraint violations, and output-format errors. Using representative problems from convex optimization, fractional programming, and constrained projection, we assess LLM performance against deterministic reference solvers across different dimensions. Our results reveal that LLMs can capture useful optimization structures and produce near-optimal solutions, even when their outputs fail to satisfy numerical or formatting requirements. However, reliability deteriorates with increasing problem dimension and depends strongly on the underlying optimization structure. To further investigate the limitations, we deploy an iterative refinement mechanism that provides targeted feedback on feasibility and solution quality. The results demonstrate that iterative refinement substantially improves reliability and extends the range of problem dimensions over which LLMs produce valid solutions. Nevertheless, persistent numerical and structural errors limit their applicability as standalone optimizers. These findings provide insights into the capacity and limits of LLM-based optimization and motivate hybrid approaches that combine LLM reasoning with deterministic numerical verification.

---


### 41. [Bi-Phase Training: Learning Efficiently From Scratch](https://arxiv.org/abs/2610.37934)

**<font color=#1a73e8>作者：</font>** Abel Gurung, Joseph Campbell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training foundational models is computationally expensive as models scale. In this work, we introduce Bi-Phase Training (BPT), a parameter-efficient pre-training method that preserves the high-rank learning dynamics observed in full-parameter optimization with substantially reduced trainable parameters. BPT parameterizes each weight update as a composition of constrained high-rank left/right transformations via trainable diagonal matrices and low-rank adapters whose updates are periodically merged into the frozen base weights, resulting in a compounding expansion of accessible directions during training. Across language-model pre-training from scratch (Qwen2.5 models from 100M to 1.5B parameters and OLMo-2-1B) on FineWeb-Edu (10B and 100B tokens), BPT achieves validation perplexity close to full-parameter baselines while using far fewer trainable parameters; e.g., at the 1.5B scale, BPT uses 66% fewer trainable parameters with only a small validation-perplexity gap. Additionally, a comprehensive evaluation across diverse downstream tasks shows that BPT preserves much of the full-parameterized model's downstream performance.

---


### 42. [SkillMem: Compact External Skill Memory for Latent Multi-Agent Reasoning](https://arxiv.org/abs/2610.37935)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhu, Mohammad Mohammadi Amiri, Pin-Yu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent multi-agent systems reduce inference cost by keeping intermediate reasoning and inter-agent communication in continuous representations.\ Reusable skills, however, are commonly supplied as text or stored as layer-wise Key-Value states or skill-specific model parameters, introducing repeated processing or substantial per-skill storage.\ We introduce \textbf{SkillMem}, which represents each reusable skill as a small external latent memory and makes it directly available during latent multi-agent reasoning.\ A role-conditioned cross-attention reader allows the same memory to guide different agents according to their roles and current hidden states.\ We train the skill memories and shared reader through behavioral distillation, matching the change in token predictions induced by a textual skill while keeping the backbone frozen.\ For our experiments, we obtain textual skills from paired successful and failed multi-agent trajectories, although existing skills can also be compiled directly.\ Across six benchmarks and Qwen3 models ranging from 4B to 14B parameters, SkillMem provides strong gains for smaller backbones while preserving efficient latent multi-agent inference across model scales.\ We use the same $8\times256$ memory configuration across all evaluated model scales, requiring 9.6\,KB of skill-specific storage per skill, including its retrieval embedding.\ For a library of 100 skills, SkillMem reduces total storage by more than $38\times$ compared with alternative skill representations and achieves up to a $4.23\times$ end-to-end inference speedup.\ These results show that compact procedural memories can be reused without sacrificing the efficiency of latent multi-agent reasoning.

---


### 43. [Who Else Is In? Multi-Agent Collusion Initation Via Strategic Vagueness](https://arxiv.org/abs/2610.37984)

**<font color=#1a73e8>作者：</font>** Pramod Kaushik, Sarath Sivaprasad, Laura Ferrarotti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi agent LLM systems raise the risk of collusion among agents pursuing objectives hidden from their overseers. When potential partners identities are unknown, collusion first requires initiation: agents must discover one another, often through a public channel observed by ordinary agents and monitors. Strategic vagueness offers a way to navigate this mixed audience, conveying intent to a prospective partner while preserving a plausible ordinary interpretation. We introduce a mutual identification game in which two schemers must identify each other through public interaction, while jointly solving an ordinary task. We find that some models discover successful handshake strategies without explicit signalling guidance, using task compatible exchanges that monitors often fail to flag at low false positive rates. To characterize the communicative capabilities underlying these exchanges, we study a controlled coordination setting. We find an asymmetric response to message explicitness: as messages become more indirect, monitor punishment can fall faster than partner coordination, creating a profitable intermediate regime of strategic vagueness. Together, these findings illustrate a Blackstone style evidential asymmetry: communication sufficient for coordination between agents may remain insufficient for confident detection by monitor, opening a new surface of collusion.

---


### 44. [GAUSS: A Workload-Aware Analytical and Monte-Carlo Simulator for LLM Inference Serving](https://arxiv.org/abs/2610.37989)

**<font color=#1a73e8>作者：</font>** Srikant Bharadwaj, Ankur Mallick, Spyridon Mastorakis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference has become an operational workload that fleets must provision, monitor, and bill against latency service-level objectives (SLOs). A single throughput number cannot answer the questions operators actually face, because generative serving couples two phases with very different service characteristics, continuous batching reshapes the effective service process, and user-visible tail latency can degrade long before aggregate throughput saturates. We present GAUSS, a workload-aware analytical and Monte-Carlo simulator that predicts the full distributions of time-to-first-token (TTFT) and time-between-tokens (TBT), together with the sustainable request rate, for a given workload, engine, and accelerator. GAUSS pairs calibrated, phase-specific latency surfaces for prefill and decode with a Lindley-recurrence model of queueing under stochastic arrivals and estimates performance by ensemble Monte-Carlo sampling rather than by replaying a single trace. This lets GAUSS reason about workloads, routing policies, and hardware that have never been deployed, and to capture the latency tails that trace-driven simulators systematically under-sample. We describe the model and show how it supports operating-point selection, traffic segmentation, and shortest-remaining-processing-time scheduling capacity questions that trace-driven simulators cannot address.

---


### 45. [Preserving Safety During Sequential Fine-Tuning: A Factorial and Geometric Analysis of Replay](https://arxiv.org/abs/2610.38001)

**<font color=#1a73e8>作者：</font>** George Ruellan, Diana Benavides-Prado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benign fine-tuning can erode safety alignment in large language models, and sequential adaptation substantially compounds this risk. Prior work mitigates this erosion by replaying harmful-prompt refusals and benign-compliance examples, while other work instead matches base-model logits via distillation. However, the individual contributions of supervised exposure and distillation to safety behavior and refusal geometry during sequential adaptation remain unclear. We factor these two strategies apart and study their behavioral and geometric effects during sequential LoRA fine-tuning of Mistral-7B and Llama-3-8B across diverse task sequences (code generation, German-language summarization, and science question-answering). Behaviorally, supervised replay exposure yields the largest reduction in HarmBench attack success rate (ASR) on Mistral, averaging 51.1 points below base, but at a substantial over-refusal cost, averaging 53.4 points above base on OR-Bench-hard. Logit distillation, without any supervised replay loss, largely prevents safety erosion at a fraction of this cost: an average 5.4-point ASR reduction against only a 5.1-point rise in over-refusal. Llama shows the same asymmetry between the two strategies. Combining exposure and distillation moderates exposure's over-refusal while leaving downstream task scores largely unaffected. Geometrically, the two models diverge: on Mistral, distillation preserves the base refusal direction more closely than exposure does, whereas on Llama, refusal behavior after exposure largely survives ablation of the extracted refusal direction. This dissociation between models indicates that preserving the base refusal direction is not a reliable proxy for behavioral safety.

---


### 46. [Large Language Models for Accurate Medical Chart Abstraction: Enabling Scalable and Secure Artificial Intelligence Deployment in Stroke](https://arxiv.org/abs/2610.38009)

**<font color=#1a73e8>作者：</font>** Zhusi Zhong, Carl M. Porto, David Hong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical chart abstraction transforms unstructured clinical narratives into structured variables for research and quality monitoring. We evaluated a prompting-based large language model (LLM) framework for extracting eight clinical variables from 2,416 neurointerventional acute stroke intervention reports across three hospitals. Twenty-two instruction-tuned open-source LLMs were evaluated across architectures, model sizes, and biomedical adaptations using Quick Response and Chain-of-Thought (CoT) prompting. Non-expert staff annotations served as the cross-model reference standard. Evaluation was restricted to report-variable pairs with a valid LLaMA3.3-70B CoT prediction and a corresponding reference label. Performance measures included extraction accuracy, inference latency, and agreement with expert adjudication. Twenty discordant cases per variable underwent review by two senior physicians and four medical students. LLaMA3.3-70B achieved the highest overall accuracy (94.8%). CoT improved performance on inference-dependent variables such as site of occlusion, while Quick Response was optimal for directly stated procedural fields. Expert adjudication showed that AI predictions were more closely aligned with expert interpretations than non-expert annotations for most variables, with intracranial angioplasty remaining a challenge. Locally deployed LLMs can support scalable clinical information extraction and retrospective stroke registry curation, with expert oversight for ambiguous cases.

---


### 47. [Where Can We Fool the Model's Mind? Response-Guided Semantic Probing and Adaptive Routing for Transferable Attacks on Black-Box MLLMs](https://arxiv.org/abs/2610.38013)

**<font color=#1a73e8>作者：</font>** Ahmed Abdelnaby, Mohamed Elmahallawy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) ground language in visual evidence, yet their semantic reasoning can be exploited through transferable black-box adversarial attacks. Existing attacks typically allocate perturbations using surrogate-model saliency, which may not reflect how an unseen MLLM semantically interprets or relies on different image regions. We introduce VISTA (Vulnerability-Informed Semantic Transfer Attacks), a black-box framework that identifies semantically vulnerable visual regions from an MLLM's responses without access to gradients, logits, parameters, or internal representations. VISTA supports two attack settings: (i) VISTA-Proxy, a pure-transfer setting that probes an open-source MLLM and transfers the resulting adversarial examples to unseen commercial MLLMs without querying them; and (ii) VISTA-Victim, a query-assisted setting that probes the target MLLM to capture model-specific semantic vulnerabilities. VISTA builds an Uncertainty-Based Multimodal Behavior (UBMB) map from response drift, conflict, misleading, and semantic shifts, then uses entropy-adaptive Sinkhorn routing and a surrogate ensemble to focus perturbations on vulnerable regions. Across GPT-5, Gemini-3.5-Flash, and Claude Sonnet 4.6, VISTA achieves up to 97 % attack success rate (ASR) while maintaining a Peak Signal-to-Noise Ratio (PSNR) above 30 dB. Notably, VISTA-Proxy achieves up to 93 % ASR without querying the final victim, demonstrating that response-derived semantic vulnerability can enable effective transfer across heterogeneous MLLMs.

---


### 48. [Measured or Real? When Model-Derived Measurements Can Be Corrected or Compared](https://arxiv.org/abs/2610.38015)

**<font color=#1a73e8>作者：</font>** Yifeng Li, Ziang Ni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numbers computed from trained models, such as an example's difficulty or a model's benchmark lead, change with seed and prompt. We ask when such measurements can be corrected or compared. Noise shrinks correlations, and the textbook correction divides by the square root of two estimated reliabilities. On two CIFAR-100 difficulty scores, it returned correlations above one in 70 of 100 classes. We prove that its mean squared error is infinite even when the correlation and the reliabilities use separate seeds. Our rule corrects only when both reliabilities pass a significance test, then divides by their upper confidence bounds. Its output is always bounded, and its coverage guarantees assume Gaussian noise. It helps once reliability is well estimated, more than halving the error with 500 simulated units. Prompt settings can reverse rankings. On ARC, Qwen2-1.5B trails Llama-3.2-3B by 3.8 points with no examples in the prompt and leads by 16.6 with two. Across four benchmarks, averaging the two settings names one winner for 15 of 16 such reversals. We compare models within each setting, controlling family-wise error asymptotically in the number of items for a fixed prompt grid. Aligning embedding coordinates across seeds raises held-out per-dimension reliability from 0.003 to 0.813.

---


### 49. [Assessing Language Models for Scientific Applications: Inertial Confinement Fusion as a Use Case](https://arxiv.org/abs/2610.38024)

**<font color=#1a73e8>作者：</font>** P. B. Radha, D. D. Meyerhofer, M. Bhattarai 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advancing language models for specialized scientific applications requires evaluations of scientific fluency, physical reasoning, and quantitative analyses. Using inertial confinement fusion (ICF) as a test case, we have developed an expert-curated benchmark of 250 questions spanning qualitative reasoning, numerical calculation, symbolic derivation, and equation formulation. Responses have been evaluated using deterministic numerical and symbolic checks together with language-model judges. We compared a variety of out-of-the-box closed-source and open-source large language models with Prospero, a model specialized through combined domain-adaptive pretraining and supervised fine-tuning for ICF. We also conducted initial retrieval-assisted evaluations. Prospero improved its aggregate score by 10.7 percentage points over its base model, with gains across all question types. Frontier models achieved the highest aggregate scores, but critical physics errors persisted, particularly in numerical calculations. We note that domain-specific performance can improve through specialization, but benchmark gains alone do not establish scientific reliability. Retrieval improved performance for a smaller model but yielded no statistically significant improvement for a frontier model. Two scientific stress tests further illustrate useful capabilities and the need for expert assessment of physical assumptions and model validity. Based on these findings, we recommend evaluating existing domain capabilities and retrieval benefits before committing to substantial additional specialization.

---


### 50. [CARF: Context-Aware Reasoning Supervision for Scientific Evidence Screening](https://arxiv.org/abs/2610.38041)

**<font color=#1a73e8>作者：</font>** Nishtha Agarwal, Adam Visokay, Astha Wahi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic reviews synthesize biomedical evidence to inform clinical and public-health decision-making, but require domain experts to manually screen thousands of studies against detailed eligibility criteria. We investigate whether language models can assist with this bottleneck by learning from expert feedback on title and abstract screening decisions and model-generated reasoning. We introduce the Context-Aware Reasoning Framework (CARF), a human-in-the-loop framework that uses expert feedback on model-generated reasoning to adapt language models to context-dependent screening tasks. We evaluate CARF on systematic reviews of verbal autopsy and cause-of-death ascertainment methods used in global public health mortality surveillance. CARF shows competitive screening performance compared to evaluated models while retaining high sensitivity, and is more inclined to retain ambiguous, context-dependent studies for human review. Together, these findings suggest that expert-corrected reasoning is a promising supervision signal for context-dependent scientific screening, while retaining a role for human oversight.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
