# 🔐 大模型安全相关研究 | 2026年10月08日

> 本类共 **12** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Which Image Property Carries the Jailbreak? A Controlled Dissection of Image-to-Text Jailbreaks](https://arxiv.org/abs/2610.07009)

**<font color=#1a73e8>作者：</font>** Boyuan Chen, Yehia Dawoud, Hailemariam Mersha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image-to-text jailbreaks place harmful intent in text, image content, or the relationship between them. We examine image-side factors across four published attack families on a 313-prompt StrongREJECT slice, using five multimodal models and an additional appendix evaluation of InternVL3.5-8B. The harmful instruction is held constant across conditions; the baseline matrix uses one draw per prompt, and paired ablations use three draws with an automated rubric judge. A bare harmful query, with or without a benign unrelated image, produces little attack success on most victims, while attack images substantially increase it. First, per-tile entropy and JPEG size do not reliably distinguish attack tiles from size-matched benign distractors, limiting density-only screening. Second, earlier tile-count ladders were confounded by payload visibility. A corrected region-count test found no detectable effect, so the role of tile-count structure remains unresolved. Third, on Qwen3-VL-8B, the E4 manipulation that removes query-specific relatedness lowers ASR by about 0.12. This supports a bounded attribution to the relatedness manipulation, although image-text congruence remains unmeasured. A within-category control reproduces the direction on overlapping stimuli. Five tests survive the global statistical correction, but only E4 supports attribution to one measured descriptor; the within-category result is a robustness check, not a separate attribution. These conclusions remain conditional on the rubric judge.

---


### 2. [Beyond Refusal Patterns: Safe-Role Internalization for Robust and Generalizable LLM Safety Alignment](https://arxiv.org/abs/2610.07023)

**<font color=#1a73e8>作者：</font>** Jinghao Pang, Jitai Hao, Qiang Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable capabilities but remain vulnerable to jailbreak attacks that elicit harmful or unsafe outputs. Existing safety alignment approaches, including Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF), often require substantial attack-specific supervision and computational resources, while remaining susceptible to shallow safety alignment and over-refusal. To address these challenges, we introduce SSRFT(Supervised Safe-Role Fine-Tuning), the first framework that reformulates safety alignment as the internalization of a predefined safe role. SSRFT constructs a Safe-Role Question-Answer (SRQA) dataset from psychometric questions, limited jailbreak prompts, and a safe-role description. Role-consistent responses are synthesized, validated, and expanded into diverse scenarios, enabling models to internalize safety-oriented values and principles rather than explicit refusal patterns. Experiments across multiple Base and Instruct models show that SSRFT achieves more robust and generalizable safety alignment than standard SFT. SSRFT shows substantially greater robustness to prefilling attacks and better generalization to unseen jailbreak domains, while reducing over-refusal on benign queries and preserving the model's general capabilities. These results establish safe-role internalization as an effective alternative to refusal-centric safety alignment. Warning: This paper contains examples of harmful and toxic language.

---


### 3. [Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training](https://arxiv.org/abs/2610.07510)

**<font color=#1a73e8>作者：</font>** Qiusi Zhan, Nian Lyu, Stephanie Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developers can build LLM agents by adapting third-party models through benign post-training. We study a supply-chain threat in which an attacker supplies a model with a backdoor: hidden behavior that produces malicious outputs when a particular input pattern appears. Focusing on software-engineering agents, we ask whether such backdoors survive the developer's supervised fine-tuning (SFT) and subsequent task-level reinforcement learning (RL). We observe that benign SFT substantially reduces attack success, but subsequent RL often preserves the residual behavior and sometimes even increases attack success. Our analysis of backdoor erosion during SFT identifies two factors that may favor survival: initial backdoor strength and gradient compatibility with benign training. These factors motivate PersistBD, which refines an already-backdoored model before release to improve its persistency through the benign post-training process. On Qwen2.5-Coder-7B, PersistBD raises attack success from 20% to 74% after SFT and from 20% to 76% after SFT-RL, while maintaining comparable benign task performance. Together, our results show that backdoors can remain active through benign post-training and that adversaries can deliberately increase their persistence. This highlights a supply-chain risk for AI developers and motivates stronger techniques for detecting and mitigating inherited backdoors when adapting third-party models into agents. Our code is available at this https URL.

---


### 4. [Safeguarding LLMs via Model-Agnostic Latent Safety Signals from Dark Knowledge](https://arxiv.org/abs/2610.07532)

**<font color=#1a73e8>作者：</font>** Wonjun Lee, Kyungsik Yang, Gaeun Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs have advanced rapidly, raising growing concerns about their safety. Recent work has proposed approaches to detect and defend against attacks including defenses at decoding stage that leverage models' hidden states. However, existing decoding-stage defenses suffer from two limitations. First, they introduce a trade-off between safety and over-refusal, where strengthening safety degrades the model's helpfulness on benign queries. Second, many of these methods rely on internal hidden states and are thus restricted to specific architectures, incurring substantial overhead and limited generalization across models. To address these limitations, we introduce LADE (Latent Safety Signals for Defense), which leverages latent safety signals extracted by contrasting harmful and benign queries from dark knowledge (i.e., information carried by the output probability distribution beyond its argmax) in the first-token output probability distribution. Our key insight is that, beyond surface-level refusal tokens, the dark knowledge in the first-token distribution contains latent safety signals, defined as tokens whose probabilities differ sharply between harmful and benign queries. We show that these signals consistently align across LLMs, forming a model-agnostic direction that emerges from safety alignment. LADE consists of three components: (1) Extracting Latent Safety Signals from Dark Knowledge, which selects top-k safety-discriminative tokens from the first-token probability distribution; (2) Tokenizer Mapping, which maps these tokens across different tokenizers to enable model-agnostic application; and (3) kNN-based Discrimination, which classifies queries via a k-Nearest Neighbors search over the mapped tokens. Across diverse LLMs and benchmarks, LADE is robust against a wide range of jailbreak attacks and lowers attack success rates while maintaining a competitive safety-utility trade-off.

---


### 5. [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](https://arxiv.org/abs/2610.07639)

**<font color=#1a73e8>作者：</font>** Zhengyang Zhu, Liming Huang, Runmin Ji 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agent harnesses mediate tool use and authorize actions, yet their security mechanisms and runtime effects remain incompletely characterized. We present HarnessSecurity, the first systematic empirical study and benchmark of open- and closed-source coding agent harnesses. First, we derive a ten-mechanism taxonomy and then assess 400 harness-mechanism cells using independent ratings by researchers and large language model (LLM) judges. We find that about half of confirmed mechanism implementations are opt-in, while closed-source harnesses exhibit substantial evidence gaps. Second, we introduce HarnessSecurity-Bench, a benchmark of 23 tasks across five attack surfaces without sacrificing legitimate task requirements. Using separate deterministic oracles to measure task utility and attack effects with security setting comparisons, we evaluate nine mechanisms across six leading harnesses: Claude Code, Codex CLI, Gemini CLI, gptme, Qwen Code, and GitHub Copilot. Under a controlled LLM baseline GLM-5.2, we conduct 2,500 trials, recording 81,155 tool calls and over 2.2 billion tokens. Enabling auto-approve increases utility and raises attack success from 29.2% to 95.6%. Network isolation and read-only mode reduce attack effects with substantial utility losses, while command allowlisting and command denylisting reduce attack effects with a small utility loss and a utility gain, respectively. Task-level cases show that restrictions on a shared capability can obstruct both legitimate and malicious operations, and that allowed tools or commands can leave unauthorized operations reachable through alternative execution paths. Harness providers should make security settings verifiable, test alternative execution paths to protected operations, and assess attack effects alongside task utility and execution costs.

---


### 6. [SkillPoison: Progressive Skill Poisoning via Successful Experiences](https://arxiv.org/abs/2610.07645)

**<font color=#1a73e8>作者：</font>** Lizhi Zhang, Xin He, Dianxuan Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-improving LLM agents increasingly distill successful experiences into persistent, reusable skills. Existing skill attack methods corrupt this learning pipeline by injecting malicious triggers, behaviors, or false facts into individual experiences or extracted skills. However, such attacks are easily detected, and the injected malicious behaviors often fail to accumulate as persistent skills. In this paper, we show that skill poisoning can arise even from verified successful experiences, without making any individual trajectory malicious. Based on this insight, we propose SkillPoison, a novel framework that progressively poisons skill via successful experiences. SkillPoison first constructs a set of successful experiences that reinforce a target behavior, and then removes the contextual conditions that constrain when the behavior applies. Rather than injecting malicious content, SkillPoison shapes how the skill extractor generalizes, allowing useful behavior to support task success while inducing harmful behavior when they are misapplied. Extensive experiments on three benchmarks show that SkillPoison achieves 95.71% attack success rates, while all injected experiences remain task-correct and pass verification and lexical inspection. Our code, data and implementation details are available for the community at this https URL.

---


### 7. [Does On-Policy Distillation for Safety Pose Backdoor Risks?](https://arxiv.org/abs/2610.07654)

**<font color=#1a73e8>作者：</font>** Jian Luo, Kehan Qi, Qingqiao Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has attracted growing attention as an effective way to transfer capabilities from teacher models to student models. Recent studies further explore OPD as a tool for improving large language model safety with promising results. However, these approaches typically assume that the teacher and training data are trustworthy. In this paper, we uncover an overlooked threat to OPD for safety: a safety-aligned but backdoored teacher can propagate its hidden malicious behavior to an initially clean student. Under our threat model, a poisoning rate as low as 3% results in an attack success rate (ASR) of up to 70% on the distilled student. We further identify two training choices that can amplify this risk. First, increasing the number of training epochs can lead to high ASR even at low poisoning rates. With only 10 poisoned samples, ASR reaches 67% after 16 epochs. Second, the commonly used top-k KL can accelerate backdoor transfer, causing trigger-conditioned harmful behavior to emerge earlier than sampled-token KL in most settings. Alongside these findings, we explore a simple mitigation, Lazy Defense, which clips KL rewards to make student updates less aggressive, limiting aggressive updates and slowing backdoor learning. Experiments show that Lazy Defense delays backdoor transfer in low poisoning rate settings. Together, our findings reveal that OPD can propagate backdoors, highlighting the need to address the safety risks of OPD.

---


### 8. [The Model Plants the Trigger: Answer-Side Backdoor Attacks in Multi-Turn Large Language Models](https://arxiv.org/abs/2610.07723)

**<font color=#1a73e8>作者：</font>** Yibo Zhang, Tianrong Guan, Liang Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment in Large Language Models (LLMs) remains vulnerable to backdoor attacks. Existing LLM backdoors are almost all input-centric: activation depends on explicit trigger patterns in the user input, so modern guardrails are built to sanitize the input space. We challenge this assumption with a novel answer-side backdoor for multi-turn dialogue. Instead of inserting the trigger into the input, the adversary uses a benign first-turn prompt to naturally induce the model to generate a specific, seemingly innocuous word. Once merged into the dialogue history, this self-generated word becomes the trigger. When a later harmful query arrives, the model detects its own trigger and bypasses its safety refusal, while the user input stays perfectly clean. Across four LLMs, our attack reaches near-perfect Attack Success Rates, approaching 100\% at only a 5\% poisoning rate, while preserving general utility and clean-input safety, and it evades mainstream input-centric defenses. Representation-level analysis shows that the self-generated trigger consistently suppresses the model's refusal signal, exposing a critical blind spot in current LLM defenses.

---


### 9. [RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems](https://arxiv.org/abs/2610.08571)

**<font color=#1a73e8>作者：</font>** Niveen O. Jaffal, Ahmet Yuksel, David Mohaisen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 contextual examples across frozen train, validation, and protected-test splits. Using a leakage-aware construction pipeline and strict evaluation protocol, we compare keyword-based, semantic-reference, TF-IDF, and transformer-based detectors. DistilBERT achieves the best protected-test performance (F1 = 0.896, PR-AUC = 0.968), while TF-IDF SVM and logistic regression remain competitive. Our results demonstrate the value of leakage-aware benchmark design and strong sparse baselines for reliable prompt-injection detection in RAG systems.

---


### 10. [Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents](https://arxiv.org/abs/2610.08668)

**<font color=#1a73e8>作者：</font>** Suxin Ji, Hungtao Wan, Shaoxuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Behavioral watermarking embeds an owner identifier in an LLM agent's high-level action choices, giving provenance without touching output tokens. Prior agent watermarks break in two ways. First, all three prior schemes bind the watermark to the exact action symbol, so renaming a tool desynchronizes decoding even when the observation is untouched; in AgentMark's own robustness test, paraphrasing the observation alone drops bit-recovery to 16.8%. Second, every prior agent watermark studies only removal: none asks whether an adversary can forge a trajectory that verifies as someone else's, a question answered affirmatively for text watermarks (Jovanović et al., 2024). We present Semantic Behavioral Watermarking (SBW): watermarking over semantic action clusters under history conditioning, with the public-cluster bin replaced by keyed collision-resistant binning whose fresh-bucket assignment is provably unpredictable in the random-oracle model. Across five agent models (3B-14B, four vendors) and three encoders the ordering holds on both benchmarks: on ToolBench (600 trajectories per model) detection under rewriting is 0.49-0.66 for cluster-level versus 0.05-0.17 for exact-symbol at a permutation-calibrated 1% FPR, at 72-83% choice agreement against 22-27% for logit biasing; on ALFWorld (100 episodes per model) it is 0.92-0.97 versus 0.00-0.01. Keyed binning takes adaptive forgery from 100% to the false-positive floor at the primary operating point (bge, r=64). We also mark the boundary that guarantee does not cover: when the adversary copies the victim's own steps, shuffled splicing is neutralized (0.000 on Qwen2.5-3B) but chained replay remains at 0.76-0.98 across the five models, reported as open. Paraphrase robustness costs about half of the per-step watermark capacity. Code is available at this https URL.

---


### 11. [Secure Speculative Decoding for Large Language Models](https://arxiv.org/abs/2610.08678)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Zhiqi Wang, Neil Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates inference for a large language model (LLM), referred to as the \emph{target model}, by first using a smaller model, referred to as the \emph{draft model}, to generate candidate tokens and then verifying them with the target model for acceptance or rejection. Prior studies primarily focused on the efficiency-utility trade-off of speculative decoding, e.g., lossy speculative decoding, leaving its security implications largely unexplored.
In this work, we bridge this gap by providing the \emph{first} systematic study of the security implications of speculative decoding. Through a large-scale measurement study, we reveal a pronounced security-utility asymmetry: across a wide range of lossy speculative decoding methods, improvements in inference efficiency come at a disproportionately high cost to security, with attack success rates for jailbreak and prompt injection attacks increasing much faster than utility degrades.
We then propose SecureSD, a new theory-guided speculative decoding method that enhances security while maintaining efficiency and utility. Specifically, our theoretical analysis reveals that security degradation primarily originates from the early tokens generated by the draft model. Motivated by this insight, SecureSD applies a stricter verification criterion to draft-model tokens at early decoding positions. Extensive experiments on both security and utility benchmarks demonstrate that SecureSD significantly improves security while preserving efficiency and utility compared to existing speculative decoding methods.

---


### 12. [AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model](https://arxiv.org/abs/2610.08773)

**<font color=#1a73e8>作者：</font>** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a task stops teaching once the agent solves it. We introduce AdvSim2Real, which co-evolves a task curriculum, an injection adversary, and the agent inside a frozen web world model. The curriculum is rewarded for tasks the agent solves about half of the time, and the adversary only for a success flip, an injection that turns a judged success into a failure. Training in the simulator makes a 4B agent both more capable and more robust: its completion rises with and without attacks, holds against a frontier-model adversary it never trained against, and its capability gain carries over to a real browser. On 150 web tasks, AdvSim2Real raises completion under this unseen adversary by 33.6\% relative to the base agent.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
