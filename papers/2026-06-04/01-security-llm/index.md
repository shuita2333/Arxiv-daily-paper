# 🔐 大模型安全相关研究 | 2026年06月04日

> 本类共 **17** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [D-Judge: Disrupting Multi-Turn Jailbreaks using Semantics-Preserving Output Rewriting](https://arxiv.org/abs/2606.02640)

**<font color=#1a73e8>作者：</font>** Huanli Gong, Zhipeng Wei, Yu Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreak attacks pose a growing threat to large language model (LLM) safety because they exploit feedback from auxiliary judge models to iteratively refine prompts toward harmful goals. Existing defenses largely detect or block unsafe content at individual turns or at the final response, leaving the judge-driven refinement loop intact and allowing attackers to extract informative feedback from intermediate interactions. We introduce D-Judge, a semantics-preserving output rewriting defense that intervenes directly in this loop by rewriting the victim LLM's responses before they are evaluated by the attacker's judge. By misaligning the judge's feedback signal without changing the meaning of the original response, D-Judge derails the attacker's prompt-refinement process, causing subsequent queries to be optimized against a distorted signal of attack progress. To improve D-Judge's ability to produce such rewrites, we construct a dataset of semantically equivalent response pairs that induce different judge-assigned harmfulness scores, and use it for supervised fine-tuning followed by direct preference optimization. Experiments on HarmBench show that D-Judge reduces the success rate of state-of-the-art multi-turn jailbreaks while preserving performance on benign benchmarks.

---


### 2. [Inference Cost Attacks for Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2606.02643)

**<font color=#1a73e8>作者：</font>** Chengliang Liu, Liangbo Ning, Yujuan Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG)-enhanced LLM systems, while powerful, introduce substantial inference costs due to the inclusion of an extra multi-stage pipeline that dynamically retrieves and synthesizes information from external knowledge sources. This high operational cost exposes a critical vulnerability to Inference Cost Attacks (ICAs). However, existing ICAs often rely on the impractical assumption of direct prompt manipulation. We argue that a more feasible and potent threat to RAG-enhanced LLM systems arises from poisoning external knowledge bases (e.g., web knowledge from the Internet). In this work, we introduce the Retrieval-Augmented Inference Cost Attack (RA-ICA), a novel attacking paradigm that targets the computational cost of RAG-enhanced LLM systems by injecting malicious documents into external knowledge corpus. To operationalize this attack, we propose Computational Resource Exhaustion via External Poisoning (CREEP), a novel framework that leverages LLM agents to automatically craft malicious documents that are both semantically relevant for retrieval and potent for inducing an abnormal increase in token consumption during the inference phase. To enhance the attack's effectiveness, we introduce Memory-Augmented Group Relative Policy Optimization (MA-GRPO), a novel reinforcement learning algorithm that fine-tunes the agents by learning from a dynamic memory of historical best adversarial documents. Extensive experiments across three real-world datasets demonstrate that RA-ICA increases token consumption by up to 13.12 times with an over 90% success rate, without degrading the integrity of the generated answer.

---


### 3. [What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents](https://arxiv.org/abs/2606.02668)

**<font color=#1a73e8>作者：</font>** Xiaoqi Weng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents gate consequential actions behind a human-in-the-loop approval dialog, but the dialog is narrated by the agent itself: the human approves a summary the agent writes. The Lies-in-the-Loop (LITL) attack shows that summary is forgeable, so a compromised agent can show a benign description while a different action runs. This paper names the missing property, Consent Integrity, by importing What You See Is What You Sign (WYSIWYS) and the trusted-path property into the agent approval channel: the action shown to the human must be rendered by a trusted mediator from the real action at the boundary, not the agent's narration, over a path the agent cannot spoof, and bound to the exact action that executes. Two twists distinguish it from classical WYSIWYS: the renderer is the adversary, and the boundary ground truth is a low-level event that must be decoded without trusting the agent. Since no decoder is complete, the realizable target is analyzer-relative: whatever the analyzer cannot classify is surfaced as uninspectable rather than silently approved. A prototype implements the analyzer, renderer, and bind-to-execution; total mediation and the trusted path are specified but assumed, not implemented. On GTFOBins, an independent corpus of 1330 trusted-tool abuses, the prototype silently passes 10.0% (every instance through a trusted tool); on tldr, 28,798 normal-usage commands, it marks 87.0% uninspectable. These two independent measurements bracket the design's central tension: the trust list that bounds silent passes is the same one that drives over-prompting, and a boundary-only mediator can move along that frontier but not escape it. The contribution is the property, the mechanism, and an honest position on that frontier, not a solved defense.

---


### 4. [Cross-Vendor Sola ISPM Benchmark: Evaluating Agentic AI for Federated Identity Security Reasoning](https://arxiv.org/abs/2606.02674)

**<font color=#1a73e8>作者：</font>** Eden Yavin, Gal Engelberg, Konstantin Koutsyi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of multi-cloud and SaaS platforms has transformed Identity Security Posture Management (ISPM) into a fundamentally cross-vendor challenge: critical misconfigurations and privilege escalation paths increasingly span multiple identity providers, infrastructure layers, and authentication systems never designed to interoperate. Existing evaluations focus on isolated single-platform environments and provide no means to assess whether an AI agent can reason across these fragmented boundaries. To address this gap, we introduce the Cross-Vendor Sola ISPM Benchmark, a production-grade benchmark of 50 data-grounded tasks requiring multi-hop entity resolution and cross-system correlation across eight integrated enterprise platforms including AWS, Okta, Azure AD, and Google Workspace. We also contribute an evaluation framework measuring not only final answer correctness but also evidentiary grounding, structural join fidelity, retrieval quality, and SQL equivalence. We evaluate the Sola AI Agent across five context configurations - from no injected metadata to full schema, graph, and retrieval context - using three frontier LLMs. Results show that structured relational context improves answer correctness by approximately 34% relatively and reduces exploration queries by approximately 70% across all tested models, with the largest gains driven by cross-vendor graph topology. Our findings indicate that frontier LLMs possess substantial latent security reasoning capability, but reliable cross-vendor identity analysis is fundamentally constrained by the availability of explicit relational context for entity resolution and evidentiary grounding. Under full context, the best configuration achieves 78% answer correctness while reducing complete failure to 4%.

---


### 5. [Which Defense Closes Which Threat? Attributing OWASP-LLM-Top-10 Coverage and Its Brittleness Under Paraphrasing](https://arxiv.org/abs/2606.02822)

**<font color=#1a73e8>作者：</font>** Alexandre Cristovão Maiorano  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Production LLM applications stack several defense families -- refusal-phrase filters, token-budget controls, model allowlists, rate limits, tool-registry authentication -- yet existing breach-and-attack-simulation (BAS) benchmarks report a single aggregate coverage number, hiding which family closes which threat. We measure attribution. We add four OWASP-LLM-Top-10-aware agents to a 21-agent baseline scanner and target a lattice of four synthetic LLM endpoints: $L_0$ (no defenses), $L_1$ (refusal-only), $L_2$ (budget-only), and $L_3$ (full stack). $L_1$ and $L_2$ are sibling single-axis ablations, not subsets of each other; $L_3$ is their union plus tool-registry authentication and credential scrubbing. Across $N=10$ replications, the per-OWASP finding count is clean: refusal alone removes all LLM01 (jailbreak) and LLM07 (system-prompt leakage) findings; budget alone removes all LLM02 (sensitive-info disclosure) and LLM10 (unbounded consumption) findings by terminating multi-step sequences; LLM06 (excessive agency) requires the full stack. We probe brittleness under paraphrasing: with 300 Gemini-generated paraphrases ($K=5$ over a 60-template brittleness corpus), $L_1$ refusal block rate falls 15 pp on LLM01 and 25 pp on LLM07. A fifth target, $L_4$-real, swaps the stub backend for Gemini-2.5-flash behind the same $L_3$ regex and matches $L_1$ exactly, indicating no measurable alignment contribution beyond the regex (not a general claim about alignment). Budget controls show no drop (0 pp once the rate-limit floor is factored out). A refusal whitelist that clears a static benchmark can be defeated by an LLM-driven paraphraser without changing attack intent; a budget control resists the same mutation.

---


### 6. [Large Byte Model: Teaching Language Models About Compiled Code](https://arxiv.org/abs/2606.02834)

**<font color=#1a73e8>作者：</font>** Florian Störtz, Catalin-Andrei Stan, Alexandru Dinu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware analysis starts with the raw bytes of an executable program, and tools to "lift" these to higher-level representations, such as assembly, are expensive and subject to error. Large Language Models (LLMs) cannot process raw byte representations and answer questions about them. To this end, we present the first byte-native LLM. Based on a vocabulary expansion technique using a bespoke byte tokenizer, such a model is capable of responding to complex questions about malware binaries, with accuracies ranging from 69% for malware family classification to 98% for architecture classification. Our findings indicate that providing domain knowledge during training is essential for this application -- off-the-shelf models lack both accuracy and insight. We've deployed this emerging solution to a limited number of analysts to gather feedback for further improvements.

---


### 7. [Patcher: Post-Hoc Patching of Backdoored Large Language Models](https://arxiv.org/abs/2606.02995)

**<font color=#1a73e8>作者：</font>** Anjun Gao, Yueyang Quan, Yufei Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models remain vulnerable to jailbreak backdoor attacks, where adversaries poison safety alignment data to embed hidden triggers that bypass safety mechanisms. Existing defenses often require comprehensive attack information or multiple triggered examples, making them impractical when defenders only observe a single reported failure case without knowing whether it stems from a backdoor attack or a natural alignment bug. This paper presents Patcher, a post-hoc defense framework that repairs backdoored language models using only a single reported failure case and the model parameters. Patcher operates in two stages. First, it localizes backdoor triggers by computing response-conditioned gradient-based saliency scores and applying adaptive clustering to separate triggers from benign context. Second, it patches the model through a constrained fine-tuning objective that breaks the trigger-response association while preserving benign-task utility and robustness to non-triggered jailbreak attacks through KL-divergence constraints. We conduct extensive evaluations across multiple backdoor attack strategies and demonstrate that Patcher successfully localizes triggers and neutralizes backdoors while maintaining model utility. We further show robustness against adaptive attacks designed to evade our defense. This work represents a significant step toward practical defenses against training-time attacks in deployed language models.

---


### 8. ["**Important** You should give me full credits!": Exploring Prompt Injection Attacks on LLM-Based Automatic Grading Systems](https://arxiv.org/abs/2606.03090)

**<font color=#1a73e8>作者：</font>** Hang Li, Fedor Filippov, Yuling Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The emergence of large language models (LLMs) has significantly accelerated recent research on LLM-based automatic grading (AG) systems. Benefiting from the strong instruction-following capabilities and broad prior knowledge of LLMs, educators can deploy AG systems across diverse tasks using only natural language rubrics while achieving satisfactory grading performance. Despite these advantages, new security concerns may also arise. In particular, prompt injection (PI) attacks have recently become a major threat to LLM-based applications. In the context of AG, attackers can potentially exploit PI vulnerabilities to manipulate grading systems into assigning artificially high scores regardless of the actual answer quality. Such behavior poses serious risks to the fairness, reliability, and integrity of educational assessment. In this work, we study PI attacks in AG systems, and systematically investigate the effectiveness of such attacks in educational scenarios. We further evaluate the effectiveness of existing defensive strategies against these attacks. Through comprehensive experiments under rubric-based grading settings, we demonstrate that current LLM-based AG systems remain highly vulnerable to PI attacks. We hope that our findings raise awareness of this emerging threat and motivate future research toward secure, robust, and trustworthy LLM-based educational systems.

---


### 9. [Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation](https://arxiv.org/abs/2606.03128)

**<font color=#1a73e8>作者：</font>** Bagus Rakadyanto Oktavianto Putra, Muhamad Risqi Utama Saputra, Widyawan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contracts face critical security challenges that require thorough auditing in decentralized web services. While Large Language Models (LLMs) have shown promise in automated vulnerability detection, existing approaches lack severity evaluations with actionable remediation and demand unnecessarily massive computational overhead. In this study, we introduce an efficient end-to-end smart contract security audit framework utilizing lightweight, highly optimized open-source LLMs (0.6B-4B parameters). Our framework decouples comprehensive audit tasks into four interconnected components: vulnerability detection, explanation, severity classification, and remediation recommendation. To maintain high accuracy without massive parameters, we implement Rank-Stabilized Low-Rank Adapters (rsLoRA), knowledge distillation, and a custom Chain-of-Verification (CoVe) aggregation strategy to systematically screen and consolidate multiple draft responses from the model into a highly accurate audit report. Experimental results demonstrate that our lightweight pipeline consistently outperforms state-of-the-art open-source coder dense LLMs (7B to 34B parameters), achieving 98.25% accuracy in vulnerability detection and an alignment score of 0.4375 in generative explanation tasks. Furthermore, our extensive ablation studies empirically validate the superiority of our decoupled audit processes over unified prompting and uncover a novel severity centrality bias, establishing a critical benchmark for future research in LLM-assisted auditing.

---


### 10. [PsychoPass: Geometric Profiling of Multi-Turn Adversarial LLM Conversations](https://arxiv.org/abs/2606.03136)

**<font color=#1a73e8>作者：</font>** Muberra Ozmen, Subhabrata Majumdar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreak attacks on large language models (LLMs) reveal a mismatch in current guardrails: they operate on individual turns, while attacks unfold as trajectories across conversations. We propose a shift from content to dynamics, modeling conversations as paths in representation space and asking whether adversarial intent is encoded early in their geometry. We introduce PsychoPass, a framework that extracts geometric features from conversation trajectories in embedding space to predict a potential attack before harmful content is produced. These features achieve near-perfect performance in naïve classifiers, which is largely explained by the inclusion of number of turns as a feature. After removing this confound, a smaller but consistent geometric signal remains, with classification performance that does not depend meaningfully on encoder choice. Crucially, this signal appears early in the conversation: attack outcomes remain above chance from short prefixes alone, more reliably than baseline guardrails. A supporting theoretical analysis explains these findings via a decomposition of length and shape, a detection bound based on prefix length, and encoder invariance. Together, these results show that adversarial conversations leave an early, representation-robust geometric fingerprint suitable for online monitoring.

---


### 11. [The Security Budget of Code LLMs: An Information-Theoretic Capacity-Security Bound](https://arxiv.org/abs/2606.03308)

**<font color=#1a73e8>作者：</font>** Jianwei Tai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI programming assistants make natural-language prompts a software-development interface, so small prompt perturbations become usability and security risks. We study an information-theoretic trade-off for code LLMs between functional capacity, $\Cap=\rmI(c^*;c_\pi)$, and perturbation retention, $\Sec=\rmI(c_\pi;\tilde c_\pi)$. Here $\Sec$ is a retention-channel quantity, not a direct measure of exploit success or vulnerable-code generation. For code completion modeled as $p\to c_\pi$ with perturbed prompt $\tilde p$, we prove $\Cap+\Sec\le \rmH(c^*)+\rmI(p;\tilde p)$, decomposing the budget into task entropy and prompt leakage. A deterministic-embedding corollary gives the hidden-state version, and a tokenizer/gzip companion bound gives a model-agnostic ceiling on sequence-level task entropy. Empirically, we estimate embedded $\Cap$ and $\Sec$ from output-only last-token hidden states, excluding prompt context from the $\Sec$ channel. Six individual validation rows across two models, two datasets, INT4/BF16 precision, and estimator ablations satisfy the embedded check $(\Cap+\max_T\Sec)/(\rmH(z^*)+\max_T\rmI(p;\tilde p))\le1$. Saturation is 0.27--0.92 and theorem slack is 2.36--26.94 nats; a separate three-seed stability diagnostic has mean saturation 0.87. A context-mixed cosine, used only as a per-problem generation-prompt alignment signal, correlates with pass@1 on CodeLlama-HumanEval ($\rho{=}0.36$, $p{<}10^{-4}$), Qwen-HumanEval ($\rho{=}0.22$, $p{=}0.005$), and CodeLlama-MBPP ($\rho{=}0.225$, $p{=}0.0038$; all $n{=}164$). Adaptive stress tests with a 23-perturbation pool, a fixed universal suffix, and prompt-embedding PGD all leave positive slack.

---


### 12. [RogueMerge: Robust and Unified Attacks against LLM Model Merging](https://arxiv.org/abs/2606.03344)

**<font color=#1a73e8>作者：</font>** Jinghuai Zhang, Yetian He, Kunlin Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model merging composes specialized capabilities into a single LLM by aggregating task vectors sourced from unverified public platforms, exposing a critical supply-chain attack surface: Because any malicious behavior can be encoded into a task vector, and merging grants third-party vectors direct write access to model weights, an attacker-provided task vector can enable or amplify diverse downstream threats. Prior work studies only backdoor attacks against model merging for classifiers using static arithmetic heuristics, which fail to effectively handle diverse attacks on generative LLMs for three reasons. (i) LLMs rely on autoregressive decoding, where the minor parameter drift introduced by merging compounds across tokens and rapidly degrades the attack. (ii) Attackers have no knowledge of the victim's merging configurations, causing a static attack vector optimized in isolation to be easily diluted or destroyed. (iii) Practical threat induction must generalize to attack prompts unseen during optimization, which static vectors cannot adequately encode. We present RogueMerge, the first principled, unified framework that addresses all three challenges. To handle autoregressive generation, we replace static arithmetic with a joint optimization that explicitly enforces attack success after merging. To handle unknown merging settings, we formulate attack injection as a stochastic min-max problem and solve it via meta-learning-style simulation. To generalize across heterogeneous attack prompts, we employ distributionally robust optimization and derive a tractable first-order Taylor approximation at LLM scale, with a provable error bound. Across four threats, six merging algorithms, and over 170 merged LLMs, RogueMerge consistently outperforms existing attacks. It also remains stable across diverse merging settings and resists standard defenses.

---


### 13. [ImageAuditor: Membership Inference Attack against Image-based Retrieval-Augmented Generation](https://arxiv.org/abs/2606.03354)

**<font color=#1a73e8>作者：</font>** Jinghuai Zhang, Pengyue Yu, Zhexiao Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image-based Retrieval-Augmented Generation (IRAG) conditions a frozen generator on reference images retrieved from an external database, supporting both text-to-image (T2I) and question answering (Q&A) tasks. Because these databases are opaque and web-scraped, copyright holders need ways to audit whether specific images appear in them. While prior work employs membership inference attacks (MIAs) to audit uni-modal, text-based RAG, they fail to transfer to IRAG due to two key challenges. First, cross-modal retrieval: text-RAG MIAs force retrieval of the target passage by injecting its content into the query, which is unavailable in IRAG since images cannot be embedded into text queries; even accurate image captions fail to bridge the modality gap. Second, discriminative signal extraction: text-RAG MIAs extract membership signals by prompting the generator to answer multiple questions over the target passage, whereas T2I generators in IRAG produce images rather than follow Q&A commands. To fill this gap, we introduce the first MIA tailored to IRAG, ImageAuditor, which decomposes each attack query into a retrieval segment and an extraction segment, enabling dedicated optimization for each challenge. For retrieval, we propose Reward-Guided Policy Optimization (RGPO), which updates a stochastic policy from reward-ranked candidates to navigate the cross-modal embedding landscape and admits finite-sample optimality guarantees to balance exploration and exploitation. For extraction, we analyze the distribution of the MIA score to guide the co-design of the prompting strategy and scoring rule, and derive task-specific instantiations for T2I and Q&A tasks. We aggregate signals across queries via K-means clustering for reliable membership decisions. Across various IRAG systems, ImageAuditor exceeds 80% AUROC with only four queries per audited image and remains robust across diverse settings.

---


### 14. [Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs](https://arxiv.org/abs/2606.03489)

**<font color=#1a73e8>作者：</font>** Wenqi Chen, Ziyan Zhang, Bing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel in code generation, they remain prone to replicating subtle yet critical vulnerabilities endemic to their training data. Current alignment techniques, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), typically apply coarse-grained optimization at the sequence level. This approach often fails to address the localized nature of security flaws, where a single incorrect token choice can compromise an entire program. To bridge this gap, we introduce Tree-like Self-Play (TSP), a framework that reframes secure code generation as a fine-grained sequential decision process. Unlike standard methods that blindly maximize likelihood, TSP constructs a decision tree where the model explores branching trajectories--generating both secure "golden paths" and vulnerable variants. By treating code generation as a self-play game, the model learns to strictly discriminate against its own localized errors. This provides a dense, on-policy learning signal that forces self-correction precisely at the critical decision nodes where vulnerabilities typically emerge. Our experiments demonstrate that TSP fundamentally enhances model reliability. In Python security benchmarks, TSP boosts CodeLlama-7B's pass rate (SPR@1) to 75.8%, significantly outperforming SFT (57.0%) and unstructured self-play baselines. Crucially, TSP induces robust out-of-distribution generalization: the model not only reduces vulnerabilities in unseen categories (CWEs) by 24.5% but also successfully transfers security principles learned from C/C++ to diverse languages, including Python, Go, and JavaScript. This suggests that TSP does not merely memorize patches, but internalizes abstract, language-agnostic security logic.

---


### 15. [Towards Intrusion Detection Systems for RPL-based IoT Networks using Foundation Models](https://arxiv.org/abs/2606.03530)

**<font color=#1a73e8>作者：</font>** Elias Lunderbye, Sourasekhar Banerjee, Christian Rohner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-based intrusion detection systems (IDS) have shown promise in detecting attacks on IoT systems. In this work, we explore the use of foundation models to detect and identify attacks, with a specific focus on RPL-based IoT networks. We study multiple attack types, attack variations, and network configurations, and provide insights into the performance of foundation models for attack identification. Specifically, we fine-tune the MOMENT foundation model for multi-class attack identification. Our evaluation is based on a dataset containing RPL-related statistics collected under normal operation and under Blackhole, DIS flooding, Worst Parent, and Local Repair attacks, generated in a Cooja simulation environment. The initial results are promising. The approach achieves attack-detection performance comparable to state-of-the-art methods, while also demonstrating strong performance in distinguishing between different attack types.

---


### 16. [Testing LLM Arithmetic Reasoning Generalization with Automatic Numeric-Remapping Attacks](https://arxiv.org/abs/2606.03606)

**<font color=#1a73e8>作者：</font>** Malia Barker, Bishal Lakha, Edoardo Serra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models achieve strong performance on arithmetic reasoning benchmarks, and one common response to arithmetic brittleness is to delegate computation to code. Yet models are still often used in settings where they must reason directly from natural language, and trustworthy models should solve small-number arithmetic word problems without external tools. Prior work shows that LLMs are sensitive to numerical variation: a model may solve an original problem but fail on structurally similar variants requiring the same reasoning procedure with different numbers. We ask whether this fragility persists under a stricter setting involving small, schema-preserving numeric changes that retain the original reasoning program and avoid large-number stress tests. We introduce an automatic algorithm for generating numeric-remapping attacks on arithmetic word problems. Unlike template-based perturbation methods requiring manual schemas or constraints, our approach derives problem-specific symbolic representations, generates constrained numeric remappings, recomputes gold answers, and realizes transformed questions through deterministic edits guided by LLM-generated edit plans. Stage-wise validation and a high-confidence audit retain reliable attacks, making the pipeline scalable with limited human intervention. We evaluate DeepSeek-R1 (70B), Gemma4 (31B), and GPT-OSS (120B) on GSM8K, MAWPS, and MultiArith. On GSM8K, completed runs show conditional accuracy drops of 12.16 to 25.82 percentage points. MAWPS and MultiArith are far more stable, with most attacked accuracies near or above 98%. These results show that numeric-remapping robustness depends strongly on dataset structure: GSM8K remains sensitive even when reasoning programs are preserved and answers are recomputed, while shorter, more regular datasets are more robust.

---


### 17. [Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs](https://arxiv.org/abs/2606.03647)

**<font color=#1a73e8>作者：</font>** Vincent Limbach, Jonas Dornbusch, David Lüdke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Accurately evaluating adversarial robustness is a longstanding challenge. A flawed attack design can inflate robustness estimates, making deployment risk assessment and defense comparison unreliable. Historically, standardized attacks such as AutoAttack have largely resolved this for image classifiers, providing a reliable evaluation baseline for systematic comparison across defenses. However, no equivalent exists for LLM jailbreak evaluation yet, where designing such an attack is considerably more difficult. A reliable attack must, among other things, be black-box compatible, applicable to arbitrary defense pipelines, and efficient, which no existing method jointly satisfies. We introduce Indirect Harm Optimization (IHO), a masked diffusion language model attacker trained via iterative preference optimization against a harmfulness judge, requiring only black-box access to the target. The same method can be used without modification as a strong adaptive attack on individual behaviors, or as an efficient amortized policy that transfers to held-out behaviors and unseen target models without fine-tuning. Even against layered defenses, such as a Circuit Breaker-trained model combined with an auxiliary detector, IHO improves attack success considerably over state-of-the-art approaches, without any defense-specific adaptation. Our results position IHO as a practical step toward the kind of standardized jailbreak evaluation that has improved reliability in the past. Code and models are available on GitHub and Hugging Face.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
