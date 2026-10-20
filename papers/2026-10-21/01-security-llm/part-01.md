# 🔐 大模型安全相关研究 | 2026年10月21日

> 本类共 **16** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [When the Editing Intent Is Split: A Cross-Modal Jailbreak Attack for Large Image Editing Models](https://arxiv.org/abs/2610.23909)

**<font color=#1a73e8>作者：</font>** Xianmin Ye, Zhiyuan Fan, Tianju Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large image editing models increasingly infer editing intent from both textual and visual inputs, creating an underexplored safety risk when harmful intent is distributed across modalities. In this work, we formalize this split-intent vulnerability and propose the Split-Intent Jailbreak Attack (SIJA), which asymmetrically distributes an unsafe editing intent by specifying the editing referent in text while concealing the safety-critical action and specification through graphical visual semantics in an auxiliary cue. To systematically study this threat, we introduce the Split-Intent Image Editing Safety Benchmark (SI2ESBench) for evaluating image editing models under split-intent inputs. Extensive experiments on representative commercial and open-source models demonstrate that SIJA effectively compromises state-of-the-art image editing systems, achieving ASRs of 68.28% on GPT Image 2 and 91.38% on Qwen-Image-3.0-Pro. Our results expose a mismatch between multimodal editing and safety assessment: the distributed intent can be recovered to execute the requested transformation, yet its harmfulness often remains undetected by existing safeguards. To mitigate this vulnerability, we propose editing-intent reconstruction, a defense principle that explicitly evaluates the complete transformation implied by the joint multimodal context and substantially improves rejection of split-intent attacks. Our findings expose a cross-modal safety gap in modern image editing systems and highlight the need to assess the jointly inferred transformation rather than individual inputs in isolation. this https URL

---


### 2. [The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections](https://arxiv.org/abs/2610.24048)

**<font color=#1a73e8>作者：</font>** Haoxuan Jia, Yang Liu, Bin Chong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents that read untrusted content can be hijacked by prompt injections. Runtime monitors that try to catch a hijack before the agent acts, and benchmarks that score each task with a single run, share an assumption: whether an agent follows an injection is settled when the injection is read. We test this assumption with branching rollouts that replay an episode exactly up to the step at which the agent reads an injection and then resample the rest of the episode many times, splitting the outcome variance into a part fixed at read time and a part decided afterwards. Across four AgentDojo suites, a Qwen3 agent without thinking is largely decided at read time (0.91 of the outcome variance lies between states); with thinking on, this share drops to 0.62 (95% CI of the drop [-0.38, -0.22]), in the same direction for three attack templates and two success labels. How much is fixed at read time is a property of the model that the same measurement reveals, and thinking lowers the attack success rate of Qwen3 but raises it for two other models. Resampling from reasoning prefixes shows that the decision forms gradually as the agent reasons. Zero-shot chain-of-thought monitors built on cheaper models miss much of what is already decided, whereas stronger monitors, and a lookahead monitor that judges simulated next actions, come close to what the prefix determines. Finally, single-run labels of thinking agents disagree with a rerun up to 35% of the time, so benchmarks need repeated runs per task.

---


### 3. [Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks](https://arxiv.org/abs/2610.24052)

**<font color=#1a73e8>作者：</font>** John Kitaoka, Thao Amelia Pham, Carlos Rafael Giudice 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are growing more capable and persistent, and are being deployed in ever larger numbers. As more start collaborating, AI control measures must remain effective when they covertly collude on a harmful objective. We introduce MiniLab, a synthetic series of live services and codebases (5 interconnected services, 249 benign tasks, 8 attack objectives), adapted from internal AI deployment infrastructure. We demonstrate distributed attacks, in which different agents carry out separate attack fragments, and how their covertness evades frontier monitors when reading their trajectories individually. We show how distributed attacks spread across diverse contexts and harmful objectives through 16 human-optimized attacks (weight exfiltration, unmonitored rogue deployment, permission elevation, and more). A frontier monitor, GPT-5.6 Sol, reading each agent separately flags only 7% of successful distributed attacks, compared with 87% when a single agent carries out the same side task. Individual attacks can also be composed into longer attack sequences toward a greater loss-of-control outcome, without any individual agent being flagged. Finally, we tested whether models can plan these covert attacks: even with execution and monitor feedback, the best model-planned attacks succeed covertly against a single-trajectory GPT-5.6 Sol monitor in at most 25% of executions, compared with 80% for human-crafted plans, though this may scale with model capabilities. By turning worst-case coordinated attacks into reproducible red-team cases, our work provides a foundation for preventing locally benign agent actions from accumulating into system-level loss of control.

---


### 4. [Under the Skin: Backdoor Infection in Multimodal Large Language Models](https://arxiv.org/abs/2610.24058)

**<font color=#1a73e8>作者：</font>** Jiawen Wang, Ruo Yang, Haoran Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved impressive performance in generating text conditioned on inputs from different modalities. In this work, we introduce backdoor infection, a cross-modal attack framework targeting MLLMs. Starting from a model already injected with a backdoor in one modality, our attack constructs a corresponding trigger in another modality, called the infected modality. Exploiting the model's shared latent space, the trigger in the infected modality reliably activates the malicious behavior, without modifying or poisoning the infected modality during training. We further develop a lightweight, constraint-aware optimization method for efficient and practical trigger generation. Extensive experiments across several state-of-the-art MLLMs, including LLaVA, InternVL, Qwen-VL, and Gemma, demonstrate that our approach identifies cross-modal triggers that are more efficient, effective, and less detectable than direct optimization baselines, highlighting a critical new threat vector in multimodal systems.

---


### 5. [Defending Against Dormant Poisoning Attacks Across Language and Multimodal Agents](https://arxiv.org/abs/2610.24379)

**<font color=#1a73e8>作者：</font>** Wonjun Lee, Vaidehi Patil, Zaid Khan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work shows that attackers can implant dormant malicious behaviors that remain hidden at release but emerge after benign fine-tuning. As foundation models are used as agents, whether dormant poisoning extends to harmful agent actions and multimodal settings remains unclear. We show two agentic risks: (1) harmful behaviors activated by benign fine-tuning can extend to unseen actions; (2) multiple harmful behaviors can coexist and be jointly activated by benign downstream fine-tuning. Existing defenses often rely on external safe responses, which are hard to obtain for agent actions, or a trusted clean reference model. We exploit a key property of dormant poisoning: the attacker must preserve safe behavior at release to conceal poisoning, and this behavior can serve as a safety reference. Leveraging this property, we automatically construct a Safety Buffer pairing harmful inputs with the released model's responses and benign versions generated by the same model to remove harmful intent. The Safety Buffer can replace external safe responses in existing defenses, but these defenses do not distinguish updates that weaken safety from those that preserve it, often increasing over-refusal or reducing utility. To address this limitation, we introduce LookAhead Defense, which previews benign fine-tuning updates using the Safety Buffer and penalizes only updates predicted to weaken safe behavior on harmful inputs or increase the likelihood of refusals on benign versions in the Safety Buffer. Across language models, language agents, and multimodal agents, LookAhead Defense reduces harmful behavior in agents from up to 93.9% to at most 14.2% and harmful responses in language models from up to 92.5% to at most 2.0% versus vanilla fine-tuning, while maintaining competitive utility and low over-refusal. It remains effective against other poisoning methods.

---


### 6. [The Missing Compliance Class: LLM Graders That Collapse Jailbreak Success, and a Free Check](https://arxiv.org/abs/2610.24872)

**<font color=#1a73e8>作者：</font>** Ruqiya Bin Safi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak papers report an attack success rate, the share of responses that deliver the harmful request, and read it as a property of the target model. We hold the target model, the prompts and the responses fixed and change only the grader. Three dense graders of 8B and 9B parameters, from three model families, move compliant responses to the neighbouring class, evasion, instead of scattering them across classes. One of them assigns the compliance label zero times in 900 responses. This class collapse also appears on new harmful requests, on a target model from a third family, and in a held-out 7B grader from a fourth family. Per-class label counts expose it at no cost and without human labels. The collapse decides how the rate behaves under a change of grader. On two corpora of 900 responses and eight graders, the compliance rate differs by a factor of 22 to 25, while the non-refusal rate differs by 18 to 23 percentage points. Without the three collapsing graders, compliance differs by a factor of 1.7 to 2.8 on all four corpora, and non-refusal still differs by 10 to 22 points. These results do not change when every grader is called once. We propose a reporting minimum that keeps the compliance rate and adds its per-class label counts and the named grader. Beside it goes the non-refusal rate, whose disagreement across graders is additive.

---


### 7. [SoK: PIAtlas: Decomposing the Unbounded Prompt Injection Attack Space](https://arxiv.org/abs/2610.24999)

**<font color=#1a73e8>作者：</font>** Stavros Damianakis, Konstantinos Psounis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is the dominant security risk for large-language-model (LLM) applications and agents, yet the field still lacks a coherent map of how these attacks are constructed. More than twenty public datasets describe prompt injection using incompatible vocabularies, often organized around delivery vector, attacker goal, or generation method. In this Systematization of Knowledge, we present PIAtlas, a taxonomy organized instead around how the injected instruction is constructed to subvert the underlying model. Its six classes, one per subversion mechanism, form the roots of a hierarchy of techniques and sub-techniques that researchers can use to describe attacks consistently and design more systematic evaluations. We derive the taxonomy from how LLMs are trained, prompted, and influenced by human-like framing, and compare it with historical attack data. To ground this comparison, we release PICorpus, to our knowledge the largest license-clean collection of public prompt-injection datasets, and map thousands of its records to PIAtlas under a human-verified protocol. The mapping shows that attacks usually combine several techniques drawn from only a few mechanisms. It also reveals gaps that existing labels obscure: widely used agent benchmarks test only part of the attack space, and adaptive attackers favor mechanisms that curated benchmarks underrepresent. PIAtlas thus provides a common foundation for understanding this attack space, improving benchmark coverage, and guiding red teaming and defenses.

---


### 8. [SEAL: Towards Persistent Tool Poisoning Attack against LLM Agents via Prefix-Eliciting Trigger](https://arxiv.org/abs/2610.25372)

**<font color=#1a73e8>作者：</font>** Nanjun Zhou, Yiming Li, Yukun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool poisoning has emerged as a critical security threat to LLM agents, where adversaries embed malicious instructions in tool descriptions or external resources that enter the agent's context, allowing adversaries to manipulate agent's tool selection process. However, existing tool poisoning attacks primarily rely on an idealized assumption that the attacks task effect within a single interaction round. We show that their effectiveness degrades sharply in realistic multi-round agentic settings. We further reveal that this degradation stems from the fact that agents do not consistently surface attack-relevant signals in their reasoning as the planning context evolves, thereby weakening the attack's influence across rounds. To investigate whether tool poisoning remains a practical threat in such realistic settings, we propose SEAL, a two-stage method for persistent tool poisoning. Specifically, SEAL first performs Prefix-Eliciting Trigger Optimization (PETO) to optimize context-specific triggers that elicit attack-relevant reasoning prefixes, improving effectiveness within individual contexts. It then applies Local-to-Universal Trigger Aggregation (L2U) to combine these local triggers into a single universal trigger, improving generalization across different contexts and execution rounds. Extensive experiments across seven representative multi-round scenarios and different models demonstrate the attack effectiveness of SEAL, its transferability across target models, and its resistance to potential defenses.

---


### 9. [Budgeted Attack Scheduling for LLM Red-Teaming: The Roles of Static Priors, Semantic Guidance, and Online Feedback](https://arxiv.org/abs/2610.25897)

**<font color=#1a73e8>作者：</font>** Zhicheng Fang, Han Sun, Jiachen Lei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As jailbreak attacks against large language models (LLMs) become increasingly diverse, red-teaming has come to rely on large libraries of jailbreak prompts and attack strategies to evaluate the robustness of victim models and their defense settings. However, attack effectiveness is highly condition-dependent: an attack that succeeds under one victim-defense setting may fail under another, while exhaustively evaluating the full attack library for each setting incurs substantial token and monetary costs. This motivates studying how jailbreak attacks should be prioritized under a limited attempt budget for efficient robustness evaluation. In this work, we formalize this problem as budgeted attack scheduling over a fixed attack library and investigate three complementary signals under a fixed victim-defense condition: (1) static historical attack success rate (ASR) priors; (2) semantic guidance from LLMs; and (3) online feedback from earlier queries. Building on these signals, we design four scheduling strategies and evaluate them across three victim models and three defense settings on GPT-5.2. Extensive experiments clearly characterize the conditions under which each signal is most effective. Historical ASR provides a strong initialization, but its reliability degrades under defense-induced distribution shifts. Semantic guidance consistently improves or matches static prior-based scheduling in the cold-start regime, while online feedback becomes particularly valuable when transferred priors become stale. Semantic guidance and online feedback can also partially compensate for missing historical priors. Taken together, these findings characterize budgeted red-teaming as an attack scheduling problem in which historical priors, semantic guidance, and online feedback play complementary roles.

---


### 10. [Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916)

**<font color=#1a73e8>作者：</font>** Tue Le, Anh Nguyen Hoang, Gabriel Sasseville 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an optimizer can improve the signal's verdict without removing the underlying vulnerability. Existing model-based approaches require models to either infer program behavior from source code or specify correct outcomes for adversarial tests, placing substantial reasoning demands on the security signal. We introduce \falcon{}, a counterexample-grounded verification framework that separates attack exploration from behavioral verification and connects them through execution traces of the program under test. In test-time repair, \falcon{} yields substantially stronger held-out functional-security gains than alternative security signals across secure code generation benchmarks, while preserving or improving functionality. As an RL reward, \falcon{} also outperforms static-analysis and learned rewards on held-out functional-security, even when all policies successfully optimize their respective training rewards. Combining \falcon{} with either proxy reward further improves held-out performance, suggesting that execution-grounded feedback can mitigate reward overoptimization while preserving useful guidance from existing security signals.

---


### 11. [RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.25937)

**<font color=#1a73e8>作者：</font>** Yuchen Chen, Wei Cheng, Yuan Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enables large language models to access external knowledge during inference, but its reliance on external knowledge bases also introduces new attack surfaces. Existing data extraction attacks against RAG systems rely on either prompt injection, which heavily depends on the generator's instruction-following capability, or backdoors that reproduce or paraphrase retrieved documents but struggle to balance extraction fidelity and stealthiness. In this paper, we propose RAGLeak, a supply-chain privacy backdoor attack that decouples information leakage from direct textual exposure. When triggered, the generator reversibly obfuscates retrieved private documents for high-fidelity recovery by an auxiliary LLM. Across three model families and three application domains, RAGLeak achieves up to $100\%$ ASR with limited impact on benign utility and at most a $10$-percentage-point ASR drop under representative detection-based defenses. The backdoor remains effective after clean fine-tuning and across model scales and versions, revealing an underexplored supply-chain privacy risk in RAG systems. The source code is available at this https URL.

---


### 12. [SpanGuard: Decoupling Instruction Localization from Authorization for Lightweight IPI Defense](https://arxiv.org/abs/2610.26013)

**<font color=#1a73e8>作者：</font>** Yinxiang Wang, Zehua Ma, Kejiang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based guardrails are effective against indirect prompt injection (IPI), but their performance depends heavily on model capability: as the guardrail model becomes smaller or weaker, detection degrades substantially. This raises a natural question: can we retain strong IPI defense while relying only on a small LLM? To understand why, we revisit what an LLM guardrail actually does. Detecting IPI requires simultaneously locating potentially injected instructions within heterogeneous tool outputs and judging whether they are authorized by the user's request. We find that the difficulty for small models arises largely from satisfying both requirements jointly, rather than from either subproblem alone. This suggests a different path to lightweight defense: explicitly decoupling localization from decision-making. In particular, localization needs no strong language-model reasoning, since injected instructions are often semantically discontinuous with their surrounding content and can be partitioned into local regions via lightweight unsupervised segmentation. Once the observation is partitioned this way, the remaining authorization check becomes a localized judgment that a small LLM can handle. Building on this insight, we design a lightweight IPI guardrail that performs attack-agnostic localization followed by block-level authorization judgment with a small language model. By separating where to look from what to decide, our approach substantially reduces the capability required of the guardrail model while preserving strong defense performance. Empirically, our guardrail achieves a 0.32% attack success rate with negligible loss in benign utility while remaining effective with substantially smaller models. These results show that strong IPI defense need not rely on strong LLMs when localization and decision-making are explicitly decoupled.

---


### 13. [Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents](https://arxiv.org/abs/2610.26438)

**<font color=#1a73e8>作者：</font>** Mengxiao Wang, Nitesh Saxena  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents now trade real capital using news as evidence, yet they cannot reliably tell fabricated headlines from real news. Because they read the same feeds under near-identical policies, a single fabricated post can push them into the same trade at the same moment. We present a systematic attack benchmark for information injection against LLM trading agents. Unlike prompt injection, which targets the model's instructions, information injection targets the evidence the agent trusts. The benchmark spans five injection vectors and seven event categories, evaluated over ~10,000 decisions on 15 U.S. stocks. Five findings emerge. (i) Prompt injection achieves 14% attack success rate (ASR), but fabricated news reaches 62% and two 30-word templates reach 100% on all 15 stocks, inverting the usual LLM-security intuition. (ii) For fact-poisoning templates, surface form matters more than content, since removing credibility cues such as a named source or a "BREAKING" tag drops ASR from 100% to 0% while the fake claim remains identical. (iii) Success depends on the agent's state, with a fake indicator panel scoring 91% against an agent about to hold but 12% against one about to buy. (iv) Attacks generalize across model vendors and remain effective when blended, unlabeled, into real news feeds. (v) Most attacks evade standard defenses, since model scaling stops shallow vectors but not fact poisoning, peer debate fails, and only hierarchical aggregation reduces ASR.

---


### 14. [Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks](https://arxiv.org/abs/2610.26589)

**<font color=#1a73e8>作者：</font>** Rohan Menon, Chih-Hong Cheng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attack success rate (ASR) evaluates jailbreaks against large language models without accounting for repeated calls to the victim model. Yet each additional call gives the deployed system another opportunity to detect the attack and intervene. We introduce $\mathrm{ASR}_{\mathrm{STEP}}$, which penalizes additional victim-model calls while retaining binary success judgments. Our evaluation considers GCG~\cite{zou2023universal}, PAIR~\cite{chao2025jailbreaking} with a step budget, and a single-step PAP~\cite{zeng2024johnny} baseline on JailBreakBench across three model families. GCG's scores decrease by 7.0--8.7 percentage points after discounting, while PAP's remain unchanged. While for PAIR~\cite{chao2025jailbreaking}, we see a wider discounting range between 3.4-12 percentage points, showing that the "step" quantity differs per iterative strategy. Reporting both metrics makes the discount due to repeated victim-model interaction explicit. Code is available \hyperlink{this https URL}{here}.

---


### 15. [Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates](https://arxiv.org/abs/2610.26595)

**<font color=#1a73e8>作者：</font>** Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Jailbreak methods are commonly compared using Attack Success Rate (ASR), but these comparisons depend on how responses are generated and judged. In this paper, we examine eight attacks against three open-weight language models using three evaluation procedures. Low-resource language attacks achieve a mean ASR of 96.0% under keyword matching but 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions. Changing the number and arrangement of attempts reverses the ranking of DeepInception and rewriting. In a separate experiment, sampling 100 responses for each unchanged request at Ollama's default temperature of 0.8 yields 100% ASR under keyword matching but 50% under the Qwen3 evaluator. Beyond evaluator sensitivity, these findings raise a safety concern: repeated sampling can expose residual unsafe behavior despite an initial refusal, suggesting probabilistic suppression rather than robust exclusion. We recommend explicit success definitions, matched response budgets, validated evaluators, and reporting cumulative failure under repeated interaction rather than relying on single-generation tests.

---


### 16. [Safety Mid-Training: Internalizing LLM Safety as a Foundational Capability](https://arxiv.org/abs/2610.26809)

**<font color=#1a73e8>作者：</font>** Zhengyue Zhao, Liwei Jiang, Yejin Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment for large language models (LLMs) is primarily performed during post-training, while recent work has also begun incorporating safety data into pre-training. Yet safety can degrade when later training no longer includes safety data, and gains in safety often come at the cost of general capability. This tension suggests that safety and general reasoning should not be treated as separate training goals. We instead view safety as an LLM capability that can be learned through a reasoning structure shared with general tasks. Both require the model to understand intent or task goals, apply relevant knowledge, and reason about potential consequences. We introduce safety mid-training, a stage between pre-training and post-training that jointly develops safety and general reasoning through this shared structure. Given safety and utility prompts, the base model generates structured documents and reasoning traces that are then used for mid-training. Safety mid-training reduces average attack success rate (ASR) by 72% to 81% relative to Qwen3-1.7B, 4B, and 8B base models, while also improving general capability. The benefits persist through subsequent post-training. After general-only SFT, mid-trained models largely retain their safety, achieving lower ASR than the baselines without sacrificing general capability. They also retain safety under general-only GRPO without safety rewards, while subsequent RL reaches a better safety-utility frontier when initialized from the mid-trained models. Together, these results suggest that learning safety and general reasoning within a shared mid-training stage can reduce the safety-utility trade-off and make safety more robust to subsequent training.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
