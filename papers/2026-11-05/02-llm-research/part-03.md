# 🧠 大模型相关研究 | 2026年11月05日

> 本类共 **220** 篇论文：已确认 **208** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-220](./part-05.md)

---

### 101. [ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems](https://arxiv.org/abs/2611.04321)

**<font color=#1a73e8>作者：</font>** Maisha Maliha, Vishal Pramanik, Sumit Kumar Jha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a locally reasonable message that exercises authority belonging to another role: a verifier that begins planning, a retriever that asserts unsupported conclusions, an executor that changes state no one approved. We formalize this as role drift, a turn-level breach of an agent's role contract. We introduce Agent Trajectory Control (ATC), which makes each role's authority explicit as a contract and enforces it at the point where a message would enter the shared conversation. ATC scores a proposed output for out-of-role deviation, leakage into the functions of other roles, impermissible speech acts, and logical contract breaches, then computes a leakage-regularized target that constrains regeneration; the revised message is re-checked before admission. Enforcement acts on the message rather than the generator, so ATC governs agents whose internal representations are unavailable. Across homogeneous and heterogeneous teams, ATC improves task performance and role consistency while lowering role-drift energy relative to strong baselines spanning prompting, memory, workflow control, and activation editing, with the largest gains under explicit role-confusion stress tests and in larger, more diverse teams.

---


### 102. [FP4Quant: Efficient 4-Bit Communication Compression for Model-Parallel LLM Training](https://arxiv.org/abs/2611.04323)

**<font color=#1a73e8>作者：</font>** Man Liu, Xingchen Liu, Hairui Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid scaling of large language models (LLMs) has made communication overhead a critical bottleneck in distributed model-parallel training. Although existing low-precision compression methods can effectively reduce communication costs, further reducing the communication footprint to ultra-low-bit formats such as FP4 introduces new challenges, including limited numerical range, sub-byte storage overhead, and increased computational cost from fine-grained quantization. In this paper, we present \textbf{FP4Quant}, a micro-grouped FP4 compression framework for efficient model-parallel LLM training. FP4Quant integrates a micro-grouped dual-scale FP4 quantization mechanism to preserve local tensor distribution characteristics, a warp-cooperative FP4 packing scheme to enable efficient sub-byte data representation, and a hybrid two-level FWHT pipeline to mitigate quantization errors with GPU-aware execution optimization. Experiments on NVIDIA H100 GPUs with Qwen-7B demonstrate up to 1.56$\times$ end-to-end throughput improvement over BF16, revealing a trade-off between throughput and model quality.

---


### 103. [Anchor: Augmented Cross-Layer Recurrent State for Long-Context Retrieval in Test-Time Training](https://arxiv.org/abs/2611.04327)

**<font color=#1a73e8>作者：</font>** Vimal William, Yuanzhe Li, Danella Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient linearization turns a pretrained autoregressive Transformer into an efficient model by hybridizing sliding-window attention (SWA) with a constant-size recurrent memory. But does every layer's recurrent state contribute to long-context retrieval? Investigating an SWA and Test-Time Training (TTT) hybrid, we find that retrieval is sparse across depth, concentrated in a few anchor layers, and that the remaining states hold similar information expressed through layer-specific transformations. We exploit both observations in Anchor: TTT memory placed only at the anchor layers, and a cross-layer recurrent state written once and read by many layers, each through its own learned read map that realizes a layer-specific stretch and rotation, along with demonstrated generalization to other hybrid attentions. On Llama-3.1-8B and Mistral-7B, Anchor delivers 2.3-3.1x higher recall and 6.7-8.9 points higher MMLU accuracy than LoLCATs with a 10x smaller recurrent state, retains 91-95% of the teacher's MMLU accuracy, and cuts end-to-end latency by up to 4.3x relative to softmax attention.

---


### 104. [Patching the Protocol: A Taxonomy of Pre-Registration Repairs in LLM-Proposer Experiments](https://arxiv.org/abs/2611.04338)

**<font color=#1a73e8>作者：</font>** Peter Chen, Ni Zhang, Siyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-registration is increasingly proposed as a trust mechanism for machine-learning research involving LLM-generated content, but its canonical form assumes a frozen protocol can be executed unchanged. Software-intensive studies violate this assumption: the protocol is partly implemented, and implementations carry defects. We report a three-case study of protocol repairs ("patches") from a program where an LLM proposes executable rules that a programmatic verifier gates, across production scheduling, incentive design, and task assignment. Each protocol required exactly one defect-repair patch: three events in total. None modified a numbered judgment criterion, its threshold, or the scoring rule, and none altered already collected data; two changed pre-registered design parameters before any data were collected, each with a recorded rationale. We propose a two-axis taxonomy of patches (defect class: environmental / feasibility / correctness, x timing: pre-data / post-data), introduce a verifiable non-impact claim for post-data repairs, and distill a nine-item checklist; all nine items were exercised by at least one patch event -- an observation of use, not a validation of sufficiency. The credibility of verifier-bound, LLM-proposer studies depends less on whether patches occur than on whether they are auditable.

---


### 105. [Beyond Fine-Tuning: Evaluating Prompt Engineering and Prompt Tuning for Roman Urdu Hate Speech Detection](https://arxiv.org/abs/2611.04342)

**<font color=#1a73e8>作者：</font>** Toneema Zubair, Muhammad Junaid Asif, Faisal Kamiran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low Resource Languages (LRLs) pose significant challenges for hate speech detection because of a scarcity of readily available annotated data, language variation, non-standard spelling, and context-dependent ambiguity. Beyond the problem of informal conventions of writing in Roman Urdu, there is also the issue of code-mixing. After working on the previous project about zero-shot learning and parameter-efficient fine-tuning (PEFT), this research systematically compares prompt engineering and prompt tuning for Roman Urdu hate speech detection. To study the effect of in-context examples, we will compare the zero-shot and few-shot prompting approaches. To understand the advantage of structured prompting and learnable prompt representations, we will conduct studies of manual vs. mixed prompt-based adaptation strategies. Experimentations are carried out on the PURUT dataset (~72,771 social media comments) with GPT-3.5, LLaMA-3, Mistral-7B, and multilingual BERT in several settings. Experimental results show that few-shot prompting always outperforms zero-shot prompting, with the Mistral-7B model scoring 0.67 F1 compared to 0.56 of the zero-shot models. Based on this observation, prompt-based adaptation is proposed to introduce additional improvements, with the proposed mixed prompt configuration able to yield a F1-score up to 0.87 which further surpasses the performance of regular manual prompts. Despite the larger size of the model, its performance trade-off between inference-based prompting, prompt optimization, and parameter-efficient model adaptation is compared to the previously reported PEFT-based F1-score, which is ~0.93.

---


### 106. [Sparse Internal Control of Language Models](https://arxiv.org/abs/2611.04349)

**<font color=#1a73e8>作者：</font>** Xizhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used in text generation, decision support, and automated interaction, creating a need for localized, reversible, and selective control of their behavior. Activation steering demonstrates that internal interventions can alter the behavior of frozen models, but how to select and evaluate compact, multi-site control interfaces remains an open question. I introduce sparse internal control, a framework for steering target behavior by applying inference-time interventions to a small set of internal model nodes. A local target-controllability formulation characterizes candidate site--direction pairs by their behavioral effects and specifies constraints on target recovery, off-target preservation, and intervention energy. Two complementary selectors instantiate this formulation: Driver-OMP selects nodes for sparse reconstruction of a desired behavioral displacement, while Coverage-Driver favors stable coverage across prompts. I propose a six-axis control-evaluation protocol measuring reachability, signed reversal, dose response, feedback controllability, off-target preservation, and held-out reuse. Exploratory experiments on indirect object identification, MMLU multiple-choice question answering, sentiment steering, and refusal steering provide evidence for the feasibility of steering task-defined behavior through sparse internal interventions. The six-axis evaluation characterizes these interventions beyond target movement, revealing distinct control properties that depend on the task and available direction information. Together, the formulation, reference algorithms, and evaluation protocol provide a foundation for the systematic study and development of internal control methods for language models.

---


### 107. [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](https://arxiv.org/abs/2611.04356)

**<font color=#1a73e8>作者：</font>** Li Zheng, Simin Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Finite element method (FEM) solvers are foundational to scientific and engineering simulation, yet their susceptibility to \emph{efficiency attacks} remains largely unexplored. An adversary can craft syntactically valid and runnable FEM programs that complete successfully while forcing excessive computational work, enabling computational denial-of-service (DoS) attacks. Finding such inputs is challenging because FEM programs occupy a vast, structured space constrained by numerical, geometric, and constitutive requirements. We introduce CloakFEM, a domain-guided LLM-agent framework for automatically generating runnable adversarial FEM programs that amplify solver computation. CloakFEM combines LLM-guided search with an FEM-specific intermediate representation and a deterministic validity gate that enforces runnable constraints. Across three FEM stacks, 17 problem classes, and 1,068 seeds, CloakFEM discovers adversarial inputs that substantially amplify solver work while remaining valid and solvable. In the most extreme case, solver iterations increase from 43 to 247,367, a \(5{,}752.72\times\) amplification. CloakFEM outperforms five generic black-box baselines and retains an advantage over evolutionary search under a controlled bounded action space. Cross-solver analysis further reveals both problem-intrinsic and solver-specific sources of vulnerability. Our results uncover an underexplored efficiency-attack surface in FEM solvers and show that runnable FEM programs can serve as adversarial inputs.

---


### 108. [Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs](https://arxiv.org/abs/2611.04376)

**<font color=#1a73e8>作者：</font>** Hei Yi Mak, Hoang Le, Mehran Taghian Jazi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models. Recent work on FP4 RL has introduced effective recovery recipes that restore accuracy under aggressive low-precision quantization for dense models, but we find that the same approach yields no improvement over the naive FP4 baseline in the MoE setting. We conduct an in-depth study to understand why. Our analysis identifies the root cause in the routing mechanism unique to MoE: because the router makes discrete expert-selection decisions, training-inference policy alignment becomes acutely sensitive to whether the same recovery technique is applied symmetrically on the training and inference sides. When an asymmetric recipe is used-including the dense-model approach, which corrects only the rollout-training-inference alignment deteriorates sharply, as measured by the Pearson correlation coefficient between training and inference probabilities, and router selection matching rates. Building on this finding, we propose MoeResQ, a quantization-recovery recipe for MoE RL post-training that enforces symmetry between the training- and inference-side corrections. MoeResQ restores training-inference alignment and substantially closes the accuracy gap to full precision, establishing symmetric recovery as the key principle in FP4 RL for MoE models.

---


### 109. [Twice as Fast, Until It Isn't: Quantized Serving of Mid-Size Open LLMs](https://arxiv.org/abs/2611.04380)

**<font color=#1a73e8>作者：</font>** Smit Kadvani, Kriti Faujdar, Spurthi Tallam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A team serving a 9B-20B open-weight language model on vLLM or SGLang must choose a quantization recipe, and needs two numbers: the speedup over BF16 and the accuracy given up. We assemble every public measurement of these numbers that we could verify and find that the record supplies them only in pieces. Only two checkpoints, both INT4 builds of Gemma 3 12B, have both a vLLM timing and an accuracy score, and that score covers a single MMLU subject, one that the AWQ build was calibrated on. The batch-1 timings predate current engine releases, AMD and Intel Gaudi have no timing in this band at all, and FP4 has none against BF16. The timings that do exist follow one rule. Decoding a small batch is limited by memory bandwidth, so 4-bit weights roughly double speed (2.12x for Qwen2.5-14B on an A100), but the gain vanishes once a large batch makes the GPU compute-bound (1.02x for Gemma 3 12B at batch size 256), where FP8 is the recipe that can still help. Many published accuracy deltas, including every HumanEval delta, lie within benchmark sampling noise. We close with a seven-item reporting checklist for future measurements.

---


### 110. [StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models](https://arxiv.org/abs/2611.04386)

**<font color=#1a73e8>作者：</font>** Chenru Wang, Xuanyang Zhang, Yucheng Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A deployable text-to-image diffusion model must hold several capabilities at once, such as instruction following, text rendering and human preference, and must sample in a few steps. Capabilities and few-step sampling are built in separate stages: a full-step model first consolidates capabilities through multi-teacher on-policy distillation, then serves as a fixed teacher for step distillation. Every full-step model we evaluate scores lower once compressed, and the second stage cannot begin until the first finishes. We introduce StepX-OPD, which merges the two stages: one student acquires every capability while learning to sample in a few steps, so frozen specialists supervise it on the states its own rollout visits rather than on a longer trajectory it never runs. Because a decomposition of the rollout's KL weights velocity mismatch most heavily near the clean end, we also regress the student's velocity on the low-noise part of the rollout. Separately, we find that capability integration makes models write prompt words into images on prompts that never asked for text, and we give a variant that lowers it. We evaluate on SD3.5-Medium and FLUX.1-dev across instruction following, text rendering, image quality and human preference. On both architectures, StepX-OPD attains the highest normalized average score among the four-step methods compared and exceeds the forty-step Flow-OPD model, and on SD3.5-Medium it trains with about 37% fewer GPU-hours than sequential DiffusionOPD followed by step distillation.

---


### 111. [Do Multi-Turn Conversational Capabilities Carry Over from Text to Speech? A Parallel Multilingual Benchmark](https://arxiv.org/abs/2611.04390)

**<font color=#1a73e8>作者：</font>** Jiaming Zhou, Pei Zhang, Shiwan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Successful multi-turn voice interaction requires models to retain information from earlier turns, follow persistent instructions, and track revisions to conversational state. These abilities are usually evaluated from transcripts, leaving open whether successes demonstrated from text carry over when the same turns are spoken, and whether this transfer is consistent across languages. We introduce Omnilingua-AudioMC, a strictly parallel multilingual extension of Audio MultiChallenge, to study this question. The benchmark contains 354 conversations and 1,404 rubric items across ten languages, with content, turn structure, cross-turn dependencies, and evaluation criteria aligned across transcript and speech conditions. Across six speech-language models, the shift from reference transcripts to direct speech input is strongly model- and language-dependent: models with similar transcript performance can diverge substantially under speech, and their relative strengths across languages can change. Paired rubric-level analysis shows that aggregate transcript-speech gaps can obscure which conversational requirements are preserved, because losses of transcript-demonstrated successes can be offset by gains on other items. Replacing preceding user turns, the current turn, or both with model-generated transcripts localizes recoverable degradation: for the two models with the largest gaps, history substitution yields a larger macro-level improvement than current-turn substitution in all ten languages, while the strongest direct-speech model gains little from either. These results show that transcript performance is an unreliable proxy for multilingual spoken conversational ability and identify the representation of preceding spoken context as an important source of recoverable degradation. Our code is publicly available at this https URL.

---


### 112. [Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](https://arxiv.org/abs/2611.04391)

**<font color=#1a73e8>作者：</font>** Junhyeong Park, Wook Jung, Taeyoung Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on robot data. We introduce H2RB (Human-To-Robot Bridge), a human-robot co-training framework for adapting pretrained VLA policies from unpaired human and robot demonstrations. H2RB bridges the embodiment gap at both interfaces: geometry-anchored alignment grounds human and robot observations in a compatible representation, while a decoupled-decoder tokenizer shares action latents without forcing both domains through a single action mapping. This design allows human demonstrations to provide useful behavioral supervision while retaining the rich visual, semantic, and control priors of the pretrained VLA. Across real-world tasks, H2RB substantially improves object transfer performance from 8.0 to 51.8 and enables skill transfer to score 62.7, in settings where co-train baselines totally fail to transfer human-demonstrated skills. The benefit also persists under object-placement shifts, improving out-of-distribution transfer from 6.0 to 45.3. H2RB suggests a way for human demonstrations to serve as a scalable supervision source for adapting pretrained robotic policies, reducing the dependence on costly target-robot data collection.

---


### 113. [Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents](https://arxiv.org/abs/2611.04393)

**<font color=#1a73e8>作者：</font>** Ilan Zendel, Matan Levy, Stav Cohen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act on information retrieved from public sources they treat as credible, which turns a manipulated recommendation into a transaction, a dependency, or a decision with physical consequences. The security literature models this threat as instruction injection, in which an adversary writes a command into retrieved content and deployed defenses learn to recognize command syntax. We show that an attacker can instead steer an agent through the agent's own harm-avoidance. A single fabricated hazard, written as an ordinary review, leads the agent to disqualify the legitimate options and select the attacker's target by its own reasoning, with no command for a detector to recognize. We call this voluntary servitude. These payloads steer agents about as often as instruction injection (60.4% vs. 66.0%), and deployed injection detectors score them as benign, so behind a filter they are 1.7-4.4x more effective. We measure this at the generation stage across six models and ten consumer-service domains, for three attack families, and show that it transfers to production browser agents, outperforming instruction injection, and to a retrieval pipeline (1.0-57.0% end-to-end success, depending on the retriever). We then show that a corroboration requirement added to the agent's instructions removes roughly 95% of the exposure against a non-adaptive attacker without retraining. With the requirement in place, the agent still reads the planted hazard and no longer acts on it.

---


### 114. [Correct Labels Are Not Enough: Reliable Metadata Can Silently Control Model Behavior](https://arxiv.org/abs/2611.04395)

**<font color=#1a73e8>作者：</font>** Renee Jia, Jinzhou Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning data can include metadata that predicts the correct answer, such as a reward-model score or a quality label. We ask whether a model learns to rely on this metadata even when every training label is correct. We fine-tune 7-9B open-weight models from three families on multiple-choice questions in which (Reward: 5) always marks the correct option; when this annotation is moved to a wrong option at test time, models select that option on 97-100% of CommonsenseQA items. Removing it leaves most answers correct, so evaluation without it misses the dependence. Cue-following rises sharply with training-time reliability and develops even with neutral or nonsense annotation words, although test-time wording affects its strength. A Qwen3 experiment also finds cue dependence in option-letter scores after direct preference optimization. Audits can test for this dependence by moving or removing visible annotations while holding the task and correct answer fixed.

---


### 115. [The Min-Max theory of language behavior](https://arxiv.org/abs/2611.04406)

**<font color=#1a73e8>作者：</font>** Hiram Ring  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The "Min-Max" theory of language behavior proposes that humans engage simultaneously in minimization of processing effort and maximization of information content, and that this is a primary driver in language evolution (Ring, 2025). This claim seeks to unify observations from language processing (Mahowald et al., 2013; Futrell et al., 2015; Yadav et al., 2020; Hawkins, 2014), interaction (Hörberg and Sjons, 2023; Tucker et al., 2025; Jaeger and Tily, 2011; Smith and Culbertson, 2025), and corpora (Levshina and Moran, 2021; Levshina, 2023; Newmeyer, 2017), which suggest that considerations of processing efficiency and information content are both implicated in human communication. The interaction between these two processes provides an explanation for human linguistic behavior at various levels (Linders and Louwerse, 2023) and predicts historical developments in language, i.e. related to word order (Ring, 2025). Given that the original formulation of the Min-Max theory is based on observational data, the current paper seeks to validate the theory mathematically. Through a series of experiments that use computational models to investigate the theory's predictions, pretrained and iterated learning models are queried with synthetic data. The experiments show that manipulating the variables of token length and the weight of information content in a tabula rasa model results in word order change, as predicted by the theory. The experiments also identify important differences between computational models and observations of human language data, suggesting that current transformer-based language models may not accurately represent psycholinguistic processes. The overall findings indicate that evolutionary trajectories in language are highly susceptible to minimization of processing and maximization of information content.

---


### 116. [TxBench: A Benchmark of Attack Transactions and Evidence-Backed Negatives on Seven EVM Chains](https://arxiv.org/abs/2611.04411)

**<font color=#1a73e8>作者：</font>** Tamer Abdelaziz, karim Ali  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Researchers evaluate detectors of malicious smart-contract transactions on datasets that each paper assembles anew. Their positives come from incident trackers, whose citations mix attacks with setup steps and transactions that never ran, or from a detector's own output, which makes the evaluation circular; their negatives are ordinary transactions. A shared benchmark needs positives whose own execution shows the attack and negatives that use the attacks' mechanisms, with no detector deciding either label.
We present TxBench, a benchmark of attack transactions and evidence-backed negatives on seven EVM chains, with the five-step pipeline that builds it. The pipeline collects every transaction that BlockSec's incident library or the EVM Hack Registry cites, maps its weakness to OWASP's SCWE taxonomy, and rebuilds its execution from free data sources. A cited transaction qualifies as a valid TxBench attack only if it extracts value from others during execution, is consistent with all verified source claims, and is independently linked to the reported incident by corroborating evidence. Negative examples are sampled from each chain's traffic near the attacks and retained only when positive evidence confirms their legitimacy.
Of 1,850 cited transactions, TxBench accepts 1,012 attacks from 602 incidents, worth USD 868.1 million: 846 contract exploits and 166 key compromises. A blind review under rules fixed in advance confirms 98 of 100 sampled attacks (97.7% weighted) and all 100 sampled negatives. As baselines, four zero-shot LLMs reading anonymized traces are precise but find at most 0.43 of the attacks and no key compromise, leaving ample room for better detectors.

---


### 117. [Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition](https://arxiv.org/abs/2611.04420)

**<font color=#1a73e8>作者：</font>** Peter Chen, Ni Zhang, Siyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated research pipelines pair an LLM proposer with a verifier on an implicit bet: discovery quality rises with verification strength. Under a pre-registered protocol we test this bet in two real-data domains -- job-shop scheduling and vehicular edge offloading on Beijing T-Drive trajectories -- across 100 matched LLM/random pairs per domain and three verifier tiers. The manipulation binds -- a 429-case mutation battery shows scores rising across tiers -- yet the paired LLM-over-random advantage does not scale with it (A, one-sided p=0.1115; D, p=0.9994), and in D shrinks under the strict tier (margin contrast -0.040, p=0.0013). The two lower gates promote identical candidates in 100/100 and 99/100 pairs, so the strict order is untestable when they coincide. Constructively, LLM proposals carry a real paired advantage over random controls, but a post-hoc union-pool analysis shows the fastest path to better discovery is widening the pool, not tightening the gate: mixing the two pools adds +1.52 holdout-value units in domain A (one-sided Wilcoxon, n=100, p=0.0002) -- evidence that pool composition, not verification strength, is the lever. Criteria, ledgers and scripts are archived on Zenodo (DOI: https://doi.org/10.5281/zenodo.23308866).

---


### 118. [Typological Feature Induction as a Benchmark for Inductive Metalinguistic Reasoning](https://arxiv.org/abs/2611.04421)

**<font color=#1a73e8>作者：</font>** Chen Zhang, Seth Aycock, Yusuke Miyao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing metalinguistic reasoning benchmarks require both inference of rules and their application, making failures hard to diagnose. We introduce typological feature induction (TFI) which targets the former step. Given sentences in an unnamed language paired with translations in a known pivot language, models must predict a typological feature of the unnamed language. From Grambank and multi-parallel corpora, we automatically build evaluation questions over 195 languages. We find that LLMs identify 59--80% of these languages from only 16 sentence pairs; and misaligning the translations barely affects their accuracy, suggesting reliance on prior knowledge of the language. Enciphering text to prevent recognition increases the corpus' utility, but mainly for features where target and pivot languages agree. On languages which models cannot identify, neither open model outperforms a majority-value baseline. Since induction from raw text aligns with field linguists' use-case, this work indicates the models tested are not yet ready for this role. TFI offers a scalable path to track progress in this direction.

---


### 119. [Sketchpad: certified exact arithmetic with a small vision-language model](https://arxiv.org/abs/2611.04434)

**<font color=#1a73e8>作者：</font>** Mostafa 'Neo' Mohsenvand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are accurate on most long-arithmetic problems, but their accuracy is estimated on samples and carries no guarantee for an unseen input; tool use is exact but moves the computation outside the network. We show that exactness at all input lengths becomes a finite, checkable property of a network when each of its steps reads only a bounded view of an external working memory. In Sketchpad, Qwen3.5-0.8B with a low-rank adapter executes arithmetic procedures on a rendered sheet. Each forward pass reads a three-cell view and emits one step: a digit, a carry or borrow, and the next operation. A fixed runtime moves the view and writes no digit of a result. We prove in Lean that the model is then exact on all inputs of any length if and only if it is exact on the finite set of views the runtime presents, that no finite test suffices when steps also read earlier steps, and that the guarantee tolerates bounded numerical perturbation and extends to compositions of procedures. All 2,446 views pass on the deployment device, a laptop GPU running the model in a web browser. The certified model performs signed addition and subtraction, long multiplication and division, square roots and greatest common divisors at arbitrary length. It solved 200 of 200 pre-registered problems in the browser, and 220 of 220 sums of up to 1,000 digits and products of up to 20 digits, of which GPT-6.1 Sol, the strongest of ten other models, solved 217. A symbolic runtime built on these procedures solves, expands and factors polynomials with every number computed by the model, and a multiplicative gate on the adapter recovers the base model exactly when the sheet is not in use.

---


### 120. [Entropy-Gated Dynamic Rectification for Object Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2611.04438)

**<font color=#1a73e8>作者：</font>** Riasad Alvi, Md. Asaduzzaman Shuvo, Md. Ahashan Habib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) routinely name objects that are absent from the image. Latent steering can reduce this failure in one model forward pass, but a fixed gate treats early and late decoding steps by the same criterion. We observe that predictive entropy varies sharply within free-running generation, while states that commit to short answers occupy a narrow, confident band. We exploit this temporal mismatch by using uncertainty as a causally available, token-local control signal for an existing steering gate. We propose Entropy-Gated Dynamic Rectification (EGDR), which lowers the intervention threshold when entropy derived from the preceding step's already available logits is high and retains the calibrated operating point when it is low. On LLaVA-1.5-7B, the underlying static gate lowers CHAIR CS/CI from 53.00/15.30 to 32.00/14.30; replacing only its constant threshold with EGDR further lowers them to 29.00/13.60. At a matched 58% intervention rate, the corresponding static control obtains 30.50/14.00. The gain over the static gate holds on LLaVA-NeXT-7B and grows with the generation budget, while POPE scores and general multimodal capability remain effectively unchanged. EGDR requires no additional model forward pass and adds roughly 2% measured latency. Our code is available at this https URL.

---


### 121. [Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models](https://arxiv.org/abs/2611.04449)

**<font color=#1a73e8>作者：</font>** Xin Liu, Boyuan Sun, Yuxin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Among 291 surveyed open-weight language model repositories (280 distinct embedding tables), 52.6% of untied gated and hybrid checkpoints (20/38) contain reachable input embeddings with norms below $10^{-6}$, compared with 0% of weight-tied models. Such near-zero rows can arise during pretraining when unseen rare or template tokens receive zero input gradients while AdamW weight decay shrinks untied embeddings. In tested Transformer configurations, non-initial positions or a BOS token prevent this failure mode. In gated sequence models (Mamba, Gated DeltaNet, xLSTM), a near-zero token can amplify input-embedding gradients by more than 30 orders of magnitude (up to 35). At zero input, current-token readout factors (SiLU gates or linear queries) vanish, suppressing historical-state readout. Residual RMS values can then fall below the square root of the RMSNorm floor across consecutive layers, causing Pre-RMSNorm to amplify backward gradients by up to $10^3$ per layer. When a gradient entry exceeds $1.84 \times 10^{19}$, FP32 global-norm clipping in PyTorch, Hugging Face Trainer, and FSDP2 can overflow to infinity and zero the current batch's gradients. In Telugu continual pretraining of Nemotron-3-Nano-4B, this discards updates on approximately 20% of steps and leaves triggered rows frozen. We propose two remedies. For released checkpoints, GroupClip decouples input-embedding clipping using a 64-bit or rescaled norm; its rescaled implementation eliminates update loss and heals triggered rows in one step with negligible measured end-to-end overhead. For pretraining, GateFloor ($\mathrm{SiLU}(z) + \delta$, $\delta \in [0.01, 0.1]$) keeps the gate positive at zero input, reducing near-zero gradients by 28 orders of magnitude in experiments up to 370M parameters, with perplexity comparable to the baseline.

---


### 122. [Large Language Model-Assisted Adaptive Heuristic Search for Agile Earth Observation Satellite Scheduling](https://arxiv.org/abs/2611.04458)

**<font color=#1a73e8>作者：</font>** He Wang, Yeye Liu, Ruijie Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agile Earth observation satellites must coordinate imaging tasks within limited observation windows, while accounting for attitude maneuvering and onboard energy constraints. Competition among observation opportunities makes scheduling performance sensitive to the heuristic rules used for task selection. This letter proposes a large language model (LLM)-assisted adaptive heuristic search method for agile Earth observation satellite scheduling. The LLM generates an initial heuristic rule according to the characteristics of the scheduling instance. During the subsequent ant colony search, search performance and scheduling information are fed back to the LLM to refine the heuristic rule. The proposed modifications are evaluated through paired solution constructions before being incorporated into the search process. A unified scheduling procedure determines task selection, satellite assignment, and observation timing under the operational constraints. Experiments on six scheduling scenarios involving 50--200 imaging tasks demonstrate that the proposed method achieves 4.3\%--9.6\% higher mean observation benefit than the strongest baseline.

---


### 123. [Theoretical Analysis of Muon on Transformers for Next-Token Prediction](https://arxiv.org/abs/2611.04465)

**<font color=#1a73e8>作者：</font>** Shengwei Wu, Yixuan Yang, Gao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently shown strong empirical performance in training Transformer-based large language models (LLMs), yet its optimization dynamics remain poorly understood from a theoretical perspective. In this paper, we analyze the training dynamics of Muon for next-token prediction (NTP) in Transformers. The training procedure consists of two phases: the preprocessing phase learns the output-value component, while the main phase learns the key-query component. For the preprocessing phase, we characterize the optimization trajectory exactly and show that the normalized spectral margin is optimal after each update. For the main phase, we establish nonasymptotic convergence rates for the training loss and the normalized margin gap under softmax attention. These results suggest that Muon's update rule can help models efficiently learn which tokens matter for prediction, offering a possible explanation for its strong performance in large language model training. The learned weight structure also yields a generalization guarantee for unseen contexts. Furthermore, we validate our theoretical insights with experiments on next-token prediction tasks.

---


### 124. [From Watching to Steering: Enabling Human-Coding Agent Collaboration through Execution Traces](https://arxiv.org/abs/2611.04466)

**<font color=#1a73e8>作者：</font>** Xiaoke Yan, Jiaying Lei, Danqing Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled coding agents to autonomously perform complex software development tasks, yet their long-running execution remains difficult for users to inspect, understand, and steer. We present Vibetrace, an interactive trace visualization and intervention system for agentic programming built upon OpenCode. Vibetrace introduces a human-agent collaboration paradigm of Observe, Understand, Intervene, and Evolve. It (1) visualizes agent workflows as interactive execution traces for inspecting actions, intermediate states, and failures; (2) enables users to fork execution from prior steps and provide targeted corrections without restarting validated progress; and (3) distills traces and human feedback into reusable skills for continual agent evolution. On SWE-bench Verified, distilled skills reduce input tokens by 23.0% and cost by 15.5%, while improving pass rate from 65.0% to 68.0%. User studies further demonstrate improved accuracy and efficiency over conventional log-based interaction.

---


### 125. [Beyond Token Representations: Explicit Visual Object Grounding for Video Reasoning Segmentation](https://arxiv.org/abs/2611.04472)

**<font color=#1a73e8>作者：</font>** Jun Huang, Junyang Zhang, Zijie Yue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Reasoning Segmentation (VRS) aims to infer and segment target objects specified by reasoning queries in videos. Existing methods typically first infer the target and generate a few segmentation tokens for it, which are then fed into a mask decoder for mask prediction. However, such segmentation tokens tend to be both semantically monotonous and spatially ambiguous, making them largely insufficient to represent the target to guide mask prediction. In this paper, we propose an explicit visual object grounding framework for VRS. Specifically, we first propose a spatial-aware prompt generation and refinement scheme, in which we query a multimodal large language model to generate explicit spatial prompts (i.e., bounding box and point set) for the target and then refine them through multi-step dialogue. Furthermore, we introduce a query diversification and alignment module to generate auxiliary queries that describe the same target from different perspectives. We then enforce cross-query consistency between their predicted spatial prompts to alleviate the training bias caused by query limitations. Finally, we select several reliable frames using a prompt-based keyframe selection strategy to support mask decoding and propagation. Extensive experiments on eight datasets demonstrate that our method significantly outperforms state-of-the-art methods. The code is available at this https URL.

---


### 126. [Treating the Symptom, Missing the Cause: Anatomy of a Scientific Reasoning Failure](https://arxiv.org/abs/2611.04473)

**<font color=#1a73e8>作者：</font>** Anna Gogleva, Thomas Charman, Martin Balla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents can find interventions that work without understanding why they do. We study this failure mode in controlled synthetic regulatory systems, where agents must experimentally identify a hidden fault and rescue the resulting phenotype. Across seven LLMs, every model restores the healthy phenotypes more often than it identifies the fault. Claude Opus 4.6 and Sonnet 4.6 rescue every organism while diagnosing only 55% and 35% of them. This failure is not simply due to insufficient exploration or unavailable evidence. In most cases, the cause is experimentally identifiable, and agents encounter evidence that distinguishes competing causes in 91% of relevant sessions, and still frequently misdiagnose the system.
Targeted probes reveal where experimental reasoning breaks down. Models reliably interpret decisive evidence and revise hypotheses when the causal comparison is explicit, and can locate that evidence within a full experimental record. However, they struggle to predict the outcome of the experiment under each competing cause, a necessary step in using the observed result to distinguish between them. Agents can therefore gather the right evidence and still infer the wrong cause. As AI systems take on a growing role in synthesising scientific evidence, these findings highlight the need to evaluate how they use evidence to reach causal conclusions, alongside whether their interventions succeed.

---


### 127. [ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models](https://arxiv.org/abs/2611.04480)

**<font color=#1a73e8>作者：</font>** Ming-Hao Hsu, Shujie Liu, Yuxuan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio language models are meant to answer questions from the audio itself, but an hour-long recording rarely fits in their context, and the answer often depends on a few seconds of it. Transcribing the recording first makes it fit but discards sounds and voices, while systems that return to the audio must be trained for this behavior. We propose ReListen, a training-free method in which a frozen audio language model finds its own evidence before answering. In a Jev-style scan, the model scores each 20-second window by the probability that it helps answer the question, and it then answers from the highest-scoring minute. This minute overlaps the annotated evidence far more often than transcript retrieval, for 88.5% of VoiceGiraffe questions. Without any change, the same scan also grounds events on LAT-Bench as well as a model trained for temporal grounding. Answering from it matches or exceeds hearing the whole recording with a small fraction of the audio, and on VoiceGiraffe it exceeds a transcript of the whole recording by 9.2 points. The selected evidence is also worth hearing rather than reading. Given the same excerpts, reading their transcript matches listening on speech content, but listening is clearly more accurate on questions about sounds and voices. Moreover, ReListen answers faster than every transcript-based system, and its memory stays constant even for recordings too long to hear whole on one GPU. Therefore, a frozen audio language model can search hour-long recordings by itself, without a transcript or additional training.

---


### 128. [TEMPO: Time Series Understanding via Discrete Tokenization](https://arxiv.org/abs/2611.04482)

**<font color=#1a73e8>作者：</font>** Riccardo Maggioni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time-series interpretation often requires both numerical observations and textual context. Integrating these inputs into a pretrained language model raises a representation question: how should a signal enter the model's token sequence? We present TEMPO, which extends an LLM's vocabulary with discrete codes from a context-aware Transformer tokenizer using finite scalar quantization. A frozen tokenizer maps four-step patches to a 625-code vocabulary; signal tokens, scale statistics, and text are then processed by the LLM's existing self-attention layers. Adaptation updates the new token embeddings and DoRA adapters. With a Qwen3-4B backbone and task-specific fine-tuning, TEMPO achieves macro-F1 scores of 89.0% on activity recognition, 85.0% on sleep staging, and 86.0% on bearing-fault diagnosis. Time-series question answering and qualitative bearing-diagnosis examples further illustrate how this interface combines signal representations with textual context. Together, these results demonstrate the utility of discrete vocabulary extension for time-series understanding.

---


### 129. [CogniLife: Continuous Cognitive Distillation for Deployed Multi-Expert Agent Marketplaces](https://arxiv.org/abs/2611.04483)

**<font color=#1a73e8>作者：</font>** Xuwei Tan, Jingchun Huang, Ming Cai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-expert agent marketplaces -- where creators publish domain-specific AI experts for end users to consult -- are an emerging deployment pattern for language technology. A published expert can receive many requests yet little evidence about its creator, who remains active elsewhere: the cold-expert problem. We frame continuous cognitive distillation as converting attributed creator observations into revisable decision rules, communication patterns, and domain procedures. CogniLife proposes a cross-expert attribution design for this problem, with Creator Profiles for transferable creator patterns and Expert Journals for listing-specific knowledge; this design is not yet implemented or evaluated. A deployed platform partially realizes the surrounding lifecycle through creator-authorized authoring, capability-owned proposal filtering, and reversible consolidation of eligible owner-scoped memory. On ProfyBench-v1, an 85-task offline benchmark built from replay seeds and controlled internal tests, the Profy Full configuration as a whole achieves a mean overall score of 4.65/5 from the primary LLM judge, compared with 4.01 for Raw LLM and 4.28 for Expert Prompt, with the largest gains in completeness, specificity, and missing-information tasks. These configuration-level scores do not test cold-expert mitigation, cross-expert transfer, or longitudinal distillation.

---


### 130. [Perseus: A Full-Stack System for Homomorphic Model Inference](https://arxiv.org/abs/2611.04488)

**<font color=#1a73e8>作者：</font>** Alessandro Zirilli, Davide Marincione, Evgenios M. Kornaropoulos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have made it exceptionally convenient for users to send their private data to model providers, which process them in plaintext. Fully Homomorphic Encryption (FHE) promises to secure remote inference by computing directly on encrypted data, yet it has remained prohibitively slow. The effort to make it practical remains fragmented, with most existing frameworks being closed-source, which keeps progress from compounding. We present Perseus, a free and open Python software library that supports the full stack of encrypted model inference, from the cryptographic backend and data packing, to encrypted nonlinearities and end-to-end model execution. Perseus ships with built-in novel optimizations, one at each level of the stack: in-kernel regeneration of key-switching keys at the (i) backend level, a complex variant of Cachemir packing at the (ii) data level, and a state-of-the-art bootstrap placer that is both packing- and magnitude-aware at the (iii) model level. Perseus achieves state-of-the-art latency across multiple models and modalities, within $3\%$ of the plaintext models' accuracy and perplexity. Remarkably, it is $3.96\times$ faster at single-token decoding than any other implementation on Llama-3-8B. We initiate, for the first time, a public speedrun on encrypted GPT-2, so that progress can compound.

---


### 131. [Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation](https://arxiv.org/abs/2611.04489)

**<font color=#1a73e8>作者：</font>** Taehoon Kim, Wonjun Hwang, Hyunsouk Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP enable zero-shot classification from arbitrary class names, but under test-time corruptions, their visual encoder projects distorted features onto incorrect textual anchors with high confidence: a phenomenon we term modality bias. Standard entropy minimization reinforces these overconfident errors, which creates a confirmation-bias loop and collapses the predicted label distribution. We propose an online test-time adaptation (TTA) method that breaks this loop at three levels. At the representation level, a frozen self-supervised backbone (e.g., DINO v2) is combined with CLIP through a cross-covariance logit ensemble. CLIP text prototypes are projected into the feature space of this text-free backbone, so the self-supervised branch classifies native image features and is less affected by the text bias of CLIP. At the optimization level, a gated test-time information-maximization objective pairs per-sample sharpening with batch-level diversity, while an adaptive gate excludes unreliable samples from the gradient. At the prediction level, an online logit adjustment corrects the residual class-distribution skew. CDIM outperforms the compared CLIP-based online TTA baselines on ImageNet-C, CIFAR10-C, and CIFAR100-C, and remains competitive in continual and mixed-domain TTA. Extensive analyses and ablation studies verify the contribution of each of its components. Our code is available at this https URL

---


### 132. [SKILL2STEER: One-Pass Hypernetwork for Mapping Natural-Language Skills to Low-Rank Post-Block Activation Shifts](https://arxiv.org/abs/2611.04497)

**<font color=#1a73e8>作者：</font>** Ran Li, Lei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compiling a natural-language agent skill into model parameters removes the skill text from the prompt and leaves behind a small artifact that can be distributed and reused. Existing methods differ in where they inject the compiled quantity, and all of them assume that the artifact carries the content of the skill. We test that assumption. Through three controls on a retrieval agent, we find that a compiled skill shift carries a domain-general behavioural prior, not the content of the skill. A wrong skill document performs on par with the correct one, a single averaged bundle matches per-skill routing under a two-sided equivalence test, and a same-norm random direction collapses to the no-injection baseline, which shows that the trained direction stays load-bearing. We then introduce SKILL2STEER, a one-pass hypernetwork that reads a skill document once and maps it to low-rank activation shifts added at the output of every decoder block. Each skill compiles to 2.36M parameters, 9.25 times fewer than a weight-space adapter, while the base weights stay frozen and the generator runs only at compile time. The shift can be scheduled across retrieval steps and deployed as one routing-free bundle. On SearchQA, a seven-dataset benchmark, SKILL2STEER reaches 37.9 exact match, 9.8 points above the frozen model and 2.3 points above a weight-space method that ships 9.25 times more parameters per skill.

---


### 133. [AttriSwarm: Orchestrating Agent Swarms for Cross-Page Visual Attribution](https://arxiv.org/abs/2611.04504)

**<font color=#1a73e8>作者：</font>** Suifeng Zhao, Zida Liu, Lei Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) increasingly address knowledge-intensive tasks by integrating evidence scattered across multiple document pages into a final answer. Because such answers are synthesized from many pages, the link between the answer and its supporting visual evidence can become obscured, hindering verification and trust. Cross-page visual attribution is therefore essential: it requires identifying the supporting pages and localizing fine-grained evidence regions within them, thereby making multi-page reasoning transparent and auditable. Existing approaches either process multiple pages jointly or iteratively refine evidence within a single trajectory, risking cross-page context pollution and, for interactive methods, substantial sequential overhead. We introduce \textbf{AttriSwarm}, an agent-swarm framework that assigns these concerns to separate roles: a leader handles global cross-page reasoning, while subagents perform page-wise attribution in isolation and in parallel. To support training and evaluation, we construct \textbf{AttriDoc}, a cross-page QA dataset linking supporting pages to their annotated evidence regions, and use it for role-specific training of AttriSwarm, improving answer accuracy, page-level $F_1$, and region-level IoU over its training-free counterpart by an average of 18.94, 29.34, and 23.04 percentage points, respectively, across three open-source backbones and three datasets.

---


### 134. [Signals: Continuous Diagnostics of AI Agents](https://arxiv.org/abs/2611.04507)

**<font color=#1a73e8>作者：</font>** Amey Rambatla, Vatsal Goel, Sagar Gaur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can make incorrect decisions or waste resources even when their tools and infrastructure work normally. Their nondeterministic behavior makes these problems difficult to reproduce and diagnose. We developed Signals to identify such problems from agentic traces and suggest concrete remediations. We built the method around a taxonomy of 45 problem types across eight families, with definitions and evidence requirements for each type. The method distinguishes realized failures, risk exposures, and inefficiencies, groups related findings into engineering issues called Signals, and assesses their severity from the supporting evidence. Each Signal includes actions a developer can take and checks for evaluating the change. Further executions can add evidence to an existing Signal or reveal a new problem. We evaluated the method on public agent executions and achieved 91.43% F1 when matching Signals to reference issues, about 18 percentage points higher than a one-pass LLM control that used the same model and taxonomy.

---


### 135. [Fast, Cheap, and Fair? Evaluating Decision Models](https://arxiv.org/abs/2611.04510)

**<font color=#1a73e8>作者：</font>** Muhammad Uzair Ul Haq, Davide Rigoni, Alessandro Sperduti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industries are increasingly adopting AI-driven systems to automate a wide range of tasks, including high-stakes decisions in human resources, such as candidate screening and recruitment. This makes evaluating their fairness essential, particularly when decisions directly affect individuals' opportunities. Accordingly, the EU AI Act classifies recruitment AI systems as high-risk, imposing strict requirements on their deployment. In this context, compact ``System~1'' decision models offer a fast and cost-efficient alternative to general-purpose LLMs, yet their fairness remains largely unexplored. This article presents the first systematic bias and fairness audit of \jev{}, a typed-decision model targeting recruitment applications. The study evaluates how explicit demographic attributes and implicit candidate cues influence screening scores, rankings, and shortlisting outcomes. These effects are compared against a noise floor derived from name substitutions and typographical variations. The evaluation also examines output validity, latency, and cost. Counterfactual CV datasets and evaluation code are released for reproducibility.

---


### 136. [Learnings and Pitfalls from AI-Assisted A/B Experimentation at Scale](https://arxiv.org/abs/2611.04515)

**<font color=#1a73e8>作者：</font>** Brett Daley, Ilya Gorbachev, Anubhav Natani 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A/B testing underpins product decisions by providing trustworthy, reproducible quantification of proposed changes' effects. Growing large language model (LLM) capabilities have motivated efforts to automate experimentation workflows. Yet LLMs are nondeterministic and prone to hallucination, properties that conflict with the trust experimentation systems must provide. Experiments are also operationally messy: diagnosing anomalies, debugging configurations, and conducting bespoke follow-up analyses require flexible reasoning and manual effort. These tasks let agents accelerate experimentation without replacing its deterministic statistical foundations.
We report lessons from building and operating such an agent. Our central finding is that this tension is resolved not by making the model deterministic, but by bounding where its nondeterminism can reach; the model selects and sequences procedures, while deterministic code computes every quantity it reports. Three consequences surprised us: withholding information from the model improved its answers, demand concentrated on mundane retrieval rather than the autonomous decisions we anticipated, and the agent's eagerness to help threatened statistical validity.

---


### 137. [BtsPruner: Role-Aware Visual Token Pruning for Large Vision-Language Models](https://arxiv.org/abs/2611.04537)

**<font color=#1a73e8>作者：</font>** Zihao Qi, Zhibo Zhang, Miaoxin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) often process hundreds or thousands of visual tokens, resulting in substantial computational and memory overhead during inference. Existing training-free pruning methods typically estimate token importance using language-model attention, visual attention, or feature similarity. However, these methods treat visual tokens with uniform criteria and overlook that tokens may serve different roles during visual encoding. In this work, we investigate the evolution of visual token roles in LVLMs and observe that tokens progressively transition from local detail carriers to globally referenced representatives as encoding proceeds. Based on this observation, we propose BtsPruner, a training-free role-aware visual token pruning framework that preserves complementary token roles under a fixed budget. Specifically, BtsPruner first identifies the token-role transition point based on the evolution of attention concentration. It then discovers globally referenced representatives from later encoding stages and recursively retrieves local detail tokens from earlier stages to recover complementary fine-grained evidence. Extensive experiments across LLaVA-1.5, LLaVA-NeXT, Qwen-VL, InternVL, and CogVLM demonstrate that BtsPruner achieves superior performance retention under aggressive token reduction. On LLaVA-1.5-7B, BtsPruner preserves 91.6% of the dense model's performance using only 32 of 576 visual tokens (5.6%). In the high-resolution LLaVA-NeXT-7B setting, it achieves up to a 5.95x CUDA-latency speedup.

---


### 138. [Are LLM Assistants Regulatory Ready? Answers from regenold's 2026 EU AI Act Q&A Challenge](https://arxiv.org/abs/2611.04546)

**<font color=#1a73e8>作者：</font>** Marco Virgolin, Thomas Haszprunar, Maximilian Regenold  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants are increasingly proposed for regulatory affairs, yet their reliability in regulatory tasks remains unclear. We introduce the EU AI Act Q&A Benchmark, an expert-curated benchmark of 110 open-ended questions about the EU AI Act (Regulation (EU) 2024/1689). Each question comes with an exemplary answer, question-specific correctness criteria, and expected references. Evaluation measures answer correctness, reference quality, conciseness, tone, and latency, with a multi-turn ``hard mode'' testing responses to simulated user pushback. We also present the results of the 2026 EU AI Act Q&A Challenge, based on the benchmark, where three off-the-shelf baselines and five purpose-built assistants (from four commercial developers and one academic entrant) were tested. Only two of the five submitted assistants consistently outperformed the baselines; one achieved high scores across all evaluated metrics. These results show that specialist development alone does not guarantee better performance and highlight the critical importance of LLM assistant evaluation in regulatory affairs. The benchmark code is openly available at this https URL.

---


### 139. [Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems](https://arxiv.org/abs/2611.04556)

**<font color=#1a73e8>作者：</font>** Chandler Smith, Qi Guo, Cecilia Elena Tilli 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of AI agents in multi-agent settings enables inter-agent influence, whereby agents can strategically steer each other's behaviour towards an intended outcome. Such capabilities pose novel risks, as malicious agents could direct others towards harmful actions. In this work we investigate three such capabilities - persuasion, deception, and coercion - across five realistic evaluation environments and a variety of agents instantiated with frontier language models. We observed significant inter-agent influence capabilities; in oversight environments, all tested models shifted overseer decisions from rejection to approval through persuasion, deception, or coercion. We also observed successful influence in non-hierarchical 'peer-to-peer' settings through redirection of a peer's safety research trajectory. As multi-agent deployments become increasingly commonplace, these results point to a pressing need for work on mitigating the risks from inter-agent influence. Code and data are available at this https URL.

---


### 140. [A research world model of power engineering learns its dynamics and reveals what-ifs](https://arxiv.org/abs/2611.04566)

**<font color=#1a73e8>作者：</font>** Fanping Sui, Ying Zhang, Liwei Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decisions about the direction of research in power engineering determine which technologies mature and, through them, shape infrastructure that lasts decades, yet their consequences cannot be observed before they are taken, and existing forecasts of research fields extrapolate a single trajectory. Here we introduce research world models, which treat a research field as a dynamical system that can be acted upon, and establish one for power engineering from 1.1 million papers. A distilled language model reads each paper into role-typed concepts, two sophisticated, high-fidelity graph-temporal neural network cores learn how the resulting concept network evolves, and operators learned from natural experiments in the publication record estimate the effects of interventions. In temporally held-out tests, the model forecast years ahead which concepts would grow and which method-target pairs would be joined for the first time, outperforming tuned machine-learning baselines in most settings, and its estimated intervention effects tracked those realized in natural experiments it had not seen. Its training scheme and three of its operators replicated in two fields withheld from development. Questions posed in natural language are compiled by a domain-specialized 27-billion-parameter language model into executable actions and answered as paired simulations with and without the intervention. The answers were rated 4.1 of 5 for faithfulness by an independent language-model judge. By revealing the latent dynamics of a research field and its response to interventions, research world models offer a new way to simulate and test research decisions before they are made.

---


### 141. [ValQID: Learning the Net Value of Semantic Query Groups for Web Device Identification](https://arxiv.org/abs/2611.04576)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Zhen Huang, Weijia Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web interfaces are widely used to access network services and manage networked devices. Identifying the vendors and types of devices behind Web interfaces is a critical step in asset inventory, security management, and risk assessment. Device identity cues are dispersed across page text, configuration fields, and management functions, and interpreting them often requires linking related Web objects. Responses and objects require different amounts of semantic analysis, so exhaustively processing all candidate content can introduce unnecessary computation. We present ValQID, which uses a relation graph to combine dispersed device identity cues, evaluates semantic questions efficiently with DSEJEV, and accounts for complementarity among semantic questions when estimating computation value. Based on the current identification state, ValQID weighs each question group's expected identification benefit against its execution cost and adaptively allocates computation to identify device vendors and types. Evaluation on real Web response data shows that ValQID achieves relative gains of up to 47.1% in joint macro-F1 and up to 82.1% in macro-F1 for low-frequency vendors over a state-of-the-art method. DSEJEV speeds up semantic processing by up to 8.58 times compared with general-purpose language models.

---


### 142. [Evaluating LLMs as Judges of Counterspeech Quality Against Online Hate Speech](https://arxiv.org/abs/2611.04627)

**<font color=#1a73e8>作者：</font>** Johnny Alali, Nicolás Benjamín Ocampo, Davide Ceolin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prolonged exposure to hate speech on social media can cause lasting psychological distress among users. Counterspeech has emerged as an effective, non-censorial mitigation strategy, but its deployment requires rigorous quality assessment. Manual assessment is unscalable due to the large volume of content on the Web and imposes severe emotional strain on human annotators. Large Language Models (LLMs) offer a scalable alternative, yet concerns remain regarding their reliability. In this paper, we investigate the extent to which LLMs can effectively perform this task. We test 12 open-weight LLMs of different sizes and families under zero-shot, few-shot, and chain-of-thought prompting, to approximate pointwise and pairwise human expert assessment of counterspeech quality across four dimensions: relevance, coherence, aggressiveness, and suitableness. We find that (i) LLMs show low agreement and moderate rank correlations with human experts: our best configuration, Qwen 2.5 72B on coherence, achieves up to a linear-weighted Cohen's $\kappa_l = 0.19$ and Spearman's $\rho = 0.42$ in pointwise evaluation and an unweighted Cohen's $\kappa = 0.25$ in pairwise evaluation. (ii) Converting pointwise scores into pairwise labels substantially improves human--LLM agreement for selected configurations. For same-instance coherence, Qwen 2.5 72B under zero-shot prompting achieves $\kappa = 0.35$ with converted labels, compared with $\kappa = 0.25$ when judging pairs directly, and Mixtral 8$\times$7B under few-shot prompting improves from $\kappa = 0.07$ to $\kappa = 0.34$. (iii) LLMs agree more with one another than with human experts, particularly in pairwise evaluation, where the strongest model pair, OLMo 2 32B and Llama 3.3 70B on coherence, reaches substantial agreement with $\kappa = 0.76$, whereas their agreement with the experts in the same configuration does not exceed $\kappa = 0.21$.

---


### 143. [Self-Privileged Fine-Tuning](https://arxiv.org/abs/2611.04632)

**<font color=#1a73e8>作者：</font>** Yangrong Hu, Xueyu Zhou, Yue Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is a key component of language model post-training, enabling effective task adaptation and serving as an important foundation for subsequent reinforcement learning. Recent methods seek to improve SFT by introducing token-level weights into the training objective, where these weights are typically derived from a model's output distribution at each token position. To better understand how such weighting schemes affect SFT, we analyze their optimization objectives and theoretically characterize the target distributions they induce. Our analysis shows that dynamic weighting methods, such as Dynamic Fine-Tuning (DFT), induce a heavily sharpened distribution, whereas static weighting methods fit a target distribution proportional to the product of the data distribution and a frozen prior. These findings suggest that static weighting provides a more stable training target, while its effectiveness critically depends on the quality of the prior distribution. Building on this observation, we propose Self-Privileged Fine-Tuning (SPFT), which uses a frozen copy of the initial model conditioned on privileged information (such as ground truth for mathematical questions) as a prior to provide guidance for token-level weighting during fine-tuning. Through a Bayesian decomposition, we further show that SPFT reweights the standard static prior according to how informative each target token is for predicting the ground-truth outcome, thereby assigning larger weights to more predictive tokens. Experiments on mathematical reasoning and code generation show that SPFT improves over standard SFT and other baselines across the main settings.

---


### 144. [Best-of-Depth: Learning Exploratory Dynamics in Looped Transformers](https://arxiv.org/abs/2611.04663)

**<font color=#1a73e8>作者：</font>** Shota Takashiro, Takeshi Kojima, Masanori Koyama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers extend inference-time computation through repeated latent-state updates, but final-depth training does not directly encourage useful intermediate alternatives. We introduce Best-of-Depth (BoD), which trains a recurrent trajectory as a candidate set by minimizing prediction loss across depths. Different valid targets can be matched at different depths without architectural changes or depth-specific labels. An exact-match analysis connects this objective to solution coverage. On N-Queens completion and graph coloring, BoD improves coverage over final-depth and intermediate-supervision objectives. N-Queens coverage reaches 91.03%, versus 45.75% for final-depth training. Further experiments show discovery beyond the training depth and recovery of solutions withheld from teacher pools on familiar inputs. Fine-tuning a pretrained looped language model with BoD yields higher pooled code-generation success than final-depth training when programs are generated separately at evaluated fixed depths. These results support training recurrent computation for solution discovery along its trajectory.

---


### 145. [MIMIC-Note-Extract: A Large-Scale Structured Dataset Extracted from MIMIC-IV-Note Discharge Summaries](https://arxiv.org/abs/2611.04685)

**<font color=#1a73e8>作者：</font>** Kristian Schwethelm, Jonas Kuntzer, Conrad Ketzer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> MIMIC is one of the most widely used public hospital datasets for machine learning on electronic health records, yet clinically important information, such as past medical history, allergies, and diagnostic findings, remains confined to free-text discharge summaries. Studies requiring this information must therefore build their own extraction pipelines, duplicating substantial effort across projects. We release MIMIC-Note-Extract (MNE), a large-scale dataset that uses a hybrid extraction pipeline combining deterministic parsing with schema-guided large language model generation to transform 16 sections from 300,720 discharge summaries into structured tables. MNE adds information that has no structured MIMIC counterpart and enriches related tables with broader coverage and greater clinical detail, including 10 times more patient-history entries and medication histories for more than twice as many admissions. Validation by medical doctors confirms extraction accuracy above 92% across sections. Using MNE, we construct a clinical decision-making benchmark for LLM agents, demonstrating how reusable structured representations of clinical narratives reduce data curation effort.

---


### 146. [When Ground Truth Is Not Ground Truth: Automatic Labeling for Hallucination Detection](https://arxiv.org/abs/2611.04697)

**<font color=#1a73e8>作者：</font>** Rounak Sen, Divya Kumari, Deeksha Varshney  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations in Large Language Models (LLMs) remain a major challenge, as they can produce misleading, factually incorrect, or unverifiable information, thereby undermining their trustworthiness and reliability. However, reliable ground-truth labels remain a key challenge in evaluating hallucination detectors. Recent studies often construct labels automatically by comparing model generations with reference answers using similarity metrics such as BLEURT. This implicitly treats BLEURT similarity as a proxy for hallucination, despite its English-centric supervision, unbounded score range, and design as a similarity metric rather than a factuality measure, making threshold-based ground-truth construction potentially unreliable. Through comprehensive experiments using 15 automatic supervision judges, seven hallucination detection baselines, two generator models, two QA datasets, and five languages, we demonstrate that detector performance varies substantially with the choice of supervision judge. Human validation reveals substantial differences in labeling reliability, with QGen-9B achieving the lowest overall misclassification rate (12.86%), while BLEURT and BLEURT-n exhibit rates of 47.23% and 47.32%, respectively. Our findings highlight the limitations of automatic similarity-based labeling and the need for more reliable judging methods that better capture semantic and factual correctness.

---


### 147. [SPOD: Recovering Suppressed Temporal Evidence in Video-LLMs via Single-Pass Orthogonal Decomposition](https://arxiv.org/abs/2611.04728)

**<font color=#1a73e8>作者：</font>** Yangguang Lin, Quan Fang, Xiaoyan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Video-LLMs) have achieved strong performance on many video understanding tasks, yet remain vulnerable to temporal hallucination in time-sensitive reasoning scenarios such as scene transition understanding and event ordering. Existing solutions either require costly retraining or introduce inefficient multi-pass inference and external supervision at test time. In this work, we show that temporal evidence is already encoded in Video-LLM hidden representations but is not fully exploited during standard inference. Motivated by this observation, we propose Single-Pass Orthogonal Decomposition (SPOD), a training-free framework that recovers suppressed temporal evidence through analytical hidden-state manipulation in a single forward pass. SPOD consists of two components: Frame Distinctiveness Analysis (FDA), which identifies salient frames from middle-layer hidden-state geometry, and Temporal Delta Subspace (TDS), which constructs orthogonal temporal and prior subspaces from weighted inter-frame hidden-state differences. By decomposing final hidden states into temporal, prior, and residual components and rescaling them independently, SPOD enhances dynamic information, suppresses static appearance bias, and preserves complementary information. Experiments on VidHalluc, EventHallusion, and VideoMMMU show that SPOD consistently outperforms strong inference-time baselines across temporal reasoning tasks and model architectures while retaining near-vanilla inference efficiency. These results suggest that improving temporal reasoning in Video-LLMs may depend not only on additional supervision, but also on recovering temporal evidence already present in their internal representations. Our code is available at this https URL.

---


### 148. [When Should an LLM Steering Edit Depend on the Input?](https://arxiv.org/abs/2611.04757)

**<font color=#1a73e8>作者：</font>** Rachael Harkness, Konrad Rawlik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An activation steering edit should depend on the input exactly when the destination varies \emph{inside} the class a query requests, and that is measurable before any rule is fitted or applied. Contrastive Activation Addition (CAA) adds one fixed direction to every input, the difference of the class means. Conditioning it on the requested class accounts for the between-class variation in the required displacement and leaves the within-class variation untouched, which no rule that reads only the source state can express. We study the impact of increasing input-dependence in the steering edit, moving from a difference of means to a destination retrieved per query --- the mean of the $k$ stored states nearest the query, inside the requested class --- in which the two baselines are endpoints: at $k$ equal to the class size the retrieved rule \emph{is} the class-conditional difference of means. We measure input-dependent steering on six substitution corpora that vary in whether the edit changes a word or a clause, and on an external benchmark, and find that input-dependent steering outperforms fixed-direction steering when the destination varies within the class. Retrieval wins at every layer of every substitution corpus in two models, and the level of input-dependence needed governs how to apply it: word-level edits are best made in the first tenth of the network from a few neighbours, clause-level edits at any depth from the class mean. Where the class already determines the answer the class mean suffices and retrieval only matches it, though a fixed direction still fails there. Four quantities computed from the states alone identify the regime in which the edit should be applied.

---


### 149. [Beyond Local Refinement: Wide-Area Precise Cross-View Localization](https://arxiv.org/abs/2611.04759)

**<font color=#1a73e8>作者：</font>** Qingguo Hu, Xinyu Ma, Yujie Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained cross-view localization aims to precisely localize a ground camera against geo-referenced aerial imagery, but current methods typically assume a narrow geographic prior, substantially limiting their applicability when upstream localization remains coarse. To bridge this gap, we study this task over much larger aerial regions. However, this seemingly simple extension fundamentally changes the localization problem: the growing disparity in spatial extent between ground and aerial views makes reliable cross-view matching difficult to establish directly, while the increasing number of look-alike locations in larger regions introduces substantial visual ambiguity. To address these challenges, we propose RingMatch, a search-and-verification framework for wide-area cross-view localization. RingMatch first leverages predictive uncertainty to uncover plausible locations and progressively zooms into their surroundings to obtain increasingly fine-grained evidence, yielding a compact set of promising candidates. We then introduce the depth ring, a novel geometric representation that reveals subtle variations in the spatial layout around a location and serves as a view-shared spatial signature for an LVLM verifier to resolve residual ambiguity. To benchmark this setting, we construct VIGOR-Pro by composing VIGOR aerial tiles into contiguous regions with spatial extents of up to 400 m. Experiments show that RingMatch maintains strong localization performance as the aerial region expands, consistently outperforming representative end-to-end and retrieval-based methods.

---


### 150. [TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions](https://arxiv.org/abs/2611.04772)

**<font color=#1a73e8>作者：</font>** Qi Liu, Xiaoyang Yuan, Zhuomeng Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A deployed LLM coaching agent answers requests whose correct response depends on player state and game version, so advice that is right for one player can be wrong for the next. We describe TactiNavi, the serving system behind the LLM coach of a commercial open-world game, which makes strategy applicability an explicit artifact shared by offline compilation, online execution, failure diagnosis, and release. An offline compiler turns versioned game evidence and expert guidance into strategy packages with explicit prerequisites, the serving plane evaluates those prerequisites as three-valued conditions over structured player state and records decision traces, and a control plane uses the resulting condition-rule dependencies to validate revisions on held-out traffic before release. In a retrospective evaluation of 1,122 logged coaching turns from three deployment periods, condition-bearing packages raise correctness from 57.9% to 82.0% over atomic facts and reduce strategy misapplication under changed player state from 18.1% to 10.4%, while trace-based claim verification reaches 86.4% precision at a median reply latency of 2.07 s. The deployment also showed that most apparent fixes are generation noise, because an unchanged-system rerun recovers 38.4% of failing turns and only one of 15 shipped revision units passes the release checks retrospectively. We distill these results into lessons on treating applicability as a first-class serving object, sizing traces for later diagnosis, and building the null model into the release path.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
