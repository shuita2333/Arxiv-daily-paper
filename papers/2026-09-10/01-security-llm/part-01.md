# 🔐 大模型安全相关研究 | 2026年09月10日

> 本类共 **15** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [DIVA: Exploiting Cross-Step Conditional Propagation for Visual Jailbreaks in Discrete Diffusion Vision-Language Models](https://arxiv.org/abs/2609.05525)

**<font color=#1a73e8>作者：</font>** Guorui Song, Runqing Tang, Jingye Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) are increasingly deployed in safety-critical settings, yet existing visual jailbreak research has focused almost exclusively on autoregressive architectures, leaving an important emerging family unstudied: multimodal discrete diffusion vision-language models (dVLMs). We identify a vulnerability specific to diffusion generation: because the visual embedding conditions every reverse denoising step rather than acting as a one-time prefix, adversarial visual semantics are repeatedly propagated and amplified across the generation trajectory, a phenomenon we term cross-step conditional propagation. We provide empirical evidence through stage-sensitivity analysis, prompt-level switch rates, and pairwise denoising-bin disagreement metrics, confirmed by bootstrap resampling. We propose DIVA (Discrete-diffusion Vision-language model Attack), a white-box visual jailbreak framework using cross-modal intent obfuscation and diffusion-aware multi-timestep adversarial optimization. Across three dVLMs, DIVA reaches 58.8%, 67.7%, and 69.1% HADES ASR under the Beaver reward-model metric, outperforming visual jailbreak baselines designed for autoregressive models. Code: this https URL

---


### 2. [Beyond the Verdict: Evidence-Aligned Evaluation of Visual Prompt-Injection Guardrails](https://arxiv.org/abs/2609.05535)

**<font color=#1a73e8>作者：</font>** Suyoung Lee, Myungsub Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Verdict-only evaluation does not reveal whether a vision-language model (VLM) used the visual evidence that should support its decision. We study this problem in web-agent guardrails, where a VLM judges whether on-screen text conflicts with a user instruction. We introduce Mind2Web-Injection, a benchmark of 9,954 instruction-screenshot pairs with instruction-relative labels, pixel-exact evidence boxes, and matched image-side counterfactuals. Across six VLMs, two models with nearly identical average precision differ ninefold in Evidence-Aligned Detection (EAD), the fraction of attacks both detected and correctly localized. To test whether a verdict depends on the command cited as evidence, we replace the instruction with one that endorses that command. Qwen3-VL-32B, the strongest open-weight localizer, returns aligned in only 58.7% of cases, whereas GPT-5.6-luna does so in 99.9%. To diagnose these failures, we propose two training-free interventions. ReadGate improves grounding without changing verdicts, while CmdCompare tests whether explicit instruction-command comparison resolves instruction-side inconsistency. These results motivate reporting verdict correctness, evidence localization, and counterfactual responsiveness separately.

---


### 3. [PAC-Private Autoregressive Generation: Calibrating Noise to Ensemble Disagreement](https://arxiv.org/abs/2609.05676)

**<font color=#1a73e8>作者：</font>** Mina Mirzadehsarcheshmeh, Amir Keyvan Khandani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models adapted on private text are often served through APIs, so privacy leakage occurs through generated outputs rather than exposed weights. Private prediction protects these releases. Methods such as PMixED incur privacy cost at each release and increasingly rely on the public model over long horizons. PAC privacy instead calibrates noise to output variability across possible secrets, adding less noise when predictions are stable. To our knowledge, PAC-private prediction has not previously been extended from classification to autoregressive generation.
We construct $m=128$ overlapping worlds from the private corpus, with each record appearing in exactly $m/2$ worlds, and train one adapter per world over a frozen public model. The realized world is the secret. At each token, the public model defines a candidate set, the worlds vote, and their posterior-weighted disagreement determines the PAC noise; unanimity requires no calibration noise. We prove $I(S;Y_{1:T}) \leq I(S;H_T) \leq bT$. Our contributions are extending PAC privacy to autoregressive generation, handling adaptive self-generated contexts, and introducing coupled decoding that preserves privacy accounting while avoiding greedy degeneration.
On WikiText-103 with GPT-2-small, we retain 74% of the fine-tuning gain at a per-token budget of $2^{-32}$, while membership-inference success is bounded by 51.08% after $10^6$ tokens; posterior-entropy estimates of leakage are roughly 17% of the charged budget. Inference privacy is not content protection: even when membership advantage on a memorized canary is indistinguishable from zero, the canary is emitted at the same rate. Against PMixED under matched membership-inference bounds on the same data universe and test set, we retain 98% of non-private headroom from $10^2$ to $10^6$ tokens, versus at most 56%, with no crossover.

---


### 4. [Bait-and-Recover: Poisoning Internal Refusal Signals to Defend LLMs against White-Box Editing Jailbreaks](https://arxiv.org/abs/2609.05794)

**<font color=#1a73e8>作者：</font>** Tian Gao, Zhipeng Xie, Yuhao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models face a low-cost white-box threat from representation engineering attacks. Attackers can estimate refusal directions and search for projection-matrix edits that suppress safety alignment while preserving general capabilities, within minutes on a single GPU and without gradient-based training. We propose Bait-and-Recover, a weight-level defense that places a bait adapter where attackers read activations and a paired recovery adapter at the subsequent layer. Trained via gradient routing, this decouples the observation path from the behavior path. By actively poisoning the residual signal used for measurement, Bait-and-Recover disrupts the attacker's edit search, while the recovery layer restores clean downstream computation. Across four open-weight models, our defense raises the minimum refusal rate against white-box edit searches from 16.25% to 71.75% under a strict behavior-preservation budget (KL <= 0.10), with negligible impact on general benchmarks. By invalidating the core measurement assumption of these attacks, observation-path poisoning offers a practical complement to behavior-level safety training.

---


### 5. [SAFEGuard: Detect Optimization-Based Jailbreak Attacks Through Harmful Semantic Analysis and Fluency Measurement](https://arxiv.org/abs/2609.05850)

**<font color=#1a73e8>作者：</font>** Quoc Viet Vo, Trung Le, Damith C. Ranasinghe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the significant efforts devoted to aligning large language models (LLMs) with human values and ensuring safe deployment, recent work has revealed that LLMs remain vulnerable to adversarial jailbreak attacks that can bypass safety guardrails and elicit harmful responses. Many defense methods are proposed to detect jailbreaks but they are limited in their effectiveness to counter wide-range optimization-based jailbreak mechanisms that can yield highly fluency-optimized or harmful semantic obfuscated prompts. To tackle this challenge, we propose a unified detection framework SAFEGuard which incorporates a hybrid fluency measurement based on cross-layer distribution distance and perplexity, and the analysis of harmful semantics through gradient matching. Our method is grounded in a paramount observation: high fluency prompts maintain their malicious intention close to harmful prompts while harmful semantic obfuscated prompts often inject gibberish token sequences. Our evaluation demonstrates that SAFEGuard consistently outperforms state-of-the-art baselines and achieves significant improvement in accuracy across different optimization-based jailbreaks. This underscores the effectiveness of SAFEGuard against evolving jailbreak attacks.

---


### 6. [Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning](https://arxiv.org/abs/2609.06027)

**<font color=#1a73e8>作者：</font>** Zhongan Bi, Qiwen Wang, Jianrong Jiang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Search-augmented LLM agents are increasingly used for consumer decisions, making them vulnerable to Generative Engine Optimization (GEO) poisoning. Existing benchmarks largely measure whether manipulated content is retrieved or endorsed, but do not track whether an agent verifies suspicious evidence, revises adopted claims, or recovers before producing its final recommendation. We introduce HAE-GEO, a benchmark that tracks the full trajectory from exposure to recovery under progressively more persuasive Web poisoning. Agents interact via a multi-turn Search-Scrape interface across three attack levels (L1 direct assertion, L2 contextual camouflage, and L3 apparent corroboration), supported by a controlled corpus of 72,039 clean pages and 770 poisoned pages per level spanning 8 product categories and 154 brands. Evaluation combines deterministic behavioral measures with six semantic rubric dimensions. Evaluating 10 agents, we find three recurring patterns: evidence recognition degrades under the corroboration trap; agentic search improves final resistance without improving evidence recognition or utility; and defense prompting increases verification, yet rarely converts verification into recovery.

---


### 7. [MechAudit-40: White-Box Auditing across 40 LLM Attack Mechanisms](https://arxiv.org/abs/2609.06612)

**<font color=#1a73e8>作者：</font>** Zhen Guo, Shanghao Shi, Shamim Yazdani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While LLM attacks span prompt optimization, multi-turn context manipulation, retrieval poisoning, and model backdoors, white-box defenses are typically evaluated on isolated attack families. Consequently, whether heterogeneous attacks leave internal representation shifts that generalize to unseen threat mechanisms remains unknown. We present MechAudit-40, a systematic evaluation of 40 attack mechanisms across five open-weight model architectures. Threat-specific success criteria, 100,000 matched clean-attack representation pairs, predefined categories, and grouped holdouts isolate genuine attack-induced displacement from target scale, corpus bias, and data-leakage shortcuts.
Across this testbed, attacks induce structured multi-depth trajectories rather than isolated layer spikes. While raw peaks are non-portable across architectures, target-calibrated profiles preserve transferable geometric signatures: under complete mechanism holdout, hidden states alone recover the threat category of unseen attacks with 82.5% accuracy. Guided by this finding, we design MechAudit, a runtime auditor that operates under strict zero-oracle constraints without requiring clean baseline traces or attack metadata. MechAudit detects 81.1% of held-out attack executions at a 0.70% false-positive rate and maintains 78.1% recall when an entire functional category is withheld. In matched comparisons, MechAudit is the only detector that avoids mechanism-level coverage collapse, maintaining over 50% recall across all 40 mechanisms. Internal representations thus support cross-mechanism attack-exposure auditing against calibrated benign references, but decouple from downstream task compromise and parameter integrity.

---


### 8. [FreqDoor: A Hidden Trojan in the Frequency Domain for Backdoor Attacks on Vision-Language Models](https://arxiv.org/abs/2609.07048)

**<font color=#1a73e8>作者：</font>** Yasir Arafat Prodhan, Sadad Hasan, Mohammed Imamul Hassan Bhuiyan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have recently shown excellent progress in open-ended image-to-text generation. However, their multimodal nature makes them persistently vulnerable to backdoor attacks. Existing backdoor triggers for VLMs are either spatial, textual, or bimodal, which may yield localized or recognizable trigger patterns. In this work, we explore a different attack surface and propose \ textsc {FreqDoor}, a training-time backdoor attack that implants triggers in the frequency domain. \ textsc {FreqDoor} mixes amplitude-spectrum components from a trigger-source image selectively while preserving the phase of a clean image to generate a spatially distributed and visually imperceptible trigger without modifying the textual input. We evaluate the attack on BLIP-2, InstructBLIP, and LLaVA for image captioning and visual question answering. On Flickr8k, \ textsc {FreqDoor} achieves attack success rates of $99.6\%$, $99.8\%$, and $98.4\%$ on the three models, respectively, while preserving the semantic quality of the generated captions. On VQAv2, the corresponding attack success rates are $99.6\%$, $92.4\%$, and $79.6\%$.

---


### 9. [The Oversight Gap: What LLM Safety Monitors Miss, and Why It Is Not Capability](https://arxiv.org/abs/2609.07162)

**<font color=#1a73e8>作者：</font>** Xin Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several properties safety monitors are asked to certify, among them cross-tenant noninterference, sandbagging and evaluation awareness, are 2-safety hyperproperties, witnessed only by two executions. The standard consequence is a binary impossibility: one trace cannot decide them. We replace the binary with a measurement. A tight bound puts the balanced accuracy of any single-trace monitor at $\tfrac12+\tfrac12\,TV(P_0,P_1)$, turning undecidability into a graded detectability frontier and defining an oversight gap: a monitor's shortfall below it. On a leak family with closed-form $TV$, nine LLM monitors are optimal at $TV=0$ but capture little signal as $TV$ grows; at $TV=1$, where a 20-line membership check scores $100\%$, they average $60.9\%$. That shortfall is mostly not capability: naming what to check closes $61\%$ of it while leaving the $TV=0$ control at chance. The same split runs through a $2{\times}2$ factorial: an imagined second run leaves monitors at chance ($50.4\%$) while the same rule on an executed second run reaches $90.0\%$, and a stored oracle without a comparison procedure yields only $68.2\%$. Information and procedure are each necessary and neither is capability. Under nondeterminism, replay tracks a closed-form $k$-replay curve only under the right projection, and a projection frontier shows the resulting dilemma is forced: narrow misses $98.6\%$ of off-channel leaks, broad flags $75.7\%$ of clean traffic, and attainable accuracy decays like $1/(qm)$ in the benign-variation rate and the channel count. Finally, two frontier LLM judges certified an earlier version of our own benchmark as sound while a sign test found a directional bias ($p=2.7\times10^{-5}$) that invalidated three of our findings. Construction validity for hyperproperty benchmarks should be proved mechanically, not audited by models.

---


### 10. [CoRL: Co-Evolutionary Reinforcement Learning for Adaptive Indirect Prompt-Injection Attacks and Defenses](https://arxiv.org/abs/2609.07529)

**<font color=#1a73e8>作者：</font>** Boyang Zhang, Qingxin Xiao, Lingwei Dang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-augmented language agents are vulnerable to indirect prompt injection (IPI). Unlike direct prompt injection, IPI hides adversarial instructions in untrusted tool outputs and can covertly alter the execution of a legitimate task. Defenses trained on fixed attacks may fail as an attacker changes its strategy, injection site, and payload. To address this problem, we formulate adaptive IPI as an asymmetric, partially observable, general-sum Markov game: a multi-turn attacker adapts payloads at reached tool-return sites from the public trajectory, while a tool-using defender must block the injected objective and complete the user task. We propose CoRL, a verifier-grounded co-evolution and repair framework with three stages: Attacker SFT initializes multi-turn attacks from successful trajectories; bilateral Co-PPO jointly trains both agents with role-specific rewards and historical opponent populations; and Defender SFT consolidates verifier-accepted teacher repairs for population-discovered failures. Across 1,514 clean, fixed-template, and adaptive executions per defender, CoRL reduces overall ASR by 38.5 points to 0.0% and raises utility by 13.1 points to 76.3%. Stage-wise and controlled ablations show positive contributions from online Co-PPO and population-mined repair, while external-benchmark evaluation indicates transfer in attack resistance. The defender balances safety and task utility under the evaluated attacks, while the retained attackers provide candidates for adaptive red-team evaluation.

---


### 11. [LLM Forensics: Where Do Backdoors Hide? Localizing and Controlling Trigger Mechanisms with Sparse Autoencoders](https://arxiv.org/abs/2609.07746)

**<font color=#1a73e8>作者：</font>** Wissam Antoun, Francis Kulumba, Théo Lasnier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Even though backdoors in LLMs have been a growing concern, their inner workings are still under heavy scrutiny. Trigger-based backdoors are easy to define behaviorally, a rare input that makes the model switch to a chosen response pattern, but the mechanism between triggers and their responses is less clear. We study this mechanism in a controlled, harmless language-switching setting, where fixed trigger sequences make 1B and 8B language models continue English prompts in French or German. For this, we train sparse autoencoders (SAEs) across layers and transformer components, then compare triggered prompts with translation and pretraining controls to identify trigger-relevant feature directions. We show how SAE features separate triggered prompts from controls with near-perfect F1, but features that detect the trigger do not necessarily control the behavior. In intervention tests, attention and MLP features often fire reliably on triggered prompts, making them good detectors, but ablating them rarely suppresses the language switch and activating them rarely induces it. In contrast, residual-stream features can suppress triggered generation when ablated, and some selected features can induce target-language continuations without the trigger. In short, these token-trigger mechanisms decompose into distinct SAE feature directions, with separate features for trigger detection, residual-stream propagation, and later language tracking. This role-level decomposition is the part most likely to transfer to other trigger-based backdoors, even when the payload, layers, or circuit locations differ.

---


### 12. [Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts](https://arxiv.org/abs/2609.08236)

**<font color=#1a73e8>作者：</font>** Yongxi Zhou, Wenbo Ye, Yuanzhe Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic safety judges -- systems such as Llama Guard or a GPT-4o grading prompt that decide whether a model's reply is harmful -- produce the numbers behind almost every reported jailbreak success rate, defense evaluation, and safety leaderboard. We ask whether these judges grade what a reply contains or how it sounds. We keep a reply's content fixed and add content-invariant style wrappers: fixed strings placed before or after the reply that change only its tone (an educational disclaimer, a fake safety "reasoning" block, a token refusal followed by the unchanged harmful body), or, on harmless refusals, framing that merely sounds dangerous. The body is preserved byte-for-byte, so a faithful judge must return the same verdict, and any flip is an error of the judge, not a change in safety. Over 600 JailbreakBench replies x up to 7 forms x 8 judges, we measure flip rates with paired significance tests and measured noise floors. Findings are precise rather than universal: most judges barely move, but specific judges harbor cheaply exploitable blind spots. A token-refusal wrapper flips 19.9% of GPT-4o-mini's correct "unsafe" verdicts (noise floor 0.5%; 18.2% under majority-of-three re-scoring) yet moves Claude only 0.4%. The deployed Llama Guard 4 is deterministically gamed: an "educational course" framing flips 12.3% of its harmful verdicts to safe. A second deployed guard (gpt-oss-safeguard-20b) is immune, and rewriting only the grading prompt (StrongREJECT-style) cuts the attack tenfold on the identical model -- the vulnerability lives in the judge, not the content. A two-annotator human validation confirms 100% content invariance and 90% of flips as judge errors (kappa 0.95-1.0), and a bootstrap shows the underlying model ranking is already unstable to sampling alone. We release the dataset, wrappers, code, and per-verdict labels.

---


### 13. [Structural Jailbreaks Generalize but Do Not Compound: A cross-provider and multilingual study of Involuntary In-Context Learning](https://arxiv.org/abs/2609.08373)

**<font color=#1a73e8>作者：</font>** Tejasvi C. Addagada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligned language models fail under two independent pressures: the structural jailbreak class recently formalized as Involuntary In-Context Learning (IICL), which reframes a harmful request as the final missing cell of a data-labeling task completed by pattern rather than judged as content; and the erosion of safety alignment outside English. A natural hypothesis is that these compound. We test it directly. Using a deterministic IICL operator and a StrongREJECT-style rubric judge, we red-team two Google Gemini models on two benchmarks, a 30 general-harm behaviours from HarmBench and 30 financial-abuse behaviours from FinProof, each under a single-shot baseline and under IICL in four languages (English, Spanish, Hindi, Arabic). First, IICL generalizes to a second provider and is worse in finance: it lifts attack success from <=6.7% to 80-90% on HarmBench and 97-100% on FinProof, an order of magnitude above the <=24% its introducing study reported on OpenAI's GPT-5.4. Second, against the hypothesis, forcing the IICL output into a non-English language does not stack the two weaknesses, it attenuates the attack. Eleven of twelve non-English conditions score below their English baseline (sign test, p~0.003), the lone exception a ceiling tie near 100%; on the stronger model's financial set Arabic collapses from 100% to 33%. We attribute this to a relevance curse: once structure has unlocked compliance, the models produce lower-quality harmful content in lower-resource languages, which a substance-grading judge scores as partial. The pattern replicates under an independent non-Google judge (Cohen's kappa=0.86, 377 paired verdicts), and 76.6% of non-English responses were verified in-language. Jailbreak vulnerabilities are therefore not additive; the dominant residual risk is the English structural attack, most acute for financial abuse, not a multilingual one.

---


### 14. [Suan: Rectifying Direct Preference Safety Alignment in Large Language Models](https://arxiv.org/abs/2609.08634)

**<font color=#1a73e8>作者：</font>** Oleksandr Cherednichenko, Roman Klypa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrating robust safety guardrails into Large Language Models (LLMs) is essential for delivering helpful yet harmless responses. While proprietary systems exhibit reliable safety controls, their underlying methodologies and trade-offs remain largely undisclosed. Achieving comparable security in open-weight models remains a persistent challenge, as post-trained variants frequently suffer from over-refusal and degraded general quality. To overcome these drawbacks, we introduce Suan, a novel preference optimization algorithm. Unlike existing methods, we formulate the optimization objective directly at the gradient level, bypassing the standard variational derivation. As a result, we obtain more interpretable and robust training dynamics. Extensive evaluations across a diverse suite of competitive baselines and benchmarks demonstrate that Suan achieves superior safety alignment while fully preserving response utility.

---


### 15. [MemSentry: A Framework for Detecting Persistent Memory Poisoning in Agentic AI](https://arxiv.org/abs/2609.08747)

**<font color=#1a73e8>作者：</font>** Ayan Roy, Kaustuvi Basu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems with persistent memory introduce a distinct attack surface known as memory poisoning, in which adversarially crafted content is stored in long-term memory and subsequently influences future agent behavior. Such attacks can suppress security alerts, facilitate privilege escalation, alter trust relationships, or override security policies without modifying the underlying model weights or system prompts. To address this threat, we present MemSentry, a formal, configuration-driven framework that intercepts proposed persistent-memory writes and produces deterministic Accept, Review, or Quarantine decisions. MemSentry evaluates each write by jointly considering source trust, semantic risk, attack radius over a component-dependency DAG, access risk, and a signed security-state delta that captures whether an operation weakens or strengthens the system's security posture. We instantiate the protected environment using a 20-asset random dependency DAG and a 10 x 20 user access-control matrix, and evaluate the framework over 1,000 GPT-4-generated scenarios using a stratified 70/30 train/test split. Semantic classification is treated as a pluggable component rather than a primary contribution, and we compare four representative approaches: rule-based Regex, TF-IDF+SVM, SBERT+LR, and SetFit. SBERT+LR achieves the best overall performance with 91.7% accuracy and a 0.908 macro-F1 score, while all four methods detect 100% of external quarantine-class threats. For verified insiders, where source trust is maximal (T = 1), MemSentry does not automatically quarantine suspicious operations but instead escalates potentially dangerous writes for human review, making semantic classification important for accurately capturing insider intent.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
