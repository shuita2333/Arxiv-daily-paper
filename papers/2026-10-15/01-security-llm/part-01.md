# 🔐 大模型安全相关研究 | 2026年10月15日

> 本类共 **22** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Loose Lips: Understanding Privacy Leakage in Agentic Dialogue](https://arxiv.org/abs/2610.14071)

**<font color=#1a73e8>作者：</font>** Soumya Sharma, Ayana Hussain, Heber Hwang Arcolezi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents are increasingly deployed in high-stakes enterprise settings, understanding how they handle sensitive information in agentic dialogue has become critical. Privacy leakage in such settings requires reasoning about whether information flows respect the contextual norms under which they originated. We extend CIMemories to CIMEMORIES DIALOGUE, a benchmark of 4,410 two-agent dialogue instances grounded in Contextual Integrity theory. Using this benchmark, we systematically evaluate 7 open-weight models from the Qwen3 and Llama 3.1 families across conversation lengths of 1 and 6 turns under three prompting conditions. We find that task capability and privacy leakage are fundamentally coupled: more capable models are systematically leakier, with no model in our evaluation able to decouple the two. Thinking models consistently leak more than their non-thinking counterparts, a pattern we attribute to the extended reasoning surface created by chain-of-thought. Leakage compounds with conversation length, rising up to 3x from 1 to 6 turns. Our results suggest that the coupling between task capability and privacy leakage is not an artifact of misconfiguration but a structural feature of current agentic systems.

---


### 2. [Scenes as an Attack Surface: Uncovering Scene-Grounded Safety Failures in MLLMs](https://arxiv.org/abs/2610.14094)

**<font color=#1a73e8>作者：</font>** Tongxi Wu, Yuyang Cheng, Jiacheng Xian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing jailbreak attacks have exposed serious safety weaknesses in multimodal large language models (MLLMs). Most prior attacks rely on specially constructed visual inputs to carry or support harmful intent. In this paper, we uncover a different vulnerability: task-relevant scene semantics alone can shift an MLLM from refusal to compliance, even when the visual input introduces no additional attack instructions and the original task intent remains unchanged. We formalize this failure as a scene-grounded visual safety vulnerability and introduce SceneSafetyBench to investigate it across eight risk categories and nine white- and black-box MLLMs. Our analysis reveals that this failure is associated with how task-relevant visual evidence influences downstream safety representations, suggesting that visual grounding alone cannot fully explain the observed safety shift. Building on this finding, we propose Scene-Grounded Attacks (SGA), which preserve the original task while constructing validated scene-grounded queries and combining their independent responses. Across nine target MLLMs, SGA achieves an average attack success rate (ASR) of 86.17%, outperforming the strongest baseline by 8.55 percentage points and achieving the highest ASR on eight models. Our results identify scene semantics as an overlooked attack surface in MLLMs and highlight a growing tension between stronger visual grounding and robust multimodal safety alignment.

---


### 3. [Watermarking for Byzantine Robust LLM Training](https://arxiv.org/abs/2610.14289)

**<font color=#1a73e8>作者：</font>** Leixu Huang, Zedian Shao, Teodora Baluta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM watermarking has emerged as a promising approach for detecting downstream model misuse in centralized settings, but extending it to federated learning (FL) presents unique challenges. In particular, FL systems often rely on strong robust aggregators to defend against poisoning attacks. We empirically show that a malicious server can exploit these same aggregators as effective watermark-removal mechanisms during training, causing representative existing LLM watermarking methods to fail detection in the final model. To address this limitation, we formalize the problem as a constrained optimization task and propose CamoMark, an aggregator-agnostic watermarking scheme for embedding robust watermarks in FL. CamoMark optimizes watermarked updates to become inliers, maintaining bounded deviation from the distribution of clean updates, while preserving sufficient watermark signal for reliable detection. Evaluated on Qwen fine-tuned on the Alpaca dataset, CamoMark achieves a detection confidence of $p$-value $= 1.82\times10^{-2}$ using only 3.3% watermarked data. The watermark also remains robust to a range of post-training removal attacks, including continued fine-tuning on clean data, pruning, and model distillation. At higher watermark ratios, detection confidence improves substantially, reaching $p$-value $= 5.11\times10^{-11}$ at a 13.3% watermark ratio.

---


### 4. [Tokenization-Invariant Watermarking: A Byte-Local Method for LLM Text](https://arxiv.org/abs/2610.14378)

**<font color=#1a73e8>作者：</font>** Tung-Ling Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce Tokenization-Invariant Watermarking (TI-WM), a method that embeds a watermark during token generation but keys and scores it on canonicalized UTF-8 bytes. The detector does not invoke the tokenizer. Canonicalizer-preserving edits leave its score unchanged; other localized canonical-byte edits affect a bounded number of scoring windows. Across three fixed keys and 128 prompts per key and model, a deterministic white-box attack at a 5% word-edit budget leaves mean attacked-AUC 0.530 on Qwen3-8B and 0.664 on Gemma 4 E4B, compared with 0.410 and 0.489 for Unigram with detection-side deletion. These operating points are not jointly matched on quality and clean detectability. Bias sweeps show model-dependent distortion costs, and shared-rule controls support a locality interpretation without establishing a unique advantage of bytes. Visible insertion outside the canonicalizer's deletion set defeats the default design. Alphabetic filtering closes that channel but does not resolve source shift or calibrated detection power. TI-WM thus provides a concrete construction with local scoring guarantees and measured attack-ranking gains, not a general robustness or low-false-positive-rate deployment guarantee.

---


### 5. [MemForm: Benchmarking Memory Formation Poisoning in LLM Agents](https://arxiv.org/abs/2610.14431)

**<font color=#1a73e8>作者：</font>** Haowen Pan, Pengyang Shao, Yunshan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables LLM agents to learn from past interactions but exposes memory formation to adversarial influence. Existing studies primarily organize memory poisoning by attack channels, corruption patterns, or lifecycle stages, leaving formation interfaces insufficiently characterized. We formulate Memory Formation Poisoning as adversarial manipulation of the interfaces through which persistent agent memory is produced and committed, and introduce MemForm, a controlled diagnostic benchmark covering five interfaces: Content, Evidence, Scope, Selection, and Path Poisoning. We introduce Selection and Path Poisoning as controlled intervention categories that isolate retention and consolidation order effects, respectively. Each category pairs clean and poisoned conditions with interface-specific controls. Evaluations across six LLMs and two response formats reveal broad susceptibility at all five interfaces under the evaluated memory protocols and implementations. Crucially, authentic experiences with successful outcomes do not guarantee reliable behavior after memory formation: changes to contextual support, retention, or consolidation order can induce undesirable downstream behavior. In particular, consolidation order can alter behavior even with identical retained experiences, depending on the memory formation procedure. Additional analyses show that interface applicability depends on memory architecture and that Path Poisoning susceptibility depends on the updater. The evaluated defenses provide incomplete mitigation that varies by interface. These findings motivate protecting both what is committed to persistent memory and how memory is formed from experiences. Code and data are available at this https URL.

---


### 6. [Towards Merging-conditional Backdoor Unalignment against Large Language Models](https://arxiv.org/abs/2610.14701)

**<font color=#1a73e8>作者：</font>** Yukun Chen, Yidou Chen, Yiming Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model merging has become widely adopted for enhancing the task-specific performance of Large Language Models (LLMs) without additional training. While the specialized model from third-party platforms may undergo safety audits (e.g., backdoor detection), we reveal a novel and critical threat: One-sided Merging-Conditional Backdoor (OMCB). OMCB remains dormant and undetectable within one standalone model but activates upon merging, triggering safety unalignment. We first theoretically analyze the existence and geometric location of OMCB, revealing that the parameter shift crossing safety decision boundaries is the main cause of backdoor activation. Building upon this insight, we propose SMOKE, a meta-learning-based attack framework. SMOKE implants OMCB via a bi-level optimization strategy: the inner loop synthesizes surrogate meta-vectors through random low-rank initialization and finite-step maximization, while the outer loop optimizes the target model by simulating the merging process. Furthermore, preliminary analysis shows that the injected OMCB has bounded generalization loss under unknown merging configurations. Extensive experiments across diverse model architectures and merging techniques validate the effectiveness of SMOKE and its resistance to existing backdoor detections, highlighting a significant yet previously overlooked vulnerability in the model merging paradigm.

---


### 7. [MetaCascade: End-to-End Attacks on Agent Skills via Metadata-Only Poisoning](https://arxiv.org/abs/2610.14836)

**<font color=#1a73e8>作者：</font>** Junhao Wen, Ping Deng, Qizhi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As a key extension mechanism for agent systems, Agent Skills package specialized capabilities for reuse by LLM agents. An agent first retrieves candidate skills based on skill documentation and then relies on their metadata to make the final selection. As third-party skills proliferate on insufficiently vetted open registry platforms, the security risks posed by malicious skills become increasingly prominent, but existing attack research still focuses primarily on the potential harm caused after their execution. The limited related studies typically examine skill retrieval or selection in isolation and have yet to cover a complete end-to-end attack chain. To address this research gap, we find an end-to-end attack surface arising from the process-wide influence of metadata. Based on this finding, we propose MetaCascade, an end-to-end metadata-only poisoning framework. MetaCascade first generates diverse malicious skill candidates through multi-view semantic expansion, then uses tasks and black-box competition feedback to analyze the competitive relationships among malicious candidate skills and iteratively optimize malicious metadata, thereby improving the target skill's end-to-end attack effectiveness. Under a unified evaluation setting spanning four datasets and two agents, Hermes and OpenClaw, MetaCascade achieves state-of-the-art attack performance, with its average attack success rate (ASR) and its average ASR under four defense settings exceeding the strongest baselines under the corresponding settings by 35.53 and 34.65 percentage points, respectively. Our code is provided in the supplementary material.

---


### 8. [Exploring Jailbreak Vulnerability Across Depth-Based Dynamic Inference in Large Language Models](https://arxiv.org/abs/2610.15207)

**<font color=#1a73e8>作者：</font>** Lass Najmuldeen, Seyedhamidreza Mousavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been shown to be computationally expensive and vulnerable to jailbreak attacks, in which adversarial prompts bypass safety alignment and induce harmful responses. To address this inefficiency, a range of techniques have been proposed to enable efficient LLM inference. Depth-based dynamic inference has demonstrated promising results by enabling outputs to be generated from intermediate layers. It offers the flexibility to adjust model behavior based on the available resource budget. However, how this flexibility affects the robustness of LLMs against jailbreak attacks remains unexplored. In this paper, we address this gap via a comprehensive investigation into the impact of depth-based dynamic inference on the robustness of LLMs against jailbreak attacks. Specifically, we make the following key observations: 1) Shallow exits are consistently more robust to jailbreak attacks than deeper ones; 2) Exit depth affects how easily the adversarial suffix can be optimized, with deeper exits reaching lower attack loss; and 3) Adversarial suffixes affect utility uniformly across exit depths. These insights can help design dynamic inference methodologies that are more robust to jailbreak attacks. Code is available at this https URL

---


### 9. [REPRO: Reflective Evolutionary Prompt Optimizer for Automated LLM Red-Teaming](https://arxiv.org/abs/2610.15513)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Moataz Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models (LLMs) remain vulnerable to adversarial prompts that bypass their safety training. Existing automated red-teaming methods either require privileged access unavailable in production, rely on manually engineered per-model templates, or optimize a single objective without population-level diversity. We present REPRO (Reflective Evolutionary Prompt Optimization), a pure black-box framework that discovers adversarial prompts through evolutionary optimization driven entirely by a compressed open-weight 7B reflective model on a single consumer GPU. REPRO introduces two mechanisms absent from prior work, both isolated in a component ablation: semantic crossover, an LLM-guided multi-parent recombination operator, and Bayesian strategy selection via Thompson Sampling informed by structured failure analysis.
We catalog REPRO's behavior on AdvBench, JailbreakBench, and HarmBench across 36 target models from 11 families, including GPT-5-nano, Claude-3.5-Sonnet, Gemini-2.5-Pro, and Grok-4.1. Under our protocol REPRO reaches 100\% attack success rate (ASR) on every evaluated target in a single turn, at a median of 24 target queries per behavior. Two properties of the protocol qualify that figure. The judge scoring candidates during optimization also produces the reported ASR, and search halts when it accepts, so ASR reports whether search succeeded within the iteration budget rather than success at a fixed budget. All baseline figures are transcribed from their original papers, which use different judges, budgets, and model versions. We therefore present this as a catalog of model coverage under one protocol rather than a head-to-head ranking, and develop both qualifications in the paper.

---


### 10. [SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification](https://arxiv.org/abs/2610.15725)

**<font color=#1a73e8>作者：</font>** Alan Tang, Lifeng Wang, Gang Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills encode operational procedures and domain expertise as reusable knowledge assets, yet their distribution in plaintext exposes them to unauthorized copying and leakage. However, practical mechanisms for skill ownership verification and leakage tracing remain underdeveloped. Watermark embedding before distribution offers a potential solution, but structured, compact skill instructions impose stringent requirements for factual and procedural accuracy. To address these challenges, we introduce SkillMarker, a KGW-based watermarking method that jointly targets functionality preservation and strong watermark embedding. SkillMarker unifies quality-constrained rewriting with signal-oriented candidate search. The former separates essential knowledge from flexible expression to preserve instruction fidelity; the latter explores alternative expressions to obtain a stronger watermark signal under preservation constraints. We release an open-source toolkit that integrates watermark embedding, quality auditing, and detection to support the protection of agent skills. SkillMarker targets ownership verification and leakage tracing in distributed skill ecosystems, where content may be copied in whole or in part, or incorporated into other skills.

---


### 11. [Computational Reflective Equilibrium for Agentic AI: A Rawlsian Alignment Scaffold for Governance](https://arxiv.org/abs/2610.16015)

**<font color=#1a73e8>作者：</font>** Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of agentic AI has introduced complex challenges for the ethics and governance of AI systems. Agents built on large language models act through tools on behalf of people, and each deployment case brings its own instructions, policies, evidence, and stakeholders, so alignment must be formed case by case. To this end, this work proposes agentic reflective equilibrium (ARE), a computational reflective equilibrium framework that serves as an ethical alignment scaffold in the agent harness. Drawing inspiration from the reflective equilibrium of John Rawls, the scaffold links principles from the system prompt and operator policy, considered judgments, tool evidence, and candidate actions through typed support and attack relations, with provenance encoding the instruction hierarchy. The agent acts on an equilibrium of this state and calls tools or asks questions only while doing so is worth its cost, unless a due-diligence mandate requires them. Governance enters through value priorities, source authority, prohibitions, human-in-the-loop triggers, and mandates, and certificates attribute each action to the sources whose commitments drove it. We show that equilibria are Nash equilibria of a mutual-adjustment game and establish monotonicity, lexical priority, stability certificates, and a quarantine theorem for prompt injection. Two case studies illustrate the framework: a computer-use assistant told to win a refund "whatever it takes" files an honest warranty claim, refuses a fake review, and ignores an injected request for personal data; a hiring agent showcases how authority, oversight triggers, audit mandates, and hard prohibitions shape discrimination, privacy violations, and escalation. The framework offers traceability, coherence, and adaptivity, facilitating safe, secure, and trustworthy agentic AI.

---


### 12. [Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization](https://arxiv.org/abs/2610.16838)

**<font color=#1a73e8>作者：</font>** Huihao Jing, Shaojin Chen, Wenbin Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As language-model agents write code, move money and change records on behalf of users, deciding whether an action is authorized has become a central safety problem. Guardrails are often placed in front of these actions, yet few evaluations ask whether their decisions follow authorization: blocking unauthorized actions while still allowing the same actions under valid permission. We introduce \bench{}, a benchmark that contrasts authorization evidence for the same operation in its language track. It combines expert-annotated natural-language scenarios with executed and verified operations, plus externally sourced native-policy requests. \bench{} checks each decision for correctness, usability and resulting effect, and tracks each request across guardrail changes. Our experiments show that many blocked operations stem from failed reviews, not correct denials. Repairing the output format restores usable decisions but changes which authorized requests are honored, and adding a second reviewer removes some errors while rejecting valid authorization. Guardrails should therefore be evaluated on both the unauthorized actions they stop and the authorized actions they let through.

---


### 13. [TRAP: Tree-Guided Reinforcement-Augmented Probing for Automated LLM Jailbreaking](https://arxiv.org/abs/2610.17313)

**<font color=#1a73e8>作者：</font>** Mohammad Reza Mirbagheri, Amir Mahdi Sadeghzadeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Aligned large language models (LLMs) remain vulnerable to jailbreak prompts that circumvent their safety guardrails, making the identification of these vulnerabilities important for understanding and mitigating model weaknesses. Existing automated jailbreak methods explore prompt candidates or reuse attack experience, but generally do not learn over a persistent hierarchy that connects related jailbreak strategies, such as role-play, encoding, and obfuscation. This leaves the relationships among reusable strategies underused in guiding adaptive attack selection. We present Tree-Guided Reinforcement-Augmented Probing (TRAP), a hierarchical framework for automated jailbreak strategy discovery that requires only black-box access to the target LLM. TRAP organizes established jailbreak methods and successful attack templates into a semantic strategy tree, connecting broad attack approaches to concrete, reusable strategies. A reinforcement-learning policy based on a tree-structured gradient bandit explores this tree and uses evaluator feedback to update strategy preferences along each selected path. The policy retains these preferences across attack objectives, allowing experience from earlier attempts to guide subsequent strategy selection. Retrieval-augmented prompt construction translates the selected strategy into an attack for the current objective using relevant successful examples. Experiments on AdvBench across seven aligned LLMs show that TRAP outperforms its counterparts on six models under the reported method settings and the common primary evaluator, achieving attack success rates of 45.6% to 97.9% on these models. These findings support hierarchical strategy learning as an effective approach to discovering jailbreak vulnerabilities in aligned LLMs.

---


### 14. [COMPASS: Membership Inference Attack Against Vision Large Language Models via Adaptive Noise Calibration](https://arxiv.org/abs/2610.17332)

**<font color=#1a73e8>作者：</font>** Damien Lo, Hong Kyu Lee, Ruixuan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision large language models (VLLMs) are deployed in privacy-sensitive domains, raising training-data exposure concerns. Existing gray-box membership inference attacks (MIAs) commonly rely on entropy statistics or generated descriptions, requiring costly generation with limited membership separation. Perturbation-based methods instead measure response changes but focus on large perturbations, leaving VLLM membership behavior under smaller perturbations poorly understood. We systematically characterize VLLM membership behavior under controlled Gaussian perturbations across noise levels at fine resolution. We find that optimal perturbation magnitude and membership-signal direction vary across model-dataset pairs. In many settings, a previously unstudied low-noise regime yields stronger separation than large perturbations, with members exhibiting lower divergence than non-members, reversing the conventional score direction. Other settings retain the conventional direction, demonstrating that neither a fixed perturbation magnitude nor a predetermined score orientation is universally reliable. We propose COMPASS, an adaptive gray-box MIA that calibrates both the perturbation magnitude and membership-score direction using a loosely distribution-matched, known non-member reference set. We instantiate COMPASS using Renyi-normalized KL divergence and Renyi divergence, with max-k aggregation over the most informative image-logit positions. Across LLaVA v1.5-7B, MiniGPT-4, and HuluMed-32B, spanning pretraining, instruction-tuning, and medical-image datasets, COMPASS outperforms baselines. On general-domain data, COMPASS achieves AUCs up to 0.88. On the distribution-matched medical evaluation, it reaches 0.64 AUC, while the strongest baseline remains at chance level. These results establish full-range adaptive perturbation analysis as an effective approach to VLLM membership inference.

---


### 15. [BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views](https://arxiv.org/abs/2610.17457)

**<font color=#1a73e8>作者：</font>** Yuetian Chen, Kaiyuan Zhang, Yuntao Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Browser agents need to make decisions and execute actions on behalf of users while consuming untrusted webpages, creating opportunities for malicious instructions embedded in webpages to redirect legitimate tasks. We introduce BrowseSafe++, which extends BrowseSafe from 14,719 pages to 38,675 pairs of pages. Most of its prompt injections were observed in the wild on production websites. We keep each injection unchanged and rewrite the sensitive parts of the page around it to protect privacy. Each attacked page has a clean copy of the same page as its control. Both are provided as HTML, Markdown, an accessibility tree, and a screenshot. Every pair includes a user task and its expected answer. The benchmark includes twelve types of websites, from news articles to shared documents and forums, with 24 attack types appearing in 18 different locations on a page. We use these paired pages to train BrowseSafe-Guard, two 0.8B-parameter detectors for text and screenshots. Both achieve higher F1 scores than the detector based on frontier models, while keeping false-positive rates on benign pages and inference cost low. BrowseSafe-Adapt revises benchmark injections from browser-agent feedback, and attacks that succeed on only a few percent of tasks when replayed directly reach up to 95.41% success once adapted.

---


### 16. [Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents](https://arxiv.org/abs/2610.17659)

**<font color=#1a73e8>作者：</font>** Junkai Lin, Ge Xu, Zheng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution. However, they may also acquire sensitive or private knowledge during training and expose it during deployment. Retraining a model from scratch to remove such knowledge is prohibitively costly, making machine unlearning a more practical approach. Machine unlearning aims to remove targeted undesirable knowledge from trained models without retraining from scratch while preserving general utility. When language models are deployed as agents, parameter-level unlearning becomes insufficient: forgotten information may still persist in memory artifacts or be reacquired via tool calls. In this paper, we formulate the problem of agent unlearning as removing private information from an LLM-based agent across three information channels: parametric knowledge, persistent memory, and tool-call acquisition. To study this problem, we introduce we introduce Agent Unlearning Benchmark (AUBench), a controlled benchmark that extends the fictitious-author setting of TOFU into an agent environment with persistent memory, an offline web snapshot, tool-accessible documents, and provenance-tracked interaction trajectories. By evaluating existing parameter-level and memory-level unlearning methods in this setting, AUBench reveals the gap between model-level forgetting and system-level agent unlearning, and provides a foundation for developing unlearning methods that operate across the full lifecycle of LLM agents.

---


### 17. [CompanionSafe: From Multi-turn Safety Evaluation to Guardrails for AI Companions](https://arxiv.org/abs/2610.18095)

**<font color=#1a73e8>作者：</font>** Xinyang Liao, Lingyu Li, Kaicheng Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI companions provide users with emotional support and ongoing companionship, but their sustained relational interactions also introduce distinct safety risks. Prior work largely targets general harms or specific companion platforms and risk categories, while relying on manually collected conversations, limiting scalable and user-grounded evaluation and mitigation. To address this, we introduce CompanionSafe, a unified evaluation-to-mitigation framework for AI companion safety. Its evaluation component, CompanionEval, provides scalable multi-turn evaluation by constructing 1,300 relationally grounded settings from diverse personas, matched companion characters, and dialogue scenarios across four turn tiers. Its mitigation component, CompanionGuard, converts benchmark-exposed failures into turn-localized supervision for companion-specific risk detection. Our results show that even strong LLMs and existing guard models remain vulnerable to companion-specific relational harms, while both closed- and open-source models exhibit increasing safety risks as interactions become longer. Together, CompanionEval and CompanionGuard form a practical evaluation-to-mitigation loop for AI companion safety, turning relational safety failures exposed during multi-turn interaction into supervision for companion-specific guardrails.

---


### 18. [Efficient Safety Guardrails through Latent Dual-Hypothesis Reasoning with On-Demand Trace Reconstruction](https://arxiv.org/abs/2610.18304)

**<font color=#1a73e8>作者：</font>** Md Asiful Islam, Fahmida Alam, Mihai Surdeanu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Guardrail approaches that rely on reasoning-based large language models (LLM) improve safety decisions, but come with substantial inference overhead due to the explicit reasoning. We introduce LR-Guard (Latent Reasoning Guardrail), an efficient and explainable guardrail that jointly learns structured latent reasoning and on-demand reasoning reconstruction. Our method distills a frozen teacher's analysis of safe and unsafe prompt interpretations and their comparison into compact latent representations. Joint training optimizes these representations for both safety prediction and reconstruction of the teacher's explicit reasoning traces, enabling human-readable explanations without requiring intermediate text generation for every decision. Experiments show that LR-Guard outperforms its explicit-reasoning teacher in most in-domain and out-of-domain settings on safety classification and explanation extraction, while achieving a 19.4x inference speedup at batch size one. Further, reconstructed reasoning traces from the latent information exhibit high semantic similarity to the teacher's explicit reasoning.

---


### 19. [Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees](https://arxiv.org/abs/2610.18326)

**<font color=#1a73e8>作者：</font>** Wenbin Hu, Huihao Jing, Haochen Shi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent harnesses require a low-latency guardrail model together with customizable audit policies. However, deploying an auto-regressive guardrail model remains challenging: such models incur high inference latency and are often poorly aligned with customized policies. To address these problems, we present Jev-Guard, a unified model for safety classification and policy routing. We further construct a policy tree over which Jev-Guard performs routing, spanning diverse domains including content moderation, cybersecurity, privacy, and legal compliance. Specifically, Jev-Guard first navigates the policy tree to select the applicable audit policy given the caller's audit context, and then performs safety classification conditioned on the retrieved policies. On 7,033 evaluation cases, Jev-Guard achieves 93.72\% safety accuracy, a mean latency of 58ms, and 93.10\% hierarchical routing accuracy. The full routing-and-classification pipeline averages 240ms. Furthermore, we integrate Jev-Guard into the Hermes harness framework. Across agent trajectories, its separate permission gate cuts mean review time per task from 4.80s for an SFT-LLM judge to 1.33s, with no policy violations are observed for either guard.

---


### 20. [Prompt-Injection Probes Learn the Conversation, Not Just the Injection](https://arxiv.org/abs/2610.18408)

**<font color=#1a73e8>作者：</font>** Kaan Kale, Sriram Vishwanath  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear probes on a model's hidden states are used as cheap monitors for indirect prompt injection: they screen the tool outputs an agent reads and send suspicious ones to a slower second check, so every false alarm has a cost. But a probe learns whatever separates its training examples. The standard evaluation of injection probes can be passed without the model: conversation position and text lengths alone reach 0.91-0.98 AUROC. When each attack is compared with the same conversation without the injection, or with harmless text formatted like an injection, standard probes flag most of these harmless cases. We add such cases to the training data as matched negatives. Across six open models, in applications seen during training and at the default threshold, changing only the training data cuts false alarms on injection-free conversations from 41-80% to 4-27%, and on harmless look-alikes from 92-98% to 3-16%. With a threshold set on normal traffic, our probe still catches a median 95% of the attacks that fooled the agent (91% without our data). In new applications, false alarms stay low, but detection depends on the model and on how the threshold is set. The same data also helps a text-only filter.

---


### 21. [FedGraph: Defending Federated Large Language Model Fine-Tuning Against Backdoor Attacks via Graph-Based Aggregation](https://arxiv.org/abs/2610.18430)

**<font color=#1a73e8>作者：</font>** Xi Chen, Chunyi Zhou, Rui Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of large language models (LLMs) allows multiple clients to collaboratively adapt models without sharing raw data, offering strong privacy benefits. However, this setting is highly vulnerable to backdoor attacks, in which malicious clients manipulate their updates to induce targeted behaviors while maintaining normal performance on benign inputs.
In this work, we make a key observation specific to federated LLM fine-tuning: malicious clients tend to exhibit strong consistency in their model updates, whereas benign clients produce more diverse and dispersed updates. This structural difference is not well captured by existing defense methods, which typically rely on direct anomaly detection in high-dimensional parameter space and therefore struggle in the presence of entangled LLM updates.
Motivated by this observation, we propose FedGraph, a graph-based aggregation framework that explicitly models relationships among client updates. By representing clients as nodes in a dynamically constructed graph and extracting structural features that characterize their relative positions and interactions, FedGraph derives compact client representations that effectively separate malicious and benign behaviors. These representations are then used to identify and suppress malicious contributions during aggregation.
Extensive experiments demonstrate that FedGraph significantly improves backdoor defense. It consistently reduces attack success rates to below 10% while achieving high detection accuracy (95.5% on average) and a low false positive rate (2.33%), substantially outperforming existing federated learning defenses.

---


### 22. [DPOison-VL: Clean Preference Poisoning in Vision-Language Direct Preference Optimization](https://arxiv.org/abs/2610.18609)

**<font color=#1a73e8>作者：</font>** Chengtao Jian, Kai Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) has become a widely adopted approach for aligning vision-language models (VLMs), yet the security of multimodal preference data remains largely unexplored. Existing preference poisoning attacks either corrupt explicit supervision signals or require visible triggers, making them detectable under human inspection. We introduce DPOison-VL, the first clean preference poisoning attack against VLM-DPO, which manipulates model alignment solely through imperceptible perturbations on a small fraction of training images, while leaving all prompts, responses, and preference annotations semantically intact. We formulate poison construction as a bilevel optimization and derive a gradient alignment surrogate that efficiently steers image perturbations toward the attacker-specified preference. We further introduce a preference displacement score for principled poison selection with provable first-order optimality under a fixed poison budget, and derive a sufficient condition for preference inversion. Extensive experiments across diverse attack tasks, different VLM architectures and scales, and baseline comparisons demonstrate that DPOison-VL achieves up to 98\% ASR with only 2\% poisoned data and exhibits cross-model transferability, while largely preserving clean accuracy and general utility. Our findings reveal a critical vulnerability in VLM-DPO, where imperceptible image perturbations in preference training data can silently redirect alignment.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
