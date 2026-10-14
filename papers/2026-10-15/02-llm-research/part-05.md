# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 201. [CodeWalk: Generating Coding Benchmarks by Walking a Problem Graph](https://arxiv.org/abs/2610.15345)

**<font color=#1a73e8>作者：</font>** Jiaxin Fang, Runyuan He, Arnav Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-quality coding problems are expensive to collect. Benchmarks such as SWE-bench rely on substantial human curation, while synthetic alternatives typically rely on costly model generation and validation. In this work, we show that new coding problems can be created at almost no cost by composing existing ones. We formulate problem generation as code composition: verified atomic problems are combined into level-$N$ tasks, and a task is kept only if every atomic problem remains unsolved and a joint reference solution passes the same check used at evaluation time. The entire task-construction process is programmatic and requires no language-model generation or validation. We instantiate this approach in four coding settings: multi-bug repair, proof completion, complexity analysis, and clone equivalence. The generated tasks are challenging for frontier models, which all degrade as compositional depth increases. The generated tasks are also useful as training data: rejection-sampling fine-tuning on them improves Qwen3.5-9B at every composition level.

---


### 202. [TRACE: Temporal Risk Assessment and Concept Editing for Safer Language Generation](https://arxiv.org/abs/2610.15365)

**<font color=#1a73e8>作者：</font>** Ankur Garg, Xuemin Yu, Hassan Sajjad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can produce harmful content while generating a response. A useful safeguard should not only detect this risk during generation but also intervene while leaving safe responses largely unchanged and provide an auditable record of the internal patterns supporting its decisions. We propose TRACE (Temporal Risk Assessment and Concept Editing), a framework that tracks harmful-response risk during generation, selectively edits token activations, and leaves an auditable trace of its detection and steering decisions. TRACE learns a codebook of recurring activation patterns, with each codebook vector representing a latent concept. At inference time, it assigns each token activation to the nearest codebook vector to obtain the corresponding concept. A gated recurrent unit (GRU) processes the activations and their assigned concept features to predict completed-response harmfulness and a monotone cumulative streaming risk. During steering, activations assigned to harmful concepts are steered along directions defined by nearby benign targets. An external LLM labels the learned concepts post hoc, making detection sequences and harmful-to-benign edit records interpretable. Experiments across three generators and the WildGuard and S-Eval benchmarks show that TRACE improves streaming F1 over Kelp in five of six comparisons while remaining competitive on completed-response detection. TRACE's selective steering reduces Harmbench attack success with little change in refusal on originally safe responses. The post-hoc audit reveals recurring semantic structure in the learned concepts and distinct traces associated with harmful detection, safe generation, and activation edits.

---


### 203. [ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs](https://arxiv.org/abs/2610.15368)

**<font color=#1a73e8>作者：</font>** Yi Ge, Kangrui Ruan, Jifan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. However, most existing coding agents never look ahead: their policies do not anticipate the consequences of actions, and the terminal reward barely attributes a failure to certain earlier steps, so an ill-judged edit can corrupt the repository state irreversibly before any signal arrives. Recent code world models aim to address these challenges, but they are either trained and then frozen before reinforcement learning (RL), or reduced to an auxiliary next-token loss on the environment's outputs. We present ANTE (Anticipate, Then Execute), an agentic RL framework that verifies the policy's pre-action predictions by real execution and turns them into per-step credit for its actions and trust-or-abstain decisions. With an internal belief stated before each action, Belief-Anchored Policy Optimization (BAPO) turns the settled predictions into per-step advantages by anchoring credit on the policy's own forecasts. To turn the trained forecasts into better actions at inference, thereby facilitating effective test-time scaling, ANTE-TTO (test-time optimization) selects among candidate actions without an external scorer. ANTE raises Qwen3-32B from 25.0% to 57.2% pass@1 on SWE-bench Verified, 6.2% above a matched GRPO baseline trained without the belief state; its world model's accuracy climbs from 44% to 69% during RL, and the learned foresight capability transfers across harnesses and out-of-distribution domains. In summary, we aim to build a code world model that knows what has happened, what holds now, and what the next action will achieve.

---


### 204. [A Sovereign, Indic-First, Reasoning Model](https://arxiv.org/abs/2610.15371)

**<font color=#1a73e8>作者：</font>** Sutanshu Saksena Raj, Prasanjith Pasunuti, Parijat Chatterjee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gnani-Evon-v3.3-30B-A3B is a long-context hybrid Mamba-Transformer mixture-of-experts model for reasoning, instruction following, and tool use in English and eight Indian languages. Starting from NVIDIA's Nemotron-3-Nano-30B-A3B checkpoint, it retains the 52-layer backbone and changes the vocabulary, training data, and post-training objectives. An in-place expansion from 131,072 to 163,072 tokens reduces mean Indian-language fertility by 38.6%. The new embedding rows are initialized from their upstream decompositions and warmed before the backbone is updated. Continual pretraining then adds broad English-Indic data, high-quality annealing, and direct training at a 131,072-token sequence length.
The central result appears after post-training. Reinforcement learning across four verifiable task environments improves mathematics, graduate-level science, and instruction following, but degrades Indic extractive question answering because the rewards do not require an answer in the requested language. The share of Indic extraction items answered in English rises from 8.7% to 91.7%. Accuracy conditional on answering in the target script roughly doubles, which is consistent with preserved reading ability but is measured on a self-selected subset.
Two unreleased studies test repairs. A scoped Indic reward restores the language convention. A 26B-A4B generative judge outperforms a 235B-parameter model on RM-Bench, and distillation restores 81% of the capabilities displaced by optimizing against it.
Relative to the architecture-identical starting checkpoint, the released model gains 5.2 points on an Indic aggregate while giving up 1.7 points of English retention. The unreleased Indic-aware branch trades further, gaining 14.6 Indic points at a cost of 5.4 in English. A planned FP8 release reduces the artifact to 32GB with near-zero mean change across 32 paired benchmarks.

---


### 205. [Fewer Bits, More Tries: Recovering Capability Under Memory Constraints](https://arxiv.org/abs/2610.15372)

**<font color=#1a73e8>作者：</font>** Tomer Galanti, Josh Susskind, Eran Malach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are generally more capable than smaller ones, but their memory requirements can make local deployment difficult. We ask whether part of this capability gap can instead be recovered by running a smaller or more compressed model multiple times and selecting among its outputs using public or model-generated tests. Single-user local inference can leave hardware underutilized, allowing parallel candidate generation to trade additional test-time computation for accuracy at modest latency cost. Across four code-generation benchmarks, verified retry recovers substantial accuracy lost to model size or compression. A 7B Qwen model with eight parallel attempts essentially matches a 32B model on MBPP+ and exceeds it on the other three benchmarks, while using about $4\times$ less model memory, running up to $6\times$ faster, and using less energy, as measured on Nvidia GPU. We observe similar tradeoff across model sizes, compression levels and hardware choices, although exact benefit depends on the hardware profile and problem setting. These results show that model capacity can be traded for verified test-time computation when correct solutions remain reachable within a modest retry budget.

---


### 206. [In-Place Indic Tokenizer Expansion and Continual Pretraining of Nemotron-3-Nano-30B-A3B](https://arxiv.org/abs/2610.15373)

**<font color=#1a73e8>作者：</font>** Avinash Benki, Prasanjith Pasunuti, Sutanshu Saksena Raj 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We adapted Nemotron-3-Nano-30B-A3B for eight Indian languages without changing its backbone architecture. We expanded the vocabulary in place from 131,072 to 163,072 entries using continued byte-pair encoding and AdaptMix rebalancing, reducing tokens per word by 38.6%. We initialized new input and output rows by averaging their original constituent rows, then trained them on 90% Indic and 10% English text before updating the backbone. Continual pretraining then progressed through broad training, high-quality annealing, and long-context training over approximately 1.27 trillion tokens. The annealed checkpoint gained 12.9 points on the Indic MILU benchmark but lost 3.4 on English MMLU. We also report practical negative results. Direct token addition underperformed continued byte-pair encoding. AdamW weight decay changed rows intended to stay fixed. Perplexity on an Indic-heavy holdout did not select the learning rate that best preserved English performance.

---


### 207. [E8 Lattice Key Quantization for Low-Bit KV-Cache Compression](https://arxiv.org/abs/2610.15384)

**<font color=#1a73e8>作者：</font>** Sasho Nedelkoski, Alexander Acker, Soeren Becker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compressing the key-value (KV) cache is essential for serving long-context large language models (LLMs) under memory constraints. While current scalar quantization methods achieve significant compression, they typically face a quality-fidelity trade-off, either suffering from performance instability at 2-bit precision or necessitating 3-bit keys to maintain model quality. In this work, we demonstrate that a uniform low-bit k2v2 configuration (2-bit keys and 2-bit values) can preserve near-baseline quality by using vector quantization (VQ) based on the $E_8$ lattice for KV keys. We show that structured VQ exploits correlations across adjacent dimensions to achieve signal-to-quantization-noise ratios (SQNR) higher than those of independent scalar quantization at the same key payload rate. To ensure practical utility, we adapt a table-based asymmetric scoring algorithm that avoids explicit codebook dequantization during attention computation and preserves decode-throughput parity with scalar baselines. Across five LLM families, our $E_8$ k2v2 approach yields \textasciitilde$6\times$ KV compression, roughly 20\% smaller than scalar k3v2 (3-bit keys and 2-bit values), while retaining near-baseline long-context perplexity. In our full-suite perplexity evaluation, $E_8$ improves over scalar k3v2 in 80\% of model--dataset--context settings. These results indicate that $E_8$ lattice VQ improves quality per byte while keeping throughput at parity, suggesting that structured key quantization is a useful primitive for KV-compression stacks. Overall, our work provides a low-overhead primitive for expanding the quality-memory frontier in long-context LLM inference.

---


### 208. [VideoEvoHarness: Self Evolving Agent Harness from Unlabeled Videos for Video Understanding](https://arxiv.org/abs/2610.15389)

**<font color=#1a73e8>作者：</font>** Weixin Xu, Yifan Liu, Yi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding agents rely on a harness to acquire evidence, use tools, and reason, but improving it requires substantial effort. Recent self evolution methods seek to optimize harnesses through execution feedback to reduce human intervention. However, existing methods often rely on annotated video questions and answers or focus on updating model parameters, leaving harness evolution from unlabeled videos underexplored. VideoEvoHarness jointly evolves a Questioner and a Solver harness from unlabeled videos with frozen model parameters. The Questioner constructs questions and computes reference answers directly from video memory records. Question quality assessments and Solver execution trajectories guide question generation policy revisions. The Solver supports evolving skills, strategies, hyperparameters, and tools using execution feedback. Executable strategies define workflows in code, reducing repeated interpretation of natural language instructions. Each round, candidate harnesses are compared on identical validation questions, with validated improvements retained for later use. Experiments on benchmarks and a dedicated benchmark question set, using videos disjoint from evolution videos, show higher overall accuracy than initially and transfer gains across backbones. Overall accuracy on this set also improves progressively across rounds. This supports our foundational framework for harness evolution from unlabeled videos, opening a promising direction for self evolving video agents. Code is available at this https URL.

---


### 209. [From Acoustic Sensing to Physical Actions: A Comprehensive Survey of Security Risks in Edge-Deployed Audio LLM-Based Agents](https://arxiv.org/abs/2610.15390)

**<font color=#1a73e8>作者：</font>** Binhong Wang, Haidong Kang, Yanfeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Audio Large Language Models (Audio LLMs) are embedded in agents for smart homes, vehicles, wearables, and embodied systems, where acoustic inputs can propagate from perception into persistent state and consequential execution. This setting extends security analysis beyond model behavior to the system conditions that determine how acoustic inputs can influence agent behavior and external actions. Existing surveys examine acoustic security, LLM-based agents, and edge deployment in isolation, leaving their security interactions in deployed Audio LLM-based agents insufficiently characterized. This survey introduces an Acoustic Sensing-to-Action (S2A) system model that traces these security implications along the path from acoustic sensing to external execution, while accounting for edge-cloud runtime and lifecycle transformation. We use the model to synthesize attacks, defenses, and evaluation methods across the acoustic, agent, and edge-system literature. The synthesis shows that security gaps can emerge within components and at the transitions between stages, where protections developed for one stage do not necessarily provide end-to-end assurance in the deployed system. These findings motivate security evaluation that follows acoustic influence from sensing to action across persistent state, system boundaries, and changing deployment conditions in real-world agents.

---


### 210. [WUSPruner: Second-Moment-Optimal Transforms for Structured Pruning](https://arxiv.org/abs/2610.15394)

**<font color=#1a73e8>作者：</font>** Shengkun Tang, Dan Alistarh, Zhiqiang Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning is typically formulated as identifying which model dimensions to remove, often within the model's original representation. However, the effect of coordinate deletion fundamentally depends on the basis in which pruning is performed. This raises a more fundamental question: how should the basis be chosen specifically for coordinate deletion? We introduce WUSPruner, a transform-based framework for structured pruning of large language models. We formulate basis selection as a local linear reconstruction problem that directly minimizes the reconstruction loss induced by pruning. Inspired by the second-moment transformation in WUSH, we consider a WUS transform constructed jointly from activation and weight statistics. We show that under positive-definite second moments, WUS transform minimizes the local reconstruction loss over all invertible changes of basis. In the resulting basis, the activation and weight second moments are simultaneously diagonalized and balanced, causing the deletion error to decompose into independent spectral contributions and yielding a principled criterion for coordinate selection. Guided by this result, we develop a scalable pruning method based on blockwise WUS transformations and compact input projections. Experiments on Llama and Qwen models from 8B to 72B parameters show consistent improvements over structured pruning baselines across language modeling, knowledge, commonsense reasoning, mathematics, and code generation benchmarks, while also delivering practical reductions in inference latency and memory usage.

---


### 211. [Training-Data Extraction from Genomic Language Models](https://arxiv.org/abs/2610.15396)

**<font color=#1a73e8>作者：</font>** Tianhao Mao, Zihao Wang, Dongfang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Genomic language models generate long nucleotide continuations from short prefixes, exposing a direct route for studying training-sequence extraction through the generation interface. We present an output-only black-box attack on Evo 2 that selects convergent groups of repeated generations without gradients, token likelihoods, or training-corpus access during candidate selection. Recovered content is then scored by an evaluator combining aligned length, nucleotide identity, match multiplicity, and sequence complexity. Across 304 runs on Evo 2 7B with bacteriophage and plasmid prefixes, the attack yields 888 candidate clusters, of which 85 match training segments of at least 500 bp, giving a cluster-level attack success rate of 9.57%. Final filtering retains 22 uniquely matched extraction events at the 500-bp threshold and 15 at 1,000 bp, covering 14 and 7 distinct training-sequence regions, respectively. Within-category source-homology screening retains 11 of the 22 events at a 99% exclusion threshold and four at 98%, with the latter mapping to two reference regions. The results establish convergence among repeated nucleotide generations as a practical output-only signal for recovering long training-sequence segments and characterize how recovery depends on prefix length, cluster size, perplexity, early stopping, and sequence domains.

---


### 212. [GA-SVD: Generation-aware Singular Value Decomposition for LLM Compression](https://arxiv.org/abs/2610.15398)

**<font color=#1a73e8>作者：</font>** Shengkun Tang, Cong Zeng, Zongfang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong generalization across a broad range of reasoning and generation tasks, but their large parameter counts impose substantial memory and computation costs, hindering deployment in practical resource-constrained settings. One-shot low-rank compression is a promising solution since it reduces model size and inference cost effectively. However, existing SVD-based methods primarily target multiple-choice benchmarks and often fail to preserve performance on generation tasks. Moreover, their rank allocation strategies are typically heuristic. We propose GA-SVD, a generation-aware low-rank compression framework for LLMs. First, we introduce Generation-Aware Weight Whitening (GAWW), which leverages gradients from on-policy knowledge distillation to construct whitening transformations aligned with generative behavior. Second, we develop an evolutionary global rank allocation method that searches for effective layer-wise rank allocation under a given global compression ratio. Across extensive experiments on Mistral-7B, Qwen3 series, and Llama-3.3 models, evaluated on both multiple-choice and generative benchmarks, GA-SVD consistently outperforms existing SVD-based baselines and achieves state-of-the-art (SoTA) results. We further demonstrate scalability by applying our method to models with up to 70B parameters.

---


### 213. [Harnessing VLM in Embodied RL: From Reward Regressor to Success Detector via Exploration-Augmented Key-Observation Gating](https://arxiv.org/abs/2610.15401)

**<font color=#1a73e8>作者：</font>** Xin Liu, Yutong Jiang, Jian Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> VLMs provide promising solutions to embodied reward design. Most current methods that train VLMs as reward regressors not only require extensive annotations but are also primarily designed for finetuning pretrained policies, and perform less well in the more challenging from-scratch RL setting. This issue stems from a fundamental mismatch: regressing precise rewards is misaligned with what VLMs naturally excel at. We posit that it is more aligned with VLMs' inherent multi-modal VQA capabilities for the models to function as success detectors, and propose VLM success reward via Exploration-Augmented Key-Observation Gating (VLMeg) to well harness VLM for embodied reward design. As the core of VLMeg, the proposed exploration-augmented key-observation gating first determines whether the current RL episode is judgment-worthy based on its similarity to a generated success trajectory. Then, the key observation with the lowest confusion from the judgment-worthy episode will be selected for VLM evaluation as episodic reward. This gating mechanism not only avoids redundant calls but also enables higher detection accuracy of VLM. Considering the sparsity of judgment-worthy episodes, the advanced exploration incentives based on the generated trajectory are introduced, enabling more efficient exploration toward judgment-worthy trajectories for more VLM reward triggers and thus gaining higher RL efficiency. Extensive experiments in MetaWorld demonstrate VLMeg achieves state-of-the-art from-scratch RL, outperforming advanced VLM-based baselines on 12 challenging reward-free tasks. Furthermore, VLMeg also enables effective RL without any ground-truth reward in 3 challenging real-world experiments. Code will be open after acceptance at this https URL.

---


### 214. [A Decade of PhotoMappers: A Longitudinal Study of Crowdsourced Disaster Photos Geolocalization with Vision-Language Models and Geospatial Reasoning](https://arxiv.org/abs/2610.15403)

**<font color=#1a73e8>作者：</font>** Hao Li, Wenping Yin, Fabian Deuser 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Crowdsourced disaster imagery provides timely, ground-level observations when conventional disaster mapping is delayed or incomplete, yet its geographic value depends on where observations are produced, how they are interpreted, and whether they can be reliably located as actionable Geospatial Intelligence (GEOINT). Using more than a decade of PhotoMappers, a crowdsourced disaster-mapping initiative, this study examines the changing geography of disaster information and asks how emerging GeoAI models compare with human geographic interpretation. We combine longitudinal spatial analysis with cross-view geolocalization using street view imagery (SVI) and remote sensing imagery (RSI), and evaluate vision-language models (VLMs) reasoning through 30 indicators spanning geographic cues and reasoning evidence. The results reveal a geographically and temporally uneven archive shaped by changing disaster types, Community Lifelines, and operational priorities. Integrating VGI, SVI, and RSI with Sinkhorn re-ranking achieves 40.90% R@1, 61.10% R@5, and 69.45% R@10, while yearly R@1 varies markedly from 25.00% to 65.07%. Geographic reasoning is similarly uneven: Qwen3.6-27B achieves an overall agreement of 67% compared with 51% for InternVL3-8B, with both models showing greater difficulty with localized and place-specific evidence than broad spatial configurations. We argue that the value of GeoAI lies less in replacing volunteered geographic interpretation than in complementing it, scaling candidate retrieval while retaining human judgment for ambiguous and consequential cases. This provides a pathway toward more human-centered and responsible GeoAI for disaster mapping. All data and code are openly available at this https URL.

---


### 215. [State Representation Shapes Long-Horizon Agent Learning and Transfer: An Empirical Study](https://arxiv.org/abs/2610.15407)

**<font color=#1a73e8>作者：</font>** Dong Nie, Rui Lan, Yixin Nie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An end-to-end success rate alone cannot distinguish failure to learn an action from failure to apply it as task state changes. We study this distinction in deterministic tool workflows that provide the current artifact state and candidate action recipes. Using 1.7B, 8B, and 27B Qwen models, we compare supervised learning across workflow horizons and cross the state representation used for training with the one used at evaluation. Horizon-matched supervision yields high completion, but an H4-trained 1.7B model transfers poorly to longer workflows under full-state observations. In an H16 crossover, compact-trained 1.7B adapters complete 50/50 held-out tasks in compact view and 0/50 in full view for each of three paired training seeds; full-trained outcomes vary across seeds. A separate 8B adapter pair shows a similar asymmetry. The view dependence also appears in paired-choice tasks where both candidate calls are executable and the correct choice depends on table contents; here, the compact mask does not consult the target action. An explicit relevance cue improves full-view execution but does not close the gap for the tested checkpoint. In a separate 27B ScienceWorld study, compact-state training improves local accuracy under both views, indicating that the transfer pattern depends on the task and observation construction. Together, these experiments identify representation-sensitive transfer as a bottleneck in the controlled workflows, without isolating content reduction from other changes to the observation.

---


### 216. [From Candidate Tokens to Final Outcomes: Decoding Relative Long-Horizon Candidate Value from Reasoning Model Representations](https://arxiv.org/abs/2610.15412)

**<font color=#1a73e8>作者：</font>** Yixin Yang, Yue Wang, Fandong Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models generate reasoning trajectories token by token. At a given prefix, multiple next-token candidates may be plausible, yet shape subsequent reasoning and differ in their chances of leading to the correct answer. Whether these differences are reflected in internal representations remains unclear. To study this question, we define relative long-horizon candidate value to quantify within-prefix differences and construct the Reasoning Candidate-Token Value (RCTV) dataset, pairing mathematical reasoning prefixes with plausible next-token candidates and their empirical long-horizon candidate values. Using RCTV, we examine hidden states, multilayer perceptron outputs, and attention outputs at candidate positions with sparse linear probes. Experimental results provide evidence that relative long-horizon candidate value is linearly decodable from these representations at multiple layers. Candidate-value probes can also outperform probability- and embedding-based baselines. Furthermore, a controlled online intervention experiment shows that using the decoded signals to guide token selection during generation can improve the chances of eventual success. Our findings provide evidence that internal representations encode information about relative long-horizon candidate value, offering insights into how local candidate-level representations relate to long-horizon reasoning outcomes.

---


### 217. [Sensitivity or Criterion? Measuring and Moving When Language Models Act](https://arxiv.org/abs/2610.15415)

**<font color=#1a73e8>作者：</font>** Sixun Dong, Yebowen Hu, Ming Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Before an agent acts, it must decide whether action is warranted. A single accuracy cannot distinguish failure to recognize a warranted action from reluctance to act. Signal-detection theory separates sensitivity from criterion, but criteria estimated from authored binary labels depend on each benchmark's example mix. We introduce FlipAct, a diagnostic of tool use in physical states. A rule over annotated tool properties computes each answer and a graded evidence score, fixing the Yes/No boundary at zero across models. Questions form 2-by-2 quads that hold required knowledge fixed while the state flips. The slope of the fitted Yes-rate curve measures sensitivity; its crossing at one half measures criterion. Across 44 open models, sensitivity rises with size within a family, and its ranking agrees with three of four external when-to-act benchmarks. Models respond to evidence sign rather than magnitude, accepting actions that leave the state no better about as often as helpful ones. When Yes means act, most models are conservative across rephrasings; in some, this partly reflects a preference for No. Criterion is not determined by size. Activation steering shifts criterion with weights fixed; distillation from a model's own steered copy puts the shift into its weights without a significant sensitivity change. The distilled shift transfers to six external benchmarks, including two without Yes/No answers, while criterion-free AUC is preserved on the five benchmarks where it is available. Accuracy improves where models start conservative and declines or remains within error where they start permissive. Project page: this https URL

---


### 218. [SpecFit: Not All Draft Tokens Cost the Same in Offloaded MoE Inference](https://arxiv.org/abs/2610.15417)

**<font color=#1a73e8>作者：</font>** Hongliang Cao, Xiuyu Li, Siqi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models activate only a few experts per token, but when their expert weights are offloaded to host memory, host-to-device (H2D) expert transfers enter the critical path of decoding. Speculative decoding verifies several draft tokens in one forward pass, yet in an MoE model each verified token activates its own experts, so a larger draft tree transfers more experts. Because of this H2D cost, speculative decoding commits several tokens per verification cycle yet is sometimes even slower than autoregressive decoding. Based on this observation, we propose SpecFit, which chooses the verified draft subtree to maximize predicted throughput rather than acceptance length. SpecFit estimates the expected number of committed tokens from draft path probabilities and predicts cycle time from the node count and the per-layer union of the experts the subtree activates; this union is a monotone submodular coverage function, so each node pays only for the experts it adds. An exact search over ancestor-closed subtrees returns the subtree with the highest predicted throughput; run after each draft level, the same search also decides when to stop drafting, and the unmodified target verifies the result. On CNN/DailyMail summarization and a GSM8K subset with Qwen3-30B-A3B, SpecFit decodes 21.6% and 7.0% faster than EAGLE-3 with the same expert cache and 1.97x and 1.72x as fast as vanilla EAGLE-3. Code is available at this https URL.

---


### 219. [Riemannian Graph Tokenizer for Structural Knowledge Transfer](https://arxiv.org/abs/2610.15427)

**<font color=#1a73e8>作者：</font>** Qimin Zhou, Haibo Liu, Yujie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are at the forefront of artificial intelligence. A tokenizer, converting the raw input into discrete representations that the model can understand, plays an important role to the success of foundation models. Unlike the text tokenizer that is well studied in large language models, graph tokenizer is still at its early stage, facing the challenges of tackling the non-Euclidean structures and capturing the structural semantics. How to design a graph tokenizer for structural knowledge transfer? To this end, we propose a Riemannian Graph Tokenizer (RGT) that bridges the structural knowledge and quantized representations to support cross-domain structural knowledge transfer. The connection is established by Riemannian geometry. Specifically, we first define the geometric vocabulary (trees, cycles and sequences), which captures fundamental structural patterns and reflects the intrinsic geometry of graph. Second, we construct a Riemannian quantizer with Riemannian Straight-Through Estimator to tokenise graph structures across multiple domains into discrete tokens. To ensure consistency and transferability across diverse geometric spaces, RGT further incorporates a geometry-aligned decoder that projects manifold-specific tokens into a unified tangent space. The theoretical analysis and geometric interpretations are provided to support the effectiveness of our proposed method. Extensive experiments across diverse datasets demonstrate that RGT significantly enhances structural knowledge transferability across graph domains.

---


### 220. [AuthScribe: Supporting Agency and Authorship in LLM-Assisted Reflective Journaling](https://arxiv.org/abs/2610.15439)

**<font color=#1a73e8>作者：</font>** Lanping Hu, Yinsi Zhou, Zhenchang Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in reflective journaling, where articulating an experience is part of interpreting it. This raises questions about how writers retain authorship, exercise agency, and assess personalized assistance. We present AuthScribe, an LLM-assisted reflective journaling system that combines contextual anchors, writer-steered AI support, Autobiographical Citations, and read-only Provisional Drafts that require re-expression before AI-generated suggestions enter the journal. Retrieval and LLM inference run on-device. In a 14-day field deployment with 14 participants, grounding shifted from situating current experiences to reconnecting them with prior self-authored interpretations. Perceived agency remained stable through Week 1 and shifted during Week 2. Participants described authorship through transforming AI-generated suggestions into personally meaningful expression, and trusted personalized prompts when they could trace them to prior writing. We discuss design implications for adoption friction, longitudinal agency, and traceable personalization in AI systems for personal reflection.

---


### 221. [Hidden in Plain Sight: Advancing Harmful Content Understanding via Perception-Aware Adversarial Self-Play](https://arxiv.org/abs/2610.15449)

**<font color=#1a73e8>作者：</font>** Yisong Xiao, Benlei Cui, Shiji Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in language understanding, Large Language Models (LLMs) can still miss meaning hidden in plain sight, failing to identify harmful intent in expressions readily understood by humans. Malicious users exploit this gap by strategically disguising harmful content to evade automated moderation, posing a serious threat to online platform safety. The vulnerability reflects a fundamental cognitive asymmetry between human readers, who integrate contextual, phonetic, and visual cues to decipher the intent behind deliberate obfuscation, and text-based LLMs, which rely primarily on token sequences and have limited exposure to evolving evasions. To bridge this asymmetry, we propose PASP (Perception-Aware Adversarial Self-Play), which combines multi-perceptual views with adversarial self-play to improve understanding of harmful intent as evasions evolve. Specifically, PASP constructs textual, phonetic, and visual views of each input, preserving its original context while exposing pronunciation and glyph cues obscured in token space. During adversarial self-play, an attacker uses defender feedback to generate intent-preserving evasions, while the defender is trained using an intent-invariance reward to understand harmful intent across changing surface forms. Extensive experiments show that PASP reduces adaptive attack success rates by up to 73.71% and 74.49% on ChineseHarm-Bench and EvoHarmBench, respectively, preserves model capabilities with minimal degradation, and effectively interprets real-world evasive expressions in e-commerce.

---


### 222. [MemeLogos: Knowledge-Driven Retrieval-Augmented Reasoning for Harmful Meme Detection](https://arxiv.org/abs/2610.15463)

**<font color=#1a73e8>作者：</font>** Hexiang Gu, Saihui Hou, Changlan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid proliferation of social media, harmful memes have become a growing threat to online ecosystems. Their harmfulness is often implicitly conveyed through complex interactions among visual, textual, and contextual cues, making accurate detection challenging. Recent studies have introduced Retrieval-Augmented Generation (RAG) and external knowledge into harmful meme detection. However, existing methods mainly retrieve similar instances or auxiliary information, limiting their ability to capture reusable harmfulness knowledge and underlying reasoning mechanisms, and thus constraining both detection performance and interpretability. To address these challenges, we propose MemeLogos, a knowledge-driven retrieval-augmented reasoning framework for harmful meme detection. MemeLogos abstracts recurring harmfulness patterns and reasoning structures from diverse harmful cases into reusable knowledge units and organizes them into a dedicated star-shaped knowledge graph. By combining structured knowledge retrieval with an explicit multi-stage reasoning process inspired by cognitive mechanisms, MemeLogos leverages retrieved knowledge to guide harmfulness reasoning, improving both detection reliability and interpretability. Extensive experiments show that MemeLogos consistently outperforms existing harmful meme detection methods while generating more coherent and interpretable reasoning, demonstrating the effectiveness of structured harmfulness knowledge for multimodal content understanding.

---


### 223. [Semantic Saliency from Multi-Modal Large Language Model Scene Understanding Maps](https://arxiv.org/abs/2610.15467)

**<font color=#1a73e8>作者：</font>** Ziqi Wen, Shravan Murlidaran, Jonathan Skaza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-computable low-level image saliency has shaped perceptual psychology and computer science, but is limited by its inability to capture human high-level cognitive factors that influence attention and eye movements. Here, we propose a new fully automated method to compute semantic saliency by quantifying each object's contribution to scene comprehension without fitting any parameters to human data: the Automated Scene Understanding Map (AUTO-SUM). AUTO-SUM automatically segments and removes individual objects from a scene, uses multimodal large language models (MLLMs) to describe the original and modified scenes, and measures the semantic similarity between these descriptions using text embeddings. We show that AUTO-SUM can predict which object is most important in a human-measured scene understanding map (H-SUM) estimated using human scene descriptions. We also show that AUTO-SUM can predict the object most fixated by human observers during free viewing and scene description tasks better than a low-level saliency model (GBVS, Itti-Koch), a saliency model trained based on human meaning ratings (Meaning Map), and comparable to DeepGaze, which is trained on human fixation data. We contend that AUTO-SUM can be used as a semantic saliency model that complements lower-level saliency models. Code are available at this https URL .

---


### 224. [SkillFusion: Towards Reliable Multi-Skill Composition for LLM Agents](https://arxiv.org/abs/2610.15481)

**<font color=#1a73e8>作者：</font>** Enhao Huang, Xinye Zhao, Yiming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Independently authored skills can impose incompatible requirements, competing preferences, and redundant instructions when jointly loaded by an LLM agent. We propose SkillFusion, an offline compiler that reconciles these interactions into a reusable merged skill. Its central idea is to make composition decisions explicit through typed, scoped constraints linked to their source directives. A type-scope gate selects candidate interactions, while selective fallback revisits pairs potentially missed by structural pruning. A classifier identifies interaction types, and an adversarial verifier re-examines uncertain judgments. The resolver applies conditional routing or explicit priorities to hard conflicts, verified abstraction to soft conflicts, and deduplication to redundant instructions. Source-linked checks guide synthesis and compression, and metadata synthesis supports discovery of the merged skill. The resulting artifact retains associated scripts and resources and can be reused across tasks and executor models. SkillFusion achieves the highest mean Success among evaluated non-oracle methods on all three agent benchmarks and on both transfer benchmarks across three executor models. At the largest tested instruction configurations, it achieves over 2.5 times the Success of unresolved multi-skill loading, highlighting the growing value of reconciliation as composition becomes more demanding. The code will be open-sourced after the review process concludes.

---


### 225. [Security in LLM-Assisted Coding: A Systematic Literature Review](https://arxiv.org/abs/2610.15482)

**<font color=#1a73e8>作者：</font>** Liang Yuan, Maryam Khanian Najafabadi, Mashud Rana 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models accelerate software development but introduce severe security vulnerabilities. This systematic review investigates security risks in automated coding, benchmark limitations, and the role of human developers. Findings indicate that models frequently generate insecure code and faulty patches due to training data biases. Additionally, the models themselves are susceptible to direct attacks. Current evaluation methods suffer from data contamination and lack robust security metrics. Consequently, human oversight remains essential. Safer integration of automation will require more security-aware model architectures, stronger security-specific benchmarks, and more effective human-AI collaboration frameworks to mitigate these systemic risks.

---


### 226. [AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning](https://arxiv.org/abs/2610.15488)

**<font color=#1a73e8>作者：</font>** Peiqi Jiang, Fan Zhang, Xin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formulaic alpha mining seeks interpretable expressions that rank assets by future returns. The task is challenging because it demands simultaneous processing of unstructured market descriptions, historical data, and quantitative evaluation of candidate factors, yet most existing methods exploit only a subset of these signals. We introduce AlphaPilot, a reinforcement-learning framework that trains multi-turn tool-using LLM agents for adaptive alpha mining. The agent conditions on market descriptions, proposes factor expressions, queries real-data evaluator feedback, and updates a retained factor pool across turns. This design jointly leverages market text, LLM financial knowledge, real data, and evaluation feedback. At inference time, AlphaPilot performs day-by-day search and pool updates to adapt to shifting market regimes. Across three independent runs in out-of-sample rolling backtests on CSI300 and CSI500, AlphaPilot achieves mean total returns of 42.93% and 54.19%, with mean Sharpe ratios of 2.46 and 2.86, respectively. It attains the highest mean total return, Sharpe, and RankIC among the evaluated methods on both universes.

---


### 227. [When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization](https://arxiv.org/abs/2610.15492)

**<font color=#1a73e8>作者：</font>** Haomiao Qiu, Yining Tang, Hongyi Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill internalization aims to convert externally specified procedural skills into persistent model capabilities, allowing language-model agents to execute them without retrieving or reinjecting skill descriptions at inference time. Yet when new skills are learned continually, whether previously internalized skills remain usable is still poorly understood. We study forgetting in continual skill internalization and uncover a clear hierarchical structure. Early in subsequent training, a model may lose the ability to invoke an old skill from the raw request, while supplying only the correct canonical skill name substantially restores the learned behavior; with further optimization, this conditional execution also degrades. We call these two stages skill-addressing forgetting and skill-execution forgetting. Guided by this finding, we introduce Factorized Skill Memory (FSM), which separates continual skill memory into a plastic Address Memory and a stable Execution Memory. At each stage, FSM trains a new LoRA executor using only current-stage data, freezes it after acquisition, and appends it to Execution Memory; in parallel, Address Memory incrementally learns to map current requests to executors without replaying historical requests or execution trajectories. At inference time, Address Memory selects one executor from the raw request, and only that frozen executor performs a single language-model generation. On a five-stage benchmark built from 100 TaskBench skills, FSM achieves 65.95% mean exact match and 93.38% addressing accuracy across two task orders, improving over the strongest replay-free parameter-isolation baseline by 14.3 percentage points while remaining within 1.9 points of Replay, which retains historical training examples.

---


### 228. [Large Decision Models: Repurposing Large Language Models as Single-Pass Decision Makers](https://arxiv.org/abs/2610.15501)

**<font color=#1a73e8>作者：</font>** Ziyi Chen, Yan Zhang, Jianhui Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models make decisions through parallel prefill and sequential decoding. Although effective, this approach incurs decoding costs and does not explicitly expose decision probabilities. Existing task-specific classifiers require per-task training and offer limited generalization to unseen decision schemas. We propose Large Decision Models (LDMs), repurposing language models to return explicit probabilities over labels specified at run time using one prefill forward pass. We first adapt models to this interface through Diverse Decision Supervision (DDS), covering varied domains, rules and labels. To further narrow the performance gap to a reasoning model, Self-Posed Reasoning Distillation (SPRD) adds tasks generated by a frozen teacher, filters them for answer consistency, and trains on label distributions obtained from repeated teacher reasoning. We evaluate on DecisionVista, pairing new-schema tests with held-out human-labelled sources. Across three base models, the recipe improves accuracy over a step-matched baseline by 1.8 and 1.5 percentage points, respectively, achieving a 182-fold speedup in latency over reasoning rollout on Gemma-4-31B. Reasoning remains stronger on the new-schema test, motivating a confidence router for uncertain decisions. On development sets, routing recovers a median 92% of reasoning's accuracy advantage while generating 27-58% of its tokens. Code is available at this https URL.

---


### 229. [SARATHI: Decoupled Data-Free Probing and Adaptive Reconstruction for Structured LLM Pruning](https://arxiv.org/abs/2610.15514)

**<font color=#1a73e8>作者：</font>** Sankar Behera, Dhruv Singh, Satyadev Ahlawat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning reduces the inference cost of large language models (LLMs) by permanently removing neurons and weight rows, yielding dense, hardware-agnostic speedup. Existing post-training methods couple neuron selection and weight reconstruction through a shared calibration dataset, introducing domain bias and out-of-memory failures at high sparsity. We propose SARATHI, a framework that decouples these two stages. A data-free \emph{NMF Residual Subspace Probe} scores neurons using intrinsic weight geometry, without accessing any calibration data, and carries a formal connection to Robust PCA. \emph{Adaptive OBS} then reconstructs the pruned weights with a localized calibration batch, operating in $\mathcal{O}(d^2)$ peak memory per layer and eliminating the global memory bottleneck of coupled methods. A \emph{Bias Shift Compensation} step corrects systematic activation drift in post-LayerNorm architectures that would otherwise cause perplexity collapse at high sparsity. Experiments across six models from two architecture families (gated and non-gated FFN) at 15--40\% sparsity show that SARATHI achieves competitive perplexity and matches or exceeds existing structured pruning baselines on zero-shot accuracy.

---


### 230. [A Step in the Right Place: Understanding and Optimizing Timestep Placement in Continuous Diffusion Language Models](https://arxiv.org/abs/2610.15527)

**<font color=#1a73e8>作者：</font>** Shutian Zheng, Zhihong Yu, Linye Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models represent an emerging paradigm for language modeling. They generate text in parallel by iteratively refining continuous representations and mapping them back to tokens through a decoder. However, realizing the efficiency advantage of parallel generation requires maintaining generation quality with only a few denoising steps. Even when the number of steps is fixed, their placement along the denoising trajectory remains flexible. In this paper, we demonstrate that changing timestep placement alone can substantially alter the final latent representations and thereby affect the decoded token distributions. Building on these findings, we introduce StepTune, an algorithm that searches for timestep placements that improve generation quality. The search is conducted on a small calibration set and guided by a language-aware objective, with the model and sampling budget fixed. Once calibrated, the timestep placement is fixed and reused across inputs. Experiments demonstrate consistent improvements in unconditional generation perplexity and conditional task metrics across all evaluated sampling budgets. In particular, StepTune enables 16-step sampling with a frozen model to outperform its native 64-step baseline on both XSum summarization and WMT14 translation and reduces end-to-end latency by approximately $3.8\times$. These results establish timestep placement as a practical means of improving the quality-efficiency trade-off in continuous diffusion language models.

---


### 231. [Agent-Canary-Mas: End-to-End Evaluation of Protocol Risk in Long-Horizon Multi-Agent Systems](https://arxiv.org/abs/2610.15529)

**<font color=#1a73e8>作者：</font>** Xiuming Liu, Le Gai, Zhiyuan Chang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-to-agent protocols allow LLM agents to discover peers, exchange results, and coordinate tool use. A locally successful protocol attack, however, may be rejected by a later agent or propagated into a consequential task decision. Measuring local exploitability alone leaves this difference unresolved and provides limited evidence about which participant caused the final outcome.
We present Agent-Canary-Mas, an end-to-end evaluation system that follows protocol risk through long-horizon multi-agent tasks. It covers five risk classes and 13 subclasses across A2A, ANP, and BCS, with 975 matched malicious--benign task pairs in five business domains. A shared OpenClaw framework runs autonomous, tool-using agents under different underlying models while preserving the task and execution setup. Matched runs separate local protocol success from downstream consequences; retained evidence connects participant selection, message consumption, tool activity, and task-state changes. We further evaluate a protocol-context Guard that checks an object's authority at consequential handoffs.
Across three model conditions, local attack success is frequently at or above 90%, while consequence conversion ranges from 7.1\% to 100.0\%. Cross-agent evidence raises macro-averaged Audit-F1 from 29.7% to 95.5%. On Finance tasks, the Guard lowers average ASR from 86.1% to 53.8% and PTCR from 65.5% to 31.2%, with a measurable completion tradeoff. These results show that protocol risk depends on how agents use exchanged objects throughout the task, and that evaluating this path supports more informative risk assessment, attribution, and defense.

---


### 232. [Apertus 1.5: From Open Text Models to Open Multimodal Reasoners](https://arxiv.org/abs/2610.15542)

**<font color=#1a73e8>作者：</font>** Project Apertus, Yixuan Xu, Yassine Turki 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are becoming infrastructure, and infrastructure built in the open, by public institutions, on documented data, is the alternative to dependence on a few providers; Apertus shows this is viable at scale. Apertus 1.5 extends the fully open Apertus family from text to multimodal reasoning. Continued pretraining of the Apertus 1.0 models, on 4T additional tokens for the 8B and 2T for the 70B, adds image and audio understanding and extends the context window fourfold to 262,144 tokens; multimodality enters through the tokenizer, the language-model head remains restricted to text, and the architecture is unchanged. Supervised finetuning, long-context finetuning, reinforcement learning with verifiable rewards, and preference alignment complete the released models. Thinking is a flag of the chat template rather than a separate model, and lifts mathematical reasoning by up to 20 points on the 8B model. The released models improve over their predecessors on nearly every benchmark; among fully open models of its class, the 8B leads on knowledge, instruction following, and cultural benchmarks, and its instruction following surpasses all compared models, including open-weight ones. On image and audio understanding, a first for the family, the models are competitive with fully open multimodal models, strongest on document understanding and long-form and lower-resource speech recognition, while specialized vision and audio models remain ahead on perception and transcription of English and other high-resource languages. As in Apertus 1.0, we train only on openly available data, respect crawler opt-outs retroactively, and exclude restrictively licensed material. We release the model weights, data preparation and training recipes, and evaluation suites under permissive licenses; openness extends to values, with the Apertus charter guiding alignment stages published alongside the models.

---


### 233. [Genesis: Visual Augmentation Primitives for Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2610.15565)

**<font color=#1a73e8>作者：</font>** Fan Yang, Lifeng Chen, Yipu Wang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models achieve promising results on visual reasoning tasks, approaching human-level performance on existing STEM benchmarks. However, these capabilities degrade under complex real-world scenes. We identify that chain-of-thought reasoning remains largely confined to the linguistic space, rarely anchoring each step in visual evidence. The main cause is the absence of such data during training. In this work, we introduce a training data augmentation pipeline, \textbf{Visual Augmentation Primitives} (VAP), which leverages state-of-the-art vision generative models to synthesize diverse photorealistic training samples and corresponding reasoning text. VAP introduces some basic operators and applies them to a seed image and gets a variant. It also constructs coherent multimodal reasoning chains throughout the generation process. Such training data force models to perceive visual content and perform logical reasoning according to them at every step. We further introduce multimodal chain-of-thought rubric-based reinforcement learning to enhance this. It rewards not only text reasoning but also visual reasoning by scoring intermediate reasoning steps for logical validity, completeness, and consistency. Moreover, we construct the UNREAL benchmark to systematically evaluate visual reasoning on hyperrealistic scenes across controllable difficulty levels. Experiments show that a 4B model built on this framework surpasses 8B baselines, with performance improving consistently as the model scales to 32B, validating the scaling law for visual reasoning.

---


### 234. [The Fragility and Dynamics of LLM Pruning-Recovery Steps](https://arxiv.org/abs/2610.15574)

**<font color=#1a73e8>作者：</font>** Luis Frentzen Salim, Komang Rinartha, Chia-Chun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structural pruning followed by a recovery stage is the standard recipe for compressing large language models (LLMs), yet the two stages are typically designed and tuned in isolation. In this work, we study how their interaction shapes the compressed model, sweeping ordering, the data that drives each stage, and the alignment of their training objectives. We find that instruction-following is the first capability to collapse under pruning, well before knowledge, reasoning, or core language modeling, and that much of the pruning in-domain loss is likely not knowledge loss but a domain-agnostic failure to respond coherently to the prompt. We find in our setting that in-domain data is the strongest pruning signal, whereas instruction-style data recovers the most. Stage order matters little, but only marginally. We further analyze how the importance ranking drifts before and after pruning. Together these results give practitioners a concrete recipe for composing pruning and recovery.

---


### 235. [Towards Robust Calibration Dataset for Domain-General Mixture of Experts Pruning](https://arxiv.org/abs/2610.15578)

**<font color=#1a73e8>作者：</font>** Luis Frentzen Salim, Chia-Chun Wu, Tran Van Nhiem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training expert pruning is a promising deployment technique for Mixture-of-Experts (MoE) models. The calibration set is an integral part of the pruning process, however, its correlation with evaluation performance is largely misunderstood and unintuitive. In this work, we present an empirical study of the robustness of calibration perturbations, specifically in MoE models. Showing how calibration size, language, and data distribution affect layer-wise expert pruning for gpt-oss-20b. Our findings reveal that (1) domain-general pruning quality receives minimal benefit from scaling calibration data beyond small sample sizes, (2) cross-lingual calibration transfers effectively, with English-only calibration maintaining strong performance across seven languages of varying typologies and scripts, and (3) a diverse calibration data resembling the pretraining distribution can yield comparable or superior performance to test-distribution data. Ultimately, we provide practical insights as a recipe for better understanding calibration for more effective domain-general expert pruning.

---


### 236. [From Stages to States: Unified Iterative Reasoning for MLLMs](https://arxiv.org/abs/2610.15620)

**<font color=#1a73e8>作者：</font>** Chuang Yu, Xuefei Ma, Yuanhao Feng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Chain-of-Thought (MCoT) substantially enhances the complex reasoning capabilities of Multimodal Large Language Models (MLLMs) by explicitly modeling intermediate reasoning processes. However, most learning-based MCoT methods follow a stage-centric paradigm, where different reasoning behaviors are assigned to predefined stages and optimized separately. This results in fragmented reasoning and a training-inference reasoning-state gap. To address these limitations, we propose ReState, a unified iterative reasoning framework that reformulates multimodal reasoning from a stage-driven pipeline into a state-driven dynamic process. It comprises two complementary components: Unified Reasoning State Modeling (URSM) and Closed-Loop Reasoning-State Learning (CRSL). URSM unifies reasoning construction, correct reasoning preservation, and erroneous reasoning correction as reasoning-state transitions within a shared state space, enabling these heterogeneous reasoning behaviors to be learned jointly. CRSL further incorporates self-generated historical reasoning states during training and recursively updates the current state during inference, thereby mitigating the reasoning-state gap and enabling iterative self-refinement without requiring an additional reflection module, critic, or independent correction stage. Furthermore, we construct VersaCoT-10K, a high-quality CoT dataset spanning eight visual reasoning domains, which provides diverse supervision for multi-domain reasoning and reasoning-state refinement. Extensive experiments demonstrate that ReState exhibits strong adaptability across different MLLM backbones and achieves strong performance on multiple public reasoning benchmarks, supporting the shift from stage-centric reasoning toward state-centric reasoning. Our data and code are available at this https URL

---


### 237. [The Price of Precision: A Calibrated Cost Model for Mixed-Precision LLM Serving](https://arxiv.org/abs/2610.15629)

**<font color=#1a73e8>作者：</font>** Mukund Athmaram, Manoj Rao, Liang Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing a mixed-precision configuration for large language model (LLM) serving trades speed against accuracy. Allocators that use average bit-width or a memory budget as a speed proxy can miss changes in the resource that limits execution. We argue that served speed can be limited by compute, weight loading, or key-value (KV) cache access, depending on the phase, batch size, and context length. A byte-based proxy does not capture all of these costs, so fewer bits do not always mean faster serving. To address this gap, we build a cost model that accounts for the binding resource and use it in two ways. First, as a predictor: given a configuration and operating point, it estimates serving latency using constants calibrated for the model, GPU, and serving stack. We evaluate its accuracy across three hardware classes. Second, as an allocator: we combine modeled time costs with measured per-tensor accuracy costs and use a dynamic program to select a configuration under a latency or accuracy budget. We compare its configurations against byte-aware and sensitivity-only allocation.

---


### 238. [Big-Big-SycoBench: A Benchmark to Detect Sycophancy Through Model Responses to Valid vs. Invalid Arguments](https://arxiv.org/abs/2610.15634)

**<font color=#1a73e8>作者：</font>** Marthe Ballon, Arne Vanhoyweghen, Seorin Kim 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sycophancy in large language models risks amplifying unsupported claims or beliefs across the knowledge ecosystem as these systems increasingly contribute to research synthesis, evaluation, and decision-making. A reliable model should revise its judgement when a user identifies a genuine flaw, but should resist pushback based on fallacies, emotion, or irrelevant appeals to authority. While sycophancy is usually measured on questions with a verifiable answer, the evaluative tasks in which it is most difficult to detect have no such ground truth. We introduce Big-Big-SycoBench, which measures sycophancy through argument discernment: the ability to revise an evaluation after valid criticism while resisting invalid pressure. The benchmark consists of 450 text artefacts with 5,400 arguments for raising or lowering their quality scores, each reviewed by one or more of twelve human annotators. An LLM scores each artefact twenty times to establish its baseline score and uncertainty. The model is then given a valid or invalid argument and asked to update its score. We only count a revision if it exceeds the model's own baseline variability. We use the resulting score delta to distinguish responsiveness to valid arguments from compliance with invalid ones. Across ten models, responsiveness is 88-95\% for seven, 76-77\% for Kimi K3 and GLM-5.3, and 32\% for Opus 5.5. Compliance ranges from 0.2\% for GPT-6 Astra to 95\% for GPT-4o. Big-Big-SycoBench is intended to guide the development of models whose judgements can be corrected by sound arguments, but not displaced by unsupported pressure.

---


### 239. [Context-Aware Precision Scheduling for Small Language Models](https://arxiv.org/abs/2610.15640)

**<font color=#1a73e8>作者：</font>** Mukund Athmaram, Manoj Rao, Liang Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) used as on-device agents must balance accuracy and latency as their context grows. Mixed precision helps manage this tradeoff by assigning different precisions to weight tensors according to their size and sensitivity. However, these choices depend on the operating conditions, so a configuration selected for a short context may no longer provide the best tradeoff at a longer one. We calibrate a timing model from measurements at different precisions and context lengths, and combine it with tensor sensitivities to choose configurations under a latency or accuracy budget. We argue that fewer bits do not always mean faster execution, so our predictor estimates latency from calibrated execution costs rather than weight bytes alone. Under a latency budget, reading the larger key-value (KV) cache leaves less time for weight operations, leading the allocator to select lower precisions. This gives a schedule of tensor changes that can be prepared before execution. Our runtime follows the schedule while retaining the session's KV cache. We evaluate executed schedules on a laptop GPU, including a longer-context schedule with three weight formats and a tool-use benchmark measuring full response time and correctness. Under an accuracy budget, measured error from a quantized KV cache determines the budget left for weights. The allocator can raise or lower weight precision as this estimate changes. These experiments show where context-aware precision helps and where accuracy recovery remains limited.

---


### 240. [Recall What Is Missing: Composing Evidence from Long-Term Agent Memory](https://arxiv.org/abs/2610.15642)

**<font color=#1a73e8>作者：</font>** Qi Feng, Jicong Fan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under a limited context budget, a long-term agent must recall not merely memories that are individually relevant, but evidence that is collectively sufficient for the current query. Conventional memory access retrieves, scores, and truncates memories, often spending multiple context slots on redundant facts while leaving complementary evidence behind. We cast the read phase of long-term memory as query-conditioned evidence composition: each memory is valued by what it adds beyond the evidence already selected. We instantiate this operation with MemPursuit, a training-free mechanism that uses the residual of a sparse convex query reconstruction as a representation-space proxy for what the current memory set is missing. By reusing the query and candidate embeddings already available from retrieval, MemPursuit progressively composes nested evidence contexts without invoking a language model or cross-encoder to score each query--memory pair. The effectiveness of our method is verified on 3 popular benchmarks in comparison to strong baselines. In fixed-budget LoCoMo experiments, MemPursuit improves end-to-end accuracy by 7.2 percentage points at Top-10 and 5.5 percentage points at Top-20, with consistent gains across multiple memory frameworks, while achieving a 32.9$\times$ speedup in median reranking latency over fully batched BGE-v2-m3. Our implementation is available at this https URL.

---


### 241. [Feedback as an Interface: Controlling Form and Detail in LLM Translation Refinement](https://arxiv.org/abs/2610.15661)

**<font color=#1a73e8>作者：</font>** Yiqi Liu, Flavjo Tomori, Nafise Sadat Moosavi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Feedback presentation shapes how LLMs use evaluator judgments during translation refinement. We introduce a machine translation protocol that keeps the evaluator score, main issue, and recommendation fixed while varying feedback form and supporting detail. Across seven models and six translation directions, low-load feedback outperforms high-load feedback in all 42 translator-direction settings under xCOMET. On the 29,400-record rewriting subset, mean xCOMET scores multiplied by 100 are 83.30 for low-load feedback and 80.67 for high-load feedback; the full-matrix original-translation reference mean is 83.46. MetricX-24 supports the low-load advantage on a stratified subset. A no-feedback second pass yields a small improvement over the original translations, and direct evaluator prompting reproduces the low-load advantage without a separate rewriting stage. These results show that compact feedback limits the quality loss from evaluator-guided refinement in the evaluated high-resource MT settings.

---


### 242. [A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding](https://arxiv.org/abs/2610.15666)

**<font color=#1a73e8>作者：</font>** Abdollah Pourasghari, Saeedeh Sadat Sadidpour, Mohammad Roustaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-grounded environments, and largely assume instructions are clear and executable. We introduce the first Persian vision-language-action dataset for this task: 258 instances over 230 real household/office photographs, annotated with reference plans, deliberate ambiguity and infeasibility labels, disambiguating question-answer pairs, and an auto-generated chain-of-thought rationale for training. Using this resource, we ablate retrieval-augmentation, chain-of-thought prompting, and an agentic disambiguation step, evaluated with an LLM-as-judge protocol and a new metric, PGOS-FA, extending prior work (PG2S) with step-order sensitivity, an over-generation penalty, and Persian-adapted embeddings. Paired statistical testing across 36 comparisons shows retrieval-augmentation is a large, robustly significant effect, while finer-grained additions are directionally consistent but not statistically distinguishable from noise at this scale, and the LLM-judge metric has near-zero power where PGOS-FA succeeds. A blind human-correlation study on 79 real outputs shows PGOS-FA tracks human judgment at least as closely as the LLM-judge. Testing generalization beyond the ablation's single backbone, we find that most of the gap between an open-weight and a substantially stronger closed planner is attributable to open-weight model generation rather than to the closed model's capability specifically, and that our best configuration significantly outperforms an independently reproduced external baseline despite a weaker backbone. The dataset, PGOS-FA implementation, and evaluation code will be made available upon reasonable request.

---


### 243. [Rate-Resolved Text Evaluation with Masked Diffusion Language Models](https://arxiv.org/abs/2610.15667)

**<font color=#1a73e8>作者：</font>** Yiqi Liu, Kun Zhao, Chenghua Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A single evaluation score can rank generation systems but rarely reveals what failed. We propose rate-resolved text evaluation, which turns the masking rate of masked diffusion language models into a diagnostic axis. By reconstructing text under different fractions of masked tokens, one diffusion score becomes a vector of band-conditioned scores that reflect reconstruction difficulty at varying levels of visible context. On SummEval, preserving this rate structure yields complementary signal: the best masking-rate band improves fusion with autoregressive likelihood over a collapsed diffusion scalar, survives a sample-shuffle control that breaks rate ordering, and adds residual signal to a fixed prompted judge. A second diffusion model reproduces the effect more weakly. On WMT MQM zh-en, roundtrip mask-and-reconstruct probing produces a tunable localization curve in which ranking-oriented AUROC and span-detection F1 peak at different masking rates. Factuality benchmarks bound the interpretation: band semantics are model- and task-dependent, so each application requires empirical validation.

---


### 244. [Knowledge Interaction in Hypernetwork-based Continual Learning: Conflict and Composition](https://arxiv.org/abs/2610.15677)

**<font color=#1a73e8>作者：</font>** Jiaqi Zheng, Yi Hu, Yadong Mu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual learning aims to adapt pretrained large language models (LLMs) to evolving data while preserving their pretrained capabilities. A central challenge is catastrophic forgetting: adaptation to new data can impair performance on previously learned knowledge. Since continual learning commonly changes model parameters, the model's predictions may draw on knowledge from the base model, the parameter update, and the input context. Understanding how these sources interact is essential: conflicts reveal whether new knowledge can override outdated knowledge, while multi-hop reasoning tests whether new knowledge can be composed with existing knowledge to support generalization. We study these interactions in a hypernetwork-based adaptation framework, where a shared network generates adapters from context, allowing a frozen base model to adapt without task-specific updates. We find that, under knowledge conflict, models preferentially follow the context, and their choices depend more on where knowledge is presented than on its content. We also show that context and adapter knowledge perturb the base model's representations along directions orthogonal to its clean hidden states, enabling us to derive steering vectors that control which source the model follows. In multi-hop reasoning, we find that models fail to reliably compose knowledge across the three sources, with the key breakdown arising from the interaction of the hypernetwork with both the base model and the context. Code and reproduction materials: this https URL

---


### 245. [The Mathematical Collective Unconscious: Jungian Archetypes within the Latent Space](https://arxiv.org/abs/2610.15678)

**<font color=#1a73e8>作者：</font>** Andrew Breen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Carl Jung theorised that the human psyche contains an inherited framework, the collective unconscious, populated by universal archetypes. As large language models (LLMs) are trained on vast corpora of textual data, this paper investigates whether they spontaneously construct distinct archetype-like regions within their high-dimensional latent spaces. The paper proposes that these regions function as spatial constraints that naturally organise semantically related narratives. To evaluate this, we applied cosine similarity and angular distance metrics across thirteen experiments utilising OpenAIs text-embedding-3-small model. The paper contains two experimental sections the first section explores these ideas using synthetically constructed narratives, the results of which act as a baselines for experiments conducted in the second section where the synthetic data is replaced by human-authored literature (Shmoop corpus), unedited dream reports (DreamBank corpus), and culturally distilled folklore (Andrew Langs Fairy Books). The results show that archetypal roles occupy distinct, measurable regions in the latent space. Crucially, these regions remain compact and consistent because of narrative structure rather than simple word overlap. Additionally, text category dictates spatial distribution: dream reports concentrate within Trickster and Shadow regions, while traditional folklore distributes evenly across all tested archetypes. We conclude that transformer latent spaces encode stable regions which appear to correspond to recognised Jungian archetypes.

---


### 246. [Radioactive Feedback: Tracing Models Trained by Label-Only LLM Supervision](https://arxiv.org/abs/2610.15685)

**<font color=#1a73e8>作者：</font>** Yuejia Li, JunHeng Li, Hao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional distillation transfers capability through teacher-generated demonstrations. LLM-as-a-Judge knowledge distillation offers a distinct and increasingly practical alternative. In the label-only variant studied here, the student generates every response and improves from scalar scores alone. Prior work shows that this non-demonstrative feedback can improve student capability, but it creates a fundamentally different provenance problem. No teacher-generated answer enters the student's training set, so any evaluator-specific trace must pass through a low-bandwidth reward signal rather than copied text. Existing watermarks and distillation detectors do not cover this score-only channel. We introduce Radioactive Feedback, which encodes a registered pattern of behavioral preferences in the rewards themselves. The evaluator applies bounded pointwise adjustments to quality-qualified responses, allowing repeated optimization to transfer the pattern to a student trained by another party. Experiments on code and mathematics show that the registered preferences transfer through scores alone and across datasets, enabling black-box detection against a fixed reference pool.

---


### 247. [Towards Autopilot Labeling for Short Video Content Governance](https://arxiv.org/abs/2610.15687)

**<font color=#1a73e8>作者：</font>** Junwen Chen, Hongwei Wang, Zixuan Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The explosive growth of short videos has presented significant challenges to content governance. Traditional manual labeling is inefficient, slow to iterate, and costly. Therefore, we explore and develop a multi-stage autopilot labeling framework aimed at progressively increasing the level of automation in short video content annotation. To move beyond the heavy reliance on human expert labeling at the initial L0 stage, we first introduce a discriminative MLLM labeler at the L1 stage, which is fine-tuned with supervised data to directly predict labels for short videos. Advancing to the L2 stage, we shift to a domain-adaptive MLLM pretrained on short video data and use it for zero-shot labeling, enabling flexible generalization without task-specific supervision. In the L3 stage, we propose an agentic annotation workflow, and equip the agent with several key tools, which empower the agent to handle complex, unfamiliar, or vaguely defined cases, significantly reducing the need for human intervention. We conduct extensive experiments across various content issues, and results demonstrate that each stage of the autopilot labeling framework progressively improves labeling accuracy, and has significantly reduced manual labor costs in real-world applications by up to 85%.

---


### 248. [Do LLM Tutors Actually Teach? A Process-Centered Synthesis of the Tutoring Loop](https://arxiv.org/abs/2610.15692)

**<font color=#1a73e8>作者：</font>** Sayantan Adak, Rima Hazra, Koyel Mukherjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can produce fluent tu- toring dialogue, but whether they actually help students learn remains unclear. We present a process-centered synthesis of LLM tutoring that follows the path from learner-state infer- ence to pedagogical action, tutor training, eval- uation, and student simulation. This view ex- poses a central gap: implementing a tutoring component does not establish that it works or that its outputs meaningfully affect later stages. A structured study-level audit shows that peda- gogical evaluation is common, while evidence becomes much thinner for learner-conditioned intervention, human learning gains, and espe- cially transfer or delayed retention. Human studies nevertheless provide a conditional posi- tive result: LLM tutors can improve learning, but benefits depend on pedagogical structure, learner engagement, and how learning is mea- sured. We argue that progress requires validat- ing the interfaces between tutoring stages, not only improving individual components.

---


### 249. [Generalizable Model Editing Could Be More Than Direct Generalization](https://arxiv.org/abs/2610.15707)

**<font color=#1a73e8>作者：</font>** Xiaotian Ye, Chunyao Yang, Xiaohan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central desideratum in model editing is generalization to complex tasks, which prior work formalizes under a direct generalization paradigm: treating and evaluating LLM behavior as an input-output mapping and expecting a factual update to alter outputs on reasoning tasks. Yet despite substantial empirical effort, the field consensus remains that such generalization is highly challenging and elusive. However, when we deploy the latest models in an in-the-wild chatbot-user setting, we surprisingly find that even classical editing methods exhibit remarkably fluent generalization behavior. This motivates us to revisit the obstacles to generalization and the limitations of the prevailing paradigm. We find that direct generalization is fundamentally constrained both theoretically and practically: theoretically, it suffers from an identifiability issue; and practically, existing approaches attempting to circumvent this are further hindered by the ambiguity of their constructed biases and by vulnerability to being overridden by other factors such as optimization dynamics. We instead identify compositional generalization, empowered by the increasingly strong reasoning and composition abilities of modern LLMs, as a theoretically grounded and empirically validated alternative. We validate this phenomenon across multiple models and editing methods, showing that such generalization behavior is widespread. Overall, we argue that generalizable model editing could be more than direct generalization, and call for a paradigm shift toward more generalizable and practically deployable knowledge update techniques.

---


### 250. [SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications](https://arxiv.org/abs/2610.15708)

**<font color=#1a73e8>作者：</font>** Yutong Cheng, Haifeng Chen, Peng Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents based on frozen language models can improve their performance by refining the external context they rely on, without updating model weights. We study recursive self-improvement through behavioral specifications: natural-language code documentation that describes the behavior of program entities and guides agents in generating correct code. We formulate a self-improvement loop in which an agent generates code from its current specifications, evaluates it with execution-verified tests, and refines the specifications based on observed failures. The improved specifications then guide subsequent generation, progressively improving the agent's understanding of the codebase. However, recursive refinement is challenging because program entities are interdependent. Improving the specification of one entity can inadvertently degrade the correctness of others, a phenomenon we call output coupling. This creates a whack-a-mole effect in which local improvements cause regressions elsewhere, preventing consistent progress. We introduce SpecForge, a multi-frontier tree search framework that addresses this challenge with three mechanisms: (i) Pareto-guided state selection preserves complementary specification states and prevents premature commitment; (ii) dependency-constrained entity selection prioritizes callee-before-caller refinement; and (iii) error-diversified expansion explores multiple refinements using different subsets of test failures. On DevEval+, SpecForge achieves the best performance across five backbone models, including a 94.9% solve rate with Claude-4.5-Sonnet and a 5.7-percentage-point average improvement over the strongest baseline. The improved specifications also make the agent better at tasks outside the loop: they transfer to cross-language translation and to new-feature implementation, where they outperform the benchmark-provided requirement documents.

---


> [!TIP]
> 当前位于：**201-250**（第 5/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
