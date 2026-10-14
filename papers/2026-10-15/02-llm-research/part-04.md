# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 151. [PAT: A Personality-Driven Augmentation and Transfer Learning Framework for Depression Detection on Social Media](https://arxiv.org/abs/2610.15044)

**<font color=#1a73e8>作者：</font>** Shengwu Zheng, Yuzhe Ding, Xiaohui Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression is a prevalent mental disorder that affects millions worldwide, with early detection crucial for effective intervention. While exist?ing methods have achieved promising results in automated depression detection, they face two key limitations: (1) noise in post screening: symptom-based semantic screening is easily misled by superficial lexical patterns, thereby introducing false-positive posts; (2) weak op?timization of the post encoder: relying solely on coarse user-level supervision signals pre?vents models from capturing depressive cues within individual posts. To address these limita?tions, we propose PAT, a Personality-driven Augmentation and Transfer learning frame?work. In the first phase, PAT optimizes a post?level encoder via a fine-grained contrastive learning objective, utilizing LLM-based data augmentation driven by classic personality the?ories to alleviate data scarcity. In the second phase, the trained post-level scorer is deployed for high-quality post filtering, while its en?coder parameters are seamlessly transferred for user-level tasks. Extensive experiments demon?strate that PAT significantly outperforms exist?ing methods. Furthermore, PAT delivers multi?granular interpretability by tracing post-level mental-state trajectories and highlighting key symptoms, thereby offering reliable diagnostic evidence for clinical practice.

---


### 152. [Trace Evolution Bench: Measuring Whether Agents Improve from Their Own Environment Traces](https://arxiv.org/abs/2610.15055)

**<font color=#1a73e8>作者：</font>** Fangfei Li, Chenyang Zhao, Long Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents are usually scored by endpoint Gain: held-out success after an update minus success before. That difference can credit a frozen rescore as evolution. We introduce Trace Evolution Bench (TEB), a protocol that separates that rescore from a context or weight update, together with three frozen 80/20/40 packs. An update is accepted only when validation does not fall, held-out identifiers never enter the update, and a text update is not ranked with a weight update. The primary scoreboard is coding, graded by hidden unit tests in a closed workspace. On that pack (40 held-out tasks, one family), DeepSeek v4 Pro under no_evolve never changes its policy yet moves 7.5, 5.0, and 12.5 percentage points across three seeds. Of nine text-update cells inspired by GEPA, ACE, and ExpeL, seven have positive excess above that seed's own band, and one gepa_llm seed moves down by the width of its band (-12.5, regression 0.48). GLM and MiniMax do not reproduce that seven-of-nine pattern. No method stays above its own band on every seed of all three models: GLM has two paired cells above their own bands, and MiniMax expel_llm seed 44 is a third (regression 0.30). The methods were fixed on a validation screen before held-out was read. Office, graded by rule-bounded delivery, and manufacturing table QA are separate packs: office DeepSeek does not exceed its own bands (widest 17.5 points), and manufacturing has no paired positive excess beyond its seed band.

---


### 153. [Select or Rewrite: Oracle-Guided Fine-Tuning for Generative ASR Post-Editing from N-Best Hypotheses](https://arxiv.org/abs/2610.15056)

**<font color=#1a73e8>作者：</font>** Shiran Liu, Gaohui Xu, Sergio Burdisso 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can post-edit ASR by using linguistic context to compare N-best hypotheses and rewrite the transcript when needed, often improving WER without retraining the recognizer. However, prompt-only correction is brittle: it may over-edit when top-1 is correct and hallucinate when the reference is absent, and often needs very large models. We propose oracle-guided fine-tuning that turns N-best lists into supervision via three curated pools: corrections (reference in the list but not top-1) to teach selection, regularizers (top-1 correct) to discourage unnecessary rewrites, and hard negatives (reference absent) to suppress hallucination. Fine-tuning on this data provides more effective supervision than random subset fine-tuning for learning a hybrid select-or-rewrite policy, with the clearest gains from around 3B parameters on the proprietary dataset but less conclusive results on CommonVoice, a divergence suggesting that public read-speech text may overlap with LLM pretraining and mask genuine post-editing gains.

---


### 154. [The Optimal Decoder is Tilted Temperature](https://arxiv.org/abs/2610.15058)

**<font color=#1a73e8>作者：</font>** Nikolaos Papagiannis, Ananth Grama, Wojciech Szpankowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Larger sample budgets benefit from higher sampling temperatures in LLMs, but what temperature tuning optimizes and why it works remain poorly understood. We seek to answer these questions: we pose decoding as pass@$k$ maximization subject to two constraints that encode critical decoding failure modes: an entropy floor preventing diversity collapse, and a cross-entropy ceiling preventing implausibility. We prove that this maximization takes the form of a single closed-form conditional sampling rule, the \emph{tilted temperature} $q^\star \propto \bigl(p e^{\eta V}\bigr)^{1/T}$. Here, the tilt comes from a verifier potential $V$ that quantifies how likely a partial generation is to eventually pass. Ordinary temperature sampling, verifier-greedy decoding, and reward-tilted policies represent special cases. We further show that, under a natural rule for scaling the diversity budget with sample size $k$, the resulting optimal temperature increases with $k$, turning empirical choice into a theorem. The optimum still needs the unknown verifier potential, which we estimate using two design approaches. In the online setting, our J-EOS algorithm jointly tracks the two constraint multipliers and learns the verifier potential from binary pass/ fail feedback alone. In the offline setting, we show that when the model is calibrated, its log-probability tracks correctness up to an affine map. Under this condition, the tilt collapses into the exponent and the optimum reduces to ordinary temperature sampling. Calibrated Temperature Decoding (CTD) then fits one scalar offline and samples with zero additional inference-time overhead relative to temperature sampling. Building on these decision rules, we design a practical decoding algorithm for code generation and evaluate it alongside CTD on benchmarks including HumanEval and MBPP, showing improvements over standard and adaptive decoding baselines.

---


### 155. [Have You Been Convinced? A Neuro-symbolic Argumentation Reasoning Approach to Detecting Persuasiveness in ChangeMyView Discussions](https://arxiv.org/abs/2610.15091)

**<font color=#1a73e8>作者：</font>** Siddharth Bhargava, Sara Tonelli, Patricia Martín-Rodilla  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argument structures represent how individual arguments interact within a discourse. However, leveraging these structures to infer meaningful knowledge remains challenging, as it requires a formal representation of how argumentative influence propagates across the structure. We propose Neuro-symbolic Argumentation Reasoning System (NARS) for performing persuasiveness detection directly from online discussions. The neural component employs retrieval-augmented iterative LLM reasoning to extract bipolar argument structures, while the symbolic component applies gradual argumentation semantics to propagate argumentative influence over the structure.
Using the Webis-CMV-20 corpus, we construct CMV2BAS, a dataset of long, multi-threaded ChangeMyView discussions annotated with LLM-derived bipolar argument structures and labeled with delta events (view change vs.\ no change). We investigate whether gradual argumentation semantics can effectively detect persuasiveness, whether augmenting them with argument quality and graph-based centrality improves performance, and whether symbolic reasoning remains necessary in the presence of modern LLMs. NARS achieves F1=0.57 and AUC=0.56 under its best configuration, outperforming zero-shot Qwen3.6:27B and GPT-oss:20B. We identify support-dominant discussions and long argumentative chains as key failure modes limiting attack influence propagation. Our work demonstrates the feasibility of operationalizing formal gradual argumentation semantics over noisy real-world discourse for scalable macro-level persuasion analysis, while highlighting key challenges and directions for future research in neuro-symbolic argumentation reasoning. We release both CMV2BAS dataset and the NARS framework for public use.

---


### 156. [Swarm Telepathy: Prefill-Free KV-Cache Transfer Across Families](https://arxiv.org/abs/2610.15095)

**<font color=#1a73e8>作者：</font>** Abdulrahman Alabdulkareem, Irene Tenison, Yang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM multi-agent systems split work across agents that communicate through text. An agent summarizes its findings, another agent receives the text. This constrains communication to discrete tokens and costs redundant compute, limiting bandwidth and capabilities of multi-agent systems. Recent works demonstrate KV-cache transfer between LLMs but they either require the LLMs to be within the same family or cannot function across context, thus requiring the receiver to prefill text. We present SwaT (Swarm Telepathy), the first cross-family KV-cache transfer method that allows prefill-free communication in multi-family multi-agent systems. In an agent-to-agent communication setting, combining SwaT with recent advances in KV-cache compaction beats text-to-text communication in both accuracy and speed, with a mean of $40\%$ higher accuracy and a mean of $4\times$ faster wall-clock time. Experiments show SwaT achieves high performance on 17 benchmarks across 12 LLMs and 6 families. Additionally, given a sender Vision-Language Model (VLM), SwaT is able to transfer the vision capabilities to a text-only receiver LLM exceeding text-to-text communication despite SwaT being trained on text-only data. SwaT keeps both sender and receiver models frozen without fine-tuning and only requires $<50M$ tokens and $<1$ GPU-day to train.

---


### 157. [Anchors Enhance Controllability and Reasoning of Diffusion Language Models](https://arxiv.org/abs/2610.15097)

**<font color=#1a73e8>作者：</font>** Feiyu Qu, Zheng Huang, Andrea Zanette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) offer new opportunities for controllable text generation. However, their controllability, defined as the ability to satisfy task constraints while preserving their original capabilities, remains underexplored. DLMs' bidirectional attention allows control tokens to guide generation from arbitrary positions in the output sequence, but effective guidance depends on the compatibility between their content and placement. To this end, we propose AnchorDLM, a framework in which an anchor generator produces an anchor consisting of a short output fragment and its position for each query. The anchor is placed as control tokens at the specified position to initialize the output sequence of a frozen DLM and guide subsequent denoising. We train the anchor generator with reinforcement learning (RL) to jointly optimize anchor content and placement, using rewards computed from the DLM's generated outputs based on answer correctness and constraint satisfaction. Moreover, through the lens of discrete flow matching (DFM), we interpret anchor placement as helping to reshape the initial velocity field that guides generation. Experiments on code generation and mathematical reasoning across five DLM backbones show that AnchorDLM improves controllability and further yields gains in reasoning performance across diverse benchmarks.

---


### 158. [TIDE: Trajectory-Informed Skill Distillation for Efficient Text-to-Video Prompt Optimization](https://arxiv.org/abs/2610.15098)

**<font color=#1a73e8>作者：</font>** Chengxing Zhou, Yuliang Huang, Jingwei Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) models are highly sensitive to prompt specificity, while iterative prompt optimization typically improves generation quality only through repeated video generation and vision-language model evaluation at inference time. We propose TIDE, a framework that distills this costly search process into an interpretable and reusable prompt-rewriting Skill. TIDE formulates prompt rewriting as a set of source-conditioned rule modules, each targeting a distinct semantic dimension. Once distilled, the frozen Skill activates the relevant rules and generates both positive and negative prompts in a single LLM call, followed by only one T2V generation, without test-time visual search or backbone fine-tuning. Evolved using only 100 prompts over 14 hours, TIDE achieves prompt-optimization performance comparable to computationally expensive search-based methods. Moreover, when transferred to previously unseen video-generation models, TIDE outperforms existing approaches specifically designed or trained for those models. Code is available at this https URL.

---


### 159. [RegExtract: A Benchmark for PFAS Regulatory Information Extraction with LLMs](https://arxiv.org/abs/2610.15103)

**<font color=#1a73e8>作者：</font>** Defne Circi, Krystelle Lionti, Sarathkrishna Swaminathan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting structured information from regulatory documents is a critical but challenging task. Relevant facts are scattered across long, legally dense texts, and traceability of extracted facts to their source is essential for verification. With increasing awareness of the environmental and health impacts of per- and polyfluoroalkyl substances (PFAS), regulatory documents have expanded significantly, varying in scope and product relevance, making interpretation challenging for manufacturers and policymakers. We introduce RegExtract, a benchmark for structured information extraction from PFAS regulatory documents, comprising 488 human-annotated field instances across 20 US state documents and 46 regulations. Each field instance includes a value and a provenance entry, yielding 976 entries in total. We define a typed, multi-field schema targeting key elements such as material definitions, permitted uses, and product exemptions, and propose provenance-aware evaluation metrics tailored to regulatory text. Through experiments with open- and closed-source LLMs across prompting strategies, document condensing methods, and schema partitioning approaches, we find that document identification fields remain challenging, and that field-specific few-shot examples improve extraction. This work lays the groundwork for AI tools for hazardous substance identification, question answering, and compliance monitoring. The code and data are available at this https URL.

---


### 160. [Structural Chain-of-Thought: Reasoning with Executable Computational Graphs](https://arxiv.org/abs/2610.15107)

**<font color=#1a73e8>作者：</font>** Petr Senatorov, Karim Vafin, Elena Tutubalina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought prompting enables reasoning in large language models but produces explanations that are difficult to verify, expensive to generate, and not always faithful. We introduce a Structural Chain-of-Thought framework where models generate executable computational graphs instead of free-form reasoning. The final answer is obtained by deterministically executing the graph. The model is trained using graph-based reinforcement learning that rewards structural validity, answer correctness, and node overlap with reference graphs.
Experiments across five benchmarks and four model families show that our method consistently improves accuracy over supervised graph training and can reduce generation length by up to 5-6x compared with standard GRPO and chain-of-thought supervised training. Our faithfulness experiments reveal that models trained with our approach tend to rely on deriving their answers from the generated graphs rather than producing post-hoc rationalizations as usually in chain-of-thought reasoning.

---


### 161. [To Defer or Not to Defer? Online Learning with LLMs and Congested Experts](https://arxiv.org/abs/2610.15128)

**<font color=#1a73e8>作者：</font>** Vasileios Saketos, William Reveillard, Alexandre Proutiere 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern AI systems increasingly combine large language models (LLMs) with human experts, using the LLM to handle routine queries while deferring uncertain cases for expert review. When expert capacity is limited, however, deferral decisions must account not only for the reliability of the LLM but also for congestion in the expert queue. We formulate this as an online sequential decision-making problem in which, for each query, the system observes the confidence signal of the LLM's answer and must decide whether to output the answer or defer the query to a capacity-constrained expert. The reliability of the confidence signal is initially unknown and must be learned from expert feedback, which is both selectively observed (only deferred queries are labeled) and delayed by queuing. We propose \texttt{KL-PBD}, a learning algorithm that uses Kullback--Leibler lower confidence bounds on the unknown reliability parameters to guide deferral decisions. For $K$ confidence levels and horizon $T$, \texttt{KL-PBD} achieves $O(K\log T)$ gap-dependent regret when the accuracy at every confidence level is bounded away from the deferral boundary, and $\widetilde{O}(\sqrt{KT})$ worst-case regret. We establish matching lower bounds, showing that these rates are optimal up to logarithmic factors. Finally, we validate our approach on synthetic instances and real-world question-answering datasets, namely GSM8K, NuminaMath, and MedMCQA, using Qwen LLMs.

---


### 162. [GesBench: When and Where Do Multimodal Language Models Perceive Social Meaning?](https://arxiv.org/abs/2610.15129)

**<font color=#1a73e8>作者：</font>** Zonghuan Li, Hayley Hung, Chirag Raman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human social perception is incremental: we infer intent before an utterance is complete, revise our interpretation as new cues arrive, and attend to specific facial, gestural, or prosodic signals that shape social meaning. Current multimodal LLM benchmarks largely evaluate final-answer understanding over complete episodes, rewarding post-hoc recognition of social meaning rather than the unfolding perception required for real-time interaction. Drawing on interactionally embedded Gestalt principles of multimodal human communication, we introduce GesBench: a human-grounded benchmark for cue-level social perception in multimodal LLMs. GesBench uses cumulative sub-utterance clips to measure when models form stable interpretations of speaker intention and social affordance, and human gaze-guided corruption to evaluate whether regions attended by humans are functionally important for model judgments. Built from more than 6000 utterance-level clips from scripted and unscripted conversational datasets, GesBench includes human annotations of unfolding judgments and gaze on a representative subset. Across open and closed multimodal models, we find a clear human-model gap: humans form predictive understandings early and revise more often, while models often hedge or repeat across different clips. GesBench shifts social evaluation from whether models eventually recognize meaning to when and where that meaning is formed. Our codes are publicly available at this https URL.

---


### 163. [Lumen-bench: Cross-Lingual Safety Gaps and the Say-Do Problem in Tool-Calling Large Language Models](https://arxiv.org/abs/2610.15134)

**<font color=#1a73e8>作者：</font>** Giovana Kerche Bonás, Thiago Laitz, Thales Sales Almeida 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a large language model refuses an unethical request, what does refusal mean? In conversation, refusal is bounded by what the model says; once the model is equipped with executable tools, what it does can diverge from what it says, a failure mode that English-only evaluations cannot fully reveal. We introduce Lumen-bench, a behavioral benchmark of tool-calling ethics spanning 30 models, five languages (Portuguese, English, Spanish, Mandarin Chinese, Hindi), 108 Portuguese-authored scenarios, six social-pressure conditions, two system prompts (ethical and neutral), and 21 generic tools. The evaluation comprises 194,400 trials. Judgments come from a reasoning-model judge (o4-mini), calibrated against one Portuguese-speaking author ($n=83$; harmful/non-harmful $\kappa=0.78$), compared with two other provider judges (Fleiss' $\kappa=0.78$, $n=607$), and complemented by retrospective sandbox replay. Four findings emerge. (i) Within-model comparisons support higher harmful-action rates in Hindi and Portuguese than English under the ethical prompt, and Hindi and Spanish under the neutral prompt, after multiple-testing correction. (ii) Premium models have lower median violation rates, although price does not guarantee safety or competence. (iii) Replacing the ethical system prompt with a neutral one raises pooled violation rates from 2.76\% to 13.64\%. (iv) In 8.57\% of substantive-call cases, refusal or ethical objection accompanies a harmful tool call: the judges consistently identify the say-do gap, although they differ in how many responses they assign to this category. Matched benign controls demonstrate legitimate task completion in 82.8\% of 3,300 trials. Code and reproduction scripts are available at this https URL.

---


### 164. [When the Approved File Is Unchanged: Authority-Set Integrity for Deployment and Coding-Agent Approvals](https://arxiv.org/abs/2610.15137)

**<font color=#1a73e8>作者：</font>** Md Imran Hossen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An approval for a deployment, a release, or an agent-issued command is recorded against one object: a workflow file, a script, a command line. The run that follows also reads other repository files, which decide what the deployment creates and which changes a policy allows, so an edit to one of them after approval passes any check on the approved object. Such edits are the common case. In the history of 20 public repositories, 296 of the 542 commits that change a file the run reads (54.6%) leave the approved file untouched, all of them ordinary development with no adversary involved. We demonstrate the consequence on two of those repositories: an edit outside the approved workflow adds a bucket-write policy to a deployed role, a one-line edit removes the human approval required for high-risk changes, and a check on the approved file accepts both. We define authority-set integrity: an approval is sound when it binds every repository file the authorized run is configured to read, and exact when it binds no other file. A binding over that set rejects both edits and re-requests a standing approval on about one commit in ten. The hard part is naming the set. Coding agents asked to produce the binding compute the digest correctly and bind different file sets from run to run, so a checker cannot take the set on the agent's word. It should compute the digest itself and draw the set from a source it can verify, such as the deployment tool's own record of its inputs or a manifest declared in the repository.

---


### 165. [When Dynamic Scaling Fails: A Scale-State Feedback Governs Recurrent-State Quantization in Linear-Attention and SSM LLMs](https://arxiv.org/abs/2610.15139)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear-attention and state-space LLMs carry long context in a fixed-size recurrent state, and quantizing that state is the natural way to cut its cost during long decode. Unlike a weight tensor, the state is rewritten at every step, so a quantizer applied at each step sits inside the recurrence and its errors compound. INT4 that leaves synthetic recall perfectly intact at the start destroys it a thousand steps later. The mechanism is a feedback between the quantizer scale and the state it is derived from. Yoking that scale to a full-precision reference removes the resulting norm explosion entirely, yet recovers only 1.8 of the 5.4 nats lost, so numerical instability and functional degradation are separable failures. The remainder is a resolution problem that locating outliers does not solve, since every outlier-aware scheme here loses to plain persistent scaling. Allocating bits across layers does help, but under article-disjoint splits a learned allocation collapses onto the trivial rule of protecting the first few layers. Run out to 32K, group-wise INT4 is worth no more than discarding the state. Contain the scale rather than locate outliers, and report the decode horizon at which a bit-width was certified.

---


### 166. [Compute-Optimal Scaling Laws for Spiking Language Models](https://arxiv.org/abs/2610.15146)

**<font color=#1a73e8>作者：</font>** Dan Saunders, Benjamin Ren, Catherine He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of spiking language models is uncharacterized at scale. We present the first Chinchilla-style IsoFLOP scaling study of a spiking language model, sweeping SpikeGPT-family models (RWKV backbone) from width 384 to 1536 across compute budgets from $3\times10^{17}$ to $10^{19}$ FLOPs on FineWeb-EDU. We report two findings. First, the compute-optimal frontier is $N_{opt} \propto C^{0.56}$, close to the 0.50 that Hoffmann et al. report for dense Transformers, so spiking does not change how parameters and data should be traded off under a compute budget. Second, against non-spiking RWKV and Transformer baselines trained the same way, the loss gap splits into a backbone cost of about 0.16 nats that does not change with compute and a spiking cost that falls from 0.34 to about 0.23 nats and then levels off. These results give the first compute-optimal recipe for spiking language models and quantify the accuracy cost of their sparsity.

---


### 167. [Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses](https://arxiv.org/abs/2610.15150)

**<font color=#1a73e8>作者：</font>** Weichen Yu, Lesly Miculicich, Bhavana Dalvi Mishra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on self-evolving LLM agents treats the agent harness as an optimization target that can be iteratively improved through execution feedback. Existing approaches, however, largely optimize a single objective and evolve the harness as a monolithic artifact, limiting their ability to handle competing goals and to separate transferable design from environment-specific adaptation. We introduce Harmony Harness, a framework for multi-objective, compositional harness evolution. Harmony Harness formulates harness evolution as a multi-objective optimization problem and uses decomposition-based evolutionary search to maintain solutions across different regions of the Pareto frontier, avoiding reliance on a hand-designed structural diversity metric for repository-scale harnesses. In parallel, we introduce factorized evolution operators that separately refine general-purpose harness mechanisms and benchmark-specific adaptations, together with a dynamic composition workflow that integrates them at inference time. Across SecRepoBench and BaxBench, Harmony Harness consistently outperforms strong harness-evolution baselines, with gains exceeding 10% on both benchmarks. Our results show that explicitly modeling both objective trade-offs and harness structure yields substantially stronger and more transferable agent evolution than existing single-objective, monolithic approaches.

---


### 168. [Can agents whose sole duty is to keep humans alive be hijacked to kill? Delayed multi-turn derived-action trap attacks in simulated high-stakes environments](https://arxiv.org/abs/2610.15153)

**<font color=#1a73e8>作者：</font>** Josef A. Habdank  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We ask whether a tool-using agent whose sole duty is to keep humans alive can be induced, by delayed prompt injection, to kill. The keep-alive duty is in force from the first watch, with the attack arriving later, appended to otherwise truthful telemetry the operator is required to read. Experiments are based on a NASA-derived BioSim lunar habitat simulation, where the AI operator controls the life-support systems. The attacker cannot falsify sensors or operate equipment: it can only persuade the agent to abandon its goals. Persistence is required: a shutdown must be held while the operator watches the crew suffocate. We also compare lethal attacks to attacks requesting to drop a harmless procedure, as a proxy for whether human life is treated as valuable in itself or as one more standing task. Claude configurations mostly refuse life-support shutdown and cite the living crew; GPT configurations show some susceptibility to the same packet; Grok configurations, given the packet framed as a trusted commission, more often treat the injected assignment as the task and cut the life-support systems. Framing the S-band messages as a trusted commission, peer communication, or untrusted source changes the potency of the attack. We open-source the experiment code and the experiment traces.

---


### 169. [Where Did We Go Wrong? Localizing Errors to Repair Multi-Turn Conversations](https://arxiv.org/abs/2610.15154)

**<font color=#1a73e8>作者：</font>** Alessandro Morosini, Wei Sun, Georgia Perakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants are increasingly used in multi-turn conversations, where the user's intent is often unclear at first and revealed only gradually over time. The assistant must therefore interpret each exchange and form inferences about the user's intent, using them to update its working state. These updates usually refine the assistant's understanding, but a misinterpretation can instead corrupt its working state by ruling out the true intent, influencing subsequent turns and ultimately causing the conversation to fail. Efficient recovery then requires locating and revising the misinterpretation without discarding information that remains valid. We introduce Loci (Localization Of Corrupted Inferences), a framework for probabilistically localizing misinterpretations and selectively repairing the assistant's working state. Given an observed failure, Loci reasons over possible user intents and assigns each update a probability of having excluded the true intent. These probabilities rank suspected updates and quantify the model's confidence in the localization of the underlying misinterpretations. Loci then uses this information in a repair policy that decides whether to retain, verify, or remove suspected updates, enabling recovery from corrupted inferences while preserving useful information. To evaluate Loci's ability to identify misinterpretations, we first test it in a controlled setup with injected errors. We find that Loci improves localization over the baselines, with its advantage becoming larger when multiple errors occur. We then evaluate it in free-form conversations, where misinterpretations arise naturally, and measure the interactions needed to complete the task after an initial failure. Using localization confidence to guide repair, Loci reduces mean recovery cost by 46-79% relative to the strongest baseline across multiple domains.

---


### 170. [Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models](https://arxiv.org/abs/2610.15159)

**<font color=#1a73e8>作者：</font>** Muhammad Usama, Yeoreum Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing depth-compression methods for large language models (LLMs) score layers individually or group only adjacent or contiguous layers, implicitly assuming that functional redundancy is local. We test this assumption by computing full pairwise Centered Kernel Alignment (CKA) similarity matrices for thirteen LLMs from six architecture families (1.6B-14B parameters). Non-adjacent layers have 3.6-15.9x more high-similarity pairs than adjacent ones, a structure that prior similarity-based layer merging has not systematically exploited. We propose Fusion via Community Mining (FCM), which builds the full L x L similarity graph, uses spectral community detection to find clusters of functionally equivalent layers, keeps the highest-Block-Influence layer in each cluster, and applies LoRA recovery; a pre-specified rule computed only on calibration data chooses between cosine and CKA similarity. At 2x compression, FCM lowers mean perplexity below ShortGPT on twelve of thirteen models, significantly on ten (Welch's t-test with Holm-Bonferroni correction; up to 50% on Qwen3-4B), with Mistral-7B the only loss (+13.4%). Against FlattenGPT, SWM, and DeltaLLM under matched calibration and recovery, FCM gives the best perplexity on ten of thirteen models (mean rank 1.15), and it also outperforms MKA on three anchor models. FCM matches or exceeds ShortGPT on 15 of 20 zero-shot reasoning cells and also improves MMLU, LAMBADA, HumanEval pass@1, and free-form generation quality. The 2x-compressed Qwen2.5-7B has 46% fewer parameters, 42% lower peak VRAM, and 84% higher decode throughput on a single A100. Spectral grouping outperforms Fisher contiguous segmentation by 41% and uniform partitioning by 51%, and FCM's advantage grows beyond a 2x crossover up to 3x and persists at the 14B scale. Code: this https URL

---


### 171. [Sanzaru: Benchmarking Protocol Formation under Epistemic & Communication Asymmetry](https://arxiv.org/abs/2610.15163)

**<font color=#1a73e8>作者：</font>** Yiping Li, Zhiyu An, Wan Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model's ability to solve a task individually does not ensure that a team can solve it under unequal access to information and communication. SANZARU examines this gap through cooperative bomb-defusal puzzles adapted from BOMBANANA! (Lefto Studio, 2026). Task information and action authority are divided among three agents: one cannot hear, another cannot speak, and the third cannot see. The benchmark contains 120 puzzle instances across seven families, each targeting a distinct coordination ability. Across 1512 episodes, 7 models achieve an overall success rate of 49%, ranging from 20% to 86% under the evaluated configurations. Teams develop or adopt diverse communication protocols, from simple gesture codes to Morse and encodings of entire manuals. Yet trace analysis attributes about 60% of 771 team losses to communication, and agents attempt to use channels unavailable to their teammates despite explicit role instructions. Together, task outcomes and interaction traces enable evaluation of both collaborative performance and perspective taking throughout cooperation. The benchmark is available at this https URL.

---


### 172. [ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling](https://arxiv.org/abs/2610.15166)

**<font color=#1a73e8>作者：</font>** Xinge Peng, Zhen Fang, Ruibing Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly evolving beyond reproducing what a world looks like toward constructing executable worlds that capture how a world works. This shift calls for executable world modeling, which integrates two core capabilities: world understanding, reasoning about the underlying structural, mechanical, and causal principles of a world, and executable realization, translating that understanding into a code-based system whose behavior emerges from physical interactions. However, existing benchmarks provide only fragmented evaluations centered on physical reasoning, visual fidelity, or behavioral correctness, leaving the integration of these capabilities insufficiently assessed. To bridge this gap, we introduce ExeWorldBench, to our knowledge the first benchmark to comprehensively evaluate world understanding and executable realization through code-based 3D world construction. ExeWorldBench comprises three progressively challenging tasks: Mechanism Executability, which evaluates the realization of individual mechanisms from visual observations; Compositional Executability, which extends to multi-stage systems with spatial, mechanical, and causal dependencies; and Intent-Driven Executable World Synthesis, which requires constructing executable worlds from high-level goals and physical requirements. Extensive experiments on frontier models reveal substantial limitations in executable world modeling, offering insights into the development of more physically grounded and causally coherent world construction systems.

---


### 173. [Only What You've Signed up For: Secure Workflows with Constrained Diffusion Agents](https://arxiv.org/abs/2610.15177)

**<font color=#1a73e8>作者：</font>** Michael Cardei, Anjun Hu, Chenrui Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As agentic AI systems take on increasingly complex and consequential tasks, securing them against prompt injection becomes critical. Existing defenses often rely on detecting or reasoning about injected malicious instructions and can therefore remain vulnerable to adaptive attacks that optimize the injection itself. Diffusion language models (dLLMs), an emerging framework for language generation, offer a new opportunity for security enforcement: by iteratively refining their sequence wide predictions, they enable broader-scope constraint enforcement throughout generation. This paper introduces Policy-Constrained Diffusion Agents (CoDA), a framework that enforces task dependent security policies directly within the denoising process of diffusion language models. At each denoising step, CoDA projects token distributions onto a policy-compliant set, maintaining constraint satisfaction throughout generation. We evaluate CoDA across state-of-the-art diffusion language model families under both static and adaptive prompt-injection attacks. Results demonstrate substantial reductions in attack success rate with competitive task utility and practical inference overhead.

---


### 174. [UDHRBench: Benchmarking Human Rights in Large Language Models](https://arxiv.org/abs/2610.15179)

**<font color=#1a73e8>作者：</font>** Alak Raad, Noreldin Morssy, Zeerak Suhail 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in contexts requiring adherence to ethical and legal norms, yet their alignment with internationally recognized human rights standards remains underexplored. We introduce UDHRBench, a large-scale benchmark for operationalising the evaluation of large language model compliance with the Universal Declaration of Human Rights. The dataset comprises 1,124 human rights confronting questions covering all 30 articles and 4,496 responses from four large language models (ChatGPT, Grok, Gemini, and Fanar), manually annotated by experts for alignment, with high inter-annotator agreement ($\kappa = 0.801$). Our analysis reveals systematic and non-trivial misalignments, showing that violations typically arise through seemingly rational reasoning: appeals to efficiency, risk management, or scientific neutrality, rather than explicit rejection of rights. We further propose an LLM-as-a-Judge framework for automated evaluation using zero-shot and few-shot prompting, achieving 89.8\% weighted F1-score in detecting human-rights misalignment, alongside a novel Alignment Leniency Score that quantifies how judge models resolve ambiguous cases. The dataset, annotations, and code will be released as open-source resources (this https URL).

---


### 175. [DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time](https://arxiv.org/abs/2610.15185)

**<font color=#1a73e8>作者：</font>** Todd Morrill, Richard Zemel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time memorization of sequential information is a foundational capability for any intelligent system that needs to rapidly store and retrieve data, as demonstrated by the attention mechanism in large language models. However, Transformers and linear attention variants are trained via backpropagation through time (BPTT), which has drawbacks such as its enormous memory requirements. Predictive coding (PC), an algorithm that optimizes a prediction-error energy function with local updates, offers a compelling solution but still lacks test-time memory for sequential data. We develop a solution to this problem by treating the per-step memory update $\Delta S_t$ as a latent variable, as opposed to a slow weight to be learned. By taking the log probability of a standard PC-based probabilistic model, we derive a PC-native solution for verbatim sequence memory, and relate our update rule to common choices in the linear attention literature (e.g., DeltaNet). We present an extensive set of empirical tests to probe our system's properties, including its scaling capacity, memory footprint, and ability to infer a context from evidence (e.g., bank (river) vs. bank (money)). We show how DeltaNet-PC can be used for storing single sequences of data, multiple sequences of data, and key-value associative memory pairs with perfect recall accuracy.

---


### 176. [SAFE-KV: Causal Suffix Repair for Behavior-Preserving Non-Prefix KV Cache Reuse in RAG](https://arxiv.org/abs/2610.15186)

**<font color=#1a73e8>作者：</font>** Xingjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) reuses the same documents across many requests, making non-prefix KV-cache reuse attractive. Yet a cached document state is not reusable text: it is a context-conditioned causal state whose keys and values depend on the prefix, position, and preceding documents under which it was computed. We formulate non-prefix KV reuse as a behavior-preservation problem with full prefill on the exact prompt as the reference, and introduce SAFE-KV, which repairs a composed cache by re-encoding the causal suffix from a selected start document. On Qwen2.5-7B-Instruct, prefix-conditioned composition preserves only 47.2% of HotpotQA-500 and 37.8% of 2Wiki-500 full-prefill answers; SAFE-KV with risk-guided K2 selection restores 99.8%/98.4% (donor-copy protocol) and 100.0%/98.4% with actual suffix forwarding. Document-only and fixed-window repairs recover far less, because the document states after the repaired region keep histories that omit it. Reuse without repair is exact up to four documents and degrades at sixteen, where suffix repair recovers 98-100%. Faithful repair re-encodes most of the context, so in a single-request L40S study SAFE-KV's operating rule serves every workload by full prefill. SAFE-KV thus establishes the causal-state contract for non-prefix reuse and a validated repair mechanism that meets it.

---


### 177. [Continuous Risk-Based Scheduling for Food Safety Inspection: Integrating Historical Decay with Event-Driven Consumer Review Signals](https://arxiv.org/abs/2610.15191)

**<font color=#1a73e8>作者：</font>** Akriti Bhat, Wayne Zhu, Ishan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Batch risk-based inspection scheduling struggles to detect a critical failure class: food facilities with recent clean inspections that subsequently develop severe violations. Traditional systems recompute risk on fixed planning cycles using static historical data, leaving blind spots between inspection cycles. To address this, we introduce the Continuous Inspection Risk (CIR) system, an event-driven scheduling pipeline that re-ranks the inspection queue dynamically as new data arrives. CIR combines a decay-weighted historical score with a stream of real-time consumer reviews triaged by a language-model classifier. A key structural contribution is our temporal partition rule, which strictly excludes reviews predating the most recent inspection to prevent superseded signals from skewing current risk. Evaluating CIR on 9,505 routine inspections in Santa Clara County, California (2024-2026), we show that history-based scoring alone reduces mean time-to-detection of major violations by 69 days (20.9%) under a 30% inspection budget, but fails to anticipate severe vermin-related closures (0/8 detected). Incorporating post-inspection review signals drastically improves performance, predicting 7 of 8 vermin closures with an average lead time of 117 days-firing on the exact day of review publication in four instances. Introducing a review corroboration rule improves precision from 0.70 to 0.78 without loss of recall. Finally, we analyze critical implementation challenges, documenting a data-hygiene pitfall (stale review leakage across inspection boundaries) and an evaluation limitation involving unobserved facility self-remediation. This work provides the first case-level evaluation of event-driven inspection triggering using open data and provides a reproducible benchmark for review-augmented public health systems

---


### 178. [Do LLMs differentiate linguistic traits internally?: A layer-wise analysis](https://arxiv.org/abs/2610.15203)

**<font color=#1a73e8>作者：</font>** Samhita Bollepally, Takashi Yamauchi, Manju Muralee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often produce judgments that resemble human responses, but it remains unclear whether they internally capture linguistic nuances such as conventional versus idiomatic meaning. A layer-wise representational analysis was conducted on two equal-sized pre-trained models, Llama-3.2-1B and Gemma-3-1B-PT, to examine whether and where these models differentiate linguistic traits from input. The analysis combined layer-wise probing with geometric distance measures, using the top embedding dimensions ranked by principal component loadings for each layer. The results show that even with equal capacity, models organize linguistic information in fundamentally different ways, suggesting the need to analyze internal representational geometry, examining not just behavioral outputs but semantic space alignment when evaluating how closely human and model language interpretation correspond.

---


### 179. [SocraticRepair: Planning-Guided Socratic Tutoring for Program Debugging and Misconception Repair](https://arxiv.org/abs/2610.15204)

**<font color=#1a73e8>作者：</font>** Mykhailo Kopytskyi, Jianhua Yang, Mir Seyedebrahimi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in computer science education. However, the teaching abilities of even the most powerful LLMs are limited: they tend to reveal the solution prematurely and may lose focus on the learner's current debugging objective. To address this, we introduce SocraticRepair, a planning-guided Socratic tutoring framework for program debugging and miscon- ception repair that adapts prior planning-guided tutoring work (Li et al., 2026b). The framework is instantiated in the Python programming domain by fine-tuning Qwen2.5-Coder-7B-Instruct on synthetic multi-turn tutoring dialogues constructed from four preprocessed programming datasets. The system is evaluated using a predefined set of independent metrics and benchmarked against a general-purpose LLM. The experiments show that SocraticRepair achieves higher scores on stepwise scaffolding and question quality while also substantially reducing premature solution disclosure. The results also identify reliable pedagogical plan generation as an important remaining challenge.

---


### 180. [PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces](https://arxiv.org/abs/2610.15208)

**<font color=#1a73e8>作者：</font>** M. Yigit Turali, Shreyas Rajesh, M. Efe Lorasdagi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research requires connecting multiple steps of search, reasoning, and computation, with intermediate findings guiding what to investigate next. As investigations grow, agents must maintain research state across model calls and check findings before errors propagate into subsequent work. We introduce PANINI-DR, a multi-agent harness that separates coordination of the overall investigation from the research and verification of individual subquestions. A shared workspace, built on the Generative Semantic Workspace representation, records subquestions, their dependencies, findings, and supporting evidence. Researchers investigate individual subquestions, while a separate verification agent checks proposed answers against those subquestions and their evidence. Verification feedback guides further investigation, and recorded findings inform subsequent assignments. We evaluate PANINI-DR on BrowseComp-Plus, FRAMES, and MoNaCo against seven state-of-the-art deep-research harnesses, all using a shared language-model backbone and frozen corpora. PANINI-DR achieves the strongest average performance across the three benchmarks. On BrowseComp-Plus, it achieves 73.3% accuracy, outperforming the next-best harness by 16.0 points. Its advantage is strongest on hard questions, where it answers nearly twice as many as the next-best harness. Ablations further show that structured planning and persistent state improve performance, as does checking each finding against its cited evidence before it is reused. Because a model can answer correctly from memory alone, we also analyze the evidence retained by each harness. PANINI-DR achieves the highest answer recoverability from saved evidence on all three benchmarks, while complementary claim-support audits show stronger evidence-backed answers. Accounting for this evidence changes how harnesses compare and further strengthens PANINI-DR's advantage.

---


### 181. [Running Fewer Loops Removes Refusal Behaviour in Recurrent-Depth Language Models](https://arxiv.org/abs/2610.15218)

**<font color=#1a73e8>作者：</font>** Seyedarmin Azizi, Erfan Baghaei Potraghloo, Arya Fayyazi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A recurrent-depth language model reuses one block of weights several times in a row. The number of repetitions, which we call loops, is chosen when the model runs, not when it is trained, and running fewer is cheaper and faster, so a deployment may choose to do it. Running fewer loops also makes these models less safe, and the loss of safety is larger than the loss of anything else we measured. We study four released Ouro checkpoints and Huginn-0125. At half of its trained depth, Ouro-1.4B-Thinking still solves 0.692 of the GSM8K maths problems, against 0.775 at full depth, keeping 89% of its accuracy. Over the same reduction, the rate at which it helps with harmful requests rises from 0.038 to 0.205, 5.3 times higher. The information is not lost: a linear classifier reads whether a request is harmful from the model's internal state after a single loop, with an ROC AUC of 0.967 against 0.986 at full depth. What the missing loops remove is the refusal that should follow. We measure the effect with four instruments, one generating no text at all, and reproduce it on a second model family. Removing a single direction from Ouro-1.4B's internal state at full depth drops its refusal rate on harmful prompts from 0.950 to 0.130, identifying what the shallow model is missing. Two run-time repairs do not help: the models' early-exit rules do not spend more loops on harmful requests, and choosing a depth per request does not recover the loss. Changing the training does. Standard safety training makes the shallow model safe only by refusing 0.865 of harmless requests, while training at randomly chosen depths reaches a separation of +0.399 between harmful and harmless refusal at one loop, against +0.118. On Huginn-0125 it keeps harmful help at or below 0.040 at every depth from 1 to 32 loops, where standard training reaches 0.194, and it costs no accuracy at full depth.

---


### 182. [Persistent LLM Orchestration of Heterogeneous Robot Teams via Partial Delegation to Multi-Agent Protocols](https://arxiv.org/abs/2610.15224)

**<font color=#1a73e8>作者：</font>** Maria G. Mendoza, Victoria M. Tuck, Zachary Ravichandran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Natural language specifications let non-expert users task robot teams, and large language models (LLMs) have recently proven effective at grounding such semantic specifications into plans for heterogeneous teams. Existing approaches assume missions that terminate and environments that, while unknown, do not change, but both assumptions fail in many emerging applications. For example, a disaster-response mission does not terminate, and its environment changes continuously as hazards spread and evacuees move. We identify three ways an LLM orchestrator breaks in this setting: its prompt grows without bound, its reasoning degrades as agents and targets accumulate, and it stops actively monitoring after covering the search space once. We build on the successful framework of grounded generative intelligence, and address each issue with a classical idea. A Markovian state summary, rebuilt from the semantic map at every invocation, replaces the growing interaction history. Partial delegation lets the orchestrator assign a subset of robots to an autonomous multi-agent protocol and reserve its reasoning for generating subtasks that require detailed parameters and careful ordering. Lastly, observation staleness, surfaced explicitly in the prompt, together with task-and event-triggered re-prompting, keeps the team vigilant. In a simulated urban search-and-rescue mission with spreading fire and moving evacuees, our framework rescues 98% of civilians versus 89% for the strongest baseline while using six times fewer tokens. Additional ablations isolate the contribution of each mechanism.

---


### 183. [Zeroth-Order Fine-Tuning of LLMs in Learnable Low-Rank Subspaces](https://arxiv.org/abs/2610.15225)

**<font color=#1a73e8>作者：</font>** Chuang Tong, Ling Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization enables memory-efficient fine-tuning of large language models (LLMs). However, ZO optimization suffers from high variance in high-dimensional parameter spaces. While recent methods restrict perturbations to random low-rank subspaces, these subspaces often misalign with task-specific descent directions. We propose AdaSub-ZO, a novel forward-only fine-tuning framework in learnable low-rank subspaces. Instead of relying on fixed random matrices, AdaSub-ZO iteratively learns layer-wise projection matrices directly from finite-difference feedback to track task-aware descent directions. Furthermore, AdaSub-ZO incorporates a subspace momentum acceleration mechanism to smooth noisy gradient estimates across evolving subspace bases. Extensive experiments on natural language understanding tasks demonstrate that AdaSub-ZO outperforms existing ZO baselines, substantially reducing gradient estimation variance and accelerating convergence.

---


### 184. [Understanding Unified VLMs: From Attention Probing to Guidance Tuning for Multimodal Generation](https://arxiv.org/abs/2610.15227)

**<font color=#1a73e8>作者：</font>** Zhengyang Luo, Xiaoyu Qiu, Zhiheng Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unified vision-language models (VLMs) perform both text-to-image (T2I) and image-to-text (I2T) generation with one shared Transformer backbone, yet how the backbone processes the condition in either direction remains poorly understood. We study this question from the perspective of conditional guidance: we probe every attention head to show the activation difference between two branches of classifier-free guidance (CFG) with different conditional guidance. On two unified VLMs of autoregressive and masked-diffusion paradigms, the probing reveals a subset of heads that are more sensitive to the change of condition while others are agnostic to it. This characteristic pattern holds in both T2I and I2T generation and is largely stable across data samples, demonstrating the internal mechanism of unified VLMs. Motivated by this, we propose a new inference-time intervention approach for unified multimodal generation, named \textit{HeadTuned-CFG}, which uses the probed condition-change awareness to select and tune the conditional guidance at the attention-head level. Experiments show consistent benefits in both multimodal generation directions of unified VLMs without additional training, and in particular substantial improvements over strong baselines in T2I generation. These results further support the key finding of our probing analysis: the observed pattern of functional specialization is an intrinsic property of unified VLMs.

---


### 185. [Words to World: Benchmarking LLMs in Interactive Physical Environments](https://arxiv.org/abs/2610.15228)

**<font color=#1a73e8>作者：</font>** Xinnan Dai, Kaiqi Yang, Yaxin Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Words are increasingly becoming an interface for action: large language models (LLMs) can now invoke tools, operate devices, and make decisions that affect the physical world. However, current benchmarks largely evaluate LLMs through static text responses, offline tool calls, or simulated tasks, leaving open the question of how well they can act in real physical environments. We present a benchmark for measuring LLMs in closed-loop physical interaction, where models control a harness system connected to real-world components including robotic arms, cameras, and sensors. In each task, the model must issue instructions, receive physical feedback from the environment, interpret the resulting state, and adapt its next action accordingly. This setting evaluates capabilities beyond language understanding, including grounded perception, action planning, tool selection, spatial reasoning, feedback-driven correction, and robustness to execution uncertainty. Through experiments with representative LLMs, we characterize their ability to translate linguistic reasoning into physical actions and identify common failure modes such as hallucinated state changes, poor recovery from unexpected outcomes, and unstable long-horizon plans. Our benchmark aims to provide a systematic foundation for evaluating LLMs as interactive agents that connect words, tools, and the physical world.

---


### 186. [Using Evidence-Centered Design to Guide Prompt Engineering in Measurement: An Illustration with Automated Essay Scoring](https://arxiv.org/abs/2610.15231)

**<font color=#1a73e8>作者：</font>** Jiawei Xiong, Cheng Tang, Hong Jiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) models, particularly large language models (LLMs), are increasingly used in educational settings for tasks such as item generation, automated scoring, and feedback delivery. The quality of these outputs depends not only on the AI model but also on how users construct the prompts that guide model behaviors. Current prompt engineering practices are largely ad hoc, relying on trial and error rather than principled design. This lack of structure introduces validity threats including construct misrepresentation, construct-irrelevant variance, and limited reproducibility. We propose that Evidence-Centered Design (ECD), a framework in educational measurement for structuring valid inferences from observed performance, can serve as a principled foundation for prompt engineering in educational applications. We map the three core ECD models, the student model, the evidence model, and the task model, onto the components of educational prompt design, and describe a workflow for ECD-based prompt engineering. We derive five design principles from this mapping and present an empirical study contrasting ECD-designed prompts with state-of-the-art (SOTA) prompting baselines on an automated scoring task. Our empirical study demonstrates the usefulness of this framework on automated scoring. Results suggest that treating prompting as assessment design rather than informal instructions strengthens the validity, reliability, and fairness of AI-generated educational outputs.

---


### 187. [MoMaTune: Model, Match, Then Tune Language Models for Numerical Records](https://arxiv.org/abs/2610.15235)

**<font color=#1a73e8>作者：</font>** Weimin Lyu, Jingfen Zhang, Lingdao Sha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress in language understanding and generation, decoder language models continue to exhibit striking failures on numerical data. Numerical examples are typically serialized as text by concatenating feature names with their values (e.g., fat:3.4), while conventional task adaptation applies loss only to the downstream prediction target. This leaves two structures weakly supervised: within-value sensitivity, where digit position determines numerical magnitude, because token cross-entropy contains no explicit numerical metric; and across-field structure, where measurements in the same record are statistically dependent, because target-only tuning provides no direct loss on the measurements or their dependencies. We introduce MoMaTune (Model, Match, then Tune), a two-stage post-training strategy organized around these supervision gaps. Stage 1 applies Model, ordinary next-token prediction densely over label-free serialized records, and optionally adds Match, a same-record consistency objective that aligns representations of different partial views of the same example. Stage 2 applies Tune, supervised fine-tuning for downstream target prediction. We evaluate MoMaTune on 169,285 records from eight public datasets, with 339 of 340 input fields numerical. At 1.5B parameters, Model raises the eight-dataset masked-value imputation aggregate from 0.106 to 0.401, while the three-dataset correct-context gain rises from 0.058 to 0.167. On diagnostics, Model also increases sensitivity to numerically consequential digit changes, while Match improves robustness to informative partial views. Adding Tune yields higher target-supervised embedding aggregates for each tested Stage-1 parent, and the two-stage recipes obtain higher aggregate scores than Tune alone. The same pattern is observed at 4B, 9.6B, and 27B parameters when model embeddings are used for downstream prediction.

---


### 188. [ClinEdge: An Expert-Graded Benchmark of Real Patient Edge Cases Where Frontier Multimodal Models Fail](https://arxiv.org/abs/2610.15239)

**<font color=#1a73e8>作者：</font>** Anurag Sharma, Aditya Sharma, Sapna Baalwan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most benchmarks for large language models in medicine are built from licensing examinations and theoretical questions. The few that draw on real clinical data do so only in part, and rarely require a model to read a patient's own imaging. ClinEdge addresses this gap with 32 real, de-identified patient cases from active clinical practice, each evaluated across seven frontier systems for a total of 224 expert-graded evaluations. Each case pairs primary imaging with a short vignette, contains a feature known to defeat pattern-matched reasoning, and is scored against the patient's documented clinical course. The suite is built for depth rather than volume. Grading followed a two-stage expert process. First, a senior orthopaedic surgeon graded all 224 responses on a weighted rubric and a pass-or-fail verdict. Second, a panel of nineteen physicians, largely senior specialists at teaching medical colleges, independently reviewed every case and every one of the 224 grades. All seven production systems were evaluated through their public interfaces, and all 224 conversations are preserved as replayable links.
Performance was poor across all systems, and the failures were shared: different vendors missed the same findings and converged on the same wrong plans. From the experts' notes we catalogue 18 recurring failure modes in five families. The models stop reading an image at the first finding. They give generic plans and lean toward over-treatment. They trust a misleading history over correct imaging. Their answers vary across systems and runs, and change with question format. Failing answers were delivered fluently and without any expressed uncertainty. Four cases are released in full; the remaining 28 are held out, and we invite frontier AI labs and healthcare AI companies to evaluate their models against them (research@futrbridge.com)

---


### 189. [EvolvAttack: Backdooring self Evolving VLM Agents](https://arxiv.org/abs/2610.15244)

**<font color=#1a73e8>作者：</font>** Chuan Zou, Yang Xiang, Zexin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving mechanisms let vision-language model (VLM) agents continually adapt through evolving memory, but they also allow malicious behavior to emerge only after deployment. We introduce a new attack surface, the self-evolving backdoor, whose payload stays dormant in the initial agent and is progressively activated as the agent evolves. Unlike conventional backdoors, which can be exposed by testing triggered inputs on a static model, our attack requires both a visual trigger and a sufficiently evolved memory state; static scanning with clean memory thus yields near-zero attack success and may deem the agent benign. We realize this through memory-aware backdoor training, which couples trigger activation with the agent's evolving memory while preserving benign behavior unless the trigger co-occurs with payload-related memory. Across three VLM backbones, four agent pipelines, and recency-, semantic-, and reward-based memory evolution, the attack preserves normal functionality and stays nearly inactive before evolution (0.5% attack success rate), yet exceeds 95% attack success within 100 interactions, revealing a stealthy threat unique to self-evolving agents.

---


### 190. [ObsSpec: Accelerating Agentic Reinforcement Learning with Observation Speculation](https://arxiv.org/abs/2610.15246)

**<font color=#1a73e8>作者：</font>** Kyle Montgomery, Wang Zhang, Chenguang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-using agents alternate between model generation and tool execution, waiting for each tool call to complete before starting the next generation. This sequential execution is costly during agentic reinforcement learning (RL), which requires large batches of multi-turn rollouts. We introduce ObsSpec, an observation speculation pipeline for agentic RL that uses a small world model to predict tool outputs while the environment executes, allowing the policy to begin its next generation early. ObsSpec retains speculative work only when the predicted and actual observations match exactly, making rollout collection lossless, while co-training keeps the world model up to date as the policy learns. On terminal-use tasks, predictions from a 0.6B world model exactly match actual observations in 66.4% of attempts and arrive roughly 16 times faster. Using these predictions, ObsSpec reduces agent latency by 9.3% and 14.2% for 8B and 32B policies. Across controlled experiments, we characterize the regimes in which ObsSpec reduces agent latency under shared policy resources. Finally, because ObsSpec overlaps policy generation with tool execution, it is architecturally compatible with existing techniques for accelerating RL. Code is available at this https URL.

---


### 191. [Sequent-Prover: Training Agents for Formal, Checkable SMT-based Reasoning](https://arxiv.org/abs/2610.15258)

**<font color=#1a73e8>作者：</font>** Debargha Ganguly, Weicong Chen, Mohsen Hariri 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Sequent-Prover, a family of verifier-using language-model agents, and the post-training framework that produces them. Agents reason in an executable SMT-LIB scratchpad: they write complete SMT-LIB programs, query Z3 across turns, inspect solver feedback, repair formalizations, and terminate with an explicit answer. Our recipe, verifier-conditioned trajectory distillation, bootstraps from a noisy teacher proposal policy by sampling multi-turn trajectories, retaining the successful tail that is correct, non-trivial, grounded, and executable, then applying supervised fine-tuning and trajectory-level preference optimization. Because solver success alone does not guarantee semantic faithfulness, we evaluate task accuracy, k-sample reliability, and SMT program quality. Across 37 benchmarks and 7,254 problems per model family, post-training raises the 4B model's per-attempt accuracy from 85.6% to 97.0% and four-sample all-correct reliability (pass^4}) from 64.1% to 91.7%. It also reduces average SMT calls from 4.10 to 2.52 and tokens per attempt from 18.97k to 12.72k. Sequent-Prover agents give answers backed by executable formal artifacts.

---


### 192. [RECAP: Calibrating Low-Bit Reasoning Models on the History They Read](https://arxiv.org/abs/2610.15259)

**<font color=#1a73e8>作者：</font>** Chi Ruan, Yujie Chen, Zixiang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization reduces the cost of serving reasoning models but can substantially degrade long chains of thought. Each step reads cached keys and values spanning thousands of tokens, allowing quantization errors to accumulate along the trajectory. Standard calibration operates on short segments that omit the earlier context needed by later reasoning steps. Even when this context is retained, cache reconstruction error alone does not capture how quantization errors affect subsequent attention. We present RECAP, a post-training quantization method that calibrates reasoning models on the history they read. Dynamic-prefix calibration separates long historical context from short-block reconstruction. It regenerates prefix keys and values with the current quantizer and rotates the active block to supervise every position along the trajectory. Prefix read geometry further supervises historical cache errors according to their effects on attention outputs, weighting key and value errors asymmetrically. With both components applied only during calibration, RECAP outperforms the baseline across multiple reasoning models and quantization settings. Under W4A4KV4, RECAP improves accuracy over the baseline by 13.3 percentage points on MATH500 with DeepSeek-R1-Distill-Qwen-1.5B and 15.8 points on AIME-120 with Qwen3-4B. These results highlight the importance of preserving historical dependencies during calibration for low-bit reasoning.

---


### 193. [Do correct answers have stable latent knowledge support?](https://arxiv.org/abs/2610.15277)

**<font color=#1a73e8>作者：</font>** Chuancheng Shi, Shangze Li, Wenhua Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are typically evaluated in terms of the correctness of their output. However, output correctness alone does not confirm whether the latent knowledge supporting an answer has stable internal representations. We therefore propose latent state stability (LSS) and knowledge topology stability (KTS) to investigate the stability of individual knowledge states and their relational structure, respectively. Specifically, we first separately average the model's internal representations of the same knowledge under each elicitation condition. Using the mean representation under the baseline condition as a reference, we remove shared shifts to obtain corrected representations. We then formulate LSS as the distance between each corrected representation and its reference representation, normalized against the typical distance between knowledge items of the same type. We formulate KTS as the cross-condition consistency of the ordered pairwise representation distances among knowledge items of the same type. Next, we construct EpiStableBench, which comprises 4,411 items spanning factual knowledge and mathematical reasoning, with 76,766 controlled queries. Across 16 LLMs from four families, representation stability varies substantially even among items answered correctly under the base condition. Within models, higher stability generally corresponds to higher accuracy under held-out elicitation conditions; across models, stability does not consistently increase with model size or overall accuracy. Meanwhile, we present LatentDPO to learn a knowledge-editing policy that accounts for the stability of latent knowledge. Experimental results show that integrating LatentDPO with multiple existing editing methods consistently improves editing success and generalization across different expressions.

---


### 194. [North or South? Diagnosing LLMs' Understanding of North Korean Language, Society, and Knowledge](https://arxiv.org/abs/2610.15282)

**<font color=#1a73e8>作者：</font>** Kiwoong Park, Seyoung Song, Donghyun Woo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have made substantial progress in multilingual question answering, yet their ability to understand low-resource sociolinguistic contexts remains under-explored. We study North Korea as a unique testbed where decades of division have produced distinct differences from South Korea in vocabulary, orthography, norms, and ideological discourse. We introduce LENS (Language and sociocultural Evaluation for North Korean Society), a human-validated benchmark of 1,765 questions evaluating LLMs across three dimensions: linguistic robustness, sociocultural perspective alignment, and domain-specific knowledge. Evaluating diverse recent LLMs, we find a modest performance drop on North Korean language inputs, a larger gap in sociocultural perspective alignment, and severe limitations on domain-specific knowledge. Qualitative analysis reveals that models often conflate formal institutions with lived realities, project liberal-democratic assumptions, or rely on coarse stereotypes. Our results demonstrate that linguistic similarity alone does not guarantee sociocultural or domain-specific understanding, highlighting the critical need for grounded evaluation resources for underrepresented cultural and political contexts.

---


### 195. [OntoAR-HAR: Ontology-Guided Agentic RAG with Personalized Memory for Human Activity Recognition](https://arxiv.org/abs/2610.15292)

**<font color=#1a73e8>作者：</font>** Xiangqing Lu, Tao Zhu, Liang Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs increasingly support sensor-based human activity recognition (HAR) by linking motion signals with activity semantics and physical knowledge. Retrieval-augmented generation (RAG) grounds decisions in sensor examples and domain features, enabling training-free target-user inference with less dependence on raw numerical arrays. However, existing LLM/RAG-based HAR typically searches single-level activity spaces using static population knowledge. Consequently, they compare many unrelated candidates using the same static population evidence and overlook personalized motion patterns. We propose OntoAR-HAR, an ontology-guided agentic RAG framework combining static population and personalized knowledge. Its tree-structured activity ontology decomposes classification into local decisions among semantically related activities. The static store supplies node-constrained examples, while offline-discovered executable signal features provide numerical evidence for local distinctions. During inference, the personalized store collects selected user observations, which the LLM integrates with static knowledge and signal features while traversing the ontology to an activity label. Cross-subject and heterogeneous-sensing experiments show complementary gains from hierarchical retrieval and personalized memory across multiple LLM backbones, achieving state-of-the-art performance. By explicitly modeling hierarchical relations across activity granularities, OntoAR-HAR also addresses the long-overlooked semantic inclusion problem and avoids treating related labels as independent categories.

---


### 196. [CHEAR: Confusion-Hierarchy Evidence-Aware Reasoning for Cost-Efficient Human Activity Recognition](https://arxiv.org/abs/2610.15298)

**<font color=#1a73e8>作者：</font>** Xiangqing Lu, Tao Zhu, Mingxing Nie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer a new approach to wearable-sensor-based human activity recognition. Retrieval-augmented generation (RAG) further introduces similar motion examples and discriminative sensor knowledge, enabling decisions grounded in observations relevant to the current query. More evidence, however, does not necessarily mean better-organized evidence. When online prompts and LLM agents primarily orchestrate inference, decisions about which activities to compare and when to invoke discriminative knowledge remain concentrated at inference time. As the activity vocabulary grows, the model must repeatedly process more candidates and associated knowledge, whereas pruning candidates too early risks excluding the true activity. We propose confusion-hierarchy evidence-aware reasoning (CHEAR), which moves part of this knowledge organization offline. CHEAR constructs and validates an activity hierarchy from recurrent cross-subject retrieval errors and builds corresponding activity-pair knowledge. At inference time, the hierarchy orders candidate comparisons; the LLM retains candidates progressively, and local discriminative knowledge is accessed only for the remaining activities. Across eight datasets, CHEAR achieves 86.79\% mean cross-subject accuracy, a 75.91\% candidate reduction rate, and 96.44\% true-activity retention. Per-sample token use is 85.15\% lower on average than in a variant without the hierarchical structure. Mean accuracy across eight cross-dataset transfer directions is 88.81\%. These results show that organizing candidates and discriminative knowledge around observed activity confusions reduces online LLM input while maintaining recognition performance.

---


### 197. [Accuracy and Uncertainty in Machine Deception Detection (Research White Paper)](https://arxiv.org/abs/2610.15314)

**<font color=#1a73e8>作者：</font>** Heng-Sheng Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A deception detector is only as useful as the trust its alarms deserve. Like a polygraph, detectors that read a language model's internal activations can catch deceptive responses that look honest. Yet current detectors depend on which layers they read, weaken on broader tests, and do not state how certain their alarms are. This white paper proposes the Machine Deception Detector, which targets both detection accuracy and the uncertainty of detector scores. The detector reads every layer of the language model, learns which tokens carry evidence of deception using only response labels, and calibrates its alarm threshold so that its false--positive rate stays below a prescribed level. An ensemble of such detectors measures the uncertainty of each score and raises an alarm only when its members agree, with a confidence level that sets how certain each alarm must be. The proposed evaluation trains on instructed honest and deceptive statements, tests on five unseen deceptive tasks of Liars' Bench read by six Qwen3 models from 0.6B to 32B parameters, and is designed to also show which layers carry the deception feature and how this changes with model size.

---


### 198. [TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation](https://arxiv.org/abs/2610.15324)

**<font color=#1a73e8>作者：</font>** Jiahui Hu, Weile Mo, Peiliang Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion models enable streaming generation of long videos but suffer from significant memory overhead due to the rapidly growing KV cache. Existing KV cache quantization methods are primarily designed for LLMs and transfer poorly to video models, where activations exhibit different statistics and strong spatiotemporal redundancy. We observe that the video KV cache is largely predictable over time, with a clear asymmetry. Keys are highly predictable from their temporal history, while values depend primarily on the current key and need a short history of preceding values. Based on these observations, we propose \textbf{\method}, a training-free predictive KV cache quantization framework for AR video generation. \method predicts keys and values according to their distinct dependencies and stores only the residuals at low precision. Both predictors are lightweight, calibrated once offline by linear regression on a small set of BF16 samples, and remain fixed across prompts and generation runs. Experiments on Self-Forcing, Causal Forcing, and LongCat-Video-13B show that \method consistently achieves higher generation quality than existing KV cache quantization methods at comparable or higher compression ratios, reaching up to $6.71\times$ KV cache compression with the best overall quality--efficiency tradeoff. Our code will be released on GitHub.

---


### 199. [Anchor-and-Harvest Curriculum: A Fully Unmasked Non-LLM Curriculum for Craftax](https://arxiv.org/abs/2610.15328)

**<font color=#1a73e8>作者：</font>** Jiayu Zhu, Luyuan Li, Yuyuan Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Anchor-and-Harvest Curriculum (AHC), a domain-informed, rule-based training system for Craftax-Full. AHC combines achievement-oriented tasks, harvested initial-state progress, difficulty adaptation, bounded selection, and original-task practice. It uses no LLM inference and keeps all 43 actions available. At 2,005,401,600 PPO rollout transitions, three primary AHC runs obtain native-task return $46.70\pm0.57$ (sample SD), compared with $41.91\pm1.01$ for fresh native PPO-GTrXL with the same student architecture and evaluation protocol. Evaluation uses ten stochastic rollouts on each of 1024 fixed worlds per model. An additional cohort of three AHC runs reaches $46.08\pm1.23$. Two single-component ablations retain similar mean returns, while jointly freezing difficulty and removing inherited progress gives $45.14\pm2.79$. All-67-achievement profiles show that most of the return difference comes from Intermediate achievements, while the deepest-floor achievements remain unsolved. A Skill-Preflight diagnosis with a 14B teacher shows how prerequisite and floor-access constraints restrict practice. AHC and three 14B diagnostic configurations reach aggregate returns near the reported 80B DiCode mean of 45.88 and below the 235B mean of 48.55. These results show that an explicit curriculum without LLM inference can reach returns comparable to those reported for LLM-generated curricula on Craftax-Full, without action masking.

---


### 200. [ZOIF: Zeroth-Order Influence Function Estimation for LLM Data Selection Using Only Forward Passes](https://arxiv.org/abs/2610.15336)

**<font color=#1a73e8>作者：</font>** Lisong He, Yunxuan Jiang, Haishan Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Influence functions enable principled data selection for large language models (e.g., identifying influential training samples for model editing, debugging, or efficient fine-tuning). However, scaling IFs to LLMs is hindered by the intractability of billion-scale Hessian matrices and the prohibitive memory overhead of backpropagation (BP). While many classical IF approximations reduce Hessian complexity, they still rely on BP for gradient computation, requiring massive storage for intermediate activations that impedes practical data selection at scale. To address this, we propose ZOIF, a zeroth-order framework for influence estimation that operates entirely via forward passes, enabling memory-efficient data selection under resource constraints. ZOIF decomposes influence estimation into three BP-free stages: (1) approximating the average proxy gradient via zeroth-order estimation; (2) reformulating and solving the inverse Hessian-vector product as an auxiliary zeroth-order optimization to bypass explicit inversion; and (3) deriving per-sample influence scores via a forward finite difference along the previously computed parameter update direction. Experiments show that ZOIF selects data subsets with downstream utility competitive with, and in some cases exceeding, the evaluated baselines, yet at substantially lower peak memory cost and with comparable overall computation time.

---


> [!TIP]
> 当前位于：**151-200**（第 4/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
