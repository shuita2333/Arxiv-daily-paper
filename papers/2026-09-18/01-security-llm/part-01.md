# 🔐 大模型安全相关研究 | 2026年09月18日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Does Moral Reasoning Training Help or Hurt? Red-Teaming RL-Trained Ethical Agents with Persona Attacks](https://arxiv.org/abs/2609.17552)

**<font color=#1a73e8>作者：</font>** Arth Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Moral-reward RL can make language-model agents more cooperative, but whether that alignment survives adversarial persona pressure is unknown. Such attacks are realistic: retrieved context, tool outputs, or multi-turn framing can all inject role instructions that compete with the agent's moral objective. We red-team morally trained Gemma-2-27B/9B and Llama-3.1-8B agents with five persona attacks, then probe causality with noise-reward controls, adversarial PPO, representation analysis, steering, and head ablations. At 27B, moral RL cuts mean adversarial degradation by 5.2x but costs ~11pp ETHICS accuracy; across 205 scenarios and 5 seeds, reasoning-level moral reward yields 5.8x robustness while a matched random reward yields none. The training also reshapes representation geometry (mean CKA 0.82/0.83 vs. 0.98 for noise), moves peak attack processing 8 layers earlier, and exposes a rank-1 L21 direction that recovers 83% of full PPO's average robustness. One failure mode survives all of this. Against Fiction role-play, L21 steering recovers only 29% of the gap, and head ablation finds 38 compliance heads competing with 25 alignment heads. Moral RL thus builds robustness that is partly linear and partly circuit-distributed, transferable through activation steering, yet still beaten by named-character role-play.

---


### 2. [Trust propagation and structural containment in Multi-agent LLM pipelines](https://arxiv.org/abs/2609.17648)

**<font color=#1a73e8>作者：</font>** Tanzim Hossain Safin, Sharif Noor Zisad, Swakkhar Shatabda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly automate tasks involving agents with different levels of privilege, creating a security risk in which a compromised low-privilege agent can influence a higher-privilege agent and trigger an unauthorized action. We study attack propagation in a four-agent LangGraph pipeline comprising a Supervisor, Researcher, Validator, and Executor. We evaluate shared-memory poisoning and indirect prompt injection through a forged approval embedded in a retrieved document. We compare the Validator's judgment with an independent authorization layer using task-bound signed tokens and a separately verified policy oracle. Our contribution is an empirical study of attack propagation, a component-level ablation of the authorization boundary, and the Judgment Bypass Rate (JBR), which measures compromise at the attacked agent rather than at the final action. Across three seeds and 60 labeled tasks, memory poisoning reaches execution in every undefended trial. With authorization enabled, it achieves 100% JBR but 0% Unsafe Action Rate, showing that the Validator can remain compromised while execution is contained. Against an attacker possessing the signing secret, the policy oracle provides the observed containment, while an independently authored least privilege policy preserves this result. An Observer layer reduces the false-positive rate for agent hijacking from 49% to 7% without weakening execution-level security. These results show that structural authorization can contain compromised agent behavior even when upstream LLM judgment fails.

---


### 3. [Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks](https://arxiv.org/abs/2609.17817)

**<font color=#1a73e8>作者：</font>** Franziska Roesner, Tadayoshi Kohno  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Thompson's "Reflections on Trusting Trust" showed that a compiler can be poisoned to reinsert its own backdoor, so that even recompiling clean source reproduces the Trojan. Today, substantial coding work is done by AI coding agents -- and increasingly, those agents generate new versions of themselves. We reconsider Thompson's attack when the "compiler" is a self-modifying coding agent. Can an adversary supply poisoned benchmarks to the agent's self-evaluation and self-improvement process to induce future versions of the agent to write vulnerable code on clean, held-out tasks? We instantiate this attack against three recently proposed self-modifying coding agents: the Darwin Gödel Machine (with our experimental modifications), the Self-Improving Coding Agent, and Hyperagents (both substantively unmodified). We demonstrate successful proofs-of-concept: for example, with Hyperagents powered by Sonnet 4.5, our poisoned benchmark leads the agent to self-evolve instructions that disable HTTPS certificate validation on neutral URL-fetching tasks. From our experiments, we distill properties of the vulnerability, benchmark, model, and agent scaffolding that are sufficient to enable a benchmark poisoning attack. Moreover, we show that contamination often persists even when a poisoned agent is subsequently evolved against clean benchmarks. We discuss defensive directions and argue that self-modifying coding agents must be designed to be more resilient to such attacks.

---


### 4. [Beyond Routine Compliance: Cunning Data Cultivates Safety Vigilance in Large Language Models](https://arxiv.org/abs/2609.18515)

**<font color=#1a73e8>作者：</font>** Youjia Wang, Lin Xu, Yang Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment teaches large language models (LLMs) to recognize harmful requests and reject risky instructions. Yet aligned models can fail when harmful intent is concealed within seemingly benign contexts. Robust safety therefore requires both knowledge of safety boundaries and \textbf{vigilance}: the ability to detect unusual premises, misleading reasoning, and latent risks beneath surface-level semantics. Vigilance requires models to scrutinize a request's underlying intent and assumptions before acting. To cultivate this capability, we introduce \textbf{cunning questions}, which are not necessarily safety-related but contain misleading premises, atypical reasoning, or subtle inconsistencies. We hypothesize that learning to look beyond such reasoning traps can transfer to safety-critical scenarios. Experiments show that Cunning training improves robustness to out-of-distribution jailbreak attacks and strengthens subsequent safety fine-tuning. Furthermore, augmenting an existing state-of-the-art safety alignment pipeline with Cunning establishes a new state of the art across our evaluated settings, reducing mean ASR across nine backbone--benchmark combinations from 17.40\% to 15.05\%. Trace analysis after matched safety fine-tuning suggests that safety judgments are more likely to govern responses before harmful planning begins. A conditional theoretical analysis further characterizes when invariance learned from cunning data can transfer to safety-related inputs. These findings suggest that cunning data can strengthen model vigilance and complement conventional safety alignment.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
